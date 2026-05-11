#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_CONFIG = BASE / "knowledge_sources.json"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_SUMMARY = DEFAULT_OUTPUT / "live-knowledge-monitor.md"
DEFAULT_SNAPSHOT_DIR = BASE / "ingest" / "raw"
DEFAULT_RUNS_DIR = BASE / "ingest" / "runs"
DEFAULT_STATE_PATH = BASE / "ingest" / "state.json"
DEFAULT_PHASE2_DIR = BASE / "ingest" / "phase2"
DEFAULT_PHASE3_DIR = BASE / "ingest" / "phase3"
DEFAULT_PHASE5_DIR = BASE / "ingest" / "phase5"
DEFAULT_PHASE6_DIR = BASE / "ingest" / "phase6"
DEFAULT_PHASE7_DIR = BASE / "ingest" / "phase7"
DEFAULT_PHASE8_DIR = BASE / "ingest" / "phase8"
DEFAULT_PHASE9_DIR = BASE / "ingest" / "phase9"
DEFAULT_PHASE10_DIR = BASE / "ingest" / "phase10"
DEFAULT_PHASE11_DIR = BASE / "ingest" / "phase11"
DEFAULT_PHASE12_DIR = BASE / "ingest" / "phase12"
DEFAULT_PHASE13_DIR = BASE / "ingest" / "phase13"
DEFAULT_PHASE14_DIR = BASE / "ingest" / "phase14"
DEFAULT_PHASE15_DIR = BASE / "ingest" / "phase15"
DEFAULT_PHASE16_DIR = BASE / "ingest" / "phase16"
DEFAULT_PHASE17_DIR = BASE / "ingest" / "phase17"
DEFAULT_PHASE18_DIR = BASE / "ingest" / "phase18"
DEFAULT_PHASE19_DIR = BASE / "ingest" / "phase19"
DEFAULT_PHASE20_DIR = BASE / "ingest" / "phase20"
DEFAULT_PHASE21_DIR = BASE / "ingest" / "phase21"
DEFAULT_PHASE22_DIR = BASE / "ingest" / "phase22"
DEFAULT_PHASE23_DIR = BASE / "ingest" / "phase23"
DEFAULT_PHASE24_DIR = BASE / "ingest" / "phase24"
DEFAULT_PHASE25_DIR = BASE / "ingest" / "phase25"
DEFAULT_PHASE26_DIR = BASE / "ingest" / "phase26"
DEFAULT_PHASE27_DIR = BASE / "ingest" / "phase27"
DEFAULT_PHASE28_DIR = BASE / "ingest" / "phase28"
DEFAULT_PHASE29_DIR = BASE / "ingest" / "phase29"
DEFAULT_PHASE30_DIR = BASE / "ingest" / "phase30"
DEFAULT_PHASE31_DIR = BASE / "ingest" / "phase31"
DEFAULT_PHASE12_CONFIG = BASE / "knowledge_sources_writer_marketing.json"
DEFAULT_PHASE17_CONFIG = BASE / "knowledge_sources_charles.json"
DEFAULT_PHASE23_CONFIG = BASE / "knowledge_sources_support.json"
DEFAULT_PHASE25_CONFIG = BASE / "knowledge_sources_dev_qa.json"
DEFAULT_PACKS_FILE = BASE / "task_packs.json"
DEFAULT_DB = BASE / "squad_memory.db"
DEFAULT_PHASE31_GRAPH_DB = BASE / "seo_elite_memory.db"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_FIXTURES = BASE / "evals" / "fixtures.json"
DEFAULT_MEMORY_ROUTER = DEFAULT_SKILLS_ROOT / "seo" / "MEMORY.md"
DEFAULT_INDEX = DEFAULT_OUTPUT / "INDEX.md"
DEFAULT_LOCK = BASE / "locks" / "phase_pipeline.lock"
DEFAULT_OPENCLAW_ROOT = HOME / ".openclaw"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Locked end-to-end squad memory pipeline runner")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--summary-path", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--snapshot-dir", default=str(DEFAULT_SNAPSHOT_DIR))
    parser.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    parser.add_argument("--phase2-dir", default=str(DEFAULT_PHASE2_DIR))
    parser.add_argument("--phase3-dir", default=str(DEFAULT_PHASE3_DIR))
    parser.add_argument("--phase5-dir", default=str(DEFAULT_PHASE5_DIR))
    parser.add_argument("--phase6-dir", default=str(DEFAULT_PHASE6_DIR))
    parser.add_argument("--phase7-dir", default=str(DEFAULT_PHASE7_DIR))
    parser.add_argument("--phase8-dir", default=str(DEFAULT_PHASE8_DIR))
    parser.add_argument("--phase9-dir", default=str(DEFAULT_PHASE9_DIR))
    parser.add_argument("--phase10-dir", default=str(DEFAULT_PHASE10_DIR))
    parser.add_argument("--phase11-dir", default=str(DEFAULT_PHASE11_DIR))
    parser.add_argument("--phase12-dir", default=str(DEFAULT_PHASE12_DIR))
    parser.add_argument("--phase13-dir", default=str(DEFAULT_PHASE13_DIR))
    parser.add_argument("--phase14-dir", default=str(DEFAULT_PHASE14_DIR))
    parser.add_argument("--phase15-dir", default=str(DEFAULT_PHASE15_DIR))
    parser.add_argument("--phase16-dir", default=str(DEFAULT_PHASE16_DIR))
    parser.add_argument("--phase17-dir", default=str(DEFAULT_PHASE17_DIR))
    parser.add_argument("--phase18-dir", default=str(DEFAULT_PHASE18_DIR))
    parser.add_argument("--phase19-dir", default=str(DEFAULT_PHASE19_DIR))
    parser.add_argument("--phase20-dir", default=str(DEFAULT_PHASE20_DIR))
    parser.add_argument("--phase21-dir", default=str(DEFAULT_PHASE21_DIR))
    parser.add_argument("--phase22-dir", default=str(DEFAULT_PHASE22_DIR))
    parser.add_argument("--phase23-dir", default=str(DEFAULT_PHASE23_DIR))
    parser.add_argument("--phase24-dir", default=str(DEFAULT_PHASE24_DIR))
    parser.add_argument("--phase25-dir", default=str(DEFAULT_PHASE25_DIR))
    parser.add_argument("--phase26-dir", default=str(DEFAULT_PHASE26_DIR))
    parser.add_argument("--phase27-dir", default=str(DEFAULT_PHASE27_DIR))
    parser.add_argument("--phase28-dir", default=str(DEFAULT_PHASE28_DIR))
    parser.add_argument("--phase29-dir", default=str(DEFAULT_PHASE29_DIR))
    parser.add_argument("--phase30-dir", default=str(DEFAULT_PHASE30_DIR))
    parser.add_argument("--phase31-dir", default=str(DEFAULT_PHASE31_DIR))
    parser.add_argument("--phase12-config", default=str(DEFAULT_PHASE12_CONFIG))
    parser.add_argument("--phase17-config", default=str(DEFAULT_PHASE17_CONFIG))
    parser.add_argument("--phase23-config", default=str(DEFAULT_PHASE23_CONFIG))
    parser.add_argument("--phase25-config", default=str(DEFAULT_PHASE25_CONFIG))
    parser.add_argument("--packs-file", default=str(DEFAULT_PACKS_FILE))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES))
    parser.add_argument("--memory-router", default=str(DEFAULT_MEMORY_ROUTER))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX))
    parser.add_argument("--lock-path", default=str(DEFAULT_LOCK))
    parser.add_argument("--openclaw-sync", action="store_true", help="Mirror Codex memory into OpenClaw after the memory phases")
    parser.add_argument("--openclaw-root", default=str(DEFAULT_OPENCLAW_ROOT))
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    return parser.parse_args()


@contextmanager
def pipeline_lock(path: Path) -> Iterator[Optional[object]]:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("a+")
    acquired = False
    try:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            yield None
            return
        acquired = True
        handle.seek(0)
        handle.truncate()
        handle.write(
            json.dumps(
                {
                    "pid": os.getpid(),
                    "started_at": datetime.now(timezone.utc).isoformat(),
                },
                ensure_ascii=True,
            )
        )
        handle.flush()
        yield handle
    finally:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        handle.close()
        if acquired:
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass


def run_command(name: str, command: List[str]) -> Dict[str, Any]:
    started_at = datetime.now(timezone.utc).isoformat()
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    return {
        "name": name,
        "command": command,
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def build_commands(args: argparse.Namespace) -> List[tuple[str, List[str]]]:
    python = sys.executable
    commands: List[tuple[str, List[str]]] = [
        (
            "phase1",
            [
                python,
                str(BASE / "knowledge_ingest.py"),
                "run",
                "--config",
                args.config,
                "--output-dir",
                args.output_dir,
                "--summary-path",
                args.summary_path,
                "--snapshot-dir",
                args.snapshot_dir,
                "--runs-dir",
                args.runs_dir,
                "--state-path",
                args.state_path,
                "--top",
                str(args.top),
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
            ],
        ),
        (
            "phase2",
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
            ],
        ),
        (
            "phase3",
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
            ],
        ),
        (
            "phase4",
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
            ],
        ),
        (
            "phase5",
            [
                python,
                str(BASE / "phase5_promote_memory.py"),
                "--output-dir",
                args.output_dir,
                "--phase3-manifest",
                str(Path(args.phase3_dir) / "latest.json"),
                "--phase5-dir",
                args.phase5_dir,
                "--state-path",
                str(Path(args.phase5_dir) / "state.json"),
            ],
        ),
        (
            "phase6",
            [
                python,
                str(BASE / "phase6_promote_approved.py"),
                "--output-dir",
                args.output_dir,
                "--phase5-manifest",
                str(Path(args.phase5_dir) / "latest.json"),
                "--phase6-dir",
                args.phase6_dir,
                "--decisions-path",
                str(Path(args.phase6_dir) / "decisions.json"),
                "--state-path",
                str(Path(args.phase6_dir) / "state.json"),
                "--memory-router",
                args.memory_router,
                "--index-path",
                args.index_path,
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase7",
            [
                python,
                str(BASE / "phase7_merge_canon.py"),
                "--output-dir",
                args.output_dir,
                "--phase6-decisions",
                str(Path(args.phase6_dir) / "decisions.json"),
                "--phase7-dir",
                args.phase7_dir,
            ],
        ),
        (
            "phase8",
            [
                python,
                str(BASE / "phase8_promote_canon.py"),
                "--output-dir",
                args.output_dir,
                "--phase6-decisions",
                str(Path(args.phase6_dir) / "decisions.json"),
                "--phase7-registry",
                str(Path(args.phase7_dir) / "canonical_registry.json"),
                "--phase7-dir",
                args.phase7_dir,
                "--phase8-dir",
                args.phase8_dir,
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase9",
            [
                python,
                str(BASE / "phase9_merge_summaries.py"),
                "--output-dir",
                args.output_dir,
                "--phase6-decisions",
                str(Path(args.phase6_dir) / "decisions.json"),
                "--phase7-registry",
                str(Path(args.phase7_dir) / "canonical_registry.json"),
                "--phase7-dir",
                args.phase7_dir,
                "--phase8-dir",
                args.phase8_dir,
                "--phase9-dir",
                args.phase9_dir,
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase10",
            [
                python,
                str(BASE / "phase10_fuse_evidence.py"),
                "--output-dir",
                args.output_dir,
                "--phase7-registry",
                str(Path(args.phase7_dir) / "canonical_registry.json"),
                "--phase10-dir",
                args.phase10_dir,
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase11",
            [
                python,
                str(BASE / "phase11_bootstrap_writer_marketing.py"),
                "--skills-root",
                args.skills_root,
                "--phase11-dir",
                args.phase11_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase12",
            [
                python,
                str(BASE / "phase12_external_writer_marketing.py"),
                "--config",
                args.phase12_config,
                "--skills-root",
                args.skills_root,
                "--phase12-dir",
                args.phase12_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase13",
            [
                python,
                str(BASE / "phase13_promote_writer_marketing.py"),
                "--skills-root",
                args.skills_root,
                "--phase12-manifest",
                str(Path(args.phase12_dir) / "latest.json"),
                "--phase13-dir",
                args.phase13_dir,
                "--state-path",
                str(Path(args.phase13_dir) / "state.json"),
            ],
        ),
        (
            "phase14",
            [
                python,
                str(BASE / "phase14_promote_writer_marketing_approved.py"),
                "--phase13-manifest",
                str(Path(args.phase13_dir) / "latest.json"),
                "--phase14-dir",
                args.phase14_dir,
                "--decisions-path",
                str(Path(args.phase14_dir) / "decisions.json"),
                "--state-path",
                str(Path(args.phase14_dir) / "state.json"),
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase15",
            [
                python,
                str(BASE / "phase15_outcome_telemetry.py"),
                "--phase15-dir",
                args.phase15_dir,
                "--db-path",
                args.db_path,
            ],
        ),
        (
            "phase16",
            [
                python,
                str(BASE / "phase16_bootstrap_charles.py"),
                "--skills-root",
                args.skills_root,
                "--phase16-dir",
                args.phase16_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase17",
            [
                python,
                str(BASE / "phase17_external_charles.py"),
                "--config",
                args.phase17_config,
                "--skills-root",
                args.skills_root,
                "--phase17-dir",
                args.phase17_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase18",
            [
                python,
                str(BASE / "phase18_promote_charles.py"),
                "--skills-root",
                args.skills_root,
                "--phase17-manifest",
                str(Path(args.phase17_dir) / "latest.json"),
                "--phase18-dir",
                args.phase18_dir,
                "--state-path",
                str(Path(args.phase18_dir) / "state.json"),
            ],
        ),
        (
            "phase19",
            [
                python,
                str(BASE / "phase19_promote_charles_approved.py"),
                "--phase18-manifest",
                str(Path(args.phase18_dir) / "latest.json"),
                "--phase19-dir",
                args.phase19_dir,
                "--decisions-path",
                str(Path(args.phase19_dir) / "decisions.json"),
                "--state-path",
                str(Path(args.phase19_dir) / "state.json"),
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase20",
            [
                python,
                str(BASE / "phase20_triage_charles_queue.py"),
                "--phase19-manifest",
                str(Path(args.phase19_dir) / "latest.json"),
                "--decisions-path",
                str(Path(args.phase19_dir) / "decisions.json"),
                "--phase20-dir",
                args.phase20_dir,
            ],
        ),
        (
            "phase22",
            [
                python,
                str(BASE / "phase22_bootstrap_support.py"),
                "--skills-root",
                args.skills_root,
                "--phase22-dir",
                args.phase22_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase23",
            [
                python,
                str(BASE / "phase23_external_support.py"),
                "--config",
                args.phase23_config,
                "--skills-root",
                args.skills_root,
                "--phase23-dir",
                args.phase23_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase24",
            [
                python,
                str(BASE / "phase24_bootstrap_dev_qa.py"),
                "--skills-root",
                args.skills_root,
                "--phase24-dir",
                args.phase24_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase25",
            [
                python,
                str(BASE / "phase25_external_dev_qa.py"),
                "--config",
                args.phase25_config,
                "--skills-root",
                args.skills_root,
                "--phase25-dir",
                args.phase25_dir,
                "--db-path",
                args.db_path,
                "--build-db",
            ],
        ),
        (
            "phase26",
            [
                python,
                str(BASE / "phase26_promote_dev_qa.py"),
                "--skills-root",
                args.skills_root,
                "--phase25-manifest",
                str(Path(args.phase25_dir) / "latest.json"),
                "--phase26-dir",
                args.phase26_dir,
            ],
        ),
        (
            "phase27",
            [
                python,
                str(BASE / "phase27_promote_dev_qa_approved.py"),
                "--phase26-manifest",
                str(Path(args.phase26_dir) / "latest.json"),
                "--phase27-dir",
                args.phase27_dir,
                "--decisions-path",
                str(Path(args.phase27_dir) / "decisions.json"),
                "--state-path",
                str(Path(args.phase27_dir) / "state.json"),
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
            ],
        ),
        (
            "phase28",
            [
                python,
                str(BASE / "phase28_triage_dev_qa_queue.py"),
                "--phase27-manifest",
                str(Path(args.phase27_dir) / "latest.json"),
                "--decisions-path",
                str(Path(args.phase27_dir) / "decisions.json"),
                "--phase28-dir",
                args.phase28_dir,
            ],
        ),
        (
            "phase29",
            [
                python,
                str(BASE / "phase29_task_result_eval.py"),
                "--phase29-dir",
                args.phase29_dir,
                "--db-path",
                args.db_path,
                "--packs-file",
                args.packs_file,
            ],
        ),
        (
            "phase30",
            [
                python,
                str(BASE / "phase30_scorecard_learning.py"),
                "--phase30-dir",
                args.phase30_dir,
                "--db-path",
                args.db_path,
                "--packs-file",
                args.packs_file,
            ],
        ),
        (
            "phase21",
            [
                python,
                str(BASE / "phase21_control_plane.py"),
                "report",
                "--phase21-dir",
                args.phase21_dir,
                "--ingest-root",
                str(Path(args.phase21_dir).parent),
                "--skills-root",
                args.skills_root,
                "--db-path",
                args.db_path,
                "--packs-file",
                args.packs_file,
                "--fixtures",
                args.fixtures,
                "--limit",
                "5",
            ],
        ),
        (
            "phase31",
            [
                python,
                str(BASE / "phase31_memory_graph.py"),
                "build",
                "--phase31-dir",
                args.phase31_dir,
                "--phase21-status",
                str(Path(args.phase21_dir) / "control_plane_status.json"),
                "--ingest-root",
                str(Path(args.phase21_dir).parent),
                "--db-path",
                str(DEFAULT_PHASE31_GRAPH_DB if DEFAULT_PHASE31_GRAPH_DB.exists() else Path(args.db_path)),
                "--packs-file",
                args.packs_file,
            ],
        ),
    ]
    if args.openclaw_sync:
        commands.append(
            (
                "openclaw_sync",
                [
                    python,
                    str(BASE / "refresh_openclaw_memory.py"),
                    "--codex-root",
                    str(Path(args.skills_root).parent),
                    "--openclaw-root",
                    args.openclaw_root,
                ],
            )
        )
    return commands


def run_pipeline(args: argparse.Namespace) -> Dict[str, Any]:
    with pipeline_lock(Path(args.lock_path)) as lock_handle:
        if lock_handle is None:
            return {
                "status": "skipped_locked",
                "started_at": datetime.now(timezone.utc).isoformat(),
                "lock_path": args.lock_path,
                "phases": [],
            }

        phases: List[Dict[str, Any]] = []
        status = "ok"
        for name, command in build_commands(args):
            result = run_command(name, command)
            phases.append(result)
            if result["returncode"] != 0:
                status = "failed"
                break

        return {
            "status": status,
            "started_at": datetime.now(timezone.utc).isoformat(),
            "lock_path": args.lock_path,
            "phases": phases,
        }


def print_result(result: Dict[str, Any]) -> None:
    print(f"Status: {result['status']}")
    print(f"Lock: {result['lock_path']}")
    for phase in result["phases"]:
        print(f"- {phase['name']}: rc={phase['returncode']}")
        if phase["stdout"]:
            print(phase["stdout"])
        if phase["stderr"]:
            print(phase["stderr"])


def main() -> int:
    args = parse_args()
    result = run_pipeline(args)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0 if result["status"] in {"ok", "skipped_locked"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
