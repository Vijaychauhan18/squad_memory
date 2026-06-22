#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from openclaw_hq_context import build_graph_hq_context
from refresh_openclaw_seo_missions import refresh_openclaw_seo_missions


HOME = Path.home()
DEFAULT_WORKSPACE = HOME / ".openclaw" / "workspace" / "squad" / "seo"

ROLE_LIBRARY: Dict[str, Dict[str, str]] = {
    "pinchy": {
        "label": "Pinchy",
        "skill_pack": "orchestrator-pinchy",
        "summary": "Orchestrates the mission, decides sequencing, and resolves blockers.",
    },
    "coral": {
        "label": "Coral",
        "skill_pack": "seo-coral",
        "summary": "Owns SEO judgment, prioritization, and recommendation quality.",
    },
    "kelp": {
        "label": "Kelp",
        "skill_pack": "researcher-kelp",
        "summary": "Pulls evidence, canon support, and context before decisions are locked.",
    },
    "plankton": {
        "label": "Plankton",
        "skill_pack": "writer-plankton",
        "summary": "Turns findings into briefs, copy, and operator-facing assets.",
    },
    "chitin": {
        "label": "Chitin",
        "skill_pack": "developer-chitin",
        "summary": "Translates technical findings into fix plans and implementation-ready tasks.",
    },
    "reef": {
        "label": "Reef",
        "skill_pack": "qa-reef",
        "summary": "Validates fixes, catches regressions, and keeps execution defensible.",
    },
}

MISSION_ROLE_PLANS: Dict[str, List[Dict[str, Any]]] = {
    "freshness-radar": [
        {
            "role": "pinchy",
            "responsibility": "Set the operating order and collapse the fresh evidence into one clear bet.",
            "handoff_when": "Before the queue starts moving and again before publish.",
            "tasks": ["collect-fresh-signals", "publish-priority-output"],
        },
        {
            "role": "kelp",
            "responsibility": "Pull fresh evidence and supporting canon so the same-day move is grounded.",
            "handoff_when": "Immediately after Pinchy sets the priority.",
            "tasks": ["collect-fresh-signals", "retrieve-supporting-canon"],
        },
        {
            "role": "coral",
            "responsibility": "Turn the evidence into the final SEO brief and ranked actions.",
            "handoff_when": "Once fresh evidence and canon support are gathered.",
            "tasks": ["draft-same-day-brief", "publish-priority-output"],
        },
    ],
    "gsc-opportunity-mining": [
        {
            "role": "pinchy",
            "responsibility": "Keep the opportunity sweep focused on the highest-lift segment first.",
            "handoff_when": "At mission start and before the final queue is published.",
            "tasks": ["pull-page-query-opportunities", "publish-improvement-queue"],
        },
        {
            "role": "kelp",
            "responsibility": "Gather the page/query evidence and outside context that explains the upside.",
            "handoff_when": "After mission selection and before SEO judgment is locked.",
            "tasks": ["pull-page-query-opportunities"],
        },
        {
            "role": "coral",
            "responsibility": "Own intent diagnosis, CTR reasoning, and the ranked win list.",
            "handoff_when": "After the raw evidence is collected.",
            "tasks": ["analyze-intent-title-gaps", "rank-top-wins"],
        },
        {
            "role": "plankton",
            "responsibility": "Package the improvement queue into a clear editing brief for operators.",
            "handoff_when": "At the publish stage.",
            "tasks": ["publish-improvement-queue"],
        },
    ],
    "cannibalization-cleanup": [
        {
            "role": "pinchy",
            "responsibility": "Keep the cleanup limited to the highest-cost overlap clusters first.",
            "handoff_when": "At mission start and before plan publication.",
            "tasks": ["find-overlap-clusters", "publish-canonicalization-plan"],
        },
        {
            "role": "kelp",
            "responsibility": "Pull evidence on overlapping URLs and confirm context before merge choices.",
            "handoff_when": "After mission selection.",
            "tasks": ["find-overlap-clusters", "confirm-winning-urls"],
        },
        {
            "role": "coral",
            "responsibility": "Choose winners, losers, and SEO-safe merge logic.",
            "handoff_when": "Once evidence is in.",
            "tasks": ["confirm-winning-urls", "define-merge-actions"],
        },
        {
            "role": "chitin",
            "responsibility": "Translate consolidation decisions into implementation-ready redirect and link actions.",
            "handoff_when": "At the action-definition stage.",
            "tasks": ["define-merge-actions", "publish-canonicalization-plan"],
        },
    ],
    "indexation-war-room": [
        {
            "role": "pinchy",
            "responsibility": "Run the war-room order and keep the team on the highest-severity URLs first.",
            "handoff_when": "At mission start and before the brief is published.",
            "tasks": ["inspect-affected-urls", "publish-war-room-brief"],
        },
        {
            "role": "coral",
            "responsibility": "Lead the indexing diagnosis and rank the SEO repair order.",
            "handoff_when": "Immediately after affected URLs are identified.",
            "tasks": ["inspect-affected-urls", "rank-fix-order"],
        },
        {
            "role": "chitin",
            "responsibility": "Trace technical causes and convert them into fixable implementation slices.",
            "handoff_when": "After the affected set is known.",
            "tasks": ["crawl-technical-causes", "rank-fix-order"],
        },
        {
            "role": "reef",
            "responsibility": "Validate the war-room repair order and the checks needed before rollout.",
            "handoff_when": "Before the final brief is published.",
            "tasks": ["publish-war-room-brief"],
        },
    ],
    "content-gap-to-brief": [
        {
            "role": "pinchy",
            "responsibility": "Choose the single gap worth briefing now and keep the scope tight.",
            "handoff_when": "At mission start and before publish.",
            "tasks": ["select-topic-gap", "publish-content-brief"],
        },
        {
            "role": "kelp",
            "responsibility": "Gather the best supporting canon, SERP context, and evidence of the missing angle.",
            "handoff_when": "After the gap is named.",
            "tasks": ["select-topic-gap", "route-pack-and-canon"],
        },
        {
            "role": "coral",
            "responsibility": "Own search intent, opportunity framing, and the SEO angle of the brief.",
            "handoff_when": "After context is gathered.",
            "tasks": ["analyze-intent-gap", "route-pack-and-canon"],
        },
        {
            "role": "plankton",
            "responsibility": "Turn the gap analysis into a writer-ready brief with concrete deliverables.",
            "handoff_when": "At the publish stage.",
            "tasks": ["publish-content-brief"],
        },
    ],
    "technical-audit-sprint": [
        {
            "role": "pinchy",
            "responsibility": "Keep the audit sprint constrained to the highest-value fixes.",
            "handoff_when": "At mission start and before the issue queue is shipped.",
            "tasks": ["crawl-technical-snapshot", "publish-issue-queue"],
        },
        {
            "role": "coral",
            "responsibility": "Lead SEO risk analysis and prioritize what matters most.",
            "handoff_when": "After the crawl snapshot lands.",
            "tasks": ["crawl-technical-snapshot", "prioritize-fixes"],
        },
        {
            "role": "chitin",
            "responsibility": "Turn issues into concrete implementation and system-change tasks.",
            "handoff_when": "During prioritization and issue-queue assembly.",
            "tasks": ["analyze-link-and-eeat-risks", "publish-issue-queue"],
        },
        {
            "role": "reef",
            "responsibility": "Add validation checks so fixes can be verified cleanly after execution.",
            "handoff_when": "Before the issue queue is finalized.",
            "tasks": ["prioritize-fixes", "publish-issue-queue"],
        },
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an HQ-aware mission plan from the local SEO mission router")
    parser.add_argument("--workspace", default=str(DEFAULT_WORKSPACE))
    parser.add_argument("--status-json", default=str(DEFAULT_WORKSPACE / "automation" / "data" / "latest-status.json"))
    parser.add_argument("--digest-json", default=str(DEFAULT_WORKSPACE / "automation" / "digest" / "latest.json"))
    parser.add_argument("--goal", help="Optional explicit goal to route before building the HQ plan")
    parser.add_argument("--graph-hq-root", help="Optional shared graph/HQ import root")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_managed_text(path: Path, text: str) -> None:
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if "Generated by HQ deterministic fallback" not in current and "Awaiting the first HQ mission run." not in current:
            return
    path.write_text(text, encoding="utf-8")


def hq_readme() -> str:
    return """# HQ Mission Runner

This folder turns the mission router, queue, graph, and control-plane state into one operating plan.

## Files
- `current-plan.json`: structured HQ plan for the selected mission.
- `current-plan-deterministic.md`: deterministic HQ plan generated from local state.
- `current-plan.md`: live HQ plan target for OpenClaw cron runs.
- `role-handoffs.json`: structured role ownership and handoff map.
- `role-handoffs.md`: readable role ownership map.

## Use Rule
- Treat `current-plan-deterministic.md` as the trusted fallback when the live plan is stale or missing.
- Use `role-handoffs.md` to decide which squad role should own the current focus task.
"""


def role_skill_path(skill_pack: str) -> str:
    return f"../../memory/imports/codex/skill-packs/{skill_pack}/SKILL.md"


def default_role_plan() -> List[Dict[str, Any]]:
    return [
        {
            "role": "pinchy",
            "responsibility": "Own sequencing and resolve blockers before execution drifts.",
            "handoff_when": "At mission start and before final publish.",
            "tasks": [],
        },
        {
            "role": "kelp",
            "responsibility": "Gather supporting context and evidence before decisions are finalized.",
            "handoff_when": "Immediately after mission selection.",
            "tasks": [],
        },
        {
            "role": "coral",
            "responsibility": "Own final SEO judgment and operator recommendations.",
            "handoff_when": "After evidence is assembled.",
            "tasks": [],
        },
    ]


def fallback_role_for_item(item: Dict[str, Any]) -> str:
    owner = item.get("owner", "agent")
    if owner == "mixed":
        return "pinchy"
    if item.get("priority") == "later":
        return "plankton"
    return "coral"


def build_role_handoffs(current_queue: Dict[str, Any], selected_route: Dict[str, Any]) -> Dict[str, Any]:
    mission_id = selected_route["selected"]["id"]
    plan = MISSION_ROLE_PLANS.get(mission_id, default_role_plan())
    items = current_queue.get("items", [])
    items_by_suffix = {item["id"].split(".", 1)[-1]: item for item in items}
    current_focus = current_queue.get("current_focus") if isinstance(current_queue.get("current_focus"), dict) else None
    current_focus_id = ""
    if current_focus:
        current_focus_id = current_focus["id"].split(".", 1)[-1]

    handoffs: List[Dict[str, Any]] = []
    task_owner_map: Dict[str, str] = {}
    for entry in plan:
        for task_id in entry.get("tasks", []):
            item = items_by_suffix.get(task_id)
            if not item:
                continue
            task_owner_map[item["id"]] = entry["role"]

    current_focus_role_id = task_owner_map.get(current_focus.get("id", "") if current_focus else "")

    for entry in plan:
        role = ROLE_LIBRARY[entry["role"]]
        assigned_tasks: List[Dict[str, Any]] = []
        for task_id in entry.get("tasks", []):
            item = items_by_suffix.get(task_id)
            if not item:
                continue
            assigned_tasks.append(
                {
                    "id": item["id"],
                    "title": item["title"],
                    "status": item["status"],
                    "deliverable": item["deliverable"],
                }
            )
        handoffs.append(
            {
                "role_id": entry["role"],
                "label": role["label"],
                "skill_pack": role["skill_pack"],
                "skill_path": role_skill_path(role["skill_pack"]),
                "summary": role["summary"],
                "responsibility": entry["responsibility"],
                "handoff_when": entry["handoff_when"],
                "assigned_tasks": assigned_tasks,
                "is_current_focus": current_focus_role_id == entry["role"],
            }
        )

    queue_assignments: List[Dict[str, Any]] = []
    for item in items:
        role_id = task_owner_map.get(item["id"], fallback_role_for_item(item))
        role = ROLE_LIBRARY[role_id]
        queue_assignments.append(
            {
                "task_id": item["id"],
                "task_title": item["title"],
                "status": item["status"],
                "role_id": role_id,
                "role_label": role["label"],
                "skill_pack": role["skill_pack"],
                "skill_path": role_skill_path(role["skill_pack"]),
            }
        )

    current_focus_role = None
    if current_focus:
        current_focus_role = next(
            (item for item in queue_assignments if item["task_id"] == current_focus["id"]),
            None,
        )

    return {
        "mission_id": mission_id,
        "handoffs": handoffs,
        "queue_assignments": queue_assignments,
        "current_focus_role": current_focus_role,
    }


def build_connector_plan(selected_route: Dict[str, Any], components_by_id: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    connectors: List[Dict[str, Any]] = []
    for component_id in selected_route["selected"].get("stack", []):
        component = components_by_id.get(component_id, {})
        connectors.append(
            {
                "id": component_id,
                "label": component.get("label", component_id),
                "status": component.get("status", "missing"),
                "summary": component.get("summary", ""),
                "command": component.get("command", "local artifact only"),
                "tools": component.get("tools", [])[:8],
            }
        )
    return connectors


def build_success_checks(
    selected_route: Dict[str, Any],
    current_queue: Dict[str, Any],
    connectors: List[Dict[str, Any]],
    hq_context: Dict[str, Any],
) -> List[Dict[str, Any]]:
    ready_connectors = sum(1 for item in connectors if item["status"] == "ready")
    current_focus = current_queue.get("current_focus") if isinstance(current_queue.get("current_focus"), dict) else None
    checks = [
        {
            "label": "HQ imports are available",
            "status": "ok" if hq_context.get("ready") else "at-risk",
            "details": "Both Phase 21 HQ and Phase 31 graph snapshots were found."
            if hq_context.get("ready")
            else "The plan can run, but HQ or graph inputs are partial or missing.",
        },
        {
            "label": "Mission queue has an active focus",
            "status": "ok" if current_focus else "blocked",
            "details": current_focus.get("title", "No current focus task was identified.")
            if current_focus
            else "No current focus task was identified.",
        },
        {
            "label": "Approved local connectors are available",
            "status": "ok" if ready_connectors > 0 else "blocked",
            "details": f"{ready_connectors} ready connector(s) are attached to this mission stack.",
        },
        {
            "label": "Mission output target exists",
            "status": "ok" if selected_route["selected"].get("outbox_path") else "at-risk",
            "details": selected_route["selected"].get("outbox_path", "No outbox path found in route payload."),
        },
    ]
    return checks


def render_role_handoffs_markdown(role_payload: Dict[str, Any]) -> str:
    lines = [
        "# HQ Role Handoffs",
        "",
        f"Generated: {now_utc_iso()}",
        "",
    ]
    for handoff in role_payload["handoffs"]:
        lines.extend(
            [
                f"## {handoff['label']}",
                f"- skill pack: `{handoff['skill_pack']}`",
                f"- skill path: `{handoff['skill_path']}`",
                f"- responsibility: {handoff['responsibility']}",
                f"- handoff when: {handoff['handoff_when']}",
                f"- current focus owner: `{handoff['is_current_focus']}`",
            ]
        )
        if handoff["assigned_tasks"]:
            lines.append("- assigned tasks:")
            for task in handoff["assigned_tasks"]:
                lines.append(f"  - {task['title']} (`{task['status']}`) -> {task['deliverable']}")
        else:
            lines.append("- assigned tasks: none")
        lines.append("")
    return "\n".join(lines)


def render_current_plan_markdown(plan: Dict[str, Any]) -> str:
    route = plan["selected_route"]
    queue = plan["current_queue"]
    lines = [
        "# HQ Mission Runner",
        "",
        f"Generated by HQ deterministic fallback at {plan['generated_at']}.",
        "",
        "## Selected Mission",
        f"- mission: {route['selected']['name']} (`{route['selected']['id']}`)",
        f"- score / confidence: `{route['score']}` / `{route['confidence']}`",
        f"- objective: {route['selected']['objective']}",
    ]
    if queue.get("current_focus"):
        focus = queue["current_focus"]
        lines.append(
            f"- current focus: {focus['title']} (`{focus['status']}`) -> {focus['deliverable']}"
        )
    lines.extend(["", "## HQ Signals"])
    lines.append(f"- SEO queue hold: `{plan['hq_context']['phase21']['seo_queue_hold']}`")
    lines.append(f"- SEO stale sources: `{plan['hq_context']['phase21']['seo_stale_sources']}`")
    lines.append(f"- graph topics / paths / links: `{plan['hq_context']['phase31']['topics_total']}` / `{plan['hq_context']['phase31']['memory_paths_total']}` / `{plan['hq_context']['phase31']['links_total']}`")
    lines.append(f"- graph primary skill accuracy: `{plan['hq_context']['phase31']['primary_skill_accuracy']:.2%}`")
    lines.extend(["", "## Why This Wins"])
    lines.extend(f"- {reason}" for reason in route["reasons"][:4])
    lines.extend(["", "## Role Handoffs"])
    for handoff in plan["role_handoffs"]["handoffs"]:
        marker = " current-focus-owner" if handoff["is_current_focus"] else ""
        lines.append(
            f"- {handoff['label']}{marker} | {handoff['responsibility']} | handoff when: {handoff['handoff_when']}"
        )
    lines.extend(["", "## Approved Local Connectors"])
    for connector in plan["connectors"]:
        lines.append(
            f"- {connector['label']} (`{connector['status']}`) | command: `{connector['command']}`"
        )
        if connector["tools"]:
            lines.append(f"  tools: {', '.join(connector['tools'])}")
    lines.extend(["", "## Success Checks"])
    for check in plan["success_checks"]:
        lines.append(f"- [{check['status']}] {check['label']} | {check['details']}")
    lines.extend(["", "## Files Used"])
    lines.extend(f"- `{path}`" for path in plan["files_used"])
    lines.append("")
    return "\n".join(lines)


def build_hq_plan(
    workspace: Path,
    payload: Dict[str, Any],
    digest: Dict[str, Any],
    missions: Dict[str, Any],
    graph_hq_root: Path | None = None,
) -> Dict[str, Any]:
    capabilities = load_json(workspace / "automation" / "capabilities" / "local-stack.json")
    components = capabilities.get("components", [])
    components_by_id = {component["id"]: component for component in components}
    selected_route = missions.get("goal_route") or missions["automatic_route"]
    current_queue = missions.get("current_queue", {})
    hq_context = build_graph_hq_context(workspace, graph_hq_root=graph_hq_root)
    role_handoffs = build_role_handoffs(current_queue, selected_route)
    connectors = build_connector_plan(selected_route, components_by_id)
    success_checks = build_success_checks(selected_route, current_queue, connectors, hq_context)

    files_used = [
        "automation/control/command-center.md",
        "automation/missions/router/mission-scoreboard.md",
        "automation/missions/execution/current-queue.md",
        "automation/capabilities/local-stack.md",
        "automation/digest/latest.md",
        "automation/data/latest-status.md",
        "../../memory/imports/codex/graph-hq/phase21/HQ_STATUS.md",
        "../../memory/imports/codex/graph-hq/phase31/GRAPH_STATUS.md",
        "../../memory/imports/codex/skill-packs/INDEX.md",
    ]

    return {
        "generated_at": now_utc_iso(),
        "workspace": str(workspace),
        "headline": digest.get("headline", ""),
        "selected_route": selected_route,
        "current_queue": current_queue,
        "hq_context": hq_context,
        "role_handoffs": role_handoffs,
        "connectors": connectors,
        "success_checks": success_checks,
        "files_used": files_used,
    }


def refresh_openclaw_hq_mission_runner(
    workspace: Path,
    payload: Dict[str, Any],
    digest: Dict[str, Any],
    missions: Dict[str, Any] | None = None,
    goal: str | None = None,
    graph_hq_root: Path | None = None,
) -> Dict[str, Any]:
    if missions is None:
        missions = refresh_openclaw_seo_missions(
            workspace=workspace,
            payload=payload,
            digest=digest,
            goal=goal,
            graph_hq_root=graph_hq_root,
        )

    hq_root = workspace / "automation" / "hq"
    hq_root.mkdir(parents=True, exist_ok=True)
    readme_path = hq_root / "README.md"
    current_plan_json = hq_root / "current-plan.json"
    current_plan_md = hq_root / "current-plan.md"
    current_plan_deterministic_md = hq_root / "current-plan-deterministic.md"
    role_handoffs_json = hq_root / "role-handoffs.json"
    role_handoffs_md = hq_root / "role-handoffs.md"

    plan = build_hq_plan(workspace, payload, digest, missions, graph_hq_root=graph_hq_root)
    current_plan_text = render_current_plan_markdown(plan)

    readme_path.write_text(hq_readme(), encoding="utf-8")
    current_plan_json.write_text(json.dumps(plan, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    current_plan_deterministic_md.write_text(current_plan_text, encoding="utf-8")
    role_handoffs_json.write_text(json.dumps(plan["role_handoffs"], indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    role_handoffs_md.write_text(render_role_handoffs_markdown(plan["role_handoffs"]), encoding="utf-8")
    write_managed_text(current_plan_md, current_plan_text)

    return {
        "status": "ok",
        "generated_at": plan["generated_at"],
        "workspace": str(workspace),
        "current_plan_json": str(current_plan_json),
        "current_plan_markdown": str(current_plan_md),
        "current_plan_deterministic_markdown": str(current_plan_deterministic_md),
        "role_handoffs_json": str(role_handoffs_json),
        "role_handoffs_markdown": str(role_handoffs_md),
        "selected_mission_id": plan["selected_route"]["selected"]["id"],
        "current_focus_role": plan["role_handoffs"]["current_focus_role"],
        "hq_context": plan["hq_context"],
    }


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace)
    payload = load_json(Path(args.status_json))
    digest = load_json(Path(args.digest_json))
    result = refresh_openclaw_hq_mission_runner(
        workspace=workspace,
        payload=payload,
        digest=digest,
        goal=args.goal,
        graph_hq_root=Path(args.graph_hq_root) if args.graph_hq_root else None,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(
            f"HQ mission runner refreshed | mission={result['selected_mission_id']} "
            f"workspace={result['workspace']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
