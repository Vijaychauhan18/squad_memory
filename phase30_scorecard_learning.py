#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from squad_memory import DB_PATH, TASK_PACKS_PATH, task_result_report, train_result_priors


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_PHASE30_DIR = BASE / "ingest" / "phase30"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 30 scorecard-driven learning and reporting")
    parser.add_argument("--phase30-dir", default=str(DEFAULT_PHASE30_DIR))
    parser.add_argument("--db-path", default=str(DB_PATH))
    parser.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def fmt(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.2f}"


def build_report(train_summary: Dict[str, Any], result: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Phase 30 Scorecard Learning",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Summary",
        f"- Scored outcomes: {result['scored_outcomes']}",
        f"- Manual scorecards: {result['manual_scorecards']}",
        f"- Suggested scorecards: {result['suggested_scorecards']}",
        f"- Pending manual reviews: {result['pending_manual_reviews']}",
        f"- Avg overall score (manual): {fmt(result['avg_overall_manual'])}",
        f"- Avg overall score (all scorecards): {fmt(result['avg_overall_all'])}",
        f"- Learned result pack priors: {train_summary['result_pack_priors']}",
        f"- Learned result path priors: {train_summary['result_path_priors']}",
        f"- Learned result skill priors: {train_summary['result_skill_priors']}",
        "",
        "## Top Learned Pack Priors",
    ]
    if result["top_learned_packs"]:
        for item in result["top_learned_packs"][:8]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): score={item['score']:.3f}, "
                f"avg_score={item['avg_overall_score']:.2f}, manual={item['manual_count']}, "
                f"suggested={item['suggested_count']}, exposure={item['exposure_count']}"
            )
    else:
        lines.append("- No learned pack priors yet.")

    lines.extend(["", "## Weak Learned Pack Priors"])
    if result["weak_learned_packs"]:
        for item in result["weak_learned_packs"][:8]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): score={item['score']:.3f}, "
                f"avg_score={item['avg_overall_score']:.2f}, manual={item['manual_count']}, "
                f"suggested={item['suggested_count']}, exposure={item['exposure_count']}"
            )
    else:
        lines.append("- No weak learned pack priors yet.")

    lines.extend(["", "## Top Learned Paths"])
    if result["top_learned_paths"]:
        for item in result["top_learned_paths"][:8]:
            lines.append(
                f"- `{item['path']}`: score={item['score']:.3f}, avg_score={item['avg_overall_score']:.2f}, "
                f"manual={item['manual_count']}, suggested={item['suggested_count']}, exposure={item['exposure_count']}"
            )
    else:
        lines.append("- No learned path priors yet.")

    lines.extend(["", "## Top Learned Skills"])
    if result["top_learned_skills"]:
        for item in result["top_learned_skills"][:8]:
            lines.append(
                f"- `{item['skill']}`: score={item['score']:.3f}, avg_score={item['avg_overall_score']:.2f}, "
                f"manual={item['manual_count']}, suggested={item['suggested_count']}, exposure={item['exposure_count']}"
            )
    else:
        lines.append("- No learned skill priors yet.")

    lines.extend(["", "## Weak Scored Packs"])
    if result["weak_packs"]:
        for item in result["weak_packs"][:8]:
            lines.append(
                f"- `{item['pack_id']}` ({item['pack_name']}): avg_score={item['avg_overall_score']:.2f}, count={item['count']}"
            )
    else:
        lines.append("- No weak scored packs yet.")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    phase30_dir = Path(args.phase30_dir)
    db_path = Path(args.db_path)
    packs_path = Path(args.packs_file)
    phase30_dir.mkdir(parents=True, exist_ok=True)

    train_summary = train_result_priors(db_path)
    result = task_result_report(db_path, packs_path, args.limit)
    generated_at = datetime.now(timezone.utc).isoformat()

    ledger = {
        "generated_at": generated_at,
        "phase30_dir": str(phase30_dir),
        "db_path": str(db_path),
        "packs_file": str(packs_path),
        "train_summary": train_summary,
        "task_result_report": result,
    }
    ledger_path = phase30_dir / "scorecard_learning_ledger.json"
    report_path = phase30_dir / "scorecard_learning_report.md"
    latest_path = phase30_dir / "latest.json"

    write_json(ledger_path, ledger)
    report_path.write_text(build_report(train_summary, result), encoding="utf-8")
    latest_payload = {
        "generated_at": generated_at,
        "phase30_dir": str(phase30_dir),
        "db_path": str(db_path),
        "scored_outcomes": result["scored_outcomes"],
        "manual_scorecards": result["manual_scorecards"],
        "suggested_scorecards": result["suggested_scorecards"],
        "pending_manual_reviews": result["pending_manual_reviews"],
        "result_pack_priors": train_summary["result_pack_priors"],
        "result_path_priors": train_summary["result_path_priors"],
        "result_skill_priors": train_summary["result_skill_priors"],
        "top_learned_packs": [item["pack_id"] for item in result["top_learned_packs"][:5]],
        "weak_learned_packs": [item["pack_id"] for item in result["weak_learned_packs"][:5]],
        "report_path": str(report_path),
        "ledger_path": str(ledger_path),
    }
    write_json(latest_path, latest_payload)

    payload = {
        "generated_at": generated_at,
        "phase30_dir": str(phase30_dir),
        "train_summary": train_summary,
        "task_result_summary": {
            "scored_outcomes": result["scored_outcomes"],
            "manual_scorecards": result["manual_scorecards"],
            "suggested_scorecards": result["suggested_scorecards"],
            "pending_manual_reviews": result["pending_manual_reviews"],
            "avg_overall_manual": result["avg_overall_manual"],
            "avg_overall_all": result["avg_overall_all"],
        },
        "ledger_path": str(ledger_path),
        "report_path": str(report_path),
        "latest_path": str(latest_path),
    }
    print(json.dumps(payload, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
