#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


HOME = Path.home()
DEFAULT_MEMORY_ROUTER = HOME / ".codex" / "skills" / "seo" / "MEMORY.md"
DEFAULT_INDEX = HOME / ".codex" / "skills" / "seo" / "memory" / "INDEX.md"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE3 = HOME / "squad_memory" / "ingest" / "phase3" / "latest.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = HOME / "squad_memory" / "squad_memory.db"

MEMORY_BEGIN = "<!-- BEGIN AUTO LIVE SOURCE CANON -->"
MEMORY_END = "<!-- END AUTO LIVE SOURCE CANON -->"
INDEX_BEGIN = "<!-- BEGIN AUTO LIVE SOURCE PIPELINE -->"
INDEX_END = "<!-- END AUTO LIVE SOURCE PIPELINE -->"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 4 router refresh for live source monitoring")
    parser.add_argument("--memory-router", default=str(DEFAULT_MEMORY_ROUTER))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase3-manifest", default=str(DEFAULT_PHASE3))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true", help="Rebuild squad_memory after refreshing router files")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def insert_or_replace(text: str, begin: str, end: str, block: str, anchor: str) -> str:
    wrapped = f"{begin}\n{block.rstrip()}\n{end}"
    if begin in text and end in text:
        start = text.index(begin)
        finish = text.index(end, start) + len(end)
        return text[:start] + wrapped + text[finish:]
    if anchor in text:
        return text.replace(anchor, f"{wrapped}\n\n{anchor}", 1)
    return text.rstrip() + "\n\n" + wrapped + "\n"


def memory_block(manifest: Dict[str, Any]) -> str:
    lines = [
        "## Live Pipeline Generated Notes",
        "",
        "### Canonical Live Monitoring Notes",
        f"- Live source canon monitor: `memory/live-source-canon.md`",
    ]
    for item in manifest.get("notes", []):
        lines.append(f"- {item['title'].replace('Live Source Canon - ', '')}: `memory/{item['filename']}`")
    lines.append("- Freshness and promotion gate: `memory/live-source-cluster-report.md`")
    lines.append("")
    lines.append("Use these notes for freshness-first source routing before loading durable memory.")
    return "\n".join(lines)


def index_block(manifest: Dict[str, Any]) -> str:
    gate = manifest.get("gate", {})
    lines = [
        "## Live Monitoring Pipeline",
        f"- Last refresh: {manifest.get('generated_at', '')}",
        f"- Eval gate: {'approved' if gate.get('approved') else 'blocked'}",
        f"- Primary accuracy: {gate.get('primary_accuracy', 0.0):.2f}",
        f"- Top-3 skill hit: {gate.get('top3_skill_hit', 0.0):.2f}",
        f"- Top-5 path hit: {gate.get('top5_path_hit', 0.0):.2f}",
        "",
        "| File | Purpose |",
        "|------|---------|",
        "| [live-source-canon.md](./live-source-canon.md) | Monitoring entrypoint across the live source canon notes |",
        "| [live-source-cluster-report.md](./live-source-cluster-report.md) | Freshness, clustering, and eval-gate status |",
    ]
    for item in manifest.get("notes", []):
        lines.append(f"| [{item['filename']}](./{item['filename']}) | Freshness-first canon for {item['topic']} |")
    return "\n".join(lines)


def refresh(memory_router: Path, index_path: Path, phase3_manifest: Path, skills_root: Path, db_path: Path, build_db: bool) -> Dict[str, Any]:
    manifest = load_json(phase3_manifest, {})
    if not manifest:
        raise SystemExit(f"Missing Phase 3 manifest: {phase3_manifest}")
    if not manifest.get("gate", {}).get("approved"):
        raise SystemExit("Phase 3 eval gate is blocked; router refresh aborted")

    memory_text = memory_router.read_text()
    index_text = index_path.read_text()

    memory_text = insert_or_replace(memory_text, MEMORY_BEGIN, MEMORY_END, memory_block(manifest), "## Routing Guide")
    index_text = insert_or_replace(index_text, INDEX_BEGIN, INDEX_END, index_block(manifest), "## AI Search & Visibility")

    memory_router.write_text(memory_text)
    index_path.write_text(index_text)

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "memory_router": str(memory_router),
        "index_path": str(index_path),
        "phase3_manifest": str(phase3_manifest),
        "note_count": len(manifest.get("notes", [])),
        "gate": manifest.get("gate", {}),
    }
    if build_db:
        completed = subprocess.run(
            [
                sys.executable,
                str(HOME / "squad_memory" / "squad_memory.py"),
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
        if completed.returncode != 0:
            raise SystemExit(completed.returncode)
        result["build"] = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
        }
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Memory router: {result['memory_router']}")
    print(f"Index: {result['index_path']}")
    print(f"Notes promoted: {result['note_count']}")
    print(f"Gate approved: {result['gate'].get('approved')}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = refresh(
        memory_router=Path(args.memory_router),
        index_path=Path(args.index_path),
        phase3_manifest=Path(args.phase3_manifest),
        skills_root=Path(args.skills_root),
        db_path=Path(args.db_path),
        build_db=args.build_db,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
