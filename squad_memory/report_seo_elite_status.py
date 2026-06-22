#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import warnings
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple
from urllib.parse import urlparse


HOME = Path.home()
BASE = HOME / "squad_memory"
DB_PATH = Path(os.getenv("SEO_ELITE_STATUS_DB_PATH", str(BASE / "seo_elite_memory.db")))
SKILL_ROOT = Path(os.getenv("SEO_ELITE_SKILL_ROOT", str(HOME / ".codex" / "elite-skills" / "seo-elite")))
OPENCLAW_ROOT = HOME / ".openclaw"
OPENCLAW_WORKSPACE = OPENCLAW_ROOT / "workspace"
OPENCLAW_IMPORT_ROOT = OPENCLAW_WORKSPACE / "memory" / "imports" / "codex"
OPENCLAW_MAIN_DB = OPENCLAW_ROOT / "memory" / "main.sqlite"
OPENCLAW_SEO_DB = OPENCLAW_ROOT / "memory" / "seo.sqlite"
OPENCLAW_CRON_JOBS = OPENCLAW_ROOT / "cron" / "jobs.json"
OPENCLAW_IMPORT_INDEX = OPENCLAW_IMPORT_ROOT / "IMPORT_INDEX.md"
OPENCLAW_QUEUE_PATH = OPENCLAW_WORKSPACE / "squad" / "seo" / "automation" / "missions" / "execution" / "current-queue.md"
OPENCLAW_PLAN_PATH = OPENCLAW_WORKSPACE / "squad" / "seo" / "automation" / "hq" / "current-plan-trusted.md"
SQUAD_DB_PATH = Path(os.getenv("SEO_ELITE_SQUAD_DB_PATH", str(BASE / "squad_memory.db")))
BRIDGE_TARGET_ROOT = Path(
    os.getenv(
        "SEO_ELITE_BRIDGE_TARGET_ROOT",
        str(HOME / ".codex" / "skills" / "seo" / "memory" / "imports" / "seo-elite"),
    )
)
BRIDGE_MANIFEST_PATH = BRIDGE_TARGET_ROOT / "bridge-manifest.json"
BRIDGE_INDEX_PATH = BRIDGE_TARGET_ROOT / "IMPORT_INDEX.md"
STATUS_DIR = Path(os.getenv("SEO_ELITE_STATUS_DIR", str(SKILL_ROOT / "status")))
STATUS_PATH = Path(os.getenv("SEO_ELITE_STATUS_PATH", str(STATUS_DIR / "latest-status.md")))
STATUS_JSON_PATH = Path(os.getenv("SEO_ELITE_STATUS_JSON", str(STATUS_DIR / "latest-status.json")))
HISTORY_DIR = Path(os.getenv("SEO_ELITE_HISTORY_DIR", str(STATUS_DIR / "history")))
HISTORY_PATH = Path(os.getenv("SEO_ELITE_HISTORY_PATH", str(HISTORY_DIR / "timeline.jsonl")))
LIVE_MONITOR = SKILL_ROOT / "memory" / "live-knowledge-monitor.md"
ARCHIVE_MONITOR = SKILL_ROOT / "memory" / "archive" / "live-archive-monitor.md"
LIVE_ARTICLES = SKILL_ROOT / "memory" / "articles"
ARCHIVE_ARTICLES = SKILL_ROOT / "memory" / "archive" / "articles"
PRIMARY_DIR = SKILL_ROOT / "memory" / "primary"
LOG_DIR = Path(os.getenv("SEO_ELITE_LOG_DIR", str(BASE / "logs")))
LOCKS_DIR = Path(os.getenv("SEO_ELITE_LOCKS_DIR", str(BASE / "locks")))
TARGET_CHUNKS = int(os.getenv("SEO_ELITE_TARGET_CHUNKS", "30000"))
ITEM_PREFIX = "- "
HISTORY_LIMIT = 2000
FETCH_RE = re.compile(r"Fetched \((\d+)\) <GET ([^>]+)>")
PROGRESS_RE = re.compile(r"Harvest progress: (\d+)/(\d+)")
HARVESTED_RE = re.compile(r"Harvested article notes: (\d+)")
TOTAL_URLS_RE = re.compile(r"Total harvested URLs: (\d+)")
LOG_TS_RE = re.compile(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]")
OPENCLAW_IMPORT_COUNT_RE = re.compile(r"^- (?P<label>.+?): (?P<count>\d+)$")
QUEUE_METRIC_RE = re.compile(r"^- (?P<key>total|done|ready|at-risk|queued|blocked): `(?P<count>\d+)`$")
QUEUE_MISSION_RE = re.compile(r"^- id: `(?P<mission>[^`]+)`$")
QUEUE_FOCUS_RE = re.compile(r"^- task: (?P<label>.+?) \(`(?P<task_id>[^`]+)`\)$")

JOB_LOGS = {
    "live_sync": ("seo_elite_live_sync.log", 900),
    "primary_refresh": ("seo_elite_primary_sources.log", 900),
    "archive_backfill": ("seo_elite_archive_backfill.log", 1800),
    "article_harvest": ("seo_elite_article_harvest.log", 1800),
    "bulk_backfill": ("seo_elite_bulk_backfill.log", 2400),
    "bridge_sync": ("seo_elite_to_squad.log", 2400),
    "status_ping": ("seo_elite_status_ping.log", 600),
}


def now_local() -> datetime:
    return datetime.now().astimezone()


def iso_local(dt: datetime) -> str:
    return dt.astimezone().isoformat()


def safe_read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return default


def db_counts() -> Dict[str, int]:
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        chunks = int(cur.execute("select count(*) from chunks").fetchone()[0])
        paths = int(cur.execute("select count(distinct path) from chunks").fetchone()[0])
        primary_chunks = int(cur.execute("select count(*) from chunks where path like '%/memory/primary/%'").fetchone()[0])
        live_article_chunks = int(
            cur.execute(
                "select count(*) from chunks where path like '%/memory/articles/%' and path not like '%/memory/archive/articles/%'"
            ).fetchone()[0]
        )
        archive_article_chunks = int(cur.execute("select count(*) from chunks where path like '%/memory/archive/articles/%'").fetchone()[0])
        google_patent_chunks = int(cur.execute("select count(*) from chunks where path like '%google-patents/%'").fetchone()[0])
        google_search_central_chunks = int(cur.execute("select count(*) from chunks where path like '%google-search-central/%'").fetchone()[0])
        google_crawling_chunks = int(cur.execute("select count(*) from chunks where path like '%google-crawling-infrastructure/%'").fetchone()[0])
        return {
            "chunks": chunks,
            "paths": paths,
            "primary_chunks": primary_chunks,
            "live_article_chunks": live_article_chunks,
            "archive_article_chunks": archive_article_chunks,
            "google_patent_chunks": google_patent_chunks,
            "google_search_central_chunks": google_search_central_chunks,
            "google_crawling_chunks": google_crawling_chunks,
        }
    finally:
        conn.close()


def count_files(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob(pattern) if item.is_file())


def count_child_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_dir())


def safe_sqlite_scalar(path: Path, query: str) -> int | None:
    if not path.exists():
        return None
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=2.0)
    except sqlite3.Error:
        return None
    try:
        conn.execute("PRAGMA query_only = ON")
        row = conn.execute(query).fetchone()
        return int(row[0]) if row and row[0] is not None else 0
    except sqlite3.Error:
        return None
    finally:
        conn.close()


def load_bridge_status() -> Dict[str, Any]:
    manifest = safe_read_json(BRIDGE_MANIFEST_PATH, {})
    selected_files = manifest.get("selected_files", []) if isinstance(manifest.get("selected_files"), list) else []
    copied_files = manifest.get("copied", []) if isinstance(manifest.get("copied"), list) else []
    removed_files = manifest.get("removed", []) if isinstance(manifest.get("removed"), list) else []
    recent_article_files = int(manifest.get("recent_article_files") or 0)
    if not recent_article_files and selected_files:
        recent_article_files = sum(1 for item in selected_files if "/articles/" in str(item))

    import_chunks = safe_sqlite_scalar(
        SQUAD_DB_PATH,
        "select count(*) from chunks where path like 'seo/memory/imports/seo-elite/%'",
    )
    import_paths = safe_sqlite_scalar(
        SQUAD_DB_PATH,
        "select count(distinct path) from chunks where path like 'seo/memory/imports/seo-elite/%'",
    )
    squad_chunks = safe_sqlite_scalar(SQUAD_DB_PATH, "select count(*) from chunks")
    squad_paths = safe_sqlite_scalar(SQUAD_DB_PATH, "select count(distinct path) from chunks")

    return {
        "available": BRIDGE_MANIFEST_PATH.exists(),
        "generated_at": str(manifest.get("generated_at") or ""),
        "latest_source_update": str(manifest.get("latest_source_update") or ""),
        "selected_files": len(selected_files),
        "recent_article_files": recent_article_files,
        "copied_last_run": len(copied_files),
        "removed_last_run": len(removed_files),
        "target_root": str(BRIDGE_TARGET_ROOT),
        "manifest_updated_at": file_mtime(BRIDGE_MANIFEST_PATH),
        "index_updated_at": file_mtime(BRIDGE_INDEX_PATH),
        "log_updated_at": file_mtime(LOG_DIR / "seo_elite_to_squad.log"),
        "squad_db": {
            "path": str(SQUAD_DB_PATH),
            "chunks": squad_chunks,
            "paths": squad_paths,
            "db_size_bytes": SQUAD_DB_PATH.stat().st_size if SQUAD_DB_PATH.exists() else 0,
            "updated_at": file_mtime(SQUAD_DB_PATH),
        },
        "import_corpus": {
            "chunks": import_chunks,
            "paths": import_paths,
        },
    }


def article_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.rglob("*.md") if p.name != "INDEX.md")


def source_note_count(path: Path) -> int:
    if not path.exists():
        return 0
    total = 0
    for note in path.glob("live-source-*.md"):
        if note.name.startswith("live-source-canon") or note.name in {"live-source-canon.md", "live-source-cluster-report.md"}:
            continue
        total += 1
    return total


def file_mtime(path: Path) -> str:
    if not path.exists():
        return "missing"
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def file_mtime_dt(path: Path) -> datetime | None:
    if not path.exists():
        return None
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone()


def tail_lines(path: Path, limit: int = 6) -> List[str]:
    if not path.exists():
        return []
    lines = [line.rstrip() for line in path.read_text(errors="replace").splitlines() if line.strip()]
    return lines[-limit:]


def normalize_source_from_url(url: str) -> str:
    host = urlparse(url).netloc.lower().strip()
    if host.startswith("www."):
        host = host[4:]
    return host or "unknown"


def parse_log_timestamp(line: str) -> datetime | None:
    match = LOG_TS_RE.search(line)
    if not match:
        return None
    try:
        naive = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None
    return naive.astimezone()


def parse_runtime_activity() -> Dict[str, Any]:
    bulk_log = LOG_DIR / "seo_elite_bulk_backfill.log"
    live_log = LOG_DIR / "seo_elite_live_sync.log"
    now = now_local()
    lines = []
    if bulk_log.exists():
        lines.extend([line.rstrip() for line in bulk_log.read_text(errors="replace").splitlines() if line.strip()][-500:])
    latest_progress = {"current": 0, "total": 0, "percent": 0.0}
    latest_harvested = 0
    latest_total_urls = 0
    fetch_counts: Counter[str] = Counter()
    error_counts: Counter[str] = Counter()
    recent_fetch_counts: Counter[str] = Counter()
    recent_error_counts: Counter[str] = Counter()
    recent_fetch_total = 0
    recent_fetch_ok = 0
    recent_fetch_error = 0
    latest_fetch_source = ""
    latest_fetch_url = ""
    latest_fetch_code = 0
    latest_fetch_at = ""
    build_active = False
    ticker: List[str] = []

    for line in lines:
        if "Harvest progress:" in line:
            match = PROGRESS_RE.search(line)
            if match:
                current = int(match.group(1))
                total = int(match.group(2))
                latest_progress = {
                    "current": current,
                    "total": total,
                    "percent": round((current / total) * 100, 1) if total else 0.0,
                }
        elif line.startswith("Harvested article notes:"):
            match = HARVESTED_RE.search(line)
            if match:
                latest_harvested = int(match.group(1))
        elif line.startswith("Total harvested URLs:"):
            match = TOTAL_URLS_RE.search(line)
            if match:
                latest_total_urls = int(match.group(1))
        elif line.startswith("Build DB:") or line.startswith("Built index with"):
            build_active = True

        fetch_match = FETCH_RE.search(line)
        if fetch_match:
            code = int(fetch_match.group(1))
            url = fetch_match.group(2)
            source = normalize_source_from_url(url)
            ts = parse_log_timestamp(line)
            if code >= 400:
                error_counts[source] += 1
            else:
                fetch_counts[source] += 1
            if ts is not None:
                latest_fetch_source = source
                latest_fetch_url = url
                latest_fetch_code = code
                latest_fetch_at = ts.strftime("%Y-%m-%d %H:%M:%S %Z")
                age_seconds = (now - ts).total_seconds()
                if age_seconds <= 120:
                    recent_fetch_total += 1
                    if code >= 400:
                        recent_fetch_error += 1
                        recent_error_counts[source] += 1
                    else:
                        recent_fetch_ok += 1
                        recent_fetch_counts[source] += 1

    ticker.extend(tail_lines(bulk_log, 12))
    ticker.extend(tail_lines(live_log, 4))
    ticker = ticker[-14:]

    if latest_progress["total"] > 0:
        current_phase = "harvesting"
    elif recent_fetch_total > 0:
        current_phase = "discovering"
    elif build_active:
        current_phase = "building"
    else:
        current_phase = "idle"

    return {
        "bulk_progress": latest_progress,
        "latest_harvested_notes": latest_harvested,
        "latest_total_urls": latest_total_urls,
        "current_phase": current_phase,
        "recent_fetch_total": recent_fetch_total,
        "recent_fetch_ok": recent_fetch_ok,
        "recent_fetch_error": recent_fetch_error,
        "recent_fetch_window_seconds": 120,
        "recent_fetch_sources": [{"source": source, "count": count} for source, count in recent_fetch_counts.most_common(10)],
        "recent_error_sources": [{"source": source, "count": count} for source, count in recent_error_counts.most_common(10)],
        "latest_fetch_source": latest_fetch_source,
        "latest_fetch_url": latest_fetch_url,
        "latest_fetch_code": latest_fetch_code,
        "latest_fetch_at": latest_fetch_at,
        "top_fetch_sources": [{"source": source, "count": count} for source, count in fetch_counts.most_common(10)],
        "top_error_sources": [{"source": source, "count": count} for source, count in error_counts.most_common(10)],
        "ticker": ticker,
    }


def recent_notes(path: Path, limit: int = 5) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    notes = [note for note in path.rglob("*.md") if note.name != "INDEX.md"]
    notes.sort(key=lambda note: note.stat().st_mtime, reverse=True)
    rendered: List[Dict[str, str]] = []
    for note in notes[:limit]:
        relative = note.relative_to(SKILL_ROOT).as_posix()
        updated = datetime.fromtimestamp(note.stat().st_mtime).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
        rendered.append({"path": relative, "updated": updated})
    return rendered


def render_recent_notes(items: List[Dict[str, str]]) -> List[str]:
    return [f"- `{item['path']}` updated `{item['updated']}`" for item in items]


def iter_source_notes() -> Iterable[Tuple[str, Path]]:
    live_root = SKILL_ROOT / "memory"
    archive_root = SKILL_ROOT / "memory" / "archive"
    bulk_root = archive_root / "bulk"
    for note in live_root.glob("live-source-*.md"):
        if note.name.startswith("live-source-canon") or note.name in {"live-source-canon.md", "live-source-cluster-report.md"}:
            continue
        yield "live", note
    for note in archive_root.glob("live-source-*.md"):
        if note.name.startswith("live-source-canon") or note.name in {"live-source-canon.md", "live-source-cluster-report.md"}:
            continue
        yield "archive", note
    for note in bulk_root.glob("bulk-source-*.md"):
        yield "bulk", note


def parse_source_note(path: Path, layer: str) -> Dict[str, Any]:
    slug = path.stem.replace("live-source-", "").replace("bulk-source-", "")
    item_count = 0
    latest = "unknown"
    latest_value = ""
    for line in path.read_text(errors="replace").splitlines():
        if not line.startswith(ITEM_PREFIX):
            continue
        if " | [" not in line or "](" not in line:
            continue
        item_count += 1
        published = line[2:].split(" | ", 1)[0].strip()
        if published != "unknown" and (latest == "unknown" or published > latest_value):
            latest = published
            latest_value = published
    return {
        "slug": slug,
        "layer": layer,
        "path": path.relative_to(SKILL_ROOT).as_posix(),
        "item_count": item_count,
        "latest_published": latest,
        "updated_at": file_mtime(path),
    }


def source_snapshots(limit: int = 24) -> List[Dict[str, Any]]:
    snapshots = [parse_source_note(path, layer) for layer, path in iter_source_notes()]
    snapshots.sort(key=lambda item: item["updated_at"], reverse=True)
    return snapshots[:limit]


def article_source_counts(path: Path, layer: str) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    rows: List[Dict[str, Any]] = []
    for source_dir in sorted(p for p in path.iterdir() if p.is_dir()):
        count = sum(1 for note in source_dir.rglob("*.md") if note.name != "INDEX.md")
        if count == 0:
            continue
        latest_note = max((note for note in source_dir.rglob("*.md") if note.name != "INDEX.md"), key=lambda note: note.stat().st_mtime, default=None)
        rows.append(
            {
                "source": source_dir.name,
                "layer": layer,
                "article_count": count,
                "updated_at": file_mtime(latest_note) if latest_note else "missing",
            }
        )
    rows.sort(key=lambda item: item["article_count"], reverse=True)
    return rows


def load_openclaw_import_counts() -> Dict[str, int]:
    counts = {
        "seo_memory_notes": 0,
        "seo_router_files": 0,
        "dejan_pack_files": 0,
        "durable_notes": 0,
        "graph_hq_assets": 0,
        "graph_hq_docs": 0,
        "skill_packs": 0,
        "skill_docs": 0,
    }
    if OPENCLAW_IMPORT_INDEX.exists():
        for raw_line in OPENCLAW_IMPORT_INDEX.read_text(errors="replace").splitlines():
            match = OPENCLAW_IMPORT_COUNT_RE.match(raw_line.strip())
            if not match:
                continue
            label = match.group("label").strip().lower()
            value = int(match.group("count"))
            if label == "seo memory notes":
                counts["seo_memory_notes"] = value
            elif label == "seo router files":
                counts["seo_router_files"] = value
            elif label == "dejan pack files":
                counts["dejan_pack_files"] = value
            elif label == "durable memory notes":
                counts["durable_notes"] = value
            elif label == "graph + hq raw assets":
                counts["graph_hq_assets"] = value
            elif label == "graph + hq summary docs":
                counts["graph_hq_docs"] = value
            elif label == "squad skill packs":
                counts["skill_packs"] = value
            elif label == "squad skill docs":
                counts["skill_docs"] = value
        if any(counts.values()):
            return counts

    skill_root = OPENCLAW_IMPORT_ROOT / "skill-packs"
    graph_root = OPENCLAW_IMPORT_ROOT / "graph-hq"
    counts["skill_packs"] = count_child_dirs(skill_root)
    counts["skill_docs"] = count_files(skill_root, "*.md")
    counts["graph_hq_assets"] = count_files(graph_root, "*")
    counts["graph_hq_docs"] = count_files(graph_root, "*.md")
    counts["seo_memory_notes"] = count_files(OPENCLAW_IMPORT_ROOT / "seo-memory", "*.md")
    counts["seo_router_files"] = count_files(OPENCLAW_IMPORT_ROOT / "seo-router", "*.md")
    counts["dejan_pack_files"] = count_files(OPENCLAW_IMPORT_ROOT / "dejan-pack", "*.md")
    counts["durable_notes"] = count_files(OPENCLAW_IMPORT_ROOT / "durable", "*.md")
    return counts


def parse_current_queue() -> Dict[str, Any]:
    summary = {
        "mission": "missing",
        "current_focus": "missing",
        "total": 0,
        "done": 0,
        "ready": 0,
        "queued": 0,
        "blocked": 0,
        "at_risk": 0,
        "updated_at": file_mtime(OPENCLAW_QUEUE_PATH),
    }
    if not OPENCLAW_QUEUE_PATH.exists():
        return summary
    for raw_line in OPENCLAW_QUEUE_PATH.read_text(errors="replace").splitlines():
        line = raw_line.strip()
        metric_match = QUEUE_METRIC_RE.match(line)
        if metric_match:
            key = metric_match.group("key")
            count = int(metric_match.group("count"))
            if key == "at-risk":
                summary["at_risk"] = count
            else:
                summary[key] = count
            continue
        mission_match = QUEUE_MISSION_RE.match(line)
        if mission_match and summary["mission"] == "missing":
            summary["mission"] = mission_match.group("mission")
            continue
        focus_match = QUEUE_FOCUS_RE.match(line)
        if focus_match:
            summary["current_focus"] = focus_match.group("label")
    return summary


def parse_hq_plan() -> Dict[str, Any]:
    payload = {
        "updated_at": file_mtime(OPENCLAW_PLAN_PATH),
        "trusted_mode": "missing",
        "mission": "missing",
    }
    if not OPENCLAW_PLAN_PATH.exists():
        return payload
    for raw_line in OPENCLAW_PLAN_PATH.read_text(errors="replace").splitlines():
        line = raw_line.strip()
        if line.startswith("<!-- trusted-mode:"):
            payload["trusted_mode"] = line.replace("<!-- trusted-mode:", "").replace("-->", "").strip()
        elif line.startswith("- mission:"):
            match = re.search(r"\(`([^`]+)`\)", line)
            if match:
                payload["mission"] = match.group(1)
    return payload


def load_openclaw_jobs() -> Dict[str, Any]:
    state = {
        "enabled_jobs": 0,
        "seo_jobs": 0,
        "error_jobs": 0,
        "ok_jobs": 0,
        "updated_at": file_mtime(OPENCLAW_CRON_JOBS),
    }
    payload = safe_read_json(OPENCLAW_CRON_JOBS, {"jobs": []})
    jobs = payload.get("jobs", [])
    if not isinstance(jobs, list):
        return state
    enabled_jobs = [job for job in jobs if job.get("enabled")]
    seo_jobs = [job for job in enabled_jobs if str(job.get("id", "")).startswith("seo_")]
    state["enabled_jobs"] = len(enabled_jobs)
    state["seo_jobs"] = len(seo_jobs)
    state["error_jobs"] = sum(1 for job in seo_jobs if job.get("state", {}).get("lastStatus") == "error")
    state["ok_jobs"] = sum(1 for job in seo_jobs if job.get("state", {}).get("lastStatus") == "ok")
    return state


def openclaw_status() -> Dict[str, Any]:
    imports = load_openclaw_import_counts()
    queue = parse_current_queue()
    hq = parse_hq_plan()
    jobs = load_openclaw_jobs()
    main_chunks = safe_sqlite_scalar(OPENCLAW_MAIN_DB, "select count(*) from chunks")
    main_paths = safe_sqlite_scalar(OPENCLAW_MAIN_DB, "select count(distinct path) from chunks")
    seo_chunks = safe_sqlite_scalar(OPENCLAW_SEO_DB, "select count(*) from chunks")
    seo_paths = safe_sqlite_scalar(OPENCLAW_SEO_DB, "select count(distinct path) from chunks")
    return {
        "imports": imports,
        "main": {
            "chunks": main_chunks,
            "paths": main_paths,
            "db_size_bytes": OPENCLAW_MAIN_DB.stat().st_size if OPENCLAW_MAIN_DB.exists() else 0,
            "updated_at": file_mtime(OPENCLAW_MAIN_DB),
        },
        "seo": {
            "chunks": seo_chunks,
            "paths": seo_paths,
            "db_size_bytes": OPENCLAW_SEO_DB.stat().st_size if OPENCLAW_SEO_DB.exists() else 0,
            "updated_at": file_mtime(OPENCLAW_SEO_DB),
        },
        "jobs": jobs,
        "queue": queue,
        "hq": hq,
    }


def active_jobs() -> List[Dict[str, Any]]:
    now = now_local()
    rows: List[Dict[str, Any]] = []
    for key, (filename, threshold) in JOB_LOGS.items():
        path = LOG_DIR / filename
        mtime = file_mtime_dt(path)
        if mtime is None:
            rows.append({"job": key, "status": "missing", "updated_at": "missing", "age_seconds": None})
            continue
        age_seconds = int((now - mtime).total_seconds())
        rows.append(
            {
                "job": key,
                "status": "active" if age_seconds <= threshold else "idle",
                "updated_at": mtime.strftime("%Y-%m-%d %H:%M:%S %Z"),
                "age_seconds": age_seconds,
            }
        )
    sprint_lock = LOCKS_DIR / "seo_elite_2h_sprint.lock"
    if sprint_lock.exists():
        rows.append(
            {
                "job": "sprint_cycle",
                "status": "active",
                "updated_at": file_mtime(sprint_lock),
                "age_seconds": int((now - file_mtime_dt(sprint_lock)).total_seconds()) if file_mtime_dt(sprint_lock) else None,
            }
        )
    return rows


def collect_pending_snapshot(limit: int = 6000) -> Dict[str, Any]:
    state_path = BASE / "ingest" / "seo_elite" / "article_harvest" / "state.json"
    default = {"fetched_urls": {}, "failed_urls": {}}
    state = safe_read_json(state_path, default)
    fetched = state.get("fetched_urls", {})
    failed = state.get("failed_urls", {})
    try:
        warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL")
        spec = importlib.util.spec_from_file_location("harvest_seo_elite_articles", BASE / "harvest_seo_elite_articles.py")
        if spec is None or spec.loader is None:
            raise RuntimeError("harvest module unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        source_sets = [
            (SKILL_ROOT / "memory", SKILL_ROOT / "memory"),
            (SKILL_ROOT / "memory" / "archive", SKILL_ROOT / "memory" / "archive"),
        ]
        pending = module.collect_pending_candidates(source_sets, fetched, failed, limit)
    except Exception as exc:
        return {
            "pending_total": 0,
            "failed_total": len(failed),
            "fetched_total": len(fetched),
            "top_sources": [],
            "sample_urls": [],
            "error": f"{type(exc).__name__}: {exc}",
        }
    counts = Counter(source for source, _homepage, _item, _output in pending)
    sample_urls = [
        {
            "source": source,
            "published": item.get("published", "unknown"),
            "url": item.get("url", ""),
            "title": item.get("title", ""),
        }
        for source, _homepage, item, _output in pending[:12]
    ]
    return {
        "pending_total": len(pending),
        "failed_total": len(failed),
        "fetched_total": len(fetched),
        "top_sources": [{"source": source, "count": count} for source, count in counts.most_common(12)],
        "sample_urls": sample_urls,
    }


def build_status_payload() -> Dict[str, Any]:
    now = now_local()
    counts = db_counts()
    live_articles = article_count(LIVE_ARTICLES)
    archive_articles = article_count(ARCHIVE_ARTICLES)
    primary_notes = article_count(PRIMARY_DIR)
    live_sources = source_note_count(SKILL_ROOT / "memory")
    archive_sources = source_note_count(SKILL_ROOT / "memory" / "archive")
    progress = (counts["chunks"] / TARGET_CHUNKS) * 100 if TARGET_CHUNKS else 0
    pending = collect_pending_snapshot()
    runtime_activity = parse_runtime_activity()
    claw = openclaw_status()
    bridge = load_bridge_status()
    return {
        "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "updated_at_iso": iso_local(now),
        "goal": {
            "target_chunks": TARGET_CHUNKS,
            "progress_percent": round(progress, 1),
            "over_target": counts["chunks"] > TARGET_CHUNKS,
        },
        "db": {
            **counts,
            "db_path": str(DB_PATH),
            "db_size_bytes": DB_PATH.stat().st_size if DB_PATH.exists() else 0,
        },
        "coverage": {
            "live_source_notes": live_sources,
            "archive_source_notes": archive_sources,
            "primary_source_notes": primary_notes,
        },
        "articles": {
            "live_article_notes": live_articles,
            "archive_article_notes": archive_articles,
        },
        "monitors": {
            "live_monitor_updated": file_mtime(LIVE_MONITOR),
            "archive_monitor_updated": file_mtime(ARCHIVE_MONITOR),
        },
        "recent_knowledge": {
            "live_articles": recent_notes(LIVE_ARTICLES),
            "archive_articles": recent_notes(ARCHIVE_ARTICLES),
            "primary_notes": recent_notes(PRIMARY_DIR),
        },
        "logs": {
            "live_sync": tail_lines(LOG_DIR / "seo_elite_live_sync.log", 8),
            "primary_refresh": tail_lines(LOG_DIR / "seo_elite_primary_sources.log", 8),
            "archive_backfill": tail_lines(LOG_DIR / "seo_elite_archive_backfill.log", 8),
            "article_harvest": tail_lines(LOG_DIR / "seo_elite_article_harvest.log", 8),
            "bulk_backfill": tail_lines(LOG_DIR / "seo_elite_bulk_backfill.log", 12),
            "bridge_sync": tail_lines(LOG_DIR / "seo_elite_to_squad.log", 8),
        },
        "active_jobs": active_jobs(),
        "pending": pending,
        "activity": runtime_activity,
        "openclaw": claw,
        "bridge": bridge,
        "sources": {
            "snapshots": source_snapshots(),
            "live_article_sources": article_source_counts(LIVE_ARTICLES, "live")[:16],
            "archive_article_sources": article_source_counts(ARCHIVE_ARTICLES, "archive")[:16],
        },
    }


def render_status_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# SEO Elite Status",
        "",
        f"Updated: {payload['updated_at']}",
        "",
        "## Goal",
        f"- target chunks: `{payload['goal']['target_chunks']}`",
        f"- progress: `{payload['goal']['progress_percent']:.1f}%`",
        "",
        "## DB",
        f"- chunks: `{payload['db']['chunks']}`",
        f"- unique paths: `{payload['db']['paths']}`",
        "",
        "## Coverage",
        f"- live source notes: `{payload['coverage']['live_source_notes']}`",
        f"- archive source notes: `{payload['coverage']['archive_source_notes']}`",
        f"- primary source notes: `{payload['coverage']['primary_source_notes']}`",
        "",
        "## Articles",
        f"- live article notes: `{payload['articles']['live_article_notes']}`",
        f"- archive article notes: `{payload['articles']['archive_article_notes']}`",
        "",
        "## OpenClaw",
        f"- main chunks: `{payload['openclaw']['main']['chunks']}`",
        f"- main paths: `{payload['openclaw']['main']['paths']}`",
        f"- seo chunks: `{payload['openclaw']['seo']['chunks']}`",
        f"- seo paths: `{payload['openclaw']['seo']['paths']}`",
        f"- skill packs: `{payload['openclaw']['imports']['skill_packs']}`",
        f"- skill docs: `{payload['openclaw']['imports']['skill_docs']}`",
        f"- HQ mission: `{payload['openclaw']['hq']['mission']}`",
        (
            f"- HQ queue ready/done/blocked: `{payload['openclaw']['queue']['ready']}` / "
            f"`{payload['openclaw']['queue']['done']}` / `{payload['openclaw']['queue']['blocked']}`"
        ),
        "",
        "## Pending Queue",
        f"- pending total: `{payload['pending']['pending_total']}`",
        f"- fetched URLs: `{payload['pending']['fetched_total']}`",
        f"- failed URLs: `{payload['pending']['failed_total']}`",
        "",
        "## Squad Bridge",
        f"- bridge selected files: `{payload['bridge']['selected_files']}`",
        f"- bridge recent article files: `{payload['bridge']['recent_article_files']}`",
        f"- bridge imported chunks in squad db: `{payload['bridge']['import_corpus']['chunks']}`",
        f"- bridge imported paths in squad db: `{payload['bridge']['import_corpus']['paths']}`",
        f"- squad db chunks: `{payload['bridge']['squad_db']['chunks']}`",
        f"- bridge manifest updated: `{payload['bridge']['manifest_updated_at']}`",
        "",
        "## Monitors",
        f"- live monitor updated: `{payload['monitors']['live_monitor_updated']}`",
        f"- archive monitor updated: `{payload['monitors']['archive_monitor_updated']}`",
        "",
        "## Recent Knowledge",
        "- newest live article notes:",
        *render_recent_notes(payload["recent_knowledge"]["live_articles"]),
        "- newest archive article notes:",
        *render_recent_notes(payload["recent_knowledge"]["archive_articles"]),
        "- newest primary source notes:",
        *render_recent_notes(payload["recent_knowledge"]["primary_notes"]),
        "",
        "## Recent Logs",
        "- live sync:",
        *[f"  - {line}" for line in payload["logs"]["live_sync"]],
        "- primary-source refresh:",
        *[f"  - {line}" for line in payload["logs"]["primary_refresh"]],
        "- archive backfill:",
        *[f"  - {line}" for line in payload["logs"]["archive_backfill"]],
        "- article harvest:",
        *[f"  - {line}" for line in payload["logs"]["article_harvest"]],
        "- bulk backfill:",
        *[f"  - {line}" for line in payload["logs"]["bulk_backfill"]],
        "- bridge sync:",
        *[f"  - {line}" for line in payload["logs"]["bridge_sync"]],
        "",
    ]
    return "\n".join(lines) + "\n"


def append_history(payload: Dict[str, Any]) -> None:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "updated_at": payload["updated_at"],
        "updated_at_iso": payload["updated_at_iso"],
        "chunks": payload["db"]["chunks"],
        "paths": payload["db"]["paths"],
        "primary_chunks": payload["db"]["primary_chunks"],
        "live_article_chunks": payload["db"]["live_article_chunks"],
        "archive_article_chunks": payload["db"]["archive_article_chunks"],
        "live_article_notes": payload["articles"]["live_article_notes"],
        "archive_article_notes": payload["articles"]["archive_article_notes"],
        "primary_source_notes": payload["coverage"]["primary_source_notes"],
        "pending_total": payload["pending"]["pending_total"],
        "current_phase": payload["activity"]["current_phase"],
        "recent_fetch_total": payload["activity"]["recent_fetch_total"],
        "recent_fetch_ok": payload["activity"]["recent_fetch_ok"],
        "recent_fetch_error": payload["activity"]["recent_fetch_error"],
    }
    existing: List[str] = []
    if HISTORY_PATH.exists():
        existing = [line for line in HISTORY_PATH.read_text().splitlines() if line.strip()]
        if existing:
            try:
                last = json.loads(existing[-1])
                if all(
                    last.get(key) == entry.get(key)
                    for key in (
                        "chunks",
                        "paths",
                        "pending_total",
                        "live_article_notes",
                        "archive_article_notes",
                        "primary_source_notes",
                        "current_phase",
                        "recent_fetch_total",
                        "recent_fetch_ok",
                        "recent_fetch_error",
                    )
                ):
                    return
            except json.JSONDecodeError:
                pass
    existing.append(json.dumps(entry, ensure_ascii=True))
    if len(existing) > HISTORY_LIMIT:
        existing = existing[-HISTORY_LIMIT:]
    HISTORY_PATH.write_text("\n".join(existing) + "\n")


def write_outputs(payload: Dict[str, Any]) -> None:
    STATUS_DIR.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(render_status_markdown(payload))
    STATUS_JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")
    append_history(payload)


def send_notification(chunks: int, live_articles: int, archive_articles: int) -> None:
    # Keep scheduled status refreshes silent unless notifications are explicitly enabled.
    if os.getenv("SEO_ELITE_NOTIFY", "").strip().lower() not in {"1", "true", "yes", "on"}:
        return
    message = f"{chunks} chunks | live articles {live_articles} | archive articles {archive_articles}"
    script = f'display notification "{message}" with title "SEO Elite Status"'
    subprocess.run(["/usr/bin/osascript", "-e", script], check=False, capture_output=True)


def main() -> int:
    payload = build_status_payload()
    write_outputs(payload)
    send_notification(
        payload["db"]["chunks"],
        payload["articles"]["live_article_notes"],
        payload["articles"]["archive_article_notes"],
    )
    print(
        json.dumps(
            {
                "status_path": str(STATUS_PATH),
                "status_json_path": str(STATUS_JSON_PATH),
                "history_path": str(HISTORY_PATH),
                "chunks": payload["db"]["chunks"],
                "live_articles": payload["articles"]["live_article_notes"],
                "archive_articles": payload["articles"]["archive_article_notes"],
                "pending_total": payload["pending"]["pending_total"],
            },
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
