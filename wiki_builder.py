#!/usr/bin/env python3
"""
wiki_builder.py — P1 Wiki Synthesis Builder
Pulls chunks from squad_memory.db by topic, synthesizes wiki articles via Claude API.
Run manually or add as a cron phase.

Usage:
  python3 wiki_builder.py build          # synthesize all P1 articles
  python3 wiki_builder.py health         # check articles for staleness/gaps
  python3 wiki_builder.py list           # list articles + metadata
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path.home() / "squad_memory" / "squad_memory.db"
WIKI_DIR = Path.home() / "squad_memory" / "wiki"
WIKI_DIR.mkdir(exist_ok=True)

# P1 topic definitions — tag filters to pull chunks per article
P1_TOPICS = [
    {
        "slug": "sro-selection-rate-optimization",
        "title": "SRO — Selection Rate Optimization",
        "skill": "dejan-ai-reverse-engineering",
        "tag_filter": "selection_rate",
        "priority": "p1",
    },
    {
        "slug": "query-fan-out-mechanics",
        "title": "Query Fan-Out Mechanics",
        "skill": "dejan-ai-reverse-engineering",
        "tag_filter": "fan_out",
        "priority": "p1",
    },
    {
        "slug": "grounding-chunk-optimization",
        "title": "Grounding Chunk Optimization",
        "skill": "dejan-ai-reverse-engineering",
        "tag_filter": "grounding",
        "priority": "p1",
    },
    {
        "slug": "google-patents-seo-signal-map",
        "title": "Google Patents — SEO Signal Map",
        "skill": "seo",
        "tag_filter": "patent",
        "priority": "p1",
    },
    {
        "slug": "ai-overview-ranking-factors",
        "title": "AI Overview Ranking Factors — Full Playbook",
        "skill": "seo",
        "tag_filter": "ai_overview",
        "priority": "p1",
    },
]

SYNTHESIS_PROMPT = """You are Pinchy, an SEO orchestrator agent. Your task is to synthesize
a wiki article from the raw knowledge chunks below.

Article title: {title}
Topic tags: {tags}

Rules:
- Write a dense, actionable .md wiki article
- Front-load key facts — answer first, context second
- Include: What it is, Why it matters for SEO, How to apply it, Debug checklist if relevant
- End with ## Sources section listing source chunk headings
- Keep total length 600-900 words
- Use tables and bullet lists where they compress information better than prose
- Add frontmatter: title, type: wiki, priority: p1, confidence: 0.85, last_updated: {date}, tags: [{tags}]

Raw chunks:
{chunks}

Write the wiki article now:"""


def get_chunks(skill: str, tag_filter: str, limit: int = 20) -> list[dict]:
    """Pull top chunks matching skill + tag from DB."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(
        """
        SELECT heading, text, tags_json, section_kind, published_on
        FROM chunks
        WHERE skill = ?
          AND tags_json LIKE ?
          AND text != ''
          AND LENGTH(text) > 100
        ORDER BY LENGTH(text) DESC
        LIMIT ?
        """,
        (skill, f"%{tag_filter}%", limit),
    )
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def format_chunks_for_prompt(chunks: list[dict]) -> str:
    parts = []
    for i, c in enumerate(chunks, 1):
        parts.append(f"[Chunk {i}] {c['heading']}\n{c['text'][:800]}")
    return "\n\n---\n\n".join(parts)


def synthesize_article(topic: dict) -> str:
    """Call Claude API to synthesize wiki article. Falls back to placeholder if no key."""
    chunks = get_chunks(topic["skill"], topic["tag_filter"])
    if not chunks:
        return f"# {topic['title']}\n\n_No chunks found. Ingest source data first._\n"

    chunk_text = format_chunks_for_prompt(chunks)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    prompt = SYNTHESIS_PROMPT.format(
        title=topic["title"],
        tags=topic["tag_filter"],
        date=today,
        chunks=chunk_text,
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(f"  [SKIP] No ANTHROPIC_API_KEY — writing placeholder for {topic['slug']}")
        return _placeholder(topic, chunks)

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
    except Exception as e:
        print(f"  [ERROR] API call failed for {topic['slug']}: {e}")
        return _placeholder(topic, chunks)


def _placeholder(topic: dict, chunks: list[dict]) -> str:
    """Write a minimal wiki stub with raw chunk headings for manual editing."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    chunk_list = "\n".join(f"- {c['heading']}" for c in chunks[:10])
    return f"""---
title: {topic['title']}
type: wiki
skill: {topic['skill']}
priority: {topic['priority']}
confidence: 0.70
last_updated: {today}
tags: [{topic['tag_filter']}]
status: stub — needs synthesis
---

# {topic['title']}

_Stub generated from {len(chunks)} chunks. Run with ANTHROPIC_API_KEY set to auto-synthesize._

## Source chunks available
{chunk_list}
"""


def cmd_build():
    print(f"Building {len(P1_TOPICS)} P1 wiki articles...\n")
    for topic in P1_TOPICS:
        path = WIKI_DIR / f"{topic['slug']}.md"
        # Skip if manually written (check for 'type: wiki' + recent date)
        if path.exists():
            content = path.read_text()
            if "type: wiki" in content and "status: stub" not in content:
                print(f"  [SKIP] {topic['slug']}.md already exists (manually written)")
                continue
        print(f"  Synthesizing: {topic['slug']}...")
        article = synthesize_article(topic)
        path.write_text(article, encoding="utf-8")
        size = len(article.split())
        print(f"  Wrote {size} words → {path.name}")
    print("\nDone. Wiki articles at:", WIKI_DIR)


def cmd_health():
    print("Wiki health check\n" + "=" * 40)
    articles = sorted(WIKI_DIR.glob("*.md"))
    if not articles:
        print("No wiki articles found. Run: python3 wiki_builder.py build")
        return
    for path in articles:
        content = path.read_text()
        lines = content.splitlines()
        # Extract last_updated
        updated = next((l.split(": ")[1] for l in lines if l.startswith("last_updated:")), "unknown")
        confidence = next((l.split(": ")[1] for l in lines if l.startswith("confidence:")), "?")
        stub = "stub" in content
        words = len(content.split())
        gaps_line = next((l for l in lines if l.startswith("gaps:")), None)
        status = "STUB" if stub else "OK"
        print(f"  [{status}] {path.name}")
        print(f"         updated={updated} confidence={confidence} words={words}")
        if gaps_line:
            print(f"         gaps={gaps_line}")
    print()


def cmd_list():
    articles = sorted(WIKI_DIR.glob("*.md"))
    print(f"Wiki articles ({len(articles)} total):")
    for path in articles:
        content = path.read_text()
        lines = content.splitlines()
        updated = next((l.split(": ")[1] for l in lines if l.startswith("last_updated:")), "?")
        priority = next((l.split(": ")[1] for l in lines if l.startswith("priority:")), "?")
        words = len(content.split())
        print(f"  {priority.upper()}  {path.stem}  ({words}w, updated {updated})")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "build":
        cmd_build()
    elif cmd == "health":
        cmd_health()
    elif cmd == "list":
        cmd_list()
    else:
        print(f"Unknown command: {cmd}. Use: build | health | list")
        sys.exit(1)


if __name__ == "__main__":
    main()
