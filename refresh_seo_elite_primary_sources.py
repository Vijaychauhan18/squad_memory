#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_CONFIG = BASE / "seo_elite_primary_sources.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "elite-skills"
DEFAULT_MEMORY_DIR = DEFAULT_SKILLS_ROOT / "seo-elite" / "memory"
DEFAULT_PRIMARY_DIR = DEFAULT_MEMORY_DIR / "primary"
DEFAULT_DB = BASE / "seo_elite_memory.db"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
HTML_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,text/xml;q=0.8,*/*;q=0.7"
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b.*?>.*?</\1>", re.IGNORECASE | re.DOTALL)
TITLE_RE = re.compile(r"<title\b[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
H1_RE = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
P_RE = re.compile(r"<p\b[^>]*>(.*?)</p>", re.IGNORECASE | re.DOTALL)
BODY_RE = re.compile(r"<body\b.*?>(.*?)</body>", re.IGNORECASE | re.DOTALL)
UPDATED_RE = re.compile(r"Last updated\s+([A-Za-z0-9,\-\s]+UTC)", re.IGNORECASE)
ABSTRACT_SECTION_RE = re.compile(r"<section\b[^>]*itemprop=[\"']abstract[\"'][^>]*>(.*?)</section>", re.IGNORECASE | re.DOTALL)
ABSTRACT_DIV_RE = re.compile(r"<div\b[^>]*class=[\"'][^\"']*\babstract\b[^\"']*[\"'][^>]*>(.*?)</div>", re.IGNORECASE | re.DOTALL)
DESCRIPTION_PARA_RE = re.compile(r"<div\b[^>]*class=[\"'][^\"']*\bdescription-paragraph\b[^\"']*[\"'][^>]*>(.*?)</div>", re.IGNORECASE | re.DOTALL)
CLAIM_TEXT_RE = re.compile(r"<div\b[^>]*class=[\"'][^\"']*\bclaim-text\b[^\"']*[\"'][^>]*>(.*?)</div>", re.IGNORECASE | re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh elite SEO primary sources into durable notes")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--primary-dir", default=str(DEFAULT_PRIMARY_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def strip_html(text: str) -> str:
    return WS_RE.sub(" ", TAG_RE.sub(" ", unescape(text))).strip()


def fetch_html(url: str, timeout: int = 30) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": HTML_ACCEPT,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def normalize_paragraphs(blocks: Iterable[str], *, min_len: int = 90, limit: int = 18) -> List[str]:
    paragraphs: List[str] = []
    seen = set()
    for block in blocks:
        text = strip_html(block)
        if len(text) < min_len:
            continue
        if text in seen:
            continue
        seen.add(text)
        paragraphs.append(text)
        if len(paragraphs) >= limit:
            break
    return paragraphs


def extract_patent_text(html: str) -> List[str]:
    patent_blocks: List[str] = []

    abstract_section = ABSTRACT_SECTION_RE.search(html)
    if abstract_section:
        patent_blocks.extend(ABSTRACT_DIV_RE.findall(abstract_section.group(1)))
    if not patent_blocks:
        patent_blocks.extend(ABSTRACT_DIV_RE.findall(html))

    patent_blocks.extend(DESCRIPTION_PARA_RE.findall(html)[:8])
    claim_blocks = CLAIM_TEXT_RE.findall(html)
    if claim_blocks:
        patent_blocks.extend(claim_blocks[:3])

    return normalize_paragraphs(patent_blocks, min_len=70, limit=12)


def extract_page_text(html: str, *, kind: str = "reference") -> Tuple[str, List[str], str]:
    html = COMMENT_RE.sub(" ", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    title_match = H1_RE.search(html) or TITLE_RE.search(html)
    title = strip_html(title_match.group(1)) if title_match else ""
    if kind == "patent":
        paragraphs = extract_patent_text(html)
    else:
        body_match = BODY_RE.search(html)
        block = body_match.group(1) if body_match else html
        paragraphs = normalize_paragraphs(P_RE.findall(block), min_len=90, limit=18)
    updated_match = UPDATED_RE.search(html)
    updated = updated_match.group(1).strip() if updated_match else ""
    return title, paragraphs, updated


def render_note(item: Dict[str, object], title: str, paragraphs: Iterable[str], page_updated: str) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    source = str(item["url"])
    item_title = title or str(item["title"])
    tags = ", ".join(str(tag) for tag in item.get("tags", []))
    confidence = str(item.get("confidence", "medium"))
    kind = str(item.get("kind", "reference"))
    topic = str(item.get("topic", "seo_reference"))
    use_for = str(item.get("use_for", "primary-source reasoning"))
    lines = [
        "---",
        f"source: {source}",
        f"title: {item_title}",
        f"scraped: {today}",
        f"tags: {tags}",
        f"topic: {topic}",
        "intent: research, synthesis, source_selection, primary_source_reasoning",
        "role: researcher, seo, pinchy",
        f"confidence: {confidence}",
        "canonical: true",
        f"canonical_group: Primary source {kind}",
        f"use_for: {use_for}",
        "avoid_for: claiming any patent or doc alone proves live ranking behavior",
        "---",
        "",
        f"# {item_title}",
        "",
        f"Source type: {kind}",
        f"Original URL: {source}",
    ]
    if page_updated:
        lines.append(f"Page updated label: {page_updated}")
    lines.extend(
        [
            "",
            "## Why This Matters",
            use_for,
            "",
            "## Extracted Passages",
            *[f"- {para}" for para in paragraphs],
            "",
            "## Retrieval Use",
            "- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.",
            "- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def render_index(primary_dir: Path, grouped: Dict[str, List[Dict[str, object]]]) -> str:
    lines = [
        "# SEO Elite Primary Sources",
        "",
        "Curated official Google Search docs and Google patents for first-principles SEO reasoning.",
        "",
    ]
    for group in sorted(grouped):
        group_title = group.replace("-", " ").title()
        lines.append(f"## {group_title}")
        lines.append("")
        for item in grouped[group]:
            rel = Path(str(item["group"])) / f"{item['slug']}.md"
            lines.append(f"- [{item['title']}](./{rel.as_posix()})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    config = json.loads(Path(args.config).read_text())
    primary_dir = Path(args.primary_dir)
    primary_dir.mkdir(parents=True, exist_ok=True)

    refreshed: List[Dict[str, object]] = []
    grouped: Dict[str, List[Dict[str, object]]] = {}

    for item in config["items"]:
        group = str(item["group"])
        slug = str(item["slug"])
        target = primary_dir / group / f"{slug}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            html = fetch_html(str(item["url"]))
            title, paragraphs, page_updated = extract_page_text(html, kind=str(item.get("kind", "reference")))
            if not paragraphs:
                continue
            target.write_text(render_note(item, title, paragraphs, page_updated))
            refreshed.append({"slug": slug, "path": str(target), "url": str(item["url"])})
            grouped.setdefault(group, []).append(item)
        except (HTTPError, URLError, OSError, ValueError):
            continue

    (primary_dir / "INDEX.md").write_text(render_index(primary_dir, grouped))

    payload = {
        "refreshed": len(refreshed),
        "paths": refreshed,
        "db_path": args.db_path,
        "build_stdout": "",
    }
    if not args.skip_build:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "build",
                "--root",
                str(Path(args.skills_root)),
                "--db",
                str(Path(args.db_path)),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            raise SystemExit(completed.returncode)
        payload["build_stdout"] = completed.stdout.strip()
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(f"Refreshed primary source notes: {len(refreshed)}")
        if payload["build_stdout"]:
            print(payload["build_stdout"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
