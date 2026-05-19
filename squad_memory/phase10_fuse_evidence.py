#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from phase9_merge_summaries import (
    NoteDoc,
    collect_notes,
    extract_core_concept,
    parse_frontmatter,
    write_note_body,
)


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE7_REGISTRY = BASE / "ingest" / "phase7" / "canonical_registry.json"
DEFAULT_PHASE10_DIR = BASE / "ingest" / "phase10"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

PHASE10_BEGIN = "<!-- phase10:begin -->"
PHASE10_END = "<!-- phase10:end -->"
EVIDENCE_LEDGER_PATH = DEFAULT_PHASE10_DIR / "evidence_ledger.json"
TODAY = date(2026, 3, 20)

SOURCE_LABELS = {
    "ahrefs": "Ahrefs",
    "dejan": "DEJAN",
    "hobo": "Hobo",
    "google": "Google",
    "gsqi": "GSQi",
    "ipullrank": "iPullRank",
    "jono": "Jono",
}

CONFIDENCE_WEIGHTS = {"high": 1.0, "medium": 0.7, "low": 0.4, "": 0.5}

TOPIC_TENSIONS = {
    "ai_visibility": "Rankings still help, but multiple sources treat mentions, citations, and answer-layer selection as separate systems.",
    "ai_overviews": "Visibility can increase while clicks contract, so citation wins and traffic wins should not be treated as the same outcome.",
    "aio_click_loss": "Some sources frame AIOs as brand exposure, while others emphasize the direct CTR compression on informational SEO.",
    "brand_mentions": "Entity mentions and backlinks overlap, but the stronger sources here treat broader off-site presence as more important than links alone.",
    "brand_visibility": "Brand consistency work looks like messaging on the surface, but the evidence cluster treats it as a search and recommendation system input.",
    "ai_reverse_engineering": "Platform behavior changes quickly, so reverse-engineering notes are powerful but should be checked against fresh source behavior before making hard bets.",
    "quality_systems": "Fresh feature launches can be noisy; leak-system notes are stronger for durable interpretation than product UI changes alone.",
    "document_quality_system": "Quality scoring appears systemic, but no single leaked field should be treated as a complete ranking explanation on its own.",
    "site_trust_system": "Human-quality framing and machine-quality scoring reinforce each other, but neither should be read as a standalone ranking recipe.",
    "technical_architecture": "Technical health remains necessary, but the supporting notes here do not support treating it as sufficient on its own.",
}

TOPIC_ACTIONS = {
    "ai_visibility": "Use this canon for AI visibility audits, then open supporting notes only for measurement or citation-specific diagnostics.",
    "ai_overviews": "Use this canon when separating citation strategy from click strategy on informational SERPs.",
    "aio_click_loss": "Use this canon to model traffic compression, then pair it with brand-demand or citation notes if the task is broader than CTR loss.",
    "brand_mentions": "Use this canon when the question is off-site presence, entity mentions, or visibility beyond rankings.",
    "brand_visibility": "Use this canon when aligning SEO, messaging, and entity positioning across site and off-site surfaces.",
    "ai_reverse_engineering": "Use this canon first for AI Mode, fan-out, grounding, and selection questions before opening raw reverse-engineering notes.",
    "click_behavior_systems": "Use this canon when the task is about click satisfaction, interaction signals, or post-click ranking mechanics.",
    "document_quality_system": "Use this canon when the task is page quality, document modeling, or quality-system interpretation from the leaks.",
    "site_trust_system": "Use this canon when the task is trust, rater-adjacent quality systems, or E-E-A-T style audits.",
    "technical_architecture": "Use this canon when the question is crawlability, rendering, or structural technical constraints affecting search systems.",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 10 cross-source evidence fusion")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase7-registry", default=str(DEFAULT_PHASE7_REGISTRY))
    parser.add_argument("--phase10-dir", default=str(DEFAULT_PHASE10_DIR))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true", help="Rebuild squad_memory after evidence fusion changes")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")


def extract_note_date(note: NoteDoc) -> date | None:
    text = note.meta.get("published", "") or note.meta.get("approved_on", "") or note.meta.get("scraped", "")
    text = text.strip()[:10]
    if not text:
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def freshness_score(notes: List[NoteDoc]) -> float:
    dates = [d for d in (extract_note_date(note) for note in notes) if d is not None]
    if not dates:
        return 0.4
    latest = max(dates)
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


def evidence_confidence(notes: List[NoteDoc]) -> float:
    if not notes:
        return 0.0
    source_count = len({note.source_slug for note in notes})
    avg_conf = sum(CONFIDENCE_WEIGHTS.get(note.meta.get("confidence", "").strip().lower(), 0.5) for note in notes) / len(notes)
    score = 0.35 + min(source_count * 0.12, 0.36) + min(len(notes) * 0.05, 0.25) + avg_conf * 0.12
    return round(min(score, 1.0), 4)


def confidence_label(score: float) -> str:
    if score >= 0.82:
        return "high"
    if score >= 0.62:
        return "medium"
    return "low"


def select_source_notes(topic_notes: List[NoteDoc]) -> List[Tuple[str, NoteDoc]]:
    by_source: Dict[str, List[NoteDoc]] = {}
    for note in topic_notes:
        by_source.setdefault(note.source_slug, []).append(note)
    selected: List[Tuple[str, NoteDoc]] = []
    for source, notes in by_source.items():
        ordered = sorted(
            notes,
            key=lambda note: (
                1 if note.meta.get("canonical", "").strip().lower() in {"true", "yes", "1"} else 0,
                CONFIDENCE_WEIGHTS.get(note.meta.get("confidence", "").strip().lower(), 0.5),
                note.filename,
            ),
            reverse=True,
        )
        selected.append((source, ordered[0]))
    selected.sort(key=lambda item: (item[0] != "ahrefs", item[0] != "dejan", item[0] != "hobo", item[0]))
    return selected[:4]


def recurring_signals(topic_notes: List[NoteDoc]) -> List[str]:
    counts: Counter[str] = Counter()
    for note in topic_notes:
        raw = note.meta.get("tags", "")
        for part in raw.split(","):
            tag = part.strip().lower()
            if not tag:
                continue
            if tag in {"seo", "google", "search", "ai", "durable_note", "live_pipeline_promoted"}:
                continue
            counts[tag] += 1
    return [tag for tag, count in counts.most_common(4) if count >= 2]


def default_consensus(topic: str, signals: List[str], sources: List[str]) -> List[str]:
    human = topic.replace("_", " ")
    lines = [f"Sources converge that `{human}` should be treated as a repeatable operating concern, not a one-off tactic."]
    if signals:
        lines.append(f"Recurring signals across the evidence set: {', '.join(signals[:3])}.")
    if len(sources) >= 2:
        lines.append(f"This topic is reinforced by {len(sources)} distinct source perspectives, which makes the canonical note safer to use as the default planning baseline.")
    return lines


def fusion_consensus(topic: str, signals: List[str]) -> List[str]:
    custom: Dict[str, List[str]] = {
        "ai_visibility": [
            "The strongest sources agree that AI visibility is broader than rankings and should be tracked through mentions, citations, and topic association.",
            "Search strength still matters, but answer-layer formatting and off-site representation materially affect whether brands get surfaced.",
        ],
        "ai_overviews": [
            "The evidence set agrees that AI Overviews change informational SERP economics and should be modeled separately from classic blue-link rankings.",
            "Citation opportunity and traffic retention are now different goals, even when the same query triggers both.",
        ],
        "brand_mentions": [
            "The evidence set converges on off-site brand presence as a durable discovery signal, not just a PR side effect.",
            "Mentions, reputation, and third-party presence shape visibility even when the website itself is technically sound.",
        ],
        "document_quality_system": [
            "The leak-oriented sources agree that document quality is modeled systemically rather than through one simple page-level factor.",
            "Quality signals cluster around effort, structure, and page-level scoring rather than isolated keyword tuning.",
        ],
        "ai_reverse_engineering": [
            "The strongest notes agree that AI answer selection depends on retrieval fit, grounding, and sub-query expansion, not only rank position.",
            "Reverse-engineering work is most useful when it explains why a page is selected, not just whether it ranks.",
        ],
    }
    if topic in custom:
        lines = list(custom[topic])
        if signals:
            lines.append(f"Recurring source signals: {', '.join(signals[:3])}.")
        return lines
    return default_consensus(topic, signals, [])


def tension_lines(topic: str, sources: List[str]) -> List[str]:
    tension = TOPIC_TENSIONS.get(topic, "")
    if not tension:
        return ["No strong source conflict stands out in the current evidence set; the supporting notes mostly add nuance rather than contradict the primary canon."]
    if len(sources) < 2:
        return [f"{tension} Current evidence is still source-concentrated, so treat it as directional rather than fully cross-validated."]
    return [tension]


def squad_action(topic: str) -> str:
    return TOPIC_ACTIONS.get(
        topic,
        "Use the canonical note first, then open supporting evidence only when you need source-specific proof, edge cases, or fresher platform behavior.",
    )


def replace_managed_block(body: str, block: str) -> str:
    managed = f"{PHASE10_BEGIN}\n{block.rstrip()}\n{PHASE10_END}"
    import re

    pattern = re.compile(r"\n?<!-- phase10:begin -->.*?<!-- phase10:end -->\n?", re.DOTALL)
    if pattern.search(body):
        updated = pattern.sub("\n\n" + managed + "\n", body).rstrip() + "\n"
        return updated
    return body.rstrip() + "\n\n" + managed + "\n"


def build_fusion_block(topic: str, topic_entry: Dict[str, Any], source_notes: List[Tuple[str, NoteDoc]], evidence: Dict[str, Any]) -> str:
    lines = [
        "## Evidence Fusion",
        "",
        f"Evidence confidence: {evidence['confidence_label']}",
        f"Freshness status: {evidence['freshness_label']}",
        f"Distinct sources: {', '.join(evidence['distinct_sources']) if evidence['distinct_sources'] else 'single-source'}",
        "",
        "### Cross-Source Signals",
    ]
    for source, note in source_notes:
        label = SOURCE_LABELS.get(source, source.title())
        summary = extract_core_concept(note.body) or note.title
        lines.append(f"- **{label}**: {summary.rstrip('.')}.")
    if not source_notes:
        lines.append("- No source signals were available for this topic in the current ledger.")

    lines.extend(["", "### Consensus"])
    for row in evidence["consensus"]:
        lines.append(f"- {row}")

    lines.extend(["", "### Tension / Caveat"])
    for row in evidence["tension"]:
        lines.append(f"- {row}")

    lines.extend(["", "### Squad Action", f"- {evidence['squad_action']}"])
    return "\n".join(lines)


def build_topic_evidence(topic: str, topic_entry: Dict[str, Any], notes: Dict[str, NoteDoc]) -> Dict[str, Any]:
    paths = [topic_entry["primary_path"], *topic_entry.get("merge_candidate_paths", []), *topic_entry.get("supporting_paths", [])]
    topic_notes = [notes[path] for path in paths if path in notes]
    distinct_sources = sorted({SOURCE_LABELS.get(note.source_slug, note.source_slug.title()) for note in topic_notes if note.source_slug})
    evidence_conf = evidence_confidence(topic_notes)
    fresh_score = freshness_score(topic_notes)
    source_notes = select_source_notes(topic_notes)
    signals = recurring_signals(topic_notes)
    consensus = fusion_consensus(topic, signals)
    if signals and topic not in {"ai_visibility", "ai_overviews", "brand_mentions", "document_quality_system", "ai_reverse_engineering"}:
        consensus = default_consensus(topic, signals, distinct_sources)
    tension = tension_lines(topic, [source for source, _ in source_notes])
    return {
        "topic": topic,
        "primary_path": topic_entry["primary_path"],
        "evidence_paths": paths,
        "distinct_sources": distinct_sources,
        "source_count": len(distinct_sources),
        "evidence_count": len(topic_notes),
        "merge_candidate_count": len(topic_entry.get("merge_candidate_paths", [])),
        "supporting_count": len(topic_entry.get("supporting_paths", [])),
        "freshness_score": fresh_score,
        "freshness_label": freshness_label(fresh_score),
        "confidence_score": evidence_conf,
        "confidence_label": confidence_label(evidence_conf),
        "consensus": consensus,
        "tension": tension,
        "squad_action": squad_action(topic),
        "source_signals": [
            {
                "source": SOURCE_LABELS.get(source, source.title()),
                "path": note.rel_path,
                "summary": extract_core_concept(note.body) or note.title,
            }
            for source, note in source_notes
        ],
    }


def build_evidence_ledger(output_dir: Path, registry: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Tuple[str, Dict[str, Any]]]]:
    notes = collect_notes(output_dir)
    topic_rows: List[Tuple[str, Dict[str, Any]]] = []
    for entry in registry.get("topics", []):
        if entry.get("topic_status") != "healthy":
            continue
        primary_path = str(entry.get("primary_path", "")).strip()
        if not primary_path:
            continue
        topic = str(entry.get("topic", "")).strip()
        if not topic:
            continue
        evidence = build_topic_evidence(topic, entry, notes)
        topic_rows.append((topic, evidence))
    ledger = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase": 10,
        "topics": {topic: payload for topic, payload in topic_rows},
        "primary_paths": {payload["primary_path"]: payload for _, payload in topic_rows},
    }
    return ledger, topic_rows


def refresh_fusion_blocks(output_dir: Path, topic_rows: List[Tuple[str, Dict[str, Any]]]) -> List[Dict[str, Any]]:
    notes = collect_notes(output_dir)
    updates: List[Dict[str, Any]] = []
    for topic, evidence in topic_rows:
        primary_path = evidence["primary_path"]
        note = notes.get(primary_path)
        if note is None:
            continue
        topic_entry = {
            "primary_path": primary_path,
            "merge_candidate_paths": [path for path in evidence["evidence_paths"] if path != primary_path][: evidence["merge_candidate_count"]],
            "supporting_paths": [path for path in evidence["evidence_paths"] if path != primary_path][evidence["merge_candidate_count"] :],
        }
        source_notes = []
        for item in evidence["source_signals"]:
            path = item["path"]
            if path in notes:
                source = notes[path].source_slug
                source_notes.append((source, notes[path]))
        block = build_fusion_block(topic, topic_entry, source_notes, evidence)
        changed = write_note_body(note.abs_path, lambda body, block=block: replace_managed_block(body, block))
        if changed:
            updates.append(
                {
                    "topic": topic,
                    "primary_path": primary_path,
                    "confidence_score": evidence["confidence_score"],
                    "source_count": evidence["source_count"],
                }
            )
    return updates


def build_report(ledger: Dict[str, Any], updates: List[Dict[str, Any]]) -> str:
    topics = list(ledger["topics"].values())
    strongest = sorted(topics, key=lambda item: (item["confidence_score"], item["freshness_score"]), reverse=True)[:10]
    disputed = [item for item in topics if not item["tension"][0].startswith("No strong source conflict")]
    stale = [item for item in topics if item["freshness_label"] in {"aging", "stale"}][:10]

    lines = [
        "---",
        "source: local phase10 evidence fusion",
        "title: Evidence Fusion Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase10_fuse_evidence, evidence_fusion, consensus, conflicts",
        "topic: evidence_fusion",
        "intent: maintenance, synthesis, evidence_weighting",
        "role: pinchy, researcher, seo",
        "confidence: high",
        "canonical: false",
        "canonical_group: Evidence fusion",
        "use_for: cross_source_review, canonical_weighting, evidence_audit",
        "avoid_for: direct_strategy_without_note_review",
        "---",
        "",
        "# Evidence Fusion Report",
        "",
        f"Topics fused: {len(topics)}",
        f"Canonical notes refreshed: {len(updates)}",
        "",
        "## Strongest Topics",
    ]
    if not strongest:
        lines.append("- No healthy canonical topics were available.")
    for item in strongest:
        lines.append(
            f"- `{item['topic']}` | confidence={item['confidence_label']} ({item['confidence_score']:.2f}) | freshness={item['freshness_label']} | sources={item['source_count']}"
        )

    lines.extend(["", "## Topics With Tension"])
    if not disputed:
        lines.append("- No major cross-source tensions detected in the current ledger.")
    for item in disputed[:12]:
        lines.append(f"- `{item['topic']}` | {item['tension'][0]}")

    lines.extend(["", "## Aging Topics"])
    if not stale:
        lines.append("- No aging topics detected in the current ledger.")
    for item in stale:
        lines.append(f"- `{item['topic']}` | freshness={item['freshness_label']} | sources={item['source_count']}")
    return "\n".join(lines) + "\n"


def run(output_dir: Path, phase7_registry: Path, phase10_dir: Path, skills_root: Path, db_path: Path, build_db: bool) -> Dict[str, Any]:
    phase10_dir.mkdir(parents=True, exist_ok=True)
    registry = load_json(phase7_registry, {"topics": []})
    ledger, topic_rows = build_evidence_ledger(output_dir, registry)
    ledger_path = phase10_dir / "evidence_ledger.json"
    write_json(ledger_path, ledger)
    updates = refresh_fusion_blocks(output_dir, topic_rows)

    build_result = None
    if build_db and updates:
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

    report_path = phase10_dir / "evidence_fusion_report.md"
    report_path.write_text(build_report(ledger, updates))
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase10_dir": str(phase10_dir),
        "ledger_path": str(ledger_path),
        "report_path": str(report_path),
        "topics_fused": len(topic_rows),
        "fusion_updates": updates,
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase10_dir / f"phase10-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase10_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Ledger: {result['ledger_path']}")
    print(f"Report: {result['report_path']}")
    print(f"Topics fused: {result['topics_fused']}")
    print(f"Canonical notes refreshed: {len(result['fusion_updates'])}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = run(
        output_dir=Path(args.output_dir),
        phase7_registry=Path(args.phase7_registry),
        phase10_dir=Path(args.phase10_dir),
        skills_root=Path(args.skills_root),
        db_path=Path(args.db_path),
        build_db=args.build_db,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
