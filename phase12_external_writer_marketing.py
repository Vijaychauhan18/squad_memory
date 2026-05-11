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


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_CONFIG = BASE / "knowledge_sources_writer_marketing.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE12_DIR = BASE / "ingest" / "phase12"
DEFAULT_DB_PATH = BASE / "squad_memory.db"
TODAY = date(2026, 3, 20)
PHASE12_BEGIN = "<!-- phase12:begin -->"
PHASE12_END = "<!-- phase12:end -->"
CONFIDENCE_WEIGHTS = {"high": 1.0, "medium": 0.7, "low": 0.4, "": 0.5}

DOMAIN_CONFIG: Dict[str, Dict[str, Any]] = {
    "writer": {
        "label": "Writer",
        "router": "MEMORY.md",
        "operating_canon": "memory/writer-operating-canon-2026.md",
        "external_canon_filename": "writer-external-source-canon-2026.md",
        "summary_note": "live-external-source-monitor.md",
        "topic": "writer_external_sources",
        "intent": "monitoring, research, writing_examples, editorial_patterns",
        "role": "writer, plankton, pinchy, current",
        "use_for": "fresh_examples, source_selection, editorial_monitoring",
        "avoid_for": "seo_strategy, final_copy_without_core_workflow",
        "canonical_group": "Writer external source canon",
        "bundle_roles": ["Plankton", "Pinchy", "Current"],
        "research_hints": {"recent", "fresh", "examples", "example", "research", "editorial", "writing", "voice", "hooks", "swipe", "monitoring", "sources"},
        "consensus": [
            "Fresh external writing sources are best used for examples, framing, and editorial pattern detection, not as a replacement for the core writing workflow.",
            "Hooks, clarity, structure, and voice keep reappearing as the durable craft layer across strong writing sources.",
        ],
        "tension": [
            "The main tradeoff is originality versus imitation: external examples are useful for pattern recognition, but direct copycat writing weakens the output fast.",
        ],
        "action": "Start with the writer operating canon for the workflow, then use this external canon for fresh examples, message framing, and editorial pattern checks.",
    },
    "marketing": {
        "label": "Marketing",
        "router": "MEMORY.md",
        "operating_canon": "memory/marketing-operating-canon-2026.md",
        "external_canon_filename": "marketing-external-source-canon-2026.md",
        "summary_note": "live-external-source-monitor.md",
        "topic": "marketing_external_sources",
        "intent": "monitoring, research, distribution_examples, campaign_patterns",
        "role": "marketing, current, charles, pinchy",
        "use_for": "fresh_examples, source_selection, marketing_monitoring",
        "avoid_for": "technical_seo, product_claims_without_verification",
        "canonical_group": "Marketing external source canon",
        "bundle_roles": ["Current", "Charles", "Pinchy"],
        "research_hints": {"recent", "fresh", "examples", "example", "research", "distribution", "launch", "social", "channel", "campaign", "monitoring", "sources"},
        "consensus": [
            "Fresh marketing sources matter most for channel shifts, campaign examples, and distribution ideas, not for replacing the core marketing operating system.",
            "The strongest sources keep reinforcing distribution, adaptation, and audience fit over one-size-fits-all posting.",
        ],
        "tension": [
            "The main tradeoff is novelty versus repeatability: fresh tactics help, but the durable gains still come from consistent rollout, measurement, and platform fit.",
        ],
        "action": "Start with the marketing operating canon for the system, then use this external canon for fresh platform moves, campaign examples, and distribution experiments.",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 12 external source ingestion and fusion for writer and marketing")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase12-dir", default=str(DEFAULT_PHASE12_DIR))
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


def parse_date(text: str) -> date | None:
    raw = str(text or "").strip()[:10]
    if not raw:
        return None
    try:
        return date.fromisoformat(raw)
    except ValueError:
        return None


def confidence_score(sources: Sequence[Dict[str, Any]]) -> float:
    if not sources:
        return 0.0
    total = 0.0
    for source in sources:
        total += CONFIDENCE_WEIGHTS.get(str(source.get("confidence", "")).strip().lower(), 0.5)
    avg = total / len(sources)
    return round(min(0.5 + avg * 0.35 + len(sources) * 0.04, 1.0), 4)


def confidence_label(score: float) -> str:
    if score >= 0.82:
        return "high"
    if score >= 0.62:
        return "medium"
    return "low"


def freshness_score(results: Sequence[Dict[str, Any]]) -> float:
    dates = [parse_date(result.get("latest_published", "")) for result in results]
    parsed = [item for item in dates if item is not None]
    if not parsed:
        return 0.35
    latest = max(parsed)
    days_old = max((TODAY - latest).days, 0)
    if days_old <= 14:
        return 1.0
    if days_old <= 45:
        return 0.85
    if days_old <= 120:
        return 0.65
    if days_old <= 240:
        return 0.45
    return 0.25


def freshness_label(score: float) -> str:
    if score >= 0.9:
        return "current"
    if score >= 0.7:
        return "recent"
    if score >= 0.45:
        return "aging"
    return "stale"


def build_domain_summary_note(domain: str, cfg: Dict[str, Any], results: Sequence[Dict[str, Any]], snapshot_hint: Path) -> str:
    ok_results = [result for result in results if result["status"] == "ok"]
    error_results = [result for result in results if result["status"] != "ok"]
    lines = [
        "---",
        "source: local phase12 external source ingest",
        f"title: {cfg['label']} External Source Monitor",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: phase12_external_sources, {domain}, monitoring, freshness",
        f"topic: {cfg['topic']}",
        f"intent: {cfg['intent']}",
        f"role: {cfg['role']}",
        "confidence: medium",
        "canonical: true",
        f"canonical_group: {cfg['label']} live source monitor",
        "use_for: freshness, source_selection, triage",
        "avoid_for: final_strategy_without_core_canon",
        "---",
        "",
        f"# {cfg['label']} External Source Monitor",
        "",
        f"This note is generated by Phase 12. Use it to spot fresh external-source activity for the {domain} domain before opening the domain external canon or source-specific canons.",
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
    domain_cfg = DOMAIN_CONFIG[domain]
    items = result.get("items", [])[:top_n]
    use_for = "fresh examples, source selection, pattern detection"
    if domain == "marketing":
        use_for = "fresh examples, source selection, campaign and channel pattern detection"
    lines = [
        "---",
        f"source: {source_cfg.get('homepage', '')}",
        f"title: Live Source Canon - {source_cfg['name']}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: live_source_canon, phase12_external_sources, {domain}, {source_cfg['slug']}",
        f"topic: {source_cfg.get('topic', domain_cfg['topic'])}",
        f"intent: {', '.join(source_cfg.get('intent', []))}",
        f"role: {', '.join(source_cfg.get('roles', []))}",
        f"confidence: {source_cfg.get('confidence', 'medium')}",
        "canonical: true",
        f"canonical_group: {domain_cfg['label']} live source canon",
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
            f"- Pull one reusable pattern, example, or channel shift before using the source in final advice.",
            f"- Promote a durable note only if the update changes how the squad should write, distribute, or frame the work.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def latest_source_signal(result: Dict[str, Any]) -> str:
    items = result.get("items", [])
    if items:
        item = items[0]
        return f"{item.get('title', 'Untitled')} ({item.get('published', 'unknown date')})"
    if result["status"] != "ok":
        return f"Feed fetch error: {result.get('error', 'unknown error')}"
    return "No fresh items parsed."


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
                "source": "phase12_external_sources",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": f"phase12, {domain}, external sources, canon, squad",
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
    lines.append("2. Open this external canon when the task needs fresh examples, recent patterns, or source-aware research.")
    for idx, result in enumerate(source_rows, start=3):
        lines.append(f"{idx}. Open `memory/live-source-canon-{result['slug']}.md` when the task needs source-specific context from {result['name']}.")
    lines.extend(["", "## Team Use"])
    lines.append(f"- **{cfg['label']} specialist**: Use this canon for fresh source monitoring without losing the base operating system.")
    lines.append("- **Pinchy**: Use this canon when the task explicitly needs fresh examples, recent patterns, or source-backed external research.")
    if domain == "marketing":
        lines.append("- **Charles**: Use this canon when platform changes or campaign examples matter more than generic posting advice.")
    else:
        lines.append("- **Current**: Use this canon when writing tasks need fresh message framing or examples before distribution work starts.")
    return "\n".join(lines).rstrip() + "\n"


def build_phase12_block(evidence: Dict[str, Any]) -> str:
    lines = [
        "## Phase 12 External Source Fusion",
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


def replace_phase12_block(body: str, block: str) -> str:
    import re

    managed = f"{PHASE12_BEGIN}\n{block.rstrip()}\n{PHASE12_END}"
    pattern = re.compile(r"\n?<!-- phase12:begin -->.*?<!-- phase12:end -->\n?", re.DOTALL)
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
        "source: local phase12 writer-marketing external sources",
        "title: Writer Marketing External Sources Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase12_external_sources, writer, marketing, canon, monitoring",
        "topic: writer_marketing_external_sources",
        "intent: maintenance, monitoring, canon_fusion",
        "role: pinchy, writer, marketing, charles",
        "confidence: high",
        "canonical: false",
        "canonical_group: Writer marketing external source report",
        "use_for: source_monitoring, phase12_reporting",
        "avoid_for: seo_strategy",
        "---",
        "",
        "# Writer Marketing External Sources Report",
        "",
    ]
    for result in domain_results:
        lines.extend(
            [
                f"## {result['domain'].title()}",
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


def run_domain(domain: str, sources: Sequence[Dict[str, Any]], skills_root: Path, phase12_dir: Path, top_n: int) -> Dict[str, Any]:
    cfg = DOMAIN_CONFIG[domain]
    memory_root = skills_root / domain / "memory"
    memory_root.mkdir(parents=True, exist_ok=True)
    router_path = skills_root / domain / cfg["router"]
    operating_canon_path = skills_root / domain / cfg["operating_canon"]
    external_canon_path = memory_root / cfg["external_canon_filename"]
    summary_path = memory_root / cfg["summary_note"]

    snapshot_dir = phase12_dir / "raw" / domain
    runs_dir = phase12_dir / "runs" / domain
    state_path = phase12_dir / "state" / f"{domain}.json"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)
    state = load_json(state_path, {"generated_at": "", "sources": {}})
    now = datetime.now(timezone.utc)

    results: List[Dict[str, Any]] = []
    for source_cfg in sources:
        fetch_result = fetch_source_feed(source_cfg, snapshot_dir, now)
        items = fetch_result["items"]
        fetched_from = fetch_result["fetched_from"]
        channel_title = fetch_result["channel_title"]
        snapshot_path = fetch_result["snapshot_path"]
        last_error = fetch_result["error"]

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
            "channel_title": channel_title,
            "item_count": len(items),
            "new_item_count": new_item_count,
            "latest_published": latest_published(items),
            "snapshot_path": snapshot_path,
            "items": items,
            "error": last_error if not fetched_from else "",
            "attempted_urls": fetch_result.get("attempted_urls", []),
            "discovered_urls": fetch_result.get("discovered_urls", []),
            "note_filename": note_filename(source_cfg),
        }

        note_text = build_source_note(source_cfg, result, top_n)
        (memory_root / result["note_filename"]).write_text(note_text)
        result["note_path"] = str(memory_root / result["note_filename"])

        canon_filename = f"live-source-canon-{source_cfg['slug']}.md"
        canon_text = build_source_canon_note(domain, source_cfg, result, top_n)
        (memory_root / canon_filename).write_text(canon_text)
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
            "last_snapshot_path": snapshot_path,
            "last_note_path": result["note_path"],
            "last_canon_path": result["canon_path"],
            "seen_ids": merge_seen_ids(current_ids, previous_seen),
        }

    summary_path.write_text(build_domain_summary_note(domain, cfg, results, snapshot_dir))
    state["generated_at"] = now.isoformat()
    write_json(state_path, state)

    external_canon_text = build_external_canon(domain, cfg, results)
    external_canon_changed = write_note(external_canon_path, external_canon_text)

    router_changed = replace_canonical_notes_block(router_path, cfg["external_canon_filename"])
    bundle_changes: List[str] = []
    for role_name in cfg["bundle_roles"]:
        if replace_bundle_block(router_path, role_name, cfg["external_canon_filename"]):
            bundle_changes.append(role_name)

    external_canon_rel = f"{domain}/memory/{cfg['external_canon_filename']}"
    evidence = domain_evidence(domain, cfg, results, external_canon_rel)
    ledger_path = phase12_dir / f"{domain}_external_evidence_ledger.json"
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
        lambda body, evidence=evidence: replace_phase12_block(body, build_phase12_block(evidence)),
    )

    return {
        "domain": domain,
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


def run(skills_root: Path, config_path: Path, phase12_dir: Path, db_path: Path, top_n: int, build_db: bool) -> Dict[str, Any]:
    config = load_config(config_path)
    phase12_dir.mkdir(parents=True, exist_ok=True)
    grouped = select_domain_sources(config)
    domain_results = [run_domain(domain, grouped.get(domain, []), skills_root, phase12_dir, top_n) for domain in DOMAIN_CONFIG]

    report_path = phase12_dir / "writer_marketing_external_sources_report.md"
    report_path.write_text(build_report(domain_results))

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
        "phase12_dir": str(phase12_dir),
        "config_path": str(config_path),
        "report_path": str(report_path),
        "domains": domain_results,
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase12_dir / f"phase12-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase12_dir / "latest.json", result)
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
        phase12_dir=Path(args.phase12_dir),
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
