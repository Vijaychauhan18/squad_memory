#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.error import URLError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


HOME = Path("/Users/vijaychauhan")
DEFAULT_CONFIG = HOME / "squad_memory" / "seo_expert_sources.json"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_LOG_DIR = HOME / "squad_memory" / "logs"
DEFAULT_SUMMARY = DEFAULT_OUTPUT / "live-seo-feed-monitor.md"
USER_AGENT = "Mozilla/5.0 (compatible; CodexSEOFeedSync/1.0; +https://openai.com)"
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync curated SEO expert feeds into squad memory")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Fetch feeds and write markdown snapshots")
    run.add_argument("--config", default=str(DEFAULT_CONFIG))
    run.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    run.add_argument("--summary-path", default=str(DEFAULT_SUMMARY))
    run.add_argument("--top", type=int, default=8)
    run.add_argument("--build-db", action="store_true")
    return parser.parse_args()


def fetch_bytes(url: str, timeout: int = 25) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, text/html;q=0.8"})
    with urlopen(req, timeout=timeout) as response:
        return response.read()


def strip_html(text: str) -> str:
    text = TAG_RE.sub(" ", text)
    text = unescape(text)
    return WS_RE.sub(" ", text).strip()


def text_or_empty(node: Optional[ET.Element]) -> str:
    if node is None or node.text is None:
        return ""
    return node.text.strip()


def normalize_date(raw: str) -> str:
    if not raw:
        return ""
    raw = raw.strip()
    try:
        dt = parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).date().isoformat()
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc).date().isoformat()
        except ValueError:
            continue
    return raw


def parse_feed(xml_bytes: bytes) -> Tuple[str, List[Dict[str, str]]]:
    root = ET.fromstring(xml_bytes.lstrip())
    tag = root.tag.lower()
    items: List[Dict[str, str]] = []

    if tag.endswith("rss"):
        channel = root.find("channel")
        channel_title = text_or_empty(channel.find("title")) if channel is not None else ""
        for item in channel.findall("item") if channel is not None else []:
            title = strip_html(text_or_empty(item.find("title")))
            link = text_or_empty(item.find("link"))
            pub = normalize_date(text_or_empty(item.find("pubDate")))
            summary = strip_html(text_or_empty(item.find("description")))
            items.append({"title": title, "link": link, "published": pub, "summary": summary})
        return channel_title, items

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    if tag.endswith("feed"):
        channel_title = strip_html(text_or_empty(root.find("atom:title", ns)) or text_or_empty(root.find("title")))
        entries = root.findall("atom:entry", ns) or root.findall("entry")
        for entry in entries:
            title = strip_html(text_or_empty(entry.find("atom:title", ns)) or text_or_empty(entry.find("title")))
            link = ""
            link_node = entry.find("atom:link[@rel='alternate']", ns) or entry.find("atom:link", ns) or entry.find("link")
            if link_node is not None:
                link = link_node.attrib.get("href", "").strip() or text_or_empty(link_node)
            pub = normalize_date(
                text_or_empty(entry.find("atom:updated", ns))
                or text_or_empty(entry.find("atom:published", ns))
                or text_or_empty(entry.find("updated"))
                or text_or_empty(entry.find("published"))
            )
            summary = strip_html(
                text_or_empty(entry.find("atom:summary", ns))
                or text_or_empty(entry.find("atom:content", ns))
                or text_or_empty(entry.find("summary"))
                or text_or_empty(entry.find("content"))
            )
            items.append({"title": title, "link": link, "published": pub, "summary": summary})
        return channel_title, items

    if tag.endswith("rdf"):
        rss_ns = {"rss": "http://purl.org/rss/1.0/", "dc": "http://purl.org/dc/elements/1.1/"}
        channel = root.find("rss:channel", rss_ns)
        channel_title = strip_html(text_or_empty(channel.find("rss:title", rss_ns)) if channel is not None else "")
        for item in root.findall("rss:item", rss_ns):
            title = strip_html(text_or_empty(item.find("rss:title", rss_ns)))
            link = text_or_empty(item.find("rss:link", rss_ns))
            pub = normalize_date(text_or_empty(item.find("dc:date", rss_ns)))
            summary = strip_html(text_or_empty(item.find("rss:description", rss_ns)))
            items.append({"title": title, "link": link, "published": pub, "summary": summary})
        return channel_title, items

    raise ValueError(f"Unsupported feed format: {root.tag}")


def load_config(path: Path) -> List[Dict[str, Any]]:
    payload = json.loads(path.read_text())
    return payload["sources"]


def build_note(source_cfg: Dict[str, Any], fetched_from: str, channel_title: str, items: List[Dict[str, str]], top_n: int) -> str:
    today = datetime.now().date().isoformat()
    name = source_cfg["name"]
    strengths = source_cfg["strength"]
    topic = source_cfg["topic"]
    selected = items[:top_n]
    bullets = []
    for item in selected:
        title = item["title"] or "(untitled)"
        published = item["published"] or "undated"
        link = item["link"] or source_cfg["homepage"]
        summary = item["summary"]
        bullets.append(f"- {published} | [{title}]({link})")
        if summary:
            bullets.append(f"  {summary[:260]}")

    body = "\n".join(bullets) if bullets else "- No items extracted"
    return f"""---
source: {fetched_from}
title: Live Feed Snapshot - {name}
scraped: {today}
tags: live feed, seo expert, monitoring, {source_cfg["slug"]}
topic: live_seo_feeds
intent: monitoring, research, source_selection
role: researcher, coral, pinchy
confidence: medium
canonical: false
canonical_group: Live SEO feed snapshots
use_for: freshness, new_articles, source_monitoring
avoid_for: durable_strategy_without_supporting_notes
---

# Live Feed Snapshot - {name}

Homepage: {source_cfg["homepage"]}
Feed source: {fetched_from}
Feed title: {channel_title or name}

## What This Expert Is Best For
{strengths}

## Latest Items
{body}
"""


def build_summary(sources: List[Dict[str, Any]], results: List[Dict[str, Any]]) -> str:
    today = datetime.now().date().isoformat()
    lines = [
        "---",
        "source: curated SEO and AI search source feed sync",
        "title: Live Search Source Feed Monitor",
        f"scraped: {today}",
        "tags: live feed, seo experts, monitoring, freshness",
        "topic: live_seo_feed_monitor",
        "intent: monitoring, routing, research",
        "role: researcher, coral, pinchy",
        "confidence: medium",
        "canonical: true",
        "canonical_group: Live search source feed monitor",
        "use_for: freshness, source_monitoring, routing",
        "avoid_for: final_strategy_without_durable_notes",
        "---",
        "",
        "# Live Search Source Feed Monitor",
        "",
        "Generated by the automated curated-source sync job. Use this note for freshness, then load the durable official, publication, and practitioner notes for interpretation.",
        "",
        "## Source Status",
    ]

    by_slug = {item["slug"]: item for item in sources}
    for result in results:
        source_cfg = by_slug[result["slug"]]
        status = result["status"]
        if status == "ok":
            lines.append(f"- {source_cfg['name']}: ok via {result['fetched_from']} ({result['item_count']} items)")
        else:
            lines.append(f"- {source_cfg['name']}: failed ({result['error']})")

    lines.append("")
    lines.append("## Durable Notes To Pair With Freshness")
    lines.extend([
        "- `seo-source-canon-2026.md`",
        "- `google-search-central-ai-features-2026.md`",
        "- `industry-ai-search-monitoring-2026.md`",
        "- `seo-expert-canon-2026.md`",
        "- `practitioner-ai-search-watchlist-2026.md`",
        "- `dejan-ai-reverse-engineering-pack.md`",
        "- `ahrefs-ai-visibility-guide.md`",
        "- `patrick-stox-ai-search-data-2026.md`",
        "- `glenn-gabe-ai-search-quality-2026.md`",
        "- `marie-haynes-ai-mode-and-quality-2026.md`",
        "- `lily-ray-ai-quality-rag-2026.md`",
        "- `cindy-krum-serp-observation-2026.md`",
        "- `brodie-clark-ai-mode-and-serp-reporting-2026.md`",
        "- `mike-king-ipullrank-relevance-engineering-2026.md`",
        "- `aleyda-solis-ai-search-and-international-2026.md`",
        "- `jono-alderson-technical-architecture-2026.md`",
    ])
    lines.append("")
    lines.append("## Latest Snapshot Files")
    for source_cfg in sources:
        lines.append(f"- `live-seo-feed-{source_cfg['slug']}.md`")
    lines.append("")
    return "\n".join(lines) + "\n"


def run_sync(config_path: Path, output_dir: Path, summary_path: Path, top_n: int, build_db: bool) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    DEFAULT_LOG_DIR.mkdir(parents=True, exist_ok=True)
    sources = load_config(config_path)
    results: List[Dict[str, Any]] = []

    for source_cfg in sources:
        last_error = "no feed URLs configured"
        items: List[Dict[str, str]] = []
        channel_title = ""
        fetched_from = ""
        for url in source_cfg.get("feed_urls", []):
            try:
                raw = fetch_bytes(url)
                channel_title, items = parse_feed(raw)
                fetched_from = url
                break
            except Exception as exc:
                last_error = str(exc)
        if fetched_from:
            note_path = output_dir / f"live-seo-feed-{source_cfg['slug']}.md"
            note_path.write_text(build_note(source_cfg, fetched_from, channel_title, items, top_n))
            results.append({"slug": source_cfg["slug"], "status": "ok", "fetched_from": fetched_from, "item_count": len(items)})
        else:
            results.append({"slug": source_cfg["slug"], "status": "error", "error": last_error})

    summary_path.write_text(build_summary(sources, results))
    state_path = DEFAULT_LOG_DIR / "seo_expert_feed_sync.json"
    state_path.write_text(json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "results": results}, indent=2))

    if build_db:
        subprocess.run([sys.executable, str(HOME / "squad_memory" / "squad_memory.py"), "build"], check=False)
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "run":
        return run_sync(Path(args.config), Path(args.output_dir), Path(args.summary_path), args.top, args.build_db)
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
