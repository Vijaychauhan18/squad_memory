#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


BASE = Path(__file__).resolve().parent
DEFAULT_DURABLE_MEMORIES = (
    "dejan-ai-reverse-engineering-2026-03-20.md",
    "curated-seo-source-canon-2026-03-20.md",
    "practitioner-expansion-stox-krum-ray-2026-03-20.md",
    "practitioner-expansion-gabe-haynes-2026-03-20.md",
    "seo-expert-canon-2026-03-20.md",
)

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json"}
GRAPH_HQ_PHASE21_FILES = ("control_plane_report.md", "control_plane_status.json", "latest.json")
GRAPH_HQ_PHASE31_FILES = ("memory_graph_report.md", "memory_graph.json", "latest.json")
GRAPH_HQ_UI_FILES = ("index.html", "app.js", "graph-pro.js", "styles.css")
GRAPH_HQ_SOURCE_FILES = (
    "phase21_control_plane.py",
    "phase31_memory_graph.py",
    "run_phase21_control_plane.sh",
    "run_phase31_memory_graph.sh",
)


@dataclass(frozen=True)
class SyncConfig:
    codex_root: Path
    openclaw_workspace: Path
    squad_memory_root: Path = BASE
    selected_durable_memories: tuple[str, ...] = DEFAULT_DURABLE_MEMORIES

    @property
    def import_root(self) -> Path:
        return self.openclaw_workspace / "memory" / "imports" / "codex"

    @property
    def seo_memory_dir(self) -> Path:
        return self.codex_root / "skills" / "seo" / "memory"

    @property
    def seo_router(self) -> Path:
        return self.codex_root / "skills" / "seo" / "MEMORY.md"

    @property
    def seo_index(self) -> Path:
        return self.codex_root / "skills" / "seo" / "memory" / "INDEX.md"

    @property
    def dejan_root(self) -> Path:
        return self.codex_root / "skills" / "dejan-ai-reverse-engineering"

    @property
    def memories_dir(self) -> Path:
        return self.codex_root / "memories"

    @property
    def seo_agent_workspace(self) -> Path:
        return self.openclaw_workspace / "squad" / "seo"

    @property
    def skills_root(self) -> Path:
        return self.codex_root / "skills"

    @property
    def squad_memory_index(self) -> Path:
        return self.skills_root / "SQUAD_MEMORY.md"

    @property
    def graph_hq_root(self) -> Path:
        return self.import_root / "graph-hq"

    @property
    def phase21_dir(self) -> Path:
        return self.squad_memory_root / "ingest" / "phase21"

    @property
    def phase31_dir(self) -> Path:
        return self.squad_memory_root / "ingest" / "phase31"

    @property
    def memory_graph_ui_dir(self) -> Path:
        return self.squad_memory_root / "memory_graph_ui"


def parse_args() -> argparse.Namespace:
    home = Path.home()
    parser = argparse.ArgumentParser(description="Mirror Codex memory into OpenClaw workspace")
    parser.add_argument("--codex-root", default=str(home / ".codex"))
    parser.add_argument("--openclaw-workspace", default=str(home / ".openclaw" / "workspace"))
    parser.add_argument("--squad-memory-root", default=str(BASE))
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_text_tree(src_dir: Path, dest_dir: Path, suffixes: set[str] = TEXT_SUFFIXES) -> int:
    if not src_dir.exists():
        return 0
    dest_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for src in sorted(src_dir.rglob("*")):
        if not src.is_file():
            continue
        if src.suffix.lower() not in suffixes:
            continue
        relative = src.relative_to(src_dir)
        dest = dest_dir / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        count += 1
    return count


def copy_md_tree(src_dir: Path, dest_dir: Path) -> int:
    return copy_text_tree(src_dir, dest_dir, suffixes={".md"})


def copy_file_if_exists(src: Path, dest: Path) -> bool:
    if not src.exists():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return True


def copy_named_files(src_root: Path, dest_root: Path, file_names: tuple[str, ...]) -> list[str]:
    copied: list[str] = []
    for file_name in file_names:
        if copy_file_if_exists(src_root / file_name, dest_root / file_name):
            copied.append(file_name)
    return copied


def load_json_if_exists(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def format_percent(value: Any) -> str:
    if isinstance(value, (int, float)):
        return f"{value * 100:.2f}%"
    return "n/a"


def graph_hq_asset_count(summary: dict[str, Any]) -> int:
    return sum(
        len(summary.get(key, []))
        for key in ("phase21_files", "phase31_files", "ui_files", "source_files")
    )


def discover_skill_dirs(skills_root: Path) -> list[Path]:
    skill_dirs: list[Path] = []
    if not skills_root.exists():
        return skill_dirs
    for child in sorted(skills_root.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if (child / "SKILL.md").exists():
            skill_dirs.append(child)
    return skill_dirs


def copy_skill_pack(skill_dir: Path, dest_root: Path) -> dict[str, Any]:
    dest_dir = dest_root / skill_dir.name
    doc_count = copy_text_tree(skill_dir, dest_dir)
    entry_files = [
        name
        for name in ("SKILL.md", "MEMORY.md", "IDENTITY.md", "BOOTSTRAP.md", "AGENTS.md", "TOOLS.md", "SOUL.md")
        if (skill_dir / name).exists()
    ]
    memory_count = len(list((skill_dir / "memory").rglob("*.md"))) if (skill_dir / "memory").exists() else 0
    reference_count = len(list((skill_dir / "references").rglob("*.md"))) if (skill_dir / "references").exists() else 0
    return {
        "name": skill_dir.name,
        "doc_count": doc_count,
        "memory_count": memory_count,
        "reference_count": reference_count,
        "entry_files": entry_files,
        "dest_dir": str(dest_dir),
    }


def write_router(config: SyncConfig) -> None:
    router = config.openclaw_workspace / "MEMORY.md"
    text = f"""# OpenClaw Memory Router

This workspace imports curated SEO and AI-search memory from the local Codex stack.

## Imported Source
- Imported from `{config.codex_root}`
- Synced into `{config.import_root}`

## Start Here
- `memory/imports/codex/IMPORT_INDEX.md`
- `memory/imports/codex/graph-hq/INDEX.md`
- `memory/imports/codex/skill-packs/INDEX.md`
- `memory/imports/codex/seo-router/SEO_MEMORY.md`
- `memory/imports/codex/seo-memory/seo-expert-canon-2026.md`
- `memory/imports/codex/seo-memory/dejan-ai-reverse-engineering-pack.md`
- `memory/imports/codex/seo-memory/live-seo-feed-monitor.md`

## Best Reading Paths
- Squad role packs:
  `memory/imports/codex/skill-packs/INDEX.md`
- Graph + HQ surfaces:
  `memory/imports/codex/graph-hq/INDEX.md`
- AI search reverse engineering:
  `memory/imports/codex/seo-memory/dejan-ai-reverse-engineering-pack.md`
- Expert selection and routing:
  `memory/imports/codex/seo-memory/seo-expert-canon-2026.md`
- Source selection:
  `memory/imports/codex/seo-memory/seo-source-canon-2026.md`
- Freshness / newest titles:
  `memory/imports/codex/seo-memory/live-seo-feed-monitor.md`
- Durable dated context:
  `memory/imports/codex/durable/`

## Use Rule
- Treat imported Codex notes as the SEO intelligence layer.
- Treat imported skill packs as the squad operating layer.
- Treat graph + HQ imports as the live command-center and topology layer.
- Prefer the expert canon or SEO router before reading many files.
- Use live feed snapshots for freshness and durable notes for stable judgment.
"""
    router.parent.mkdir(parents=True, exist_ok=True)
    router.write_text(text)


def write_seo_agent_router(config: SyncConfig) -> None:
    text = f"""# SEO Agent Memory Router

This SEO workspace uses the shared Codex import mirrored into OpenClaw.

## Shared Import
- `{config.import_root}`

## Open First
- `../../memory/imports/codex/IMPORT_INDEX.md`
- `../../memory/imports/codex/graph-hq/INDEX.md`
- `../../memory/imports/codex/skill-packs/INDEX.md`
- `../../memory/imports/codex/seo-router/SEO_MEMORY.md`
- `../../memory/imports/codex/seo-memory/seo-expert-canon-2026.md`
- `../../memory/imports/codex/seo-memory/dejan-ai-reverse-engineering-pack.md`

## Use Rule
- Use the expert canon for source selection and practitioner routing.
- Use the DEJAN pack for AI search reverse engineering and grounding analysis.
- Use graph + HQ when the task depends on control-plane state, queue health, or memory graph topology.
- Use the squad skill index when the task needs a non-SEO role pack or handoff.
- Use the live feed monitor for newest items; use durable notes for stable advice.
"""
    root_router = config.seo_agent_workspace / "MEMORY.md"
    memory_router = config.seo_agent_workspace / "memory" / "ROUTER.md"
    root_router.parent.mkdir(parents=True, exist_ok=True)
    memory_router.parent.mkdir(parents=True, exist_ok=True)
    root_router.write_text(text)
    memory_router.write_text(text)


def write_skill_index(config: SyncConfig, skill_summaries: list[dict[str, Any]], shared_docs_count: int) -> None:
    index_path = config.import_root / "skill-packs" / "INDEX.md"
    synced_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Codex Squad Skill Packs",
        "",
        f"Synced at: {synced_at}",
        "",
        "## Imported Packs",
        f"- skill packs: {len(skill_summaries)}",
        f"- skill docs: {sum(int(item['doc_count']) for item in skill_summaries) + shared_docs_count}",
        "",
        "## Shared Squad Memory",
        f"- docs: `{shared_docs_count}`",
        "- entry files: SQUAD_MEMORY.md" if shared_docs_count else "- entry files: none",
        "- import path: `skill-packs/SQUAD_MEMORY.md`" if shared_docs_count else "- import path: none",
        "",
    ]
    for item in skill_summaries:
        lines.extend(
            [
                f"## {item['name']}",
                f"- docs: `{item['doc_count']}`",
                f"- memory notes: `{item['memory_count']}`",
                f"- references: `{item['reference_count']}`",
                f"- entry files: {', '.join(item['entry_files']) if item['entry_files'] else 'none'}",
                f"- import path: `skill-packs/{item['name']}`",
                "",
            ]
        )
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text("\n".join(lines))


def write_graph_hq_index(config: SyncConfig, summary: dict[str, Any]) -> None:
    index_path = config.graph_hq_root / "INDEX.md"
    lines = [
        "# Graph + HQ Import",
        "",
        f"Synced at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Source root: `{config.squad_memory_root}`",
        "",
        "## What Is Included",
        f"- Phase 21 HQ snapshots: `{len(summary.get('phase21_files', []))}`",
        f"- Phase 31 graph snapshots: `{len(summary.get('phase31_files', []))}`",
        f"- Graph / HQ UI files: `{len(summary.get('ui_files', []))}`",
        f"- Source builders and runners: `{len(summary.get('source_files', []))}`",
        f"- Generated graph / HQ docs: `{summary.get('docs_count', 0)}`",
        "",
        "## Best Files To Open First",
        "- `phase21/HQ_STATUS.md`",
        "- `phase21/control_plane_report.md`",
        "- `phase31/GRAPH_STATUS.md`",
        "- `phase31/memory_graph_report.md`",
        "- `ui/HQ_UI.md`",
        "- `source/BUILD_PIPELINE.md`",
        "",
        "## Raw Asset Paths",
        f"- Phase 21: {', '.join(f'`phase21/{name}`' for name in summary.get('phase21_files', [])) or 'none'}",
        f"- Phase 31: {', '.join(f'`phase31/{name}`' for name in summary.get('phase31_files', [])) or 'none'}",
        f"- UI: {', '.join(f'`ui/{name}`' for name in summary.get('ui_files', [])) or 'none'}",
        f"- Source: {', '.join(f'`source/{name}`' for name in summary.get('source_files', [])) or 'none'}",
        "",
        "## Use Rule",
        "- Read HQ status when deciding what the squad should do next.",
        "- Read graph status when the task needs topology, pack relationships, or memory-bank coverage.",
        "- Read the UI summary when the task needs the local command-surface behavior.",
        "- Open the raw JSON, JS, HTML, or Python files only when the summary is not enough.",
    ]
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text("\n".join(lines), encoding="utf-8")


def write_hq_status_doc(config: SyncConfig, phase21_status: dict[str, Any]) -> None:
    path = config.graph_hq_root / "phase21" / "HQ_STATUS.md"
    lines = [
        "# Squad HQ Status",
        "",
        f"Source: `{config.phase21_dir}`",
        "",
    ]
    if not phase21_status:
        lines.extend(
            [
                "Phase 21 status is not available in the source project.",
                "",
                "## Raw Files",
                "- `control_plane_report.md`",
                "- `control_plane_status.json`",
                "- `latest.json`",
            ]
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines), encoding="utf-8")
        return

    alerts = phase21_status.get("alerts", [])
    queues = phase21_status.get("queues", {})
    sources = phase21_status.get("sources", {})
    memory_health = phase21_status.get("memory_health", {})
    lines.extend(
        [
            "## Snapshot",
            f"- Generated: `{phase21_status.get('generated_at', 'n/a')}`",
            f"- Alerts: `{len(alerts)}`",
            f"- Queue groups: `{len(queues)}`",
            f"- Source groups: `{len(sources)}`",
            f"- Timeline phases tracked: `{len(phase21_status.get('timeline', []))}`",
            "",
            "## Queue Health",
        ]
    )
    if queues:
        for key, payload in sorted(queues.items()):
            counts = payload.get("counts", {})
            label = payload.get("label", key.title())
            lines.append(
                f"- {label}: total={payload.get('items_total', 0)} "
                f"hold={counts.get('hold', 0)} approve={counts.get('approve', 0)} reject={counts.get('reject', 0)}"
            )
    else:
        lines.append("- No queue data available.")
    lines.extend(["", "## Source Health"])
    if sources:
        for key, payload in sorted(sources.items()):
            label = payload.get("label", key.title())
            lines.append(
                f"- {label}: healthy={payload.get('ok_source_count', 0)}/{payload.get('source_count', 0)} "
                f"stale={payload.get('stale_source_count', 0)} errors={payload.get('error_source_count', 0)} "
                f"new_items={payload.get('new_items_total', 0)}"
            )
    else:
        lines.append("- No source health data available.")
    lines.extend(["", "## Memory Health"])
    if memory_health:
        lines.extend(
            [
                f"- Topics total: `{memory_health.get('topics_total', 0)}`",
                f"- Healthy topics: `{memory_health.get('healthy_topics', 0)}`",
                f"- Stale topics: `{memory_health.get('stale_topics', 0)}`",
                f"- Low-confidence topics: `{memory_health.get('low_confidence_topics', 0)}`",
                f"- Monitor-only topics: `{memory_health.get('monitor_only_topics', 0)}`",
            ]
        )
    else:
        lines.append("- No memory health data available.")
    lines.extend(
        [
            "",
            "## Raw Files",
            "- `control_plane_report.md`",
            "- `control_plane_status.json`",
            "- `latest.json`",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_graph_status_doc(config: SyncConfig, phase31_graph: dict[str, Any]) -> None:
    path = config.graph_hq_root / "phase31" / "GRAPH_STATUS.md"
    lines = [
        "# Memory Graph Status",
        "",
        f"Source: `{config.phase31_dir}`",
        "",
    ]
    if not phase31_graph:
        lines.extend(
            [
                "Phase 31 graph output is not available in the source project.",
                "",
                "## Raw Files",
                "- `memory_graph_report.md`",
                "- `memory_graph.json`",
                "- `latest.json`",
            ]
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines), encoding="utf-8")
        return

    meta = phase31_graph.get("meta", {})
    evaluation = meta.get("evaluation", {})
    task_evaluation = meta.get("task_evaluation", {})
    workspace = phase31_graph.get("workspace", {})
    lines.extend(
        [
            "## Snapshot",
            f"- Generated: `{phase31_graph.get('generated_at', 'n/a')}`",
            f"- Nodes: `{meta.get('nodes_total', 0)}`",
            f"- Links: `{meta.get('links_total', 0)}`",
            f"- Domains: `{meta.get('domains_total', 0)}`",
            f"- Packs: `{meta.get('packs_total', 0)}`",
            f"- Skills: `{meta.get('skills_total', 0)}`",
            f"- Topics: `{meta.get('topics_total', 0)}`",
            f"- Memory paths: `{meta.get('memory_paths_total', 0)}`",
            f"- Chunks: `{meta.get('chunks_total', 0)}`",
            f"- Alerts: `{meta.get('alerts_total', 0)}`",
            f"- Meetings: `{meta.get('meetings_total', len(phase31_graph.get('meetings', [])))}`",
            f"- Workspace contexts: `{meta.get('workspace_contexts_total', len(workspace.get('contexts', [])))}`",
            f"- Workspace items: `{meta.get('workspace_items_total', len(workspace.get('items', [])))}`",
            "",
            "## Evaluation",
            f"- Primary skill accuracy: `{format_percent(evaluation.get('primary_skill_accuracy'))}`",
            f"- Top-3 skill hit rate: `{format_percent(evaluation.get('top3_skill_hit_rate'))}`",
            f"- Top-5 path hit rate: `{format_percent(evaluation.get('top5_path_hit_rate'))}`",
            f"- Pack accuracy: `{format_percent(task_evaluation.get('pack_accuracy'))}`",
            f"- Pass rate: `{format_percent(task_evaluation.get('pass_rate'))}`",
            "",
            "## Raw Files",
            "- `memory_graph_report.md`",
            "- `memory_graph.json`",
            "- `latest.json`",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_hq_ui_doc(config: SyncConfig) -> None:
    path = config.graph_hq_root / "ui" / "HQ_UI.md"
    lines = [
        "# Graph + HQ UI",
        "",
        f"Source: `{config.memory_graph_ui_dir}`",
        "",
        "## View Modes",
        "- `HQ`: the default command-center board for meetings and handoffs.",
        "- `Split`: graph and meeting surfaces together.",
        "- `Graph`: the standard constellation view.",
        "- `Graph Pro`: the full drill-down scene with filters and playback.",
        "",
        "## UI Surfaces",
        "- Live Event Bus for queries, handoffs, and completions.",
        "- Agent Meeting stage with the Squad HQ board and live ticker.",
        "- Memory Constellation graph stage for nodes, packs, topics, and outcomes.",
        "- Inspector panel for selection details and legend context.",
        "",
        "## Raw Files",
        "- `index.html`",
        "- `app.js`",
        "- `graph-pro.js`",
        "- `styles.css`",
        "",
        "## Use Rule",
        "- Read this summary first when an OpenClaw task needs the local UI behavior.",
        "- Open the raw JS or HTML only when you need implementation details.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_graph_hq_build_doc(config: SyncConfig) -> None:
    path = config.graph_hq_root / "source" / "BUILD_PIPELINE.md"
    lines = [
        "# Graph + HQ Build Pipeline",
        "",
        f"Source: `{config.squad_memory_root}`",
        "",
        "## Flow",
        "- `phase21_control_plane.py` writes the HQ control-plane snapshots under `phase21/`.",
        "- `phase31_memory_graph.py` builds the graph snapshot from the live memory system and Phase 21 status.",
        "- `run_phase21_control_plane.sh` and `run_phase31_memory_graph.sh` are the local automation entrypoints.",
        "- `memory_graph_ui/` contains the local command-surface files used by the served viewer.",
        "",
        "## Raw Files",
        "- `phase21_control_plane.py`",
        "- `phase31_memory_graph.py`",
        "- `run_phase21_control_plane.sh`",
        "- `run_phase31_memory_graph.sh`",
        "",
        "## Use Rule",
        "- Use the source files when the squad must explain how HQ or graph outputs are produced.",
        "- Use the phase21 and phase31 snapshots when the squad only needs the current state.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def sync_graph_hq_bundle(config: SyncConfig) -> dict[str, Any]:
    summary = {
        "source_root": str(config.squad_memory_root),
        "phase21_files": copy_named_files(config.phase21_dir, config.graph_hq_root / "phase21", GRAPH_HQ_PHASE21_FILES),
        "phase31_files": copy_named_files(config.phase31_dir, config.graph_hq_root / "phase31", GRAPH_HQ_PHASE31_FILES),
        "ui_files": copy_named_files(config.memory_graph_ui_dir, config.graph_hq_root / "ui", GRAPH_HQ_UI_FILES),
        "source_files": copy_named_files(config.squad_memory_root, config.graph_hq_root / "source", GRAPH_HQ_SOURCE_FILES),
    }
    phase21_status = load_json_if_exists(config.phase21_dir / "control_plane_status.json")
    phase31_graph = load_json_if_exists(config.phase31_dir / "memory_graph.json")
    write_hq_status_doc(config, phase21_status)
    write_graph_status_doc(config, phase31_graph)
    write_hq_ui_doc(config)
    write_graph_hq_build_doc(config)
    summary["docs_count"] = 5
    write_graph_hq_index(config, summary)
    summary["asset_count"] = graph_hq_asset_count(summary)
    return summary


def write_import_index(
    config: SyncConfig,
    counts: dict[str, int],
    skill_summaries: list[dict[str, Any]],
    graph_hq_summary: dict[str, Any],
) -> None:
    index_path = config.import_root / "IMPORT_INDEX.md"
    synced_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"""# Codex -> OpenClaw Import Index

Synced at: {synced_at}

## What Was Imported
- SEO memory notes: {counts["seo_memory"]}
- SEO router files: {counts["seo_router"]}
- DEJAN pack files: {counts["dejan"]}
- Durable memory notes: {counts["durable"]}
- Graph + HQ raw assets: {counts["graph_hq_assets"]}
- Graph + HQ summary docs: {counts["graph_hq_docs"]}
- Squad skill packs: {counts["skill_packs"]}
- Squad skill docs: {counts["skill_docs"]}

## Layout
- `seo-memory/`:
  mirrored markdown notes from `~/.codex/skills/seo/memory`
- `seo-router/`:
  mirrored router files from `~/.codex/skills/seo`
- `dejan-pack/`:
  mirrored DEJAN skill summary and references
- `durable/`:
  selected durable dated memory notes from `~/.codex/memories`
- `graph-hq/`:
  mirrored graph snapshots, HQ control-plane snapshots, UI files, and generated graph/HQ summaries
- `skill-packs/`:
  mirrored Codex squad skills, role packs, and operating memories from `~/.codex/skills`

## Best Files To Open First
- `graph-hq/INDEX.md`
- `graph-hq/phase21/HQ_STATUS.md`
- `graph-hq/phase31/GRAPH_STATUS.md`
- `graph-hq/ui/HQ_UI.md`
- `skill-packs/INDEX.md`
- `skill-packs/orchestrator-pinchy/SKILL.md`
- `skill-packs/seo-coral/SKILL.md`
- `skill-packs/researcher-kelp/SKILL.md`
- `seo-memory/seo-expert-canon-2026.md`
- `seo-memory/seo-source-canon-2026.md`
- `seo-memory/dejan-ai-reverse-engineering-pack.md`
- `seo-memory/live-seo-feed-monitor.md`
- `durable/seo-expert-canon-2026-03-20.md`

## Imported Skill Packs
{chr(10).join(f"- {item['name']} | docs={item['doc_count']} memory={item['memory_count']} references={item['reference_count']}" for item in skill_summaries)}

## Graph + HQ Asset Groups
- phase21: {", ".join(graph_hq_summary.get("phase21_files", [])) or "none"}
- phase31: {", ".join(graph_hq_summary.get("phase31_files", [])) or "none"}
- ui: {", ".join(graph_hq_summary.get("ui_files", [])) or "none"}
- source: {", ".join(graph_hq_summary.get("source_files", [])) or "none"}
"""
    index_path.write_text(text)


def sync_openclaw_memory(config: SyncConfig) -> dict[str, Any]:
    reset_dir(config.import_root)

    counts: dict[str, int] = {
        "seo_memory": 0,
        "seo_router": 0,
        "dejan": 0,
        "durable": 0,
        "graph_hq_assets": 0,
        "graph_hq_docs": 0,
        "skill_packs": 0,
        "skill_docs": 0,
    }
    skill_summaries: list[dict[str, Any]] = []

    counts["seo_memory"] = copy_md_tree(config.seo_memory_dir, config.import_root / "seo-memory")

    if copy_file_if_exists(config.seo_router, config.import_root / "seo-router" / "SEO_MEMORY.md"):
        counts["seo_router"] += 1
    if copy_file_if_exists(config.seo_index, config.import_root / "seo-router" / "SEO_INDEX.md"):
        counts["seo_router"] += 1

    if copy_file_if_exists(config.dejan_root / "SKILL.md", config.import_root / "dejan-pack" / "SKILL.md"):
        counts["dejan"] += 1
    counts["dejan"] += copy_md_tree(
        config.dejan_root / "references",
        config.import_root / "dejan-pack" / "references",
    )

    for name in config.selected_durable_memories:
        if copy_file_if_exists(config.memories_dir / name, config.import_root / "durable" / name):
            counts["durable"] += 1

    graph_hq_summary = sync_graph_hq_bundle(config)
    counts["graph_hq_assets"] = int(graph_hq_summary["asset_count"])
    counts["graph_hq_docs"] = int(graph_hq_summary["docs_count"])

    if copy_file_if_exists(config.squad_memory_index, config.import_root / "skill-packs" / "SQUAD_MEMORY.md"):
        counts["skill_docs"] += 1

    for skill_dir in discover_skill_dirs(config.skills_root):
        summary = copy_skill_pack(skill_dir, config.import_root / "skill-packs")
        if summary["doc_count"] <= 0:
            continue
        skill_summaries.append(summary)
        counts["skill_packs"] += 1
        counts["skill_docs"] += int(summary["doc_count"])

    shared_docs_count = 1 if (config.import_root / "skill-packs" / "SQUAD_MEMORY.md").exists() else 0
    write_skill_index(config, skill_summaries, shared_docs_count)
    write_import_index(config, counts, skill_summaries, graph_hq_summary)
    write_router(config)
    write_seo_agent_router(config)

    return {
        "synced_at": datetime.now().isoformat(),
        "codex_root": str(config.codex_root),
        "openclaw_workspace": str(config.openclaw_workspace),
        "import_root": str(config.import_root),
        "counts": counts,
        "graph_hq": graph_hq_summary,
        "skill_packs": skill_summaries,
    }


def main() -> int:
    args = parse_args()
    config = SyncConfig(
        codex_root=Path(args.codex_root),
        openclaw_workspace=Path(args.openclaw_workspace),
        squad_memory_root=Path(args.squad_memory_root),
    )
    result = sync_openclaw_memory(config)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        counts = result["counts"]
        print(
            f"Synced Codex -> OpenClaw | seo_memory={counts['seo_memory']} "
            f"seo_router={counts['seo_router']} dejan={counts['dejan']} durable={counts['durable']} "
            f"graph_hq_assets={counts['graph_hq_assets']} graph_hq_docs={counts['graph_hq_docs']}"
        )
        print(result["import_root"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
