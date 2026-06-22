#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from refresh_openclaw_hq_mission_runner import refresh_openclaw_hq_mission_runner
from refresh_local_seo_stack import refresh_local_seo_stack
from refresh_openclaw_seo_missions import refresh_openclaw_seo_missions
from run_openclaw_seo_action_runner import run_openclaw_seo_action_runner
from report_seo_elite_status import build_status_payload, render_status_markdown


HOME = Path.home()
DEFAULT_STATUS_DIR = HOME / ".codex" / "elite-skills" / "seo-elite" / "status"
DEFAULT_STATUS_JSON = DEFAULT_STATUS_DIR / "latest-status.json"
DEFAULT_STATUS_MD = DEFAULT_STATUS_DIR / "latest-status.md"
DEFAULT_OPENCLAW_WORKSPACE = HOME / ".openclaw" / "workspace" / "squad" / "seo"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh deterministic SEO automation artifacts for the OpenClaw SEO workspace")
    parser.add_argument("--status-json", default=str(DEFAULT_STATUS_JSON))
    parser.add_argument("--status-md", default=str(DEFAULT_STATUS_MD))
    parser.add_argument("--openclaw-workspace", default=str(DEFAULT_OPENCLAW_WORKSPACE))
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_iso_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def unique_preserve_order(items: List[str]) -> List[str]:
    seen: set[str] = set()
    unique: List[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique


def load_status_payload(status_json_path: Path) -> Dict[str, Any]:
    if status_json_path.exists():
        return json.loads(status_json_path.read_text(encoding="utf-8"))
    return build_status_payload()


def summarize_pipeline(payload: Dict[str, Any]) -> str:
    metrics = payload["db"]
    pending = payload["pending"]
    activity = payload["activity"]
    return (
        f"{metrics['chunks']} chunks across {metrics['paths']} paths, "
        f"{pending['pending_total']} pending harvest candidates, "
        f"phase={activity['current_phase']}, "
        f"fetch-ok={activity['recent_fetch_ok']}, fetch-error={activity['recent_fetch_error']}."
    )


def build_alerts(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    alerts: List[Dict[str, Any]] = []
    for job in payload.get("active_jobs", []):
        status = job.get("status", "missing")
        if status == "active":
            continue
        severity = "high" if status == "missing" else "medium"
        action = "Restore the job or inspect its log before trusting fresh output." if status == "missing" else "Check why the job stopped updating and inspect the corresponding log."
        alerts.append(
            {
                "severity": severity,
                "title": f"{job.get('job', 'unknown')} is {status}",
                "details": f"Last update: {job.get('updated_at', 'missing')}",
                "action": action,
                "files": [f"logs/{job.get('job', 'unknown')}"],
            }
        )

    pending_total = int(payload.get("pending", {}).get("pending_total", 0))
    if pending_total >= 500:
        alerts.append(
            {
                "severity": "high",
                "title": "Harvest backlog is large",
                "details": f"{pending_total} pending article candidates are waiting for extraction.",
                "action": "Push backlog harvesting first so new source signals become usable article notes.",
                "files": ["automation/data/latest-status.json"],
            }
        )
    elif pending_total >= 150:
        alerts.append(
            {
                "severity": "medium",
                "title": "Harvest backlog is building",
                "details": f"{pending_total} pending article candidates are still queued.",
                "action": "Prioritize the noisiest pending sources before adding new source coverage.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    recent_fetch_error = int(payload.get("activity", {}).get("recent_fetch_error", 0))
    if recent_fetch_error > 0:
        top_errors = payload.get("activity", {}).get("recent_error_sources", [])
        detail = ", ".join(f"{item['source']} ({item['count']})" for item in top_errors[:3]) or "unknown sources"
        alerts.append(
            {
                "severity": "medium",
                "title": "Recent fetch errors detected",
                "details": f"{recent_fetch_error} fetch errors in the last short activity window. Sources: {detail}.",
                "action": "Inspect the affected sources before relying on freshness-driven routing.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    primary_notes = int(payload.get("coverage", {}).get("primary_source_notes", 0))
    if primary_notes < 10:
        alerts.append(
            {
                "severity": "medium",
                "title": "Primary-source layer is still thin",
                "details": f"Only {primary_notes} primary-source notes are currently available.",
                "action": "Keep expanding Google and patent-style primary sources so downstream judgments stay anchored.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    return alerts[:8]


def build_opportunities(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    opportunities: List[Dict[str, Any]] = []

    pending_sources = payload.get("pending", {}).get("top_sources", [])
    if pending_sources:
        source_summary = ", ".join(f"{item['source']} ({item['count']})" for item in pending_sources[:4])
        opportunities.append(
            {
                "title": "Harvest backlog focus",
                "why_now": f"Pending sources are already identified: {source_summary}.",
                "action": "Convert these sources into article notes first so the agent layer has fresher material to reason over.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    live_articles = payload.get("recent_knowledge", {}).get("live_articles", [])
    if live_articles:
        note_summary = ", ".join(item["path"] for item in live_articles[:3])
        opportunities.append(
            {
                "title": "Fresh source exploitation",
                "why_now": f"Recent live notes landed in: {note_summary}.",
                "action": "Turn the freshest notes into answer-engine, content-gap, and technical-change briefs before they age out.",
                "files": [item["path"] for item in live_articles[:3]],
            }
        )

    primary_chunks = payload.get("db", {}).get("google_search_central_chunks", 0) + payload.get("db", {}).get("google_patent_chunks", 0)
    if primary_chunks > 0:
        opportunities.append(
            {
                "title": "Primary-source canon expansion",
                "why_now": f"Primary-source chunk inventory is already present ({primary_chunks} chunks) and can anchor durable guidance.",
                "action": "Use the primary layer to produce stricter technical SEO and AI-visibility operating notes, not just reactive summaries.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    live_article_sources = payload.get("sources", {}).get("live_article_sources", [])
    if live_article_sources:
        source_summary = ", ".join(f"{item['source']} ({item['article_count']})" for item in live_article_sources[:4])
        opportunities.append(
            {
                "title": "High-yield source patterns",
                "why_now": f"Live article velocity is clustering around: {source_summary}.",
                "action": "Extract repeated patterns from the top live sources and convert them into reusable SEO operating heuristics.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    recent_fetch_sources = payload.get("activity", {}).get("recent_fetch_sources", [])
    if recent_fetch_sources:
        source_summary = ", ".join(f"{item['source']} ({item['count']})" for item in recent_fetch_sources[:4])
        opportunities.append(
            {
                "title": "Hot-source radar",
                "why_now": f"Fresh fetch activity is concentrated in: {source_summary}.",
                "action": "Use the active fetch window to prioritize same-day triage, especially for AI-search and technical-search sources.",
                "files": ["automation/data/latest-status.json"],
            }
        )

    return opportunities[:6]


def build_digest(payload: Dict[str, Any], workspace: Path, status_json_path: Path, status_md_path: Path) -> Dict[str, Any]:
    recent_live = [item["path"] for item in payload.get("recent_knowledge", {}).get("live_articles", [])[:5]]
    recent_primary = [item["path"] for item in payload.get("recent_knowledge", {}).get("primary_notes", [])[:5]]
    return {
        "generated_at": now_utc_iso(),
        "workspace": str(workspace),
        "status_source": {
            "json": str(status_json_path),
            "markdown": str(status_md_path),
        },
        "headline": summarize_pipeline(payload),
        "metrics": {
            "chunks": payload["db"]["chunks"],
            "paths": payload["db"]["paths"],
            "progress_percent": payload["goal"]["progress_percent"],
            "pending_total": payload["pending"]["pending_total"],
            "live_article_notes": payload["articles"]["live_article_notes"],
            "archive_article_notes": payload["articles"]["archive_article_notes"],
            "primary_source_notes": payload["coverage"]["primary_source_notes"],
            "phase": payload["activity"]["current_phase"],
            "recent_fetch_ok": payload["activity"]["recent_fetch_ok"],
            "recent_fetch_error": payload["activity"]["recent_fetch_error"],
        },
        "alerts": build_alerts(payload),
        "opportunities": build_opportunities(payload),
        "recent_files": {
            "live_articles": recent_live,
            "primary_notes": recent_primary,
        },
    }


def render_digest_markdown(digest: Dict[str, Any]) -> str:
    lines = [
        "# OpenClaw SEO Automation Digest",
        "",
        f"Generated: {digest['generated_at']}",
        "",
        "## Headline",
        f"- {digest['headline']}",
        "",
        "## Metrics",
        f"- chunks: `{digest['metrics']['chunks']}`",
        f"- paths: `{digest['metrics']['paths']}`",
        f"- progress: `{digest['metrics']['progress_percent']}`%",
        f"- pending total: `{digest['metrics']['pending_total']}`",
        f"- live article notes: `{digest['metrics']['live_article_notes']}`",
        f"- archive article notes: `{digest['metrics']['archive_article_notes']}`",
        f"- primary source notes: `{digest['metrics']['primary_source_notes']}`",
        f"- current phase: `{digest['metrics']['phase']}`",
        f"- recent fetch ok/error: `{digest['metrics']['recent_fetch_ok']}` / `{digest['metrics']['recent_fetch_error']}`",
        "",
        "## Alerts",
    ]

    if digest["alerts"]:
        for alert in digest["alerts"]:
            lines.append(f"- [{alert['severity']}] {alert['title']} | {alert['details']} | action: {alert['action']}")
    else:
        lines.append("- No active alerts. Treat the system as steady-state, not complete.")

    lines.extend(["", "## Opportunities"])
    if digest["opportunities"]:
        for item in digest["opportunities"]:
            lines.append(f"- {item['title']} | why now: {item['why_now']} | action: {item['action']}")
    else:
        lines.append("- No high-signal opportunities were derived from the current status payload.")

    lines.extend(["", "## Recent Files"])
    if digest["recent_files"]["live_articles"]:
        lines.append("- live articles:")
        lines.extend(f"  - {path}" for path in digest["recent_files"]["live_articles"])
    else:
        lines.append("- live articles: none")
    if digest["recent_files"]["primary_notes"]:
        lines.append("- primary notes:")
        lines.extend(f"  - {path}" for path in digest["recent_files"]["primary_notes"])
    else:
        lines.append("- primary notes: none")
    lines.append("")
    return "\n".join(lines)


def automation_readme() -> str:
    return """# OpenClaw SEO Automation

This folder is the deterministic handoff between the shell-based SEO data engine and the OpenClaw SEO agent.

## Control Layer
- `control/command-center.json`: the single machine-readable view of what to trust right now.
- `control/command-center.md`: the human-readable operator desk with selected mission, trust checks, and immediate actions.
- `outbox/*-trusted.md`: stable aliases that always point at the best available watchtower, radar, and daily-plan artifacts.
- `missions/router/next-best-mission-trusted.md`: stable alias for the best current mission decision.

## Generated Inputs
- `data/latest-status.json`: machine-readable SEO Elite system status.
- `data/latest-status.md`: readable copy of the latest status.
- `digest/latest.json`: synthesized alert + opportunity payload for agentic triage.
- `digest/latest.md`: readable digest for fast review.
- `hq/current-plan.json`: structured HQ operating plan built from the router, queue, graph, and control-plane state.
- `hq/current-plan-deterministic.md`: deterministic HQ mission plan.
- `hq/role-handoffs.md`: readable role ownership and handoff map for the selected mission.
- `capabilities/local-stack.md`: local MCP and knowledge inventory.
- `capabilities/workflows.md`: recommended local workflows mapped to those tools.
- `missions/catalog.md`: reusable OpenClaw mission catalog built from the local stack.
- `missions/router/next-best-mission.md`: deterministic mission router output.
- `missions/execution/current-queue.md`: the active ordered task queue for the selected mission.
- `missions/execution/action-runner-state.json`: the latest deterministic execution-runner state.
- `missions/execution/artifacts/*`: task-level execution artifacts used for auto-progress and auditability.

## Agent Prompts
- `prompts/watchtower.md`: recurring operational watchtower brief.
- `prompts/opportunity-radar.md`: recurring opportunity triage brief.
- `prompts/daily-ops-plan.md`: recurring 24-hour plan brief.
- `prompts/mission-runner.md`: recurring mission-router brief.
- `prompts/hq-mission-runner.md`: recurring HQ planner brief.

## Agent Outputs
- `outbox/watchtower-latest.md`
- `outbox/watchtower-deterministic.md`
- `outbox/watchtower-trusted.md`
- `outbox/opportunity-radar.md`
- `outbox/opportunity-radar-deterministic.md`
- `outbox/opportunity-radar-trusted.md`
- `outbox/daily-ops-plan.md`
- `outbox/daily-ops-plan-deterministic.md`
- `outbox/daily-ops-plan-trusted.md`
- `missions/outbox/*.md`
- `missions/execution/*.md`
- `missions/execution/current-queue.md`
- `missions/execution/artifacts/*`
- `missions/router/next-best-mission.md`
- `missions/router/next-best-mission-deterministic.md`
- `missions/router/next-best-mission-trusted.md`
- `missions/router/mission-scoreboard.md`
- `hq/current-plan.md`
- `hq/current-plan-deterministic.md`
- `hq/current-plan-trusted.md`
- `hq/role-handoffs.md`

## Refresh Path
- Shell cron updates `seo_elite` status every 5 minutes.
- `refresh_openclaw_seo_automation.py` mirrors that status here and rebuilds the digest.
- `refresh_openclaw_seo_missions.py` converts that state into reusable workflow missions and OpenProse-ready programs.
- `run_openclaw_seo_action_runner.py` executes one supported queue task per cycle and leaves task artifacts behind for auto-progress.
- The control layer compares live agent-written files with deterministic companions so stale outputs are easier to spot.
- OpenClaw cron jobs should read only from this folder and write only to `outbox/` or `missions/router/`.
"""


def watchtower_prompt() -> str:
    return """# SEO Watchtower

Work only inside this SEO workspace.

Read:
- `MEMORY.md`
- `automation/README.md`
- `automation/control/command-center.md`
- `automation/capabilities/local-stack.md`
- `automation/capabilities/workflows.md`
- `automation/missions/execution/current-queue.md`
- `automation/digest/latest.md`
- `automation/data/latest-status.md`

Task:
- Overwrite `automation/outbox/watchtower-latest.md`.
- Include: current system state, top alerts, next 3 actions, and files used.
- Keep it under 220 words.
- If the automation files are missing or stale, write the blocker instead of guessing.
- Do not edit any file outside `automation/outbox/watchtower-latest.md`.
"""


def opportunity_radar_prompt() -> str:
    return """# SEO Opportunity Radar

Work only inside this SEO workspace.

Read:
- `MEMORY.md`
- `automation/README.md`
- `automation/control/command-center.md`
- `automation/capabilities/local-stack.md`
- `automation/capabilities/workflows.md`
- `automation/missions/execution/current-queue.md`
- `automation/digest/latest.md`
- `automation/data/latest-status.md`

Task:
- Overwrite `automation/outbox/opportunity-radar.md`.
- Include the best 3 opportunities across fresh-source research, technical/primary-source work, and AI-search or content opportunities.
- End with one recommended execution sequence for the next 24 hours.
- Keep it under 320 words.
- Do not edit any file outside `automation/outbox/opportunity-radar.md`.
"""


def daily_ops_prompt() -> str:
    return """# SEO Daily Ops Plan

Work only inside this SEO workspace.

Read:
- `automation/README.md`
- `automation/control/command-center.md`
- `automation/capabilities/local-stack.md`
- `automation/capabilities/workflows.md`
- `automation/missions/execution/current-queue.md`
- `automation/digest/latest.md`
- `automation/data/latest-status.md`
- `automation/outbox/watchtower-trusted.md`
- `automation/outbox/opportunity-radar-trusted.md`

Task:
- Overwrite `automation/outbox/daily-ops-plan.md`.
- Convert the latest status into a sequenced 24-hour plan with sections for `Now`, `Next 4 Hours`, `Next 12 Hours`, and `Next 24 Hours`.
- Prefer the trusted files named above if live agent outputs are stale or missing.
- Keep it under 350 words.
- Do not edit any file outside `automation/outbox/daily-ops-plan.md`.
"""


def mission_runner_prompt() -> str:
    return """# SEO Mission Runner

Work only inside this SEO workspace.

Read:
- `MEMORY.md`
- `automation/README.md`
- `automation/control/command-center.md`
- `../../memory/imports/codex/graph-hq/phase21/HQ_STATUS.md`
- `../../memory/imports/codex/graph-hq/phase31/GRAPH_STATUS.md`
- `automation/capabilities/local-stack.md`
- `automation/capabilities/workflows.md`
- `automation/missions/catalog.md`
- `automation/missions/router/mission-scoreboard.md`
- `automation/digest/latest.md`
- `automation/data/latest-status.md`

Task:
- Choose the best current SEO mission from `automation/missions/catalog.md`.
- Overwrite `automation/missions/router/next-best-mission.md`.
- Include sections: `Selected Workflow`, `Why This Wins Now`, `Stack`, and `First Actions`.
- Keep it under 260 words.
- Do not edit any file outside `automation/missions/router/next-best-mission.md`.
"""


def hq_mission_runner_prompt() -> str:
    return """# SEO HQ Mission Runner

Work only inside this SEO workspace.

Read:
- `MEMORY.md`
- `automation/README.md`
- `automation/control/command-center.md`
- `automation/hq/current-plan-trusted.md`
- `automation/hq/role-handoffs.md`
- `automation/capabilities/local-stack.md`
- `automation/missions/router/mission-scoreboard.md`
- `automation/missions/execution/current-queue.md`
- `automation/digest/latest.md`
- `automation/data/latest-status.md`
- `../../memory/imports/codex/graph-hq/phase21/HQ_STATUS.md`
- `../../memory/imports/codex/graph-hq/phase31/GRAPH_STATUS.md`
- `../../memory/imports/codex/skill-packs/INDEX.md`

Task:
- Overwrite `automation/hq/current-plan.md`.
- Include sections: `Selected Mission`, `HQ Signals`, `Role Handoffs`, `Approved Local Connectors`, `Success Checks`, and `Files Used`.
- Keep it under 360 words.
- Prefer the trusted HQ plan if the live plan is stale or missing.
- Do not edit any file outside `automation/hq/current-plan.md`.
"""


def render_fallback_watchtower(digest: Dict[str, Any]) -> str:
    lines = [
        "# SEO Watchtower",
        "",
        f"Generated by deterministic fallback at {digest['generated_at']}.",
        "",
        "## System State",
        f"- {digest['headline']}",
        "",
        "## Top Alerts",
    ]
    if digest["alerts"]:
        for alert in digest["alerts"][:3]:
            lines.append(f"- [{alert['severity']}] {alert['title']} | {alert['action']}")
    else:
        lines.append("- No active alerts.")
    lines.extend(["", "## Next Actions"])
    if digest["opportunities"]:
        for item in digest["opportunities"][:3]:
            lines.append(f"- {item['title']} | {item['action']}")
    else:
        lines.append("- Maintain the current pipeline and wait for the next refresh.")
    lines.append("")
    return "\n".join(lines)


def render_fallback_opportunity_radar(digest: Dict[str, Any]) -> str:
    lines = [
        "# SEO Opportunity Radar",
        "",
        f"Generated by deterministic fallback at {digest['generated_at']}.",
        "",
        "## Best Current Opportunities",
    ]
    if digest["opportunities"]:
        for item in digest["opportunities"]:
            lines.append(f"- {item['title']} | why now: {item['why_now']} | action: {item['action']}")
    else:
        lines.append("- No high-signal opportunities were derived from the current refresh.")
    lines.append("")
    return "\n".join(lines)


def render_fallback_daily_plan(digest: Dict[str, Any]) -> str:
    opportunity_titles = [item["title"] for item in digest["opportunities"][:3]]
    first = opportunity_titles[0] if opportunity_titles else "stability checks"
    second = opportunity_titles[1] if len(opportunity_titles) > 1 else "fresh-source review"
    third = opportunity_titles[2] if len(opportunity_titles) > 2 else "primary-source strengthening"
    lines = [
        "# SEO Daily Ops Plan",
        "",
        f"Generated by deterministic fallback at {digest['generated_at']}.",
        "",
        "## Now",
        f"- Review the current alerts and clear the highest-risk blocker first: {first}.",
        "",
        "## Next 4 Hours",
        f"- Push the strongest active opportunity: {second}.",
        "",
        "## Next 12 Hours",
        f"- Convert today's freshest source movement into durable notes or briefs: {third}.",
        "",
        "## Next 24 Hours",
        "- Re-run the same cycle, compare for drift, and let OpenClaw replace this fallback once model access is healthy.",
        "",
    ]
    return "\n".join(lines)


def artifact_mode(path: Path) -> str:
    if not path.exists():
        return "missing"
    text = path.read_text(encoding="utf-8", errors="replace")
    if "Generated by deterministic fallback" in text or "Generated by HQ deterministic fallback" in text:
        return "fallback"
    if "Awaiting the first OpenClaw" in text:
        return "placeholder"
    return "live"


def artifact_snapshot(path: Path, reference_dt: datetime | None) -> Dict[str, Any]:
    if not path.exists():
        return {
            "path": str(path),
            "exists": False,
            "mode": "missing",
            "freshness": "missing",
            "updated_at": None,
        }

    updated_dt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    freshness = "fresh"
    if reference_dt and updated_dt < reference_dt:
        freshness = "stale"

    return {
        "path": str(path),
        "exists": True,
        "mode": artifact_mode(path),
        "freshness": freshness,
        "updated_at": updated_dt.replace(microsecond=0).isoformat(),
    }


def choose_preferred_artifact(current: Dict[str, Any], deterministic: Dict[str, Any]) -> Dict[str, Any]:
    if current["exists"] and current["mode"] == "live" and current["freshness"] == "fresh":
        return current
    if deterministic["exists"] and deterministic["freshness"] == "fresh":
        return deterministic
    if current["exists"]:
        return current
    if deterministic["exists"]:
        return deterministic
    return current


def build_artifact_statuses(workspace: Path, payload: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    reference_dt = parse_iso_datetime(payload.get("updated_at_iso")) or parse_iso_datetime(now_utc_iso())
    outbox_dir = workspace / "automation" / "outbox"
    router_dir = workspace / "automation" / "missions" / "router"

    artifact_groups = {
        "watchtower": {
            "current": outbox_dir / "watchtower-latest.md",
            "deterministic": outbox_dir / "watchtower-deterministic.md",
            "trusted": outbox_dir / "watchtower-trusted.md",
        },
        "opportunity_radar": {
            "current": outbox_dir / "opportunity-radar.md",
            "deterministic": outbox_dir / "opportunity-radar-deterministic.md",
            "trusted": outbox_dir / "opportunity-radar-trusted.md",
        },
        "daily_ops_plan": {
            "current": outbox_dir / "daily-ops-plan.md",
            "deterministic": outbox_dir / "daily-ops-plan-deterministic.md",
            "trusted": outbox_dir / "daily-ops-plan-trusted.md",
        },
        "mission_router": {
            "current": router_dir / "next-best-mission.md",
            "deterministic": router_dir / "next-best-mission-deterministic.md",
            "trusted": router_dir / "next-best-mission-trusted.md",
        },
        "hq_mission_runner": {
            "current": workspace / "automation" / "hq" / "current-plan.md",
            "deterministic": workspace / "automation" / "hq" / "current-plan-deterministic.md",
            "trusted": workspace / "automation" / "hq" / "current-plan-trusted.md",
        },
    }

    statuses: Dict[str, Dict[str, Any]] = {}
    for key, paths in artifact_groups.items():
        current = artifact_snapshot(paths["current"], reference_dt)
        deterministic = artifact_snapshot(paths["deterministic"], reference_dt)
        preferred = choose_preferred_artifact(current, deterministic)
        statuses[key] = {
            "current": current,
            "deterministic": deterministic,
            "preferred": preferred,
            "trusted_path": str(paths["trusted"]),
        }
    return statuses


def build_command_center(
    workspace: Path,
    payload: Dict[str, Any],
    digest: Dict[str, Any],
    missions: Dict[str, Any],
    hq: Dict[str, Any],
    action_runner: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    route = missions["automatic_route"]
    artifacts = build_artifact_statuses(workspace, payload)
    queue = missions.get("current_queue")
    selected = route["selected"]
    alerts = digest["alerts"][:3]
    opportunities = digest["opportunities"][:3]

    fresh_live_count = sum(
        1
        for item in artifacts.values()
        if item["current"]["mode"] == "live" and item["current"]["freshness"] == "fresh"
    )
    if fresh_live_count >= 3:
        operating_mode = "live-assisted"
    elif fresh_live_count >= 1:
        operating_mode = "mixed"
    else:
        operating_mode = "deterministic-first"

    queue_focus = queue.get("current_focus") if isinstance(queue, dict) else None
    current_focus_role = hq.get("current_focus_role") if isinstance(hq, dict) else None
    next_moves = unique_preserve_order(
        [
            (
                f"Start `{queue_focus['title']}` from `automation/missions/execution/current-queue.md` with `{current_focus_role['role_label']}` owning the next handoff."
                if queue_focus and current_focus_role
                else (
                    f"Start `{queue_focus['title']}` from `automation/missions/execution/current-queue.md`."
                    if queue_focus
                    else f"Run or review `{selected['name']}` first."
                )
            ),
            (
                f"Review `automation/hq/current-plan-trusted.md` before changing mission direction."
                if hq
                else f"Run or review `{selected['name']}` first."
            ),
            *(alert["action"] for alert in alerts[:2]),
            *(item["action"] for item in opportunities[:1]),
        ]
    )[:4]

    return {
        "generated_at": now_utc_iso(),
        "operating_mode": operating_mode,
        "headline": digest["headline"],
        "selected_mission": {
            "id": selected["id"],
            "name": selected["name"],
            "score": route["score"],
            "confidence": route["confidence"],
            "reasons": route["reasons"],
            "blockers": route["blockers"],
            "score_breakdown": route["score_breakdown"],
            "prompt_path": selected["prompt_path"],
            "outbox_path": selected["outbox_path"],
        },
        "artifacts": artifacts,
        "execution_queue": {
            "path": missions.get("current_queue_markdown"),
            "summary": queue.get("summary") if isinstance(queue, dict) else None,
            "current_focus": queue_focus,
        }
        if isinstance(queue, dict)
        else None,
        "hq_runner": {
            "path": hq.get("current_plan_markdown"),
            "deterministic_path": hq.get("current_plan_deterministic_markdown"),
            "role_handoffs_path": hq.get("role_handoffs_markdown"),
            "current_focus_role": current_focus_role,
        }
        if isinstance(hq, dict)
        else None,
        "action_runner": action_runner,
        "alerts": alerts,
        "opportunities": opportunities,
        "next_moves": next_moves,
    }


def render_command_center_markdown(control: Dict[str, Any]) -> str:
    mission = control["selected_mission"]
    lines = [
        "# SEO Command Center",
        "",
        f"Generated: {control['generated_at']}",
        "",
        "## Right Now",
        f"- mode: `{control['operating_mode']}`",
        f"- headline: {control['headline']}",
        f"- selected mission: {mission['name']} (`{mission['id']}`) score=`{mission['score']}` confidence=`{mission['confidence']}`",
        "",
        "## Why This Mission",
    ]
    lines.extend(f"- {reason}" for reason in mission["reasons"][:4])

    if mission["blockers"]:
        lines.extend(["", "## Blockers"])
        lines.extend(f"- {item}" for item in mission["blockers"])

    execution_queue = control.get("execution_queue")
    if execution_queue:
        lines.extend(
            [
                "",
                "## Execution Queue",
                f"- file: `{execution_queue['path']}`",
                (
                    "- summary: "
                    f"done=`{execution_queue['summary']['done']}` "
                    f"ready=`{execution_queue['summary']['ready']}` "
                    f"at-risk=`{execution_queue['summary']['at_risk']}` "
                    f"queued=`{execution_queue['summary']['queued']}` "
                    f"blocked=`{execution_queue['summary']['blocked']}`"
                ),
            ]
        )
        focus = execution_queue.get("current_focus")
        if focus:
            lines.append(
                f"- current focus: {focus['title']} (`{focus['status']}`) -> {focus['deliverable']}"
            )

    hq_runner = control.get("hq_runner")
    if hq_runner:
        lines.extend(
            [
                "",
                "## HQ Runner",
                f"- plan: `{hq_runner['path']}`",
                f"- deterministic fallback: `{hq_runner['deterministic_path']}`",
                f"- role handoffs: `{hq_runner['role_handoffs_path']}`",
            ]
        )
        if hq_runner.get("current_focus_role"):
            lines.append(
                f"- current focus owner: {hq_runner['current_focus_role']['role_label']} (`{hq_runner['current_focus_role']['skill_pack']}`)"
            )

    action_runner = control.get("action_runner")
    if action_runner:
        lines.extend(
            [
                "",
                "## Action Runner",
                f"- state: `{action_runner['status']}`",
                f"- queue: `{action_runner['queue_path']}`",
                f"- state file: `{action_runner['state_path']}`",
                f"- executed this refresh: `{action_runner['executed_count']}`",
            ]
        )
        if action_runner.get("executed_tasks"):
            latest = action_runner["executed_tasks"][-1]
            lines.append(
                f"- latest task: {latest['task_title']} -> `{latest['artifact_markdown_path']}`"
            )
        if action_runner.get("blocked_reason"):
            lines.append(f"- blocked reason: {action_runner['blocked_reason']}")

    lines.extend(["", "## Trust Check"])
    for label, artifact in control["artifacts"].items():
        preferred = artifact["preferred"]
        lines.append(
            f"- {label}: use `{artifact['trusted_path']}` -> source `{preferred['path']}` | mode=`{preferred['mode']}` freshness=`{preferred['freshness']}`"
        )

    lines.extend(["", "## Immediate Moves"])
    lines.extend(f"- {item}" for item in control["next_moves"])

    if control["alerts"]:
        lines.extend(["", "## Watch Items"])
        for alert in control["alerts"]:
            lines.append(f"- {alert['title']} | {alert['action']}")

    lines.append("")
    return "\n".join(lines)


def write_outbox_file(path: Path, text: str) -> None:
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if "Awaiting the first OpenClaw cron run." not in current and "Generated by deterministic fallback" not in current:
            return
    path.write_text(text, encoding="utf-8")


def trusted_artifact_text(preferred: Dict[str, Any]) -> str:
    source_path = Path(preferred["path"])
    if not source_path.exists():
        return (
            f"<!-- trusted-source: {preferred['path']} -->\n"
            f"<!-- trusted-mode: {preferred['mode']} -->\n"
            f"<!-- trusted-freshness: {preferred['freshness']} -->\n"
            "\n"
            "# Trusted Artifact Unavailable\n\n"
            "The preferred source file is missing.\n"
        )

    body = source_path.read_text(encoding="utf-8")
    header = (
        f"<!-- trusted-source: {preferred['path']} -->\n"
        f"<!-- trusted-mode: {preferred['mode']} -->\n"
        f"<!-- trusted-freshness: {preferred['freshness']} -->\n\n"
    )
    return header + body


def write_trusted_artifacts(control_payload: Dict[str, Any]) -> Dict[str, str]:
    written: Dict[str, str] = {}
    for artifact in control_payload["artifacts"].values():
        trusted_path = Path(artifact["trusted_path"])
        trusted_path.parent.mkdir(parents=True, exist_ok=True)
        trusted_path.write_text(trusted_artifact_text(artifact["preferred"]), encoding="utf-8")
        written[trusted_path.stem.replace("-", "_")] = str(trusted_path)
    return written


def write_generated_files(workspace: Path, payload: Dict[str, Any], digest: Dict[str, Any], status_json_path: Path, status_md_path: Path) -> Dict[str, str]:
    automation_root = workspace / "automation"
    control_dir = automation_root / "control"
    data_dir = automation_root / "data"
    digest_dir = automation_root / "digest"
    hq_dir = automation_root / "hq"
    prompts_dir = automation_root / "prompts"
    outbox_dir = automation_root / "outbox"

    for path in (automation_root, control_dir, data_dir, digest_dir, hq_dir, prompts_dir, outbox_dir):
        path.mkdir(parents=True, exist_ok=True)

    status_json_target = data_dir / "latest-status.json"
    status_md_target = data_dir / "latest-status.md"
    digest_json_target = digest_dir / "latest.json"
    digest_md_target = digest_dir / "latest.md"

    status_json_target.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    if status_md_path.exists():
        status_md_target.write_text(status_md_path.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        status_md_target.write_text(render_status_markdown(payload), encoding="utf-8")

    digest_json_target.write_text(json.dumps(digest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    digest_md_target.write_text(render_digest_markdown(digest), encoding="utf-8")

    (automation_root / "README.md").write_text(automation_readme(), encoding="utf-8")
    (prompts_dir / "watchtower.md").write_text(watchtower_prompt(), encoding="utf-8")
    (prompts_dir / "opportunity-radar.md").write_text(opportunity_radar_prompt(), encoding="utf-8")
    (prompts_dir / "daily-ops-plan.md").write_text(daily_ops_prompt(), encoding="utf-8")
    (prompts_dir / "mission-runner.md").write_text(mission_runner_prompt(), encoding="utf-8")
    (prompts_dir / "hq-mission-runner.md").write_text(hq_mission_runner_prompt(), encoding="utf-8")

    watchtower_fallback = render_fallback_watchtower(digest)
    opportunity_fallback = render_fallback_opportunity_radar(digest)
    daily_plan_fallback = render_fallback_daily_plan(digest)

    write_outbox_file(outbox_dir / "watchtower-latest.md", watchtower_fallback)
    write_outbox_file(outbox_dir / "opportunity-radar.md", opportunity_fallback)
    write_outbox_file(outbox_dir / "daily-ops-plan.md", daily_plan_fallback)
    (outbox_dir / "watchtower-deterministic.md").write_text(watchtower_fallback, encoding="utf-8")
    (outbox_dir / "opportunity-radar-deterministic.md").write_text(opportunity_fallback, encoding="utf-8")
    (outbox_dir / "daily-ops-plan-deterministic.md").write_text(daily_plan_fallback, encoding="utf-8")

    return {
        "automation_root": str(automation_root),
        "control_dir": str(control_dir),
        "status_json": str(status_json_target),
        "status_markdown": str(status_md_target),
        "digest_json": str(digest_json_target),
        "digest_markdown": str(digest_md_target),
    }
def write_control_files(
    workspace: Path,
    payload: Dict[str, Any],
    digest: Dict[str, Any],
    missions: Dict[str, Any],
    hq: Dict[str, Any],
    action_runner: Dict[str, Any] | None = None,
) -> Dict[str, str]:
    control_dir = workspace / "automation" / "control"
    control_dir.mkdir(parents=True, exist_ok=True)

    control_payload = build_command_center(
        workspace=workspace,
        payload=payload,
        digest=digest,
        missions=missions,
        hq=hq,
        action_runner=action_runner,
    )
    control_json = control_dir / "command-center.json"
    control_md = control_dir / "command-center.md"

    control_json.write_text(json.dumps(control_payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    control_md.write_text(render_command_center_markdown(control_payload), encoding="utf-8")
    trusted = write_trusted_artifacts(control_payload)

    return {
        "command_center_json": str(control_json),
        "command_center_markdown": str(control_md),
        **trusted,
    }


def refresh_openclaw_seo_automation(status_json_path: Path, status_md_path: Path, workspace: Path) -> Dict[str, Any]:
    payload = load_status_payload(status_json_path)
    digest = build_digest(payload, workspace, status_json_path, status_md_path)
    stack = refresh_local_seo_stack(workspace)
    written = write_generated_files(workspace, payload, digest, status_json_path, status_md_path)
    missions = refresh_openclaw_seo_missions(workspace=workspace, payload=payload, digest=digest)
    hq = refresh_openclaw_hq_mission_runner(workspace=workspace, payload=payload, digest=digest, missions=missions)
    action_runner = run_openclaw_seo_action_runner(workspace=workspace, max_tasks=1)
    if action_runner.get("executed_count", 0) > 0:
        missions = refresh_openclaw_seo_missions(workspace=workspace, payload=payload, digest=digest)
        hq = refresh_openclaw_hq_mission_runner(workspace=workspace, payload=payload, digest=digest, missions=missions)
    control = write_control_files(
        workspace=workspace,
        payload=payload,
        digest=digest,
        missions=missions,
        hq=hq,
        action_runner=action_runner,
    )
    return {
        "status": "ok",
        "generated_at": digest["generated_at"],
        "workspace": str(workspace),
        "headline": digest["headline"],
        "alerts": len(digest["alerts"]),
        "opportunities": len(digest["opportunities"]),
        "local_stack": stack,
        "missions": missions,
        "hq": hq,
        "action_runner": action_runner,
        "control": control,
        "written": written,
    }


def main() -> int:
    args = parse_args()
    result = refresh_openclaw_seo_automation(
        status_json_path=Path(args.status_json),
        status_md_path=Path(args.status_md),
        workspace=Path(args.openclaw_workspace),
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(
            f"OpenClaw SEO automation refreshed | alerts={result['alerts']} "
            f"opportunities={result['opportunities']} workspace={result['workspace']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
