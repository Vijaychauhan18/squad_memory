#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import http.client
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

try:
    from scrapling import Fetcher as ScraplingFetcher
except Exception:
    ScraplingFetcher = None


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "elite-skills"
DEFAULT_SKILL_ROOT = DEFAULT_SKILLS_ROOT / "seo-elite"
DEFAULT_MEMORY_DIR = DEFAULT_SKILL_ROOT / "memory"
DEFAULT_ARCHIVE_DIR = DEFAULT_MEMORY_DIR / "archive"
DEFAULT_DB = BASE / "seo_elite_memory.db"
DEFAULT_STATE = BASE / "ingest" / "seo_elite" / "article_harvest" / "state.json"
DEFAULT_RUNS = BASE / "ingest" / "seo_elite" / "article_harvest" / "runs"
DEFAULT_LOGICAL_LIMIT = 9999
FAILED_RETRY_THRESHOLD = 2
BLOCKED_SOURCES = {
    "yoast",
    "moz",
}
SOURCE_QUEUE_CAPS = {
    "yoast": 160,
    "moz": 40,
}
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
HTML_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
ITEM_RE = re.compile(r"^- (\d{4}-\d{2}-\d{2}|unknown) \| \[(.*?)\]\((.*?)\)\s*$")
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b.*?>.*?</\1>", re.IGNORECASE | re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
ARTICLE_RE = re.compile(r"<article\b.*?>(.*?)</article>", re.IGNORECASE | re.DOTALL)
BODY_RE = re.compile(r"<body\b.*?>(.*?)</body>", re.IGNORECASE | re.DOTALL)
P_RE = re.compile(r"<p\b[^>]*>(.*?)</p>", re.IGNORECASE | re.DOTALL)
H1_RE = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
TITLE_RE = re.compile(r"<title\b[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Harvest article-level notes from the elite SEO source snapshots")
    parser.add_argument("--memory-dir", default=str(DEFAULT_MEMORY_DIR))
    parser.add_argument("--archive-dir", default=str(DEFAULT_ARCHIVE_DIR))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--runs-dir", default=str(DEFAULT_RUNS))
    parser.add_argument("--limit-per-run", type=int, default=400)
    parser.add_argument("--max-workers", type=int, default=24)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_json(path: Path, default: Dict[str, object]) -> Dict[str, object]:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "article"


def strip_html(text: str) -> str:
    return WS_RE.sub(" ", TAG_RE.sub(" ", unescape(text))).strip()


def clean_candidate_url(url: str) -> str:
    match = re.search(r"https?://[^\s<>'\")]+", url.strip())
    return match.group(0).strip() if match else ""


def is_valid_http_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


SOCIAL_NETLOCS = (
    "youtube.com",
    "www.youtube.com",
    "youtu.be",
    "twitter.com",
    "x.com",
    "www.x.com",
    "linkedin.com",
    "www.linkedin.com",
    "facebook.com",
    "www.facebook.com",
    "instagram.com",
    "www.instagram.com",
    "tiktok.com",
    "www.tiktok.com",
)

NON_ARTICLE_LAST_SEGMENTS = {
    "about",
    "about-us",
    "author",
    "authors",
    "team",
    "contact",
    "careers",
    "privacy-policy",
    "terms",
    "newsletter",
    "podcast",
}

NON_ARTICLE_PATH_SEGMENTS = {
    "author",
    "authors",
    "category",
    "categories",
    "tag",
    "tags",
    "events",
    "event",
    "webinars",
    "webinar",
}

LISTING_LAST_SEGMENTS = {
    "blog",
    "articles",
    "resources",
    "category",
    "categories",
    "news",
    "seo-blog",
    "marketing-blog",
}


def normalize_netloc(value: str) -> str:
    netloc = urlparse(value).netloc.lower().strip()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


def is_same_source_domain(url: str, homepage: str) -> bool:
    if not homepage:
        return True
    host = normalize_netloc(url)
    home_host = normalize_netloc(homepage)
    if not host or not home_host:
        return True
    return host == home_host or host.endswith(f".{home_host}") or home_host.endswith(f".{host}")


def is_probable_article_url(url: str) -> bool:
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    if not is_valid_http_url(url):
        return False
    if any(netloc == host or netloc.endswith(f".{host}") for host in SOCIAL_NETLOCS):
        return False
    segments = [segment for segment in parsed.path.split("/") if segment]
    if not segments:
        return False
    if any(segment.lower() in NON_ARTICLE_PATH_SEGMENTS for segment in segments):
        return False
    last = segments[-1].lower()
    if last in NON_ARTICLE_LAST_SEGMENTS:
        return False
    if last.startswith("about-") or last.startswith("author-"):
        return False
    if last in LISTING_LAST_SEGMENTS and len(segments) <= 2:
        return False
    if "page" in segments and last.isdigit():
        return False
    return True


def parse_source_note(path: Path) -> Tuple[str, str, List[Dict[str, str]]]:
    lines = path.read_text().splitlines()
    source_name = path.stem.replace("live-source-", "").replace("bulk-source-", "")
    homepage = ""
    items: List[Dict[str, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("Homepage: "):
            homepage = line[len("Homepage: ") :].strip()
        match = ITEM_RE.match(line)
        if match:
            published, title, url = match.groups()
            cleaned_url = clean_candidate_url(url)
            if not is_probable_article_url(cleaned_url):
                i += 1
                continue
            if not is_same_source_domain(cleaned_url, homepage):
                i += 1
                continue
            summary = ""
            if i + 1 < len(lines) and lines[i + 1].startswith("  "):
                summary = lines[i + 1].strip()
                i += 1
            items.append(
                {
                    "published": published,
                    "title": title.strip(),
                    "url": cleaned_url,
                    "summary": summary,
                }
            )
        i += 1
    return source_name, homepage, items


def iter_source_notes(notes_dir: Path) -> List[Path]:
    notes: List[Path] = []
    for pattern in ("live-source-*.md", "bulk-source-*.md"):
        notes.extend(path for path in notes_dir.rglob(pattern) if path.is_file())
    return sorted(set(notes))


def fetch_html(url: str, timeout: int = 25) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": HTML_ACCEPT,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        if exc.code != 403 or ScraplingFetcher is None:
            raise
        response = ScraplingFetcher.get(url, timeout=timeout)
        html = getattr(response, "html_content", None) or getattr(response, "body", None)
        text = str(html) if html is not None else ""
        if not text or text == "None":
            raise
        return text


def extract_article_text(html: str) -> Tuple[str, List[str]]:
    html = COMMENT_RE.sub(" ", html)
    html = SCRIPT_STYLE_RE.sub(" ", html)
    title_match = H1_RE.search(html) or TITLE_RE.search(html)
    title = strip_html(title_match.group(1)) if title_match else ""
    block_match = ARTICLE_RE.search(html) or BODY_RE.search(html)
    block = block_match.group(1) if block_match else html
    paragraphs: List[str] = []
    for para in P_RE.findall(block):
        text = strip_html(para)
        if len(text) >= 80:
            paragraphs.append(text)
        if len(paragraphs) >= 16:
            break
    return title, paragraphs


def render_note(source_slug: str, source_name: str, homepage: str, item: Dict[str, str], title: str, paragraphs: Iterable[str]) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    topic = "seo_article"
    role = "researcher, seo, pinchy"
    tags = f"elite_article, seo, {source_slug}, article_snapshot"
    para_lines = [f"- {para}" for para in paragraphs]
    return "\n".join(
        [
            "---",
            f"source: {item['url']}",
            f"title: {title or item['title']}",
            f"scraped: {today}",
            f"tags: {tags}",
            f"topic: {topic}",
            "intent: research, synthesis, source_selection",
            f"role: {role}",
            "confidence: medium",
            "canonical: false",
            "canonical_group: Elite article harvest",
            "use_for: article-level context, synthesis, deeper retrieval",
            "avoid_for: exact verbatim quoting",
            "---",
            "",
            f"# {title or item['title']}",
            "",
            f"Source expert/publication: {source_name}",
            f"Source homepage: {homepage or 'unknown'}",
            f"Original URL: {item['url']}",
            f"Published: {item['published']}",
            "",
            "## Why This Matters",
            item["summary"] or "Captured from the elite SEO source layer for deeper retrieval and later synthesis.",
            "",
            "## Extracted Article Passages",
            *para_lines,
            "",
            "## Retrieval Use",
            f"- Use when the task maps to `{source_slug}` or overlaps with the article title.",
            "- Prefer this note over the source snapshot when you need article-level detail.",
            "",
        ]
    ) + "\n"


def note_path(base_dir: Path, source_slug: str, item: Dict[str, str]) -> Path:
    domain = urlparse(item["url"]).netloc.replace(".", "-")
    filename = f"{item['published']}-{slugify(item['title'])}.md"
    return base_dir / "articles" / source_slug / domain / filename


def index_path(base_dir: Path) -> Path:
    return base_dir / "articles" / "INDEX.md"


def rebuild_index(base_dir: Path) -> None:
    articles_root = base_dir / "articles"
    articles_root.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Elite Article Harvest Index",
        "",
        "Generated article-level notes from the elite SEO source snapshots.",
        "",
    ]
    for source_dir in sorted(path for path in articles_root.iterdir() if path.is_dir()):
        count = sum(1 for _ in source_dir.rglob("*.md"))
        lines.append(f"- {source_dir.name}: {count} notes")
    index_path(base_dir).write_text("\n".join(lines) + "\n")


def collect_pending_candidates(
    source_sets: List[Tuple[Path, Path]],
    fetched_urls: Dict[str, Dict[str, str]],
    failed_urls: Dict[str, Dict[str, object]],
    limit: int,
) -> List[Tuple[str, str, Dict[str, str], Path]]:
    candidates: List[Tuple[str, str, Dict[str, str], Path]] = []
    queued_urls = set()
    source_counts: Dict[str, int] = {}
    for notes_dir, output_base in source_sets:
        for note in iter_source_notes(notes_dir):
            if note.name.startswith("live-source-canon") or note.name in {"live-source-canon.md", "live-source-cluster-report.md"}:
                continue
            source_slug, homepage, items = parse_source_note(note)
            if source_slug in BLOCKED_SOURCES:
                continue
            for item in items:
                if source_counts.get(source_slug, 0) >= SOURCE_QUEUE_CAPS.get(source_slug, limit):
                    continue
                url = item["url"]
                failed_entry = failed_urls.get(url, {})
                failed_count = int(failed_entry.get("count", 0)) if isinstance(failed_entry, dict) else 0
                if failed_count >= FAILED_RETRY_THRESHOLD:
                    continue
                if not url or not is_valid_http_url(url) or url in fetched_urls or url in queued_urls:
                    continue
                queued_urls.add(url)
                candidates.append((source_slug, homepage, item, output_base))
                source_counts[source_slug] = source_counts.get(source_slug, 0) + 1
                if len(candidates) >= limit:
                    return candidates
    return candidates


def harvest_candidate(candidate: Tuple[str, str, Dict[str, str], Path]) -> Dict[str, object]:
    source_slug, homepage, item, output_base = candidate
    url = item["url"]
    try:
        html = fetch_html(url)
        extracted_title, paragraphs = extract_article_text(html)
    except HTTPError as exc:
        return {"ok": False, "url": url, "error": f"http_{exc.code}"}
    except URLError:
        return {"ok": False, "url": url, "error": "url_error"}
    except (OSError, ValueError, http.client.InvalidURL):
        return {"ok": False, "url": url, "error": "fetch_error"}
    if not paragraphs:
        return {"ok": False, "url": url, "error": "no_paragraphs"}
    return {
        "ok": True,
        "source_slug": source_slug,
        "homepage": homepage,
        "item": item,
        "output_base": str(output_base),
        "extracted_title": extracted_title,
        "paragraphs": paragraphs,
    }


def main() -> int:
    args = parse_args()
    memory_dir = Path(args.memory_dir)
    archive_dir = Path(args.archive_dir)
    state_path = Path(args.state_path)
    runs_dir = Path(args.runs_dir)
    state = load_json(state_path, {"fetched_urls": {}, "failed_urls": {}})
    fetched_urls: Dict[str, Dict[str, str]] = state.get("fetched_urls", {})  # type: ignore[assignment]
    failed_urls: Dict[str, Dict[str, object]] = state.get("failed_urls", {})  # type: ignore[assignment]
    harvested = 0
    results: List[Dict[str, str]] = []

    source_sets = [
        (memory_dir, memory_dir),
        (archive_dir, archive_dir),
    ]
    candidates = collect_pending_candidates(source_sets, fetched_urls, failed_urls, args.limit_per_run)
    max_workers = max(4, min(args.max_workers, 48))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(harvest_candidate, candidate): candidate for candidate in candidates}
        for future in concurrent.futures.as_completed(future_map):
            payload = future.result()
            if not payload.get("ok"):
                url = str(payload["url"])
                entry = failed_urls.get(url, {})
                failed_urls[url] = {
                    "count": int(entry.get("count", 0)) + 1 if isinstance(entry, dict) else 1,
                    "last_error": str(payload.get("error", "unknown")),
                    "last_attempted": datetime.now(timezone.utc).isoformat(),
                }
                continue
            source_slug = str(payload["source_slug"])
            homepage = str(payload["homepage"])
            item = payload["item"]  # type: ignore[assignment]
            output_base = Path(str(payload["output_base"]))
            target = note_path(output_base, source_slug, item)  # type: ignore[arg-type]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                render_note(
                    source_slug,
                    source_slug,
                    homepage,
                    item,  # type: ignore[arg-type]
                    str(payload["extracted_title"]),
                    payload["paragraphs"],  # type: ignore[arg-type]
                )
            )
            url = item["url"]  # type: ignore[index]
            fetched_urls[url] = {
                "source_slug": source_slug,
                "path": str(target),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
            failed_urls.pop(url, None)
            results.append({"url": url, "path": str(target)})
            harvested += 1
            if harvested % 25 == 0:
                print(f"Harvest progress: {harvested}/{len(candidates)}", flush=True)

    rebuild_index(memory_dir)
    rebuild_index(archive_dir)
    write_json(
        state_path,
        {
            "fetched_urls": fetched_urls,
            "failed_urls": failed_urls,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "harvested_count": len(fetched_urls),
        },
    )
    runs_dir.mkdir(parents=True, exist_ok=True)
    write_json(
        runs_dir / f"article-harvest-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json",
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "harvested_this_run": harvested,
            "results": results[:DEFAULT_LOGICAL_LIMIT],
        },
    )

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

    payload = {
        "harvested_this_run": harvested,
        "total_fetched_urls": len(fetched_urls),
        "db_path": args.db_path,
        "build_stdout": completed.stdout.strip(),
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(f"Harvested article notes: {harvested}")
        print(f"Total harvested URLs: {len(fetched_urls)}")
        if completed.stdout.strip():
            print(completed.stdout.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
