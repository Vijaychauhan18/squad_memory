#!/usr/bin/env python3
from __future__ import annotations

import asyncio
import argparse
import gzip
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse

import knowledge_ingest
import refresh_semrush_top30

try:
    from scrapling.fetchers import AsyncFetcher
except Exception:
    AsyncFetcher = None


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_LIVE_CONFIG = BASE / "knowledge_sources_seo_elite_live.json"
DEFAULT_ARCHIVE_CONFIG = BASE / "knowledge_sources_seo_elite_archive.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "elite-skills"
DEFAULT_BULK_DIR = DEFAULT_SKILLS_ROOT / "seo-elite" / "memory" / "archive" / "bulk"
DEFAULT_SUMMARY = DEFAULT_BULK_DIR / "bulk-backfill-monitor.md"
DEFAULT_SNAPSHOT_DIR = BASE / "ingest" / "seo_elite" / "bulk" / "raw"
DEFAULT_RUNS_DIR = BASE / "ingest" / "seo_elite" / "bulk" / "runs"
DEFAULT_DB = BASE / "seo_elite_memory.db"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deep backfill elite SEO sources into bulk source notes")
    parser.add_argument("--live-config", default=str(DEFAULT_LIVE_CONFIG))
    parser.add_argument("--archive-config", default=str(DEFAULT_ARCHIVE_CONFIG))
    parser.add_argument("--bulk-dir", default=str(DEFAULT_BULK_DIR))
    parser.add_argument("--summary-path", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--snapshot-dir", default=str(DEFAULT_SNAPSHOT_DIR))
    parser.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR))
    parser.add_argument("--items-per-note", type=int, default=180)
    parser.add_argument("--max-consecutive-failures", type=int, default=3)
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_sources(*config_paths: Path) -> Dict[str, Dict[str, Any]]:
    sources: Dict[str, Dict[str, Any]] = {}
    for path in config_paths:
        payload = json.loads(path.read_text())
        for source in payload.get("sources", []):
            sources[source["slug"]] = source
    return sources


def build_listing_pages(homepage: str, page_template: str, max_page: int, include_homepage: bool = True) -> List[str]:
    pages: List[str] = []
    if include_homepage:
        pages.append(homepage)
    for page in range(2, max_page + 1):
        pages.append(page_template.format(page=page))
    return pages


SOURCE_PLANS: Dict[str, Dict[str, Any]] = {
    "ahrefs": {"pages": build_listing_pages("https://ahrefs.com/blog/", "https://ahrefs.com/blog/page/{page}/", 70), "max_sitemap_urls": 1200, "max_sitemaps": 28},
    "dejan": {"pages": build_listing_pages("https://dejan.ai/blog/", "https://dejan.ai/blog/page/{page}/", 13), "max_sitemap_urls": 500, "max_sitemaps": 16},
    "gsqi": {"pages": build_listing_pages("https://www.gsqi.com/marketing-blog/", "https://www.gsqi.com/marketing-blog/page/{page}/", 40), "max_sitemap_urls": 1000, "max_sitemaps": 24},
    "mobilemoxie": {"pages": build_listing_pages("https://mobilemoxie.com/blog/", "https://mobilemoxie.com/blog/page/{page}/", 30), "max_sitemap_urls": 500, "max_sitemaps": 16},
    "ipullrank": {"pages": build_listing_pages("https://ipullrank.com/", "https://ipullrank.com/page/{page}/", 40), "max_sitemap_urls": 700, "max_sitemaps": 18},
    "jono": {"pages": ["https://www.jonoalderson.com/"], "max_sitemap_urls": 300, "max_sitemaps": 12},
    "patrickstox": {"pages": build_listing_pages("https://ahrefs.com/blog/author/patrick-stox/", "https://ahrefs.com/blog/author/patrick-stox/page/{page}/", 8), "max_sitemap_urls": 500, "max_sitemaps": 14},
    "search-engine-land": {"pages": build_listing_pages("https://searchengineland.com/", "https://searchengineland.com/page/{page}", 60), "max_sitemap_urls": 1200, "max_sitemaps": 28},
    "search-engine-journal": {"pages": build_listing_pages("https://www.searchenginejournal.com/", "https://www.searchenginejournal.com/page/{page}/", 60), "max_sitemap_urls": 1200, "max_sitemaps": 28},
    "hobo": {"pages": build_listing_pages("https://www.hobo-web.co.uk/", "https://www.hobo-web.co.uk/page/{page}/", 40), "max_sitemap_urls": 600, "max_sitemaps": 18},
    "moz": {"pages": ["https://moz.com/blog"], "max_sitemap_urls": 500, "max_sitemaps": 14},
    "yoast": {"pages": [], "max_sitemap_urls": 800, "max_sitemaps": 18},
    "sistrix": {"pages": build_listing_pages("https://www.sistrix.com/blog/", "https://www.sistrix.com/blog/page/{page}/", 40), "max_sitemap_urls": 700, "max_sitemaps": 18},
    "screamingfrog": {"pages": build_listing_pages("https://www.screamingfrog.co.uk/blog/", "https://www.screamingfrog.co.uk/blog/page/{page}/", 40), "max_sitemap_urls": 700, "max_sitemaps": 18},
    "searchpilot": {"pages": ["https://www.searchpilot.com/resources/blog", "https://www.searchpilot.com/resources"], "max_sitemap_urls": 600, "max_sitemaps": 16},
    "bing-webmaster": {"pages": ["https://blogs.bing.com/webmaster"] + [f"https://blogs.bing.com/webmaster?page={page}" for page in range(2, 11)], "max_sitemap_urls": 250, "max_sitemaps": 8},
    "seroundtable": {"pages": ["https://www.seroundtable.com/"]},
    "marie": {"pages": [], "max_sitemap_urls": 450, "max_sitemaps": 14},
    "lily": {"pages": ["https://lilyray.nyc/blog/"], "max_sitemap_urls": 400, "max_sitemaps": 12},
    "brodie": {"pages": [], "max_sitemap_urls": 350, "max_sitemaps": 12},
    "aleyda": {"pages": ["https://www.aleydasolis.com/en/"], "max_sitemap_urls": 450, "max_sitemaps": 14},
    "semrush": {"semrush_special": True, "max_page": 40},
    "oncrawl": {"pages": build_listing_pages("https://www.oncrawl.com/", "https://www.oncrawl.com/page/{page}/", 35), "max_sitemap_urls": 800, "max_sitemaps": 20},
    "onely": {"pages": build_listing_pages("https://www.onely.com/blog/", "https://www.onely.com/blog/page/{page}/", 30), "max_sitemap_urls": 800, "max_sitemaps": 20},
    "builtvisible": {"pages": build_listing_pages("https://builtvisible.com/blog/", "https://builtvisible.com/blog/page/{page}/", 35), "max_sitemap_urls": 700, "max_sitemaps": 18},
    "detailed": {"pages": build_listing_pages("https://detailed.com/blog/", "https://detailed.com/blog/page/{page}/", 25), "max_sitemap_urls": 500, "max_sitemaps": 14},
    "technicalseo": {"pages": ["https://technicalseo.com/insights/blog/"], "max_sitemap_urls": 300, "max_sitemaps": 12},
    "zyppy": {"pages": ["https://zyppy.com/seo/"], "max_sitemap_urls": 300, "max_sitemaps": 12},
    "portent": {"pages": build_listing_pages("https://www.portent.com/blog/seo", "https://www.portent.com/blog/seo/page/{page}", 20), "max_sitemap_urls": 500, "max_sitemaps": 16},
    "backlinko": {"pages": build_listing_pages("https://backlinko.com/blog", "https://backlinko.com/blog/page/{page}/", 25), "max_sitemap_urls": 700, "max_sitemaps": 18},
}

NON_ARTICLE_SITEMAP_SEGMENTS = {
    "author",
    "authors",
    "category",
    "categories",
    "tag",
    "tags",
    "event",
    "events",
    "webinar",
    "webinars",
    "page",
}

NON_ARTICLE_SITEMAP_SUFFIXES = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".pdf",
    ".xml",
}

SITEMAP_PRIORITY_HINTS = (
    "post-sitemap",
    "article-sitemap",
    "blog-sitemap",
    "news-sitemap",
)


def normalize_netloc(value: str) -> str:
    netloc = urlparse(value).netloc.lower().strip()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


def is_same_source_domain(url: str, homepage: str) -> bool:
    host = normalize_netloc(url)
    home_host = normalize_netloc(homepage)
    if not host or not home_host:
        return True
    return host == home_host or host.endswith(f".{home_host}") or home_host.endswith(f".{host}")


def url_slug_title(url: str) -> str:
    parsed = urlparse(url)
    last = parsed.path.rstrip("/").split("/")[-1] if parsed.path else ""
    last = re.sub(r"\.[a-z0-9]+$", "", last, flags=re.IGNORECASE)
    words = re.sub(r"[-_]+", " ", last).strip()
    return words.title() if words else url


def is_probable_sitemap_article(url: str, homepage: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False
    if not is_same_source_domain(url, homepage):
        return False
    lowered_path = parsed.path.lower()
    if any(lowered_path.endswith(suffix) for suffix in NON_ARTICLE_SITEMAP_SUFFIXES):
        return False
    segments = [segment.lower() for segment in parsed.path.split("/") if segment]
    if not segments:
        return False
    if any(segment in NON_ARTICLE_SITEMAP_SEGMENTS for segment in segments):
        return False
    last = segments[-1]
    if last in {"feed", "blog", "resources", "news"} or last.isdigit():
        return False
    return True


def sitemap_priority(url: str) -> Tuple[int, str]:
    lowered = url.lower()
    for idx, hint in enumerate(SITEMAP_PRIORITY_HINTS):
        if hint in lowered:
            return idx, lowered
    return len(SITEMAP_PRIORITY_HINTS), lowered


def parse_sitemap(raw: bytes) -> Tuple[List[str], List[Dict[str, str]]]:
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    try:
        root = ET.fromstring(raw.lstrip())
    except ET.ParseError:
        root = ET.fromstring(knowledge_ingest.sanitize_xml_bytes(raw))

    nested: List[str] = []
    items: List[Dict[str, str]] = []
    tag = root.tag.lower()

    if tag.endswith("sitemapindex"):
        for node in root.iter():
            if not node.tag.lower().endswith("sitemap"):
                continue
            loc = ""
            for child in list(node):
                if child.tag.lower().endswith("loc") and child.text:
                    loc = child.text.strip()
                    break
            if loc:
                nested.append(loc)
        return nested, items

    if tag.endswith("urlset"):
        for node in root.iter():
            if not node.tag.lower().endswith("url"):
                continue
            loc = ""
            lastmod = ""
            for child in list(node):
                child_tag = child.tag.lower()
                if child_tag.endswith("loc") and child.text:
                    loc = child.text.strip()
                elif child_tag.endswith("lastmod") and child.text:
                    lastmod = child.text.strip()
            if loc:
                items.append(
                    {
                        "title": url_slug_title(loc),
                        "link": loc,
                        "published": knowledge_ingest.normalize_date(lastmod),
                        "summary": "Discovered via XML sitemap during elite bulk backfill.",
                    }
                )
        return nested, items

    raise ValueError(f"Unsupported sitemap format: {root.tag}")


def fetch_sitemap_items(
    source_cfg: Dict[str, Any],
    snapshot_dir: Path,
    fetched_at: datetime,
    max_urls: int,
    max_sitemaps: int,
) -> Tuple[List[Dict[str, str]], List[str], List[str]]:
    homepage = str(source_cfg.get("homepage", "")).strip()
    queue: List[str] = list(source_cfg.get("sitemap_urls", []))
    seen_candidates = set(queue)
    failures: List[str] = []
    fetched_sitemaps: List[str] = []
    items: List[Dict[str, str]] = []
    visited_sitemaps = set()

    try:
        for discovered in knowledge_ingest.discover_sitemap_urls(homepage):
            if discovered not in seen_candidates:
                seen_candidates.add(discovered)
                queue.append(discovered)
    except Exception as exc:
        failures.append(f"{homepage} :: sitemap_discovery :: {type(exc).__name__}: {exc}")

    queue.sort(key=sitemap_priority)

    while queue and len(visited_sitemaps) < max_sitemaps and len(items) < max_urls:
        sitemap_url = queue.pop(0)
        if sitemap_url in visited_sitemaps:
            continue
        visited_sitemaps.add(sitemap_url)
        try:
            raw = knowledge_ingest.fetch_bytes(sitemap_url, accept=knowledge_ingest.FEED_ACCEPT)
            knowledge_ingest.save_snapshot(snapshot_dir, f"{source_cfg['slug']}-sitemap", sitemap_url, raw, fetched_at)
            nested, discovered_items = parse_sitemap(raw)
            fetched_sitemaps.append(f"sitemap:{sitemap_url}")
            for nested_url in sorted(nested, key=sitemap_priority):
                if nested_url in seen_candidates:
                    continue
                if not is_same_source_domain(nested_url, homepage):
                    continue
                seen_candidates.add(nested_url)
                queue.append(nested_url)
            queue.sort(key=sitemap_priority)
            for item in discovered_items:
                if len(items) >= max_urls:
                    break
                if is_probable_sitemap_article(item["link"], homepage):
                    items.append(item)
        except Exception as exc:
            failures.append(f"{sitemap_url} :: {type(exc).__name__}: {exc}")

    return dedupe_and_sort(items), fetched_sitemaps, failures


def normalize_items(items: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    normalized: List[Dict[str, str]] = []
    for item in items:
        title = (item.get("title") or "").strip()
        link = (item.get("link") or "").strip()
        if not title or not link:
            continue
        normalized.append(
            {
                "title": title,
                "link": link,
                "published": (item.get("published") or "").strip(),
                "summary": (item.get("summary") or "").strip(),
            }
        )
    return normalized


def dedupe_and_sort(items: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    deduped: Dict[str, Dict[str, str]] = {}
    for item in items:
        link = item["link"]
        current = deduped.get(link, {})
        deduped[link] = {
            "title": current.get("title") or item.get("title") or "",
            "link": link,
            "published": max(current.get("published", ""), item.get("published", "")),
            "summary": current.get("summary") or item.get("summary") or "",
        }
    return sorted(
        deduped.values(),
        key=lambda item: (item.get("published", ""), item.get("title", "")),
        reverse=True,
    )


def fetch_generic_feed_items(source_cfg: Dict[str, Any], snapshot_dir: Path, fetched_at: datetime) -> Tuple[str, str, str, List[Dict[str, str]]]:
    last_error = "no feed"
    candidate_urls: List[str] = list(source_cfg.get("feed_urls", []))
    homepage = str(source_cfg.get("homepage", "")).strip()
    if homepage:
        try:
            for discovered in knowledge_ingest.discover_feed_urls(homepage):
                if discovered not in candidate_urls:
                    candidate_urls.append(discovered)
        except Exception as exc:
            last_error = str(exc)

    for url in candidate_urls:
        try:
            raw = knowledge_ingest.fetch_bytes(url, accept=knowledge_ingest.FEED_ACCEPT)
            snapshot_abs = knowledge_ingest.save_snapshot(snapshot_dir, source_cfg["slug"], url, raw, fetched_at)
            try:
                title, items = knowledge_ingest.parse_feed(raw)
            except Exception:
                title, items = knowledge_ingest.parse_feed_fallback(raw)
            return url, title, str(snapshot_abs), normalize_items(items)
        except Exception as exc:
            last_error = str(exc)
    return "", "", last_error, []


def fetch_generic_listing_items(source_cfg: Dict[str, Any], pages: Sequence[str], snapshot_dir: Path, fetched_at: datetime, max_consecutive_failures: int) -> Tuple[List[Dict[str, str]], List[str], List[str]]:
    items: List[Dict[str, str]] = []
    fetched_pages: List[str] = []
    failures: List[str] = []
    consecutive_failures = 0

    for page_url in pages:
        try:
            raw = knowledge_ingest.fetch_bytes(page_url, accept=knowledge_ingest.HTML_ACCEPT)
            knowledge_ingest.save_snapshot(snapshot_dir, f"{source_cfg['slug']}-bulk", page_url, raw, fetched_at)
            _title, page_items = knowledge_ingest.parse_blog_listing_html(raw, page_url, limit=40)
            items = knowledge_ingest.merge_items(items, normalize_items(page_items))
            fetched_pages.append(page_url)
            consecutive_failures = 0
        except Exception as exc:
            failures.append(f"{page_url} :: {type(exc).__name__}: {exc}")
            consecutive_failures += 1
            if consecutive_failures >= max_consecutive_failures:
                break
    return items, fetched_pages, failures


async def fetch_listing_pages_with_scrapling(source_cfg: Dict[str, Any], pages: Sequence[str], snapshot_dir: Path, fetched_at: datetime) -> Tuple[List[Dict[str, str]], List[str], List[str]]:
    if AsyncFetcher is None:
        raise RuntimeError("Scrapling AsyncFetcher unavailable")

    semaphore = asyncio.Semaphore(10)
    items: List[Dict[str, str]] = []
    fetched_pages: List[str] = []
    failures: List[str] = []

    async def fetch_one(page_url: str) -> Tuple[str, Optional[bytes], Optional[str]]:
        async with semaphore:
            try:
                response = await AsyncFetcher.get(page_url, timeout=15, retries=2)
                html_content = response.html_content
                if isinstance(html_content, bytes):
                    raw = html_content
                else:
                    raw = str(html_content).encode("utf-8", errors="replace")
                return page_url, raw, None
            except Exception as exc:
                return page_url, None, f"{type(exc).__name__}: {exc}"

    for page_url, raw, error in await asyncio.gather(*(fetch_one(page) for page in pages)):
        if error:
            failures.append(f"{page_url} :: {error}")
            continue
        assert raw is not None
        knowledge_ingest.save_snapshot(snapshot_dir, f"{source_cfg['slug']}-bulk", page_url, raw, fetched_at)
        try:
            _title, page_items = knowledge_ingest.parse_blog_listing_html(raw, page_url, limit=40)
            items = knowledge_ingest.merge_items(items, normalize_items(page_items))
            fetched_pages.append(page_url)
        except Exception as exc:
            failures.append(f"{page_url} :: {type(exc).__name__}: {exc}")

    return items, fetched_pages, failures


def fetch_semrush_bulk(source_cfg: Dict[str, Any], snapshot_dir: Path, fetched_at: datetime, max_page: int) -> Tuple[str, str, str, List[Dict[str, str]], List[str]]:
    feed_source, feed_title, snapshot_path, feed_items = refresh_semrush_top30.fetch_feed_items(source_cfg, snapshot_dir, fetched_at)
    merged = refresh_semrush_top30.dedupe_items(feed_items)
    fetched_pages: List[str] = []

    for page_number in range(1, max_page + 1):
        page_url = source_cfg["homepage"] if page_number == 1 else f"{source_cfg['homepage']}?page={page_number}"
        try:
            page_label, page_items = refresh_semrush_top30.fetch_semrush_page(page_url, source_cfg, snapshot_dir, fetched_at, page_number)
            fetched_pages.append(page_label)
            merged = refresh_semrush_top30.dedupe_items(list(merged) + page_items)
        except Exception:
            break

    return feed_source, feed_title, snapshot_path, refresh_semrush_top30.sort_items(merged), fetched_pages


def build_bulk_note(source_cfg: Dict[str, Any], items: Sequence[Dict[str, str]], feed_source: str, feed_title: str, snapshot_path: str, fetched_pages: Sequence[str], failures: Sequence[str], items_per_note: int) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    tags = knowledge_ingest.source_tags(source_cfg) + ["bulk_backfill", "deep_archive"]
    latest = knowledge_ingest.latest_published(items)
    lines = [
        "---",
        f"source: {source_cfg['homepage']}",
        f"title: Bulk Source Snapshot - {source_cfg['name']}",
        f"scraped: {today}",
        f"tags: {knowledge_ingest.yaml_list(tags)}",
        f"topic: {source_cfg.get('topic', 'seo_research')}",
        f"intent: {knowledge_ingest.yaml_list(source_cfg.get('intent', []))}",
        f"role: {knowledge_ingest.yaml_list(source_cfg.get('roles', []))}",
        f"confidence: {source_cfg.get('confidence', 'medium')}",
        "canonical: false",
        "canonical_group: Bulk source snapshots",
        "use_for: deep archive discovery, article harvesting, broad retrieval coverage",
        "avoid_for: exact recency claims without checking the note date",
        "---",
        "",
        f"# Bulk Source Snapshot - {source_cfg['name']}",
        "",
        f"Homepage: {source_cfg['homepage']}",
        f"Kind: {source_cfg.get('kind', 'publication')}",
        f"Strength: {source_cfg.get('strength', '')}",
        f"Latest published date: {latest or 'unknown'}",
        f"Discovered items: {len(items)}",
        f"Feed source: {feed_source or 'none'}",
        f"Feed title: {feed_title or source_cfg['name']}",
        f"Snapshot path: {snapshot_path}",
        f"Fetched listing pages: {len(fetched_pages)}",
    ]
    if fetched_pages:
        lines.append(f"Page strategy: {', '.join(fetched_pages[:12])}{' ...' if len(fetched_pages) > 12 else ''}")
    if failures:
        lines.append(f"Failures: {len(failures)}")
    lines.extend(["", "## Latest Items"])
    for item in items[:items_per_note]:
        lines.append(f"- {item.get('published') or 'unknown'} | [{item.get('title') or '(untitled)'}]({item.get('link') or source_cfg['homepage']})")
        summary = item.get("summary", "").strip()
        if summary:
            lines.append(f"  {summary[:280]}")
    return "\n".join(lines) + "\n"


def build_summary(results: Sequence[Dict[str, Any]]) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "---",
        "source: elite bulk backfill",
        "title: SEO Elite Bulk Backfill Monitor",
        f"scraped: {today}",
        "tags: bulk_backfill, seo_elite, monitoring, archive_growth",
        "topic: seo_research",
        "intent: monitoring, capacity_planning, article_discovery",
        "role: researcher, seo, pinchy",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Bulk source monitors",
        "use_for: bulk discovery status and source throughput",
        "avoid_for: final strategy without article notes",
        "---",
        "",
        "# SEO Elite Bulk Backfill Monitor",
        "",
        "## Sources",
    ]
    for result in results:
        if result["status"] == "ok":
            lines.append(
                f"- {result['name']}: ok | items={result['item_count']} | pages={result['page_count']} | latest={result['latest_published'] or 'unknown'} | note=`{Path(result['note_path']).name}`"
            )
        else:
            lines.append(f"- {result['name']}: error | {result.get('error', 'unknown error')}")
    return "\n".join(lines) + "\n"


def build_db(skills_root: Path, db_path: Path) -> Dict[str, Any]:
    completed = subprocess.run(
        [
            sys.executable,
            str(BASE / "squad_memory.py"),
            "build",
            "--root",
            str(skills_root),
            "--db",
            str(db_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def main() -> int:
    args = parse_args()
    live_config = Path(args.live_config)
    archive_config = Path(args.archive_config)
    bulk_dir = Path(args.bulk_dir)
    summary_path = Path(args.summary_path)
    snapshot_dir = Path(args.snapshot_dir)
    runs_dir = Path(args.runs_dir)
    skills_root = Path(args.skills_root)
    db_path = Path(args.db_path)

    bulk_dir.mkdir(parents=True, exist_ok=True)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)

    sources = load_sources(live_config, archive_config)
    fetched_at = datetime.now(timezone.utc)
    run_id = knowledge_ingest.build_run_id(fetched_at)
    results: List[Dict[str, Any]] = []

    for slug, plan in SOURCE_PLANS.items():
        source_cfg = sources.get(slug)
        if not source_cfg:
            continue

        try:
            feed_source = ""
            feed_title = ""
            snapshot_path = ""
            failures: List[str] = []
            fetched_pages: List[str] = []

            if plan.get("semrush_special"):
                feed_source, feed_title, snapshot_path, items, fetched_pages = fetch_semrush_bulk(
                    source_cfg,
                    snapshot_dir,
                    fetched_at,
                    int(plan.get("max_page", 12)),
                )
            else:
                feed_source, feed_title, snapshot_info, feed_items = fetch_generic_feed_items(source_cfg, snapshot_dir, fetched_at)
                snapshot_path = snapshot_info if feed_source else ""
                pages = plan.get("pages", [])
                if AsyncFetcher is not None and len(pages) > 3:
                    listing_items, fetched_pages, failures = asyncio.run(
                        fetch_listing_pages_with_scrapling(source_cfg, pages, snapshot_dir, fetched_at)
                    )
                else:
                    listing_items, fetched_pages, failures = fetch_generic_listing_items(
                        source_cfg,
                        pages,
                        snapshot_dir,
                        fetched_at,
                        args.max_consecutive_failures,
                    )
                sitemap_items, fetched_sitemaps, sitemap_failures = fetch_sitemap_items(
                    source_cfg,
                    snapshot_dir,
                    fetched_at,
                    int(plan.get("max_sitemap_urls", 250)),
                    int(plan.get("max_sitemaps", 10)),
                )
                fetched_pages.extend(fetched_sitemaps)
                failures.extend(sitemap_failures)
                items = dedupe_and_sort(list(feed_items) + list(listing_items) + list(sitemap_items))

            items = dedupe_and_sort(items)
            note_path = bulk_dir / f"bulk-source-{slug}.md"
            note_path.write_text(
                build_bulk_note(
                    source_cfg=source_cfg,
                    items=items,
                    feed_source=feed_source,
                    feed_title=feed_title,
                    snapshot_path=snapshot_path,
                    fetched_pages=fetched_pages,
                    failures=failures,
                    items_per_note=args.items_per_note,
                )
            )
            results.append(
                {
                    "slug": slug,
                    "name": source_cfg["name"],
                    "status": "ok",
                    "item_count": min(len(items), args.items_per_note),
                    "page_count": len(fetched_pages),
                    "latest_published": knowledge_ingest.latest_published(items),
                    "note_path": str(note_path),
                }
            )
            print(
                f"- {source_cfg['name']}: ok items={min(len(items), args.items_per_note)} pages={len(fetched_pages)} "
                f"latest={knowledge_ingest.latest_published(items) or 'unknown'} note={note_path.name}",
                flush=True,
            )
        except Exception as exc:
            results.append({"slug": slug, "name": source_cfg["name"], "status": "error", "error": f"{type(exc).__name__}: {exc}"})
            print(f"- {source_cfg['name']}: error {type(exc).__name__}: {exc}", flush=True)

    summary_path.write_text(build_summary(results))
    manifest = {
        "run_id": run_id,
        "generated_at": fetched_at.isoformat(),
        "results": results,
        "summary_path": str(summary_path),
        "bulk_dir": str(bulk_dir),
    }
    manifest_path = runs_dir / f"bulk-backfill-{run_id}.json"
    knowledge_ingest.write_json(manifest_path, manifest)
    knowledge_ingest.write_json(runs_dir / "latest.json", manifest)

    if args.build_db:
        build = build_db(skills_root, db_path)
        manifest["build"] = build
        if build["returncode"] != 0:
            raise SystemExit(build["returncode"])

    if args.json:
        print(json.dumps(manifest, indent=2, ensure_ascii=True))
    else:
        print(f"Run ID: {run_id}")
        print(f"Summary note: {summary_path}")
        for result in results:
            if result["status"] == "ok":
                print(
                    f"- {result['name']}: ok items={result['item_count']} pages={result['page_count']} "
                    f"latest={result['latest_published'] or 'unknown'} note={Path(result['note_path']).name}"
                )
            else:
                print(f"- {result['name']}: error {result['error']}")
        if args.build_db and manifest.get("build"):
            build = manifest["build"]
            if build["stdout"]:
                print(build["stdout"])
            if build["stderr"]:
                print(build["stderr"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
