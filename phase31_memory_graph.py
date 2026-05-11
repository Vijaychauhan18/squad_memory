#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sqlite3
import time
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_INGEST_ROOT = BASE / "ingest"
DEFAULT_PHASE21_STATUS = DEFAULT_INGEST_ROOT / "phase21" / "control_plane_status.json"
DEFAULT_PHASE31_DIR = DEFAULT_INGEST_ROOT / "phase31"
DEFAULT_DB = BASE / "seo_elite_memory.db"
DEFAULT_PACKS = BASE / "task_packs.json"
DEFAULT_UI_DIR = BASE / "memory_graph_ui"

DOMAIN_COLORS = {
    "brain": "#f2f4ff",
    "seo": "#6ef2c5",
    "writer": "#ff9a62",
    "marketing": "#ffd166",
    "charles": "#87a8ff",
    "support": "#6ed0ff",
    "developer": "#d27bff",
    "qa": "#ff7db7",
    "core": "#b7becf",
}

KIND_COLORS = {
    "brain": "#f2f4ff",
    "timeline": "#8f9cff",
    "queue": "#f7b267",
    "source": "#6ed0ff",
    "stale_source": "#ff8c69",
    "publication": "#83a8ff",
    "skill": "#7fd1ff",
    "memory_bank": "#98a7ff",
    "pack": "#ffd166",
    "topic": "#7cf29c",
    "note": "#d0d6e8",
    "chunk": "#9fb3ff",
    "outcome": "#ff7db7",
    "episode": "#ff9fe5",
    "run": "#a4ff7d",
    "blocker": "#ff8a5b",
    "workspace": "#6fe0ff",
    "workspace_item": "#8ec7ff",
    "alert": "#ff5f87",
}

DOMAIN_LABELS = {
    "seo": "SEO",
    "writer": "Writer",
    "marketing": "Marketing",
    "charles": "Charles",
    "support": "Support",
    "developer": "Developer",
    "qa": "QA",
    "core": "Core",
}

SKILL_LABELS = {
    "orchestrator-pinchy": "Pinchy",
    "seo": "Coral",
    "seo-coral": "Coral",
    "writer": "Plankton",
    "writer-plankton": "Plankton",
    "marketing": "Current",
    "marketing-current": "Current",
    "charles": "Charles",
    "support-anemone": "Anemone",
    "support": "Support",
    "developer": "Chitin",
    "developer-chitin": "Chitin",
    "qa": "Reef",
    "qa-reef": "Reef",
    "devops": "Tide",
    "devops-tide": "Tide",
    "reviewer": "Barnacle",
    "reviewer-barnacle": "Barnacle",
    "researcher": "Kelp",
    "researcher-kelp": "Kelp",
    "operations": "Urchin",
    "operations-urchin": "Urchin",
    "finance": "Krill",
    "finance-krill": "Krill",
    "emily": "Emily",
    "dejan-ai-reverse-engineering": "DEJAN",
    "ahrefs": "Ahrefs",
}

ROLE_ALIAS_TO_SKILL = {
    "pinchy": "orchestrator-pinchy",
    "coral": "seo",
    "plankton": "writer",
    "current": "marketing",
    "charles": "charles",
    "anemone": "support-anemone",
    "chitin": "developer",
    "reef": "qa",
    "tide": "devops",
    "barnacle": "reviewer",
    "kelp": "researcher",
    "urchin": "operations",
    "krill": "finance",
    "emily": "emily",
    "dejan": "dejan-ai-reverse-engineering",
}

SKILL_DOMAIN_OVERRIDES = {
    "ahrefs": "seo",
    "seo": "seo",
    "seo-coral": "seo",
    "programmatic-seo": "seo",
    "dejan-ai-reverse-engineering": "seo",
    "writer": "writer",
    "writer-plankton": "writer",
    "researcher": "writer",
    "researcher-kelp": "writer",
    "marketing": "marketing",
    "marketing-current": "marketing",
    "charles": "charles",
    "support": "support",
    "support-anemone": "support",
    "finance": "support",
    "developer": "developer",
    "developer-chitin": "developer",
    "reviewer": "developer",
    "reviewer-barnacle": "developer",
    "devops": "developer",
    "devops-tide": "developer",
    "qa": "qa",
    "qa-reef": "qa",
    "operations": "core",
    "operations-urchin": "core",
    "orchestrator-pinchy": "core",
    "multi-agent-reef": "core",
    "emily": "core",
}

DOMAIN_RING = {
    "seo": (-260.0, -40.0, 0.0),
    "writer": (-150.0, 105.0, 220.0),
    "marketing": (110.0, 70.0, 260.0),
    "charles": (255.0, 10.0, 120.0),
    "support": (235.0, -70.0, -140.0),
    "developer": (20.0, -110.0, -265.0),
    "qa": (-185.0, -85.0, -210.0),
    "core": (0.0, 180.0, 0.0),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and serve the 3D squad memory graph.")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    build = subparsers.add_parser("build", help="Export the current squad graph payload and report.")
    add_shared_args(build)
    build.add_argument("--json", action="store_true", help="Emit JSON instead of text output")

    serve = subparsers.add_parser("serve", help="Serve the local 3D graph viewer with a live API.")
    add_shared_args(serve)
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8765)
    serve.add_argument("--ui-dir", default=str(DEFAULT_UI_DIR))
    serve.add_argument("--write-snapshot", action="store_true", help="Refresh the phase31 snapshot on each API request")

    return parser.parse_args()


def add_shared_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--phase31-dir", default=str(DEFAULT_PHASE31_DIR))
    parser.add_argument("--phase21-status", default=str(DEFAULT_PHASE21_STATUS))
    parser.add_argument("--ingest-root", default=str(DEFAULT_INGEST_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--packs-file", default=str(DEFAULT_PACKS))
    parser.add_argument("--outcomes-limit", type=int, default=12)
    parser.add_argument("--alerts-limit", type=int, default=8)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def parse_json_list(raw: Any) -> List[str]:
    if raw in (None, "", b""):
        return []
    if isinstance(raw, list):
        return [str(item) for item in raw if item not in (None, "")]
    try:
        payload = json.loads(str(raw))
    except json.JSONDecodeError:
        return []
    if not isinstance(payload, list):
        return []
    return [str(item) for item in payload if item not in (None, "")]


def slugify(value: str) -> str:
    cleaned = []
    prev_dash = False
    for char in value.lower():
        if char.isalnum():
            cleaned.append(char)
            prev_dash = False
        else:
            if not prev_dash:
                cleaned.append("-")
            prev_dash = True
    return "".join(cleaned).strip("-") or "item"


def title_from_slug(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").strip().title()


def domain_from_path(path: str) -> str:
    if not path:
        return "core"
    head = path.split("/", 1)[0]
    if head in {"seo", "writer", "marketing", "charles", "developer", "qa"}:
        return head
    if head.startswith("support"):
        return "support"
    return SKILL_DOMAIN_OVERRIDES.get(head, "core")


def domain_for_skill(skill: str) -> str:
    return SKILL_DOMAIN_OVERRIDES.get(skill, domain_from_path(skill))


def display_label_for_skill(skill: str) -> str:
    return SKILL_LABELS.get(skill, title_from_slug(skill))


def stable_offset(key: str, spread: float, vertical: float) -> Tuple[float, float, float]:
    digest = hashlib.sha1(key.encode("utf-8")).digest()
    a = int.from_bytes(digest[:4], "big") / 2**32
    b = int.from_bytes(digest[4:8], "big") / 2**32
    c = int.from_bytes(digest[8:12], "big") / 2**32
    angle = a * math.tau
    radius = spread * (0.45 + b * 0.55)
    return (
        math.cos(angle) * radius,
        (c - 0.5) * vertical,
        math.sin(angle) * radius,
    )


def anchored_position(domain: str, key: str, spread: float = 90.0, vertical: float = 120.0) -> Dict[str, float]:
    base_x, base_y, base_z = DOMAIN_RING.get(domain, DOMAIN_RING["core"])
    dx, dy, dz = stable_offset(key, spread, vertical)
    return {
        "x": round(base_x + dx, 2),
        "y": round(base_y + dy, 2),
        "z": round(base_z + dz, 2),
    }


def color_for(kind: str, domain: str, status: str = "") -> str:
    if kind == "source" and status == "stale":
        return KIND_COLORS["stale_source"]
    if kind in KIND_COLORS:
        return KIND_COLORS[kind]
    return DOMAIN_COLORS.get(domain, DOMAIN_COLORS["core"])


def skill_color(domain: str) -> str:
    return DOMAIN_COLORS.get(domain, KIND_COLORS["skill"])


def rgba(hex_color: str, alpha: float) -> str:
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        return f"rgba(180, 188, 204, {alpha:.3f})"
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha:.3f})"


def load_task_packs(path: Path) -> List[Dict[str, Any]]:
    payload = load_json(path, {"packs": []})
    packs = payload.get("packs", [])
    return packs if isinstance(packs, list) else []


def fetch_recent_outcomes(db_path: Path, limit: int) -> List[Dict[str, Any]]:
    if not db_path.exists():
        return []
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            """
            SELECT
              o.id,
              o.ts,
              o.query,
              o.pack_id,
              o.primary_skill,
              o.status,
              o.revision_count,
              o.user_rating,
              s.overall_score,
              s.verdict,
              s.scoring_mode
            FROM task_outcomes o
            LEFT JOIN task_result_scorecards s
              ON s.outcome_id = o.id
            ORDER BY o.id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        con.close()


def fetch_top_learned(con: sqlite3.Connection, table: str, key: str, limit: int) -> List[Dict[str, Any]]:
    try:
        rows = con.execute(
            f"SELECT {key}, score, avg_overall_score, exposure_count FROM {table} ORDER BY score DESC LIMIT ?",
            (limit,),
        ).fetchall()
    except sqlite3.OperationalError:
        return []
    return [
        {
            key: row[0],
            "score": float(row[1] or 0.0),
            "avg_overall_score": float(row[2] or 0.0),
            "exposure_count": int(row[3] or 0),
        }
        for row in rows
    ]


def fetch_learning_snapshot(db_path: Path) -> Dict[str, List[Dict[str, Any]]]:
    if not db_path.exists():
        return {"skills": [], "packs": []}
    con = sqlite3.connect(str(db_path))
    try:
        return {
            "skills": fetch_top_learned(con, "learned_result_skill_priors", "skill", 18),
            "packs": fetch_top_learned(con, "learned_result_pack_priors", "pack_id", 18),
        }
    finally:
        con.close()


def fetch_chunk_snapshot(db_path: Path) -> Dict[str, Any]:
    if not db_path.exists():
        return {"total_chunks": 0, "total_paths": 0, "domains": {}}
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        try:
            total_chunks = int(con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0])
            total_paths = int(con.execute("SELECT COUNT(DISTINCT path) FROM chunks").fetchone()[0])
            rows = con.execute(
                """
                SELECT
                  CASE
                    WHEN path LIKE 'support/%' THEN 'support'
                    WHEN instr(path, '/') > 0 THEN substr(path, 1, instr(path, '/') - 1)
                    ELSE 'core'
                  END AS bucket,
                  COUNT(*) AS chunk_count,
                  COUNT(DISTINCT path) AS path_count
                FROM chunks
                GROUP BY bucket
                """
            ).fetchall()
        except sqlite3.OperationalError:
            return {"total_chunks": 0, "total_paths": 0, "domains": {}}
        domains: Dict[str, Dict[str, int]] = {}
        for row in rows:
            bucket = str(row["bucket"])
            domain = domain_from_path(f"{bucket}/placeholder.md")
            entry = domains.setdefault(domain, {"chunk_count": 0, "path_count": 0})
            entry["chunk_count"] += int(row["chunk_count"] or 0)
            entry["path_count"] += int(row["path_count"] or 0)
        return {"total_chunks": total_chunks, "total_paths": total_paths, "domains": domains}
    finally:
        con.close()


def fetch_recent_events(db_path: Path, limit: int = 18, since_id: int = 0) -> List[Dict[str, Any]]:
    if not db_path.exists():
        return []
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        tables = {str(row["name"]) for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if "events" not in tables:
            return []
        if since_id > 0:
            rows = con.execute(
                """
                SELECT id, ts, event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
                FROM events
                WHERE id > ?
                ORDER BY id ASC
                LIMIT ?
                """,
                (since_id, limit),
            ).fetchall()
        else:
            rows = con.execute(
                """
                SELECT id, ts, event_type, event_group, source, status, query, role, pack_id, skill, path, metadata_json
                FROM events
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            rows = list(reversed(rows))
        events = []
        for row in rows:
            try:
                metadata = json.loads(str(row["metadata_json"] or "{}"))
            except json.JSONDecodeError:
                metadata = {}
            events.append(
                {
                    "id": int(row["id"]),
                    "ts": str(row["ts"] or ""),
                    "event_type": str(row["event_type"] or ""),
                    "event_group": str(row["event_group"] or ""),
                    "source": str(row["source"] or ""),
                    "status": str(row["status"] or ""),
                    "query": str(row["query"] or ""),
                    "role": str(row["role"] or ""),
                    "pack_id": str(row["pack_id"] or ""),
                    "skill": str(row["skill"] or ""),
                    "path": str(row["path"] or ""),
                    "metadata": metadata if isinstance(metadata, dict) else {},
                }
            )
        return events
    finally:
        con.close()


def fetch_recent_episodes(db_path: Path, limit: int = 12) -> List[Dict[str, Any]]:
    if not db_path.exists():
        return []
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        tables = {str(row["name"]) for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if "episodes" not in tables:
            return []
        rows = con.execute(
            """
            SELECT id, ts_start, ts_end, episode_key, episode_type, title, status, role, pack_id,
                   primary_skill, query, event_count, summary_text, metadata_json
            FROM episodes
            ORDER BY ts_end DESC, id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        episodes: List[Dict[str, Any]] = []
        for row in rows:
            try:
                metadata = json.loads(str(row["metadata_json"] or "{}"))
            except json.JSONDecodeError:
                metadata = {}
            episodes.append(
                {
                    "id": int(row["id"]),
                    "ts_start": str(row["ts_start"] or ""),
                    "ts_end": str(row["ts_end"] or ""),
                    "episode_key": str(row["episode_key"] or ""),
                    "episode_type": str(row["episode_type"] or ""),
                    "title": str(row["title"] or ""),
                    "status": str(row["status"] or ""),
                    "role": str(row["role"] or ""),
                    "pack_id": str(row["pack_id"] or ""),
                    "primary_skill": str(row["primary_skill"] or ""),
                    "query": str(row["query"] or ""),
                    "event_count": int(row["event_count"] or 0),
                    "summary_text": str(row["summary_text"] or ""),
                    "metadata": metadata if isinstance(metadata, dict) else {},
                }
            )
        return episodes
    finally:
        con.close()


def fetch_recent_pack_runs(db_path: Path, limit: int = 12) -> Dict[str, Any]:
    if not db_path.exists():
        return {"runs": [], "open_blockers": 0, "active_runs": 0, "blocked_runs": 0}
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        tables = {str(row["name"]) for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if "pack_runs" not in tables:
            return {"runs": [], "open_blockers": 0, "active_runs": 0, "blocked_runs": 0}
        active_runs = int(con.execute("SELECT COUNT(*) FROM pack_runs WHERE status = 'active'").fetchone()[0])
        blocked_runs = int(con.execute("SELECT COUNT(*) FROM pack_runs WHERE status = 'blocked'").fetchone()[0])
        open_blockers = 0
        if "pack_run_blockers" in tables:
            open_blockers = int(con.execute("SELECT COUNT(*) FROM pack_run_blockers WHERE status = 'open'").fetchone()[0])
        rows = con.execute(
            """
            SELECT id, ts_started, ts_updated, ts_completed, query, role, pack_id, pack_name, primary_skill,
                   supporting_skills_json, status, current_step_seq, step_count, blocker_count, handoff_count, notes, metadata_json
            FROM pack_runs
            ORDER BY ts_updated DESC, id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        runs: List[Dict[str, Any]] = []
        for row in rows:
            try:
                supporting_skills = json.loads(str(row["supporting_skills_json"] or "[]"))
            except json.JSONDecodeError:
                supporting_skills = []
            try:
                metadata = json.loads(str(row["metadata_json"] or "{}"))
            except json.JSONDecodeError:
                metadata = {}
            runs.append(
                {
                    "id": int(row["id"]),
                    "ts_started": str(row["ts_started"] or ""),
                    "ts_updated": str(row["ts_updated"] or ""),
                    "ts_completed": str(row["ts_completed"] or ""),
                    "query": str(row["query"] or ""),
                    "role": str(row["role"] or ""),
                    "pack_id": str(row["pack_id"] or ""),
                    "pack_name": str(row["pack_name"] or ""),
                    "primary_skill": str(row["primary_skill"] or ""),
                    "supporting_skills": supporting_skills if isinstance(supporting_skills, list) else [],
                    "status": str(row["status"] or ""),
                    "current_step_seq": int(row["current_step_seq"] or 0),
                    "step_count": int(row["step_count"] or 0),
                    "blocker_count": int(row["blocker_count"] or 0),
                    "handoff_count": int(row["handoff_count"] or 0),
                    "notes": str(row["notes"] or ""),
                    "metadata": metadata if isinstance(metadata, dict) else {},
                }
            )
        return {
            "runs": runs,
            "open_blockers": open_blockers,
            "active_runs": active_runs,
            "blocked_runs": blocked_runs,
        }
    finally:
        con.close()


def fetch_workspace_snapshot(db_path: Path, limit_contexts: int = 8, limit_items: int = 24) -> Dict[str, Any]:
    if not db_path.exists():
        return {"active_contexts": 0, "active_items": 0, "contexts": [], "items": []}
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        tables = {str(row["name"]) for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if "workspace_contexts" not in tables or "workspace_context_items" not in tables:
            return {"active_contexts": 0, "active_items": 0, "contexts": [], "items": []}
        active_contexts = int(con.execute("SELECT COUNT(*) FROM workspace_contexts WHERE status = 'active'").fetchone()[0])
        active_items = int(
            con.execute(
                """
                SELECT COUNT(*)
                FROM workspace_context_items wci
                JOIN workspace_contexts wc ON wc.id = wci.context_id
                WHERE wc.status = 'active'
                """
            ).fetchone()[0]
        )
        context_rows = con.execute(
            """
            SELECT id, ts_created, ts_updated, ts_last_used, name, scope_key, root_path, role, pack_id, notes
            FROM workspace_contexts
            WHERE status = 'active'
            ORDER BY COALESCE(ts_last_used, ts_updated) DESC, id DESC
            LIMIT ?
            """,
            (limit_contexts,),
        ).fetchall()
        contexts = [
            {
                "id": int(row["id"]),
                "ts_created": str(row["ts_created"] or ""),
                "ts_updated": str(row["ts_updated"] or ""),
                "ts_last_used": str(row["ts_last_used"] or ""),
                "name": str(row["name"] or ""),
                "scope_key": str(row["scope_key"] or ""),
                "root_path": str(row["root_path"] or ""),
                "role": str(row["role"] or ""),
                "pack_id": str(row["pack_id"] or ""),
                "notes": str(row["notes"] or ""),
            }
            for row in context_rows
        ]
        context_ids = [item["id"] for item in contexts]
        if not context_ids:
            return {"active_contexts": active_contexts, "active_items": active_items, "contexts": [], "items": []}
        placeholders = ", ".join("?" for _ in context_ids)
        item_rows = con.execute(
            f"""
            SELECT id, context_id, path, rel_path, item_type, title, token_count
            FROM workspace_context_items
            WHERE context_id IN ({placeholders})
            ORDER BY token_count DESC, id ASC
            LIMIT ?
            """,
            tuple(context_ids + [limit_items]),
        ).fetchall()
        items = [
            {
                "id": int(row["id"]),
                "context_id": int(row["context_id"]),
                "path": str(row["path"] or ""),
                "rel_path": str(row["rel_path"] or ""),
                "item_type": str(row["item_type"] or "file"),
                "title": str(row["title"] or ""),
                "token_count": int(row["token_count"] or 0),
            }
            for row in item_rows
        ]
        return {
            "active_contexts": active_contexts,
            "active_items": active_items,
            "contexts": contexts,
            "items": items,
        }
    finally:
        con.close()


def fetch_graph_pro_chunks(db_path: Path, limit: int = 1200) -> List[Dict[str, Any]]:
    if not db_path.exists():
        return []
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    try:
        columns = {str(row["name"]) for row in con.execute("PRAGMA table_info(chunks)").fetchall()}
        if not columns:
            return []
        if "chunk_id" in columns:
            rows = con.execute(
                """
                SELECT
                  chunk_id,
                  path,
                  skill,
                  file_type,
                  heading,
                  text,
                  section_kind,
                  source,
                  published_on,
                  freshness,
                  topics_json,
                  intents_json,
                  use_for_json,
                  avoid_for_json,
                  confidence,
                  tags_json,
                  roles_json,
                  bundles_json,
                  is_canonical,
                  canonical_group
                FROM chunks
                ORDER BY is_canonical DESC, freshness DESC, LENGTH(text) DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        else:
            rows = con.execute(
                """
                SELECT
                  printf('%s::%s::%s', path, COALESCE(heading, ''), COALESCE(chunk_index, 0)) AS chunk_id,
                  path,
                  '' AS skill,
                  '' AS file_type,
                  COALESCE(heading, '') AS heading,
                  COALESCE(content, '') AS text,
                  'section' AS section_kind,
                  '' AS source,
                  '' AS published_on,
                  0.0 AS freshness,
                  '[]' AS topics_json,
                  '[]' AS intents_json,
                  '[]' AS use_for_json,
                  '[]' AS avoid_for_json,
                  '' AS confidence,
                  '[]' AS tags_json,
                  '[]' AS roles_json,
                  '[]' AS bundles_json,
                  0 AS is_canonical,
                  '' AS canonical_group
                FROM chunks
                ORDER BY path, chunk_index
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return [dict(row) for row in rows]
    finally:
        con.close()


def load_evidence_topics(ingest_root: Path) -> List[Dict[str, Any]]:
    topics: List[Dict[str, Any]] = []
    for ledger_path in sorted(ingest_root.glob("phase*/**/*evidence_ledger.json")):
        payload = load_json(ledger_path, {})
        ledger_topics = payload.get("topics", {})
        if not isinstance(ledger_topics, dict):
            continue
        for topic_name, info in ledger_topics.items():
            if not isinstance(info, dict):
                continue
            primary_path = str(info.get("primary_path", ""))
            domain = domain_from_path(primary_path)
            topics.append(
                {
                    "ledger": ledger_path.name,
                    "topic": str(info.get("topic") or topic_name),
                    "domain": domain,
                    "primary_path": primary_path,
                    "confidence_score": float(info.get("confidence_score") or 0.0),
                    "confidence_label": str(info.get("confidence_label", "")),
                    "freshness_label": str(info.get("freshness_label", "")),
                    "evidence_count": int(info.get("evidence_count") or len(info.get("evidence_paths", []) or [])),
                    "source_count": int(info.get("source_count") or len(info.get("distinct_sources", []) or [])),
                    "distinct_sources": [str(item) for item in info.get("distinct_sources", [])],
                    "squad_action": str(info.get("squad_action", "")),
                    "consensus": [str(item) for item in info.get("consensus", [])[:2]],
                }
            )
    return topics


def dedupe_preserve(values: Iterable[str]) -> List[str]:
    result: List[str] = []
    seen = set()
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def infer_speaker_skill(handoff: str, participants: List[str], primary_skill: str) -> str:
    prefix = handoff.split(":", 1)[0].strip().lower()
    if prefix in ROLE_ALIAS_TO_SKILL:
        skill = ROLE_ALIAS_TO_SKILL[prefix]
        if skill in participants or skill == primary_skill:
            return skill
    for skill in participants:
        label = display_label_for_skill(skill).lower()
        if prefix in {skill.lower(), label}:
            return skill
    return primary_skill


def build_meeting_from_pack(
    pack: Dict[str, Any],
    *,
    pack_id: str,
    primary_skill: str,
    query: str,
    status: str,
    verdict: str,
    revision_count: int,
    outcome_id: Optional[int] = None,
    user_rating: float = 0.0,
    title: str = "",
    scenario_id: str = "",
) -> Dict[str, Any]:
    participant_skills = dedupe_preserve([primary_skill] + [str(item) for item in pack.get("supporting_skills", []) if item])
    if len(participant_skills) < 2:
        participant_skills = dedupe_preserve(participant_skills + ["orchestrator-pinchy"])

    participants = [
        {
            "skill": skill,
            "label": display_label_for_skill(skill),
            "domain": domain_for_skill(skill),
            "color": skill_color(domain_for_skill(skill)),
            "role": "lead" if skill == primary_skill else "support",
        }
        for skill in participant_skills
    ]

    turns: List[Dict[str, Any]] = []
    description = str(pack.get("description", "")).strip()
    if description:
        turns.append(
            {
                "speaker": primary_skill,
                "listener": "room",
                "message": description,
                "tone": "kickoff",
            }
        )

    handoffs = [str(item) for item in pack.get("handoffs", []) if item]
    for handoff in handoffs[:4]:
        speaker = infer_speaker_skill(handoff, participant_skills, primary_skill)
        speaker_index = participant_skills.index(speaker) if speaker in participant_skills else 0
        listener = participant_skills[(speaker_index + 1) % len(participant_skills)] if len(participant_skills) > 1 else "room"
        if ":" in handoff:
            _, message = handoff.split(":", 1)
            message = message.strip()
        else:
            message = handoff.strip()
        turns.append(
            {
                "speaker": speaker,
                "listener": listener,
                "message": message,
                "tone": "handoff",
            }
        )

    checklist = [str(item) for item in pack.get("checklist", []) if item]
    for index, item in enumerate(checklist[:3]):
        speaker = participant_skills[index % len(participant_skills)]
        listener = participant_skills[(index + 1) % len(participant_skills)] if len(participant_skills) > 1 else "room"
        turns.append(
            {
                "speaker": speaker,
                "listener": listener,
                "message": item,
                "tone": "working",
            }
        )

    if outcome_id is None:
        closing = str(pack.get("deliverables", ["Technical SEO resolution plan ready for rollout."])[0])
        closing = f"Live war room: {closing}."
    else:
        closing = (
            f"Status: {status}. Verdict: {verdict or 'n/a'}. "
            f"{revision_count} revision{'s' if revision_count != 1 else ''}."
        )
    turns.append(
        {
            "speaker": primary_skill,
            "listener": "room",
            "message": closing,
            "tone": "wrap",
        }
    )

    return {
        "id": scenario_id or (f"meeting-{outcome_id}" if outcome_id is not None else f"meeting-{pack_id}-live"),
        "outcome_id": outcome_id,
        "pack_id": pack_id,
        "title": title or str(pack.get("name") or title_from_slug(pack_id) or "Agent Meeting"),
        "query": query,
        "status": status,
        "verdict": verdict,
        "primary_skill": primary_skill,
        "participants": participants,
        "turns": turns[:9],
        "agenda": checklist[:5],
        "revision_count": revision_count,
        "user_rating": user_rating,
        "synthetic": outcome_id is None,
    }


def build_meeting_scenarios(packs: List[Dict[str, Any]], outcomes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pack_map = {str(pack.get("id", "")): pack for pack in packs}
    scenarios: List[Dict[str, Any]] = []

    for outcome in outcomes:
        pack_id = str(outcome.get("pack_id") or "")
        pack = pack_map.get(pack_id, {})
        primary_skill = str(outcome.get("primary_skill") or pack.get("primary_skill") or "orchestrator-pinchy")
        scenarios.append(
            build_meeting_from_pack(
                pack,
                pack_id=pack_id,
                primary_skill=primary_skill,
                query=str(outcome.get("query") or ""),
                status=str(outcome.get("status") or "accepted"),
                verdict=str(outcome.get("verdict") or ""),
                revision_count=int(outcome.get("revision_count") or 0),
                outcome_id=int(outcome["id"]),
                user_rating=float(outcome.get("user_rating") or 0.0),
            )
        )

    technical_pack = pack_map.get("technical_seo_war_room")
    if technical_pack and not any(str(item.get("pack_id")) == "technical_seo_war_room" for item in scenarios):
        scenarios.insert(
            0,
            build_meeting_from_pack(
                technical_pack,
                pack_id="technical_seo_war_room",
                primary_skill=str(technical_pack.get("primary_skill") or "seo"),
                query="Traffic slipped after a site release. Diagnose crawlability, indexation, canonicals, rendering, Core Web Vitals, and internal link flow before rollout.",
                status="active",
                verdict="war_room",
                revision_count=0,
                title="Technical SEO War Room",
                scenario_id="meeting-technical-seo-war-room",
            ),
        )

    return scenarios


def build_graph_payload(
    control_status_path: Path,
    ingest_root: Path,
    db_path: Path,
    packs_file: Path,
    outcomes_limit: int,
    alerts_limit: int,
) -> Dict[str, Any]:
    control = load_json(control_status_path, {})
    packs = load_task_packs(packs_file)
    outcomes = fetch_recent_outcomes(db_path, outcomes_limit)
    learned = fetch_learning_snapshot(db_path)
    chunk_snapshot = fetch_chunk_snapshot(db_path)
    recent_events = fetch_recent_events(db_path, limit=16)
    recent_episodes = fetch_recent_episodes(db_path, limit=10)
    run_snapshot = fetch_recent_pack_runs(db_path, limit=10)
    workspace_snapshot = fetch_workspace_snapshot(db_path, limit_contexts=6, limit_items=18)
    topics = load_evidence_topics(ingest_root)
    meetings = build_meeting_scenarios(packs, outcomes)

    nodes: Dict[str, Dict[str, Any]] = {}
    links: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    source_nodes: Dict[str, str] = {}
    note_nodes: Dict[str, str] = {}

    def add_node(node_id: str, **attrs: Any) -> None:
        existing = nodes.get(node_id)
        if existing is None:
            nodes[node_id] = {"id": node_id, **attrs}
            return
        for key, value in attrs.items():
            if value is None:
                continue
            if key in {"metrics", "details"} and isinstance(value, dict):
                merged = dict(existing.get(key, {}))
                merged.update(value)
                existing[key] = merged
            elif key == "tags" and isinstance(value, list):
                merged_tags = list(dict.fromkeys(existing.get(key, []) + value))
                existing[key] = merged_tags
            elif key not in existing or existing.get(key) in ("", None) or existing.get(key) == [] or existing.get(key) == {}:
                existing[key] = value

    def add_link(source: str, target: str, kind: str, weight: float = 1.0, color: str = "") -> None:
        link_key = (source, target, kind)
        if link_key in links:
            links[link_key]["weight"] = max(float(links[link_key]["weight"]), float(weight))
            return
        links[link_key] = {
            "source": source,
            "target": target,
            "kind": kind,
            "weight": round(float(weight), 3),
            "color": color,
        }

    add_node(
        "brain",
        label="Squad Brain",
        kind="brain",
        domain="brain",
        color=color_for("brain", "brain"),
        size=34,
        status="live",
        tags=["squad", "memory", "graph"],
        details={
            "generated_at": control.get("generated_at", now_iso()),
            "alerts": len(control.get("alerts", [])),
        },
        **{"x": 0.0, "y": 0.0, "z": 0.0},
    )

    add_node(
        "memory-bank:global",
        label="Memory Core",
        kind="memory_bank",
        domain="brain",
        color=color_for("memory_bank", "brain"),
        size=14 + min(14, chunk_snapshot["total_paths"] / 45.0),
        status="hot",
        tags=["chunks", "memory", "canon"],
        metrics={
            "chunks": int(chunk_snapshot["total_chunks"]),
            "files": int(chunk_snapshot["total_paths"]),
        },
        details={
            "total_chunks": int(chunk_snapshot["total_chunks"]),
            "total_paths": int(chunk_snapshot["total_paths"]),
            "domains": chunk_snapshot.get("domains", {}),
        },
        x=0.0,
        y=135.0,
        z=0.0,
    )
    add_link("brain", "memory-bank:global", "memory_bank", 2.0, rgba(color_for("memory_bank", "brain"), 0.34))

    if workspace_snapshot["active_contexts"]:
        add_node(
            "workspace:active",
            label="Workspace Context",
            kind="workspace",
            domain="core",
            color=color_for("workspace", "core"),
            size=12 + min(10, workspace_snapshot["active_contexts"] + workspace_snapshot["active_items"] / 28.0),
            status="active",
            tags=["workspace", "runtime", "transient"],
            metrics={
                "contexts": int(workspace_snapshot["active_contexts"]),
                "items": int(workspace_snapshot["active_items"]),
            },
            details={"contexts": workspace_snapshot["contexts"][:6]},
            x=0.0,
            y=225.0,
            z=110.0,
        )
        add_link("brain", "workspace:active", "workspace", 1.7, rgba(color_for("workspace", "core"), 0.28))
        for context in workspace_snapshot["contexts"][:6]:
            node_id = f"workspace-context:{context['id']}"
            role = str(context.get("role") or "")
            domain = domain_for_skill(ROLE_ALIAS_TO_SKILL.get(role.lower(), "")) if role else "core"
            if domain not in DOMAIN_RING:
                domain = "core"
            add_node(
                node_id,
                label=context["name"],
                kind="workspace",
                domain=domain,
                color=color_for("workspace", domain),
                size=8.5,
                status="active",
                tags=["workspace", role or "global", context.get("pack_id") or "runtime"],
                details=context,
                **anchored_position(domain, node_id, spread=110.0, vertical=95.0),
            )
            add_link("workspace:active", node_id, "workspace_context", 1.0, rgba(color_for("workspace", domain), 0.22))
            if context.get("pack_id"):
                add_link(node_id, f"pack:{context['pack_id']}", "workspace_pack", 0.75, rgba(color_for("workspace", domain), 0.18))
        for item in workspace_snapshot["items"][:18]:
            node_id = f"workspace-item:{item['id']}"
            add_node(
                node_id,
                label=item["title"] or item["rel_path"] or Path(item["path"]).name,
                kind="workspace_item",
                domain="core",
                color=color_for("workspace_item", "core"),
                size=4.4 + min(2.6, item["token_count"] / 180.0),
                status="active",
                tags=["workspace", item["item_type"]],
                details=item,
                **anchored_position("core", node_id, spread=140.0, vertical=125.0),
            )
            add_link(f"workspace-context:{item['context_id']}", node_id, "workspace_item", 0.62, rgba(color_for("workspace_item", "core"), 0.16))

    queue_map = control.get("queues", {}) if isinstance(control.get("queues"), dict) else {}
    source_map = control.get("sources", {}) if isinstance(control.get("sources"), dict) else {}
    alerts = list(control.get("alerts", []))[:alerts_limit] if isinstance(control.get("alerts"), list) else []

    domain_keys = set(source_map.keys())
    domain_keys.update(key for key in queue_map.keys() if key not in {"writer_marketing", "developer_qa"})
    domain_keys.update(topic["domain"] for topic in topics if topic["domain"] != "core")
    domain_keys.update(domain_for_skill(item["skill"]) for item in learned["skills"] if item.get("skill"))
    ordered_domains = ["seo", "writer", "marketing", "charles", "support", "developer", "qa"]
    for domain in ordered_domains:
        if domain not in domain_keys and domain not in source_map:
            continue
        queue_counts = queue_map.get(domain, {}).get("counts", {})
        source_summary = source_map.get(domain, {})
        position = DOMAIN_RING[domain]
        size = 20 + min(10, int(queue_counts.get("hold", 0)) + int(source_summary.get("source_count", 0)) // 2)
        add_node(
            f"domain:{domain}",
            label=DOMAIN_LABELS.get(domain, title_from_slug(domain)),
            kind="domain",
            domain=domain,
            color=DOMAIN_COLORS[domain],
            size=size,
            status="live",
            metrics={
                "queue_hold": int(queue_counts.get("hold", 0)),
                "queue_approved": int(queue_counts.get("approve", 0)),
                "queue_rejected": int(queue_counts.get("reject", 0)),
                "source_count": int(source_summary.get("source_count", 0)),
                "stale_sources": int(source_summary.get("stale_source_count", 0)),
            },
            details={"queue": queue_counts, "sources": source_summary},
            x=position[0],
            y=position[1],
            z=position[2],
        )
        add_link("brain", f"domain:{domain}", "domain", 3.0, rgba(DOMAIN_COLORS[domain], 0.34))

    for domain, stats in chunk_snapshot.get("domains", {}).items():
        if domain not in DOMAIN_RING:
            continue
        node_id = f"memory-bank:{domain}"
        pos = anchored_position(domain, node_id, spread=58.0, vertical=70.0)
        chunk_count = int(stats.get("chunk_count", 0))
        path_count = int(stats.get("path_count", 0))
        add_node(
            node_id,
            label=f"{DOMAIN_LABELS.get(domain, title_from_slug(domain))} Memory",
            kind="memory_bank",
            domain=domain,
            color=color_for("memory_bank", domain),
            size=10 + min(12, chunk_count / 120.0 + path_count / 10.0),
            status="hot" if chunk_count else "cold",
            tags=["chunks", "files", domain],
            metrics={
                "chunks": chunk_count,
                "files": path_count,
            },
            details={
                "chunk_count": chunk_count,
                "path_count": path_count,
            },
            **pos,
        )
        anchor = f"domain:{domain}" if f"domain:{domain}" in nodes else "brain"
        add_link(anchor, node_id, "domain_memory", 1.7, rgba(DOMAIN_COLORS.get(domain, DOMAIN_COLORS["core"]), 0.28))
        add_link("memory-bank:global", node_id, "memory_bank", 1.3, rgba(color_for("memory_bank", domain), 0.24))

    for queue_key, queue_info in queue_map.items():
        label = str(queue_info.get("label", title_from_slug(queue_key)))
        counts = queue_info.get("counts", {})
        hold_count = int(counts.get("hold", 0))
        if queue_key == "writer_marketing":
            domain = "marketing"
            anchor = "domain:marketing"
        elif queue_key == "developer_qa":
            domain = "developer"
            anchor = "domain:developer"
        else:
            domain = queue_key
            anchor = f"domain:{domain}"
        node_id = f"queue:{queue_key}"
        pos = anchored_position(domain if domain in DOMAIN_RING else "core", node_id, spread=75.0, vertical=70.0)
        add_node(
            node_id,
            label=f"{label} Queue",
            kind="queue",
            domain=domain,
            color=color_for("queue", domain),
            size=11 + min(12, hold_count),
            status="hold" if hold_count else "clear",
            metrics=counts,
            details={
                "items_total": int(queue_info.get("items_total", 0)),
                "held_items": queue_info.get("held_items", [])[:5],
                "approved_items": queue_info.get("approved_items", [])[:5],
            },
            **pos,
        )
        add_link(anchor if anchor in nodes else "brain", node_id, "queue", 1.8, rgba(color_for("queue", domain), 0.32))

    for domain, summary in source_map.items():
        node_id = f"source-summary:{domain}"
        stale_count = int(summary.get("stale_source_count", 0))
        pos = anchored_position(domain if domain in DOMAIN_RING else "core", node_id, spread=95.0, vertical=85.0)
        add_node(
            node_id,
            label=f"{summary.get('label', DOMAIN_LABELS.get(domain, title_from_slug(domain)))} Sources",
            kind="source",
            domain=domain,
            color=color_for("source", domain, "stale" if stale_count else ""),
            size=10 + min(10, int(summary.get("source_count", 0)) + stale_count),
            status="stale" if stale_count else "healthy",
            metrics={
                "source_count": int(summary.get("source_count", 0)),
                "ok_source_count": int(summary.get("ok_source_count", 0)),
                "error_source_count": int(summary.get("error_source_count", 0)),
                "stale_source_count": stale_count,
                "new_items_total": int(summary.get("new_items_total", 0)),
            },
            details=summary,
            **pos,
        )
        add_link(f"domain:{domain}" if f"domain:{domain}" in nodes else "brain", node_id, "source", 1.6, rgba(DOMAIN_COLORS.get(domain, DOMAIN_COLORS["core"]), 0.28))
        for stale in summary.get("stale_sources", [])[:4]:
            stale_id = f"stale-source:{domain}:{slugify(str(stale.get('slug', stale.get('name', 'source'))))}"
            stale_pos = anchored_position(domain, stale_id, spread=115.0, vertical=90.0)
            add_node(
                stale_id,
                label=str(stale.get("name") or stale.get("slug") or "Stale Source"),
                kind="stale_source",
                domain=domain,
                color=color_for("source", domain, "stale"),
                size=8 + min(4, int(stale.get("age_days", 0)) // 90),
                status="stale",
                metrics={"age_days": int(stale.get("age_days", 0))},
                details=stale,
                **stale_pos,
            )
            add_link(node_id, stale_id, "stale_source", 1.0, rgba(color_for("source", domain, "stale"), 0.4))

    learning_evaluation = ((control.get("learning") or {}).get("evaluation") or {}) if isinstance(control.get("learning"), dict) else {}

    for pack in packs:
        pack_id = str(pack.get("id", ""))
        if not pack_id:
            continue
        primary_skill = str(pack.get("primary_skill", ""))
        domain = domain_for_skill(primary_skill)
        learned_pack = next((item for item in learned["packs"] if item.get("pack_id") == pack_id), {})
        pack_score = float(learned_pack.get("score", 0.0))
        node_id = f"pack:{pack_id}"
        pos = anchored_position(domain, node_id, spread=65.0, vertical=95.0)
        add_node(
            node_id,
            label=str(pack.get("name", title_from_slug(pack_id))),
            kind="pack",
            domain=domain,
            color=color_for("pack", domain),
            size=12 + min(10, max(0.0, pack_score) * 6.0),
            status="active",
            metrics={
                "learned_score": round(pack_score, 3),
                "roles": len(pack.get("roles", [])),
                "deliverables": len(pack.get("deliverables", [])),
            },
            details={
                "description": pack.get("description", ""),
                "primary_skill": primary_skill,
                "supporting_skills": pack.get("supporting_skills", []),
                "checklist": pack.get("checklist", [])[:5],
            },
            tags=[str(item) for item in pack.get("intents", [])],
            **pos,
        )
        add_link(f"domain:{domain}" if f"domain:{domain}" in nodes else "brain", node_id, "pack", 1.5, rgba(DOMAIN_COLORS.get(domain, DOMAIN_COLORS["core"]), 0.3))

        related_skills = [primary_skill] + [str(item) for item in pack.get("supporting_skills", [])]
        for idx, skill in enumerate(item for item in related_skills if item):
            skill_domain = domain_for_skill(skill)
            skill_id = f"skill:{skill}"
            learned_skill = next((entry for entry in learned["skills"] if entry.get("skill") == skill), {})
            skill_score = float(learned_skill.get("score", 0.0))
            pos_skill = anchored_position(skill_domain, skill_id, spread=110.0 + idx * 6, vertical=110.0)
            add_node(
                skill_id,
                label=display_label_for_skill(skill),
                kind="skill",
                domain=skill_domain,
                color=skill_color(skill_domain),
                size=9 + min(9, max(0.0, skill_score) * 5.5),
                status="linked",
                metrics={"learned_score": round(skill_score, 3)},
                details={"skill": skill, "domain": skill_domain},
                **pos_skill,
            )
            add_link(f"domain:{skill_domain}" if f"domain:{skill_domain}" in nodes else "brain", skill_id, "skill_domain", 1.0, rgba(skill_color(skill_domain), 0.22))
            add_link(node_id, skill_id, "primary_skill" if skill == primary_skill else "support_skill", 1.4 if skill == primary_skill else 1.0, rgba(skill_color(skill_domain), 0.3))

    for topic in topics:
        domain = topic["domain"]
        topic_slug = slugify(topic["topic"])
        topic_id = f"topic:{domain}:{topic_slug}"
        confidence = float(topic.get("confidence_score", 0.0))
        evidence_count = int(topic.get("evidence_count", 0))
        pos = anchored_position(domain, topic_id, spread=135.0, vertical=120.0)
        add_node(
            topic_id,
            label=title_from_slug(topic["topic"]),
            kind="topic",
            domain=domain,
            color=color_for("topic", domain),
            size=8 + min(10, evidence_count + confidence * 4.0),
            status=str(topic.get("confidence_label", "")),
            metrics={
                "confidence_score": round(confidence, 3),
                "evidence_count": evidence_count,
                "source_count": int(topic.get("source_count", 0)),
            },
            details={
                "freshness_label": topic.get("freshness_label", ""),
                "consensus": topic.get("consensus", []),
                "squad_action": topic.get("squad_action", ""),
            },
            **pos,
        )
        add_link(f"domain:{domain}" if f"domain:{domain}" in nodes else "brain", topic_id, "topic", 1.1, rgba(color_for("topic", domain), 0.24))

        primary_path = topic.get("primary_path", "")
        if primary_path:
            note_id = note_nodes.get(primary_path)
            if note_id is None:
                note_id = f"note:{slugify(primary_path)}"
                note_nodes[primary_path] = note_id
                note_domain = domain_from_path(primary_path)
                note_pos = anchored_position(note_domain, note_id, spread=160.0, vertical=130.0)
                add_node(
                    note_id,
                    label=title_from_slug(Path(primary_path).stem),
                    kind="note",
                    domain=note_domain,
                    color=color_for("note", note_domain),
                    size=6.5,
                    status="primary",
                    metrics={"path": primary_path},
                    details={"path": primary_path},
                    **note_pos,
                )
            add_link(topic_id, note_id, "primary_note", 0.9, rgba(color_for("note", domain), 0.2))

        for source_name in topic.get("distinct_sources", [])[:4]:
            source_slug = slugify(source_name)
            source_node_id = source_nodes.get(source_name)
            if source_node_id is None:
                source_node_id = f"signal-source:{source_slug}"
                source_nodes[source_name] = source_node_id
                source_pos = anchored_position(domain, source_node_id, spread=180.0, vertical=145.0)
                add_node(
                    source_node_id,
                    label=source_name,
                    kind="source",
                    domain=domain,
                    color=color_for("source", domain),
                    size=7.5,
                    status="signal",
                    metrics={"evidence_domains": 1},
                    details={"source": source_name},
                    **source_pos,
                )
            add_link(source_node_id, topic_id, "evidence_source", 0.75, rgba(color_for("source", domain), 0.18))

    for outcome in outcomes:
        outcome_id = f"outcome:{outcome['id']}"
        pack_domain = domain_for_skill(str(outcome.get("primary_skill", "")))
        score = float(outcome.get("overall_score") or outcome.get("user_rating") or 0.0)
        pos = anchored_position(pack_domain, outcome_id, spread=55.0, vertical=80.0)
        add_node(
            outcome_id,
            label=f"Task #{outcome['id']}",
            kind="outcome",
            domain=pack_domain,
            color=color_for("outcome", pack_domain),
            size=9 + min(8, score),
            status=str(outcome.get("status", "")),
            metrics={
                "overall_score": round(float(outcome.get("overall_score") or 0.0), 2),
                "revision_count": int(outcome.get("revision_count") or 0),
                "user_rating": float(outcome.get("user_rating") or 0.0),
            },
            details={
                "ts": outcome.get("ts", ""),
                "query": outcome.get("query", ""),
                "pack_id": outcome.get("pack_id", ""),
                "primary_skill": outcome.get("primary_skill", ""),
                "verdict": outcome.get("verdict", ""),
                "scoring_mode": outcome.get("scoring_mode", ""),
            },
            **pos,
        )
        add_link("brain", outcome_id, "outcome", 0.8, rgba(color_for("outcome", pack_domain), 0.18))
        if outcome.get("pack_id"):
            add_link(outcome_id, f"pack:{outcome['pack_id']}", "used_pack", 1.2, rgba(color_for("pack", pack_domain), 0.24))
        if outcome.get("primary_skill"):
            add_link(outcome_id, f"skill:{outcome['primary_skill']}", "used_skill", 1.1, rgba(skill_color(pack_domain), 0.24))

    for episode in recent_episodes:
        episode_id = f"episode:{episode['id']}"
        episode_domain = domain_for_skill(str(episode.get("primary_skill") or ""))
        if episode_domain not in DOMAIN_RING:
            episode_domain = "core"
        pos = anchored_position(episode_domain, episode_id, spread=92.0, vertical=72.0)
        add_node(
            episode_id,
            label=str(episode.get("title") or f"Episode {episode['id']}"),
            kind="episode",
            domain=episode_domain,
            color=color_for("episode", episode_domain),
            size=8 + min(8, int(episode.get("event_count", 0)) / 2.0),
            status=str(episode.get("status") or "live"),
            metrics={"event_count": int(episode.get("event_count", 0))},
            details={
                "ts_start": episode.get("ts_start", ""),
                "ts_end": episode.get("ts_end", ""),
                "episode_type": episode.get("episode_type", ""),
                "summary_text": episode.get("summary_text", ""),
                "query": episode.get("query", ""),
            },
            **pos,
        )
        add_link("brain", episode_id, "episode", 0.95, rgba(color_for("episode", episode_domain), 0.22))
        if episode.get("pack_id"):
            add_link(episode_id, f"pack:{episode['pack_id']}", "episode_pack", 1.0, rgba(color_for("pack", episode_domain), 0.22))
        if episode.get("primary_skill"):
            add_link(
                episode_id,
                f"skill:{episode['primary_skill']}",
                "episode_skill",
                0.95,
                rgba(skill_color(episode_domain), 0.22),
            )

    for run in run_snapshot["runs"]:
        run_id = f"run:{run['id']}"
        run_domain = domain_for_skill(str(run.get("primary_skill") or ""))
        if run_domain not in DOMAIN_RING:
            run_domain = "core"
        pos = anchored_position(run_domain, run_id, spread=78.0, vertical=58.0)
        add_node(
            run_id,
            label=f"Run #{run['id']}",
            kind="run",
            domain=run_domain,
            color=color_for("run", run_domain),
            size=8 + min(8, 1 + int(run.get("handoff_count", 0)) + int(run.get("blocker_count", 0))),
            status=str(run.get("status") or "active"),
            metrics={
                "current_step_seq": int(run.get("current_step_seq", 0)),
                "step_count": int(run.get("step_count", 0)),
                "blocker_count": int(run.get("blocker_count", 0)),
                "handoff_count": int(run.get("handoff_count", 0)),
            },
            details={
                "ts_started": run.get("ts_started", ""),
                "ts_updated": run.get("ts_updated", ""),
                "ts_completed": run.get("ts_completed", ""),
                "query": run.get("query", ""),
                "pack_id": run.get("pack_id", ""),
                "pack_name": run.get("pack_name", ""),
                "notes": run.get("notes", ""),
            },
            **pos,
        )
        add_link("brain", run_id, "run", 0.9, rgba(color_for("run", run_domain), 0.22))
        if run.get("pack_id"):
            add_link(run_id, f"pack:{run['pack_id']}", "run_pack", 1.0, rgba(color_for("pack", run_domain), 0.22))
        if run.get("primary_skill"):
            add_link(run_id, f"skill:{run['primary_skill']}", "run_skill", 0.95, rgba(skill_color(run_domain), 0.22))
        if int(run.get("blocker_count", 0) or 0) > 0:
            blocker_id = f"run-blocker:{run['id']}"
            blocker_pos = anchored_position(run_domain, blocker_id, spread=102.0, vertical=62.0)
            add_node(
                blocker_id,
                label=f"Run #{run['id']} Blockers",
                kind="blocker",
                domain=run_domain,
                color=color_for("blocker", run_domain),
                size=7 + min(5, int(run.get("blocker_count", 0))),
                status="open",
                metrics={"open_blockers": int(run.get("blocker_count", 0))},
                details={"pack_id": run.get("pack_id", ""), "query": run.get("query", "")},
                **blocker_pos,
            )
            add_link(run_id, blocker_id, "run_blocker", 1.05, rgba(color_for("blocker", run_domain), 0.28))

    for index, alert in enumerate(alerts, start=1):
        node_id = f"alert:{index}"
        domain = "core"
        pos = anchored_position(domain, node_id, spread=115.0, vertical=60.0)
        add_node(
            node_id,
            label=f"Alert {index}",
            kind="alert",
            domain=domain,
            color=color_for("alert", domain),
            size=7.5,
            status="warning",
            metrics={"severity": 1},
            details={"message": alert},
            **pos,
        )
        add_link("brain", node_id, "alert", 0.7, rgba(color_for("alert", domain), 0.32))

    evaluation = learning_evaluation if isinstance(learning_evaluation, dict) else {}
    task_evaluation = ((control.get("learning") or {}).get("task_evaluation") or {}) if isinstance(control.get("learning"), dict) else {}
    payload = {
        "generated_at": now_iso(),
        "meta": {
            "domains_total": len([node_id for node_id in nodes if node_id.startswith("domain:")]),
            "packs_total": len([node_id for node_id in nodes if node_id.startswith("pack:")]),
            "skills_total": len([node_id for node_id in nodes if node_id.startswith("skill:")]),
            "topics_total": len([node_id for node_id in nodes if node_id.startswith("topic:")]),
            "memory_banks_total": len([node_id for node_id in nodes if node_id.startswith("memory-bank:")]),
            "outcomes_total": len([node_id for node_id in nodes if node_id.startswith("outcome:")]),
            "episodes_total": len(recent_episodes),
            "runs_total": len(run_snapshot["runs"]),
            "active_runs_total": int(run_snapshot["active_runs"]),
            "blocked_runs_total": int(run_snapshot["blocked_runs"]),
            "open_blockers_total": int(run_snapshot["open_blockers"]),
            "workspace_contexts_total": int(workspace_snapshot["active_contexts"]),
            "workspace_items_total": int(workspace_snapshot["active_items"]),
            "alerts_total": len(alerts),
            "meetings_total": len(meetings),
            "chunks_total": int(chunk_snapshot["total_chunks"]),
            "memory_paths_total": int(chunk_snapshot["total_paths"]),
            "nodes_total": len(nodes),
            "links_total": len(links),
            "manual_scorecards": int((((control.get("learning") or {}).get("task_results") or {}).get("manual_scorecards", 0))),
            "recent_events_total": len(recent_events),
            "evaluation": {
                "primary_skill_accuracy": float(evaluation.get("primary_skill_accuracy", 0.0)),
                "top3_skill_hit_rate": float(evaluation.get("top3_skill_hit_rate", 0.0)),
                "top5_path_hit_rate": float(evaluation.get("top5_path_hit_rate", 0.0)),
            },
            "task_evaluation": {
                "pack_accuracy": float(task_evaluation.get("pack_accuracy", 0.0)),
                "pass_rate": float(task_evaluation.get("pass_rate", 0.0)),
                "total_cases": int(task_evaluation.get("total_cases", 0) or 0),
            },
        },
        "meetings": meetings,
        "recent_events": recent_events,
        "recent_episodes": recent_episodes,
        "workspace": workspace_snapshot,
        "nodes": list(nodes.values()),
        "links": list(links.values()),
    }
    return payload


def build_graph_pro_payload(
    control_status_path: Path,
    ingest_root: Path,
    db_path: Path,
    packs_file: Path,
    outcomes_limit: int,
    alerts_limit: int,
    chunk_limit: int = 1200,
) -> Dict[str, Any]:
    payload = build_graph_payload(
        control_status_path=control_status_path,
        ingest_root=ingest_root,
        db_path=db_path,
        packs_file=packs_file,
        outcomes_limit=outcomes_limit,
        alerts_limit=alerts_limit,
    )
    nodes: Dict[str, Dict[str, Any]] = {str(node["id"]): dict(node) for node in payload.get("nodes", [])}
    existing_links = payload.get("links", [])
    links: Dict[Tuple[str, str, str], Dict[str, Any]] = {
        (str(item["source"]), str(item["target"]), str(item.get("kind", "link"))): dict(item)
        for item in existing_links
    }

    def add_node(node_id: str, **attrs: Any) -> None:
        current = nodes.get(node_id)
        if current is None:
            nodes[node_id] = {"id": node_id, **attrs}
            return
        for key, value in attrs.items():
            if value is None:
                continue
            if key in {"metrics", "details"} and isinstance(value, dict):
                merged = dict(current.get(key, {}))
                merged.update(value)
                current[key] = merged
            elif key == "tags" and isinstance(value, list):
                current[key] = list(dict.fromkeys(current.get(key, []) + value))
            elif key not in current or current.get(key) in ("", None, [], {}):
                current[key] = value

    def add_link(source: str, target: str, kind: str, weight: float = 1.0, color: str = "") -> None:
        key = (source, target, kind)
        if key in links:
            links[key]["weight"] = max(float(links[key].get("weight", 0.0)), float(weight))
            return
        links[key] = {
            "source": source,
            "target": target,
            "kind": kind,
            "weight": round(float(weight), 3),
            "color": color,
        }

    def parse_graph_dt(value: Any) -> Optional[datetime]:
        raw = str(value or "").strip()
        if not raw:
            return None
        try:
            if len(raw) == 10:
                return datetime.strptime(raw, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            normalized = raw.replace("Z", "+00:00")
            parsed = datetime.fromisoformat(normalized)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc)
        except ValueError:
            return None

    now_utc = datetime.now(timezone.utc)

    def timeline_bucket(value: Any) -> Optional[Tuple[str, str, float]]:
        parsed = parse_graph_dt(value)
        if parsed is None:
            return None
        age_days = max(0.0, (now_utc - parsed).total_seconds() / 86400.0)
        if age_days <= 1.0:
            return ("24h", "Fresh 24h", 0.98)
        if age_days <= 7.0:
            return ("7d", "Last 7 days", 0.9)
        if age_days <= 30.0:
            return ("30d", "Last 30 days", 0.78)
        if age_days <= 90.0:
            return ("90d", "Last 90 days", 0.62)
        return ("older", "Older", 0.45)

    timeline_nodes: Dict[str, str] = {}

    def ensure_timeline_node(bucket_key: str, bucket_label: str) -> str:
        node_id = timeline_nodes.get(bucket_key)
        if node_id:
            return node_id
        node_id = f"timeline:{bucket_key}"
        timeline_nodes[bucket_key] = node_id
        offset_map = {
            "24h": (-180.0, -180.0, -60.0),
            "7d": (-60.0, -140.0, -40.0),
            "30d": (70.0, -120.0, -10.0),
            "90d": (190.0, -85.0, 20.0),
            "older": (305.0, -60.0, 45.0),
        }
        base = offset_map.get(bucket_key, (0.0, -110.0, 0.0))
        add_node(
            node_id,
            label=bucket_label,
            kind="timeline",
            domain="core",
            color=color_for("timeline", "core"),
            size=9.0,
            status="time",
            metrics={"bucket": bucket_key},
            details={"bucket": bucket_key, "label": bucket_label},
            x=round(base[0], 2),
            y=round(base[1], 2),
            z=round(base[2], 2),
        )
        add_link("brain", node_id, "timeline", 0.9, rgba(color_for("timeline", "core"), 0.2))
        return node_id

    note_by_path: Dict[str, str] = {}
    existing_topic_ids = {node_id for node_id, node in nodes.items() if str(node.get("kind")) == "topic"}
    topic_by_key: Dict[Tuple[str, str], str] = {}
    pack_nodes: Dict[str, Dict[str, Any]] = {}
    for node_id, node in nodes.items():
        details = node.get("details", {})
        path = str(details.get("path", "")) if isinstance(details, dict) else ""
        if node.get("kind") == "note" and path:
            note_by_path[path] = node_id
        if node.get("kind") == "topic":
            topic_by_key[(str(node.get("domain") or "core"), slugify(str(node.get("label") or node_id)))] = node_id
        if node.get("kind") == "pack":
            pack_nodes[node_id] = node

    publication_by_name: Dict[str, str] = {}
    chunk_rows = fetch_graph_pro_chunks(db_path, chunk_limit)
    for row in chunk_rows:
        path = str(row.get("path") or "")
        if not path:
            continue
        domain = domain_from_path(path)
        chunk_id = f"chunk:{slugify(str(row.get('chunk_id') or path))}"
        note_id = note_by_path.get(path)
        if note_id is None:
            note_id = f"note:{slugify(path)}"
            note_by_path[path] = note_id
            note_pos = anchored_position(domain, note_id, spread=170.0, vertical=130.0)
            add_node(
                note_id,
                label=title_from_slug(Path(path).stem),
                kind="note",
                domain=domain,
                color=color_for("note", domain),
                size=6.5,
                status="derived",
                metrics={"path": path},
                details={"path": path},
                **note_pos,
            )
            add_link(f"domain:{domain}" if f"domain:{domain}" in nodes else "brain", note_id, "note", 0.7, rgba(color_for("note", domain), 0.18))
        anchor = nodes.get(note_id, {})
        offset = stable_offset(chunk_id, 48.0, 70.0)
        chunk_pos = {
            "x": round(float(anchor.get("x", 0.0)) + offset[0] * 0.55, 2),
            "y": round(float(anchor.get("y", 0.0)) + offset[1] * 0.35, 2),
            "z": round(float(anchor.get("z", 0.0)) + offset[2] * 0.55, 2),
        }
        topics = parse_json_list(row.get("topics_json"))
        intents = parse_json_list(row.get("intents_json"))
        tags = parse_json_list(row.get("tags_json"))
        source_name = str(row.get("source") or "")
        freshness = float(row.get("freshness") or 0.0)
        is_canonical = int(row.get("is_canonical") or 0)
        add_node(
            chunk_id,
            label=str(row.get("heading") or Path(path).stem or "Chunk"),
            kind="chunk",
            domain=domain,
            color=color_for("chunk", domain),
            size=2.6 + min(3.6, freshness * 1.8 + is_canonical * 1.2),
            status=str(row.get("confidence") or row.get("section_kind") or "chunk"),
            tags=list(dict.fromkeys(tags + topics[:3] + intents[:2])),
            metrics={
                "freshness": round(freshness, 3),
                "canonical": is_canonical,
            },
            details={
                "path": path,
                "heading": str(row.get("heading") or ""),
                "source": source_name,
                "section_kind": str(row.get("section_kind") or ""),
                "published_on": str(row.get("published_on") or ""),
                "canonical_group": str(row.get("canonical_group") or ""),
                "text_preview": str(row.get("text") or "")[:240],
                "topics": topics[:6],
                "intents": intents[:4],
            },
            **chunk_pos,
        )
        add_link(note_id, chunk_id, "note_chunk", 0.62, rgba(color_for("chunk", domain), 0.15))

        for topic_name in topics[:4]:
            topic_id = f"topic:{domain}:{slugify(topic_name)}"
            if topic_id in existing_topic_ids:
                add_link(topic_id, chunk_id, "topic_chunk", 0.56, rgba(color_for("topic", domain), 0.14))

        if source_name:
            publication_id = publication_by_name.get(source_name)
            if publication_id is None:
                publication_id = f"publication:{slugify(source_name)}"
                publication_by_name[source_name] = publication_id
                pub_pos = anchored_position(domain, publication_id, spread=205.0, vertical=150.0)
                add_node(
                    publication_id,
                    label=source_name,
                    kind="publication",
                    domain=domain,
                    color=color_for("publication", domain),
                    size=7.0,
                    status="reference",
                    metrics={"domains": 1},
                    details={"source": source_name},
                    **pub_pos,
                )
                add_link(f"domain:{domain}" if f"domain:{domain}" in nodes else "brain", publication_id, "publication", 0.7, rgba(color_for("publication", domain), 0.18))
            add_link(publication_id, chunk_id, "publication_chunk", 0.52, rgba(color_for("publication", domain), 0.18))
            add_link(publication_id, note_id, "publication_note", 0.48, rgba(color_for("publication", domain), 0.16))

        bucket = timeline_bucket(row.get("published_on"))
        if bucket is not None:
            bucket_id = ensure_timeline_node(bucket[0], bucket[1])
            add_link(bucket_id, chunk_id, "timeline_chunk", bucket[2], rgba(color_for("timeline", "core"), 0.18))

        for topic_name in topics[:4]:
            topic_id = topic_by_key.get((domain, slugify(topic_name)))
            if topic_id and source_name:
                publication_id = publication_by_name.get(source_name)
                if publication_id:
                    add_link(publication_id, topic_id, "publication_topic", 0.44, rgba(color_for("publication", domain), 0.16))

    causal_topic_pack_links = 0
    for topic_id in list(existing_topic_ids):
        topic_node = nodes.get(topic_id)
        if not topic_node:
            continue
        topic_domain = str(topic_node.get("domain") or "core")
        topic_slug = slugify(str(topic_node.get("label") or topic_id))
        for pack_id, pack_node in pack_nodes.items():
            if str(pack_node.get("domain") or "core") != topic_domain:
                continue
            pack_tags = [slugify(str(item)) for item in pack_node.get("tags", [])]
            pack_details = pack_node.get("details", {})
            primary_skill = slugify(str(pack_details.get("primary_skill") or ""))
            supporting = [slugify(str(item)) for item in pack_details.get("supporting_skills", [])]
            if topic_slug in pack_tags or topic_slug == primary_skill or topic_slug in supporting:
                add_link(topic_id, pack_id, "topic_pack", 0.58, rgba(color_for("pack", topic_domain), 0.18))
                causal_topic_pack_links += 1

    timeline_link_kinds = {"timeline_chunk", "timeline_outcome", "timeline_episode", "timeline_run"}
    for node_id, node in list(nodes.items()):
        kind = str(node.get("kind") or "")
        details = node.get("details", {})
        date_value: Any = None
        if kind == "outcome":
            date_value = details.get("ts")
        elif kind == "episode":
            date_value = details.get("ts_end") or details.get("ts_start")
        elif kind == "run":
            date_value = details.get("ts_updated") or details.get("ts_started") or details.get("ts_completed")
        else:
            continue
        bucket = timeline_bucket(date_value)
        if bucket is None:
            continue
        bucket_id = ensure_timeline_node(bucket[0], bucket[1])
        add_link(bucket_id, node_id, f"timeline_{kind}", bucket[2], rgba(color_for("timeline", "core"), 0.18))

    facet_domains = sorted({str(node.get("domain")) for node in nodes.values() if node.get("domain")})
    facet_kinds = sorted({str(node.get("kind")) for node in nodes.values() if node.get("kind")})
    facet_sources = sorted(publication_by_name.keys())[:36]
    causal_link_kinds = sorted(
        {
            str(link.get("kind"))
            for link in links.values()
            if str(link.get("kind") or "").startswith(("publication_", "evidence_", "topic_", "primary_", "used_", "episode_", "run_", "timeline_"))
        }
    )

    payload["nodes"] = list(nodes.values())
    payload["links"] = list(links.values())
    payload["meta"]["nodes_total"] = len(payload["nodes"])
    payload["meta"]["links_total"] = len(payload["links"])
    payload["meta"]["chunk_nodes_total"] = len([node for node in payload["nodes"] if node.get("kind") == "chunk"])
    payload["meta"]["publication_nodes_total"] = len([node for node in payload["nodes"] if node.get("kind") == "publication"])
    payload["filters"] = {
        "domains": facet_domains,
        "kinds": facet_kinds,
        "sources": facet_sources,
        "detail_modes": ["all", "no_chunks", "core_only"],
        "view_modes": ["topology", "timeline", "causal"],
        "drill_levels": ["overview", "domain", "topic", "note", "chunk"],
        "timeline_buckets": ["all", "24h", "7d", "30d", "90d", "older"],
        "causal_link_kinds": causal_link_kinds,
    }
    payload["meta"]["timeline_nodes_total"] = len([node for node in payload["nodes"] if node.get("kind") == "timeline"])
    payload["meta"]["causal_topic_pack_links"] = causal_topic_pack_links
    payload["graph_mode"] = "graph_pro"
    return payload


def write_artifacts(phase31_dir: Path, payload: Dict[str, Any]) -> Dict[str, str]:
    phase31_dir.mkdir(parents=True, exist_ok=True)
    graph_path = phase31_dir / "memory_graph.json"
    report_path = phase31_dir / "memory_graph_report.md"
    latest_path = phase31_dir / "latest.json"
    graph_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    report_lines = [
        "---",
        "source: local phase31 memory graph",
        "title: Squad Memory Graph Snapshot",
        f"generated_at: {payload['generated_at']}",
        "tags: phase31, graph, visualization, squad_memory",
        "---",
        "",
        "# Squad Memory Graph Snapshot",
        "",
        f"- Nodes: `{payload['meta']['nodes_total']}`",
        f"- Links: `{payload['meta']['links_total']}`",
        f"- Domains: `{payload['meta']['domains_total']}`",
        f"- Topics: `{payload['meta']['topics_total']}`",
        f"- Memory files: `{payload['meta']['memory_paths_total']}`",
        f"- Chunks: `{payload['meta']['chunks_total']}`",
        f"- Recent outcomes: `{payload['meta']['outcomes_total']}`",
        f"- Meetings: `{payload['meta']['meetings_total']}`",
        f"- Manual scorecards: `{payload['meta']['manual_scorecards']}`",
        "",
        "## Viewer",
        "",
        "Run the local viewer with:",
        "",
        "```bash",
        "python3 /Users/vijaychauhan/squad_memory/phase31_memory_graph.py serve --port 8765",
        "```",
        "",
        "Then open `http://127.0.0.1:8765`.",
        "",
    ]
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    latest_path.write_text(
        json.dumps(
            {
                "generated_at": payload["generated_at"],
                "phase31_dir": str(phase31_dir),
                "graph_path": str(graph_path),
                "report_path": str(report_path),
                "node_count": payload["meta"]["nodes_total"],
                "link_count": payload["meta"]["links_total"],
            },
            indent=2,
            ensure_ascii=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "graph_path": str(graph_path),
        "report_path": str(report_path),
        "latest_path": str(latest_path),
    }


def handle_build(args: argparse.Namespace) -> Dict[str, Any]:
    payload = build_graph_payload(
        control_status_path=Path(args.phase21_status),
        ingest_root=Path(args.ingest_root),
        db_path=Path(args.db_path),
        packs_file=Path(args.packs_file),
        outcomes_limit=args.outcomes_limit,
        alerts_limit=args.alerts_limit,
    )
    paths = write_artifacts(Path(args.phase31_dir), payload)
    return {
        "generated_at": payload["generated_at"],
        "phase31_dir": str(Path(args.phase31_dir)),
        "node_count": payload["meta"]["nodes_total"],
        "link_count": payload["meta"]["links_total"],
        **paths,
    }


def make_handler(args: argparse.Namespace):
    ui_dir = Path(args.ui_dir)

    class GraphHandler(SimpleHTTPRequestHandler):
        def __init__(self, *handler_args: Any, **handler_kwargs: Any) -> None:
            super().__init__(*handler_args, directory=str(ui_dir), **handler_kwargs)

        def end_headers(self) -> None:
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query or "")
            if parsed.path == "/api/graph":
                payload = build_graph_payload(
                    control_status_path=Path(args.phase21_status),
                    ingest_root=Path(args.ingest_root),
                    db_path=Path(args.db_path),
                    packs_file=Path(args.packs_file),
                    outcomes_limit=args.outcomes_limit,
                    alerts_limit=args.alerts_limit,
                )
                if args.write_snapshot:
                    write_artifacts(Path(args.phase31_dir), payload)
                body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if parsed.path == "/api/events":
                limit = max(1, min(50, int((params.get("limit") or ["18"])[0])))
                since_id = max(0, int((params.get("since") or ["0"])[0]))
                payload = {
                    "generated_at": now_iso(),
                    "events": fetch_recent_events(Path(args.db_path), limit=limit, since_id=since_id),
                }
                body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if parsed.path == "/api/episodes":
                limit = max(1, min(50, int((params.get("limit") or ["12"])[0])))
                payload = {
                    "generated_at": now_iso(),
                    "episodes": fetch_recent_episodes(Path(args.db_path), limit=limit),
                }
                body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if parsed.path == "/api/events/stream":
                since_id = max(0, int((params.get("since") or ["0"])[0]))
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Connection", "keep-alive")
                self.end_headers()
                try:
                    while True:
                        events = fetch_recent_events(Path(args.db_path), limit=32, since_id=since_id)
                        if events:
                            for event in events:
                                since_id = max(since_id, int(event["id"]))
                                body = (
                                    f"id: {event['id']}\n"
                                    "event: memory-event\n"
                                    f"data: {json.dumps(event, ensure_ascii=True)}\n\n"
                                ).encode("utf-8")
                                self.wfile.write(body)
                                self.wfile.flush()
                        else:
                            self.wfile.write(b": heartbeat\n\n")
                            self.wfile.flush()
                        time.sleep(1.0)
                except (BrokenPipeError, ConnectionResetError):
                    return
                return
            if parsed.path == "/api/graph-pro":
                payload = build_graph_pro_payload(
                    control_status_path=Path(args.phase21_status),
                    ingest_root=Path(args.ingest_root),
                    db_path=Path(args.db_path),
                    packs_file=Path(args.packs_file),
                    outcomes_limit=args.outcomes_limit,
                    alerts_limit=args.alerts_limit,
                )
                body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if parsed.path == "/api/health":
                body = json.dumps({"status": "ok", "generated_at": now_iso()}, ensure_ascii=True).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if parsed.path in {"", "/"}:
                self.path = "/index.html"
            super().do_GET()

    return GraphHandler


def handle_serve(args: argparse.Namespace) -> int:
    payload = build_graph_payload(
        control_status_path=Path(args.phase21_status),
        ingest_root=Path(args.ingest_root),
        db_path=Path(args.db_path),
        packs_file=Path(args.packs_file),
        outcomes_limit=args.outcomes_limit,
        alerts_limit=args.alerts_limit,
    )
    write_artifacts(Path(args.phase31_dir), payload)
    server = ThreadingHTTPServer((args.host, args.port), make_handler(args))
    print(f"Serving squad memory graph at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def main() -> int:
    args = parse_args()
    command = args.command
    if command == "serve":
        return handle_serve(args)
    result = handle_build(args)
    if getattr(args, "json", False):
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(f"Generated graph with {result['node_count']} nodes and {result['link_count']} links.")
        print(f"Graph JSON: {result['graph_path']}")
        print(f"Report: {result['report_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
