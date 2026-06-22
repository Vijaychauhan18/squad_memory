#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from squad_memory import TASK_PACKS_PATH, DB_PATH, outcome_report, pack_report, train_usage_priors


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_PHASE15_DIR = BASE / "ingest" / "phase15"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 15 real-task telemetry and outcome learning")
    parser.add_argument("--phase15-dir", default=str(DEFAULT_PHASE15_DIR))
    parser.add_argument("--db-path", default=str(DB_PATH))
    parser.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def format_metric(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.2f}"


def build_report(train_summary: Dict[str, Any], outcome: Dict[str, Any], pack: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Phase 15 Outcome Telemetry",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Summary",
        f"- Task outcomes tracked: {outcome['task_outcomes']}",
        f"- Avg revisions per task: {format_metric(outcome['averages']['avg_revision_count'])}",
        f"- Avg completion minutes: {format_metric(outcome['averages']['avg_completion_minutes'])}",
        f"- Avg user rating: {format_metric(outcome['averages']['avg_user_rating'])}",
        f"- Outcome path priors trained: {train_summary.get('outcome_path_priors', 0)}",
        f"- Outcome skill priors trained: {train_summary.get('outcome_skill_priors', 0)}",
        "",
        "## Status Breakdown",
    ]
    if outcome["status_breakdown"]:
        for item in outcome["status_breakdown"]:
            lines.append(f"- {item['status']}: {item['count']} ({item['rate']:.1%})")
    else:
        lines.append("- No completed task outcomes yet.")

    if outcome["last_outcome"]:
        last = outcome["last_outcome"]
        lines.extend(
            [
                "",
                "## Latest Outcome",
                f"- Pack: `{last['pack_id']}` ({last['pack_name']})",
                f"- Status: `{last['status']}`",
                f"- Revisions: {last['revision_count']}",
                f"- User rating: {format_metric(last['user_rating'])}",
                f"- Query: {last['query']}",
            ]
        )
        if last["notes"]:
            lines.append(f"- Notes: {last['notes']}")

    lines.extend(["", "## Strongest Packs"])
    if pack["top_packs"]:
        for item in pack["top_packs"][:5]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): score={item['score']:.3f}, "
                f"accepted={item['accepted_count']}, revised={item['revised_count']}, failed={item['failed_count']}"
            )
    else:
        lines.append("- No pack performance yet.")

    lines.extend(["", "## High Revision Packs"])
    if outcome["high_revision_packs"]:
        for item in outcome["high_revision_packs"][:5]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): outcomes={item['outcomes']}, "
                f"avg_revisions={item['avg_revision_count']:.2f}, avg_rating={format_metric(item['avg_user_rating'])}"
            )
    else:
        lines.append("- No revision-heavy pack patterns yet.")

    lines.extend(["", "## Strongest Memory Notes"])
    if outcome["top_outcome_paths"]:
        for item in outcome["top_outcome_paths"][:8]:
            lines.append(
                f"- `{item['path']}`: score={item['score']:.3f}, "
                f"accepted={item['accepted_count']}, revised={item['revised_count']}, failed={item['failed_count']}"
            )
    else:
        lines.append("- No note-level outcome signal yet.")

    lines.extend(["", "## Weak Or Risky Memory Notes"])
    if outcome["weak_outcome_paths"]:
        for item in outcome["weak_outcome_paths"][:8]:
            lines.append(
                f"- `{item['path']}`: score={item['score']:.3f}, "
                f"accepted={item['accepted_count']}, revised={item['revised_count']}, failed={item['failed_count']}"
            )
    else:
        lines.append("- No weak note patterns yet.")

    lines.extend(["", "## Over-Ranked Paths"])
    if outcome["overranked_paths"]:
        for item in outcome["overranked_paths"][:8]:
            lines.append(
                f"- `{item['path']}`: retrieval_score={item['retrieval_score']:.3f}, "
                f"outcome_score={item['outcome_score']:.3f}, retrieval_exposure={item['retrieval_exposure_count']}"
            )
    else:
        lines.append("- No over-ranked path risk detected yet.")

    lines.extend(["", "## Underused Winners"])
    if outcome["underused_winners"]:
        for item in outcome["underused_winners"][:8]:
            lines.append(
                f"- `{item['path']}`: outcome_score={item['outcome_score']:.3f}, "
                f"retrieval_score={item['retrieval_score']:.3f}, outcome_exposure={item['outcome_exposure_count']}"
            )
    else:
        lines.append("- No underused winners detected yet.")

    lines.extend(["", "## Strongest Skills"])
    if outcome["top_outcome_skills"]:
        for item in outcome["top_outcome_skills"][:8]:
            lines.append(
                f"- `{item['skill']}`: score={item['score']:.3f}, "
                f"accepted={item['accepted_count']}, revised={item['revised_count']}, failed={item['failed_count']}"
            )
    else:
        lines.append("- No skill-level outcome signal yet.")

    lines.extend(["", "## Skill Stacks"])
    if outcome["top_skill_stacks"]:
        for item in outcome["top_skill_stacks"][:8]:
            lines.append(f"- `{', '.join(item['skills'])}`: outcomes={item['outcomes']}")
    else:
        lines.append("- No repeated skill stacks yet.")

    lines.extend(["", "## Recent Outcomes"])
    if outcome["recent_outcomes"]:
        for item in outcome["recent_outcomes"][:8]:
            lines.append(
                f"- {item['ts']} | `{item['pack_id']}` | {item['status']} | "
                f"`{item['primary_skill']}` | revisions={item['revision_count']} | query={item['query']}"
            )
    else:
        lines.append("- No recent outcomes yet.")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    phase15_dir = Path(args.phase15_dir)
    db_path = Path(args.db_path)
    packs_path = Path(args.packs_file)
    phase15_dir.mkdir(parents=True, exist_ok=True)

    train_summary = train_usage_priors(db_path)
    outcome = outcome_report(db_path, packs_path, args.limit)
    pack = pack_report(db_path, packs_path, args.limit)

    generated_at = datetime.now(timezone.utc).isoformat()
    ledger = {
        "generated_at": generated_at,
        "phase15_dir": str(phase15_dir),
        "db_path": str(db_path),
        "packs_file": str(packs_path),
        "train_summary": train_summary,
        "outcome_report": outcome,
        "pack_report": pack,
    }
    ledger_path = phase15_dir / "outcome_telemetry_ledger.json"
    report_path = phase15_dir / "outcome_telemetry_report.md"
    latest_path = phase15_dir / "latest.json"

    write_json(ledger_path, ledger)
    report_path.write_text(build_report(train_summary, outcome, pack), encoding="utf-8")
    write_json(
        latest_path,
        {
            "generated_at": generated_at,
            "phase15_dir": str(phase15_dir),
            "db_path": str(db_path),
            "task_outcomes": outcome["task_outcomes"],
            "status_breakdown": outcome["status_breakdown"],
            "top_outcome_paths": [item["path"] for item in outcome["top_outcome_paths"][:5]],
            "top_outcome_skills": [item["skill"] for item in outcome["top_outcome_skills"][:5]],
            "top_packs": [item["pack_id"] for item in pack["top_packs"][:5]],
            "report_path": str(report_path),
            "ledger_path": str(ledger_path),
        },
    )

    payload = {
        "generated_at": generated_at,
        "phase15_dir": str(phase15_dir),
        "db_path": str(db_path),
        "task_outcomes": outcome["task_outcomes"],
        "status_breakdown": outcome["status_breakdown"],
        "ledger_path": str(ledger_path),
        "report_path": str(report_path),
        "latest_path": str(latest_path),
        "top_outcome_paths": outcome["top_outcome_paths"][:5],
        "top_outcome_skills": outcome["top_outcome_skills"][:5],
        "top_packs": pack["top_packs"][:5],
        "overranked_paths": outcome["overranked_paths"][:5],
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
