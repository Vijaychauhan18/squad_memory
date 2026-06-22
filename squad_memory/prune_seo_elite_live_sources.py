#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Set


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "elite-skills"
DEFAULT_SKILL_ROOT = DEFAULT_SKILLS_ROOT / "seo-elite"
DEFAULT_OUTPUT = DEFAULT_SKILL_ROOT / "memory"
DEFAULT_CONFIG = BASE / "knowledge_sources_seo_elite_live.json"
DEFAULT_STATE = BASE / "ingest" / "seo_elite" / "live" / "state.json"
DEFAULT_RUNS = BASE / "ingest" / "seo_elite" / "live" / "runs"
DEFAULT_PHASE2_DIR = BASE / "ingest" / "seo_elite" / "phase2"
DEFAULT_PHASE3_DIR = BASE / "ingest" / "seo_elite" / "phase3"
DEFAULT_DB = BASE / "seo_elite_memory.db"
DEFAULT_MEMORY_ROUTER = DEFAULT_SKILL_ROOT / "MEMORY.md"
DEFAULT_INDEX = DEFAULT_OUTPUT / "INDEX.md"
DEFAULT_FIXTURES = BASE / "evals" / "fixtures.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prune non-elite live notes and refresh the elite SEO memory router")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--runs-dir", default=str(DEFAULT_RUNS))
    parser.add_argument("--phase2-dir", default=str(DEFAULT_PHASE2_DIR))
    parser.add_argument("--phase3-dir", default=str(DEFAULT_PHASE3_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES))
    parser.add_argument("--memory-router", default=str(DEFAULT_MEMORY_ROUTER))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX))
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_config(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text())
    if "sources" not in payload or not isinstance(payload["sources"], list):
        raise SystemExit(f"Invalid config: {path}")
    return payload


def keep_slugs(config: Dict[str, Any]) -> Set[str]:
    return {str(source["slug"]).strip() for source in config.get("sources", []) if source.get("enabled", True) is not False}


def paths_to_remove(output_dir: Path, keep: Set[str]) -> List[Path]:
    remove: Set[Path] = set()
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


def run_command(command: List[str]) -> Dict[str, Any]:
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def require_success(result: Dict[str, Any], label: str) -> None:
    if int(result["returncode"]) != 0:
        raise SystemExit(f"{label} failed: {result['stderr'] or result['stdout']}")


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    config = load_config(Path(args.config))
    keep = keep_slugs(config)

    removed_paths = paths_to_remove(output_dir, keep)
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
            args.runs_dir,
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

    router_refresh = run_command(
        [
            python,
            str(BASE / "refresh_seo_elite_router.py"),
            "--memory-router",
            args.memory_router,
            "--index-path",
            args.index_path,
            "--output-dir",
            args.output_dir,
            "--skills-root",
            args.skills_root,
            "--db-path",
            args.db_path,
        ]
        + (["--build-db"] if args.build_db else [])
    )
    require_success(router_refresh, "router_refresh")

    result = {
        "kept_slugs": sorted(keep),
        "removed": [str(path) for path in removed_paths],
        "phase2": phase2,
        "phase3": phase3,
        "router_refresh": router_refresh,
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(f"Removed {len(removed_paths)} non-elite live notes.")
        for path in removed_paths:
            print(f"- {path.name}")
        print("Refreshed elite live-source canon, cluster report, router, and vector DB.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
