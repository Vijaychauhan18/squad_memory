#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sqlite3
import time
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

from openclaw_fts_backfill import ensure_schema, hash_text


HOME = Path.home()
DEFAULT_SOURCE_DB = HOME / "squad_memory" / "seo_elite_memory.db"
DEFAULT_OPENCLAW_ROOT = HOME / ".openclaw"
DEFAULT_WORKSPACE = DEFAULT_OPENCLAW_ROOT / "workspace" / "squad" / "seo"
BRIDGE_SOURCE = "seo_elite_db"
BRIDGE_MODEL = "seo-elite-db-bridge"
BRIDGE_META_KEY = "seo_elite_bridge_meta_v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bridge SEO Elite chunks directly into OpenClaw SEO memory and write a workspace map")
    parser.add_argument("--source-db", default=str(DEFAULT_SOURCE_DB))
    parser.add_argument("--openclaw-root", default=str(DEFAULT_OPENCLAW_ROOT))
    parser.add_argument("--workspace", default=str(DEFAULT_WORKSPACE))
    parser.add_argument("--target-db", default="", help="Optional explicit target DB path; defaults to seo.sqlite")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def now_ms() -> int:
    return int(time.time() * 1000)


def json_list(value: str | None) -> List[str]:
    if not value:
        return []
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return []
    if isinstance(parsed, list):
        return [str(item) for item in parsed if item]
    return []


def path_family(path: str) -> str:
    parts = [part for part in path.split("/") if part]
    if len(parts) >= 4 and parts[1] == "memory" and parts[2] == "articles":
        return f"articles/{parts[3]}"
    if len(parts) >= 3 and parts[1] == "memory":
        return f"memory/{parts[2]}"
    return "/".join(parts[:3]) if parts else "unknown"


def enriched_chunk_text(row: sqlite3.Row) -> str:
    topics = json_list(row["topics_json"])
    tags = json_list(row["tags_json"])
    source = str(row["source"] or "unknown")
    header = [
        f"Path: {row['path']}",
        f"Heading: {row['heading']}",
        f"Canonical Group: {row['canonical_group'] or 'none'}",
        f"Topics: {', '.join(topics[:8]) if topics else 'none'}",
        f"Tags: {', '.join(tags[:12]) if tags else 'none'}",
        f"Published On: {row['published_on'] or 'unknown'}",
        f"Source: {source}",
        f"Freshness: {row['freshness']}",
        f"Confidence: {row['confidence']}",
        "",
    ]
    return "\n".join(header) + str(row["text"]).strip()


def write_bridge_map(
    workspace: Path,
    summary: Dict[str, Any],
    path_manifest: List[Dict[str, Any]],
) -> Dict[str, str]:
    bridge_dir = workspace / "automation" / "knowledge-bridge"
    bridge_dir.mkdir(parents=True, exist_ok=True)

    summary_json = bridge_dir / "seo-elite-map.json"
    summary_md = bridge_dir / "seo-elite-map.md"
    path_manifest_json = bridge_dir / "seo-elite-path-manifest.json"

    summary_json.write_text(json.dumps(summary, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    path_manifest_json.write_text(json.dumps({"paths": path_manifest}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    lines = [
        "# SEO Elite -> OpenClaw Bridge Map",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Corpus",
        f"- source db: `{summary['source_db']}`",
        f"- target db: `{summary['target_db']}`",
        f"- imported chunks: `{summary['imported_chunks']}`",
        f"- imported paths: `{summary['imported_paths']}`",
        f"- chunk delta vs previous target source: `{summary['chunk_delta']}`",
        "",
        "## Top Canonical Groups",
    ]
    lines.extend(
        f"- {item['name']} | chunks=`{item['chunks']}`"
        for item in summary["top_canonical_groups"]
    )
    lines.extend(["", "## Top Topics"])
    lines.extend(
        f"- {item['name']} | chunks=`{item['chunks']}`"
        for item in summary["top_topics"]
    )
    lines.extend(["", "## Top Path Families"])
    lines.extend(
        f"- {item['name']} | chunks=`{item['chunks']}`"
        for item in summary["top_path_families"]
    )
    lines.extend(["", "## Hot Paths"])
    lines.extend(
        f"- {item['path']} | chunks=`{item['chunk_count']}` | latest=`{item['latest_published_on']}` | sample heading=`{item['sample_heading']}`"
        for item in path_manifest[:20]
    )
    lines.append("")
    summary_md.write_text("\n".join(lines), encoding="utf-8")

    return {
        "summary_json": str(summary_json),
        "summary_markdown": str(summary_md),
        "path_manifest_json": str(path_manifest_json),
    }


def bridge_seo_elite_chunks(
    source_db: Path,
    openclaw_root: Path,
    workspace: Path,
    target_db: Path | None = None,
    write_map: bool = True,
) -> Dict[str, Any]:
    if not source_db.exists():
        raise FileNotFoundError(f"Missing SEO Elite DB: {source_db}")

    if target_db is None:
        target_db = openclaw_root / "memory" / "seo.sqlite"
    target_db.parent.mkdir(parents=True, exist_ok=True)

    source_con = sqlite3.connect(str(source_db))
    source_con.row_factory = sqlite3.Row
    target_con = sqlite3.connect(str(target_db))
    target_con.row_factory = sqlite3.Row

    try:
        ensure_schema(target_con)

        previous_target_chunks = int(
            target_con.execute("SELECT COUNT(*) FROM chunks WHERE source = ?", (BRIDGE_SOURCE,)).fetchone()[0]
        )

        path_stats: Dict[str, Dict[str, Any]] = {}
        topic_counts: Counter[str] = Counter()
        canonical_counts: Counter[str] = Counter()
        family_counts: Counter[str] = Counter()

        bridge_started_ms = now_ms()
        target_con.execute("BEGIN")
        target_con.execute("DELETE FROM chunks_fts WHERE source = ?", (BRIDGE_SOURCE,))
        target_con.execute("DELETE FROM chunks WHERE source = ?", (BRIDGE_SOURCE,))
        target_con.execute("DELETE FROM files WHERE source = ?", (BRIDGE_SOURCE,))

        row_count = 0
        cursor = source_con.execute(
            """
            SELECT
              chunk_id,
              path,
              heading,
              text,
              source,
              published_on,
              freshness,
              topics_json,
              tags_json,
              confidence,
              canonical_group
            FROM chunks
            ORDER BY path, heading
            """
        )
        for row in cursor:
            enriched = enriched_chunk_text(row)
            chunk_hash = hash_text(enriched)
            chunk_id = hash_text(f"{BRIDGE_SOURCE}:{row['chunk_id']}:{row['path']}")
            published_on = str(row["published_on"] or "")
            canonical_group = str(row["canonical_group"] or "uncategorized")
            target_con.execute(
                """
                INSERT INTO chunks
                  (id, path, source, start_line, end_line, hash, model, text, embedding, updated_at)
                VALUES
                  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    chunk_id,
                    str(row["path"]),
                    BRIDGE_SOURCE,
                    0,
                    0,
                    chunk_hash,
                    BRIDGE_MODEL,
                    enriched,
                    "[]",
                    bridge_started_ms,
                ),
            )
            target_con.execute(
                """
                INSERT INTO chunks_fts
                  (text, id, path, source, model, start_line, end_line)
                VALUES
                  (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    enriched,
                    chunk_id,
                    str(row["path"]),
                    BRIDGE_SOURCE,
                    BRIDGE_MODEL,
                    0,
                    0,
                ),
            )

            stats = path_stats.setdefault(
                str(row["path"]),
                {
                    "path": str(row["path"]),
                    "chunk_count": 0,
                    "latest_published_on": published_on,
                    "sample_heading": str(row["heading"]),
                    "canonical_group": canonical_group,
                    "size": 0,
                },
            )
            stats["chunk_count"] += 1
            stats["size"] += len(enriched)
            if published_on and published_on > str(stats["latest_published_on"]):
                stats["latest_published_on"] = published_on
            if not stats["sample_heading"] and row["heading"]:
                stats["sample_heading"] = str(row["heading"])
            if stats["canonical_group"] == "uncategorized" and canonical_group != "uncategorized":
                stats["canonical_group"] = canonical_group

            canonical_counts[canonical_group] += 1
            family_counts[path_family(str(row["path"]))] += 1
            for topic in json_list(row["topics_json"]):
                topic_counts[topic] += 1

            row_count += 1

        for path, stats in path_stats.items():
            target_con.execute(
                """
                INSERT INTO files (path, source, hash, mtime, size)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    path,
                    BRIDGE_SOURCE,
                    hash_text(json.dumps(stats, sort_keys=True)),
                    bridge_started_ms,
                    int(stats["size"]),
                ),
            )

        bridge_meta = {
            "generated_at": now_iso(),
            "source_db": str(source_db),
            "target_db": str(target_db),
            "source": BRIDGE_SOURCE,
            "model": BRIDGE_MODEL,
            "chunks": row_count,
            "paths": len(path_stats),
        }
        target_con.execute(
            """
            INSERT INTO meta (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value
            """,
            (BRIDGE_META_KEY, json.dumps(bridge_meta, separators=(",", ":"))),
        )
        target_con.commit()
    except Exception:
        target_con.rollback()
        raise
    finally:
        source_con.close()
        target_con.close()

    path_manifest = sorted(
        path_stats.values(),
        key=lambda item: (-int(item["chunk_count"]), item["path"]),
    )
    summary = {
        "generated_at": now_iso(),
        "source_db": str(source_db),
        "target_db": str(target_db),
        "bridge_source": BRIDGE_SOURCE,
        "imported_chunks": row_count,
        "imported_paths": len(path_manifest),
        "previous_target_chunks": previous_target_chunks,
        "chunk_delta": row_count - previous_target_chunks,
        "top_canonical_groups": [
            {"name": name, "chunks": count}
            for name, count in canonical_counts.most_common(20)
        ],
        "top_topics": [
            {"name": name, "chunks": count}
            for name, count in topic_counts.most_common(20)
        ],
        "top_path_families": [
            {"name": name, "chunks": count}
            for name, count in family_counts.most_common(20)
        ],
    }
    if write_map:
        summary["written"] = write_bridge_map(workspace, summary, path_manifest)
    return summary


def main() -> int:
    args = parse_args()
    result = bridge_seo_elite_chunks(
        source_db=Path(args.source_db),
        openclaw_root=Path(args.openclaw_root),
        workspace=Path(args.workspace),
        target_db=Path(args.target_db) if args.target_db else None,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(
            "SEO Elite -> OpenClaw bridge complete | "
            f"chunks={result['imported_chunks']} paths={result['imported_paths']} "
            f"target={result['target_db']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
