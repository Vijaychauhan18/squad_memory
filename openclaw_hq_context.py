#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def shared_workspace_root(seo_workspace: Path) -> Path:
    if seo_workspace.name == "seo" and seo_workspace.parent.name == "squad":
        return seo_workspace.parent.parent
    return seo_workspace


def default_graph_hq_root(seo_workspace: Path) -> Path:
    return shared_workspace_root(seo_workspace) / "memory" / "imports" / "codex" / "graph-hq"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def safe_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def safe_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def build_graph_hq_context(seo_workspace: Path, graph_hq_root: Path | None = None) -> Dict[str, Any]:
    root = graph_hq_root or default_graph_hq_root(seo_workspace)
    phase21_status = load_json(root / "phase21" / "control_plane_status.json")
    phase31_graph = load_json(root / "phase31" / "memory_graph.json")

    seo_queue = phase21_status.get("queues", {}).get("seo", {})
    seo_queue_counts = seo_queue.get("counts", {})
    seo_sources = phase21_status.get("sources", {}).get("seo", {})
    phase31_meta = phase31_graph.get("meta", {})
    evaluation = phase31_meta.get("evaluation", {})
    task_evaluation = phase31_meta.get("task_evaluation", {})

    return {
        "available": bool(phase21_status or phase31_graph),
        "ready": bool(phase21_status) and bool(phase31_graph),
        "graph_hq_root": str(root),
        "files": {
            "phase21_status_json": str(root / "phase21" / "control_plane_status.json"),
            "phase21_summary_md": str(root / "phase21" / "HQ_STATUS.md"),
            "phase31_graph_json": str(root / "phase31" / "memory_graph.json"),
            "phase31_summary_md": str(root / "phase31" / "GRAPH_STATUS.md"),
            "ui_summary_md": str(root / "ui" / "HQ_UI.md"),
        },
        "phase21": {
            "alerts_total": len(phase21_status.get("alerts", [])),
            "seo_queue_total": safe_int(seo_queue.get("items_total")),
            "seo_queue_hold": safe_int(seo_queue_counts.get("hold")),
            "seo_queue_approve": safe_int(seo_queue_counts.get("approve")),
            "seo_queue_reject": safe_int(seo_queue_counts.get("reject")),
            "seo_sources_total": safe_int(seo_sources.get("source_count")),
            "seo_sources_ok": safe_int(seo_sources.get("ok_source_count")),
            "seo_stale_sources": safe_int(seo_sources.get("stale_source_count")),
            "seo_new_items": safe_int(seo_sources.get("new_items_total")),
        },
        "phase31": {
            "nodes_total": safe_int(phase31_meta.get("nodes_total")),
            "links_total": safe_int(phase31_meta.get("links_total")),
            "topics_total": safe_int(phase31_meta.get("topics_total")),
            "memory_paths_total": safe_int(phase31_meta.get("memory_paths_total")),
            "chunks_total": safe_int(phase31_meta.get("chunks_total")),
            "alerts_total": safe_int(phase31_meta.get("alerts_total")),
            "meetings_total": safe_int(phase31_meta.get("meetings_total")),
            "workspace_contexts_total": safe_int(phase31_meta.get("workspace_contexts_total")),
            "workspace_items_total": safe_int(phase31_meta.get("workspace_items_total")),
            "primary_skill_accuracy": safe_float(evaluation.get("primary_skill_accuracy")),
            "top3_skill_hit_rate": safe_float(evaluation.get("top3_skill_hit_rate")),
            "top5_path_hit_rate": safe_float(evaluation.get("top5_path_hit_rate")),
            "pack_accuracy": safe_float(task_evaluation.get("pack_accuracy")),
            "pass_rate": safe_float(task_evaluation.get("pass_rate")),
        },
    }
