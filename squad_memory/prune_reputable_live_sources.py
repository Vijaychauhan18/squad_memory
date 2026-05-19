#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Sequence, Set


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_CONFIG = BASE / "knowledge_sources.json"
DEFAULT_STATE = BASE / "ingest" / "reputable" / "state.json"
DEFAULT_PHASE2_DIR = BASE / "ingest" / "reputable" / "phase2"
DEFAULT_PHASE3_DIR = BASE / "ingest" / "reputable" / "phase3"
DEFAULT_DB = BASE / "squad_memory.db"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_FIXTURES = BASE / "evals" / "fixtures.json"
DEFAULT_MEMORY_ROUTER = DEFAULT_SKILLS_ROOT / "seo" / "MEMORY.md"
DEFAULT_INDEX = DEFAULT_OUTPUT / "INDEX.md"

KEEP_SLUGS = (
    "google-search-central",
    "ahrefs",
    "dejan",
    "gsqi",
    "marie",
    "lily",
    "mobilemoxie",
    "brodie",
    "ipullrank",
    "jono",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prune low-priority live SEO source notes and refresh the reputable-only layer")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--phase2-dir", default=str(DEFAULT_PHASE2_DIR))
    parser.add_argument("--phase3-dir", default=str(DEFAULT_PHASE3_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES))
    parser.add_argument("--memory-router", default=str(DEFAULT_MEMORY_ROUTER))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX))
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def paths_to_remove(output_dir: Path, keep_slugs: Sequence[str]) -> List[Path]:
    keep = set(keep_slugs)
    remove: Set[Path] = set()

    # The strict reputable layer uses `live-source-*` notes.
    # Remove the older `live-seo-feed-*` notes entirely so they cannot leak
    # excluded sources back into the canonicalizer.
    for path in sorted(output_dir.glob("live-seo-feed-*.md")):
        remove.add(path)

    for pattern in ("live-source-*.md", "live-source-canon-*.md"):
        for path in sorted(output_dir.glob(pattern)):
            name = path.stem
            if name in {"live-source-canon", "live-source-cluster-report"}:
                continue
            if name.startswith("live-source-canon-"):
                slug = name[len("live-source-canon-") :]
            elif name.startswith("live-source-"):
                slug = name[len("live-source-") :]
            else:
                continue
            if slug not in keep:
                remove.add(path)
    return sorted(remove)


def run_command(command: List[str]) -> Dict[str, object]:
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def require_success(result: Dict[str, object], label: str) -> None:
    if int(result["returncode"]) != 0:
        raise SystemExit(f"{label} failed: {result['stderr'] or result['stdout']}")


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    removed_paths = paths_to_remove(output_dir, KEEP_SLUGS)
    for path in removed_paths:
        path.unlink(missing_ok=True)

    python = sys.executable
    phase2 = run_command(
        [
            python,
            str(BASE / "phase2_canonicalize.py"),
            "--config",
            args.config,
            "--output-dir",
            args.output_dir,
            "--state-path",
            args.state_path,
            "--runs-dir",
            str(BASE / "ingest" / "reputable" / "runs"),
            "--phase2-dir",
            args.phase2_dir,
            "--top",
            "5",
        ]
    )
    require_success(phase2, "phase2")

    phase3 = run_command(
        [
            python,
            str(BASE / "phase3_cluster_refresh.py"),
            "--output-dir",
            args.output_dir,
            "--skills-root",
            args.skills_root,
            "--db-path",
            args.db_path,
            "--fixtures",
            args.fixtures,
            "--phase2-manifest",
            str(Path(args.phase2_dir) / "latest.json"),
            "--phase3-dir",
            args.phase3_dir,
        ]
    )
    require_success(phase3, "phase3")

    phase4 = run_command(
        [
            python,
            str(BASE / "phase4_router_refresh.py"),
            "--memory-router",
            args.memory_router,
            "--index-path",
            args.index_path,
            "--output-dir",
            args.output_dir,
            "--phase3-manifest",
            str(Path(args.phase3_dir) / "latest.json"),
            "--skills-root",
            args.skills_root,
            "--db-path",
            args.db_path,
            "--build-db",
        ]
    )
    require_success(phase4, "phase4")

    result = {
        "kept_slugs": list(KEEP_SLUGS),
        "removed": [str(path) for path in removed_paths],
        "phase2": phase2,
        "phase3": phase3,
        "phase4": phase4,
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(f"Removed {len(removed_paths)} low-priority live notes.")
        for path in removed_paths:
            print(f"- {path.name}")
        print("Refreshed live-source canon, cluster report, router, and vector DB.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
