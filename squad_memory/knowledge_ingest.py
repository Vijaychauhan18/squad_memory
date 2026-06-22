#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


HOME = Path.home()
DEFAULT_CONFIG = HOME / "squad_memory" / "knowledge_sources.json"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_SUMMARY = DEFAULT_OUTPUT / "live-knowledge-monitor.md"
DEFAULT_SNAPSHOT_DIR = HOME / "squad_memory" / "ingest" / "raw"
DEFAULT_RUNS_DIR = HOME / "squad_memory" / "ingest" / "runs"
DEFAULT_STATE_PATH = HOME / "squad_memory" / "ingest" / "state.json"
DEFAULT_BACKFILL_STATE_PATH = HOME / "squad_memory" / "ingest" / "backfill_state.json"
DEFAULT_BACKFILL_SUMMARY = HOME / "squad_memory" / "ingest" / "archive_backfill_summary.md"
DEFAULT_DB = HOME / "squad_memory" / "squad_memory.db"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
FEED_ACCEPT = "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, text/html;q=0.8"
HTML_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,text/xml;q=0.8,*/*;q=0.7"
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
INVALID_XML_BYTES_RE = re.compile(rb"[\x00-\x08\x0B\x0C\x0E-\x1F]")
BARE_AMP_RE = re.compile(rb"&(?!#?[A-Za-z0-9]+;)")
LINK_TAG_RE = re.compile(r"<link\b[^>]+>", re.IGNORECASE)
ATTR_RE = re.compile(r'([A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*([\"\'])(.*?)\2', re.DOTALL)
ITEM_BLOCK_RE = re.compile(r"<item\b.*?>.*?</item>", re.IGNORECASE | re.DOTALL)
ENTRY_BLOCK_RE = re.compile(r"<entry\b.*?>.*?</entry>", re.IGNORECASE | re.DOTALL)
TAG_BLOCK_TEMPLATE = r"<(?:[A-Za-z0-9_:-]+:)?{tag}\b[^>]*>(.*?)</(?:[A-Za-z0-9_:-]+:)?{tag}>"
REDIRECT_CODES = {301, 302, 303, 307, 308}
COMMON_FEED_PATHS = ("/feed/", "/rss.xml", "/atom.xml", "/feed.xml", "/index.xml")
COMMON_SITEMAP_PATHS = (
    "/sitemap.xml",
    "/sitemap_index.xml",
    "/post-sitemap.xml",
    "/post-sitemap1.xml",
    "/blog-sitemap.xml",
    "/article-sitemap.xml",
    "/news-sitemap.xml",
)
ROBOTS_SITEMAP_RE = re.compile(r"(?im)^sitemap:\s*(\S+)\s*$")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b.*?>.*?</\1>", re.IGNORECASE | re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
ARTICLE_BLOCK_RE = re.compile(r"<article\b.*?>.*?</article>", re.IGNORECASE | re.DOTALL)
HEADING_LINK_RE = re.compile(
    r"<h([1-4])\b[^>]*>\s*(?:<[^>]+>\s*)*<a\b[^>]*href=(['\"])(.*?)\2[^>]*>(.*?)</a>.*?</h\1>",
    re.IGNORECASE | re.DOTALL,
)
HEADING_TEXT_RE = re.compile(
    r"<h([1-4])\b[^>]*>(.*?)</h\1>",
    re.IGNORECASE | re.DOTALL,
)
ANCHOR_BLOCK_RE = re.compile(r"(<a\b[^>]*>)(.*?)</a>", re.IGNORECASE | re.DOTALL)
CARD_TITLE_RE = re.compile(
    r"<(?:div|span|h[1-4])\b[^>]*class=(['\"])[^>]*?(?:categories-title|title|text-lg-heading|post-title)[^>]*?\1[^>]*>(.*?)</(?:div|span|h[1-4])>",
    re.IGNORECASE | re.DOTALL,
)
ALT_ATTR_RE = re.compile(r"\balt=(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
DIG_DEEPER_LINK_RE = re.compile(
    r"<a\b[^>]*href=(['\"])(.*?)\1[^>]*>\s*(?:<[^>]+>\s*)*(Dig deeper|Read more|Learn more)\s*</a>",
    re.IGNORECASE | re.DOTALL,
)
PARAGRAPH_RE = re.compile(r"<p\b[^>]*>(.*?)</p>", re.IGNORECASE | re.DOTALL)
TIME_RE = re.compile(r"<time\b[^>]*datetime=(['\"])(.*?)\1[^>]*>", re.IGNORECASE | re.DOTALL)
DATE_TEXT_RE = re.compile(
    r"\b("
    r"January|February|March|April|May|June|July|August|September|October|November|December"
    r")\s+\d{1,2},\s+20\d{2}\b",
    re.IGNORECASE,
)
META_TAG_RE = re.compile(r"<meta\b[^>]*>", re.IGNORECASE)
LOC_RE = re.compile(r"<loc\b[^>]*>(.*?)</loc>", re.IGNORECASE | re.DOTALL)
JSON_LD_SCRIPT_RE = re.compile(
    r"<script\b[^>]*type=(['\"])application/ld\+json\1[^>]*>(.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)
BLOCK_ELEMENT_RE = re.compile(
    r"<(h2|h3|h4|p|ul|ol|blockquote)\b[^>]*>(.*?)</\1>",
    re.IGNORECASE | re.DOTALL,
)
LIST_ITEM_RE = re.compile(r"<li\b[^>]*>(.*?)</li>", re.IGNORECASE | re.DOTALL)
ARTICLE_SCHEMA_TYPES = {
    "article",
    "blogposting",
    "newsarticle",
    "analysisnewsarticle",
    "report",
    "techarticle",
}
FETCH_FALLBACK_CODES = {403, 429, 500, 502, 503, 504}
LOW_SIGNAL_PREFIXES = (
    "read more",
    "learn more",
    "share this",
    "subscribe",
    "sign up",
    "cookie",
    "accept ",
    "privacy policy",
    "terms of service",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 1 knowledge ingestion pipeline for squad memory")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Fetch configured feeds and write live memory snapshots")
    run.add_argument("--config", default=str(DEFAULT_CONFIG))
    run.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    run.add_argument("--summary-path", default=str(DEFAULT_SUMMARY))
    run.add_argument("--snapshot-dir", default=str(DEFAULT_SNAPSHOT_DIR))
    run.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR))
    run.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    run.add_argument("--top", type=int, default=8)
    run.add_argument("--source", action="append", dest="sources", help="Optional source slug filter")
    run.add_argument("--build-db", action="store_true")
    run.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    run.add_argument("--db-path", default=str(DEFAULT_DB))
    run.add_argument("--json", action="store_true", help="Emit the run manifest as JSON")

    backfill = sub.add_parser("backfill", help="Fetch historical article archives and write durable archive notes")
    backfill.add_argument("--config", default=str(DEFAULT_CONFIG))
    backfill.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    backfill.add_argument("--snapshot-dir", default=str(DEFAULT_SNAPSHOT_DIR))
    backfill.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR))
    backfill.add_argument("--state-path", default=str(DEFAULT_BACKFILL_STATE_PATH))
    backfill.add_argument("--summary-path", default=str(DEFAULT_BACKFILL_SUMMARY))
    backfill.add_argument("--source", action="append", dest="sources", help="Optional source slug filter")
    backfill.add_argument("--per-source-limit", type=int, default=40)
    backfill.add_argument("--max-articles", type=int, default=400)
    backfill.add_argument("--build-db", action="store_true")
    backfill.add_argument("--db-path", default=str(DEFAULT_DB))
    backfill.add_argument("--json", action="store_true", help="Emit JSON instead of text")

    report = sub.add_parser("report", help="Show the latest ingestion state")
    report.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    report.add_argument("--json", action="store_true", help="Emit JSON instead of text")

    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "item"


def strip_html(text: str) -> str:
    text = TAG_RE.sub(" ", text)
    text = unescape(text)
    return WS_RE.sub(" ", text).strip()


def clean_extracted_text(text: str) -> str:
    cleaned = strip_html(text)
    cleaned = cleaned.strip(" -:\u2022\t\r\n")
    return WS_RE.sub(" ", cleaned).strip()


def is_low_signal_text(text: str, min_length: int = 0) -> bool:
    value = clean_extracted_text(text)
    if not value:
        return True
    if min_length and len(value) < min_length:
        return True
    lowered = value.lower()
    if lowered.startswith(LOW_SIGNAL_PREFIXES):
        return True
    if len(value) < 140 and ("cookie" in lowered or "privacy" in lowered):
        return True
    return False


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


def fetch_bytes(url: str, timeout: int = 25, accept: str = FEED_ACCEPT, _seen: Optional[set[str]] = None) -> bytes:
    seen = _seen or set()
    parsed = urlparse(url)
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": accept,
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": f"{urlparse(url).scheme}://{urlparse(url).netloc}/" if urlparse(url).scheme and urlparse(url).netloc else url,
        },
    )
    try:
        with urlopen(req, timeout=timeout) as response:
            return response.read()
    except HTTPError as exc:
        if exc.code in REDIRECT_CODES:
            location = exc.headers.get("Location", "").strip()
            if location:
                next_url = urljoin(url, location)
                if next_url in seen or len(seen) >= 6:
                    raise
                seen = set(seen)
                seen.add(url)
                return fetch_bytes(next_url, timeout=timeout, accept=accept, _seen=seen)
        if exc.code in FETCH_FALLBACK_CODES and parsed.scheme in {"http", "https"}:
            return fetch_bytes_with_curl(url, timeout=timeout, accept=accept)
        raise
    except (URLError, OSError):
        if parsed.scheme in {"http", "https"}:
            return fetch_bytes_with_curl(url, timeout=timeout, accept=accept)
        raise


def fetch_bytes_with_curl(url: str, timeout: int = 25, accept: str = FEED_ACCEPT) -> bytes:
    completed = subprocess.run(
        [
            "curl",
            "-LfsS",
            "--max-time",
            str(timeout),
            "-A",
            USER_AGENT,
            "-H",
            f"Accept: {accept}",
            "-H",
            "Accept-Language: en-US,en;q=0.9",
            url,
        ],
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace").strip()
        raise OSError(stderr or f"curl failed for {url}")
    return completed.stdout


def sanitize_xml_bytes(xml_bytes: bytes) -> bytes:
    cleaned = INVALID_XML_BYTES_RE.sub(b"", xml_bytes.lstrip())
    cleaned = BARE_AMP_RE.sub(b"&amp;", cleaned)
    return cleaned


def extract_tag_content(text: str, tag: str) -> str:
    pattern = re.compile(TAG_BLOCK_TEMPLATE.format(tag=re.escape(tag)), re.IGNORECASE | re.DOTALL)
    match = pattern.search(text)
    if not match:
        return ""
    value = match.group(1)
    value = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", value, flags=re.DOTALL)
    return strip_html(value)


def extract_atom_link(text: str) -> str:
    match = re.search(r"<(?:[A-Za-z0-9_:-]+:)?link\b[^>]*href=(['\"])(.*?)\1", text, re.IGNORECASE | re.DOTALL)
    if match:
        return unescape(match.group(2).strip())
    return extract_tag_content(text, "link")


def parse_feed_fallback(xml_bytes: bytes) -> Tuple[str, List[Dict[str, str]]]:
    text = sanitize_xml_bytes(xml_bytes).decode("utf-8", errors="replace")
    items: List[Dict[str, str]] = []

    channel_title = extract_tag_content(text, "title")
    for block in ITEM_BLOCK_RE.findall(text):
        title = extract_tag_content(block, "title")
        link = extract_tag_content(block, "link")
        published = normalize_date(extract_tag_content(block, "pubDate") or extract_tag_content(block, "date"))
        summary = extract_tag_content(block, "description") or extract_tag_content(block, "encoded")
        if title or link or summary:
            items.append({"title": title, "link": link, "published": published, "summary": summary})
    if items:
        return channel_title, items

    entries = ENTRY_BLOCK_RE.findall(text)
    feed_title = channel_title or extract_tag_content(text, "title")
    for block in entries:
        title = extract_tag_content(block, "title")
        link = extract_atom_link(block)
        published = normalize_date(extract_tag_content(block, "updated") or extract_tag_content(block, "published"))
        summary = extract_tag_content(block, "summary") or extract_tag_content(block, "content")
        if title or link or summary:
            items.append({"title": title, "link": link, "published": published, "summary": summary})
    if items:
        return feed_title, items

    raise ValueError("Unable to parse feed even with fallback parser")


def parse_link_attrs(tag_html: str) -> Dict[str, str]:
    attrs: Dict[str, str] = {}
    for key, _quote, value in ATTR_RE.findall(tag_html):
        attrs[key.lower()] = unescape(value.strip())
    return attrs


def first_heading_text(html: str) -> str:
    match = re.search(r"<h1\b[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return strip_html(match.group(1))


def title_from_html(html: str) -> str:
    match = re.search(r"<title\b[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return strip_html(match.group(1))


def extract_summary_from_block(block: str) -> str:
    for para in PARAGRAPH_RE.findall(block):
        summary = clean_extracted_text(para)
        if not is_low_signal_text(summary, min_length=40):
            return summary
    return ""


def extract_published_from_block(block: str) -> str:
    time_match = TIME_RE.search(block)
    if time_match:
        return normalize_date(time_match.group(2))
    date_match = DATE_TEXT_RE.search(strip_html(block))
    if date_match:
        return normalize_date(date_match.group(0))
    return ""


def extract_json_ld_objects(html: str) -> List[Dict[str, Any]]:
    objects: List[Dict[str, Any]] = []
    for _quote, raw_payload in JSON_LD_SCRIPT_RE.findall(html):
        payload = raw_payload.strip().strip(";")
        if not payload:
            continue
        try:
            decoded = json.loads(payload)
        except json.JSONDecodeError:
            continue
        objects.extend(flatten_json_ld_nodes(decoded))
    return objects


def flatten_json_ld_nodes(payload: Any) -> List[Dict[str, Any]]:
    nodes: List[Dict[str, Any]] = []
    if isinstance(payload, list):
        for item in payload:
            nodes.extend(flatten_json_ld_nodes(item))
        return nodes
    if not isinstance(payload, dict):
        return nodes
    nodes.append(payload)
    graph = payload.get("@graph")
    if isinstance(graph, list):
        for item in graph:
            nodes.extend(flatten_json_ld_nodes(item))
    elif isinstance(graph, dict):
        nodes.extend(flatten_json_ld_nodes(graph))
    return nodes


def normalize_schema_types(value: Any) -> List[str]:
    if isinstance(value, str):
        return [value.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def first_json_ld_article_node(nodes: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    for node in nodes:
        types = {item.lower() for item in normalize_schema_types(node.get("@type"))}
        if types & ARTICLE_SCHEMA_TYPES:
            return node
    return {}


def json_ld_text(value: Any) -> str:
    if isinstance(value, str):
        return clean_extracted_text(value)
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        for key in ("name", "headline", "text", "description", "@id"):
            nested = json_ld_text(value.get(key))
            if nested:
                return nested
        return ""
    if isinstance(value, list):
        for item in value:
            nested = json_ld_text(item)
            if nested:
                return nested
    return ""


def json_ld_author_name(node: Dict[str, Any]) -> str:
    return json_ld_text(node.get("author"))


def split_plaintext_blocks(text: str, limit: int = 48) -> List[str]:
    pieces: List[str] = []
    for block in re.split(r"\n\s*\n", str(text or "").strip()):
        cleaned = clean_extracted_text(block)
        if is_low_signal_text(cleaned, min_length=40):
            continue
        pieces.append(cleaned)
        if len(pieces) >= limit:
            break
    if pieces:
        return pieces

    sentences = [clean_extracted_text(part) for part in re.split(r"(?<=[.!?])\s+", str(text or "").strip())]
    for sentence in sentences:
        if is_low_signal_text(sentence, min_length=40):
            continue
        pieces.append(sentence)
        if len(pieces) >= limit:
            break
    return pieces


def extract_article_body_blocks(html: str, limit: int = 72) -> List[str]:
    html = COMMENT_RE.sub(" ", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    blocks = ARTICLE_BLOCK_RE.findall(html) or [html]
    output: List[str] = []
    seen = set()

    def append_block(value: str) -> None:
        cleaned = value.strip()
        if not cleaned or cleaned in seen:
            return
        seen.add(cleaned)
        output.append(cleaned)

    for block in blocks:
        for match in BLOCK_ELEMENT_RE.finditer(block):
            tag = match.group(1).lower()
            inner = match.group(2)
            if tag in {"h2", "h3", "h4"}:
                heading = clean_extracted_text(inner)
                if is_low_signal_text(heading, min_length=4):
                    continue
                prefix = "### " if tag == "h2" else "#### "
                append_block(f"{prefix}{heading}")
            elif tag == "p":
                paragraph = clean_extracted_text(inner)
                if is_low_signal_text(paragraph, min_length=60):
                    continue
                append_block(paragraph)
            elif tag in {"ul", "ol"}:
                items: List[str] = []
                for index, item_html in enumerate(LIST_ITEM_RE.findall(inner), start=1):
                    item = clean_extracted_text(item_html)
                    if is_low_signal_text(item, min_length=4):
                        continue
                    marker = f"{index}. " if tag == "ol" else "- "
                    items.append(f"{marker}{item}")
                if items:
                    append_block("\n".join(items))
            elif tag == "blockquote":
                quote = clean_extracted_text(inner)
                if is_low_signal_text(quote, min_length=40):
                    continue
                append_block(f"> {quote}")
            if len(output) >= limit:
                return output
    return output


def is_probable_listing_article(link: str, title: str, page_url: str) -> bool:
    if any(char in link for char in {'"', "'", "<", ">", "\n", "\r", "\t"}):
        return False
    parsed_page = urlparse(page_url)
    parsed_link = urlparse(link)
    if parsed_page.scheme and parsed_page.netloc and parsed_link.netloc and parsed_link.netloc != parsed_page.netloc:
        return False
    if parsed_link.scheme and parsed_link.scheme not in {"http", "https"}:
        return False
    if not title or len(title) < 8:
        return False
    lowered_title = title.strip().lower()
    if lowered_title in {
        "blog",
        "resources",
        "read more",
        "learn more",
        "dig deeper",
        "all products",
        "about us",
        "careers",
        "events",
        "contact",
        "login",
        "free trial",
    }:
        return False

    path = parsed_link.path.rstrip("/")
    if not path or path == parsed_page.path.rstrip("/"):
        return False
    bad_fragments = (
        "/category/",
        "/tag/",
        "/author/",
        "/about-us/",
        "/jobs/",
        "/shop/",
        "/product/",
        "/wp-content/",
        "/wp-admin/",
        "/feed/",
        "/page/",
    )
    if any(fragment in path for fragment in bad_fragments):
        return False

    page_path = parsed_page.path.rstrip("/")
    if "/blog" in page_path and "/seo-blog" not in page_path:
        return "/blog/" in path
    if "/seo-blog" in page_path:
        if any(fragment in path for fragment in ("/product/", "/shop/", "/about-us/", "/jobs/")):
            return False
        return path.count("/") >= 1
    blogish_page = any(token in page_path for token in ("/resources",))
    if blogish_page and "/resources/" in path:
        return True
    return path.count("/") >= 1


def parse_yoast_cards(html: str, page_url: str, limit: int) -> List[Dict[str, str]]:
    items: List[Dict[str, str]] = []
    seen_links = set()
    for segment in html.split('<div class="card post">')[1:]:
        block = re.split(r'<div class="card post">|<a class="overview_link"|<div class="post-group">', segment, maxsplit=1)[0]
        link_match = re.search(
            r'<a\b[^>]*href=(["\'])(.*?)\1[^>]*>\s*<h([1-4])\b[^>]*>(.*?)</h\3>\s*</a>',
            block,
            re.IGNORECASE | re.DOTALL,
        )
        if not link_match:
            continue
        link = urljoin(page_url, unescape(link_match.group(2).strip()))
        title = strip_html(link_match.group(4))
        if not is_probable_listing_article(link, title, page_url):
            continue
        if link in seen_links:
            continue
        published = extract_published_from_block(block)
        summary = extract_summary_from_block(block)
        items.append({"title": title, "link": link, "published": published, "summary": summary})
        seen_links.add(link)
        if len(items) >= limit:
            break
    return items


def parse_blog_listing_html(html_bytes: bytes, page_url: str, limit: int = 12) -> Tuple[str, List[Dict[str, str]]]:
    html = html_bytes.decode("utf-8", errors="replace")
    html = COMMENT_RE.sub(" ", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    channel_title = first_heading_text(html) or title_from_html(html) or page_url

    if "yoast.com/seo-blog" in page_url and "card post" in html:
        yoast_items = parse_yoast_cards(html, page_url, limit)
        if yoast_items:
            return channel_title, yoast_items

    items: List[Dict[str, str]] = []
    seen_links = set()
    article_blocks = ARTICLE_BLOCK_RE.findall(html)
    blocks = article_blocks if article_blocks else [html]

    for block in blocks:
        for _level, _quote, href, anchor_html in HEADING_LINK_RE.findall(block):
            title = strip_html(anchor_html)
            link = urljoin(page_url, unescape(href.strip()))
            if not title or not link or link in seen_links:
                continue
            if link.rstrip("/") == page_url.rstrip("/"):
                continue
            if title.lower() in {"blog", "resources", "read more"}:
                continue
            published = extract_published_from_block(block)
            summary = extract_summary_from_block(block)
            items.append({"title": title, "link": link, "published": published, "summary": summary})
            seen_links.add(link)
            if len(items) >= limit:
                return channel_title, items

        # Some modern resource pages separate the heading text from the article link
        # and use a generic CTA like "Dig deeper". Pair the next CTA link with the
        # nearest preceding heading inside the same block.
        heading_matches = list(HEADING_TEXT_RE.finditer(block))
        for index, match in enumerate(heading_matches):
            title = strip_html(match.group(2))
            if not title or title.lower() in {"articles", "latest articles", "filters"}:
                continue
            segment_end = heading_matches[index + 1].start() if index + 1 < len(heading_matches) else len(block)
            segment = block[match.end() : segment_end]
            link_match = DIG_DEEPER_LINK_RE.search(segment)
            if not link_match:
                continue
            link = urljoin(page_url, unescape(link_match.group(2).strip()))
            if not link or link in seen_links:
                continue
            if link.rstrip("/") == page_url.rstrip("/"):
                continue
            published = extract_published_from_block(segment)
            summary = extract_summary_from_block(segment)
            items.append({"title": title, "link": link, "published": published, "summary": summary})
            seen_links.add(link)
            if len(items) >= limit:
                return channel_title, items

        for start_tag, inner_html in ANCHOR_BLOCK_RE.findall(block):
            attrs = parse_link_attrs(start_tag)
            href = attrs.get("href", "").strip()
            link = urljoin(page_url, unescape(href))
            title = strip_html(attrs.get("title", ""))
            if not title:
                match = CARD_TITLE_RE.search(inner_html)
                if match:
                    title = strip_html(match.group(2))
            if not title:
                title = first_heading_text(inner_html)
            if not title:
                alt_match = ALT_ATTR_RE.search(inner_html)
                if alt_match:
                    title = strip_html(alt_match.group(2))
            if not title:
                title = strip_html(inner_html)
            title = re.sub(r"\s*»\s*$", "", title).strip()
            if not is_probable_listing_article(link, title, page_url):
                continue
            if link in seen_links:
                continue
            published = extract_published_from_block(block)
            summary = extract_summary_from_block(inner_html) or extract_summary_from_block(block)
            items.append({"title": title, "link": link, "published": published, "summary": summary})
            seen_links.add(link)
            if len(items) >= limit:
                return channel_title, items

    if items:
        return channel_title, items
    raise ValueError("Unable to parse blog listing HTML")


def discover_feed_urls(page_url: str, timeout: int = 25) -> List[str]:
    raw = fetch_bytes(page_url, timeout=timeout, accept=HTML_ACCEPT)
    html = raw.decode("utf-8", errors="replace")
    discovered: List[str] = []
    seen = set()
    for tag_html in LINK_TAG_RE.findall(html):
        attrs = parse_link_attrs(tag_html)
        rel = attrs.get("rel", "").lower()
        type_ = attrs.get("type", "").lower()
        href = attrs.get("href", "")
        if not href:
            continue
        if "alternate" in rel and ("rss" in type_ or "atom" in type_ or type_ in {"application/xml", "text/xml"} or "feed" in href.lower()):
            abs_url = urljoin(page_url, href)
            if abs_url not in seen:
                seen.add(abs_url)
                discovered.append(abs_url)
    for suffix in COMMON_FEED_PATHS:
        abs_url = urljoin(page_url, suffix)
        if abs_url not in seen:
            seen.add(abs_url)
            discovered.append(abs_url)
    return discovered


def discover_sitemap_urls(page_url: str, timeout: int = 25) -> List[str]:
    parsed = urlparse(page_url)
    if not parsed.scheme or not parsed.netloc:
        return []
    site_root = f"{parsed.scheme}://{parsed.netloc}/"
    discovered: List[str] = []
    seen = set()
    robots_url = urljoin(site_root, "/robots.txt")

    try:
        raw = fetch_bytes(robots_url, timeout=timeout, accept="text/plain,*/*;q=0.1")
        text = raw.decode("utf-8", errors="replace")
        for match in ROBOTS_SITEMAP_RE.findall(text):
            abs_url = urljoin(site_root, match.strip())
            if abs_url not in seen:
                seen.add(abs_url)
                discovered.append(abs_url)
    except Exception:
        pass

    for suffix in COMMON_SITEMAP_PATHS:
        abs_url = urljoin(site_root, suffix)
        if abs_url not in seen:
            seen.add(abs_url)
            discovered.append(abs_url)
    return discovered


def domain_for_source(source_cfg: Dict[str, Any]) -> str:
    explicit = str(source_cfg.get("domain") or "").strip().lower()
    if explicit:
        return explicit
    roles = [str(item).strip().lower() for item in source_cfg.get("roles", [])]
    tags = [str(item).strip().lower() for item in source_cfg.get("tags", [])]
    joined = " ".join(roles + tags + [str(source_cfg.get("topic", "")).lower(), str(source_cfg.get("name", "")).lower()])
    if "seo" in joined or "technical_seo" in joined or "ai_visibility" in joined or "serp" in joined:
        return "seo"
    if "charles" in joined:
        return "charles"
    if "support" in joined or "anemone" in joined or "customer_service" in joined:
        return "support"
    if "developer" in joined or "chitin" in joined:
        return "developer"
    if "qa" in joined or "reef" in joined or "testing" in joined:
        return "qa"
    if "writer" in joined or "copywriting" in joined or "editorial" in joined:
        return "writer"
    if "marketing" in joined or "current" in joined or "distribution" in joined:
        return "marketing"
    return "seo"


def skill_dir_for_domain(domain: str) -> str:
    normalized = str(domain or "").strip().lower()
    if normalized == "support":
        return "support-anemone"
    return normalized or "seo"


def archive_output_dir(skills_root: Path, source_cfg: Dict[str, Any]) -> Path:
    return skills_root / skill_dir_for_domain(domain_for_source(source_cfg)) / "memory" / "archive" / str(source_cfg["slug"])


def fetch_html(url: str, timeout: int = 25) -> str:
    raw = fetch_bytes(url, timeout=timeout, accept=HTML_ACCEPT)
    return raw.decode("utf-8", errors="replace")


def extract_meta_content(html: str, *keys: str) -> str:
    wanted = {key.lower() for key in keys if key}
    for tag_html in META_TAG_RE.findall(html):
        attrs = parse_link_attrs(tag_html)
        names = {
            attrs.get("name", "").lower(),
            attrs.get("property", "").lower(),
            attrs.get("itemprop", "").lower(),
        }
        if not wanted.intersection(names):
            continue
        content = strip_html(attrs.get("content", ""))
        if content:
            return content
    return ""


def extract_article_paragraphs(html: str, limit: int = 48) -> List[str]:
    html = COMMENT_RE.sub(" ", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    blocks = ARTICLE_BLOCK_RE.findall(html) or [html]
    paragraphs: List[str] = []
    seen = set()
    for block in blocks:
        for para in PARAGRAPH_RE.findall(block):
            text = clean_extracted_text(para)
            if is_low_signal_text(text, min_length=60):
                continue
            if text in seen:
                continue
            seen.add(text)
            paragraphs.append(text)
            if len(paragraphs) >= limit:
                return paragraphs
    return paragraphs


def extract_article_document(html: str, url: str, source_cfg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    json_ld_nodes = extract_json_ld_objects(html)
    html = COMMENT_RE.sub(" ", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    article_node = first_json_ld_article_node(json_ld_nodes)
    title = (
        extract_meta_content(html, "og:title", "twitter:title")
        or json_ld_text(article_node.get("headline"))
        or json_ld_text(article_node.get("name"))
        or first_heading_text(html)
        or title_from_html(html)
    )
    title = re.sub(r"\s*[|\-–]\s*[^|–-]+$", "", title).strip()
    published = (
        normalize_date(extract_meta_content(html, "article:published_time", "og:published_time", "datePublished"))
        or normalize_date(json_ld_text(article_node.get("datePublished")))
        or extract_published_from_block(html)
    )
    summary = (
        extract_meta_content(html, "description", "og:description", "twitter:description")
        or json_ld_text(article_node.get("description"))
        or extract_summary_from_block(html)
    )
    paragraph_limit = int(source_cfg.get("paragraph_limit", 48) or 48)
    body_blocks = extract_article_body_blocks(html, limit=max(18, min(paragraph_limit * 2, 160)))
    article_body = json_ld_text(article_node.get("articleBody"))
    if len(body_blocks) < 6 and article_body:
        for block in split_plaintext_blocks(article_body, limit=max(12, min(paragraph_limit, 80))):
            if block not in body_blocks:
                body_blocks.append(block)
    paragraphs = [block for block in body_blocks if not block.startswith(("#", ">", "- ", "1. ", "2. ", "3. "))]
    if not paragraphs:
        paragraphs = extract_article_paragraphs(html, limit=max(12, min(paragraph_limit, 120)))
    if not title or len(title) < 8:
        return None
    if not paragraphs and not summary:
        return None
    if not summary and paragraphs:
        summary = paragraphs[0]
    author = (
        extract_meta_content(html, "author", "article:author")
        or json_ld_author_name(article_node)
    )
    schema_types = normalize_schema_types(article_node.get("@type"))
    headings = [clean_extracted_text(block.lstrip("#").strip()) for block in body_blocks if block.startswith("#")]
    return {
        "title": title,
        "url": url,
        "published": published,
        "summary": summary[:500],
        "paragraphs": paragraphs,
        "body_blocks": body_blocks,
        "headings": headings,
        "author": author,
        "schema_types": schema_types,
        "source_name": source_cfg["name"],
        "domain": domain_for_source(source_cfg),
    }


def parse_sitemap(raw: bytes, sitemap_url: str) -> Tuple[List[str], List[str]]:
    child_sitemaps: List[str] = []
    page_urls: List[str] = []
    try:
        root = ET.fromstring(raw.lstrip())
    except ET.ParseError:
        root = ET.fromstring(sanitize_xml_bytes(raw))
    tag = root.tag.lower()

    if tag.endswith("sitemapindex"):
        for node in root.iter():
            if node.tag.lower().endswith("loc") and node.text:
                value = urljoin(sitemap_url, node.text.strip())
                if value:
                    child_sitemaps.append(value)
        return child_sitemaps, page_urls

    if tag.endswith("urlset"):
        for node in root.iter():
            if node.tag.lower().endswith("loc") and node.text:
                value = urljoin(sitemap_url, node.text.strip())
                if value:
                    page_urls.append(value)
        return child_sitemaps, page_urls

    text = raw.decode("utf-8", errors="replace")
    for match in LOC_RE.findall(text):
        value = urljoin(sitemap_url, strip_html(match))
        if not value:
            continue
        if value.endswith(".xml") or "sitemap" in value.lower():
            child_sitemaps.append(value)
        else:
            page_urls.append(value)
    return child_sitemaps, page_urls


def collect_archive_urls(
    source_cfg: Dict[str, Any],
    timeout: int = 25,
    limit: int = 400,
    sitemap_limit: int = 20,
) -> Dict[str, Any]:
    homepage = str(source_cfg.get("homepage", "")).strip()
    sitemap_queue = [url for url in source_cfg.get("sitemap_urls", []) if url]
    if homepage:
        for discovered in discover_sitemap_urls(homepage, timeout=timeout):
            if discovered not in sitemap_queue:
                sitemap_queue.append(discovered)

    seen_sitemaps = set()
    candidate_urls: List[str] = []
    seen_urls = set()
    inspected_sitemaps: List[str] = []

    while sitemap_queue and len(inspected_sitemaps) < sitemap_limit and len(candidate_urls) < limit:
        sitemap_url = sitemap_queue.pop(0)
        if sitemap_url in seen_sitemaps:
            continue
        seen_sitemaps.add(sitemap_url)
        inspected_sitemaps.append(sitemap_url)
        try:
            raw = fetch_bytes(sitemap_url, timeout=timeout, accept="application/xml,text/xml;q=0.9,*/*;q=0.5")
            child_sitemaps, page_urls = parse_sitemap(raw, sitemap_url)
        except Exception:
            continue
        for child in child_sitemaps:
            if child not in seen_sitemaps and child not in sitemap_queue:
                sitemap_queue.append(child)
        for page_url in page_urls:
            if page_url in seen_urls:
                continue
            if homepage and not is_probable_listing_article(page_url, "Recovered archive article", homepage):
                continue
            seen_urls.add(page_url)
            candidate_urls.append(page_url)
            if len(candidate_urls) >= limit:
                break

    return {
        "sitemap_urls": inspected_sitemaps,
        "article_urls": candidate_urls,
    }


def fetch_listing_items(listing_url: str, timeout: int = 25) -> Tuple[str, List[Dict[str, str]]]:
    raw = fetch_bytes(listing_url, timeout=timeout, accept=HTML_ACCEPT)
    return parse_blog_listing_html(raw, listing_url)


def merge_items(existing: List[Dict[str, str]], new_items: List[Dict[str, str]]) -> List[Dict[str, str]]:
    merged: List[Dict[str, str]] = []
    seen = set()
    for item in existing + new_items:
        key = extract_item_id(item)
        if not key or key in seen:
            continue
        seen.add(key)
        merged.append(item)
    return merged


def fetch_source_feed(
    source_cfg: Dict[str, Any],
    snapshot_dir: Path,
    fetched_at: datetime,
    timeout: int = 25,
) -> Dict[str, Any]:
    last_error = "no feed URLs configured"
    items: List[Dict[str, str]] = []
    fetched_from = ""
    channel_title = ""
    snapshot_path = ""
    attempted: List[str] = []

    configured_urls = list(source_cfg.get("feed_urls", []))
    discovery_pages = [url for url in source_cfg.get("discovery_urls", []) if url]
    homepage = str(source_cfg.get("homepage", "")).strip()
    if homepage and homepage not in discovery_pages:
        discovery_pages.append(homepage)

    candidate_urls = list(configured_urls)
    for url in candidate_urls:
        attempted.append(url)
        try:
            raw = fetch_bytes(url, timeout=timeout, accept=FEED_ACCEPT)
            snapshot_abs = save_snapshot(snapshot_dir, source_cfg["slug"], url, raw, fetched_at)
            try:
                channel_title, items = parse_feed(raw)
            except (ValueError, ET.ParseError) as exc:
                channel_title, items = parse_feed_fallback(raw)
                last_error = str(exc)
            fetched_from = url
            snapshot_path = str(snapshot_abs)
            break
        except (URLError, ValueError, ET.ParseError, OSError) as exc:
            last_error = str(exc)
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"

    discovered_urls: List[str] = []
    if not fetched_from:
        seen_urls = set(candidate_urls)
        for page_url in discovery_pages:
            if not page_url:
                continue
            try:
                for discovered in discover_feed_urls(page_url, timeout=timeout):
                    if discovered not in seen_urls:
                        seen_urls.add(discovered)
                        discovered_urls.append(discovered)
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
        for url in discovered_urls:
            attempted.append(url)
            try:
                raw = fetch_bytes(url, timeout=timeout, accept=FEED_ACCEPT)
                snapshot_abs = save_snapshot(snapshot_dir, source_cfg["slug"], url, raw, fetched_at)
                try:
                    channel_title, items = parse_feed(raw)
                except (ValueError, ET.ParseError) as exc:
                    channel_title, items = parse_feed_fallback(raw)
                    last_error = str(exc)
                fetched_from = url
                snapshot_path = str(snapshot_abs)
                break
            except (URLError, ValueError, ET.ParseError, OSError) as exc:
                last_error = str(exc)
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"

    listing_urls = [url for url in source_cfg.get("listing_urls", []) if url]
    if source_cfg.get("listing_fallback") and not listing_urls and homepage:
        listing_urls.append(homepage)
    listing_discovery_urls = [url for url in source_cfg.get("listing_discovery_urls", []) if url]
    if source_cfg.get("listing_fallback") and homepage and homepage not in listing_discovery_urls:
        listing_discovery_urls.append(homepage)

    listing_attempted: List[str] = []
    if not fetched_from and listing_urls:
        for listing_url in listing_urls:
            listing_attempted.append(listing_url)
            try:
                channel_title, items = fetch_listing_items(listing_url, timeout=timeout)
                fetched_from = listing_url
                snapshot_path = ""
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"

    if fetched_from and source_cfg.get("supplement_listing_urls") and listing_urls:
        for listing_url in listing_urls:
            listing_attempted.append(listing_url)
            try:
                _listing_title, listing_items = fetch_listing_items(listing_url, timeout=timeout)
                items = merge_items(items, listing_items)
            except Exception:
                continue

    if not fetched_from and source_cfg.get("listing_fallback"):
        discovered_listing_urls: List[str] = []
        seen_listing = set(listing_urls)
        for page_url in listing_discovery_urls:
            try:
                raw = fetch_bytes(page_url, timeout=timeout, accept=HTML_ACCEPT)
                html = raw.decode("utf-8", errors="replace")
                for suffix in ("/blog/", "/blog/page/1/", "/resources/"):
                    guess = urljoin(page_url, suffix)
                    if guess not in seen_listing:
                        seen_listing.add(guess)
                        discovered_listing_urls.append(guess)
                if re.search(r"\bblog\b", strip_html(html), re.IGNORECASE):
                    for link_html in LINK_TAG_RE.findall(html):
                        attrs = parse_link_attrs(link_html)
                        href = attrs.get("href", "")
                        if not href:
                            continue
                        full = urljoin(page_url, href)
                        if "/blog/" in full and full not in seen_listing:
                            seen_listing.add(full)
                            discovered_listing_urls.append(full)
            except Exception:
                continue
        for listing_url in discovered_listing_urls:
            listing_attempted.append(listing_url)
            try:
                channel_title, items = fetch_listing_items(listing_url, timeout=timeout)
                fetched_from = listing_url
                snapshot_path = ""
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"

    return {
        "fetched_from": fetched_from,
        "channel_title": channel_title,
        "items": items,
        "snapshot_path": snapshot_path,
        "error": "" if fetched_from else last_error,
        "attempted_urls": attempted + listing_attempted,
        "discovered_urls": discovered_urls,
    }


def parse_feed(xml_bytes: bytes) -> Tuple[str, List[Dict[str, str]]]:
    try:
        root = ET.fromstring(xml_bytes.lstrip())
    except ET.ParseError:
        root = ET.fromstring(sanitize_xml_bytes(xml_bytes))
    tag = root.tag.lower()
    items: List[Dict[str, str]] = []

    if tag.endswith("rss"):
        channel = root.find("channel")
        channel_title = text_or_empty(channel.find("title")) if channel is not None else ""
        for item in channel.findall("item") if channel is not None else []:
            title = strip_html(text_or_empty(item.find("title")))
            link = text_or_empty(item.find("link"))
            published = normalize_date(text_or_empty(item.find("pubDate")))
            summary = strip_html(text_or_empty(item.find("description")))
            items.append({"title": title, "link": link, "published": published, "summary": summary})
        return channel_title, items

    atom_ns = {"atom": "http://www.w3.org/2005/Atom"}
    if tag.endswith("feed"):
        channel_title = strip_html(text_or_empty(root.find("atom:title", atom_ns)) or text_or_empty(root.find("title")))
        entries = root.findall("atom:entry", atom_ns) or root.findall("entry")
        for entry in entries:
            title = strip_html(text_or_empty(entry.find("atom:title", atom_ns)) or text_or_empty(entry.find("title")))
            link = ""
            link_node = entry.find("atom:link[@rel='alternate']", atom_ns) or entry.find("atom:link", atom_ns) or entry.find("link")
            if link_node is not None:
                link = link_node.attrib.get("href", "").strip() or text_or_empty(link_node)
            published = normalize_date(
                text_or_empty(entry.find("atom:updated", atom_ns))
                or text_or_empty(entry.find("atom:published", atom_ns))
                or text_or_empty(entry.find("updated"))
                or text_or_empty(entry.find("published"))
            )
            summary = strip_html(
                text_or_empty(entry.find("atom:summary", atom_ns))
                or text_or_empty(entry.find("atom:content", atom_ns))
                or text_or_empty(entry.find("summary"))
                or text_or_empty(entry.find("content"))
            )
            items.append({"title": title, "link": link, "published": published, "summary": summary})
        return channel_title, items

    rdf_ns = {"rss": "http://purl.org/rss/1.0/", "dc": "http://purl.org/dc/elements/1.1/"}
    if tag.endswith("rdf"):
        channel = root.find("rss:channel", rdf_ns)
        channel_title = strip_html(text_or_empty(channel.find("rss:title", rdf_ns)) if channel is not None else "")
        for item in root.findall("rss:item", rdf_ns):
            title = strip_html(text_or_empty(item.find("rss:title", rdf_ns)))
            link = text_or_empty(item.find("rss:link", rdf_ns))
            published = normalize_date(text_or_empty(item.find("dc:date", rdf_ns)))
            summary = strip_html(text_or_empty(item.find("rss:description", rdf_ns)))
            items.append({"title": title, "link": link, "published": published, "summary": summary})
        return channel_title, items

    raise ValueError(f"Unsupported feed format: {root.tag}")


def note_filename(source_cfg: Dict[str, Any]) -> str:
    return f"live-source-{source_cfg['slug']}.md"


def load_config(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text())
    if "sources" not in payload or not isinstance(payload["sources"], list):
        raise ValueError(f"Invalid config at {path}: missing sources list")
    return payload


def select_sources(config: Dict[str, Any], selected_slugs: Optional[Sequence[str]]) -> List[Dict[str, Any]]:
    chosen = {slug.lower() for slug in selected_slugs or []}
    sources = []
    for source in config["sources"]:
        if source.get("enabled", True) is False:
            continue
        if chosen and source["slug"].lower() not in chosen:
            continue
        sources.append(source)
    return sources


def extract_item_id(item: Dict[str, str]) -> str:
    return item.get("link") or item.get("title") or json.dumps(item, sort_keys=True)


def merge_seen_ids(current_ids: Sequence[str], previous_ids: Sequence[str], limit: int = 200) -> List[str]:
    merged: List[str] = []
    seen = set()
    for item_id in list(current_ids) + list(previous_ids):
        if not item_id or item_id in seen:
            continue
        seen.add(item_id)
        merged.append(item_id)
        if len(merged) >= limit:
            break
    return merged


def source_tags(source_cfg: Dict[str, Any]) -> List[str]:
    tags = ["live_feed", "phase1_ingest", slugify(source_cfg["slug"])]
    tags.extend(slugify(str(item)) for item in source_cfg.get("tags", []))
    return [tag for tag in tags if tag]


def yaml_list(values: Iterable[str]) -> str:
    items = [str(value).strip() for value in values if str(value).strip()]
    return ", ".join(items)


def build_source_note(
    source_cfg: Dict[str, Any],
    result: Dict[str, Any],
    top_n: int,
) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    tags = source_tags(source_cfg)
    intent = source_cfg.get("intent", ["monitoring", "research", "source_selection"])
    roles = source_cfg.get("roles", ["researcher", "seo", "pinchy"])
    confidence = source_cfg.get("confidence", "medium")
    topic = source_cfg.get("topic", "live_source_ingest")
    strengths = source_cfg.get("strength", "")

    lines = [
        "---",
        f"source: {source_cfg['homepage']}",
        f"title: Live Knowledge Snapshot - {source_cfg['name']}",
        f"scraped: {today}",
        f"tags: {yaml_list(tags)}",
        f"topic: {topic}",
        f"intent: {yaml_list(intent)}",
        f"role: {yaml_list(roles)}",
        f"confidence: {confidence}",
        "canonical: false",
        "canonical_group: Live knowledge snapshots",
        "use_for: freshness, source_monitoring, article_discovery",
        "avoid_for: final_strategy_without_durable_notes",
        "---",
        "",
        f"# Live Knowledge Snapshot - {source_cfg['name']}",
        "",
        f"Homepage: {source_cfg['homepage']}",
        f"Kind: {source_cfg.get('kind', 'publication')}",
        f"Strength: {strengths}",
    ]

    if result["status"] != "ok":
        lines.extend(
            [
                f"Status: error",
                f"Last error: {result.get('error', 'unknown error')}",
                "",
                "## Latest Items",
                "- Feed fetch failed on this run",
                "",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            f"Feed source: {result['fetched_from']}",
            f"Feed title: {result.get('channel_title') or source_cfg['name']}",
            f"Latest published date: {result.get('latest_published') or 'unknown'}",
            f"New items since last run: {result['new_item_count']}",
            f"Snapshot path: {result['snapshot_path']}",
            "",
            "## Latest Items",
        ]
    )

    selected = result["items"][:top_n]
    if not selected:
        lines.append("- No items extracted")
    for item in selected:
        title = item.get("title") or "(untitled)"
        published = item.get("published") or "undated"
        link = item.get("link") or source_cfg["homepage"]
        summary = item.get("summary") or ""
        lines.append(f"- {published} | [{title}]({link})")
        if summary:
            lines.append(f"  {summary[:280]}")

    return "\n".join(lines) + "\n"


def build_summary_note(config: Dict[str, Any], results: List[Dict[str, Any]], output_dir: Path) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    title = config.get("name", "Knowledge Source Monitor")
    lines = [
        "---",
        "source: local knowledge ingestion",
        f"title: {title}",
        f"scraped: {today}",
        "tags: live_feed, phase1_ingest, monitoring, freshness",
        "topic: live_source_monitor",
        "intent: monitoring, routing, research",
        "role: researcher, seo, pinchy",
        "confidence: medium",
        "canonical: true",
        "canonical_group: Live source monitor",
        "use_for: freshness, source_selection, triage",
        "avoid_for: final_strategy_without_durable_notes",
        "---",
        "",
        f"# {title}",
        "",
        "This note is generated by the Phase 1 ingestion pipeline. Use it to spot new source activity, then open durable memory or raw source snapshots for deeper synthesis.",
        "",
        "## Source Status",
    ]

    for result in results:
        if result["status"] == "ok":
            lines.append(
                f"- {result['name']}: ok | items={result['item_count']} | new={result['new_item_count']} | latest={result.get('latest_published') or 'unknown'} | note=`{result['note_filename']}`"
            )
        else:
            lines.append(f"- {result['name']}: error | {result.get('error', 'unknown error')}")

    lines.extend(["", "## Snapshot Notes"])
    for result in results:
        lines.append(f"- `{result['note_filename']}`")

    lines.extend(["", "## Storage", f"- Raw snapshots: `{config.get('snapshot_dir_hint', '')}`".rstrip(), ""])
    return "\n".join(line for line in lines if line is not None) + "\n"


def article_note_filename(source_cfg: Dict[str, Any], article: Dict[str, Any]) -> str:
    url = str(article.get("url", ""))
    title = str(article.get("title", "")) or url
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    title_slug = slugify(title)[:90]
    return f"{title_slug}-{url_hash}.md"


def build_article_note(source_cfg: Dict[str, Any], article: Dict[str, Any]) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    tags = list(dict.fromkeys(source_tags(source_cfg) + ["archive_backfill", "historical_source"]))
    topic = source_cfg.get("topic", "archive_backfill")
    intent = source_cfg.get("intent", ["research", "archive_backfill"])
    roles = source_cfg.get("roles", ["researcher", "pinchy"])
    confidence = source_cfg.get("confidence", "medium")
    strengths = source_cfg.get("strength", "")

    lines = [
        "---",
        f"source: {article['url']}",
        f"title: {article['title']}",
        f"scraped: {today}",
        f"published_on: {article.get('published', '')}",
        f"tags: {yaml_list(tags)}",
        f"topic: {topic}",
        f"intent: {yaml_list(intent)}",
        f"role: {yaml_list(roles)}",
        f"confidence: {confidence}",
        "canonical: false",
        f"canonical_group: Archive backfill - {source_cfg['name']}",
        "use_for: historical_patterns, archive_research, source_examples",
        "avoid_for: final_strategy_without_canonical_review",
        "---",
        "",
        f"# {article['title']}",
        "",
        f"Source: {source_cfg['name']}",
        f"Homepage: {source_cfg['homepage']}",
        f"Original URL: {article['url']}",
        f"Published: {article.get('published') or 'unknown'}",
        f"Strength: {strengths}",
        "",
    ]

    author = str(article.get("author", "")).strip()
    schema_types = [str(item).strip() for item in article.get("schema_types", []) if str(item).strip()]
    headings = [str(item).strip() for item in article.get("headings", []) if str(item).strip()]
    if author or schema_types:
        lines.extend(
            [
                "## Metadata",
                *( [f"Author: {author}"] if author else [] ),
                *( [f"Schema types: {', '.join(schema_types)}"] if schema_types else [] ),
                "",
            ]
        )

    if headings:
        lines.extend(["## Section Outline"])
        for heading in headings[:12]:
            lines.append(f"- {heading}")
        lines.append("")

    lines.extend(
        [
        "## Summary",
        article.get("summary", "") or "No summary extracted.",
        "",
        "## Extracted Body",
    ])

    body_blocks = article.get("body_blocks") or article.get("paragraphs", [])
    if not body_blocks:
        lines.append("- No body paragraphs extracted.")
    else:
        for block in body_blocks:
            lines.extend([str(block).strip(), ""])
    return "\n".join(lines).strip() + "\n"


def article_snapshot_rel_path(source_slug: str, fetched_at: datetime, article_url: str) -> Path:
    parsed = urlparse(article_url)
    path_slug = slugify(parsed.path or parsed.netloc or "article")
    url_hash = hashlib.sha1(article_url.encode("utf-8")).hexdigest()[:10]
    filename = f"{fetched_at.strftime('%Y%m%dT%H%M%SZ')}-{path_slug}-{url_hash}.html"
    return Path(source_slug) / fetched_at.strftime("%Y-%m-%d") / "articles" / filename


def save_article_snapshot(snapshot_dir: Path, source_slug: str, article_url: str, payload: str, fetched_at: datetime) -> Path:
    rel_path = article_snapshot_rel_path(source_slug, fetched_at, article_url)
    abs_path = snapshot_dir / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    abs_path.write_text(payload, encoding="utf-8")
    return abs_path


def build_backfill_summary(config: Dict[str, Any], results: List[Dict[str, Any]], skills_root: Path) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "---",
        "source: local archive backfill",
        f"title: {config.get('name', 'Archive Backfill')}",
        f"scraped: {today}",
        "tags: archive_backfill, ingestion, historical_memory",
        "topic: archive_backfill",
        "intent: research, archive_recovery, chunk_growth",
        "role: pinchy, researcher, developer",
        "confidence: medium",
        "---",
        "",
        f"# {config.get('name', 'Archive Backfill')}",
        "",
        f"Skills root: `{skills_root}`",
        "",
        "## Source Results",
    ]
    for result in results:
        lines.append(
            f"- {result['name']}: archived=`{result['archived_count']}` | candidates=`{result['candidate_count']}` | attempted=`{result['attempted_count']}` | output=`{result['output_dir']}`"
        )
    return "\n".join(lines) + "\n"


def snapshot_rel_path(source_slug: str, fetched_at: datetime, url: str) -> Path:
    parsed = urlparse(url)
    path_slug = slugify(parsed.path or parsed.netloc or "feed")
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    filename = f"{fetched_at.strftime('%Y%m%dT%H%M%SZ')}-{path_slug}-{url_hash}.xml"
    return Path(source_slug) / fetched_at.strftime("%Y-%m-%d") / filename


def save_snapshot(snapshot_dir: Path, source_slug: str, url: str, payload: bytes, fetched_at: datetime) -> Path:
    rel_path = snapshot_rel_path(source_slug, fetched_at, url)
    abs_path = snapshot_dir / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    abs_path.write_bytes(payload)
    return abs_path


def latest_published(items: Sequence[Dict[str, str]]) -> str:
    dates = [item.get("published", "") for item in items if item.get("published")]
    return max(dates) if dates else ""


def build_run_id(now: datetime) -> str:
    return now.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def run_ingest(
    config_path: Path,
    output_dir: Path,
    summary_path: Path,
    snapshot_dir: Path,
    runs_dir: Path,
    state_path: Path,
    top_n: int,
    selected_slugs: Optional[Sequence[str]],
    build_db: bool,
    skills_root: Path,
    db_path: Path,
) -> Dict[str, Any]:
    config = load_config(config_path)
    sources = select_sources(config, selected_slugs)
    output_dir.mkdir(parents=True, exist_ok=True)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)

    state = load_json(state_path, {"generated_at": "", "sources": {}})
    now = datetime.now(timezone.utc)
    run_id = build_run_id(now)
    results: List[Dict[str, Any]] = []

    for source_cfg in sources:
        fetch_result = fetch_source_feed(source_cfg, snapshot_dir, now)
        items = fetch_result["items"]
        fetched_from = fetch_result["fetched_from"]
        channel_title = fetch_result["channel_title"]
        snapshot_path = fetch_result["snapshot_path"]
        last_error = fetch_result["error"]

        previous = state.get("sources", {}).get(source_cfg["slug"], {})
        previous_seen = previous.get("seen_ids", [])
        current_ids = [extract_item_id(item) for item in items]
        new_item_count = len([item_id for item_id in current_ids if item_id and item_id not in set(previous_seen)])

        result: Dict[str, Any] = {
            "slug": source_cfg["slug"],
            "name": source_cfg["name"],
            "status": "ok" if fetched_from else "error",
            "fetched_from": fetched_from,
            "channel_title": channel_title,
            "item_count": len(items),
            "new_item_count": new_item_count,
            "latest_published": latest_published(items),
            "snapshot_path": snapshot_path,
            "items": items,
            "error": last_error if not fetched_from else "",
            "attempted_urls": fetch_result.get("attempted_urls", []),
            "discovered_urls": fetch_result.get("discovered_urls", []),
            "note_filename": note_filename(source_cfg),
        }

        note_text = build_source_note(source_cfg, result, top_n)
        (output_dir / result["note_filename"]).write_text(note_text)
        result["note_path"] = str(output_dir / result["note_filename"])
        results.append(result)

        state.setdefault("sources", {})[source_cfg["slug"]] = {
            "name": source_cfg["name"],
            "kind": source_cfg.get("kind", "publication"),
            "last_success_at": now.isoformat() if fetched_from else previous.get("last_success_at", ""),
            "last_status": result["status"],
            "latest_published": result["latest_published"],
            "last_item_count": len(items),
            "last_new_item_count": new_item_count,
            "last_snapshot_path": snapshot_path,
            "last_note_path": result["note_path"],
            "seen_ids": merge_seen_ids(current_ids, previous_seen),
        }

    config_with_hints = dict(config)
    config_with_hints["snapshot_dir_hint"] = str(snapshot_dir)
    summary_path.write_text(build_summary_note(config_with_hints, results, output_dir))

    state["generated_at"] = now.isoformat()
    state["last_run_id"] = run_id
    state["summary_path"] = str(summary_path)
    write_json(state_path, state)

    manifest = {
        "run_id": run_id,
        "generated_at": now.isoformat(),
        "config_path": str(config_path),
        "output_dir": str(output_dir),
        "summary_path": str(summary_path),
        "snapshot_dir": str(snapshot_dir),
        "state_path": str(state_path),
        "results": [
            {key: value for key, value in result.items() if key != "items"} for result in results
        ],
    }
    manifest_path = runs_dir / f"knowledge-ingest-{run_id}.json"
    write_json(manifest_path, manifest)
    write_json(runs_dir / "latest.json", manifest)

    build_summary: Optional[Dict[str, Any]] = None
    if build_db:
        completed = subprocess.run(
            [
                sys.executable,
                str(HOME / "squad_memory" / "squad_memory.py"),
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
        build_summary = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
            "skills_root": str(skills_root),
        }
        if completed.returncode != 0:
            raise SystemExit(completed.returncode)

    manifest["manifest_path"] = str(manifest_path)
    manifest["build"] = build_summary
    write_json(manifest_path, manifest)
    write_json(runs_dir / "latest.json", manifest)
    return manifest


def merge_seen_urls(current_urls: Sequence[str], previous_urls: Sequence[str], limit: int = 50000) -> List[str]:
    merged: List[str] = []
    seen = set()
    for url in list(current_urls) + list(previous_urls):
        value = str(url).strip()
        if not value or value in seen:
            continue
        seen.add(value)
        merged.append(value)
        if len(merged) >= limit:
            break
    return merged


def run_backfill(
    config_path: Path,
    skills_root: Path,
    snapshot_dir: Path,
    runs_dir: Path,
    state_path: Path,
    summary_path: Path,
    selected_slugs: Optional[Sequence[str]],
    per_source_limit: int,
    max_articles: int,
    build_db: bool,
    db_path: Path,
) -> Dict[str, Any]:
    config = load_config(config_path)
    sources = select_sources(config, selected_slugs)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)
    state = load_json(state_path, {"generated_at": "", "sources": {}})
    now = datetime.now(timezone.utc)
    run_id = build_run_id(now)
    results: List[Dict[str, Any]] = []
    remaining = max(0, max_articles)

    for source_cfg in sources:
        if remaining <= 0:
            break

        previous = state.get("sources", {}).get(source_cfg["slug"], {})
        seen_urls = set(previous.get("seen_urls", []))
        output_dir = archive_output_dir(skills_root, source_cfg)
        output_dir.mkdir(parents=True, exist_ok=True)

        feed_seed = fetch_source_feed(source_cfg, snapshot_dir, now)
        homepage = str(source_cfg.get("homepage", "")).strip()
        seed_urls = []
        for item in feed_seed.get("items", []):
            value = str(item.get("link", "")).strip()
            if not value:
                continue
            pseudo_title = value.rstrip("/").split("/")[-1].replace("-", " ")
            if homepage and not is_probable_listing_article(value, pseudo_title or "Recovered archive article", homepage):
                continue
            seed_urls.append(value)
        archive_result = collect_archive_urls(
            source_cfg,
            limit=max(per_source_limit * 6, min(remaining * 3, 5000)),
        )
        candidate_urls: List[str] = []
        candidate_seen = set()
        for url in seed_urls + archive_result["article_urls"]:
            value = str(url).strip()
            if not value or value in candidate_seen:
                continue
            candidate_seen.add(value)
            candidate_urls.append(value)

        allowed_for_source = min(per_source_limit, remaining)
        archived_articles: List[Dict[str, Any]] = []
        attempted_count = 0
        errors: List[str] = []

        for article_url in candidate_urls:
            if len(archived_articles) >= allowed_for_source:
                break
            if article_url in seen_urls:
                continue
            attempted_count += 1
            try:
                html = fetch_html(article_url)
                article = extract_article_document(html, article_url, source_cfg)
                if not article:
                    continue
                save_article_snapshot(snapshot_dir, source_cfg["slug"], article_url, html, now)
                note_filename = article_note_filename(source_cfg, article)
                note_path = output_dir / note_filename
                note_path.write_text(build_article_note(source_cfg, article), encoding="utf-8")
                archived_articles.append(
                    {
                        "title": article["title"],
                        "url": article_url,
                        "note_filename": note_filename,
                        "published": article.get("published", ""),
                    }
                )
            except Exception as exc:
                errors.append(f"{article_url} :: {type(exc).__name__}: {exc}")

        current_urls = [item["url"] for item in archived_articles]
        state.setdefault("sources", {})[source_cfg["slug"]] = {
            "name": source_cfg["name"],
            "domain": domain_for_source(source_cfg),
            "last_run_id": run_id,
            "last_run_at": now.isoformat(),
            "last_archived_count": len(archived_articles),
            "last_candidate_count": len(candidate_urls),
            "last_attempted_count": attempted_count,
            "last_output_dir": str(output_dir),
            "last_sitemap_urls": archive_result["sitemap_urls"][:20],
            "seen_urls": merge_seen_urls(current_urls, previous.get("seen_urls", [])),
        }

        results.append(
            {
                "slug": source_cfg["slug"],
                "name": source_cfg["name"],
                "domain": domain_for_source(source_cfg),
                "candidate_count": len(candidate_urls),
                "attempted_count": attempted_count,
                "archived_count": len(archived_articles),
                "output_dir": str(output_dir),
                "sitemap_urls": archive_result["sitemap_urls"][:20],
                "seed_item_count": len(feed_seed.get("items", [])),
                "articles": archived_articles[:10],
                "errors": errors[:12],
            }
        )
        remaining -= len(archived_articles)

    state["generated_at"] = now.isoformat()
    state["last_run_id"] = run_id
    state["summary_path"] = str(summary_path)
    write_json(state_path, state)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(build_backfill_summary(config, results, skills_root), encoding="utf-8")

    manifest = {
        "run_id": run_id,
        "generated_at": now.isoformat(),
        "config_path": str(config_path),
        "skills_root": str(skills_root),
        "snapshot_dir": str(snapshot_dir),
        "state_path": str(state_path),
        "summary_path": str(summary_path),
        "results": results,
    }
    manifest_path = runs_dir / f"archive-backfill-{run_id}.json"
    write_json(manifest_path, manifest)
    write_json(runs_dir / "archive-latest.json", manifest)

    build_summary: Optional[Dict[str, Any]] = None
    if build_db:
        completed = subprocess.run(
            [
                sys.executable,
                str(HOME / "squad_memory" / "squad_memory.py"),
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
        build_summary = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
            "skills_root": str(skills_root),
        }
        if completed.returncode != 0:
            raise SystemExit(completed.returncode)

    manifest["manifest_path"] = str(manifest_path)
    manifest["build"] = build_summary
    write_json(manifest_path, manifest)
    write_json(runs_dir / "archive-latest.json", manifest)
    return manifest


def report_state(state_path: Path) -> Dict[str, Any]:
    payload = load_json(state_path, {"generated_at": "", "sources": {}})
    payload["state_path"] = str(state_path)
    return payload


def print_manifest(manifest: Dict[str, Any]) -> None:
    print(f"Run ID: {manifest['run_id']}")
    print(f"Generated: {manifest['generated_at']}")
    print(f"Summary note: {manifest['summary_path']}")
    print(f"Manifest: {manifest['manifest_path']}")
    print("")
    for result in manifest["results"]:
        if result["status"] == "ok":
            print(
                f"- {result['name']}: ok items={result['item_count']} new={result['new_item_count']} "
                f"latest={result['latest_published'] or 'unknown'} note={result['note_filename']}"
            )
        else:
            print(f"- {result['name']}: error {result['error']}")
    if manifest.get("build"):
        build = manifest["build"]
        print("")
        print(f"Build DB: rc={build['returncode']} db={build['db_path']}")
        if build["stdout"]:
            print(build["stdout"])
        if build["stderr"]:
            print(build["stderr"])


def print_backfill_manifest(manifest: Dict[str, Any]) -> None:
    print(f"Run ID: {manifest['run_id']}")
    print(f"Generated: {manifest['generated_at']}")
    print(f"Summary note: {manifest['summary_path']}")
    print(f"Manifest: {manifest['manifest_path']}")
    print("")
    for result in manifest["results"]:
        print(
            f"- {result['name']} [{result['domain']}]: archived={result['archived_count']} "
            f"candidates={result['candidate_count']} attempted={result['attempted_count']}"
        )
        if result.get("errors"):
            print(f"  errors={len(result['errors'])}")
    if manifest.get("build"):
        build = manifest["build"]
        print("")
        print(f"Build DB: rc={build['returncode']} db={build['db_path']}")
        if build["stdout"]:
            print(build["stdout"])
        if build["stderr"]:
            print(build["stderr"])


def print_state(state: Dict[str, Any]) -> None:
    print(f"State: {state['state_path']}")
    print(f"Generated: {state.get('generated_at', '') or 'never'}")
    for slug, item in sorted(state.get("sources", {}).items()):
        print(
            f"- {slug}: status={item.get('last_status', 'unknown')} "
            f"latest={item.get('latest_published') or 'unknown'} "
            f"new={item.get('last_new_item_count', 0)}"
        )


def main() -> int:
    args = parse_args()
    if args.command == "run":
        manifest = run_ingest(
            config_path=Path(args.config),
            output_dir=Path(args.output_dir),
            summary_path=Path(args.summary_path),
            snapshot_dir=Path(args.snapshot_dir),
            runs_dir=Path(args.runs_dir),
            state_path=Path(args.state_path),
            top_n=args.top,
            selected_slugs=args.sources,
            build_db=args.build_db,
            skills_root=Path(args.skills_root),
            db_path=Path(args.db_path),
        )
        if args.json:
            print(json.dumps(manifest, indent=2, ensure_ascii=True))
        else:
            print_manifest(manifest)
        return 0

    if args.command == "backfill":
        manifest = run_backfill(
            config_path=Path(args.config),
            skills_root=Path(args.skills_root),
            snapshot_dir=Path(args.snapshot_dir),
            runs_dir=Path(args.runs_dir),
            state_path=Path(args.state_path),
            summary_path=Path(args.summary_path),
            selected_slugs=args.sources,
            per_source_limit=args.per_source_limit,
            max_articles=args.max_articles,
            build_db=args.build_db,
            db_path=Path(args.db_path),
        )
        if args.json:
            print(json.dumps(manifest, indent=2, ensure_ascii=True))
        else:
            print_backfill_manifest(manifest)
        return 0

    if args.command == "report":
        state = report_state(Path(args.state_path))
        if args.json:
            print(json.dumps(state, indent=2, ensure_ascii=True))
        else:
            print_state(state)
        return 0

    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
