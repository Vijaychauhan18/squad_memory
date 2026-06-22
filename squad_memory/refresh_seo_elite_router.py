#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "elite-skills"
DEFAULT_SKILL_ROOT = DEFAULT_SKILLS_ROOT / "seo-elite"
DEFAULT_MEMORY_ROUTER = DEFAULT_SKILL_ROOT / "MEMORY.md"
DEFAULT_INDEX = DEFAULT_SKILL_ROOT / "memory" / "INDEX.md"
DEFAULT_OUTPUT = DEFAULT_SKILL_ROOT / "memory"
DEFAULT_DB_PATH = BASE / "seo_elite_memory.db"

MEMORY_BEGIN = "<!-- BEGIN AUTO LIVE SOURCE CANON -->"
MEMORY_END = "<!-- END AUTO LIVE SOURCE CANON -->"
INDEX_BEGIN = "<!-- BEGIN AUTO LIVE SOURCE PIPELINE -->"
INDEX_END = "<!-- END AUTO LIVE SOURCE PIPELINE -->"
TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh the elite SEO router and index without relying on the shared eval gate")
    parser.add_argument("--memory-router", default=str(DEFAULT_MEMORY_ROUTER))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true")
    return parser.parse_args()


def insert_or_replace(text: str, begin: str, end: str, block: str, anchor: str) -> str:
    wrapped = f"{begin}\n{block.rstrip()}\n{end}"
    if begin in text and end in text:
        start = text.index(begin)
        finish = text.index(end, start) + len(end)
        return text[:start] + wrapped + text[finish:]
    if anchor in text:
        return text.replace(anchor, f"{wrapped}\n\n{anchor}", 1)
    return text.rstrip() + "\n\n" + wrapped + "\n"


def read_title(path: Path) -> str:
    text = path.read_text()
    match = TITLE_RE.search(text)
    if not match:
        return path.stem
    return match.group(1).replace("Live Source Canon - ", "").strip()


def canon_notes(output_dir: Path) -> List[Dict[str, str]]:
    notes: List[Dict[str, str]] = []
    for path in sorted(output_dir.glob("live-source-canon-*.md")):
        if path.name == "live-source-canon.md":
            continue
        notes.append({"filename": path.name, "title": read_title(path)})
    return notes


def memory_block(notes: List[Dict[str, str]]) -> str:
    lines = [
        "## Live Pipeline Generated Notes",
        "",
        "### Canonical Live Monitoring Notes",
        "- Live source canon monitor: `memory/live-source-canon.md`",
    ]
    for note in notes:
        lines.append(f"- {note['title']}: `memory/{note['filename']}`")
    lines.append("- Freshness and promotion gate: `memory/live-source-cluster-report.md`")
    lines.append("")
    lines.append("Use these notes for freshness-first source routing before loading durable memory.")
    return "\n".join(lines)


def index_block(notes: List[Dict[str, str]]) -> str:
    lines = [
        "## Live Monitoring Pipeline",
        f"- Last refresh: {datetime.now(timezone.utc).isoformat()}",
        f"- Canon notes: {len(notes)}",
        "",
        "| File | Purpose |",
        "|------|---------|",
        "| [live-source-canon.md](./live-source-canon.md) | Monitoring entrypoint across the elite live source canon notes |",
        "| [live-source-cluster-report.md](./live-source-cluster-report.md) | Freshness clustering and source-eval output |",
    ]
    for note in notes:
        lines.append(f"| [{note['filename']}](./{note['filename']}) | Freshness-first canon for {note['title']} |")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    memory_router = Path(args.memory_router)
    index_path = Path(args.index_path)
    output_dir = Path(args.output_dir)
    notes = canon_notes(output_dir)

    memory_text = memory_router.read_text()
    index_text = index_path.read_text()

    memory_text = insert_or_replace(memory_text, MEMORY_BEGIN, MEMORY_END, memory_block(notes), "## Routing Guide")
    index_text = insert_or_replace(index_text, INDEX_BEGIN, INDEX_END, index_block(notes), "## Archive")

    memory_router.write_text(memory_text)
    index_path.write_text(index_text)

    if args.build_db:
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
        if completed.stdout.strip():
            print(completed.stdout.strip())

    print(f"Memory router: {memory_router}")
    print(f"Index: {index_path}")
    print(f"Notes promoted: {len(notes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
