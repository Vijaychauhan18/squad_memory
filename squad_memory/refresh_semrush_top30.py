#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import knowledge_ingest


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_CONFIG = BASE / "knowledge_sources_seo_elite_archive.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "elite-skills"
DEFAULT_OUTPUT_DIR = DEFAULT_SKILLS_ROOT / "seo-elite" / "memory" / "archive"
DEFAULT_NOTE_PATH = DEFAULT_OUTPUT_DIR / "live-source-semrush.md"
DEFAULT_SUMMARY_PATH = DEFAULT_OUTPUT_DIR / "realtime-semrush-top30-monitor.md"
DEFAULT_SNAPSHOT_DIR = BASE / "ingest" / "seo_elite" / "realtime" / "semrush" / "raw"
DEFAULT_RUNS_DIR = BASE / "ingest" / "seo_elite" / "realtime" / "semrush" / "runs"
DEFAULT_STATE_PATH = BASE / "ingest" / "seo_elite" / "archive" / "state.json"
DEFAULT_DB = BASE / "seo_elite_memory.db"
SEM_RUSH_SLUG = "semrush"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh Semrush top-30 recent articles using feed + paginated Next.js data")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--note-path", default=str(DEFAULT_NOTE_PATH))
    parser.add_argument("--summary-path", default=str(DEFAULT_SUMMARY_PATH))
    parser.add_argument("--snapshot-dir", default=str(DEFAULT_SNAPSHOT_DIR))
    parser.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--max-pages", type=int, default=12)
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_source_cfg(config_path: Path) -> Dict[str, Any]:
    payload = json.loads(config_path.read_text())
    for source in payload.get("sources", []):
        if source.get("slug") == SEM_RUSH_SLUG:
            return source
    raise ValueError(f"Missing `{SEM_RUSH_SLUG}` source in {config_path}")


def normalize_semrush_url(raw_url: str, homepage: str) -> str:
    if not raw_url:
        return ""
    cleaned = raw_url.strip()
    if cleaned.startswith("http://") or cleaned.startswith("https://"):
        return cleaned
    return knowledge_ingest.urljoin(homepage.rstrip("/") + "/", cleaned.strip("/") + "/")


def iso_from_epoch_ms(value: Any) -> str:
    if not value:
        return ""
    try:
        epoch_ms = int(value)
    except (TypeError, ValueError):
        return ""
    return datetime.fromtimestamp(epoch_ms / 1000, tz=timezone.utc).date().isoformat()


def extract_next_data_json(raw_html: str) -> Dict[str, Any]:
    match = knowledge_ingest.re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        raw_html,
        knowledge_ingest.re.DOTALL,
    )
    if not match:
        raise ValueError("Missing __NEXT_DATA__ payload")
    return json.loads(match.group(1))


def card_to_item(card: Dict[str, Any], homepage: str) -> Dict[str, str]:
    title = str(card.get("title", "")).strip()
    link = normalize_semrush_url(str(card.get("url", "")).strip(), homepage)
    published = iso_from_epoch_ms(card.get("publishedAt"))
    summary = str(card.get("preview", "")).strip()
    return {
        "title": title,
        "link": link,
        "published": published,
        "summary": summary,
    }


def extract_semrush_page_items(page_html: bytes, homepage: str, page_number: int) -> Tuple[int, List[Dict[str, str]]]:
    raw_html = page_html.decode("utf-8", errors="replace")
    payload = extract_next_data_json(raw_html)
    props = payload.get("props", {}).get("pageProps", {})
    current_page = int(props.get("currentPage") or page_number)

    cards: List[Dict[str, Any]] = []
    if current_page == 1:
        preview = props.get("previewCard")
        if isinstance(preview, dict):
            cards.append(preview)
        big_cards = props.get("bigCards", [])
        if isinstance(big_cards, list):
            cards.extend(card for card in big_cards if isinstance(card, dict))

    articles = props.get("articles", [])
    if isinstance(articles, list):
        cards.extend(card for card in articles if isinstance(card, dict))

    items = [card_to_item(card, homepage) for card in cards]
    items = [item for item in items if item.get("title") and item.get("link")]
    return current_page, items


def fetch_feed_items(source_cfg: Dict[str, Any], snapshot_dir: Path, fetched_at: datetime) -> Tuple[str, str, str, List[Dict[str, str]]]:
    last_error = "no feed found"
    for url in source_cfg.get("feed_urls", []):
        try:
            raw = knowledge_ingest.fetch_bytes(url, accept=knowledge_ingest.FEED_ACCEPT)
            snapshot_abs = knowledge_ingest.save_snapshot(snapshot_dir, source_cfg["slug"], url, raw, fetched_at)
            try:
                feed_title, items = knowledge_ingest.parse_feed(raw)
            except Exception:
                feed_title, items = knowledge_ingest.parse_feed_fallback(raw)
            return url, feed_title, str(snapshot_abs), items
        except Exception as exc:
            last_error = str(exc)
    raise ValueError(last_error)


def fetch_semrush_page(page_url: str, source_cfg: Dict[str, Any], snapshot_dir: Path, fetched_at: datetime, page_number: int) -> Tuple[str, List[Dict[str, str]]]:
    raw = knowledge_ingest.fetch_bytes(page_url, accept=knowledge_ingest.HTML_ACCEPT)
    knowledge_ingest.save_snapshot(snapshot_dir, f"{source_cfg['slug']}-page{page_number}", page_url, raw, fetched_at)
    current_page, items = extract_semrush_page_items(raw, source_cfg["homepage"], page_number)
    return f"page={current_page}", items


def dedupe_items(items: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    merged: Dict[str, Dict[str, str]] = {}
    for item in items:
        link = item.get("link", "").strip()
        if not link:
            continue
        current = merged.get(link, {})
        current_published = current.get("published", "")
        new_published = item.get("published", "")
        preferred_published = max(current_published, new_published)
        merged[link] = {
            "title": current.get("title") or item.get("title") or "",
            "link": link,
            "published": preferred_published,
            "summary": current.get("summary") or item.get("summary") or "",
        }
    return list(merged.values())


def sort_items(items: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    return sorted(
        items,
        key=lambda item: (
            item.get("published", ""),
            item.get("title", ""),
        ),
        reverse=True,
    )


def build_note(source_cfg: Dict[str, Any], items: Sequence[Dict[str, str]], latest: str, new_item_count: int, feed_source: str, feed_title: str, snapshot_path: str, fetched_pages: Sequence[str], top_n: int) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    tags = knowledge_ingest.source_tags(source_cfg) + ["semrush_top30", "semrush_next_data"]
    lines = [
        "---",
        f"source: {source_cfg['homepage']}",
        f"title: Live Knowledge Snapshot - {source_cfg['name']}",
        f"scraped: {today}",
        f"tags: {knowledge_ingest.yaml_list(tags)}",
        f"topic: {source_cfg.get('topic', 'seo_research')}",
        f"intent: {knowledge_ingest.yaml_list(source_cfg.get('intent', []))}",
        f"role: {knowledge_ingest.yaml_list(source_cfg.get('roles', []))}",
        f"confidence: {source_cfg.get('confidence', 'medium')}",
        "canonical: false",
        "canonical_group: Live knowledge snapshots",
        "use_for: freshness, semrush monitoring, article discovery, AI-search research",
        "avoid_for: exact publication-count claims without manual verification",
        "---",
        "",
        f"# Live Knowledge Snapshot - {source_cfg['name']}",
        "",
        f"Homepage: {source_cfg['homepage']}",
        f"Kind: {source_cfg.get('kind', 'publication')}",
        f"Strength: {source_cfg.get('strength', '')}",
        f"Feed source: {feed_source}",
        f"Feed title: {feed_title or source_cfg['name']}",
        f"Latest published date: {latest or 'unknown'}",
        f"New items since last run: {new_item_count}",
        f"Snapshot path: {snapshot_path}",
        f"Supplemental Semrush pages: {', '.join(fetched_pages) if fetched_pages else 'none'}",
        "",
        "## Extraction Notes",
        "- Source mix: RSS feed for the freshest posts plus Semrush's paginated Next.js article payload.",
        "- The paginated blog index can mix in featured evergreen content, so this note sorts merged items by published date and keeps the newest unique URLs.",
        "",
        "## Latest Items",
    ]

    for item in items[:top_n]:
        lines.append(f"- {item.get('published') or 'unknown'} | [{item.get('title') or '(untitled)'}]({item.get('link') or source_cfg['homepage']})")
        summary = (item.get("summary") or "").strip()
        if summary:
            lines.append(f"  {summary[:280]}")

    return "\n".join(lines) + "\n"


def build_summary(source_cfg: Dict[str, Any], item_count: int, new_item_count: int, latest: str, note_path: Path, fetched_pages: Sequence[str], snapshot_dir: Path) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "---",
        "source: semrush realtime scrape",
        "title: Realtime Semrush Top 30 Monitor",
        f"scraped: {today}",
        "tags: semrush, realtime_scrape, archive_refresh, monitoring",
        "topic: seo_research",
        "intent: monitoring, article_discovery, source_selection",
        "role: researcher, seo, pinchy",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Realtime source monitors",
        "use_for: quick Semrush refresh status",
        "avoid_for: detailed article analysis without opening the source note",
        "---",
        "",
        "# Realtime Semrush Top 30 Monitor",
        "",
        f"- {source_cfg['name']}: ok | items={item_count} | new={new_item_count} | latest={latest or 'unknown'} | note=`{note_path.name}`",
        "",
        "## Source Mix",
        f"- Feed: {source_cfg.get('feed_urls', [''])[0]}",
        f"- Supplemental pages: {', '.join(fetched_pages) if fetched_pages else 'none'}",
        f"- Raw snapshots: `{snapshot_dir}`",
        "",
    ]
    return "\n".join(lines)


def update_state(state_path: Path, source_cfg: Dict[str, Any], items: Sequence[Dict[str, str]], latest: str, note_path: Path, snapshot_path: str, fetched_at: datetime) -> int:
    state = knowledge_ingest.load_json(state_path, {"generated_at": "", "sources": {}})
    previous = state.get("sources", {}).get(source_cfg["slug"], {})
    previous_seen = previous.get("seen_ids", [])
    current_ids = [knowledge_ingest.extract_item_id(item) for item in items]
    previous_seen_set = set(previous_seen)
    new_item_count = len([item_id for item_id in current_ids if item_id and item_id not in previous_seen_set])
    state.setdefault("sources", {})[source_cfg["slug"]] = {
        "name": source_cfg["name"],
        "kind": source_cfg.get("kind", "publication"),
        "last_success_at": fetched_at.isoformat(),
        "last_status": "ok",
        "latest_published": latest,
        "last_item_count": len(items),
        "last_new_item_count": new_item_count,
        "last_snapshot_path": snapshot_path,
        "last_note_path": str(note_path),
        "seen_ids": knowledge_ingest.merge_seen_ids(current_ids, previous_seen),
    }
    state["generated_at"] = fetched_at.isoformat()
    state["last_run_id"] = knowledge_ingest.build_run_id(fetched_at)
    knowledge_ingest.write_json(state_path, state)
    return new_item_count


def write_run_manifest(runs_dir: Path, payload: Dict[str, Any]) -> Path:
    runs_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = runs_dir / f"semrush-top30-{payload['run_id']}.json"
    knowledge_ingest.write_json(manifest_path, payload)
    knowledge_ingest.write_json(runs_dir / "latest.json", payload)
    return manifest_path


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
        "skills_root": str(skills_root),
        "db_path": str(db_path),
    }


def refresh_semrush_top30(args: argparse.Namespace) -> Dict[str, Any]:
    config_path = Path(args.config)
    output_dir = Path(args.output_dir)
    note_path = Path(args.note_path)
    summary_path = Path(args.summary_path)
    snapshot_dir = Path(args.snapshot_dir)
    runs_dir = Path(args.runs_dir)
    state_path = Path(args.state_path)
    skills_root = Path(args.skills_root)
    db_path = Path(args.db_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    note_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    source_cfg = load_source_cfg(config_path)
    fetched_at = datetime.now(timezone.utc)
    run_id = knowledge_ingest.build_run_id(fetched_at)

    feed_source, feed_title, snapshot_path, feed_items = fetch_feed_items(source_cfg, snapshot_dir, fetched_at)

    merged = dedupe_items(feed_items)
    fetched_pages: List[str] = []
    page_number = 1
    max_pages = max(args.max_pages, 1)

    while len(sort_items(merged)) < args.top and page_number <= max_pages:
        page_url = source_cfg["homepage"] if page_number == 1 else f"{source_cfg['homepage']}?page={page_number}"
        try:
            page_label, page_items = fetch_semrush_page(page_url, source_cfg, snapshot_dir, fetched_at, page_number)
            fetched_pages.append(page_label)
            merged = dedupe_items(list(merged) + page_items)
        except Exception:
            break
        page_number += 1

    sorted_items = sort_items(merged)
    selected_items = sorted_items[: args.top]
    latest = knowledge_ingest.latest_published(selected_items)
    new_item_count = update_state(state_path, source_cfg, selected_items, latest, note_path, snapshot_path, fetched_at)

    note_path.write_text(
        build_note(
            source_cfg=source_cfg,
            items=selected_items,
            latest=latest,
            new_item_count=new_item_count,
            feed_source=feed_source,
            feed_title=feed_title,
            snapshot_path=snapshot_path,
            fetched_pages=fetched_pages,
            top_n=args.top,
        )
    )
    summary_path.write_text(build_summary(source_cfg, len(selected_items), new_item_count, latest, note_path, fetched_pages, snapshot_dir))

    manifest: Dict[str, Any] = {
        "run_id": run_id,
        "generated_at": fetched_at.isoformat(),
        "source": SEM_RUSH_SLUG,
        "feed_source": feed_source,
        "feed_title": feed_title,
        "fetched_pages": fetched_pages,
        "item_count": len(selected_items),
        "new_item_count": new_item_count,
        "latest_published": latest,
        "note_path": str(note_path),
        "summary_path": str(summary_path),
        "snapshot_path": snapshot_path,
    }

    if args.build_db:
        manifest["build"] = build_db(skills_root, db_path)
        if manifest["build"]["returncode"] != 0:
            raise SystemExit(manifest["build"]["returncode"])

    manifest_path = write_run_manifest(runs_dir, manifest)
    manifest["manifest_path"] = str(manifest_path)
    return manifest


def print_manifest(manifest: Dict[str, Any]) -> None:
    print(f"Run ID: {manifest['run_id']}")
    print(f"Generated: {manifest['generated_at']}")
    print(f"Summary note: {manifest['summary_path']}")
    print(f"Manifest: {manifest['manifest_path']}")
    print("")
    print(
        f"- Semrush Blog: ok items={manifest['item_count']} new={manifest['new_item_count']} "
        f"latest={manifest['latest_published'] or 'unknown'} note={Path(manifest['note_path']).name}"
    )
    if manifest.get("fetched_pages"):
        print(f"- Supplemental pages: {', '.join(manifest['fetched_pages'])}")
    if manifest.get("build"):
        build = manifest["build"]
        print("")
        print(f"Build DB: rc={build['returncode']} db={build['db_path']}")
        if build["stdout"]:
            print(build["stdout"])
        if build["stderr"]:
            print(build["stderr"])


def main() -> int:
    args = parse_args()
    manifest = refresh_semrush_top30(args)
    if args.json:
        print(json.dumps(manifest, indent=2, ensure_ascii=True))
    else:
        print_manifest(manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
