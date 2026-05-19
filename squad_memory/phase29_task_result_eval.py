#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from squad_memory import DB_PATH, TASK_PACKS_PATH, sync_task_result_suggestions, task_result_report


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_PHASE29_DIR = BASE / "ingest" / "phase29"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 29 real-task result evaluation and scorecard sync")
    parser.add_argument("--phase29-dir", default=str(DEFAULT_PHASE29_DIR))
    parser.add_argument("--db-path", default=str(DB_PATH))
    parser.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def format_score(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.2f}"


def build_report(sync_summary: Dict[str, Any], result: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Phase 29 Task Result Evaluation",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Summary",
        f"- Task outcomes tracked: {result['task_outcomes']}",
        f"- Manual scorecards: {result['manual_scorecards']}",
        f"- Suggested scorecards: {result['suggested_scorecards']}",
        f"- Pending manual reviews: {result['pending_manual_reviews']}",
        f"- Avg overall score (manual): {format_score(result['avg_overall_manual'])}",
        f"- Avg overall score (all scorecards): {format_score(result['avg_overall_all'])}",
        f"- Suggestions inserted: {sync_summary['inserted_suggestions']}",
        f"- Suggestions updated: {sync_summary['updated_suggestions']}",
        "",
        "## Verdict Breakdown",
    ]
    if result["verdict_breakdown"]:
        for item in result["verdict_breakdown"]:
            lines.append(f"- {item['verdict']}: {item['count']}")
    else:
        lines.append("- No scorecards yet.")

    lines.extend(["", "## Pending Manual Reviews"])
    if result["pending_reviews"]:
        for item in result["pending_reviews"][:10]:
            lines.append(
                f"- outcome={item['outcome_id']} | `{item['pack_id']}` ({item['pack_name']}) "
                f"| suggested={item['suggested_overall_score']:.2f} | verdict={item['suggested_verdict']}"
            )
            lines.append(f"  query={item['query']}")
    else:
        lines.append("- No pending manual reviews.")

    lines.extend(["", "## Top Scored Packs"])
    if result["top_packs"]:
        for item in result["top_packs"][:8]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): avg_score={item['avg_overall_score']:.2f}, count={item['count']}"
            )
    else:
        lines.append("- No scored pack data yet.")

    lines.extend(["", "## Weak Scored Packs"])
    if result["weak_packs"]:
        for item in result["weak_packs"][:8]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): avg_score={item['avg_overall_score']:.2f}, count={item['count']}"
            )
    else:
        lines.append("- No weak scored packs yet.")

    lines.extend(["", "## Top Scored Paths"])
    if result["top_paths"]:
        for item in result["top_paths"][:8]:
            lines.append(f"- `{item['path']}`: avg_score={item['avg_overall_score']:.2f}, count={item['count']}")
    else:
        lines.append("- No scored path data yet.")

    lines.extend(["", "## Recent Scorecards"])
    if result["recent_scorecards"]:
        for item in result["recent_scorecards"][:8]:
            lines.append(
                f"- outcome={item['outcome_id']} | `{item['pack_id']}` | mode={item['scoring_mode']} "
                f"| score={item['overall_score']:.2f} | verdict={item['verdict']}"
            )
    else:
        lines.append("- No scorecards recorded yet.")

    return "\n".join(lines).rstrip() + "\n"


def build_queue(result: Dict[str, Any]) -> str:
    lines: List[str] = [
        "---",
        "source: local phase29 task result evaluation",
        "title: Task Result Scorecard Review Queue",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase29, task_result_eval, scorecard_review",
        "topic: task_result_eval_queue",
        "intent: maintenance, review, output_scoring",
        "role: pinchy, reviewer, qa, developer, writer, seo, marketing, charles",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Task result evaluation queue",
        "use_for: scorecard_review, output_quality_maintenance",
        "avoid_for: direct_execution_without_review",
        "---",
        "",
        "# Task Result Scorecard Review Queue",
        "",
    ]
    if not result["pending_reviews"]:
        lines.append("- No pending manual reviews.")
    for item in result["pending_reviews"][:20]:
        lines.append(
            f"- outcome={item['outcome_id']} | `{item['pack_id']}` | suggested={item['suggested_overall_score']:.2f} "
            f"| verdict={item['suggested_verdict']} | skill={item['primary_skill']}"
        )
        lines.append(f"  query={item['query']}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    phase29_dir = Path(args.phase29_dir)
    db_path = Path(args.db_path)
    packs_path = Path(args.packs_file)
    phase29_dir.mkdir(parents=True, exist_ok=True)

    sync_summary = sync_task_result_suggestions(db_path)
    result = task_result_report(db_path, packs_path, args.limit)
    generated_at = datetime.now(timezone.utc).isoformat()

    ledger = {
        "generated_at": generated_at,
        "phase29_dir": str(phase29_dir),
        "db_path": str(db_path),
        "packs_file": str(packs_path),
        "sync_summary": sync_summary,
        "task_result_report": result,
    }
    ledger_path = phase29_dir / "task_result_eval_ledger.json"
    report_path = phase29_dir / "task_result_eval_report.md"
    queue_path = phase29_dir / "scorecard_review_queue.md"
    latest_path = phase29_dir / "latest.json"

    write_json(ledger_path, ledger)
    report_path.write_text(build_report(sync_summary, result), encoding="utf-8")
    queue_path.write_text(build_queue(result), encoding="utf-8")
    latest_payload = {
        "generated_at": generated_at,
        "phase29_dir": str(phase29_dir),
        "db_path": str(db_path),
        "task_outcomes": result["task_outcomes"],
        "manual_scorecards": result["manual_scorecards"],
        "suggested_scorecards": result["suggested_scorecards"],
        "pending_manual_reviews": result["pending_manual_reviews"],
        "avg_overall_manual": result["avg_overall_manual"],
        "avg_overall_all": result["avg_overall_all"],
        "top_packs": [item["pack_id"] for item in result["top_packs"][:5]],
        "top_paths": [item["path"] for item in result["top_paths"][:5]],
        "report_path": str(report_path),
        "queue_path": str(queue_path),
        "ledger_path": str(ledger_path),
    }
    write_json(latest_path, latest_payload)

    payload = {
        "generated_at": generated_at,
        "phase29_dir": str(phase29_dir),
        "sync_summary": sync_summary,
        "task_result_summary": {
            "task_outcomes": result["task_outcomes"],
            "manual_scorecards": result["manual_scorecards"],
            "suggested_scorecards": result["suggested_scorecards"],
            "pending_manual_reviews": result["pending_manual_reviews"],
            "avg_overall_manual": result["avg_overall_manual"],
            "avg_overall_all": result["avg_overall_all"],
        },
        "ledger_path": str(ledger_path),
        "report_path": str(report_path),
        "queue_path": str(queue_path),
        "latest_path": str(latest_path),
    }
    print(json.dumps(payload, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
