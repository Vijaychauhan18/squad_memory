#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence

from squad_memory import (
    DB_PATH,
    HOME,
    TASK_PACKS_PATH,
    TASK_EVAL_FIXTURES_PATH,
    evaluate_fixtures,
    evaluate_task_fixtures,
    outcome_report,
    pack_report,
    pack_run_report,
    task_result_report,
    train_result_priors,
    train_outcome_priors,
    train_pack_priors,
    train_usage_priors,
    workspace_report,
)


BASE = HOME / "squad_memory"
DEFAULT_PHASE21_DIR = BASE / "ingest" / "phase21"
DEFAULT_INGEST_ROOT = BASE / "ingest"
DEFAULT_FIXTURES = BASE / "evals" / "fixtures.json"
DEFAULT_TASK_FIXTURES = TASK_EVAL_FIXTURES_PATH
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"

QUEUE_LABELS = {
    "seo": "SEO",
    "writer_marketing": "Writer + Marketing",
    "charles": "Charles",
    "developer_qa": "Developer + QA",
}

STALE_SOURCE_THRESHOLD_DAYS = 45


def add_shared_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--phase21-dir", default=str(DEFAULT_PHASE21_DIR))
    parser.add_argument("--ingest-root", default=str(DEFAULT_INGEST_ROOT))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DB_PATH))
    parser.add_argument("--packs-file", default=str(TASK_PACKS_PATH))
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES))
    parser.add_argument("--task-fixtures", default=str(DEFAULT_TASK_FIXTURES))
    parser.add_argument("--limit", type=int, default=5)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 21 squad control plane")
    subparsers = parser.add_subparsers(dest="command", required=True)

    report = subparsers.add_parser("report", help="Aggregate queue, source, memory, and telemetry status into one control-plane report")
    add_shared_args(report)
    report.add_argument("--json", action="store_true")

    queue_action = subparsers.add_parser("queue-action", help="Apply approve, reject, or hold actions through the existing queue gates")
    add_shared_args(queue_action)
    queue_action.add_argument("--domain", choices=sorted(QUEUE_LABELS), required=True)
    queue_action.add_argument("--approve", action="append", default=[])
    queue_action.add_argument("--reject", action="append", default=[])
    queue_action.add_argument("--hold", action="append", default=[])
    queue_action.add_argument("--build-db", action="store_true")
    queue_action.add_argument("--output-dir", help="Optional override for SEO memory output dir")
    queue_action.add_argument("--memory-router", help="Optional override for SEO MEMORY.md")
    queue_action.add_argument("--index-path", help="Optional override for SEO INDEX.md")
    queue_action.add_argument("--json", action="store_true")

    retrain = subparsers.add_parser("retrain", help="Retrain retrieval, pack, and outcome priors, then refresh the control-plane report")
    add_shared_args(retrain)
    retrain.add_argument("--json", action="store_true")

    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def path_exists_string(path: Path) -> str:
    return str(path) if path.exists() else ""


def parse_iso_day(value: str) -> Optional[date]:
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def days_old(value: str) -> Optional[int]:
    parsed = parse_iso_day(value)
    if parsed is None:
        return None
    return (datetime.now(timezone.utc).date() - parsed).days


def safe_call(func: Callable[..., Dict[str, Any]], *args: Any) -> Dict[str, Any]:
    try:
        return func(*args)
    except Exception as exc:  # pragma: no cover - defensive guard
        return {"available": False, "error": str(exc)}


def summarize_phase_timeline(ingest_root: Path) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    runs_latest = ingest_root / "runs" / "latest.json"
    runs_payload = load_json(runs_latest, {})
    if runs_payload:
        entries.append(
            {
                "phase": "phase1",
                "generated_at": runs_payload.get("generated_at", ""),
                "path": str(runs_latest),
            }
        )

    for latest_path in sorted(ingest_root.glob("phase*/latest.json")):
        payload = load_json(latest_path, {})
        entries.append(
            {
                "phase": latest_path.parent.name,
                "generated_at": payload.get("generated_at", ""),
                "path": str(latest_path),
            }
        )

    return entries


def summarize_queue(decisions_path: Path, label: str) -> Dict[str, Any]:
    payload = load_json(decisions_path, {"items": []})
    items = payload.get("items", [])
    counts = {"approve": 0, "reject": 0, "hold": 0}
    held_items: List[Dict[str, Any]] = []
    approved_items: List[Dict[str, Any]] = []
    rejected_items: List[Dict[str, Any]] = []

    for item in items:
        status = str(item.get("status", "hold"))
        counts[status] = counts.get(status, 0) + 1
        slim = {
            "draft_filename": item.get("draft_filename", ""),
            "title": item.get("title", item.get("draft_filename", "")),
            "score": item.get("score", 0.0),
            "source_slug": item.get("source_slug", ""),
            "triage_recommendation": item.get("triage_recommendation", ""),
        }
        if status == "hold":
            held_items.append(slim)
        elif status == "approve":
            approved_items.append(slim)
        elif status == "reject":
            rejected_items.append(slim)

    held_items.sort(key=lambda row: (-float(row.get("score", 0.0) or 0.0), row["draft_filename"]))
    approved_items.sort(key=lambda row: row["draft_filename"])
    rejected_items.sort(key=lambda row: row["draft_filename"])
    return {
        "label": label,
        "decisions_path": str(decisions_path),
        "generated_at": payload.get("generated_at", ""),
        "items_total": len(items),
        "counts": counts,
        "held_items": held_items[:5],
        "approved_items": approved_items[:5],
        "rejected_items": rejected_items[:5],
    }


def summarize_seo_sources(runs_latest: Path) -> Dict[str, Any]:
    payload = load_json(runs_latest, {})
    results = payload.get("results", [])
    failed_sources: List[Dict[str, Any]] = []
    stale_sources: List[Dict[str, Any]] = []
    ok_count = 0
    for item in results:
        status = item.get("status", "")
        if status == "ok":
            ok_count += 1
        else:
            failed_sources.append(
                {
                    "slug": item.get("slug", ""),
                    "name": item.get("name", item.get("slug", "")),
                    "status": status,
                    "error": item.get("error", ""),
                }
            )
        published = str(item.get("latest_published", ""))
        age_days = days_old(published)
        if age_days is not None and age_days >= STALE_SOURCE_THRESHOLD_DAYS:
            stale_sources.append(
                {
                    "slug": item.get("slug", ""),
                    "name": item.get("name", item.get("slug", "")),
                    "latest_published": published,
                    "age_days": age_days,
                }
            )

    stale_sources.sort(key=lambda row: (-row["age_days"], row["slug"]))
    return {
        "label": "SEO",
        "generated_at": payload.get("generated_at", ""),
        "manifest_path": str(runs_latest),
        "source_count": len(results),
        "ok_source_count": ok_count,
        "error_source_count": len(failed_sources),
        "failed_sources": failed_sources[:10],
        "stale_source_count": len(stale_sources),
        "stale_sources": stale_sources[:10],
        "new_items_total": sum(int(item.get("new_item_count", 0) or 0) for item in results),
    }


def summarize_external_domain(entry: Dict[str, Any], label: str, manifest_path: Path) -> Dict[str, Any]:
    return {
        "label": label,
        "generated_at": entry.get("generated_at", ""),
        "manifest_path": str(manifest_path),
        "source_count": int(entry.get("source_count", 0) or 0),
        "ok_source_count": int(entry.get("ok_source_count", 0) or 0),
        "error_source_count": int(entry.get("error_source_count", 0) or 0),
        "failed_sources": entry.get("failed_sources", [])[:10],
        "live_note_count": int(entry.get("live_note_count", 0) or 0),
        "source_canon_count": int(entry.get("source_canon_count", 0) or 0),
    }


def summarize_writer_marketing_sources(phase12_latest: Path) -> Dict[str, Dict[str, Any]]:
    payload = load_json(phase12_latest, {})
    entries = {item.get("domain", ""): item for item in payload.get("domains", [])}
    return {
        "writer": summarize_external_domain(entries.get("writer", {}), "Writer", phase12_latest),
        "marketing": summarize_external_domain(entries.get("marketing", {}), "Marketing", phase12_latest),
    }


def summarize_charles_sources(phase17_latest: Path) -> Dict[str, Any]:
    payload = load_json(phase17_latest, {})
    return {
        "label": "Charles",
        "generated_at": payload.get("generated_at", ""),
        "manifest_path": str(phase17_latest),
        "source_count": int(payload.get("source_count", 0) or 0),
        "ok_source_count": int(payload.get("ok_source_count", 0) or 0),
        "error_source_count": int(payload.get("error_source_count", 0) or 0),
        "failed_sources": payload.get("failed_sources", [])[:10],
        "live_note_count": int(payload.get("live_note_count", 0) or 0),
        "source_canon_count": int(payload.get("source_canon_count", 0) or 0),
    }


def summarize_support_sources(phase23_latest: Path) -> Dict[str, Any]:
    payload = load_json(phase23_latest, {})
    return {
        "label": "Support",
        "generated_at": payload.get("generated_at", ""),
        "manifest_path": str(phase23_latest),
        "source_count": int(payload.get("source_count", 0) or 0),
        "ok_source_count": int(payload.get("ok_source_count", 0) or 0),
        "error_source_count": int(payload.get("error_source_count", 0) or 0),
        "failed_sources": payload.get("failed_sources", [])[:10],
        "live_note_count": int(payload.get("live_note_count", 0) or 0),
        "source_canon_count": int(payload.get("source_canon_count", 0) or 0),
    }


def summarize_dev_qa_sources(phase25_latest: Path) -> Dict[str, Dict[str, Any]]:
    payload = load_json(phase25_latest, {})
    entries = {item.get("domain", ""): item for item in payload.get("domains", [])}
    return {
        "developer": summarize_external_domain(entries.get("developer", {}), "Developer", phase25_latest),
        "qa": summarize_external_domain(entries.get("qa", {}), "QA", phase25_latest),
    }


def summarize_memory_health(phase7_latest: Path, phase10_ledger: Path) -> Dict[str, Any]:
    phase7 = load_json(phase7_latest, {})
    health = phase7.get("health", {})
    evidence = load_json(phase10_ledger, {})
    topics = evidence.get("topics", {})
    if isinstance(topics, dict):
        topic_rows = list(topics.values())
    else:
        topic_rows = list(topics)

    multi_source_topics = 0
    low_confidence_topics = 0
    tension_topics = 0
    stale_topics = 0
    for row in topic_rows:
        if int(row.get("source_count", 0) or 0) > 1:
            multi_source_topics += 1
        if row.get("confidence_label") == "low":
            low_confidence_topics += 1
        if row.get("tension"):
            tension_topics += 1
        if row.get("freshness_label") not in {"current", "fresh"}:
            stale_topics += 1

    note_status_counts = health.get("note_status_counts", {})
    return {
        "generated_at": phase7.get("generated_at", ""),
        "registry_path": phase7.get("registry_path", path_exists_string(phase7_latest.parent / "canonical_registry.json")),
        "topics_total": int(health.get("topics_total", 0) or 0),
        "healthy_topics": int(health.get("healthy_topics", 0) or 0),
        "topics_needing_canonical": int(health.get("topics_needing_canonical", 0) or 0),
        "monitor_only_topics": int(health.get("monitor_only_topics", 0) or 0),
        "legacy_only_topics": int(health.get("legacy_only_topics", 0) or 0),
        "stale_legacy_notes": int(note_status_counts.get("stale_legacy_feed", 0) or 0),
        "merge_candidate_notes": int(note_status_counts.get("merge_candidate", 0) or 0),
        "multi_source_topics": multi_source_topics,
        "low_confidence_topics": low_confidence_topics,
        "tension_topics": tension_topics,
        "stale_topics": stale_topics,
        "report_path": phase7.get("report_path", path_exists_string(phase7_latest.parent / "memory_health_report.md")),
        "evidence_ledger_path": str(phase10_ledger),
    }


def summarize_learning(db_path: Path, packs_path: Path, fixtures_path: Path, task_fixtures_path: Path, limit: int) -> Dict[str, Any]:
    outcome = safe_call(outcome_report, db_path, packs_path, limit)
    packs = safe_call(pack_report, db_path, packs_path, limit)
    execution = safe_call(pack_run_report, db_path, packs_path, limit, None)
    task_results = safe_call(task_result_report, db_path, packs_path, limit)
    evaluation = safe_call(evaluate_fixtures, db_path, fixtures_path)
    task_evaluation = safe_call(evaluate_task_fixtures, db_path, packs_path, task_fixtures_path, 5)

    return {
        "outcome": outcome,
        "packs": packs,
        "execution": execution,
        "task_results": task_results,
        "evaluation": evaluation,
        "task_evaluation": task_evaluation,
    }


def summarize_workspace(db_path: Path, limit: int) -> Dict[str, Any]:
    return safe_call(workspace_report, db_path, limit)


def build_alerts(snapshot: Dict[str, Any]) -> List[str]:
    alerts: List[str] = []
    for key in ("seo", "writer_marketing", "charles", "developer_qa"):
        queue = snapshot["queues"][key]
        hold_count = int(queue["counts"].get("hold", 0) or 0)
        if hold_count:
            alerts.append(f"{queue['label']} queue has {hold_count} held item(s).")

    seo_sources = snapshot["sources"]["seo"]
    if seo_sources["error_source_count"]:
        alerts.append(f"SEO source monitor has {seo_sources['error_source_count']} failed feed(s).")
    if seo_sources["stale_source_count"]:
        alerts.append(f"SEO source monitor has {seo_sources['stale_source_count']} stale feed(s) older than {STALE_SOURCE_THRESHOLD_DAYS} days.")

    for label in ("writer", "marketing", "charles", "support", "developer", "qa"):
        domain = snapshot["sources"][label]
        if domain["error_source_count"]:
            alerts.append(f"{domain['label']} source monitor has {domain['error_source_count']} failed source(s).")

    memory = snapshot["memory_health"]
    if memory["topics_needing_canonical"]:
        alerts.append(f"Memory health shows {memory['topics_needing_canonical']} topic(s) still needing canonical synthesis.")
    if memory["stale_legacy_notes"]:
        alerts.append(f"Memory health still contains {memory['stale_legacy_notes']} stale legacy notes.")
    if memory["low_confidence_topics"]:
        alerts.append(f"Evidence fusion has {memory['low_confidence_topics']} low-confidence topic(s).")

    evaluation = snapshot["learning"]["evaluation"]
    primary_accuracy = float(evaluation.get("primary_skill_accuracy", 0.0) or 0.0)
    top5_hit = float(evaluation.get("top5_path_hit_rate", 0.0) or 0.0)
    if evaluation.get("available", True) and (primary_accuracy < 1.0 or top5_hit < 1.0):
        alerts.append("Retrieval evaluation regressed below the current all-green baseline.")
    task_evaluation = snapshot["learning"].get("task_evaluation", {})
    pack_accuracy = float(task_evaluation.get("pack_accuracy", 0.0) or 0.0)
    task_pass_rate = float(task_evaluation.get("pass_rate", 0.0) or 0.0)
    if task_evaluation.get("available", True) and (pack_accuracy < 1.0 or task_pass_rate < 1.0):
        alerts.append("Full task evaluation regressed below the current all-green baseline.")

    weak_packs = snapshot["learning"]["packs"].get("weak_packs", [])
    if weak_packs:
        alerts.append(f"{len(weak_packs)} pack(s) are currently flagged as weak or revision-heavy.")

    execution = snapshot["learning"]["execution"]
    active_runs = int(execution.get("active_runs", 0) or 0)
    blocked_runs = int(execution.get("blocked_runs", 0) or 0)
    open_blockers = int(execution.get("open_blockers", 0) or 0)
    if active_runs:
        alerts.append(f"Execution engine currently has {active_runs} active pack run(s).")
    if blocked_runs or open_blockers:
        alerts.append(f"Execution engine has {blocked_runs} blocked run(s) and {open_blockers} open blocker(s).")
    workspace = snapshot.get("workspace", {})
    if int(workspace.get("active_contexts", 0) or 0) > 4:
        alerts.append(f"Workspace context has {workspace['active_contexts']} active contexts; consider pruning old transient scopes.")
    if int(workspace.get("active_items", 0) or 0) > 180:
        alerts.append(f"Workspace context has {workspace['active_items']} active items; runtime context may be getting noisy.")

    overranked_paths = snapshot["learning"]["outcome"].get("overranked_paths", [])
    if overranked_paths:
        alerts.append(f"{len(overranked_paths)} over-ranked path(s) are being surfaced more than they help.")

    task_results = snapshot["learning"]["task_results"]
    pending_reviews = int(task_results.get("pending_manual_reviews", 0) or 0)
    if pending_reviews:
        alerts.append(f"Task result scoring has {pending_reviews} pending manual review(s).")
    weak_result_packs = task_results.get("weak_packs", [])
    if weak_result_packs:
        alerts.append(f"{len(weak_result_packs)} scored pack(s) are below the output-quality threshold.")
    weak_learned_result_packs = task_results.get("weak_learned_packs", [])
    if weak_learned_result_packs:
        alerts.append(f"{len(weak_learned_result_packs)} learned scorecard pack prior(s) are still weak.")

    return alerts


def build_status_snapshot(
    phase21_dir: Path,
    ingest_root: Path,
    db_path: Path,
    packs_path: Path,
    fixtures_path: Path,
    task_fixtures_path: Path,
    limit: int,
) -> Dict[str, Any]:
    snapshot = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase21_dir": str(phase21_dir),
        "ingest_root": str(ingest_root),
        "timeline": summarize_phase_timeline(ingest_root),
        "queues": {
            "seo": summarize_queue(ingest_root / "phase6" / "decisions.json", QUEUE_LABELS["seo"]),
            "writer_marketing": summarize_queue(ingest_root / "phase14" / "decisions.json", QUEUE_LABELS["writer_marketing"]),
            "charles": summarize_queue(ingest_root / "phase19" / "decisions.json", QUEUE_LABELS["charles"]),
            "developer_qa": summarize_queue(ingest_root / "phase27" / "decisions.json", QUEUE_LABELS["developer_qa"]),
        },
    }
    writer_marketing_sources = summarize_writer_marketing_sources(ingest_root / "phase12" / "latest.json")
    dev_qa_sources = summarize_dev_qa_sources(ingest_root / "phase25" / "latest.json")
    snapshot["sources"] = {
        "seo": summarize_seo_sources(ingest_root / "runs" / "latest.json"),
        "writer": writer_marketing_sources["writer"],
        "marketing": writer_marketing_sources["marketing"],
        "charles": summarize_charles_sources(ingest_root / "phase17" / "latest.json"),
        "support": summarize_support_sources(ingest_root / "phase23" / "latest.json"),
        "developer": dev_qa_sources["developer"],
        "qa": dev_qa_sources["qa"],
    }
    snapshot["memory_health"] = summarize_memory_health(
        ingest_root / "phase7" / "latest.json",
        ingest_root / "phase10" / "evidence_ledger.json",
    )
    snapshot["learning"] = summarize_learning(db_path, packs_path, fixtures_path, task_fixtures_path, limit)
    snapshot["workspace"] = summarize_workspace(db_path, limit)
    snapshot["alerts"] = build_alerts(snapshot)
    return snapshot


def report_markdown(snapshot: Dict[str, Any]) -> str:
    eval_payload = snapshot["learning"]["evaluation"]
    task_eval_payload = snapshot["learning"].get("task_evaluation", {})
    outcome = snapshot["learning"]["outcome"]
    packs = snapshot["learning"]["packs"]
    lines: List[str] = [
        "# Phase 21 Squad Control Plane",
        "",
        f"Generated: {snapshot['generated_at']}",
        "",
        "## Summary",
        f"- Alerts: {len(snapshot['alerts'])}",
        f"- Eval primary skill accuracy: {float(eval_payload.get('primary_skill_accuracy', 0.0) or 0.0):.2%}",
        f"- Eval top-5 path hit rate: {float(eval_payload.get('top5_path_hit_rate', 0.0) or 0.0):.2%}",
        f"- Task-eval pack accuracy: {float(task_eval_payload.get('pack_accuracy', 0.0) or 0.0):.2%}",
        f"- Task-eval pass rate: {float(task_eval_payload.get('pass_rate', 0.0) or 0.0):.2%}",
        f"- Task outcomes tracked: {outcome.get('task_outcomes', 0)}",
        "",
        "## Alerts",
    ]
    if snapshot["alerts"]:
        for alert in snapshot["alerts"]:
            lines.append(f"- {alert}")
    else:
        lines.append("- No active alerts.")

    lines.extend(["", "## Queue Health"])
    for key in ("seo", "writer_marketing", "charles", "developer_qa"):
        queue = snapshot["queues"][key]
        lines.extend(
            [
                f"### {queue['label']}",
                f"- Approve: {queue['counts'].get('approve', 0)}",
                f"- Reject: {queue['counts'].get('reject', 0)}",
                f"- Hold: {queue['counts'].get('hold', 0)}",
            ]
        )
        if queue["held_items"]:
            lines.append("- Top held items:")
            for item in queue["held_items"]:
                extra = f" | triage={item['triage_recommendation']}" if item.get("triage_recommendation") else ""
                lines.append(f"  - `{item['draft_filename']}` | score={float(item.get('score', 0.0) or 0.0):.2f}{extra}")
        else:
            lines.append("- No held items.")
        lines.append("")

    lines.extend(["## Source Health"])
    for key in ("seo", "writer", "marketing", "charles", "support", "developer", "qa"):
        domain = snapshot["sources"][key]
        lines.append(f"### {domain['label']}")
        lines.append(f"- Healthy sources: {domain['ok_source_count']}/{domain['source_count']}")
        lines.append(f"- Failed sources: {domain['error_source_count']}")
        if key == "seo":
            lines.append(f"- Stale sources: {domain['stale_source_count']}")
            lines.append(f"- New items in latest run: {domain['new_items_total']}")
        if domain["failed_sources"]:
            lines.append("- Failures:")
            for item in domain["failed_sources"][:5]:
                if isinstance(item, dict):
                    lines.append(f"  - `{item.get('slug', '')}` | {item.get('status', '')} | {item.get('error', '')}")
                else:
                    lines.append(f"  - {item}")
        if key == "seo" and domain["stale_sources"]:
            lines.append("- Stale feeds:")
            for item in domain["stale_sources"][:5]:
                lines.append(f"  - `{item['slug']}` | age={item['age_days']}d | latest={item['latest_published']}")
        lines.append("")

    memory = snapshot["memory_health"]
    lines.extend(
        [
            "## Memory Health",
            f"- Healthy canonical topics: {memory['healthy_topics']}/{memory['topics_total']}",
            f"- Topics needing canonical synthesis: {memory['topics_needing_canonical']}",
            f"- Monitor-only topics: {memory['monitor_only_topics']}",
            f"- Legacy-only topics: {memory['legacy_only_topics']}",
            f"- Stale legacy notes: {memory['stale_legacy_notes']}",
            f"- Merge-candidate notes: {memory['merge_candidate_notes']}",
            f"- Multi-source topics: {memory['multi_source_topics']}",
            f"- Cross-source tension topics: {memory['tension_topics']}",
            f"- Low-confidence topics: {memory['low_confidence_topics']}",
            "",
            "## Outcome Telemetry",
        ]
    )
    workspace = snapshot.get("workspace", {})
    lines.extend(
        [
            "## Workspace Context",
            f"- Active contexts: {workspace.get('active_contexts', 0)}",
            f"- Archived contexts: {workspace.get('archived_contexts', 0)}",
            f"- Active items: {workspace.get('active_items', 0)}",
        ]
    )
    if workspace.get("contexts"):
        lines.append("- Current scopes:")
        for item in workspace["contexts"][:5]:
            scope = []
            if item.get("role"):
                scope.append(f"role={item['role']}")
            if item.get("pack_id"):
                scope.append(f"pack={item['pack_id']}")
            lines.append(
                f"  - #{item['id']} `{item['name']}` | items={item['item_count']} | "
                f"{', '.join(scope) if scope else 'global'}"
            )
    lines.append("")
    if outcome.get("status_breakdown"):
        for item in outcome["status_breakdown"]:
            lines.append(f"- {item['status']}: {item['count']} ({item['rate']:.1%})")
    else:
        lines.append("- No task outcomes yet.")

    if packs.get("top_packs"):
        lines.append("- Strongest packs:")
        for item in packs["top_packs"][:5]:
            lines.append(f"  - `{item['pack_id']}` | score={item['score']:.3f}")
    if packs.get("weak_packs"):
        lines.append("- Weak packs:")
        for item in packs["weak_packs"][:5]:
            lines.append(f"  - `{item['pack_id']}` | score={item['score']:.3f}")

    execution = snapshot["learning"]["execution"]
    lines.extend(
        [
            "",
            "## Pack Execution",
            f"- Total runs: {execution.get('total_runs', 0)}",
            f"- Active runs: {execution.get('active_runs', 0)}",
            f"- Blocked runs: {execution.get('blocked_runs', 0)}",
            f"- Completed runs: {execution.get('completed_runs', 0)}",
            f"- Open blockers: {execution.get('open_blockers', 0)}",
        ]
    )
    if execution.get("recent_runs"):
        lines.append("- Recent runs:")
        for item in execution["recent_runs"][:5]:
            lines.append(
                f"  - run={item['id']} | `{item['pack_id']}` | {item['status']} | "
                f"step {item['current_step_seq']}/{item['step_count']} | blockers={item['blocker_count']} | handoffs={item['handoff_count']}"
            )

    if outcome.get("overranked_paths"):
        lines.append("- Over-ranked paths:")
        for item in outcome["overranked_paths"][:5]:
            lines.append(f"  - `{item['path']}` | retrieval={item['retrieval_score']:.3f} | outcome={item['outcome_score']:.3f}")

    task_results = snapshot["learning"]["task_results"]
    lines.extend(
        [
            "",
            "## Task Evaluation",
            f"- Total cases: {task_eval_payload.get('total_cases', 0)}",
            f"- Pack accuracy: {float(task_eval_payload.get('pack_accuracy', 0.0) or 0.0):.2%}",
            f"- Primary skill accuracy: {float(task_eval_payload.get('primary_skill_accuracy', 0.0) or 0.0):.2%}",
            f"- Supporting skill match rate: {float(task_eval_payload.get('supporting_skill_match_rate', 0.0) or 0.0):.2%}",
            f"- Memory path hit rate: {float(task_eval_payload.get('memory_path_hit_rate', 0.0) or 0.0):.2%}",
            f"- Output section hit rate: {float(task_eval_payload.get('output_section_hit_rate', 0.0) or 0.0):.2%}",
            f"- Deliverable hit rate: {float(task_eval_payload.get('deliverable_hit_rate', 0.0) or 0.0):.2%}",
            f"- Pass rate: {float(task_eval_payload.get('pass_rate', 0.0) or 0.0):.2%}",
        ]
    )
    if task_eval_payload.get("weak_cases"):
        lines.append("- Weak cases:")
        for item in task_eval_payload["weak_cases"][:5]:
            lines.append(
                f"  - `{item['selected_pack_id']}` | failed={', '.join(item.get('failed_checks', [])) or '-'} | "
                f"{item['query']}"
            )

    lines.extend(
        [
            "",
            "## Task Result Scoring",
            f"- Manual scorecards: {task_results.get('manual_scorecards', 0)}",
            f"- Suggested scorecards: {task_results.get('suggested_scorecards', 0)}",
            f"- Pending manual reviews: {task_results.get('pending_manual_reviews', 0)}",
        ]
    )
    manual_avg = task_results.get("avg_overall_manual")
    all_avg = task_results.get("avg_overall_all")
    lines.append(f"- Avg overall score (manual): {'-' if manual_avg is None else f'{float(manual_avg):.2f}'}")
    lines.append(f"- Avg overall score (all): {'-' if all_avg is None else f'{float(all_avg):.2f}'}")
    if task_results.get("top_packs"):
        lines.append("- Top scored packs:")
        for item in task_results["top_packs"][:5]:
            lines.append(f"  - `{item['pack_id']}` | avg_score={item['avg_overall_score']:.2f} | count={item['count']}")
    if task_results.get("weak_packs"):
        lines.append("- Weak scored packs:")
        for item in task_results["weak_packs"][:5]:
            lines.append(f"  - `{item['pack_id']}` | avg_score={item['avg_overall_score']:.2f} | count={item['count']}")
    if task_results.get("pending_reviews"):
        lines.append("- Pending review queue:")
        for item in task_results["pending_reviews"][:5]:
            lines.append(
                f"  - outcome={item['outcome_id']} | `{item['pack_id']}` | suggested={item['suggested_overall_score']:.2f} | verdict={item['suggested_verdict']}"
            )
    if task_results.get("last_result_training"):
        item = task_results["last_result_training"]
        lines.append(
            "- Last result training: "
            f"scored={item['scored_outcomes']} manual={item['manual_scorecards']} suggested={item['suggested_scorecards']} "
            f"pack_priors={item['result_pack_priors']} path_priors={item['result_path_priors']} skill_priors={item['result_skill_priors']}"
        )
    if task_results.get("top_learned_packs"):
        lines.append("- Top learned scorecard pack priors:")
        for item in task_results["top_learned_packs"][:5]:
            lines.append(
                f"  - `{item['pack_id']}` | score={item['score']:.3f} | avg_score={item['avg_overall_score']:.2f} | exposure={item['exposure_count']}"
            )
    if task_results.get("weak_learned_packs"):
        lines.append("- Weak learned scorecard pack priors:")
        for item in task_results["weak_learned_packs"][:5]:
            lines.append(
                f"  - `{item['pack_id']}` | score={item['score']:.3f} | avg_score={item['avg_overall_score']:.2f} | exposure={item['exposure_count']}"
            )

    lines.extend(
        [
            "",
            "## Retrieval Eval",
            f"- Cases: {int(eval_payload.get('total_cases', 0) or 0)}",
            f"- Primary skill accuracy: {float(eval_payload.get('primary_skill_accuracy', 0.0) or 0.0):.2%}",
            f"- Top-3 skill hit rate: {float(eval_payload.get('top3_skill_hit_rate', 0.0) or 0.0):.2%}",
            f"- Top-5 path hit rate: {float(eval_payload.get('top5_path_hit_rate', 0.0) or 0.0):.2%}",
            "",
            "## Phase Timeline",
        ]
    )
    for item in snapshot["timeline"]:
        lines.append(f"- `{item['phase']}` | {item['generated_at']}")

    return "\n".join(lines).rstrip() + "\n"


def write_report_artifacts(phase21_dir: Path, snapshot: Dict[str, Any]) -> Dict[str, Any]:
    phase21_dir.mkdir(parents=True, exist_ok=True)
    status_path = phase21_dir / "control_plane_status.json"
    report_path = phase21_dir / "control_plane_report.md"
    latest_path = phase21_dir / "latest.json"

    write_json(status_path, snapshot)
    report_path.write_text(report_markdown(snapshot), encoding="utf-8")
    latest_payload = {
        "generated_at": snapshot["generated_at"],
        "phase21_dir": str(phase21_dir),
        "alerts": snapshot["alerts"],
        "queue_counts": {key: value["counts"] for key, value in snapshot["queues"].items()},
        "source_failures": {
            key: value["error_source_count"] for key, value in snapshot["sources"].items()
        },
        "stale_sources": snapshot["sources"]["seo"]["stale_source_count"],
        "memory_health": {
            "topics_needing_canonical": snapshot["memory_health"]["topics_needing_canonical"],
            "stale_legacy_notes": snapshot["memory_health"]["stale_legacy_notes"],
            "low_confidence_topics": snapshot["memory_health"]["low_confidence_topics"],
        },
        "workspace": {
            "active_contexts": snapshot["workspace"].get("active_contexts", 0),
            "archived_contexts": snapshot["workspace"].get("archived_contexts", 0),
            "active_items": snapshot["workspace"].get("active_items", 0),
        },
        "evaluation": {
            "total_cases": snapshot["learning"]["evaluation"].get("total_cases", 0),
            "primary_skill_accuracy": snapshot["learning"]["evaluation"].get("primary_skill_accuracy", 0.0),
            "top3_skill_hit_rate": snapshot["learning"]["evaluation"].get("top3_skill_hit_rate", 0.0),
            "top5_path_hit_rate": snapshot["learning"]["evaluation"].get("top5_path_hit_rate", 0.0),
        },
        "task_evaluation": {
            "total_cases": snapshot["learning"]["task_evaluation"].get("total_cases", 0),
            "pack_accuracy": snapshot["learning"]["task_evaluation"].get("pack_accuracy", 0.0),
            "primary_skill_accuracy": snapshot["learning"]["task_evaluation"].get("primary_skill_accuracy", 0.0),
            "supporting_skill_match_rate": snapshot["learning"]["task_evaluation"].get("supporting_skill_match_rate", 0.0),
            "memory_path_hit_rate": snapshot["learning"]["task_evaluation"].get("memory_path_hit_rate", 0.0),
            "output_section_hit_rate": snapshot["learning"]["task_evaluation"].get("output_section_hit_rate", 0.0),
            "deliverable_hit_rate": snapshot["learning"]["task_evaluation"].get("deliverable_hit_rate", 0.0),
            "pass_rate": snapshot["learning"]["task_evaluation"].get("pass_rate", 0.0),
        },
        "execution": {
            "total_runs": snapshot["learning"]["execution"].get("total_runs", 0),
            "active_runs": snapshot["learning"]["execution"].get("active_runs", 0),
            "blocked_runs": snapshot["learning"]["execution"].get("blocked_runs", 0),
            "completed_runs": snapshot["learning"]["execution"].get("completed_runs", 0),
            "open_blockers": snapshot["learning"]["execution"].get("open_blockers", 0),
        },
        "task_result_scoring": {
            "manual_scorecards": snapshot["learning"]["task_results"].get("manual_scorecards", 0),
            "suggested_scorecards": snapshot["learning"]["task_results"].get("suggested_scorecards", 0),
            "pending_manual_reviews": snapshot["learning"]["task_results"].get("pending_manual_reviews", 0),
            "avg_overall_manual": snapshot["learning"]["task_results"].get("avg_overall_manual"),
            "avg_overall_all": snapshot["learning"]["task_results"].get("avg_overall_all"),
            "result_pack_priors": (snapshot["learning"]["task_results"].get("last_result_training") or {}).get("result_pack_priors", 0),
            "result_path_priors": (snapshot["learning"]["task_results"].get("last_result_training") or {}).get("result_path_priors", 0),
            "result_skill_priors": (snapshot["learning"]["task_results"].get("last_result_training") or {}).get("result_skill_priors", 0),
        },
        "report_path": str(report_path),
        "status_path": str(status_path),
    }
    write_json(latest_path, latest_payload)
    return {
        "generated_at": snapshot["generated_at"],
        "phase21_dir": str(phase21_dir),
        "report_path": str(report_path),
        "status_path": str(status_path),
        "latest_path": str(latest_path),
        "alerts": snapshot["alerts"],
        "queue_counts": latest_payload["queue_counts"],
        "evaluation": latest_payload["evaluation"],
    }


def build_and_write_report(args: argparse.Namespace) -> Dict[str, Any]:
    phase21_dir = Path(args.phase21_dir)
    ingest_root = Path(args.ingest_root) if getattr(args, "ingest_root", "") else phase21_dir.parent
    snapshot = build_status_snapshot(
        phase21_dir=phase21_dir,
        ingest_root=ingest_root,
        db_path=Path(args.db_path),
        packs_path=Path(args.packs_file),
        fixtures_path=Path(args.fixtures),
        task_fixtures_path=Path(args.task_fixtures),
        limit=args.limit,
    )
    return write_report_artifacts(phase21_dir, snapshot)


def run_json_command(command: List[str]) -> Dict[str, Any]:
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(
            f"Command failed ({completed.returncode}): {' '.join(command)}\n"
            f"stdout:\n{completed.stdout}\n\nstderr:\n{completed.stderr}"
        )
    return json.loads(completed.stdout or "{}")


def build_queue_action_command(args: argparse.Namespace) -> List[str]:
    python = sys.executable
    ingest_root = Path(args.ingest_root) if getattr(args, "ingest_root", "") else Path(args.phase21_dir).parent
    skills_root = Path(args.skills_root)
    db_path = Path(args.db_path)

    if args.domain == "seo":
        output_dir = Path(args.output_dir) if args.output_dir else skills_root / "seo" / "memory"
        memory_router = Path(args.memory_router) if args.memory_router else skills_root / "seo" / "MEMORY.md"
        index_path = Path(args.index_path) if args.index_path else output_dir / "INDEX.md"
        command = [
            python,
            str(BASE / "phase6_promote_approved.py"),
            "--output-dir",
            str(output_dir),
            "--phase5-manifest",
            str(ingest_root / "phase5" / "latest.json"),
            "--phase6-dir",
            str(ingest_root / "phase6"),
            "--decisions-path",
            str(ingest_root / "phase6" / "decisions.json"),
            "--state-path",
            str(ingest_root / "phase6" / "state.json"),
            "--memory-router",
            str(memory_router),
            "--index-path",
            str(index_path),
            "--skills-root",
            str(skills_root),
            "--db-path",
            str(db_path),
            "--json",
        ]
    elif args.domain == "writer_marketing":
        command = [
            python,
            str(BASE / "phase14_promote_writer_marketing_approved.py"),
            "--phase13-manifest",
            str(ingest_root / "phase13" / "latest.json"),
            "--phase14-dir",
            str(ingest_root / "phase14"),
            "--decisions-path",
            str(ingest_root / "phase14" / "decisions.json"),
            "--state-path",
            str(ingest_root / "phase14" / "state.json"),
            "--skills-root",
            str(skills_root),
            "--db-path",
            str(db_path),
            "--json",
        ]
    elif args.domain == "developer_qa":
        command = [
            python,
            str(BASE / "phase27_promote_dev_qa_approved.py"),
            "--phase26-manifest",
            str(ingest_root / "phase26" / "latest.json"),
            "--phase27-dir",
            str(ingest_root / "phase27"),
            "--decisions-path",
            str(ingest_root / "phase27" / "decisions.json"),
            "--state-path",
            str(ingest_root / "phase27" / "state.json"),
            "--skills-root",
            str(skills_root),
            "--db-path",
            str(db_path),
            "--json",
        ]
    else:
        command = [
            python,
            str(BASE / "phase19_promote_charles_approved.py"),
            "--phase18-manifest",
            str(ingest_root / "phase18" / "latest.json"),
            "--phase19-dir",
            str(ingest_root / "phase19"),
            "--decisions-path",
            str(ingest_root / "phase19" / "decisions.json"),
            "--state-path",
            str(ingest_root / "phase19" / "state.json"),
            "--skills-root",
            str(skills_root),
            "--db-path",
            str(db_path),
            "--json",
        ]

    for filename in args.approve:
        command.extend(["--approve", filename])
    for filename in args.reject:
        command.extend(["--reject", filename])
    for filename in args.hold:
        command.extend(["--hold", filename])
    if args.build_db:
        command.append("--build-db")
    return command


def maybe_refresh_charles_triage(args: argparse.Namespace) -> Dict[str, Any]:
    if args.domain != "charles":
        return {}
    ingest_root = Path(args.ingest_root) if getattr(args, "ingest_root", "") else Path(args.phase21_dir).parent
    command = [
        sys.executable,
        str(BASE / "phase20_triage_charles_queue.py"),
        "--phase19-manifest",
        str(ingest_root / "phase19" / "latest.json"),
        "--decisions-path",
        str(ingest_root / "phase19" / "decisions.json"),
        "--phase20-dir",
        str(ingest_root / "phase20"),
        "--json",
    ]
    return run_json_command(command)


def handle_queue_action(args: argparse.Namespace) -> Dict[str, Any]:
    if not (args.approve or args.reject or args.hold):
        raise SystemExit("queue-action requires at least one --approve, --reject, or --hold flag")

    action_result = run_json_command(build_queue_action_command(args))
    triage_result = maybe_refresh_charles_triage(args)
    report_result = build_and_write_report(args)
    queue_snapshot = report_result["queue_counts"][args.domain]
    return {
        "domain": args.domain,
        "label": QUEUE_LABELS[args.domain],
        "action_result": action_result,
        "triage_result": triage_result,
        "queue_counts": queue_snapshot,
        "report_path": report_result["report_path"],
        "latest_path": report_result["latest_path"],
    }


def handle_retrain(args: argparse.Namespace) -> Dict[str, Any]:
    usage = train_usage_priors(Path(args.db_path))
    packs = train_pack_priors(Path(args.db_path))
    outcomes = train_outcome_priors(Path(args.db_path))
    results = train_result_priors(Path(args.db_path))
    report_result = build_and_write_report(args)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "db_path": str(Path(args.db_path)),
        "usage_train": usage,
        "pack_train": packs,
        "outcome_train": outcomes,
        "result_train": results,
        "report_path": report_result["report_path"],
        "latest_path": report_result["latest_path"],
        "alerts": report_result["alerts"],
    }


def main() -> int:
    args = parse_args()
    if args.command == "report":
        payload = build_and_write_report(args)
    elif args.command == "queue-action":
        payload = handle_queue_action(args)
    elif args.command == "retrain":
        payload = handle_retrain(args)
    else:  # pragma: no cover - argparse guards this
        raise SystemExit(f"Unknown command: {args.command}")

    print(json.dumps(payload, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
