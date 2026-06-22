#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


HOME = Path.home()
DEFAULT_WORKSPACE = HOME / ".openclaw" / "workspace" / "squad" / "seo"
SUPPORTED_COMPONENTS = {"seo_elite_knowledge", "seo_memory_mcp"}
STOPWORDS = {
    "a",
    "about",
    "and",
    "busbud",
    "for",
    "from",
    "into",
    "latest",
    "local",
    "new",
    "note",
    "notes",
    "same",
    "seo",
    "source",
    "sources",
    "the",
    "this",
    "today",
    "update",
    "with",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run deterministic OpenClaw SEO mission actions for the current queue")
    parser.add_argument("--workspace", default=str(DEFAULT_WORKSPACE))
    parser.add_argument("--max-tasks", type=int, default=1, help="Maximum supported tasks to execute in one run")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def normalize_tokens(*parts: str) -> List[str]:
    tokens: List[str] = []
    for part in parts:
        tokens.extend(re.findall(r"[a-z0-9]+", part.lower()))
    unique: List[str] = []
    seen: set[str] = set()
    for token in tokens:
        if len(token) < 3 or token in STOPWORDS or token.isdigit():
            continue
        if token in seen:
            continue
        seen.add(token)
        unique.append(token)
    return unique


def relative_memory_root(workspace: Path) -> Path:
    return workspace.parents[1] / "memory" / "imports" / "codex" / "skill-packs" / "seo" / "memory"


def current_queue_paths(workspace: Path) -> Tuple[Path, Path]:
    execution_root = workspace / "automation" / "missions" / "execution"
    return execution_root / "current-queue.json", execution_root / "action-runner-state.json"


def artifact_paths(workspace: Path, item: Dict[str, Any]) -> Tuple[Path, Path]:
    return workspace / item["artifact_markdown_path"], workspace / item["artifact_json_path"]


def artifact_exists(workspace: Path, item: Dict[str, Any]) -> bool:
    markdown_path, json_path = artifact_paths(workspace, item)
    return markdown_path.exists() and json_path.exists()


def load_runner_state(path: Path) -> Dict[str, Any]:
    payload = load_json(path)
    if not payload:
        return {"runs": []}
    if not isinstance(payload.get("runs"), list):
        payload["runs"] = []
    return payload


def save_runner_state(path: Path, payload: Dict[str, Any]) -> None:
    payload["runs"] = payload.get("runs", [])[-25:]
    write_json(path, payload)


def item_is_supported(item: Dict[str, Any]) -> Tuple[bool, List[str]]:
    stack = item.get("stack", [])
    unsupported = [component_id for component_id in stack if component_id not in SUPPORTED_COMPONENTS]
    return not unsupported, unsupported


def queue_completed_ids(queue: Dict[str, Any]) -> set[str]:
    return {item["id"] for item in queue.get("items", []) if item.get("status") == "done"}


def queue_runnable_items(queue: Dict[str, Any], completed_ids: set[str]) -> List[Dict[str, Any]]:
    runnable: List[Dict[str, Any]] = []
    for item in queue.get("items", []):
        if item["id"] in completed_ids:
            continue
        missing_blocker = any("missing" in blocker.lower() for blocker in item.get("blocked_by", []))
        if missing_blocker:
            continue
        if all(dep in completed_ids for dep in item.get("depends_on", [])):
            runnable.append(item)
    return runnable


def queue_backfill_items(workspace: Path, queue: Dict[str, Any]) -> List[Dict[str, Any]]:
    backfill: List[Dict[str, Any]] = []
    for item in queue.get("items", []):
        if item.get("status") != "done":
            continue
        supported, _ = item_is_supported(item)
        if supported and not artifact_exists(workspace, item):
            backfill.append(item)
    return backfill


def file_label(path_value: str) -> str:
    name = Path(path_value).stem.replace("-", " ").replace("_", " ").strip()
    return name.title() or path_value


def classify_signal(*values: str) -> str:
    blob = " ".join(values).lower()
    if any(token in blob for token in ("ai", "gemini", "chatgpt", "dejan", "grounding", "overview")):
        return "ai-search"
    if any(token in blob for token in ("schema", "crawl", "index", "robot", "sitemap", "cwv", "fetch error")):
        return "technical"
    return "content"


def build_fresh_signal_shortlist(status_payload: Dict[str, Any], digest: Dict[str, Any]) -> List[Dict[str, Any]]:
    shortlist: List[Dict[str, Any]] = []
    for item in status_payload.get("recent_knowledge", {}).get("live_articles", [])[:5]:
        path_value = item.get("path", "")
        shortlist.append(
            {
                "kind": "live_article",
                "title": file_label(path_value),
                "path": path_value,
                "updated_at": item.get("updated"),
                "category": classify_signal(path_value),
                "why_now": "Fresh local article note landed in the current cycle.",
            }
        )
    for item in status_payload.get("recent_knowledge", {}).get("primary_notes", [])[:3]:
        path_value = item.get("path", "")
        shortlist.append(
            {
                "kind": "primary_note",
                "title": file_label(path_value),
                "path": path_value,
                "updated_at": item.get("updated"),
                "category": classify_signal(path_value),
                "why_now": "Primary-source note is available to anchor same-day judgments.",
            }
        )
    for item in digest.get("opportunities", [])[:3]:
        shortlist.append(
            {
                "kind": "opportunity",
                "title": item.get("title", "Opportunity"),
                "path": ", ".join(item.get("files", [])[:2]) or "automation/digest/latest.md",
                "updated_at": digest.get("generated_at"),
                "category": classify_signal(item.get("title", ""), item.get("why_now", ""), item.get("action", "")),
                "why_now": item.get("why_now", ""),
            }
        )
    for item in digest.get("alerts", [])[:2]:
        shortlist.append(
            {
                "kind": "alert",
                "title": item.get("title", "Alert"),
                "path": ", ".join(item.get("files", [])[:2]) or "automation/digest/latest.md",
                "updated_at": digest.get("generated_at"),
                "category": classify_signal(item.get("title", ""), item.get("details", ""), item.get("action", "")),
                "why_now": item.get("action", ""),
            }
        )
    return shortlist[:8]


def render_shortlist_markdown(generated_at: str, shortlist: List[Dict[str, Any]]) -> str:
    lines = [
        "# Fresh Signal Shortlist",
        "",
        f"Generated by action runner at {generated_at}.",
        "",
        "## Signals",
    ]
    if shortlist:
        for entry in shortlist:
            lines.extend(
                [
                    f"- [{entry['category']}] {entry['title']}",
                    f"  - path: {entry['path']}",
                    f"  - updated: {entry['updated_at'] or 'unknown'}",
                    f"  - why now: {entry['why_now']}",
                ]
            )
    else:
        lines.append("- No same-day signals were available in the current status payload.")
    lines.extend(
        [
            "",
            "## Files Used",
            "- automation/data/latest-status.json",
            "- automation/digest/latest.json",
            "",
        ]
    )
    return "\n".join(lines)


def search_supporting_canon(memory_root: Path, shortlist: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not memory_root.exists():
        return []
    tokens: List[str] = []
    for entry in shortlist:
        tokens.extend(normalize_tokens(entry.get("title", ""), entry.get("path", ""), entry.get("category", "")))
    if not tokens:
        return []

    candidates: List[Tuple[int, Path]] = []
    for path in memory_root.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")[:1200].lower()
        name = path.name.lower()
        score = 0
        for token in tokens:
            if token in name:
                score += 5
            elif token in text:
                score += 1
        if score > 0:
            candidates.append((score, path))
    candidates.sort(key=lambda item: (-item[0], item[1].name))

    results: List[Dict[str, Any]] = []
    for score, path in candidates[:6]:
        results.append(
            {
                "score": score,
                "path": str(path),
                "label": path.stem.replace("-", " "),
            }
        )
    return results


def render_canon_markdown(generated_at: str, matches: List[Dict[str, Any]]) -> str:
    lines = [
        "# Supporting Canon",
        "",
        f"Generated by action runner at {generated_at}.",
        "",
        "## Matches",
    ]
    if matches:
        for match in matches:
            lines.append(f"- {match['label']} | score=`{match['score']}` | path: `{match['path']}`")
    else:
        lines.append("- No local canon matches were found for the current shortlist.")
    lines.extend(["", "## Files Used", "- ../../memory/imports/codex/skill-packs/seo/memory/*.md", ""])
    return "\n".join(lines)


def build_same_day_actions(shortlist: List[Dict[str, Any]], canon_matches: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {"ai-search": [], "content": [], "technical": []}
    for entry in shortlist:
        grouped.setdefault(entry["category"], []).append(entry)

    actions: List[Dict[str, Any]] = []
    if grouped.get("ai-search"):
        actions.append(
            {
                "title": "Turn the freshest AI-search notes into one operating update",
                "why_now": f"{len(grouped['ai-search'])} AI-search signal(s) landed in the current cycle.",
            }
        )
    if grouped.get("technical"):
        actions.append(
            {
                "title": "Translate fresh technical warnings into one fix shortlist",
                "why_now": f"{len(grouped['technical'])} technical signal(s) need same-day triage.",
            }
        )
    if grouped.get("content"):
        actions.append(
            {
                "title": "Convert content and opportunity notes into one same-day brief",
                "why_now": f"{len(grouped['content'])} content-oriented signal(s) are ready for exploitation.",
            }
        )
    if canon_matches:
        actions.append(
            {
                "title": "Anchor the brief to local canon before publishing",
                "why_now": f"{min(len(canon_matches), 3)} canon note(s) already match the fresh signal set.",
            }
        )
    return actions[:3]


def render_same_day_brief_markdown(generated_at: str, actions: List[Dict[str, Any]], canon_matches: List[Dict[str, Any]]) -> str:
    lines = [
        "# Same-Day Brief",
        "",
        f"Generated by action runner at {generated_at}.",
        "",
        "## Top Actions",
    ]
    if actions:
        for index, action in enumerate(actions, start=1):
            lines.append(f"{index}. {action['title']} | why now: {action['why_now']}")
    else:
        lines.append("1. No same-day action was derived from the current local evidence.")
    lines.extend(["", "## Canon Support"])
    if canon_matches:
        for match in canon_matches[:3]:
            lines.append(f"- {match['label']} -> `{match['path']}`")
    else:
        lines.append("- No canon matches were attached in this cycle.")
    lines.append("")
    return "\n".join(lines)


def render_published_freshness_output(
    generated_at: str,
    actions: List[Dict[str, Any]],
    shortlist: List[Dict[str, Any]],
    canon_matches: List[Dict[str, Any]],
) -> str:
    lines = [
        "# Freshness Radar",
        "",
        f"Generated by action runner at {generated_at}.",
        "",
        "## Highest-Priority Move",
    ]
    if actions:
        lines.append(f"- {actions[0]['title']} | {actions[0]['why_now']}")
    else:
        lines.append("- No same-day move was derived from the current evidence.")
    lines.extend(["", "## Evidence"])
    for entry in shortlist[:4]:
        lines.append(f"- [{entry['category']}] {entry['title']} | {entry['why_now']}")
    lines.extend(["", "## Canon Support"])
    if canon_matches:
        for match in canon_matches[:3]:
            lines.append(f"- {match['label']} | `{match['path']}`")
    else:
        lines.append("- No canon support attached.")
    lines.extend(["", "## Next Actions"])
    for action in actions[:3]:
        lines.append(f"- {action['title']}")
    lines.append("")
    return "\n".join(lines)


def read_task_payload(workspace: Path, queue: Dict[str, Any], task_suffix: str) -> Dict[str, Any]:
    for item in queue.get("items", []):
        if item["id"].endswith(task_suffix):
            json_path = workspace / item["artifact_json_path"]
            return load_json(json_path)
    return {}


def execute_freshness_task(
    workspace: Path,
    queue: Dict[str, Any],
    item: Dict[str, Any],
    generated_at: str,
) -> Tuple[Dict[str, Any], str]:
    status_payload = load_json(workspace / "automation" / "data" / "latest-status.json")
    digest = load_json(workspace / "automation" / "digest" / "latest.json")
    task_suffix = item["id"].split(".", 1)[-1]

    if task_suffix == "collect-fresh-signals":
        shortlist = build_fresh_signal_shortlist(status_payload, digest)
        payload = {
            "task_id": item["id"],
            "generated_at": generated_at,
            "shortlist": shortlist,
            "counts": {
                "total": len(shortlist),
                "categories": {
                    "ai-search": sum(1 for entry in shortlist if entry["category"] == "ai-search"),
                    "technical": sum(1 for entry in shortlist if entry["category"] == "technical"),
                    "content": sum(1 for entry in shortlist if entry["category"] == "content"),
                },
            },
        }
        return payload, render_shortlist_markdown(generated_at, shortlist)

    if task_suffix == "retrieve-supporting-canon":
        shortlist_payload = read_task_payload(workspace, queue, "collect-fresh-signals")
        shortlist = shortlist_payload.get("shortlist", [])
        matches = search_supporting_canon(relative_memory_root(workspace), shortlist)
        payload = {
            "task_id": item["id"],
            "generated_at": generated_at,
            "matches": matches,
            "source_task": "collect-fresh-signals",
        }
        return payload, render_canon_markdown(generated_at, matches)

    if task_suffix == "draft-same-day-brief":
        shortlist_payload = read_task_payload(workspace, queue, "collect-fresh-signals")
        canon_payload = read_task_payload(workspace, queue, "retrieve-supporting-canon")
        shortlist = shortlist_payload.get("shortlist", [])
        matches = canon_payload.get("matches", [])
        actions = build_same_day_actions(shortlist, matches)
        payload = {
            "task_id": item["id"],
            "generated_at": generated_at,
            "actions": actions,
            "source_tasks": ["collect-fresh-signals", "retrieve-supporting-canon"],
        }
        return payload, render_same_day_brief_markdown(generated_at, actions, matches)

    if task_suffix == "publish-priority-output":
        shortlist_payload = read_task_payload(workspace, queue, "collect-fresh-signals")
        canon_payload = read_task_payload(workspace, queue, "retrieve-supporting-canon")
        brief_payload = read_task_payload(workspace, queue, "draft-same-day-brief")
        shortlist = shortlist_payload.get("shortlist", [])
        matches = canon_payload.get("matches", [])
        actions = brief_payload.get("actions", [])
        outbox_path = workspace / queue["mission"]["outbox_path"]
        outbox_text = render_published_freshness_output(generated_at, actions, shortlist, matches)
        write_text(outbox_path, outbox_text)
        payload = {
            "task_id": item["id"],
            "generated_at": generated_at,
            "published_path": str(outbox_path),
            "actions": actions,
        }
        return payload, outbox_text

    raise ValueError(f"Unsupported freshness task: {task_suffix}")


def execute_task(workspace: Path, queue: Dict[str, Any], item: Dict[str, Any]) -> Dict[str, Any]:
    generated_at = now_utc_iso()
    mission_id = queue["mission"]["id"]
    if mission_id != "freshness-radar":
        return {
            "status": "unsupported",
            "generated_at": generated_at,
            "task_id": item["id"],
            "reason": f"No deterministic task handler is installed yet for mission `{mission_id}`.",
        }

    payload, markdown = execute_freshness_task(workspace, queue, item, generated_at)
    markdown_path, json_path = artifact_paths(workspace, item)
    write_text(markdown_path, markdown)
    write_json(json_path, payload)
    return {
        "status": "ok",
        "generated_at": generated_at,
        "task_id": item["id"],
        "task_title": item["title"],
        "artifact_markdown_path": str(markdown_path),
        "artifact_json_path": str(json_path),
    }


def run_openclaw_seo_action_runner(workspace: Path, max_tasks: int = 1) -> Dict[str, Any]:
    queue_path, state_path = current_queue_paths(workspace)
    queue = load_json(queue_path)
    if not queue:
        return {
            "status": "blocked",
            "generated_at": now_utc_iso(),
            "reason": f"Missing current queue: {queue_path}",
            "state_path": str(state_path),
        }

    state = load_runner_state(state_path)
    completed_ids = queue_completed_ids(queue)
    executed: List[Dict[str, Any]] = []
    blocked_reason = None

    while len(executed) < max_tasks:
        backfill = queue_backfill_items(workspace, queue)
        if backfill:
            item = backfill[0]
            result = execute_task(workspace, queue, item)
            executed.append(result)
            if result["status"] != "ok":
                blocked_reason = result.get("reason", "Action runner could not backfill the completed task artifact.")
                break
            continue
        runnable = queue_runnable_items(queue, completed_ids)
        if not runnable:
            break
        item = runnable[0]
        supported, unsupported_components = item_is_supported(item)
        if not supported:
            blocked_reason = (
                f"Current runnable task `{item['title']}` still depends on unsupported connector(s): "
                + ", ".join(unsupported_components)
            )
            break
        result = execute_task(workspace, queue, item)
        executed.append(result)
        if result["status"] != "ok":
            blocked_reason = result.get("reason", "Action runner could not execute the task.")
            break
        completed_ids.add(item["id"])

    status = "ok" if executed else ("blocked" if blocked_reason else "idle")
    payload = {
        "status": status,
        "generated_at": now_utc_iso(),
        "workspace": str(workspace),
        "mission_id": queue.get("mission", {}).get("id"),
        "queue_path": str(queue_path),
        "state_path": str(state_path),
        "executed_count": len(executed),
        "executed_tasks": executed,
        "blocked_reason": blocked_reason,
        "supported_components": sorted(SUPPORTED_COMPONENTS),
    }

    state["current"] = payload
    state.setdefault("runs", []).append(payload)
    save_runner_state(state_path, state)
    return payload


def main() -> int:
    args = parse_args()
    result = run_openclaw_seo_action_runner(workspace=Path(args.workspace), max_tasks=max(1, args.max_tasks))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(
            f"OpenClaw SEO action runner | status={result['status']} "
            f"executed={result['executed_count']} mission={result.get('mission_id')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
