#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


HOME = Path.home()
DEFAULT_OPENCLAW_ROOT = HOME / ".openclaw"
DB_NAMES = ("main", "seo")
HEADER_KEYS = {
    "path",
    "heading",
    "canonical_group",
    "topics",
    "tags",
    "published_on",
    "source",
    "freshness",
    "confidence",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query local OpenClaw memory by text, topic, source, or path.")
    parser.add_argument("query", nargs="?", default="", help="Optional free-text query for FTS retrieval")
    parser.add_argument("--db", choices=DB_NAMES, default="seo", help="Target OpenClaw DB")
    parser.add_argument("--openclaw-root", default=str(DEFAULT_OPENCLAW_ROOT))
    parser.add_argument("--topic", default="", help="Filter bridge chunks by topic tag")
    parser.add_argument("--source", default="", help="Filter bridge chunks by article source")
    parser.add_argument("--path-prefix", default="", help="Filter by path prefix")
    parser.add_argument("--path-contains", default="", help="Filter by substring in path")
    parser.add_argument("--index-source", default="", help="Filter by index source such as memory or seo_elite_db")
    parser.add_argument("--bridge-only", action="store_true", help="Shortcut for --index-source seo_elite_db")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results to return")
    parser.add_argument("--snippet-chars", type=int, default=220, help="Maximum snippet length per result")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()
    if args.limit <= 0:
        parser.error("--limit must be greater than 0")
    if args.snippet_chars <= 0:
        parser.error("--snippet-chars must be greater than 0")
    if not any(
        [
            args.query.strip(),
            args.topic.strip(),
            args.source.strip(),
            args.path_prefix.strip(),
            args.path_contains.strip(),
            args.index_source.strip(),
            args.bridge_only,
        ]
    ):
        parser.error("provide a query or at least one filter")
    return args


def db_path(openclaw_root: Path, db_name: str) -> Path:
    return openclaw_root / "memory" / f"{db_name}.sqlite"


def tokenize_fts_query(query: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9_./:-]+", query)
    if not tokens:
        return ""
    return " OR ".join(f'"{token.replace(chr(34), "")}"' for token in tokens[:16])


def parse_bridge_metadata(text: str) -> tuple[dict[str, str], str]:
    metadata: dict[str, str] = {}
    lines = text.splitlines()
    body_index = 0
    for index, line in enumerate(lines[:12]):
        stripped = line.strip()
        if not stripped:
            body_index = index + 1
            break
        if ":" not in stripped:
            body_index = 0
            metadata = {}
            break
        key, value = stripped.split(":", 1)
        normalized = key.strip().lower().replace(" ", "_")
        if normalized not in HEADER_KEYS:
            body_index = 0
            metadata = {}
            break
        metadata[normalized] = value.strip()
        body_index = index + 1
    body = "\n".join(lines[body_index:]).strip() if metadata else text.strip()
    return metadata, body


def iso_from_millis(value: int | None) -> str | None:
    if not value:
        return None
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).astimezone().isoformat()


def compact_snippet(text: str, max_chars: int) -> str:
    single_line = re.sub(r"\s+", " ", text).strip()
    if len(single_line) <= max_chars:
        return single_line
    return single_line[: max_chars - 1].rstrip() + "…"


def build_filters(args: argparse.Namespace) -> tuple[list[str], list[Any]]:
    clauses: list[str] = []
    params: list[Any] = []

    index_source = "seo_elite_db" if args.bridge_only else args.index_source.strip()
    if index_source:
        clauses.append("c.source = ?")
        params.append(index_source)
    if args.path_prefix.strip():
        clauses.append("c.path LIKE ?")
        params.append(f"{args.path_prefix.strip()}%")
    if args.path_contains.strip():
        clauses.append("c.path LIKE ?")
        params.append(f"%{args.path_contains.strip()}%")
    if args.topic.strip():
        clauses.append("LOWER(c.text) LIKE ?")
        params.append(f"%topics: %{args.topic.strip().lower()}%")
    if args.source.strip():
        clauses.append("LOWER(c.text) LIKE ?")
        params.append(f"%source: {args.source.strip().lower()}%")
    return clauses, params


def run_query(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.openclaw_root)
    target_db = db_path(root, args.db)
    con = sqlite3.connect(f"file:{target_db}?mode=ro", uri=True, timeout=30)
    con.row_factory = sqlite3.Row
    try:
        con.execute("PRAGMA query_only = ON")
        clauses, params = build_filters(args)
        query_text = args.query.strip()
        rows: Iterable[sqlite3.Row]

        if query_text:
            fts_query = tokenize_fts_query(query_text)
            if not fts_query:
                raise ValueError("query did not contain searchable tokens")
            where = ["chunks_fts MATCH ?"] + clauses
            sql = f"""
                SELECT
                  c.id,
                  c.path,
                  c.source,
                  c.start_line,
                  c.end_line,
                  c.updated_at,
                  c.text,
                  bm25(chunks_fts) AS rank
                FROM chunks_fts
                JOIN chunks c ON c.id = chunks_fts.id
                WHERE {" AND ".join(where)}
                ORDER BY rank, c.updated_at DESC
                LIMIT ?
            """
            rows = con.execute(sql, [fts_query, *params, args.limit]).fetchall()
        else:
            where = clauses or ["1 = 1"]
            sql = f"""
                SELECT
                  c.id,
                  c.path,
                  c.source,
                  c.start_line,
                  c.end_line,
                  c.updated_at,
                  c.text,
                  NULL AS rank
                FROM chunks c
                WHERE {" AND ".join(where)}
                ORDER BY c.updated_at DESC, c.path, c.start_line
                LIMIT ?
            """
            rows = con.execute(sql, [*params, args.limit]).fetchall()

        results: list[dict[str, Any]] = []
        for row in rows:
            metadata, body = parse_bridge_metadata(str(row["text"]))
            results.append(
                {
                    "id": str(row["id"]),
                    "path": str(row["path"]),
                    "index_source": str(row["source"]),
                    "article_source": metadata.get("source"),
                    "heading": metadata.get("heading"),
                    "canonical_group": metadata.get("canonical_group"),
                    "topics": metadata.get("topics"),
                    "published_on": metadata.get("published_on"),
                    "confidence": metadata.get("confidence"),
                    "freshness": metadata.get("freshness"),
                    "start_line": int(row["start_line"]),
                    "end_line": int(row["end_line"]),
                    "updated_at": iso_from_millis(row["updated_at"]),
                    "rank": None if row["rank"] is None else float(row["rank"]),
                    "snippet": compact_snippet(body, args.snippet_chars),
                }
            )

        return {
            "db": args.db,
            "db_path": str(target_db),
            "query": query_text or None,
            "filters": {
                "topic": args.topic.strip() or None,
                "source": args.source.strip() or None,
                "path_prefix": args.path_prefix.strip() or None,
                "path_contains": args.path_contains.strip() or None,
                "index_source": ("seo_elite_db" if args.bridge_only else args.index_source.strip()) or None,
            },
            "count": len(results),
            "results": results,
        }
    finally:
        con.close()


def render_text(payload: dict[str, Any]) -> str:
    lines = [
        f"DB: {payload['db']}",
        f"Path: {payload['db_path']}",
        f"Matches: {payload['count']}",
    ]
    if payload["query"]:
        lines.append(f"Query: {payload['query']}")
    active_filters = {k: v for k, v in payload["filters"].items() if v}
    if active_filters:
        lines.append("Filters: " + ", ".join(f"{key}={value}" for key, value in active_filters.items()))
    if not payload["results"]:
        lines.append("")
        lines.append("No results.")
        return "\n".join(lines)

    for index, item in enumerate(payload["results"], start=1):
        meta = [f"index_source={item['index_source']}"]
        if item.get("article_source"):
            meta.append(f"article_source={item['article_source']}")
        if item.get("topics"):
            meta.append(f"topics={item['topics']}")
        if item.get("canonical_group"):
            meta.append(f"canonical_group={item['canonical_group']}")
        if item.get("updated_at"):
            meta.append(f"updated_at={item['updated_at']}")
        lines.extend(
            [
                "",
                f"{index}. {item['path']}",
                "   " + " | ".join(meta),
                f"   lines={item['start_line']}-{item['end_line']}",
                f"   {item['snippet']}",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    payload = run_query(args)
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(render_text(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
