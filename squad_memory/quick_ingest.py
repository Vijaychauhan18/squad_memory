#!/usr/bin/env python3
"""
quick_ingest.py — One-command ingest for URLs, files, or raw text into squad_memory.db

Usage:
  python3 quick_ingest.py https://patents.google.com/patent/US11816114B1/en
  python3 quick_ingest.py ~/Downloads/article.md
  python3 quick_ingest.py --text "paste raw text here" --title "My Note" --tags "patent,navboost"
  python3 quick_ingest.py https://dejan.ai/blog/sro --skill dejan-ai-reverse-engineering --tags "sro,grounding"

Options:
  --skill     skill name (default: seo)
  --tags      comma-separated tags (default: auto-detected)
  --title     override title (default: from page <title> or filename)
  --dry       dry run — show what would be inserted, don't write
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

DB_PATH = Path.home() / "squad_memory" / "squad_memory.db"
RAW_DIR = Path.home() / "squad_memory" / "raw"
RAW_DIR.mkdir(exist_ok=True)

# Skill memory directory — files saved here survive pipeline rebuilds
SKILL_MEMORY_DIR = Path.home() / ".codex" / "skills" / "seo" / "memory"
SKILL_MEMORY_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Auto-tag rules: if URL/title contains key → add tags
AUTO_TAG_RULES = [
    (["patent", "patents.google"], ["patent", "patent_research"]),
    (["navboost", "nav-boost"], ["navboost", "ranking_signals"]),
    (["dejan.ai", "dejan"], ["dejan", "ai_reverse_engineering", "sro"]),
    (["grounding", "ground"], ["grounding", "grounding_snippets"]),
    (["ai overview", "ai-overview", "aioverviews"], ["ai_overview"]),
    (["hcu", "helpful content", "helpful-content"], ["hcu", "quality_signals"]),
    (["knowledge graph", "knowledge-graph"], ["knowledge_graph"]),
    (["passage rank", "passage-rank"], ["passage_ranking"]),
    (["fan-out", "fan out", "fanout"], ["fan_out"]),
    (["selection rate", "sro"], ["selection_rate", "sro"]),
    (["eeat", "e-e-a-t", "expertise"], ["eeat"]),
]


def freshness_score(d: date) -> float:
    days_old = max((date.today() - d).days, 0)
    if days_old <= 30:   return 0.08
    if days_old <= 90:   return 0.06
    if days_old <= 180:  return 0.045
    if days_old <= 365:  return 0.03
    if days_old <= 730:  return 0.015
    return 0.0


def fetch_url(url: str) -> tuple[str, str]:
    """Fetch URL → (title, markdown_text). Uses html2text for clean conversion."""
    import requests
    import html2text

    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    # Extract title from HTML
    title_match = re.search(r"<title[^>]*>([^<]+)</title>", resp.text, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else urlparse(url).path.split("/")[-1]

    # Strip known boilerplate sections for patents
    html_content = resp.text
    if "patents.google.com" in url:
        # Keep only the abstract + description sections
        for section_id in ["abstract", "description", "claims"]:
            match = re.search(rf'<section[^>]*id="{section_id}"[^>]*>(.*?)</section>', html_content, re.DOTALL | re.IGNORECASE)
            if match:
                html_content = match.group(1)
                break

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    h.ignore_emphasis = False
    markdown = h.handle(html_content)

    # Clean up excessive whitespace
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    return title, markdown


def read_file(path: Path) -> tuple[str, str]:
    """Read local file → (title, text)."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    # If markdown with frontmatter, extract title
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()
    return title, text


def auto_tags(url_or_title: str, extra: list[str]) -> list[str]:
    """Generate tags from URL/title content."""
    haystack = url_or_title.lower()
    tags = list(extra)
    for keywords, rule_tags in AUTO_TAG_RULES:
        if any(k in haystack for k in keywords):
            tags.extend(rule_tags)
    return sorted(set(tags))


def split_chunks(text: str, title: str, max_tokens: int = 800) -> list[tuple[str, str]]:
    """Split text into (heading, chunk) pairs by H2/H3 headings."""
    sections: list[tuple[str, str]] = []
    parts = re.split(r"^#{1,3} ", text, flags=re.MULTILINE)
    intro = parts[0].strip()
    if len(intro) > 100:
        sections.append((title, intro[:max_tokens * 4]))

    # Headings to skip (noisy patent/web boilerplate)
    SKIP_HEADINGS = {
        "links", "images", "classifications", "landscapes",
        "priority applications", "applications claiming priority",
        "related parent applications", "publications", "family applications",
        "family applications before", "country status",
        "families citing this family", "citations", "info",
    }

    for part in parts[1:]:
        lines = part.splitlines()
        heading = lines[0].strip()
        if heading.lower().rstrip("s ()0123456789") in SKIP_HEADINGS:
            continue
        if any(heading.lower().startswith(s) for s in SKIP_HEADINGS):
            continue
        body = "\n".join(lines[1:]).strip()
        if not body or len(body) < 80:
            continue
        # Trim to max_tokens (approx 4 chars/token)
        body = body[: max_tokens * 4]
        sections.append((heading, body))

    return sections if sections else [(title, text[: max_tokens * 4])]


def make_chunk_id(source: str, heading: str, idx: int) -> str:
    slug = re.sub(r"[^a-z0-9]", "_", source.lower())[:40]
    h = hashlib.md5(f"{slug}::{heading}::{idx}".encode()).hexdigest()[:10]
    return f"quick_ingest/{slug}::{idx}::{h}"


def ingest_chunks(
    chunks: list[tuple[str, str]],
    source: str,
    skill: str,
    tags: list[str],
    title: str,
    dry_run: bool = False,
) -> int:
    today = date.today().isoformat()
    fresh = freshness_score(date.today())
    tags_json = json.dumps(tags)
    topics_json = json.dumps([skill, "quick_ingest"])

    if dry_run:
        print(f"\n[DRY RUN] Would insert {len(chunks)} chunks:")
        for i, (h, t) in enumerate(chunks):
            print(f"  [{i}] {h[:60]} — {len(t.split())}w")
        return len(chunks)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = skipped = 0

    for idx, (heading, text) in enumerate(chunks):
        chunk_id = make_chunk_id(source, heading, idx)
        cur.execute("SELECT 1 FROM chunks WHERE chunk_id = ?", (chunk_id,))
        if cur.fetchone():
            skipped += 1
            continue

        cur.execute(
            """
            INSERT INTO chunks (
                chunk_id, path, skill, file_type, heading, text,
                section_kind, source, published_on, freshness,
                topics_json, intents_json, use_for_json, avoid_for_json,
                confidence, tags_json, roles_json, bundles_json,
                is_canonical, canonical_group
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                chunk_id, source, skill, "quick_ingest",
                heading, text, "section", "quick_ingest",
                today, fresh,
                topics_json, json.dumps(["research"]),
                json.dumps(["seo", "research"]), json.dumps([]),
                "0.75", tags_json,
                json.dumps(["coral", "pinchy", "kelp"]),
                json.dumps(["p1"]),
                0, re.sub(r"[^a-z0-9]", "_", title.lower())[:50],
            ),
        )
        print(f"  [INS] {heading[:60]} — {len(text.split())}w")
        inserted += 1

    conn.commit()
    # Rebuild FTS
    cur.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
    conn.commit()
    conn.close()
    return inserted


def main():
    parser = argparse.ArgumentParser(description="Quick ingest URL or file into squad_memory.db")
    parser.add_argument("source", nargs="?", help="URL or file path")
    parser.add_argument("--text", help="Raw text to ingest directly")
    parser.add_argument("--title", default="", help="Override title")
    parser.add_argument("--skill", default="seo", help="Skill tag (default: seo)")
    parser.add_argument("--tags", default="", help="Comma-separated extra tags")
    parser.add_argument("--dry", action="store_true", help="Dry run — don't write to DB")
    args = parser.parse_args()

    extra_tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    # --- Get content ---
    if args.text:
        title = args.title or "Quick Note"
        text = args.text
        source = f"quick_note::{title}"
    elif args.source:
        src = args.source.strip()
        if src.startswith("http"):
            print(f"Fetching: {src}")
            try:
                title, text = fetch_url(src)
            except Exception as e:
                print(f"Fetch failed: {e}")
                sys.exit(1)
            source = src
            if args.title:
                title = args.title
        else:
            path = Path(src).expanduser()
            if not path.exists():
                print(f"File not found: {path}")
                sys.exit(1)
            print(f"Reading: {path}")
            title, text = read_file(path)
            source = str(path)
            if args.title:
                title = args.title
    else:
        # Read from stdin
        print("Reading from stdin... (paste content, then Ctrl+D)")
        text = sys.stdin.read().strip()
        title = args.title or "Stdin Note"
        source = "stdin"

    # --- Auto-tag ---
    tags = auto_tags(f"{source} {title}", extra_tags)
    tags.append("quick_ingest")

    # --- Split into chunks (for preview only — actual ingest via build) ---
    chunks = split_chunks(text, title)
    print(f"\nTitle:  {title}")
    print(f"Skill:  {args.skill}")
    print(f"Tags:   {tags}")
    print(f"Chunks: {len(chunks)} (preview — actual chunking done by squad_memory.py build)")

    # Save as skill memory file — survives pipeline rebuilds
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
    memory_file = SKILL_MEMORY_DIR / f"qi-{slug}.md"

    if not args.dry:
        # Build memory note in the format squad_memory.py build expects
        tag_str = ", ".join(tags)
        memory_content = f"""---
source: {source}
title: {title}
scraped: {date.today().isoformat()}
tags: {tag_str}
topic: quick_ingest
intent: research
role: pinchy, coral, kelp
confidence: medium
canonical: false
use_for: {args.skill}, research
avoid_for: code_implementation
---

# {title}

Source: {source}

{text}
"""
        memory_file.write_text(memory_content, encoding="utf-8")
        print(f"Saved to skill memory: {memory_file.name}")

        # Also save raw copy
        raw_file = RAW_DIR / f"{slug}.md"
        raw_file.write_text(f"# {title}\nSource: {source}\n\n{text}", encoding="utf-8")
        print(f"Raw saved: {raw_file.name}")

        # Rebuild DB so it's queryable immediately
        print("Rebuilding DB...")
        import subprocess
        result = subprocess.run(
            ["python3", str(Path.home() / "squad_memory" / "squad_memory.py"), "build"],
            capture_output=True, text=True, cwd=str(Path.home() / "squad_memory")
        )
        if result.returncode == 0:
            print("DB rebuilt — content live immediately")
        else:
            print(f"DB rebuild warning: {result.stderr[-200:] if result.stderr else 'check manually'}")
    else:
        print(f"\n[DRY] Would save to: {memory_file.name}")
        print(f"[DRY] Would rebuild DB from skill files")

    n = len(chunks)
    print(f"\n{'DRY — ' if args.dry else ''}Done: {n} chunks {'would be ' if args.dry else ''}ingested and will survive pipeline rebuilds")


if __name__ == "__main__":
    main()
