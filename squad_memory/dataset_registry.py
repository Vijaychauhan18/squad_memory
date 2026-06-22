#!/usr/bin/env python3
from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


HOME = Path.home()
BASE = HOME / "squad_memory"
REGISTRY_PATH = BASE / "dataset_registry.json"


def now_local_iso() -> str:
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"datasets": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"datasets": []}


def file_mtime(path: Path) -> str:
    if not path.exists():
        return ""
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def optional_path(value: Any) -> Optional[Path]:
    text = str(value or "").strip()
    if not text:
        return None
    return Path(text).expanduser()


def int_or_none(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def compute_delta(current: Any, previous: Any) -> int | None:
    current_value = int_or_none(current)
    previous_value = int_or_none(previous)
    if current_value is None or previous_value is None:
        return None
    return current_value - previous_value


def delta_direction(delta: int | None) -> str:
    if delta is None:
        return "unknown"
    if delta > 0:
        return "up"
    if delta < 0:
        return "down"
    return "flat"


def read_jsonl(path: Path, limit: int | None = None) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    try:
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except OSError:
        return []
    if limit is not None and limit > 0:
        lines = lines[-limit:]
    rows: List[Dict[str, Any]] = []
    for line in lines:
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            rows.append(payload)
    return rows


def safe_sqlite_counts(path: Optional[Path]) -> Dict[str, int | None]:
    if path is None or not path.exists() or not path.is_file():
        return {"chunks": None, "paths": None}
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=2.0)
    except sqlite3.Error:
        return {"chunks": None, "paths": None}
    try:
        conn.execute("PRAGMA query_only = ON")
        tables = {row[0] for row in conn.execute("select name from sqlite_master where type='table'")}
        if "chunks" not in tables:
            return {"chunks": None, "paths": None}
        row = conn.execute("select count(*), count(distinct path) from chunks").fetchone()
        if not row:
            return {"chunks": 0, "paths": 0}
        return {
            "chunks": int(row[0] or 0),
            "paths": int(row[1] or 0),
        }
    except sqlite3.Error:
        return {"chunks": None, "paths": None}
    finally:
        conn.close()


def load_registry() -> List[Dict[str, Any]]:
    payload = read_json(REGISTRY_PATH)
    items = payload.get("datasets", [])
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict) and item.get("id")]


def get_dataset_entry(dataset_id: str) -> Dict[str, Any] | None:
    for entry in load_registry():
        if entry.get("id") == dataset_id:
            return entry
    return None


def history_path_for_entry(entry: Dict[str, Any]) -> Optional[Path]:
    return optional_path(entry.get("history_path"))


def status_json_path_for_entry(entry: Dict[str, Any]) -> Optional[Path]:
    return optional_path(entry.get("status_json_path"))


def history_rows_for_entry(entry: Dict[str, Any], limit: int | None = None) -> List[Dict[str, Any]]:
    history_path = history_path_for_entry(entry)
    if history_path is None:
        return []
    rows = read_jsonl(history_path, limit=limit)
    enriched: List[Dict[str, Any]] = []
    previous: Dict[str, Any] | None = None
    for row in rows:
        item = dict(row)
        item["delta_chunks_from_previous"] = compute_delta(item.get("chunks"), previous.get("chunks") if previous else None)
        item["delta_paths_from_previous"] = compute_delta(item.get("paths"), previous.get("paths") if previous else None)
        item["delta_direction"] = delta_direction(item["delta_chunks_from_previous"])
        enriched.append(item)
        previous = item
    return enriched


def build_dataset_summary(entry: Dict[str, Any]) -> Dict[str, Any]:
    db_path = optional_path(entry.get("db_path"))
    counts = safe_sqlite_counts(db_path)
    dashboard_urls = entry.get("dashboard_urls", [])
    relations = entry.get("relations", [])
    history_path = history_path_for_entry(entry)
    status_json_path = status_json_path_for_entry(entry)
    chunks = counts["chunks"]
    paths = counts["paths"]
    return {
        "id": str(entry.get("id", "")),
        "label": str(entry.get("label", entry.get("id", ""))),
        "path": str(db_path) if db_path else "",
        "path_name": db_path.name if db_path else "",
        "query_adapter": str(entry.get("query_adapter", "counts_only")),
        "status": "ready" if db_path and db_path.exists() else "missing",
        "chunks": chunks,
        "paths": paths,
        "db_size_bytes": db_path.stat().st_size if db_path and db_path.exists() else 0,
        "updated_at": file_mtime(db_path) if db_path else "",
        "updated_at_iso": now_local_iso(),
        "purpose": str(entry.get("purpose", "")),
        "owner": str(entry.get("owner", "")),
        "update_source": str(entry.get("update_source", "")),
        "refresh_command": str(entry.get("refresh_command", "")),
        "health_command": str(entry.get("health_command", "")),
        "expected_count_band": str(entry.get("expected_count_band", "")),
        "history_path": str(history_path) if history_path else "",
        "history_available": bool(history_path and history_path.exists()),
        "status_json_path": str(status_json_path) if status_json_path else "",
        "status_json_available": bool(status_json_path and status_json_path.exists()),
        "dashboard_urls": [str(url) for url in dashboard_urls if isinstance(url, str)],
        "relations": relations if isinstance(relations, list) else [],
    }


def build_registry_payload() -> Dict[str, Any]:
    items = [build_dataset_summary(entry) for entry in load_registry()]
    by_id = {item["id"]: item for item in items}
    for item in items:
        related_items: List[Dict[str, Any]] = []
        for relation in item.get("relations", []):
            if not isinstance(relation, dict):
                continue
            target = by_id.get(str(relation.get("target", "")))
            if not target:
                continue
            related_items.append(
                {
                    "type": str(relation.get("type", "related_to")),
                    "id": target["id"],
                    "label": target["label"],
                    "chunks": target["chunks"],
                    "paths": target["paths"],
                    "status": target["status"],
                    "path_name": target["path_name"],
                }
            )
        item["related_datasets"] = related_items
    return {
        "updated_at_iso": now_local_iso(),
        "items": items,
    }


def get_dataset_summary(dataset_id: str) -> Dict[str, Any] | None:
    payload = build_registry_payload()
    for item in payload["items"]:
        if item["id"] == dataset_id:
            return item
    return None


def build_dataset_history(dataset_id: str, limit: int = 12) -> Dict[str, Any] | None:
    entry = get_dataset_entry(dataset_id)
    if entry is None:
        return None
    history_rows = history_rows_for_entry(entry, limit=limit)
    summary = build_dataset_summary(entry)
    history_path = history_path_for_entry(entry)
    return {
        "dataset": summary,
        "history_path": str(history_path) if history_path else "",
        "history_available": bool(history_path and history_path.exists()),
        "history_entry_count": len(history_rows),
        "history": list(reversed(history_rows)),
    }


def build_dataset_delta(dataset_id: str) -> Dict[str, Any] | None:
    entry = get_dataset_entry(dataset_id)
    if entry is None:
        return None
    summary = build_dataset_summary(entry)
    history_rows = history_rows_for_entry(entry)
    history_path = history_path_for_entry(entry)
    latest_history = history_rows[-1] if history_rows else None
    current_chunks = int_or_none(summary.get("chunks"))
    current_paths = int_or_none(summary.get("paths"))

    baseline: Dict[str, Any] | None = None
    baseline_source = "none"
    current_matches_latest = False
    if latest_history is not None:
        latest_chunks = int_or_none(latest_history.get("chunks"))
        latest_paths = int_or_none(latest_history.get("paths"))
        current_matches_latest = latest_chunks == current_chunks and latest_paths == current_paths
        if current_matches_latest and len(history_rows) >= 2:
            baseline = history_rows[-2]
            baseline_source = "previous_history_entry"
        else:
            baseline = latest_history
            baseline_source = "latest_history_entry"

    baseline_chunks = int_or_none(baseline.get("chunks")) if baseline else None
    baseline_paths = int_or_none(baseline.get("paths")) if baseline else None
    delta_chunks = compute_delta(current_chunks, baseline_chunks)
    delta_paths = compute_delta(current_paths, baseline_paths)

    return {
        "dataset": summary,
        "history_path": str(history_path) if history_path else "",
        "history_available": bool(history_path and history_path.exists()),
        "history_entry_count": len(history_rows),
        "current_matches_latest_history": current_matches_latest,
        "baseline_source": baseline_source,
        "baseline_entry": baseline,
        "latest_history_entry": latest_history,
        "current": {
            "chunks": current_chunks,
            "paths": current_paths,
            "updated_at": summary.get("updated_at", ""),
        },
        "delta": {
            "chunks": delta_chunks,
            "paths": delta_paths,
            "direction": delta_direction(delta_chunks),
        },
        "status": "ready" if baseline is not None else "unavailable",
    }
