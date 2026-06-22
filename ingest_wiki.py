#!/usr/bin/env python3
"""
ingest_wiki.py — Ingest wiki/*.md articles into squad_memory.db as section_kind=wiki chunks.
Splits each article into H2 sections. Deduplicates on chunk_id before insert.

Usage:
  python3 ingest_wiki.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from datetime import date, datetime, timezone
from pathlib import Path

DB_PATH = Path.home() / "squad_memory" / "squad_memory.db"
WIKI_DIR = Path.home() / "squad_memory" / "wiki"

def freshness_score(published_on: str) -> float:
    if not published_on:
        return 0.0
    try:
        d = datetime.strptime(published_on, "%Y-%m-%d").date()
    except ValueError:
        return 0.0
    days_old = max((date.today() - d).days, 0)
    if days_old <= 30:   return 0.08
    if days_old <= 90:   return 0.06
    if days_old <= 180:  return 0.045
    if days_old <= 365:  return 0.03
    if days_old <= 730:  return 0.015
    return 0.0

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML-ish frontmatter and body."""
    meta: dict = {}
    if not content.startswith("---"):
        return meta, content
    end = content.find("\n---", 4)
    if end == -1:
        return meta, content
    front = content[4:end].strip()
    body = content[end + 4:].strip()
    for line in front.splitlines():
        if ": " in line:
            k, _, v = line.partition(": ")
            meta[k.strip()] = v.strip()
    return meta, body

def split_sections(body: str, article_title: str) -> list[tuple[str, str]]:
    """Split body into (heading, text) pairs on ## boundaries."""
    sections: list[tuple[str, str]] = []
    # First block before any H2 = intro section
    parts = re.split(r"^## ", body, flags=re.MULTILINE)
    intro = parts[0].strip()
    if intro:
        sections.append((article_title, intro))
    for part in parts[1:]:
        lines = part.splitlines()
        heading = lines[0].strip()
        text = "\n".join(lines[1:]).strip()
        if text:
            sections.append((heading, text))
    return sections

def make_chunk_id(wiki_path: Path, heading: str, idx: int) -> str:
    slug = wiki_path.stem
    h = hashlib.md5(f"{slug}::{heading}::{idx}".encode()).hexdigest()[:10]
    return f"wiki/{slug}::{heading[:40].lower().replace(' ', '_')}::{idx}::{h}"

def ingest(dry_run: bool = False) -> None:
    articles = sorted(WIKI_DIR.glob("*.md"))
    if not articles:
        print("No wiki articles found in", WIKI_DIR)
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    total_inserted = 0
    total_skipped = 0

    for path in articles:
        content = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(content)

        title      = meta.get("title", path.stem)
        skill      = meta.get("skill", "seo")
        priority   = meta.get("priority", "p1")
        confidence = meta.get("confidence", "0.85")
        updated    = meta.get("last_updated", "2026-04-08")
        raw_tags   = meta.get("tags", "[]")

        # Parse tags: [sro, selection_rate, ...] → list
        tags_list = [t.strip().strip("[]") for t in raw_tags.strip("[]").split(",") if t.strip()]
        tags_list = [t for t in tags_list if t]
        tags_list += ["wiki", "p1", f"wiki_{path.stem.replace('-', '_')}"]
        tags_json  = json.dumps(sorted(set(tags_list)))

        freshness  = freshness_score(updated)
        sections   = split_sections(body, title)

        print(f"\n{path.name}  ({len(sections)} sections)")

        for idx, (heading, text) in enumerate(sections):
            chunk_id = make_chunk_id(path, heading, idx)

            # Check duplicate
            cur.execute("SELECT 1 FROM chunks WHERE chunk_id = ?", (chunk_id,))
            if cur.fetchone():
                print(f"  [SKIP] {chunk_id[:60]}")
                total_skipped += 1
                continue

            if dry_run:
                print(f"  [DRY]  {chunk_id[:60]} | {len(text.split())}w")
                total_inserted += 1
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
                    chunk_id,
                    str(path),                          # path
                    skill,                              # skill
                    "wiki",                             # file_type
                    heading,                            # heading
                    text,                               # text
                    "wiki",                             # section_kind
                    "wiki_builder",                     # source
                    updated,                            # published_on
                    freshness,                          # freshness
                    json.dumps([path.stem]),            # topics_json
                    json.dumps(["research", "strategy"]), # intents_json
                    json.dumps(["seo", "research", "diagnostics"]),  # use_for_json
                    json.dumps([]),                     # avoid_for_json
                    confidence,                         # confidence
                    tags_json,                          # tags_json
                    json.dumps(["coral", "pinchy", "dejan", "seo-elite"]),  # roles_json
                    json.dumps([priority]),             # bundles_json
                    1,                                  # is_canonical
                    path.stem,                          # canonical_group
                ),
            )
            print(f"  [INS]  {chunk_id[:60]} | {len(text.split())}w")
            total_inserted += 1

    if not dry_run:
        conn.commit()

        # Rebuild FTS index
        print("\nRebuilding FTS index...")
        cur.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
        conn.commit()

    conn.close()
    print(f"\n{'DRY RUN — ' if dry_run else ''}Done: {total_inserted} inserted, {total_skipped} skipped")

if __name__ == "__main__":
    import sys
    dry = "--dry" in sys.argv
    ingest(dry_run=dry)
