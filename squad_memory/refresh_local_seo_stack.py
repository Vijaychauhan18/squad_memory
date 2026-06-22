#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


HOME = Path.home()


@dataclass(frozen=True)
class StackPaths:
    workspace: Path
    seo_intelligence_server: Path = HOME / "Desktop" / "seo-intelligence-mcp" / "server.py"
    seo_intelligence_root: Path = HOME / "Desktop" / "seo-intelligence-mcp"
    gsc_server: Path = HOME / "Desktop" / "seomcp-busbud" / "mcp-gsc" / "gsc_server.py"
    gsc_root: Path = HOME / "Desktop" / "seomcp-busbud" / "mcp-gsc"
    gsc_service_account: Path = HOME / "Desktop" / "seomcp-busbud" / "service-account.json"
    seo_memory_server: Path = HOME / "portable-repos" / "seo-vector-snapshot" / "mcp" / "seo_memory_mcp_server.py"
    seo_memory_db: Path = HOME / "portable-repos" / "seo-vector-snapshot" / "db" / "squad_memory.db"
    seo_memory_task_packs: Path = HOME / "portable-repos" / "seo-vector-snapshot" / "tools" / "task_packs.json"
    rust_seo_mcp_binary: Path = HOME / "Downloads" / "seo-mcp-main" / "target" / "release" / "seo-mcp-server"
    rust_seo_mcp_config: Path = HOME / "Downloads" / "seo-mcp-main" / "config" / "config.toml"
    rust_seo_mcp_guide: Path = HOME / "Downloads" / "seo-mcp-main" / "SEO-REPORT-GUIDE.md"
    seo_elite_db: Path = HOME / "squad_memory" / "seo_elite_memory.db"
    squad_memory_db: Path = HOME / "squad_memory" / "squad_memory.db"
    seo_elite_status_json: Path = HOME / ".codex" / "elite-skills" / "seo-elite" / "status" / "latest-status.json"


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def sqlite_count(path: Path, query: str) -> int:
    if not path.exists():
        return 0
    try:
        with sqlite3.connect(str(path)) as con:
            return int(con.execute(query).fetchone()[0])
    except sqlite3.Error:
        return 0


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def extract_registered_tool_names(server_path: Path) -> List[str]:
    if not server_path.exists():
        return []
    return sorted(set(re.findall(r"mcp\.tool\(\)\(([\w_]+)\)", read_text(server_path))))


def extract_decorated_tool_names(server_path: Path) -> List[str]:
    if not server_path.exists():
        return []
    return sorted(set(re.findall(r"@mcp\.tool\(\)\s+async def\s+([\w_]+)\(", read_text(server_path))))


def extract_named_tool_entries(path: Path) -> List[str]:
    if not path.exists():
        return []
    names = re.findall(r'"name":\s*"([a-zA-Z0-9_\-]+)"', read_text(path))
    filtered = [name for name in names if name.startswith("seo_")]
    return sorted(set(filtered))


def extract_rust_guide_tool_names(path: Path) -> List[str]:
    if not path.exists():
        return []
    names = re.findall(r"seo-mcp\s+([a-zA-Z0-9_]+)", read_text(path))
    filtered = [name for name in names if "_" in name and name not in {"seo_mcp_server"}]
    return sorted(set(filtered))


def command_for(component_id: str, paths: StackPaths) -> str:
    if component_id == "seo_intelligence_mcp":
        return f"python3 {paths.seo_intelligence_server}"
    if component_id == "gsc_mcp":
        return f"python3 {paths.gsc_server}"
    if component_id == "seo_memory_mcp":
        return (
            f"python3 {paths.seo_memory_server} --db {paths.seo_memory_db} "
            f"--skills-root {HOME / '.claude' / 'skills'} --task-packs {paths.seo_memory_task_packs}"
        )
    if component_id == "rust_seo_mcp":
        return f"SEO_MCP_CONFIG={paths.rust_seo_mcp_config} {paths.rust_seo_mcp_binary}"
    return "local artifact only"


def load_status_summary(paths: StackPaths) -> Dict[str, Any]:
    payload = load_json(paths.seo_elite_status_json)
    if not payload:
        return {}
    return {
        "chunks": payload.get("db", {}).get("chunks", 0),
        "paths": payload.get("db", {}).get("paths", 0),
        "pending_total": payload.get("pending", {}).get("pending_total", 0),
        "phase": payload.get("activity", {}).get("current_phase", "unknown"),
        "live_article_notes": payload.get("articles", {}).get("live_article_notes", 0),
        "primary_source_notes": payload.get("coverage", {}).get("primary_source_notes", 0),
    }


def build_components(paths: StackPaths) -> List[Dict[str, Any]]:
    seo_elite_status = load_status_summary(paths)
    components = [
        {
            "id": "seo_elite_knowledge",
            "label": "SEO Elite Knowledge Layer",
            "kind": "local_knowledge",
            "status": "ready" if paths.seo_elite_db.exists() and paths.seo_elite_status_json.exists() else "partial",
            "paths": [str(paths.seo_elite_db), str(paths.seo_elite_status_json)],
            "counts": {
                "chunks": sqlite_count(paths.seo_elite_db, "select count(*) from chunks"),
                "paths": sqlite_count(paths.seo_elite_db, "select count(distinct path) from chunks"),
            },
            "summary": (
                f"Freshness-first SEO research layer. phase={seo_elite_status.get('phase', 'unknown')}, "
                f"pending={seo_elite_status.get('pending_total', 0)}, "
                f"live_articles={seo_elite_status.get('live_article_notes', 0)}."
            ),
            "command": command_for("seo_elite_knowledge", paths),
            "tools": [],
        },
        {
            "id": "seo_memory_mcp",
            "label": "SEO Memory MCP",
            "kind": "mcp_server",
            "status": "ready" if paths.seo_memory_server.exists() and paths.seo_memory_db.exists() else "partial",
            "paths": [str(paths.seo_memory_server), str(paths.seo_memory_db), str(paths.seo_memory_task_packs)],
            "counts": {
                "chunks": sqlite_count(paths.seo_memory_db, "select count(*) from chunks"),
                "task_packs": len(load_json(paths.seo_memory_task_packs).get("packs", [])),
            },
            "summary": "Task routing and local SEO memory retrieval across packs, skills, and evidence notes.",
            "command": command_for("seo_memory_mcp", paths),
            "tools": extract_named_tool_entries(paths.seo_memory_server),
        },
        {
            "id": "seo_intelligence_mcp",
            "label": "SEO Intelligence MCP",
            "kind": "mcp_server",
            "status": "ready" if paths.seo_intelligence_server.exists() else "missing",
            "paths": [str(paths.seo_intelligence_server)],
            "counts": {
                "tools": len(extract_registered_tool_names(paths.seo_intelligence_server)),
            },
            "summary": "Analysis layer for cannibalization, content gaps, intent, topical authority, SERP, internal links, redirects, and E-E-A-T.",
            "command": command_for("seo_intelligence_mcp", paths),
            "tools": extract_registered_tool_names(paths.seo_intelligence_server),
        },
        {
            "id": "gsc_mcp",
            "label": "GSC MCP",
            "kind": "mcp_server",
            "status": "ready" if paths.gsc_server.exists() and paths.gsc_service_account.exists() else "partial",
            "paths": [str(paths.gsc_server), str(paths.gsc_service_account)],
            "counts": {
                "tools": len(extract_decorated_tool_names(paths.gsc_server)),
            },
            "summary": "Google Search Console operations for analytics, inspections, sitemap management, and indexing workflows.",
            "command": command_for("gsc_mcp", paths),
            "tools": extract_decorated_tool_names(paths.gsc_server),
        },
        {
            "id": "rust_seo_mcp",
            "label": "Rust SEO MCP",
            "kind": "mcp_server",
            "status": "ready" if paths.rust_seo_mcp_binary.exists() and paths.rust_seo_mcp_config.exists() else "partial",
            "paths": [str(paths.rust_seo_mcp_binary), str(paths.rust_seo_mcp_config), str(paths.rust_seo_mcp_guide)],
            "counts": {
                "tools": len(extract_rust_guide_tool_names(paths.rust_seo_mcp_guide)),
            },
            "summary": "Broader SEO operations server with crawl, schema, GSC, GA4, CWV, sitemap, and IndexNow utilities.",
            "command": command_for("rust_seo_mcp", paths),
            "tools": extract_rust_guide_tool_names(paths.rust_seo_mcp_guide),
        },
        {
            "id": "squad_memory_db",
            "label": "Squad Memory DB",
            "kind": "local_knowledge",
            "status": "ready" if paths.squad_memory_db.exists() else "missing",
            "paths": [str(paths.squad_memory_db)],
            "counts": {
                "chunks": sqlite_count(paths.squad_memory_db, "select count(*) from chunks"),
                "paths": sqlite_count(paths.squad_memory_db, "select count(distinct path) from chunks"),
            },
            "summary": "Broader task-pack and role-routing memory for repeatable multi-skill execution plans.",
            "command": command_for("squad_memory_db", paths),
            "tools": [],
        },
    ]
    return components


def workflow_queue_templates() -> Dict[str, List[Dict[str, Any]]]:
    return {
        "freshness-radar": [
            {
                "id": "collect-fresh-signals",
                "title": "Collect Fresh Signals",
                "objective": "Pull the freshest local SEO notes and cluster them into AI-search, content, and technical changes.",
                "priority": "now",
                "owner": "agent",
                "stack": ["seo_elite_knowledge"],
                "deliverable": "Fresh-note shortlist with timestamps and source paths.",
                "depends_on": [],
            },
            {
                "id": "retrieve-supporting-canon",
                "title": "Retrieve Supporting Canon",
                "objective": "Use SEO Memory MCP to retrieve supporting canon notes or task packs for the strongest fresh signals.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_memory_mcp"],
                "deliverable": "Supporting canon notes and task-pack matches.",
                "depends_on": ["collect-fresh-signals"],
            },
            {
                "id": "draft-same-day-brief",
                "title": "Draft Same-Day Brief",
                "objective": "Turn the evidence into a same-day brief with the top 3 actions worth taking now.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_elite_knowledge", "seo_memory_mcp"],
                "deliverable": "Short same-day SEO action brief.",
                "depends_on": ["retrieve-supporting-canon"],
            },
            {
                "id": "publish-priority-output",
                "title": "Publish Priority Output",
                "objective": "Write the final mission output and highlight the single highest-priority move.",
                "priority": "later",
                "owner": "agent",
                "stack": ["seo_elite_knowledge"],
                "deliverable": "Updated mission outbox file for Freshness Radar.",
                "depends_on": ["draft-same-day-brief"],
            },
        ],
        "gsc-opportunity-mining": [
            {
                "id": "pull-page-query-opportunities",
                "title": "Pull Page-Query Opportunities",
                "objective": "Extract the best page-query and CTR opportunities from local GSC access.",
                "priority": "now",
                "owner": "mixed",
                "stack": ["gsc_mcp"],
                "deliverable": "Shortlist of promising page-query pairs.",
                "depends_on": [],
            },
            {
                "id": "analyze-intent-title-gaps",
                "title": "Analyze Intent and Title Gaps",
                "objective": "Run title, intent, and snippet analysis on the shortlisted opportunities.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_intelligence_mcp"],
                "deliverable": "Analysis of likely CTR and intent mismatches.",
                "depends_on": ["pull-page-query-opportunities"],
            },
            {
                "id": "rank-top-wins",
                "title": "Rank Top Wins",
                "objective": "Turn the evidence into a prioritized list of the fastest wins.",
                "priority": "next",
                "owner": "agent",
                "stack": ["gsc_mcp", "seo_intelligence_mcp"],
                "deliverable": "Ranked opportunity list with expected lift rationale.",
                "depends_on": ["analyze-intent-title-gaps"],
            },
            {
                "id": "publish-improvement-queue",
                "title": "Publish Improvement Queue",
                "objective": "Write the improvement queue with next edits and validation checks.",
                "priority": "later",
                "owner": "agent",
                "stack": ["seo_memory_mcp"],
                "deliverable": "Reusable page/query improvement queue.",
                "depends_on": ["rank-top-wins"],
            },
        ],
        "cannibalization-cleanup": [
            {
                "id": "find-overlap-clusters",
                "title": "Find Overlap Clusters",
                "objective": "Detect URL groups that appear to compete for the same intent.",
                "priority": "now",
                "owner": "agent",
                "stack": ["seo_intelligence_mcp"],
                "deliverable": "Overlap clusters grouped by intent.",
                "depends_on": [],
            },
            {
                "id": "confirm-winning-urls",
                "title": "Confirm Winning URLs",
                "objective": "Use GSC evidence to confirm which URL should lead each cluster.",
                "priority": "next",
                "owner": "mixed",
                "stack": ["gsc_mcp"],
                "deliverable": "Winner/loser decision per cluster.",
                "depends_on": ["find-overlap-clusters"],
            },
            {
                "id": "define-merge-actions",
                "title": "Define Merge Actions",
                "objective": "Translate the cluster decisions into merge, redirect, and internal-link changes.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_intelligence_mcp", "gsc_mcp"],
                "deliverable": "Action list for canonicalization cleanup.",
                "depends_on": ["confirm-winning-urls"],
            },
            {
                "id": "publish-canonicalization-plan",
                "title": "Publish Canonicalization Plan",
                "objective": "Write the final cleanup plan with the safest order of operations.",
                "priority": "later",
                "owner": "agent",
                "stack": ["seo_memory_mcp"],
                "deliverable": "Canonicalization and redirect plan.",
                "depends_on": ["define-merge-actions"],
            },
        ],
        "indexation-war-room": [
            {
                "id": "inspect-affected-urls",
                "title": "Inspect Affected URLs",
                "objective": "Gather URL inspection evidence for the affected pages or patterns.",
                "priority": "now",
                "owner": "mixed",
                "stack": ["gsc_mcp"],
                "deliverable": "Inspection snapshot for impacted URLs.",
                "depends_on": [],
            },
            {
                "id": "crawl-technical-causes",
                "title": "Crawl Technical Causes",
                "objective": "Check robots, sitemaps, schema, and crawlability factors that may be blocking indexation.",
                "priority": "next",
                "owner": "agent",
                "stack": ["rust_seo_mcp"],
                "deliverable": "Technical cause list with evidence.",
                "depends_on": ["inspect-affected-urls"],
            },
            {
                "id": "rank-fix-order",
                "title": "Rank Fix Order",
                "objective": "Combine inspection and crawl findings into the best fix order.",
                "priority": "next",
                "owner": "agent",
                "stack": ["gsc_mcp", "rust_seo_mcp"],
                "deliverable": "Fix-order shortlist by impact and confidence.",
                "depends_on": ["crawl-technical-causes"],
            },
            {
                "id": "publish-war-room-brief",
                "title": "Publish War Room Brief",
                "objective": "Write the final indexation brief with escalations and next checks.",
                "priority": "later",
                "owner": "agent",
                "stack": ["seo_memory_mcp"],
                "deliverable": "Indexation diagnosis with fix order.",
                "depends_on": ["rank-fix-order"],
            },
        ],
        "content-gap-to-brief": [
            {
                "id": "select-topic-gap",
                "title": "Select Topic Gap",
                "objective": "Choose the target topic or keyword gap with the strongest local evidence.",
                "priority": "now",
                "owner": "mixed",
                "stack": ["seo_elite_knowledge"],
                "deliverable": "Target topic or keyword gap.",
                "depends_on": [],
            },
            {
                "id": "analyze-intent-gap",
                "title": "Analyze Intent Gap",
                "objective": "Run content-gap and intent analysis for the selected topic.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_intelligence_mcp"],
                "deliverable": "Intent and content-gap analysis notes.",
                "depends_on": ["select-topic-gap"],
            },
            {
                "id": "route-pack-and-canon",
                "title": "Route Pack and Canon",
                "objective": "Use SEO Memory MCP to choose the best reusable pack and supporting canon.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_memory_mcp"],
                "deliverable": "Task-pack choice and supporting canon references.",
                "depends_on": ["analyze-intent-gap"],
            },
            {
                "id": "publish-content-brief",
                "title": "Publish Content Brief",
                "objective": "Write the final content brief grounded in local knowledge and live search context.",
                "priority": "later",
                "owner": "agent",
                "stack": ["seo_elite_knowledge", "seo_memory_mcp"],
                "deliverable": "Content brief with structure and evidence.",
                "depends_on": ["route-pack-and-canon"],
            },
        ],
        "technical-audit-sprint": [
            {
                "id": "crawl-technical-snapshot",
                "title": "Crawl Technical Snapshot",
                "objective": "Run the fastest crawl, schema, CWV, and sitemap checks for the current target.",
                "priority": "now",
                "owner": "mixed",
                "stack": ["rust_seo_mcp"],
                "deliverable": "Technical snapshot with raw findings.",
                "depends_on": [],
            },
            {
                "id": "analyze-link-and-eeat-risks",
                "title": "Analyze Link and E-E-A-T Risks",
                "objective": "Layer internal-link, redirect, and trust analysis over the technical snapshot.",
                "priority": "next",
                "owner": "agent",
                "stack": ["seo_intelligence_mcp"],
                "deliverable": "Risk analysis for internal links, redirects, and trust issues.",
                "depends_on": ["crawl-technical-snapshot"],
            },
            {
                "id": "prioritize-fixes",
                "title": "Prioritize Fixes",
                "objective": "Turn the findings into a fix order based on severity and speed.",
                "priority": "next",
                "owner": "agent",
                "stack": ["rust_seo_mcp", "seo_intelligence_mcp"],
                "deliverable": "Prioritized fix list.",
                "depends_on": ["analyze-link-and-eeat-risks"],
            },
            {
                "id": "publish-issue-queue",
                "title": "Publish Issue Queue",
                "objective": "Write the final technical issue queue with verification steps.",
                "priority": "later",
                "owner": "agent",
                "stack": ["seo_memory_mcp"],
                "deliverable": "Technical issue queue with next actions.",
                "depends_on": ["prioritize-fixes"],
            },
        ],
    }


def build_workflows(components: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    queue_templates = workflow_queue_templates()
    return [
        {
            "id": "freshness-radar",
            "name": "Freshness Radar",
            "objective": "Turn the latest local SEO source movement into same-day actions.",
            "best_when": "You need current industry shifts, AI search changes, or emerging technical patterns.",
            "cadence": "hourly to same-day",
            "impact": 5,
            "effort": 2,
            "automation_fit": "ambient",
            "cooldown_hours": 4,
            "goal_keywords": ["fresh", "latest", "today", "trend", "change", "ai search", "update", "news"],
            "stack": ["seo_elite_knowledge", "seo_memory_mcp"],
            "steps": [
                "Read the latest SEO Elite status and digest first.",
                "Use SEO Memory MCP to route the task or retrieve supporting canon notes.",
                "Write a short action brief focused on only the freshest items.",
            ],
            "queue_template": queue_templates["freshness-radar"],
            "output": "Short ops brief or daily priorities.",
        },
        {
            "id": "gsc-opportunity-mining",
            "name": "GSC Opportunity Mining",
            "objective": "Find high-leverage CTR, ranking, and page-query opportunities from Search Console.",
            "best_when": "You want traffic lifts from existing content instead of net-new pages.",
            "cadence": "daily to weekly",
            "impact": 5,
            "effort": 3,
            "automation_fit": "site-data",
            "cooldown_hours": 12,
            "goal_keywords": ["gsc", "search console", "ctr", "ranking", "traffic", "impressions", "queries", "pages"],
            "stack": ["gsc_mcp", "seo_intelligence_mcp", "seo_memory_mcp"],
            "steps": [
                "Pull performance overview or page-query analytics from GSC MCP.",
                "Use SEO Intelligence MCP for title/meta and intent analysis.",
                "Use SEO Memory MCP to turn findings into a reusable execution plan.",
            ],
            "queue_template": queue_templates["gsc-opportunity-mining"],
            "output": "Prioritized page/query improvement queue.",
        },
        {
            "id": "cannibalization-cleanup",
            "name": "Cannibalization Cleanup",
            "objective": "Find overlapping URLs, choose winners, and clean internal architecture.",
            "best_when": "Multiple pages compete for the same intent or rankings are unstable.",
            "cadence": "weekly or after major content changes",
            "impact": 4,
            "effort": 4,
            "automation_fit": "site-data",
            "cooldown_hours": 24,
            "goal_keywords": ["cannibalization", "overlap", "duplicate", "competing pages", "merge", "redirect", "intent conflict"],
            "stack": ["seo_intelligence_mcp", "gsc_mcp", "seo_memory_mcp"],
            "steps": [
                "Run cannibalization detection across the candidate URL set.",
                "Use GSC page-query data to confirm which URL currently wins and where confusion appears.",
                "Generate merge, redirect, and internal-link actions from the combined evidence.",
            ],
            "queue_template": queue_templates["cannibalization-cleanup"],
            "output": "Canonicalization and redirect action list.",
        },
        {
            "id": "indexation-war-room",
            "name": "Indexation War Room",
            "objective": "Diagnose why URLs are missing, delayed, or unstable in Google indexing.",
            "best_when": "Coverage issues, sitemap drift, or inspection failures are slowing growth.",
            "cadence": "daily when unstable, otherwise as needed",
            "impact": 5,
            "effort": 4,
            "automation_fit": "site-data",
            "cooldown_hours": 8,
            "goal_keywords": ["indexing", "coverage", "inspect", "sitemap", "robots", "not indexed", "crawl issue", "indexation"],
            "stack": ["gsc_mcp", "rust_seo_mcp", "seo_memory_mcp"],
            "steps": [
                "Inspect single URLs or batches with GSC MCP.",
                "Use the Rust SEO MCP for crawl, robots, schema, sitemap, or CWV checks.",
                "Use SEO Memory MCP to translate findings into an escalation-ready plan.",
            ],
            "queue_template": queue_templates["indexation-war-room"],
            "output": "Indexation diagnosis with fix order.",
        },
        {
            "id": "content-gap-to-brief",
            "name": "Content Gap to Brief",
            "objective": "Convert a target keyword or topic into a brief grounded in local knowledge and SERP analysis.",
            "best_when": "You need net-new content but want it aligned to intent and current search behavior.",
            "cadence": "daily editorial planning",
            "impact": 4,
            "effort": 3,
            "automation_fit": "topic",
            "cooldown_hours": 12,
            "goal_keywords": ["content brief", "keyword", "topic", "article", "landing page", "brief", "content gap", "outline"],
            "stack": ["seo_intelligence_mcp", "seo_memory_mcp", "seo_elite_knowledge"],
            "steps": [
                "Run content-gap and intent analysis for the topic.",
                "Route the task through SEO Memory MCP to pick the right pack and supporting canon.",
                "Pull fresh local-source context from SEO Elite before finalizing the brief.",
            ],
            "queue_template": queue_templates["content-gap-to-brief"],
            "output": "Tighter content brief with evidence and structure.",
        },
        {
            "id": "technical-audit-sprint",
            "name": "Technical Audit Sprint",
            "objective": "Run a fast technical pass using the strongest local audit primitives you already have.",
            "best_when": "You need crawl, CWV, schema, or redirect intelligence quickly.",
            "cadence": "daily or incident-driven",
            "impact": 4,
            "effort": 4,
            "automation_fit": "site-data",
            "cooldown_hours": 10,
            "goal_keywords": ["technical audit", "schema", "cwv", "core web vitals", "redirect", "internal links", "crawl", "audit"],
            "stack": ["rust_seo_mcp", "seo_intelligence_mcp", "seo_memory_mcp"],
            "steps": [
                "Use the Rust SEO MCP for crawl, schema, CWV, and sitemap checks.",
                "Use SEO Intelligence MCP for E-E-A-T, redirects, and internal-link opportunities.",
                "Use SEO Memory MCP to turn the findings into a reusable fix plan.",
            ],
            "queue_template": queue_templates["technical-audit-sprint"],
            "output": "Technical issue queue with next actions.",
        },
    ]


def render_components_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# Local SEO Stack",
        "",
        f"Generated: {payload['generated_at']}",
        "",
    ]
    for component in payload["components"]:
        lines.extend(
            [
                f"## {component['label']}",
                f"- id: `{component['id']}`",
                f"- kind: `{component['kind']}`",
                f"- status: `{component['status']}`",
                f"- summary: {component['summary']}",
                f"- command: `{component['command']}`",
            ]
        )
        if component["counts"]:
            count_text = ", ".join(f"{key}={value}" for key, value in component["counts"].items())
            lines.append(f"- counts: {count_text}")
        if component["tools"]:
            lines.append(f"- tools: {', '.join(component['tools'][:12])}")
        if component["paths"]:
            lines.append("- paths:")
            lines.extend(f"  - `{path}`" for path in component["paths"])
        lines.append("")
    return "\n".join(lines)


def render_workflows_markdown(payload: Dict[str, Any]) -> str:
    lines = [
        "# Local SEO Workflows",
        "",
        f"Generated: {payload['generated_at']}",
        "",
    ]
    for workflow in payload["workflows"]:
        lines.extend(
            [
                f"## {workflow['name']}",
                f"- id: `{workflow['id']}`",
                f"- objective: {workflow['objective']}",
                f"- best when: {workflow['best_when']}",
                f"- cadence: {workflow['cadence']}",
                f"- impact / effort: `{workflow['impact']}` / `{workflow['effort']}`",
                f"- automation fit: `{workflow['automation_fit']}`",
                f"- cooldown: `{workflow['cooldown_hours']}`h",
                f"- keywords: {', '.join(workflow['goal_keywords'])}",
                f"- stack: {', '.join(workflow['stack'])}",
                "- steps:",
            ]
        )
        lines.extend(f"  {idx}. {step}" for idx, step in enumerate(workflow["steps"], start=1))
        if workflow.get("queue_template"):
            lines.append("- execution queue:")
            lines.extend(
                f"  - [{task['priority']}] {task['title']} ({task['owner']})"
                for task in workflow["queue_template"]
            )
        lines.append(f"- output: {workflow['output']}")
        lines.append("")
    return "\n".join(lines)


def refresh_local_seo_stack(workspace: Path) -> Dict[str, Any]:
    paths = StackPaths(workspace=workspace)
    components = build_components(paths)
    workflows = build_workflows(components)

    payload = {
        "generated_at": now_utc_iso(),
        "components": components,
        "workflows": workflows,
    }

    capabilities_dir = workspace / "automation" / "capabilities"
    capabilities_dir.mkdir(parents=True, exist_ok=True)

    stack_json = capabilities_dir / "local-stack.json"
    stack_md = capabilities_dir / "local-stack.md"
    workflows_json = capabilities_dir / "workflows.json"
    workflows_md = capabilities_dir / "workflows.md"

    stack_json.write_text(json.dumps({"generated_at": payload["generated_at"], "components": components}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    stack_md.write_text(render_components_markdown(payload), encoding="utf-8")
    workflows_json.write_text(json.dumps({"generated_at": payload["generated_at"], "workflows": workflows}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    workflows_md.write_text(render_workflows_markdown(payload), encoding="utf-8")

    return {
        "generated_at": payload["generated_at"],
        "component_count": len(components),
        "workflow_count": len(workflows),
        "stack_json": str(stack_json),
        "stack_markdown": str(stack_md),
        "workflows_json": str(workflows_json),
        "workflows_markdown": str(workflows_md),
    }
