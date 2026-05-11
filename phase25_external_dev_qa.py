#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence

from knowledge_ingest import (
    build_source_note,
    extract_item_id,
    fetch_source_feed,
    latest_published,
    load_config,
    merge_seen_ids,
    note_filename,
    write_json,
)
from phase11_bootstrap_writer_marketing import (
    build_frontmatter,
    replace_bundle_block,
    replace_canonical_notes_block,
    write_note,
    write_note_body,
)
from phase12_external_writer_marketing import (
    confidence_label,
    confidence_score,
    freshness_label,
    freshness_score,
    latest_source_signal,
)


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_CONFIG = BASE / "knowledge_sources_dev_qa.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE25_DIR = BASE / "ingest" / "phase25"
DEFAULT_DB_PATH = BASE / "squad_memory.db"
TODAY = date(2026, 3, 20)
PHASE25_BEGIN = "<!-- phase25:begin -->"
PHASE25_END = "<!-- phase25:end -->"

DOMAIN_CONFIG: Dict[str, Dict[str, Any]] = {
    "developer": {
        "label": "Developer",
        "router": "MEMORY.md",
        "operating_canon": "memory/developer-operating-canon-2026.md",
        "external_canon_filename": "developer-external-source-canon-2026.md",
        "summary_note": "live-external-source-monitor.md",
        "topic": "developer_external_sources",
        "intent": "monitoring, research, engineering_examples, tooling_changes, implementation_patterns",
        "role": "developer, developer-chitin, pinchy, reviewer, qa, devops",
        "use_for": "fresh_examples, source_selection, engineering_monitoring, implementation_research",
        "avoid_for": "shipping_decisions_without_repo_context, final_architecture_without_local_constraints",
        "canonical_group": "Developer external source canon",
        "bundle_roles": ["Chitin", "Barnacle", "Reef", "Pinchy"],
        "consensus": [
            "Fresh developer sources are best used for engineering patterns, tooling changes, and implementation examples, not for replacing the Chitin operating canon.",
            "The strongest engineering sources keep reinforcing small safe changes, explicit tests, and decision clarity over clever but fragile implementation moves.",
        ],
        "tension": [
            "The main tradeoff is novelty versus local fit: fresh engineering patterns are useful, but they should only influence the codebase after Chitin maps them back to current constraints.",
        ],
        "action": "Start with the developer operating canon for implementation work, then use this external canon for recent engineering patterns, tooling changes, and source-backed development research.",
    },
    "qa": {
        "label": "QA",
        "router": "MEMORY.md",
        "operating_canon": "memory/qa-operating-canon-2026.md",
        "external_canon_filename": "qa-external-source-canon-2026.md",
        "summary_note": "live-external-source-monitor.md",
        "topic": "qa_external_sources",
        "intent": "monitoring, research, testing_examples, tooling_changes, release_patterns",
        "role": "qa, qa-reef, pinchy, developer, reviewer, devops",
        "use_for": "fresh_examples, source_selection, qa_monitoring, testing_research",
        "avoid_for": "release_signoff_without_execution, product_truth_without_local_verification",
        "canonical_group": "QA external source canon",
        "bundle_roles": ["Reef", "Chitin", "Barnacle", "Pinchy", "Tide"],
        "consensus": [
            "Fresh QA sources are best used for testing patterns, framework changes, and release-check ideas, not for replacing the Reef operating canon.",
            "The strongest testing sources reinforce clear coverage strategy, reproducible automation, and evidence-backed release calls over shallow smoke-check theatre.",
        ],
        "tension": [
            "The main tradeoff is tool novelty versus dependable coverage: recent framework updates help, but the durable gains still come from disciplined test design and reproducible verification.",
        ],
        "action": "Start with the QA operating canon for validation work, then use this external canon for recent testing patterns, framework changes, and source-backed QA research.",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 25 external source ingestion and fusion for developer and QA")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase25-dir", default=str(DEFAULT_PHASE25_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def select_domain_sources(config: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    selected: Dict[str, List[Dict[str, Any]]] = {domain: [] for domain in DOMAIN_CONFIG}
    for source in config.get("sources", []):
        domain = str(source.get("domain", "")).strip().lower()
        if domain in selected and source.get("enabled", True) is not False:
            selected[domain].append(source)
    return selected


def build_domain_summary_note(domain: str, cfg: Dict[str, Any], results: Sequence[Dict[str, Any]], snapshot_hint: Path) -> str:
    ok_results = [result for result in results if result["status"] == "ok"]
    error_results = [result for result in results if result["status"] != "ok"]
    lines = [
        "---",
        f"source: local phase25 {domain} external source ingest",
        f"title: {cfg['label']} External Source Monitor",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: phase25_external_sources, {domain}, monitoring, freshness",
        f"topic: {cfg['topic']}",
        f"intent: {cfg['intent']}",
        f"role: {cfg['role']}",
        "confidence: medium",
        "canonical: true",
        f"canonical_group: {cfg['label']} live external monitor",
        "use_for: freshness, source_selection, triage",
        "avoid_for: final_strategy_without_core_canon",
        "---",
        "",
        f"# {cfg['label']} External Source Monitor",
        "",
        f"This note is generated by Phase 25. Use it to spot fresh external-source activity for the {domain} domain before opening the domain external canon or source-specific canons.",
        "",
        "## Health Summary",
        f"- Active sources: {len(results)}",
        f"- Healthy sources: {len(ok_results)}",
        f"- Failed sources: {len(error_results)}",
        "",
        "## Source Status",
    ]
    for result in results:
        if result["status"] == "ok":
            lines.append(
                f"- {result['name']}: ok | items={result['item_count']} | new={result['new_item_count']} | latest={result.get('latest_published') or 'unknown'} | note=`{result['note_filename']}`"
            )
        else:
            lines.append(f"- {result['name']}: error | {result.get('error', 'unknown error')}")
    lines.extend(["", "## Snapshot Notes"])
    for result in results:
        lines.append(f"- `{result['note_filename']}`")
    lines.extend(["", "## Storage", f"- Raw snapshots: `{snapshot_hint}`"])
    return "\n".join(lines).rstrip() + "\n"


def build_source_canon_note(domain: str, source_cfg: Dict[str, Any], result: Dict[str, Any], top_n: int) -> str:
    items = result.get("items", [])[:top_n]
    use_for = "fresh examples, engineering research, tooling monitoring" if domain == "developer" else "fresh examples, testing research, tooling monitoring"
    lines = [
        "---",
        f"source: {source_cfg.get('homepage', '')}",
        f"title: Live Source Canon - {source_cfg['name']}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: live_source_canon, phase25_external_sources, {domain}, {source_cfg['slug']}",
        f"topic: {source_cfg.get('topic', DOMAIN_CONFIG[domain]['topic'])}",
        f"intent: {', '.join(source_cfg.get('intent', []))}",
        f"role: {', '.join(source_cfg.get('roles', []))}",
        f"confidence: {source_cfg.get('confidence', 'medium')}",
        "canonical: true",
        f"canonical_group: {DOMAIN_CONFIG[domain]['label']} live source canon",
        f"use_for: {use_for}",
        "avoid_for: final_strategy_without_core_canon",
        "---",
        "",
        f"# Live Source Canon - {source_cfg['name']}",
        "",
        f"Raw source note: [{result['note_filename']}](./{result['note_filename']})",
        f"Homepage: {source_cfg.get('homepage', '')}",
        f"Source kind: {source_cfg.get('kind', 'publication')}",
        f"Latest published date: {result.get('latest_published') or 'unknown'}",
        f"New items since last run: {result.get('new_item_count', 0)}",
        "",
        "## Best Use",
        source_cfg.get("strength", "Use this source for fresh examples and source-specific context."),
        "",
        "## Latest Signals",
    ]
    if result["status"] != "ok" or not items:
        lines.append(f"- Feed status: {result['status']} | {result.get('error', 'no items parsed')}")
    else:
        for item in items:
            lines.append(f"- {item['published']} | [{item['title']}]({item['link']})")
    lines.extend(
        [
            "",
            "## Agent Checklist",
            f"- Use this source for freshness first, then map the signal back into the {domain} operating canon.",
            "- Pull one reusable pattern, tooling shift, or release-note implication before using the source in final advice.",
            "- Promote a durable note only if the update changes how the squad should implement, test, or verify work.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_external_canon(domain: str, cfg: Dict[str, Any], results: Sequence[Dict[str, Any]]) -> str:
    ok_results = [result for result in results if result["status"] == "ok"]
    error_results = [result for result in results if result["status"] != "ok"]
    source_rows = ok_results or list(results)
    lines = [
        build_frontmatter(
            {
                "title": f"{cfg['label']} External Source Canon 2026",
                "topic": cfg["topic"],
                "intent": cfg["intent"],
                "role": cfg["role"],
                "use_for": cfg["use_for"],
                "avoid_for": cfg["avoid_for"],
                "confidence": "high",
                "canonical": "true",
                "canonical_group": cfg["canonical_group"],
                "source": "phase25_external_sources",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": f"phase25, {domain}, external sources, canon, squad",
            }
        ).rstrip(),
        f"# {cfg['label']} External Source Canon 2026",
        "",
        "## Core Concept",
        cfg["consensus"][0] + " " + cfg["consensus"][1],
        "",
        "## Best Sources",
    ]
    for result in source_rows:
        lines.append(f"- **{result['name']}**: {result['strength']}. Latest signal: {latest_source_signal(result)}.")
    if error_results:
        lines.extend(["", "## Unavailable Sources"])
        for result in error_results:
            lines.append(f"- **{result['name']}**: {result.get('error', 'unknown error')}.")
    lines.extend(["", "## Workflow Map"])
    lines.append(f"1. Start with `memory/{Path(cfg['operating_canon']).name}` for the default {domain} workflow.")
    lines.append("2. Open this external canon when the task needs fresh examples, recent patterns, tooling changes, or source-aware research.")
    for idx, result in enumerate(source_rows, start=3):
        lines.append(f"{idx}. Open `memory/live-source-canon-{result['slug']}.md` when the task needs source-specific context from {result['name']}.")
    lines.extend(["", "## Team Use"])
    if domain == "developer":
        lines.append("- **Chitin**: Use this canon for recent engineering patterns and tooling shifts without dropping the core implementation workflow.")
        lines.append("- **Barnacle**: Use this canon when review advice benefits from broader engineering references or recent implementation patterns.")
        lines.append("- **Reef**: Use this canon when testing feedback needs fresh engineering context before asking Chitin for a change.")
    else:
        lines.append("- **Reef**: Use this canon for recent testing patterns, framework changes, and evidence-backed QA research.")
        lines.append("- **Chitin**: Use this canon when implementation plans depend on recent testing-tool behavior or release notes.")
        lines.append("- **Tide**: Use this canon when release gating or deployment checks depend on fresh test-framework changes.")
    lines.append("- **Pinchy**: Use this canon when the task explicitly needs fresh technical examples, tooling changes, or source-backed engineering research.")
    return "\n".join(lines).rstrip() + "\n"


def build_phase25_block(evidence: Dict[str, Any]) -> str:
    lines = [
        "## Phase 25 External Source Fusion",
        "",
        f"Evidence confidence: {evidence['confidence_label']}",
        f"Freshness status: {evidence['freshness_label']}",
        f"Distinct sources: {', '.join(evidence['distinct_sources']) if evidence['distinct_sources'] else 'none'}",
        "",
        "### Consensus",
    ]
    for row in evidence["consensus"]:
        lines.append(f"- {row}")
    lines.extend(["", "### Tension / Caveat"])
    for row in evidence["tension"]:
        lines.append(f"- {row}")
    lines.extend(["", "### Fresh Source Signals"])
    for item in evidence["source_signals"]:
        lines.append(f"- `{Path(item['path']).name}`: {item['summary']}")
    lines.extend(["", "### Squad Action", f"- {evidence['squad_action']}"])
    return "\n".join(lines)


def replace_phase25_block(body: str, block: str) -> str:
    import re

    managed = f"{PHASE25_BEGIN}\n{block.rstrip()}\n{PHASE25_END}"
    pattern = re.compile(r"\n?<!-- phase25:begin -->.*?<!-- phase25:end -->\n?", re.DOTALL)
    if pattern.search(body):
        return pattern.sub("\n\n" + managed + "\n", body).rstrip() + "\n"
    return body.rstrip() + "\n\n" + managed + "\n"


def domain_evidence(domain: str, cfg: Dict[str, Any], results: Sequence[Dict[str, Any]], canon_rel_path: str) -> Dict[str, Any]:
    confidence = confidence_score(results)
    freshness = freshness_score(results)
    distinct_sources = [result["name"] for result in results if result["status"] == "ok"]
    source_signals = [
        {
            "source": result["name"],
            "path": f"{domain}/memory/live-source-canon-{result['slug']}.md",
            "summary": latest_source_signal(result),
        }
        for result in results
    ]
    return {
        "topic": cfg["topic"],
        "domain": domain,
        "primary_path": canon_rel_path,
        "evidence_paths": [canon_rel_path, *[item["path"] for item in source_signals]],
        "distinct_sources": distinct_sources,
        "source_count": len(distinct_sources),
        "evidence_count": len(source_signals) + 1,
        "freshness_score": freshness,
        "freshness_label": freshness_label(freshness),
        "confidence_score": confidence,
        "confidence_label": confidence_label(confidence),
        "consensus": cfg["consensus"],
        "tension": cfg["tension"],
        "squad_action": cfg["action"],
        "source_signals": source_signals,
    }


def build_report(domain_results: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "---",
        "source: local phase25 developer-qa external sources",
        "title: Developer QA External Sources Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase25_external_sources, developer, qa, canon, monitoring",
        "topic: developer_qa_external_sources",
        "intent: maintenance, monitoring, canon_fusion",
        "role: pinchy, developer, qa, reviewer, devops",
        "confidence: high",
        "canonical: false",
        "canonical_group: Developer QA external source report",
        "use_for: source_monitoring, phase25_reporting",
        "avoid_for: seo_strategy",
        "---",
        "",
        "# Developer QA External Sources Report",
        "",
    ]
    for result in domain_results:
        label = result.get("label", result["domain"].title())
        lines.extend(
            [
                f"## {label}",
                f"- External canon: `{result['external_canon_path']}`",
                f"- Sources processed: {result['source_count']}",
                f"- Healthy sources: {result['ok_source_count']}",
                f"- Failed sources: {result['error_source_count']}",
                f"- Live snapshot notes: {result['live_note_count']}",
                f"- Source canons refreshed: {result['source_canon_count']}",
                f"- Router updated: {result['router_changed']}",
                f"- Bundles updated: {', '.join(result['bundle_changes']) if result['bundle_changes'] else 'none'}",
                f"- Operating canon updated: {result['operating_canon_changed']}",
                "",
            ]
        )
        if result["failed_sources"]:
            lines.append("### Failed Sources")
            for row in result["failed_sources"]:
                lines.append(f"- {row['name']}: {row['error']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def run_domain(domain: str, sources: Sequence[Dict[str, Any]], skills_root: Path, phase25_dir: Path, top_n: int) -> Dict[str, Any]:
    cfg = DOMAIN_CONFIG[domain]
    memory_root = skills_root / domain / "memory"
    memory_root.mkdir(parents=True, exist_ok=True)
    router_path = skills_root / domain / cfg["router"]
    operating_canon_path = skills_root / domain / cfg["operating_canon"]
    external_canon_path = memory_root / cfg["external_canon_filename"]
    summary_path = memory_root / cfg["summary_note"]

    snapshot_dir = phase25_dir / "raw" / domain
    state_path = phase25_dir / "state" / f"{domain}.json"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    state = load_json(state_path, {"generated_at": "", "sources": {}})
    now = datetime.now(timezone.utc)

    results: List[Dict[str, Any]] = []
    for source_cfg in sources:
        fetch_result = fetch_source_feed(source_cfg, snapshot_dir, now)
        items = fetch_result["items"]
        fetched_from = fetch_result["fetched_from"]
        previous = state.get("sources", {}).get(source_cfg["slug"], {})
        previous_seen = previous.get("seen_ids", [])
        current_ids = [extract_item_id(item) for item in items]
        previous_seen_set = set(previous_seen)
        new_item_count = len([item_id for item_id in current_ids if item_id and item_id not in previous_seen_set])

        result: Dict[str, Any] = {
            "domain": domain,
            "slug": source_cfg["slug"],
            "name": source_cfg["name"],
            "strength": source_cfg.get("strength", ""),
            "status": "ok" if fetched_from else "error",
            "fetched_from": fetched_from,
            "channel_title": fetch_result["channel_title"],
            "item_count": len(items),
            "new_item_count": new_item_count,
            "latest_published": latest_published(items),
            "snapshot_path": fetch_result["snapshot_path"],
            "items": items,
            "error": fetch_result["error"] if not fetched_from else "",
            "attempted_urls": fetch_result.get("attempted_urls", []),
            "discovered_urls": fetch_result.get("discovered_urls", []),
            "note_filename": note_filename(source_cfg),
        }

        note_text = build_source_note(source_cfg, result, top_n)
        (memory_root / result["note_filename"]).write_text(note_text, encoding="utf-8")
        result["note_path"] = str(memory_root / result["note_filename"])

        canon_filename = f"live-source-canon-{source_cfg['slug']}.md"
        canon_text = build_source_canon_note(domain, source_cfg, result, top_n)
        (memory_root / canon_filename).write_text(canon_text, encoding="utf-8")
        result["canon_filename"] = canon_filename
        result["canon_path"] = str(memory_root / canon_filename)
        results.append(result)

        state.setdefault("sources", {})[source_cfg["slug"]] = {
            "name": source_cfg["name"],
            "last_success_at": now.isoformat() if fetched_from else previous.get("last_success_at", ""),
            "last_status": result["status"],
            "latest_published": result["latest_published"],
            "last_item_count": len(items),
            "last_new_item_count": new_item_count,
            "last_snapshot_path": result["snapshot_path"],
            "last_note_path": result["note_path"],
            "last_canon_path": result["canon_path"],
            "seen_ids": merge_seen_ids(current_ids, previous_seen),
        }

    summary_path.write_text(build_domain_summary_note(domain, cfg, results, snapshot_dir), encoding="utf-8")
    state["generated_at"] = now.isoformat()
    write_json(state_path, state)

    external_canon_changed = write_note(external_canon_path, build_external_canon(domain, cfg, results))
    router_changed = replace_canonical_notes_block(router_path, cfg["external_canon_filename"])
    bundle_changes: List[str] = []
    for role_name in cfg["bundle_roles"]:
        if replace_bundle_block(router_path, role_name, cfg["external_canon_filename"]):
            bundle_changes.append(role_name)

    external_canon_rel = f"{domain}/memory/{cfg['external_canon_filename']}"
    evidence = domain_evidence(domain, cfg, results, external_canon_rel)
    ledger_path = phase25_dir / f"{domain}_external_evidence_ledger.json"
    write_json(
        ledger_path,
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "topics": {cfg["topic"]: evidence},
            "primary_paths": {external_canon_rel: evidence},
        },
    )

    operating_canon_changed = write_note_body(
        operating_canon_path,
        lambda body, evidence=evidence: replace_phase25_block(body, build_phase25_block(evidence)),
    )

    return {
        "domain": domain,
        "label": cfg["label"],
        "external_canon_path": external_canon_rel,
        "source_count": len(results),
        "ok_source_count": len([result for result in results if result["status"] == "ok"]),
        "error_source_count": len([result for result in results if result["status"] != "ok"]),
        "live_note_count": len(results),
        "source_canon_count": len(results),
        "router_changed": router_changed,
        "bundle_changes": bundle_changes,
        "operating_canon_changed": operating_canon_changed or external_canon_changed,
        "ledger_path": str(ledger_path),
        "summary_path": str(summary_path),
        "failed_sources": [
            {"name": result["name"], "error": result.get("error", "unknown error")}
            for result in results
            if result["status"] != "ok"
        ],
    }


def run(skills_root: Path, config_path: Path, phase25_dir: Path, db_path: Path, top_n: int, build_db: bool) -> Dict[str, Any]:
    config = load_config(config_path)
    phase25_dir.mkdir(parents=True, exist_ok=True)
    grouped = select_domain_sources(config)
    domain_results = [run_domain(domain, grouped.get(domain, []), skills_root, phase25_dir, top_n) for domain in DOMAIN_CONFIG]

    report_path = phase25_dir / "developer_qa_external_sources_report.md"
    report_path.write_text(build_report(domain_results), encoding="utf-8")

    build_result = None
    if build_db:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "build",
                "--root",
                str(skills_root),
                "--db",
                str(db_path),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            raise SystemExit(completed.returncode)
        build_result = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
        }

    result: Dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase25_dir": str(phase25_dir),
        "config_path": str(config_path),
        "report_path": str(report_path),
        "domains": domain_results,
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase25_dir / f"phase25-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase25_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    for item in result["domains"]:
        print(f"{item['domain']}: external_canon={item['external_canon_path']} sources={item['source_count']}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = run(
        skills_root=Path(args.skills_root),
        config_path=Path(args.config),
        phase25_dir=Path(args.phase25_dir),
        db_path=Path(args.db_path),
        top_n=args.top,
        build_db=args.build_db,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
