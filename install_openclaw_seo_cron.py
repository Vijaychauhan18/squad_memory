#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


HOME = Path("/Users/vijaychauhan")
DEFAULT_OPENCLAW_ROOT = HOME / ".openclaw"
DEFAULT_WORKSPACE = DEFAULT_OPENCLAW_ROOT / "workspace" / "squad" / "seo"
DEFAULT_CRON_STORE = DEFAULT_OPENCLAW_ROOT / "cron" / "jobs.json"


MANAGED_JOBS = (
    {
        "id": "seo_ops_watchtower",
        "name": "SEO Ops Watchtower",
        "description": "Managed SEO watchtower run for the OpenClaw SEO workspace.",
        "every_ms": 30 * 60 * 1000,
        "prompt_file": "watchtower.md",
        "timeout_seconds": 120,
        "thinking": "low",
    },
    {
        "id": "seo_opportunity_radar",
        "name": "SEO Opportunity Radar",
        "description": "Managed opportunity sweep for the OpenClaw SEO workspace.",
        "every_ms": 2 * 60 * 60 * 1000,
        "prompt_file": "opportunity-radar.md",
        "timeout_seconds": 180,
        "thinking": "medium",
    },
    {
        "id": "seo_daily_ops_plan",
        "name": "SEO Daily Ops Plan",
        "description": "Managed 24-hour SEO execution plan refresh for the OpenClaw SEO workspace.",
        "every_ms": 12 * 60 * 60 * 1000,
        "prompt_file": "daily-ops-plan.md",
        "timeout_seconds": 180,
        "thinking": "medium",
    },
    {
        "id": "seo_workflow_router",
        "name": "SEO Workflow Router",
        "description": "Managed mission-router run for the OpenClaw SEO workspace.",
        "every_ms": 4 * 60 * 60 * 1000,
        "prompt_file": "mission-runner.md",
        "timeout_seconds": 180,
        "thinking": "medium",
    },
    {
        "id": "seo_hq_mission_runner",
        "name": "SEO HQ Mission Runner",
        "description": "Managed HQ planner run for the OpenClaw SEO workspace.",
        "every_ms": 4 * 60 * 60 * 1000,
        "prompt_file": "hq-mission-runner.md",
        "timeout_seconds": 180,
        "thinking": "medium",
    },
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install managed OpenClaw cron jobs for local SEO automation")
    parser.add_argument("--openclaw-root", default=str(DEFAULT_OPENCLAW_ROOT))
    parser.add_argument("--workspace", default=str(DEFAULT_WORKSPACE))
    parser.add_argument("--cron-store", default=str(DEFAULT_CRON_STORE))
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def load_store(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"version": 1, "jobs": []}
    return json.loads(path.read_text(encoding="utf-8"))


def load_prompt(workspace: Path, prompt_filename: str) -> str:
    prompt_path = workspace / "automation" / "prompts" / prompt_filename
    if not prompt_path.exists():
        raise FileNotFoundError(f"Missing prompt file: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8").strip()


def build_job(spec: Dict[str, Any], workspace: Path, existing: Dict[str, Any] | None) -> Dict[str, Any]:
    created_at = existing.get("createdAtMs", now_ms()) if existing else now_ms()
    updated_at = now_ms()
    existing_schedule = existing.get("schedule", {}) if existing else {}
    anchor_ms = existing_schedule.get("anchorMs", created_at)

    return {
        "id": spec["id"],
        "agentId": "seo",
        "name": spec["name"],
        "description": spec["description"],
        "enabled": True,
        "createdAtMs": created_at,
        "updatedAtMs": updated_at,
        "schedule": {
            "kind": "every",
            "everyMs": spec["every_ms"],
            "anchorMs": anchor_ms,
        },
        "sessionTarget": "isolated",
        "wakeMode": "next-heartbeat",
        "payload": {
            "kind": "agentTurn",
            "message": load_prompt(workspace, spec["prompt_file"]),
            "thinking": spec["thinking"],
            "timeoutSeconds": spec["timeout_seconds"],
            "lightContext": True,
        },
        "delivery": {
            "mode": "none",
        },
        "state": existing.get("state", {}) if existing else {},
    }


def install_jobs(workspace: Path, cron_store: Path) -> Dict[str, Any]:
    store = load_store(cron_store)
    existing_by_id = {
        job.get("id"): job
        for job in store.get("jobs", [])
        if isinstance(job, dict) and job.get("id")
    }

    managed_ids = {spec["id"] for spec in MANAGED_JOBS}
    preserved_jobs = [
        job
        for job in store.get("jobs", [])
        if isinstance(job, dict) and job.get("id") not in managed_ids
    ]

    installed_jobs = [
        build_job(spec, workspace, existing_by_id.get(spec["id"]))
        for spec in MANAGED_JOBS
    ]

    next_store = {
        "version": 1,
        "jobs": preserved_jobs + installed_jobs,
    }

    cron_store.parent.mkdir(parents=True, exist_ok=True)
    if cron_store.exists():
        shutil.copy2(cron_store, cron_store.with_suffix(".json.bak"))
    cron_store.write_text(json.dumps(next_store, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    return {
        "status": "ok",
        "cron_store": str(cron_store),
        "managed_job_ids": [job["id"] for job in installed_jobs],
        "managed_job_count": len(installed_jobs),
        "total_jobs": len(next_store["jobs"]),
    }


def main() -> int:
    args = parse_args()
    result = install_jobs(
        workspace=Path(args.workspace),
        cron_store=Path(args.cron_store),
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(
            f"Installed OpenClaw SEO cron jobs | managed={result['managed_job_count']} "
            f"total={result['total_jobs']} store={result['cron_store']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
