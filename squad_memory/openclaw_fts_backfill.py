#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MODEL = "fts-only"
SOURCE = "memory"
CHUNK_TOKENS = 400
CHUNK_OVERLAP = 80
META_KEY = "memory_index_meta_v1"


@dataclass
class Chunk:
    start_line: int
    end_line: int
    text: str
    hash: str


@dataclass(frozen=True)
class AgentTarget:
    agent_id: str
    workspace: Path
    db_path: Path
    extra_paths: tuple[Path, ...]


def parse_args() -> argparse.Namespace:
    home = Path.home()
    parser = argparse.ArgumentParser(description="Backfill OpenClaw FTS memory index from markdown")
    parser.add_argument("--openclaw-root", default=str(home / ".openclaw"))
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def walk_markdown(dir_path: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(dir_path.rglob("*.md")):
        try:
            if path.is_symlink() or not path.is_file():
                continue
        except OSError:
            continue
        files.append(path)
    return files


def add_markdown_file(result: list[Path], path: Path) -> None:
    try:
        if path.is_symlink() or not path.is_file() or path.suffix != ".md":
            return
    except OSError:
        return
    result.append(path)


def list_memory_files(workspace: Path, extra_paths: tuple[Path, ...]) -> list[Path]:
    result: list[Path] = []

    add_markdown_file(result, workspace / "MEMORY.md")
    add_markdown_file(result, workspace / "memory.md")

    memory_dir = workspace / "memory"
    try:
        if memory_dir.is_dir() and not memory_dir.is_symlink():
            result.extend(walk_markdown(memory_dir))
    except OSError:
        pass

    for input_path in extra_paths:
        try:
            if input_path.is_symlink():
                continue
            if input_path.is_dir():
                result.extend(walk_markdown(input_path))
            elif input_path.is_file() and input_path.suffix == ".md":
                result.append(input_path)
        except OSError:
            continue

    deduped: list[Path] = []
    seen_ids: set[tuple[int, int]] = set()
    seen_paths: set[str] = set()
    for path in result:
        try:
            stat = path.stat()
            key = (stat.st_dev, stat.st_ino)
            if key in seen_ids:
                continue
            seen_ids.add(key)
        except OSError:
            key_str = str(path.resolve())
            if key_str in seen_paths:
                continue
            seen_paths.add(key_str)
        deduped.append(path)
    return deduped


def chunk_markdown(content: str, tokens: int, overlap: int) -> list[Chunk]:
    lines = content.split("\n")
    if not lines:
        return []

    max_chars = max(32, tokens * 4)
    overlap_chars = max(0, overlap * 4)
    chunks: list[Chunk] = []

    current: list[tuple[str, int]] = []
    current_chars = 0

    def flush() -> None:
        if not current:
            return
        first_line_no = current[0][1]
        last_line_no = current[-1][1]
        text = "\n".join(line for line, _ in current)
        chunks.append(
            Chunk(
                start_line=first_line_no,
                end_line=last_line_no,
                text=text,
                hash=hash_text(text),
            )
        )

    def carry_overlap() -> tuple[list[tuple[str, int]], int]:
        if overlap_chars <= 0 or not current:
            return [], 0
        acc = 0
        kept: list[tuple[str, int]] = []
        for line, line_no in reversed(current):
            acc += len(line) + 1
            kept.insert(0, (line, line_no))
            if acc >= overlap_chars:
                break
        kept_chars = sum(len(line) + 1 for line, _ in kept)
        return kept, kept_chars

    for index, line in enumerate(lines, start=1):
        segments = [""]
        if line:
            segments = [line[start : start + max_chars] for start in range(0, len(line), max_chars)]
        for segment in segments:
            line_size = len(segment) + 1
            if current_chars + line_size > max_chars and current:
                flush()
                current, current_chars = carry_overlap()
            current.append((segment, index))
            current_chars += line_size

    flush()
    return [chunk for chunk in chunks if chunk.text.strip()]


def to_rel_path(workspace: Path, abs_path: Path) -> str:
    return os.path.relpath(abs_path, workspace).replace("\\", "/")


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS meta (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS files (
          path TEXT PRIMARY KEY,
          source TEXT NOT NULL DEFAULT 'memory',
          hash TEXT NOT NULL,
          mtime INTEGER NOT NULL,
          size INTEGER NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS chunks (
          id TEXT PRIMARY KEY,
          path TEXT NOT NULL,
          source TEXT NOT NULL DEFAULT 'memory',
          start_line INTEGER NOT NULL,
          end_line INTEGER NOT NULL,
          hash TEXT NOT NULL,
          model TEXT NOT NULL,
          text TEXT NOT NULL,
          embedding TEXT NOT NULL,
          updated_at INTEGER NOT NULL
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_chunks_path ON chunks(path)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source)")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS embedding_cache (
          provider TEXT NOT NULL,
          model TEXT NOT NULL,
          provider_key TEXT NOT NULL,
          hash TEXT NOT NULL,
          embedding TEXT NOT NULL,
          dims INTEGER,
          updated_at INTEGER NOT NULL,
          PRIMARY KEY (provider, model, provider_key, hash)
        )
        """
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_embedding_cache_updated_at ON embedding_cache(updated_at)"
    )
    conn.execute(
        """
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
          text,
          id UNINDEXED,
          path UNINDEXED,
          source UNINDEXED,
          model UNINDEXED,
          start_line UNINDEXED,
          end_line UNINDEXED
        )
        """
    )


def fts_only_provider_key() -> str:
    payload = json.dumps({"provider": "none", "model": MODEL}, separators=(",", ":"))
    return hash_text(payload)


def write_meta(conn: sqlite3.Connection) -> None:
    meta = {
        "model": MODEL,
        "provider": "none",
        "providerKey": fts_only_provider_key(),
        "sources": [SOURCE],
        "chunkTokens": CHUNK_TOKENS,
        "chunkOverlap": CHUNK_OVERLAP,
    }
    conn.execute(
        """
        INSERT INTO meta (key, value)
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value=excluded.value
        """,
        (
            META_KEY,
            json.dumps(meta, separators=(",", ":")),
        ),
    )


def rebuild_agent(target: AgentTarget) -> dict[str, Any]:
    files = list_memory_files(target.workspace, target.extra_paths)
    now_ms = int(time.time() * 1000)

    target.db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(target.db_path)
    try:
        ensure_schema(conn)
        conn.execute("BEGIN")
        conn.execute("DELETE FROM chunks_fts WHERE source = ?", (SOURCE,))
        conn.execute("DELETE FROM chunks WHERE source = ?", (SOURCE,))
        conn.execute("DELETE FROM files WHERE source = ?", (SOURCE,))

        file_count = 0
        chunk_count = 0
        for abs_path in files:
            try:
                content = abs_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                content = abs_path.read_text(encoding="utf-8", errors="ignore")
            stat = abs_path.stat()
            rel_path = to_rel_path(target.workspace, abs_path)
            file_hash = hash_text(content)
            chunks = chunk_markdown(content, CHUNK_TOKENS, CHUNK_OVERLAP)

            for chunk in chunks:
                chunk_id = hash_text(
                    f"{SOURCE}:{rel_path}:{chunk.start_line}:{chunk.end_line}:{chunk.hash}:{MODEL}"
                )
                conn.execute(
                    """
                    INSERT INTO chunks
                      (id, path, source, start_line, end_line, hash, model, text, embedding, updated_at)
                    VALUES
                      (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        chunk_id,
                        rel_path,
                        SOURCE,
                        chunk.start_line,
                        chunk.end_line,
                        chunk.hash,
                        MODEL,
                        chunk.text,
                        "[]",
                        now_ms,
                    ),
                )
                conn.execute(
                    """
                    INSERT INTO chunks_fts
                      (text, id, path, source, model, start_line, end_line)
                    VALUES
                      (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        chunk.text,
                        chunk_id,
                        rel_path,
                        SOURCE,
                        MODEL,
                        chunk.start_line,
                        chunk.end_line,
                    ),
                )
                chunk_count += 1

            conn.execute(
                """
                INSERT INTO files (path, source, hash, mtime, size)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    rel_path,
                    SOURCE,
                    file_hash,
                    int(stat.st_mtime * 1000),
                    stat.st_size,
                ),
            )
            file_count += 1

        write_meta(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return {
        "agent_id": target.agent_id,
        "workspace": str(target.workspace),
        "db_path": str(target.db_path),
        "files": file_count,
        "chunks": chunk_count,
    }


def build_targets(openclaw_root: Path) -> list[AgentTarget]:
    workspace = openclaw_root / "workspace"
    import_root = workspace / "memory" / "imports" / "codex"
    seo_workspace = workspace / "squad" / "seo"
    return [
        AgentTarget(
            agent_id="main",
            workspace=workspace,
            db_path=openclaw_root / "memory" / "main.sqlite",
            extra_paths=(import_root,),
        ),
        AgentTarget(
            agent_id="seo",
            workspace=seo_workspace,
            db_path=openclaw_root / "memory" / "seo.sqlite",
            extra_paths=(import_root, seo_workspace / "automation"),
        ),
    ]


def backfill_openclaw_fts(openclaw_root: Path) -> dict[str, Any]:
    agents = [rebuild_agent(target) for target in build_targets(openclaw_root)]
    return {
        "backfilled_at": datetime_now_iso(),
        "openclaw_root": str(openclaw_root),
        "agents": agents,
    }


def datetime_now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def main() -> int:
    args = parse_args()
    result = backfill_openclaw_fts(Path(args.openclaw_root))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        for agent in result["agents"]:
            print(
                f"{agent['agent_id']}: files={agent['files']} chunks={agent['chunks']} db={agent['db_path']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
