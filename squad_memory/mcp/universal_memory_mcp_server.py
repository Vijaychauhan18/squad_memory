#!/usr/bin/env python3
"""Universal MCP server for Squad Memory OS across Codex and Claude clients."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import dataset_registry  # noqa: E402
import live_patent_seo_audit  # noqa: E402
import squad_memory  # noqa: E402


SERVER_NAME = "squad-memory-os"
SERVER_TITLE = "Squad Memory OS MCP"
SERVER_VERSION = "0.2.0"
PRD_PATH = REPO_ROOT / "squad-memory-os-development-prd-2026-04-24.md"
LATEST_PROTOCOL_VERSION = "2025-06-18"
SUPPORTED_PROTOCOL_VERSIONS = {
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
}
QUERYABLE_ADAPTER = "squad_memory_rank"

DATASET_HINTS: Dict[str, set[str]] = {
    "seo_elite": {
        "seo",
        "search",
        "google",
        "serp",
        "patent",
        "crawl",
        "crawling",
        "index",
        "indexing",
        "ranking",
        "snippet",
        "snippets",
        "entity",
        "entities",
        "query",
        "queries",
        "ai",
        "overview",
        "mode",
        "citation",
        "citations",
        "schema",
        "eeat",
    },
    "squad_memory": {
        "pack",
        "packs",
        "workflow",
        "workflows",
        "task",
        "tasks",
        "agent",
        "agents",
        "coordination",
        "orchestrator",
        "pinchy",
        "developer",
        "qa",
        "writer",
        "marketing",
        "charles",
        "support",
        "run",
        "handoff",
        "report",
        "evaluation",
        "feedback",
        "router",
        "control",
        "plane",
    },
    "portable_snapshot": {
        "portable",
        "snapshot",
        "dejan",
        "gemini",
        "grounding",
        "grounded",
        "selection",
        "reverse",
        "engineering",
        "citation",
        "citations",
        "visibility",
        "ai",
        "mode",
        "overview",
        "overviews",
    },
}

DATASET_BASE_PRIORS = {
    "seo_elite": 0.9,
    "squad_memory": 0.75,
    "portable_snapshot": 0.7,
}

ROLE_DATASET_BONUSES = {
    "seo": {"seo_elite": 0.25, "portable_snapshot": 0.12},
    "coral": {"seo_elite": 0.25, "portable_snapshot": 0.12},
    "pinchy": {"squad_memory": 0.22, "seo_elite": 0.08},
    "orchestrator-pinchy": {"squad_memory": 0.24, "seo_elite": 0.08},
    "kelp": {"portable_snapshot": 0.16, "seo_elite": 0.1},
    "researcher": {"portable_snapshot": 0.16, "seo_elite": 0.1},
    "developer": {"squad_memory": 0.18},
    "qa": {"squad_memory": 0.18},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Universal MCP server for Squad Memory OS")
    parser.add_argument("--skills-root", default=str(Path.home() / ".codex" / "skills"))
    parser.add_argument("--task-packs", default=str(REPO_ROOT / "task_packs.json"))
    return parser.parse_args()


def read_message() -> Optional[Dict[str, Any]]:
    headers: Dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        decoded = line.decode("utf-8").strip()
        if not decoded:
            continue
        key, value = decoded.split(":", 1)
        headers[key.strip().lower()] = value.strip()

    length_value = headers.get("content-length")
    if not length_value:
        raise ValueError("Missing Content-Length header")
    payload = sys.stdin.buffer.read(int(length_value))
    if not payload:
        return None
    return json.loads(payload.decode("utf-8"))


def write_message(message: Dict[str, Any]) -> None:
    raw = json.dumps(message, ensure_ascii=True).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(raw)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(raw)
    sys.stdout.buffer.flush()


def clamp_top(value: Any, default: int = 5, max_value: int = 20) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return max(1, min(parsed, max_value))


def slug_label(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").strip()


def make_text_result(text: str, structured: Dict[str, Any], is_error: bool = False) -> Dict[str, Any]:
    return {
        "content": [{"type": "text", "text": text}],
        "structuredContent": structured,
        "isError": is_error,
    }


def success_response(message_id: Any, result: Dict[str, Any]) -> Dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def error_response(message_id: Any, code: int, message: str) -> Dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "error": {"code": code, "message": message}}


def format_delta(value: Any) -> str:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return "n/a"
    if number > 0:
        return f"+{number}"
    return str(number)


def read_json_file(path: Path) -> Dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def normalize_dataset_hint(dataset_id: str, query: str, role: Optional[str]) -> Dict[str, Any]:
    tokens = set(squad_memory.tokenize(query))
    query_lower = query.lower()
    explicit_matches: List[str] = []
    hint_hits = sorted(tokens & DATASET_HINTS.get(dataset_id, set()))
    score = DATASET_BASE_PRIORS.get(dataset_id, 0.55)
    reasons = [f"base-priority={score:.2f}"]

    if hint_hits:
        score += min(len(hint_hits) * 0.18, 0.72)
        reasons.append(f"keyword-hits={', '.join(hint_hits[:6])}")

    if dataset_id in query_lower:
        score += 0.75
        explicit_matches.append(dataset_id)
    if slug_label(dataset_id) in query_lower:
        score += 0.55
        explicit_matches.append(slug_label(dataset_id))
    if explicit_matches:
        reasons.append(f"explicit-match={', '.join(explicit_matches)}")

    role_key = (role or "").lower()
    role_bonus = ROLE_DATASET_BONUSES.get(role_key, {}).get(dataset_id, 0.0)
    if role_bonus:
        score += role_bonus
        reasons.append(f"role-bonus={role_bonus:.2f}")

    return {
        "dataset_id": dataset_id,
        "selection_score": round(score, 4),
        "selection_reasons": reasons,
    }


def tool_definitions() -> List[Dict[str, Any]]:
    return [
        {
            "name": "memory_registry_overview",
            "title": "Memory Registry Overview",
            "description": "List all registered memory datasets, their chunk counts, query capability, and linked surfaces.",
            "inputSchema": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_dataset_inspect",
            "title": "Memory Dataset Inspect",
            "description": "Inspect one registered dataset by id, including counts, relationships, and query capability.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "dataset_id": {
                        "type": "string",
                        "description": "Registered dataset id such as seo_elite, squad_memory, portable_snapshot, openclaw_main, or openclaw_seo.",
                    }
                },
                "required": ["dataset_id"],
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_dataset_history",
            "title": "Memory Dataset History",
            "description": "Read recent temporal history for a dataset, including chunk and path deltas across snapshots when available.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "dataset_id": {
                        "type": "string",
                        "description": "Registered dataset id such as seo_elite, squad_memory, portable_snapshot, openclaw_main, or openclaw_seo.",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of recent history entries to return.",
                        "default": 8,
                        "minimum": 1,
                        "maximum": 30,
                    },
                },
                "required": ["dataset_id"],
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_dataset_delta",
            "title": "Memory Dataset Delta",
            "description": "Explain the latest count delta for a dataset relative to its most recent usable history baseline.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "dataset_id": {
                        "type": "string",
                        "description": "Registered dataset id such as seo_elite, squad_memory, portable_snapshot, openclaw_main, or openclaw_seo.",
                    }
                },
                "required": ["dataset_id"],
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_run_ledger",
            "title": "Memory Run Ledger",
            "description": "Inspect the current local run ledger for SEO Elite and linked memory pipelines, including active jobs and recent fetch state.",
            "inputSchema": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
        {
            "name": "seo_patent_live_audit",
            "title": "SEO Patent Live Audit",
            "description": "Run a live website audit over a small smart page set, then map the findings to Google-patent-style SEO lenses.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "Website or page URL to audit.",
                    },
                    "audit_types": {
                        "type": "array",
                        "description": "Optional audit types such as eeat_trust, entity_clarity, topical_authority, information_gain, ai_search_readiness, or landing_page_quality.",
                        "items": {"type": "string"},
                    },
                    "max_pages": {
                        "type": "integer",
                        "description": "Maximum number of pages to inspect in the live audit.",
                        "default": 7,
                        "minimum": 3,
                        "maximum": 12,
                    },
                    "timeout": {
                        "type": "integer",
                        "description": "Fetch timeout in seconds for each page request.",
                        "default": 20,
                        "minimum": 5,
                        "maximum": 60,
                    },
                },
                "required": ["url"],
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_federated_query",
            "title": "Memory Federated Query",
            "description": "Search across the best-fit memory datasets automatically or use explicit dataset ids for federated retrieval.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query to run across the memory datasets."},
                    "role": {"type": "string", "description": "Optional role hint such as coral, pinchy, kelp, or developer."},
                    "skill": {"type": "string", "description": "Optional skill filter for queryable squad-memory style datasets."},
                    "top": {"type": "integer", "description": "Maximum number of overall hits to return.", "default": 8, "minimum": 1, "maximum": 20},
                    "datasets": {
                        "type": "array",
                        "description": "Optional explicit dataset ids to search. If omitted, the server auto-selects the best datasets.",
                        "items": {"type": "string"},
                    },
                },
                "required": ["query"],
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_route_task",
            "title": "Memory Route Task",
            "description": "Choose the best dataset for a task, then recommend the right skills and supporting memory.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "task": {"type": "string", "description": "The task or request to route."},
                    "role": {"type": "string", "description": "Optional role hint such as coral, pinchy, kelp, or developer."},
                    "top": {"type": "integer", "description": "Maximum number of skills to rank.", "default": 5, "minimum": 1, "maximum": 20},
                    "datasets": {
                        "type": "array",
                        "description": "Optional explicit dataset ids to consider for routing.",
                        "items": {"type": "string"},
                    },
                },
                "required": ["task"],
                "additionalProperties": False,
            },
        },
        {
            "name": "memory_execution_plan",
            "title": "Memory Execution Plan",
            "description": "Choose the best memory dataset and build an execution plan from the selected task pack.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "task": {"type": "string", "description": "The task or request to convert into an execution plan."},
                    "role": {"type": "string", "description": "Optional role hint such as coral, pinchy, kelp, or developer."},
                    "top": {"type": "integer", "description": "Maximum number of candidate packs to consider.", "default": 5, "minimum": 1, "maximum": 20},
                    "pack_id": {"type": "string", "description": "Optional explicit pack override."},
                    "datasets": {
                        "type": "array",
                        "description": "Optional explicit dataset ids to consider for routing.",
                        "items": {"type": "string"},
                    },
                },
                "required": ["task"],
                "additionalProperties": False,
            },
        },
    ]


def prompt_definitions() -> List[Dict[str, Any]]:
    return [
        {
            "name": "dataset_audit",
            "title": "Dataset Audit",
            "description": "Create an audit workflow for a specific memory dataset and explain what to inspect.",
            "arguments": [
                {"name": "dataset_id", "description": "Registered dataset id to audit.", "required": True},
                {"name": "goal", "description": "Optional audit goal such as trust, freshness, SEO patents, or routing quality.", "required": False},
            ],
        },
        {
            "name": "federated_analysis",
            "title": "Federated Analysis",
            "description": "Create a prompt for a cross-dataset research pass using federated memory retrieval.",
            "arguments": [
                {"name": "question", "description": "The research question or problem to analyze.", "required": True},
                {"name": "role", "description": "Optional role hint such as coral, pinchy, kelp, or developer.", "required": False},
            ],
        },
        {
            "name": "delta_explainer",
            "title": "Delta Explainer",
            "description": "Create a workflow prompt to explain a dataset count delta using local history, registry metadata, and run state.",
            "arguments": [
                {"name": "dataset_id", "description": "Registered dataset id to inspect.", "required": True},
                {"name": "question", "description": "Optional framing question such as why did chunks drop or what caused the spike.", "required": False},
            ],
        },
        {
            "name": "run_triage",
            "title": "Run Triage",
            "description": "Create a local run-triage workflow prompt for active jobs, stalled pipelines, and next operator actions.",
            "arguments": [
                {"name": "focus", "description": "Optional focus such as freshness, failed fetches, pending queue, or bridge sync.", "required": False},
            ],
        },
        {
            "name": "live_patent_site_audit",
            "title": "Live Patent Site Audit",
            "description": "Create a workflow prompt for a live website audit backed by patent memory and observable page evidence.",
            "arguments": [
                {"name": "url", "description": "Website or page URL to audit.", "required": True},
                {"name": "focus", "description": "Optional focus such as eeat, entity clarity, ai search readiness, or landing page quality.", "required": False},
            ],
        },
        {
            "name": "system_improvement_brief",
            "title": "System Improvement Brief",
            "description": "Create a structured product/engineering brief for improving Squad Memory OS locally.",
            "arguments": [
                {"name": "problem", "description": "The user-visible problem or product gap to improve.", "required": True},
                {"name": "focus", "description": "Optional focus area such as UX, retrieval, trust, speed, or installation.", "required": False},
            ],
        },
    ]


def build_registry_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# Squad Memory OS Registry",
        "",
        f"Updated: {payload.get('updated_at_iso', '')}",
        "",
    ]
    for item in payload.get("items", []):
        lines.extend(
            [
                f"## {item['label']} [{item['id']}]",
                f"- Status: {item.get('status', 'unknown')}",
                f"- Path: `{item.get('path', '')}`",
                f"- Query adapter: `{item.get('query_adapter', 'counts_only')}`",
                f"- Chunks: `{item.get('chunks', 'n/a')}`",
                f"- Paths: `{item.get('paths', 'n/a')}`",
                f"- Purpose: {item.get('purpose', '')}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def build_dataset_markdown(item: Dict[str, Any]) -> str:
    lines = [
        f"# Dataset: {item['label']}",
        "",
        f"- Dataset id: `{item['id']}`",
        f"- Status: `{item.get('status', 'unknown')}`",
        f"- Path: `{item.get('path', '')}`",
        f"- Query adapter: `{item.get('query_adapter', 'counts_only')}`",
        f"- Chunks: `{item.get('chunks', 'n/a')}`",
        f"- Paths: `{item.get('paths', 'n/a')}`",
        f"- Updated at: `{item.get('updated_at', '')}`",
        f"- Expected count band: `{item.get('expected_count_band', '')}`",
        f"- History available: `{item.get('history_available', False)}`",
        f"- History path: `{item.get('history_path', '')}`",
        "",
        "## Purpose",
        "",
        item.get("purpose", ""),
        "",
    ]
    related = item.get("related_datasets", [])
    if related:
        lines.extend(["## Related Datasets", ""])
        for rel in related:
            lines.append(f"- `{rel['type']}` -> {rel['label']} [`{rel['id']}`] with `{rel.get('chunks', 'n/a')}` chunks")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def build_dataset_history_markdown(payload: Dict[str, Any]) -> str:
    dataset = payload["dataset"]
    lines = [
        f"# Dataset History: {dataset['label']}",
        "",
        f"- Dataset id: `{dataset['id']}`",
        f"- History available: `{payload.get('history_available', False)}`",
        f"- History path: `{payload.get('history_path', '')}`",
        f"- History entries returned: `{payload.get('history_entry_count', 0)}`",
        "",
    ]
    history = payload.get("history", [])
    if not history:
        lines.extend(["No history entries are available for this dataset yet.", ""])
        return "\n".join(lines).strip() + "\n"
    lines.extend(["## Recent History", ""])
    for item in history:
        lines.append(
            f"- `{item.get('updated_at_iso') or item.get('updated_at', 'unknown')}` :: "
            f"chunks `{item.get('chunks', 'n/a')}` ({format_delta(item.get('delta_chunks_from_previous'))}) :: "
            f"paths `{item.get('paths', 'n/a')}` ({format_delta(item.get('delta_paths_from_previous'))}) :: "
            f"phase `{item.get('current_phase', 'unknown')}`"
        )
    lines.append("")
    return "\n".join(lines).strip() + "\n"


def build_dataset_delta_markdown(payload: Dict[str, Any]) -> str:
    dataset = payload["dataset"]
    baseline = payload.get("baseline_entry")
    current = payload.get("current", {})
    delta = payload.get("delta", {})
    lines = [
        f"# Dataset Delta: {dataset['label']}",
        "",
        f"- Dataset id: `{dataset['id']}`",
        f"- Delta status: `{payload.get('status', 'unknown')}`",
        f"- Baseline source: `{payload.get('baseline_source', 'none')}`",
        f"- Current matches latest history: `{payload.get('current_matches_latest_history', False)}`",
        f"- Current chunks: `{current.get('chunks', 'n/a')}`",
        f"- Current paths: `{current.get('paths', 'n/a')}`",
        f"- Delta chunks: `{format_delta(delta.get('chunks'))}`",
        f"- Delta paths: `{format_delta(delta.get('paths'))}`",
        "",
    ]
    if baseline:
        lines.extend(
            [
                "## Baseline",
                "",
                f"- Updated at: `{baseline.get('updated_at_iso') or baseline.get('updated_at', 'unknown')}`",
                f"- Chunks: `{baseline.get('chunks', 'n/a')}`",
                f"- Paths: `{baseline.get('paths', 'n/a')}`",
                f"- Phase: `{baseline.get('current_phase', 'unknown')}`",
                "",
            ]
        )
    else:
        lines.extend(["No usable history baseline is available for this dataset yet.", ""])
    return "\n".join(lines).strip() + "\n"


def build_run_ledger_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# Squad Memory OS Run Ledger",
        "",
        f"- Updated at: `{payload.get('updated_at', '')}`",
        f"- Status source: `{payload.get('status_source', '')}`",
        f"- Status path: `{payload.get('status_path', '')}`",
        f"- Current phase: `{payload.get('current_phase', 'unknown')}`",
        f"- Active jobs: `{payload.get('active_job_count', 0)}`",
        f"- Pending total: `{payload.get('pending_total', 0)}`",
        f"- Recent fetch total/ok/error: `{payload.get('recent_fetch_total', 0)}` / `{payload.get('recent_fetch_ok', 0)}` / `{payload.get('recent_fetch_error', 0)}`",
        "",
        "## Active Jobs",
        "",
    ]
    active_jobs = payload.get("active_jobs", [])
    if active_jobs:
        for item in active_jobs:
            lines.append(f"- `{item.get('job', 'unknown')}` updated `{item.get('updated_at', 'unknown')}` age `{item.get('age_seconds', 'n/a')}`s")
    else:
        lines.append("- No active jobs detected")
    lines.append("")
    if payload.get("seo_elite_delta"):
        delta = payload["seo_elite_delta"].get("delta", {})
        lines.extend(
            [
                "## SEO Elite Delta",
                "",
                f"- Chunks: `{format_delta(delta.get('chunks'))}`",
                f"- Paths: `{format_delta(delta.get('paths'))}`",
                "",
            ]
        )
    lines.extend(
        [
            "## OpenClaw",
            "",
            f"- Main chunks: `{payload.get('openclaw', {}).get('main', {}).get('chunks', 'n/a')}`",
            f"- SEO chunks: `{payload.get('openclaw', {}).get('seo', {}).get('chunks', 'n/a')}`",
            f"- Enabled jobs: `{payload.get('openclaw', {}).get('jobs', {}).get('enabled_jobs', 'n/a')}`",
            f"- SEO jobs: `{payload.get('openclaw', {}).get('jobs', {}).get('seo_jobs', 'n/a')}`",
            "",
        ]
    )
    ticker = payload.get("ticker", [])
    if ticker:
        lines.extend(["## Recent Ticker", ""])
        for line in ticker[:10]:
            lines.append(f"- {line}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def resource_definitions(registry_payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    resources = [
        {
            "uri": "memory://registry/overview",
            "name": "registry-overview",
            "title": "Squad Memory OS Registry Overview",
            "description": "Current local dataset registry including chunk counts, paths, and query adapters.",
            "mimeType": "text/markdown",
        },
        {
            "uri": "memory://prd/squad-memory-os",
            "name": "squad-memory-os-prd",
            "title": "Squad Memory OS Development PRD",
            "description": "Current engineering PRD for the local-first Squad Memory OS roadmap.",
            "mimeType": "text/markdown",
        },
        {
            "uri": "memory://runs/ledger",
            "name": "run-ledger",
            "title": "Squad Memory OS Run Ledger",
            "description": "Current local run ledger including active jobs, fetch state, and linked stack counts.",
            "mimeType": "text/markdown",
        },
    ]
    for item in registry_payload.get("items", []):
        resources.append(
            {
                "uri": f"memory://dataset/{item['id']}",
                "name": f"dataset-{item['id']}",
                "title": f"{item['label']} Dataset",
                "description": f"Local dataset summary for {item['label']}.",
                "mimeType": "text/markdown",
            }
        )
        resources.append(
            {
                "uri": f"memory://dataset/{item['id']}/history",
                "name": f"dataset-{item['id']}-history",
                "title": f"{item['label']} History",
                "description": f"Recent temporal history for {item['label']}.",
                "mimeType": "text/markdown",
            }
        )
        resources.append(
            {
                "uri": f"memory://dataset/{item['id']}/delta",
                "name": f"dataset-{item['id']}-delta",
                "title": f"{item['label']} Delta",
                "description": f"Latest explainable delta for {item['label']}.",
                "mimeType": "text/markdown",
            }
        )
    return resources


def resource_templates() -> List[Dict[str, Any]]:
    return [
        {
            "uriTemplate": "memory://dataset/{dataset_id}",
            "name": "dataset-template",
            "title": "Dataset Summary",
            "description": "Parameterized dataset summary resource by dataset id.",
            "mimeType": "text/markdown",
        },
        {
            "uriTemplate": "memory://dataset/{dataset_id}/history",
            "name": "dataset-history-template",
            "title": "Dataset History",
            "description": "Parameterized dataset history resource by dataset id.",
            "mimeType": "text/markdown",
        },
        {
            "uriTemplate": "memory://dataset/{dataset_id}/delta",
            "name": "dataset-delta-template",
            "title": "Dataset Delta",
            "description": "Parameterized dataset delta resource by dataset id.",
            "mimeType": "text/markdown",
        }
    ]


def summarize_registry(payload: Dict[str, Any]) -> str:
    lines = ["Registered datasets:"]
    for item in payload.get("items", []):
        lines.append(
            f"- {item['label']} [{item['id']}] :: {item['status']} :: "
            f"{item.get('chunks', 'n/a')} chunks :: adapter={item.get('query_adapter', 'counts_only')}"
        )
    return "\n".join(lines)


def summarize_dataset(payload: Dict[str, Any]) -> str:
    lines = [
        f"Dataset: {payload['label']} [{payload['id']}]",
        f"Path: {payload['path']}",
        f"Status: {payload['status']}",
        f"Query adapter: {payload.get('query_adapter', 'counts_only')}",
        f"Chunks: {payload.get('chunks', 'n/a')}",
        f"Paths: {payload.get('paths', 'n/a')}",
        f"History available: {payload.get('history_available', False)}",
    ]
    if payload.get("purpose"):
        lines.append(f"Purpose: {payload['purpose']}")
    if payload.get("related_datasets"):
        lines.append("Linked datasets:")
        for item in payload["related_datasets"][:4]:
            lines.append(f"- {item['type']}: {item['label']} [{item['id']}]")
    return "\n".join(lines)


def summarize_dataset_history(payload: Dict[str, Any]) -> str:
    dataset = payload["dataset"]
    lines = [
        f"Dataset history: {dataset['label']} [{dataset['id']}]",
        f"History available: {payload.get('history_available', False)}",
        f"Entries returned: {payload.get('history_entry_count', 0)}",
    ]
    history = payload.get("history", [])
    if not history:
        lines.append("No history entries are available.")
        return "\n".join(lines)
    lines.append("Recent entries:")
    for item in history[:6]:
        lines.append(
            f"- {item.get('updated_at_iso') or item.get('updated_at', 'unknown')} :: "
            f"chunks={item.get('chunks', 'n/a')} ({format_delta(item.get('delta_chunks_from_previous'))}) :: "
            f"paths={item.get('paths', 'n/a')} ({format_delta(item.get('delta_paths_from_previous'))})"
        )
    return "\n".join(lines)


def summarize_dataset_delta(payload: Dict[str, Any]) -> str:
    dataset = payload["dataset"]
    current = payload.get("current", {})
    delta = payload.get("delta", {})
    lines = [
        f"Dataset delta: {dataset['label']} [{dataset['id']}]",
        f"Status: {payload.get('status', 'unknown')}",
        f"Current chunks: {current.get('chunks', 'n/a')}",
        f"Current paths: {current.get('paths', 'n/a')}",
        f"Delta chunks: {format_delta(delta.get('chunks'))}",
        f"Delta paths: {format_delta(delta.get('paths'))}",
        f"Baseline source: {payload.get('baseline_source', 'none')}",
    ]
    baseline = payload.get("baseline_entry")
    if baseline:
        lines.append(f"Baseline updated at: {baseline.get('updated_at_iso') or baseline.get('updated_at', 'unknown')}")
        lines.append(f"Baseline phase: {baseline.get('current_phase', 'unknown')}")
    else:
        lines.append("No usable history baseline is available.")
    return "\n".join(lines)


def summarize_federated_query(payload: Dict[str, Any]) -> str:
    lines = [f"Query: {payload['query']}"]
    if payload.get("role"):
        lines.append(f"Role: {payload['role']}")
    lines.append("Selected datasets:")
    for item in payload.get("selected_datasets", []):
        lines.append(f"- {item['label']} [{item['id']}] score={item['selection_score']}")
    results = payload.get("results", [])
    if not results:
        lines.append("No matching memory hits found.")
        return "\n".join(lines)
    lines.append("Top federated hits:")
    for item in results[: min(len(results), 6)]:
        lines.append(
            f"- {item['dataset_label']} :: {item['path']} :: {item['heading']} "
            f"(federated={item['federated_score']}, raw={item['raw_score']})"
        )
    skipped = payload.get("skipped_datasets", [])
    if skipped:
        lines.append("Skipped datasets:")
        for item in skipped:
            lines.append(f"- {item['id']}: {item['reason']}")
    return "\n".join(lines)


def summarize_route(payload: Dict[str, Any]) -> str:
    selected = payload["selected_dataset"]
    lines = [
        f"Task: {payload['task']}",
        f"Selected dataset: {selected['label']} [{selected['id']}]",
    ]
    if payload.get("role"):
        lines.append(f"Role: {payload['role']}")
    if payload.get("recommended_skills"):
        lines.append("Recommended skills:")
        for item in payload["recommended_skills"][:4]:
            lines.append(f"- {item['skill']} [{item['score']}]")
    if payload.get("supporting_memory"):
        lines.append("Supporting memory:")
        for item in payload["supporting_memory"][:4]:
            lines.append(f"- {item['path']} :: {item['heading']}")
    return "\n".join(lines)


def summarize_execution_plan(payload: Dict[str, Any]) -> str:
    selected = payload["selected_dataset"]
    pack = payload["selected_pack"]
    lines = [
        f"Task: {payload['task']}",
        f"Selected dataset: {selected['label']} [{selected['id']}]",
        f"Selected pack: {pack['id']} ({pack['name']}) [{pack['score']}]",
        "Execution steps:",
    ]
    lines.extend(f"{idx}. {step}" for idx, step in enumerate(payload.get("execution_steps", [])[:6], start=1))
    return "\n".join(lines)


def summarize_run_ledger(payload: Dict[str, Any]) -> str:
    lines = [
        f"Run ledger updated: {payload.get('updated_at', '')}",
        f"Current phase: {payload.get('current_phase', 'unknown')}",
        f"Active jobs: {payload.get('active_job_count', 0)}",
        f"Pending total: {payload.get('pending_total', 0)}",
        (
            "Recent fetch total/ok/error: "
            f"{payload.get('recent_fetch_total', 0)} / "
            f"{payload.get('recent_fetch_ok', 0)} / "
            f"{payload.get('recent_fetch_error', 0)}"
        ),
    ]
    if payload.get("active_jobs"):
        lines.append("Active jobs:")
        for item in payload["active_jobs"][:6]:
            lines.append(f"- {item.get('job', 'unknown')} :: age={item.get('age_seconds', 'n/a')}s")
    if payload.get("seo_elite_delta"):
        delta = payload["seo_elite_delta"].get("delta", {})
        lines.append(
            f"SEO Elite delta: chunks={format_delta(delta.get('chunks'))}, "
            f"paths={format_delta(delta.get('paths'))}"
        )
    return "\n".join(lines)


def summarize_live_patent_audit(payload: Dict[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        f"Live patent audit: {summary.get('site_name', payload.get('scope', {}).get('site_root', 'unknown site'))}",
        f"Overall: {summary.get('overall_status', 'unknown')} [{summary.get('overall_score', 'n/a')}]",
        f"Pages fetched: {payload.get('page_selection', {}).get('fetched_ok', 0)} ok / {payload.get('page_selection', {}).get('fetched_error', 0)} error",
        summary.get("headline", ""),
        "Top findings:",
    ]
    findings = payload.get("top_findings", [])
    if not findings:
        lines.append("- No major findings in the audited sample.")
    else:
        for item in findings[:6]:
            lines.append(
                f"- [{item.get('severity', 'low')}] {item.get('audit_type', 'unknown')}: "
                f"{item.get('title', '')} :: patents={', '.join(item.get('patent_lenses', []))}"
            )
    actions = summary.get("priority_actions", [])
    if actions:
        lines.append("Priority actions:")
        for item in actions[:5]:
            lines.append(f"- {item}")
    return "\n".join(lines)


class SquadMemoryOsMcpServer:
    def __init__(self, skills_root: Path, task_packs_path: Path) -> None:
        self.skills_root = skills_root
        self.task_packs_path = task_packs_path
        squad_memory.SKILLS_ROOT = skills_root

    def initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        client_version = params.get("protocolVersion", LATEST_PROTOCOL_VERSION)
        protocol_version = client_version if client_version in SUPPORTED_PROTOCOL_VERSIONS else LATEST_PROTOCOL_VERSION
        return {
            "protocolVersion": protocol_version,
            "capabilities": {
                "tools": {"listChanged": False},
                "prompts": {"listChanged": False},
                "resources": {},
            },
            "serverInfo": {
                "name": SERVER_NAME,
                "title": SERVER_TITLE,
                "version": SERVER_VERSION,
                "description": "Universal MCP server for registry, federated retrieval, routing, and execution plans across Squad Memory OS.",
            },
            "instructions": (
                "Use registry tools to understand which dataset is active. Use dataset history and delta tools when you need explainability over time. "
                "Use the run ledger when you need local pipeline state. Use federated query when you need cross-corpus search, "
                "use the live patent audit when you need a real website inspected through patent-backed SEO lenses, "
                "route task when you need the best dataset plus skill recommendation, execution plan when you want a reusable operating plan, "
                "resources when you need inspectable local context, and prompts when you want repeatable local-first workflows."
            ),
        }

    def registry_payload(self) -> Dict[str, Any]:
        return dataset_registry.build_registry_payload()

    def queryable_datasets(self) -> List[Dict[str, Any]]:
        items = self.registry_payload().get("items", [])
        return [item for item in items if item.get("query_adapter") == QUERYABLE_ADAPTER and item.get("status") == "ready"]

    def dataset_lookup(self) -> Dict[str, Dict[str, Any]]:
        return {item["id"]: item for item in self.registry_payload().get("items", [])}

    def select_datasets(
        self,
        query: str,
        role: Optional[str],
        requested_ids: Optional[Iterable[str]],
    ) -> Dict[str, Any]:
        lookup = self.dataset_lookup()
        queryable_lookup = {item["id"]: item for item in self.queryable_datasets()}
        skipped: List[Dict[str, str]] = []

        if requested_ids:
            selected: List[Dict[str, Any]] = []
            for dataset_id in requested_ids:
                item = lookup.get(dataset_id)
                if not item:
                    skipped.append({"id": dataset_id, "reason": "unknown dataset id"})
                    continue
                if item.get("query_adapter") != QUERYABLE_ADAPTER:
                    skipped.append({"id": dataset_id, "reason": f"adapter {item.get('query_adapter', 'counts_only')} is not queryable in this phase"})
                    continue
                if item.get("status") != "ready":
                    skipped.append({"id": dataset_id, "reason": f"status is {item.get('status', 'unknown')}"})
                    continue
                hint = normalize_dataset_hint(dataset_id, query, role)
                selected.append({**item, **hint})
            return {"selected": selected, "skipped": skipped, "mode": "explicit"}

        scored = []
        for dataset_id, item in queryable_lookup.items():
            hint = normalize_dataset_hint(dataset_id, query, role)
            scored.append({**item, **hint})

        scored.sort(key=lambda item: item["selection_score"], reverse=True)
        if not scored:
            return {"selected": [], "skipped": skipped, "mode": "auto"}

        top_score = scored[0]["selection_score"]
        if top_score < 1.05:
            selected = scored[: min(2, len(scored))]
        else:
            threshold = max(top_score - 0.22, 0.98)
            selected = [item for item in scored if item["selection_score"] >= threshold][:2]
            if len(selected) < min(2, len(scored)):
                selected = scored[: min(2, len(scored))]

        return {"selected": selected, "skipped": skipped, "mode": "auto"}

    def federated_query(self, query: str, role: Optional[str], skill_filter: Optional[str], top: int, datasets: Optional[Iterable[str]]) -> Dict[str, Any]:
        selection = self.select_datasets(query, role, datasets)
        selected = selection["selected"]
        if not selected:
            raise ValueError("No queryable datasets available for federated query")

        all_results: List[Dict[str, Any]] = []
        per_dataset: List[Dict[str, Any]] = []
        for dataset in selected:
            db_path = Path(dataset["path"])
            results = squad_memory.rank_chunks(
                db_path,
                query,
                role=role,
                skill_filter=skill_filter,
                top=max(top * 2, 6),
                workspace_enabled=False,
            )
            dataset_top = max((float(item.get("score", 0.0)) for item in results), default=0.0)
            federated_items: List[Dict[str, Any]] = []
            for item in results:
                raw_score = float(item.get("score", 0.0))
                normalized_score = raw_score / dataset_top if dataset_top > 0 else 0.0
                federated_score = round(dataset["selection_score"] + normalized_score, 4)
                merged = dict(item)
                merged["dataset_id"] = dataset["id"]
                merged["dataset_label"] = dataset["label"]
                merged["raw_score"] = round(raw_score, 4)
                merged["normalized_score"] = round(normalized_score, 4)
                merged["federated_score"] = federated_score
                federated_items.append(merged)
            federated_items.sort(key=lambda item: item["federated_score"], reverse=True)
            all_results.extend(federated_items)
            per_dataset.append(
                {
                    "id": dataset["id"],
                    "label": dataset["label"],
                    "selection_score": dataset["selection_score"],
                    "selection_reasons": dataset["selection_reasons"],
                    "result_count": len(federated_items),
                    "top_results": federated_items[: min(4, len(federated_items))],
                }
            )

        all_results.sort(key=lambda item: item["federated_score"], reverse=True)
        return {
            "query": query,
            "role": role,
            "skill_filter": skill_filter,
            "selection_mode": selection["mode"],
            "selected_datasets": [
                {
                    "id": item["id"],
                    "label": item["label"],
                    "selection_score": item["selection_score"],
                    "selection_reasons": item["selection_reasons"],
                    "query_adapter": item["query_adapter"],
                }
                for item in selected
            ],
            "skipped_datasets": selection["skipped"],
            "per_dataset": per_dataset,
            "results": all_results[:top],
        }

    def route_task(self, task: str, role: Optional[str], top: int, datasets: Optional[Iterable[str]]) -> Dict[str, Any]:
        selection = self.select_datasets(task, role, datasets)
        selected = selection["selected"]
        if not selected:
            raise ValueError("No queryable datasets available for routing")

        evaluated = list(selected)
        if selection["mode"] == "auto" and len(evaluated) > 1:
            sorted_selected = sorted(evaluated, key=lambda item: item["selection_score"], reverse=True)
            if sorted_selected[0]["selection_score"] - sorted_selected[1]["selection_score"] >= 0.35:
                evaluated = sorted_selected[:1]

        candidates: List[Dict[str, Any]] = []
        for dataset in evaluated:
            decision = squad_memory.decide(
                Path(dataset["path"]),
                task,
                role=role,
                top=max(top, 4),
                workspace_enabled=False,
            )
            best_skill_score = float(decision.get("recommended_skills", [{}])[0].get("score", 0.0)) if decision.get("recommended_skills") else 0.0
            best_memory_score = float(decision.get("supporting_memory", [{}])[0].get("score", 0.0)) if decision.get("supporting_memory") else 0.0
            dataset_score = round(dataset["selection_score"] + best_skill_score + (best_memory_score * 0.35), 4)
            candidates.append(
                {
                    "dataset": {
                        "id": dataset["id"],
                        "label": dataset["label"],
                        "path": dataset["path"],
                        "selection_score": dataset["selection_score"],
                        "selection_reasons": dataset["selection_reasons"],
                    },
                    "dataset_score": dataset_score,
                    "decision": decision,
                }
            )

        candidates.sort(key=lambda item: item["dataset_score"], reverse=True)
        chosen = candidates[0]
        decision = chosen["decision"]
        return {
            "task": task,
            "role": role,
            "selection_mode": selection["mode"],
            "selected_dataset": chosen["dataset"],
            "selected_datasets": [
                {
                    "id": item["id"],
                    "label": item["label"],
                    "selection_score": item["selection_score"],
                }
                for item in selected
            ],
            "evaluated_dataset_ids": [item["dataset"]["id"] for item in candidates],
            "candidate_datasets": [
                {
                    "id": item["dataset"]["id"],
                    "label": item["dataset"]["label"],
                    "dataset_score": item["dataset_score"],
                    "top_skill": item["decision"].get("recommended_skills", [{}])[0].get("skill"),
                }
                for item in candidates
            ],
            "skipped_datasets": selection["skipped"],
            "inferred_intents": decision.get("inferred_intents", []),
            "expansion_terms": decision.get("expansion_terms", []),
            "recommended_skills": decision.get("recommended_skills", [])[:top],
            "supporting_memory": decision.get("supporting_memory", [])[: top * 2],
        }

    def execution_plan(self, task: str, role: Optional[str], top: int, pack_id: Optional[str], datasets: Optional[Iterable[str]]) -> Dict[str, Any]:
        routed = self.route_task(task, role, top, datasets)
        selected = routed["selected_dataset"]
        plan = squad_memory.build_execute_plan(
            Path(selected["path"]),
            self.task_packs_path,
            task,
            role,
            max(top, 4),
            pack_id=pack_id,
        )
        return {
            "task": task,
            "role": role,
            "selected_dataset": selected,
            "candidate_datasets": routed.get("candidate_datasets", []),
            "skipped_datasets": routed.get("skipped_datasets", []),
            **plan,
        }

    def dataset_history(self, dataset_id: str, limit: int) -> Dict[str, Any]:
        payload = dataset_registry.build_dataset_history(dataset_id, limit=limit)
        if payload is None:
            raise ValueError(f"Unknown dataset id: {dataset_id}")
        return payload

    def dataset_delta(self, dataset_id: str) -> Dict[str, Any]:
        payload = dataset_registry.build_dataset_delta(dataset_id)
        if payload is None:
            raise ValueError(f"Unknown dataset id: {dataset_id}")
        return payload

    def load_seo_elite_status(self) -> Dict[str, Any]:
        entry = dataset_registry.get_dataset_entry("seo_elite")
        status_path = dataset_registry.status_json_path_for_entry(entry) if entry else None
        if status_path and status_path.exists():
            payload = read_json_file(status_path)
            if payload:
                return {
                    "payload": payload,
                    "status_source": "status_json",
                    "status_path": str(status_path),
                }
        import report_seo_elite_status  # noqa: WPS433

        payload = report_seo_elite_status.build_status_payload()
        return {
            "payload": payload,
            "status_source": "rebuilt_status_payload",
            "status_path": str(report_seo_elite_status.STATUS_JSON_PATH),
        }

    def run_ledger(self) -> Dict[str, Any]:
        status = self.load_seo_elite_status()
        payload = status["payload"]
        active_jobs = [item for item in payload.get("active_jobs", []) if item.get("status") == "active"]
        seo_delta = dataset_registry.build_dataset_delta("seo_elite")
        return {
            "updated_at": payload.get("updated_at", ""),
            "updated_at_iso": payload.get("updated_at_iso", ""),
            "status_source": status["status_source"],
            "status_path": status["status_path"],
            "current_phase": payload.get("activity", {}).get("current_phase", "unknown"),
            "active_job_count": len(active_jobs),
            "active_jobs": active_jobs,
            "all_jobs": payload.get("active_jobs", []),
            "pending_total": payload.get("pending", {}).get("pending_total", 0),
            "recent_fetch_total": payload.get("activity", {}).get("recent_fetch_total", 0),
            "recent_fetch_ok": payload.get("activity", {}).get("recent_fetch_ok", 0),
            "recent_fetch_error": payload.get("activity", {}).get("recent_fetch_error", 0),
            "ticker": payload.get("activity", {}).get("ticker", []),
            "openclaw": payload.get("openclaw", {}),
            "bridge": payload.get("bridge", {}),
            "registry_counts": [
                {
                    "id": item["id"],
                    "label": item["label"],
                    "chunks": item.get("chunks"),
                    "paths": item.get("paths"),
                    "status": item.get("status"),
                }
                for item in self.registry_payload().get("items", [])
            ],
            "seo_elite_delta": seo_delta,
        }

    def patent_live_audit(
        self,
        url: str,
        audit_types: Optional[Iterable[str]],
        max_pages: int,
        timeout: int,
    ) -> Dict[str, Any]:
        return live_patent_seo_audit.audit_site(
            url,
            audit_types=list(audit_types) if audit_types else None,
            max_pages=max_pages,
            timeout=timeout,
        )

    def list_prompts(self) -> Dict[str, Any]:
        return {"prompts": prompt_definitions()}

    def get_prompt(self, name: str, arguments: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        args = arguments or {}
        if name == "dataset_audit":
            dataset_id = args.get("dataset_id")
            if not dataset_id:
                raise ValueError("dataset_id is required")
            item = dataset_registry.get_dataset_summary(dataset_id)
            if item is None:
                raise ValueError(f"Unknown dataset id: {dataset_id}")
            goal = args.get("goal") or "trust and operational clarity"
            message = (
                f"Audit the `{dataset_id}` dataset for {goal}. Start by inspecting the registry overview and the specific dataset summary. "
                f"Then evaluate dataset identity, count credibility, linked datasets, and what this dataset is best used for. "
                f"Use `memory_dataset_inspect` for `{dataset_id}` and only call heavier retrieval tools if they materially improve the audit. "
                f"Dataset summary:\\n\\n{build_dataset_markdown(item)}"
            )
            return {"description": "Dataset audit workflow", "messages": [{"role": "user", "content": {"type": "text", "text": message}}]}

        if name == "federated_analysis":
            question = args.get("question")
            if not question:
                raise ValueError("question is required")
            role = args.get("role") or "kelp"
            message = (
                f"Run a federated local-memory analysis for this question: {question}\\n\\n"
                f"Use `memory_federated_query` with role `{role}`. Compare the selected datasets, explain why they were chosen, "
                f"surface the highest-signal evidence, and separate retrieval evidence from inference. "
                f"Reference relevant local resources such as `memory://registry/overview` and any selected `memory://dataset/...` resources when useful."
            )
            return {"description": "Federated analysis workflow", "messages": [{"role": "user", "content": {"type": "text", "text": message}}]}

        if name == "delta_explainer":
            dataset_id = args.get("dataset_id")
            if not dataset_id:
                raise ValueError("dataset_id is required")
            question = args.get("question") or "Explain what changed, what the baseline is, and what likely caused the movement."
            message = (
                f"Explain the latest local delta for `{dataset_id}`.\\n\\n"
                f"Question focus: {question}\\n\\n"
                f"Start with `memory_dataset_delta` for `{dataset_id}`. If history exists, call `memory_dataset_history` as well. "
                f"Use `memory://dataset/{dataset_id}/delta` and `memory://dataset/{dataset_id}/history` when useful. "
                f"Separate hard evidence from inference, call out missing history clearly, and recommend the next operator check if the delta looks suspicious."
            )
            return {"description": "Dataset delta explainer workflow", "messages": [{"role": "user", "content": {"type": "text", "text": message}}]}

        if name == "run_triage":
            focus = args.get("focus") or "freshness and pipeline health"
            message = (
                f"Run a local Squad Memory OS triage pass with focus on {focus}.\\n\\n"
                f"Start from `memory_run_ledger`, `memory://runs/ledger`, and `memory://registry/overview`. "
                f"Identify what is active, what looks stalled, what changed recently in SEO Elite, and the highest-value next operator actions. "
                f"Prefer concise triage output with: current state, risks, likely causes, and next actions."
            )
            return {"description": "Run triage workflow", "messages": [{"role": "user", "content": {"type": "text", "text": message}}]}

        if name == "live_patent_site_audit":
            url = args.get("url")
            if not url:
                raise ValueError("url is required")
            focus = args.get("focus") or "eeat, entity clarity, and ai search readiness"
            message = (
                f"Run a live patent-backed website audit for `{url}`.\\n\\n"
                f"Focus: {focus}. Start with `seo_patent_live_audit` for the live evidence set. "
                f"Then interpret the findings through the patent lenses that were loaded, keeping direct page evidence separate from inference. "
                f"Prioritize the highest-severity findings, the cleanest fixes, and any caveats caused by JS rendering or missing crawl surfaces."
            )
            return {"description": "Live patent site audit workflow", "messages": [{"role": "user", "content": {"type": "text", "text": message}}]}

        if name == "system_improvement_brief":
            problem = args.get("problem")
            if not problem:
                raise ValueError("problem is required")
            focus = args.get("focus") or "local-first product improvement"
            message = (
                f"Create a Squad Memory OS improvement brief for this problem: {problem}\\n\\n"
                f"Focus area: {focus}. Start from the current PRD resource `memory://prd/squad-memory-os` and the registry overview `memory://registry/overview`. "
                f"Then recommend a local-first solution that improves trust, speed, interoperability, or operator experience without requiring cloud infrastructure. "
                f"Prefer actionable phases, concrete MCP capabilities, and user-visible outcomes."
            )
            return {"description": "System improvement brief workflow", "messages": [{"role": "user", "content": {"type": "text", "text": message}}]}

        raise ValueError(f"Unknown prompt: {name}")

    def list_resources(self) -> Dict[str, Any]:
        return {"resources": resource_definitions(self.registry_payload())}

    def list_resource_templates(self) -> Dict[str, Any]:
        return {"resourceTemplates": resource_templates()}

    def read_resource(self, uri: str) -> Dict[str, Any]:
        registry_payload = self.registry_payload()
        if uri == "memory://registry/overview":
            text = build_registry_markdown(registry_payload)
            return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": text}]}
        if uri == "memory://prd/squad-memory-os":
            text = read_text_file(PRD_PATH)
            if not text:
                raise ValueError("PRD file not found")
            return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": text}]}
        if uri == "memory://runs/ledger":
            text = build_run_ledger_markdown(self.run_ledger())
            return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": text}]}
        if uri.startswith("memory://dataset/"):
            remainder = uri.split("memory://dataset/", 1)[1].strip("/")
            parts = remainder.split("/")
            dataset_id = parts[0]
            suffix = parts[1] if len(parts) > 1 else ""
            if suffix == "history":
                payload = self.dataset_history(dataset_id, limit=12)
                text = build_dataset_history_markdown(payload)
            elif suffix == "delta":
                payload = self.dataset_delta(dataset_id)
                text = build_dataset_delta_markdown(payload)
            else:
                item = dataset_registry.get_dataset_summary(dataset_id)
                if item is None:
                    raise ValueError(f"Unknown dataset id: {dataset_id}")
                text = build_dataset_markdown(item)
            return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": text}]}
        raise ValueError(f"Unknown resource: {uri}")

    def list_tools(self) -> Dict[str, Any]:
        return {"tools": tool_definitions()}

    def call_tool(self, name: str, arguments: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        args = arguments or {}
        try:
            if name == "memory_registry_overview":
                payload = self.registry_payload()
                return make_text_result(summarize_registry(payload), payload)

            if name == "memory_dataset_inspect":
                payload = dataset_registry.get_dataset_summary(args["dataset_id"])
                if payload is None:
                    return make_text_result(
                        f"Unknown dataset id: {args['dataset_id']}",
                        {"dataset_id": args["dataset_id"]},
                        is_error=True,
                    )
                return make_text_result(summarize_dataset(payload), payload)

            if name == "memory_dataset_history":
                payload = self.dataset_history(
                    args["dataset_id"],
                    clamp_top(args.get("limit"), default=8, max_value=30),
                )
                return make_text_result(summarize_dataset_history(payload), payload)

            if name == "memory_dataset_delta":
                payload = self.dataset_delta(args["dataset_id"])
                return make_text_result(summarize_dataset_delta(payload), payload)

            if name == "memory_run_ledger":
                payload = self.run_ledger()
                return make_text_result(summarize_run_ledger(payload), payload)

            if name == "seo_patent_live_audit":
                payload = self.patent_live_audit(
                    args["url"],
                    args.get("audit_types"),
                    clamp_top(args.get("max_pages"), default=7, max_value=12),
                    clamp_top(args.get("timeout"), default=20, max_value=60),
                )
                return make_text_result(summarize_live_patent_audit(payload), payload)

            if name == "memory_federated_query":
                payload = self.federated_query(
                    args["query"],
                    args.get("role"),
                    args.get("skill"),
                    clamp_top(args.get("top"), default=8),
                    args.get("datasets"),
                )
                return make_text_result(summarize_federated_query(payload), payload)

            if name == "memory_route_task":
                payload = self.route_task(
                    args["task"],
                    args.get("role"),
                    clamp_top(args.get("top"), default=5),
                    args.get("datasets"),
                )
                return make_text_result(summarize_route(payload), payload)

            if name == "memory_execution_plan":
                payload = self.execution_plan(
                    args["task"],
                    args.get("role"),
                    clamp_top(args.get("top"), default=5),
                    args.get("pack_id"),
                    args.get("datasets"),
                )
                return make_text_result(summarize_execution_plan(payload), payload)
        except KeyError as exc:
            return make_text_result(
                f"Missing required argument: {exc.args[0]}",
                {"tool": name, "missing_argument": exc.args[0]},
                is_error=True,
            )
        except Exception as exc:
            return make_text_result(
                f"{type(exc).__name__}: {exc}",
                {"tool": name, "error": type(exc).__name__, "message": str(exc)},
                is_error=True,
            )

        raise ValueError(f"Unknown tool: {name}")


def serve(server: SquadMemoryOsMcpServer) -> None:
    while True:
        request = read_message()
        if request is None:
            break

        method = request.get("method")
        message_id = request.get("id")
        params = request.get("params") or {}

        if message_id is None:
            if method == "notifications/initialized":
                continue
            continue

        try:
            if method == "initialize":
                write_message(success_response(message_id, server.initialize(params)))
            elif method == "ping":
                write_message(success_response(message_id, {}))
            elif method == "tools/list":
                write_message(success_response(message_id, server.list_tools()))
            elif method == "tools/call":
                tool_name = params.get("name")
                if not tool_name:
                    write_message(error_response(message_id, -32602, "Missing tool name"))
                    continue
                write_message(success_response(message_id, server.call_tool(tool_name, params.get("arguments"))))
            elif method == "prompts/list":
                write_message(success_response(message_id, server.list_prompts()))
            elif method == "prompts/get":
                prompt_name = params.get("name")
                if not prompt_name:
                    write_message(error_response(message_id, -32602, "Missing prompt name"))
                    continue
                write_message(success_response(message_id, server.get_prompt(prompt_name, params.get("arguments"))))
            elif method == "resources/list":
                write_message(success_response(message_id, server.list_resources()))
            elif method == "resources/templates/list":
                write_message(success_response(message_id, server.list_resource_templates()))
            elif method == "resources/read":
                uri = params.get("uri")
                if not uri:
                    write_message(error_response(message_id, -32602, "Missing resource uri"))
                    continue
                write_message(success_response(message_id, server.read_resource(uri)))
            else:
                write_message(error_response(message_id, -32601, f"Method not found: {method}"))
        except Exception as exc:
            write_message(error_response(message_id, -32603, f"Internal error: {type(exc).__name__}: {exc}"))


def main() -> None:
    args = parse_args()
    server = SquadMemoryOsMcpServer(
        skills_root=Path(args.skills_root).expanduser().resolve(),
        task_packs_path=Path(args.task_packs).expanduser().resolve(),
    )
    serve(server)


if __name__ == "__main__":
    main()
