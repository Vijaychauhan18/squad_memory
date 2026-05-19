#!/usr/bin/env python3
"""
Auto-Nautilus Hook — fires on Claude Code Stop event
Records each session as a typed Event record in squad_memory.db
Runs async (background) — never blocks Claude
"""

import sys
import json
import sqlite3
import hashlib
import datetime
import os

DB_PATH = os.path.expanduser("~/squad_memory/squad_memory.db")
LOG_PATH = "/tmp/nautilus_hook.log"


def log(msg: str):
    ts = datetime.datetime.now().isoformat()
    with open(LOG_PATH, "a") as f:
        f.write(f"[{ts}] {msg}\n")


def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def session_already_ingested(conn, session_id: str) -> bool:
    row = conn.execute(
        "SELECT chunk_id FROM chunks WHERE chunk_id LIKE ? LIMIT 1",
        (f"hook::{session_id}%",)
    ).fetchone()
    return row is not None


def ingest_session_event(conversation_id: str, session_id: str):
    """Ingest a minimal typed Event record for this completed session."""
    conn = get_db()

    # Avoid double-ingesting
    if session_id and session_already_ingested(conn, session_id):
        log(f"Session {session_id} already ingested — skip")
        conn.close()
        return

    ts = datetime.datetime.now().isoformat()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    chunk_id = f"hook::{session_id or conversation_id}::{date_str}"
    chunk_id = hashlib.sha1(chunk_id.encode()).hexdigest()[:16]
    chunk_id = f"hook::{date_str}::{chunk_id}"

    event_text = json.dumps({
        "event_type": "session_complete",
        "conversation_id": conversation_id or "unknown",
        "session_id": session_id or "unknown",
        "timestamp": ts,
        "source": "auto_ingest_hook",
        "note": "Auto-captured session. Ingest deliverables separately via Nautilus."
    }, indent=2)

    topics = json.dumps(["session", "auto_ingest"])
    tags = json.dumps(["auto_hook", f"date:{date_str}"])
    roles = json.dumps(["pinchy", "nautilus"])

    try:
        conn.execute("""
            INSERT OR IGNORE INTO chunks
            (chunk_id, path, skill, file_type, heading, text,
             section_kind, source, published_on, freshness,
             topics_json, intents_json, use_for_json, avoid_for_json,
             confidence, tags_json, roles_json, bundles_json,
             is_canonical, canonical_group)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chunk_id,
            f".auto_hook/{date_str}/{session_id or conversation_id}",
            "squad_operations",
            "event",
            f"Session Event — {date_str}",
            event_text,
            "event_record",
            "auto_hook",
            date_str,
            0.5,
            topics,
            json.dumps(["session_tracking"]),
            json.dumps(["session_history"]),
            json.dumps([]),
            "low",
            tags,
            roles,
            json.dumps([]),
            0,
            ""
        ))
        conn.commit()
        log(f"Ingested session event: {chunk_id}")
    except Exception as e:
        log(f"Ingest error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    conversation_id = sys.argv[1] if len(sys.argv) > 1 else ""
    session_id = sys.argv[2] if len(sys.argv) > 2 else ""
    try:
        ingest_session_event(conversation_id, session_id)
    except Exception as e:
        log(f"Hook failed: {e}")
