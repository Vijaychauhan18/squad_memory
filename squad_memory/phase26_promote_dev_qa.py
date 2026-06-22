#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from phase13_promote_writer_marketing import (
    ITEM_RE,
    FRONTMATTER_RE,
    HEADING_RE,
    ExistingNote,
    clean_summary,
    confidence_weight,
    durable_notes,
    extract_core_concept,
    load_json,
    meta_list,
    note_title,
    parse_date,
    parse_frontmatter,
    slugify,
    tokenize,
    write_json,
)


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE25 = BASE / "ingest" / "phase25" / "latest.json"
DEFAULT_PHASE26_DIR = BASE / "ingest" / "phase26"
DEFAULT_STATE = DEFAULT_PHASE26_DIR / "state.json"

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_+\-]{1,}")
LOW_SIGNAL_PATTERNS = [
    re.compile(r"\bweekly\b", re.IGNORECASE),
    re.compile(r"\brecap\b", re.IGNORECASE),
    re.compile(r"\broundup\b", re.IGNORECASE),
    re.compile(r"\bnews\b", re.IGNORECASE),
    re.compile(r"\bwebinar\b", re.IGNORECASE),
    re.compile(r"\bconference\b", re.IGNORECASE),
]

DOMAIN_CONFIG: Dict[str, Dict[str, Any]] = {
    "developer": {
        "label": "Developer",
        "high_signal_terms": {
            "refactor",
            "refactoring",
            "testing",
            "tests",
            "tdd",
            "architecture",
            "design",
            "implementation",
            "patterns",
            "maintainability",
            "tooling",
            "engineer",
            "engineering",
            "review",
            "performance",
            "reliability",
            "codebase",
        },
        "suggested_bundle": "Chitin Bundle",
    },
    "qa": {
        "label": "QA",
        "high_signal_terms": {
            "regression",
            "coverage",
            "matrix",
            "automation",
            "framework",
            "tooling",
            "test",
            "tests",
            "testing",
            "release",
            "verification",
            "repro",
            "browser",
            "e2e",
            "playwright",
            "cypress",
            "quality",
        },
        "suggested_bundle": "Reef Bundle",
    },
}

TOPIC_ROUTING: Dict[str, Dict[str, Dict[str, str]]] = {
    "developer": {
        "engineering_patterns": {
            "note": "memory/small-prs-and-safe-refactors.md",
            "reason": "This fits safe-change discipline, maintainability, and engineering pattern decisions.",
        },
        "engineering_systems": {
            "note": "memory/developer-operating-canon-2026.md",
            "reason": "This is broad enough to affect the main Chitin operating system rather than a single implementation note.",
        },
    },
    "qa": {
        "test_tooling": {
            "note": "memory/regression-gate-and-release-verdicts.md",
            "reason": "This belongs with release gates, tooling implications, and pass/fail confidence.",
        },
        "testing_patterns": {
            "note": "memory/test-matrix-and-edge-case-coverage.md",
            "reason": "This is primarily a testing-pattern and coverage-design signal.",
        },
    },
}


@dataclass
class Candidate:
    domain: str
    source_slug: str
    source_name: str
    source_topic: str
    source_confidence: str
    roles: List[str]
    intents: List[str]
    title: str
    link: str
    published: str
    summary: str
    score: float
    freshness: float
    overlap: float
    signal_strength: float
    draft_filename: str
    routing: Dict[str, str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 26 developer and QA durable promotion drafting")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase25-manifest", default=str(DEFAULT_PHASE25))
    parser.add_argument("--phase26-dir", default=str(DEFAULT_PHASE26_DIR))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--max-candidates", type=int, default=10)
    parser.add_argument("--per-domain", type=int, default=4)
    parser.add_argument("--per-source", type=int, default=1)
    parser.add_argument("--max-age-days", type=int, default=180)
    parser.add_argument("--min-score", type=float, default=0.5)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def max_overlap(tokens: set[str], notes: Sequence[ExistingNote]) -> float:
    if not tokens or not notes:
        return 0.0
    best = 0.0
    for note in notes:
        if not note.tokens:
            continue
        score = len(tokens & note.tokens) / max(len(tokens), 1)
        best = max(best, score)
    return round(best, 4)


def low_signal_penalty(title: str) -> float:
    for pattern in LOW_SIGNAL_PATTERNS:
        if pattern.search(title):
            return 0.2
    return 0.0


def parse_live_items(path: Path) -> Tuple[Dict[str, str], List[Tuple[str, str, str, str]]]:
    meta, body = parse_frontmatter(path.read_text())
    items: List[Tuple[str, str, str, str]] = []
    lines = body.splitlines()
    for index, raw in enumerate(lines):
        match = ITEM_RE.match(raw.strip())
        if not match:
            continue
        summary = ""
        if index + 1 < len(lines):
            candidate = lines[index + 1].strip()
            if candidate and not candidate.startswith("- "):
                summary = candidate
        items.append(
            (
                match.group("published").strip(),
                match.group("title").strip(),
                match.group("link").strip(),
                clean_summary(summary),
            )
        )
    return meta, items


def freshness_score(published: str, max_age_days: int) -> float:
    parsed = parse_date(published)
    if parsed is None:
        return 0.35
    days_old = max((date.today() - parsed).days, 0)
    if days_old > max_age_days:
        return 0.0
    ratio = max(0.0, 1.0 - (days_old / max_age_days))
    return round(0.35 + ratio * 0.65, 4)


def signal_strength(domain: str, title: str, summary: str) -> float:
    tokens = set(tokenize(f"{title}\n{summary}"))
    hits = len(tokens & DOMAIN_CONFIG[domain]["high_signal_terms"])
    return round(min(hits / 4.0, 1.0), 4)


def suggest_routing(domain: str, topic: str, title: str, summary: str) -> Dict[str, str]:
    mapping = TOPIC_ROUTING.get(domain, {}).get(topic)
    if mapping:
        note = mapping["note"]
        reason = mapping["reason"]
    else:
        tokens = set(tokenize(f"{title}\n{summary}"))
        if domain == "developer":
            if {"refactor", "refactoring", "maintainability", "design", "architecture"} & tokens:
                note = "memory/small-prs-and-safe-refactors.md"
                reason = "This is mainly about safe engineering patterns, refactoring discipline, or maintainability."
            elif {"bug", "bugs", "fix", "fixes", "regression"} & tokens:
                note = "memory/bug-reproduction-and-fix-workflow.md"
                reason = "This is closest to debugging and regression-safe implementation work."
            else:
                note = "memory/implementation-and-tdd-loop.md"
                reason = "This looks closest to implementation flow and test-backed coding practice."
        else:
            if {"release", "releases", "framework", "tooling", "playwright", "cypress"} & tokens:
                note = "memory/regression-gate-and-release-verdicts.md"
                reason = "This is a release-gate or test-tooling signal that belongs near release verdicts."
            elif {"matrix", "coverage", "edge", "boundary", "cases"} & tokens:
                note = "memory/test-matrix-and-edge-case-coverage.md"
                reason = "This is primarily about shaping test coverage and edge-case strategy."
            else:
                note = "memory/bug-report-quality-and-repro-discipline.md"
                reason = "This is best treated as a reproducibility and QA evidence-quality signal."
    return {
        "suggested_note": note,
        "suggested_bundle": DOMAIN_CONFIG[domain]["suggested_bundle"],
        "reason": reason,
    }


def score_candidate(
    domain: str,
    title: str,
    summary: str,
    published: str,
    confidence: str,
    notes: Sequence[ExistingNote],
    max_age_days: int,
) -> Tuple[float, float, float, float]:
    fresh = freshness_score(published, max_age_days)
    conf = confidence_weight(confidence)
    signal = signal_strength(domain, title, summary)
    tokens = set(tokenize(f"{title}\n{summary}"))
    overlap = max_overlap(tokens, notes)
    novelty = 1.0 - overlap
    score = (fresh * 0.3) + (conf * 0.24) + (signal * 0.24) + (novelty * 0.22) - low_signal_penalty(title)
    return round(max(0.0, min(score, 1.0)), 4), fresh, signal, overlap


def build_candidate_note(candidate: Candidate) -> str:
    roles = ", ".join(candidate.roles)
    intents = ", ".join(candidate.intents)
    lines = [
        "---",
        f"source: {candidate.link}",
        f"title: Promotion Candidate - {candidate.title}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: phase26_promotion_candidate, {candidate.domain}, {candidate.source_slug}, external_sources",
        f"topic: {candidate.source_topic}",
        f"intent: {intents or 'research, monitoring'}",
        f"role: {roles or 'pinchy'}",
        f"confidence: {candidate.source_confidence or 'medium'}",
        "canonical: false",
        "canonical_group: Developer QA external promotion candidates",
        "use_for: durable_note_review, external_signal_triage",
        "avoid_for: final_strategy_without_review",
        "---",
        "",
        f"# Promotion Candidate - {candidate.title}",
        "",
        f"Source article: [{candidate.title}]({candidate.link})",
        f"Source canon: `{candidate.domain}/memory/live-source-canon-{candidate.source_slug}.md`",
        f"Published: {candidate.published}",
        f"Domain: {candidate.domain}",
        f"Source topic: {candidate.source_topic}",
        f"Promotion score: {candidate.score:.2f}",
        f"Freshness score: {candidate.freshness:.2f}",
        f"Novelty gap: {(1.0 - candidate.overlap):.2f}",
        f"Signal strength: {candidate.signal_strength:.2f}",
        "",
        "## Source Signal",
        candidate.summary or "Open the linked article and source canon for the full signal.",
        "",
        "## Why This Candidate Is In Queue",
        f"- Freshness and confidence are strong enough to justify review for the {candidate.domain} durable library.",
        f"- Suggested destination: `{candidate.routing['suggested_note']}`.",
        f"- Routing rationale: {candidate.routing['reason']}",
        "",
        "## Draft Summary",
        f"- {candidate.title}",
        f"- {candidate.summary or 'The article surfaces a reusable engineering or testing pattern worth checking against the existing canon.'}",
        f"- Best fit bundle: {candidate.routing['suggested_bundle']}",
        "",
        "## Suggested Placement",
        f"- Review against `{candidate.routing['suggested_note']}`.",
        f"- If approved, route it through `{candidate.routing['suggested_bundle']}` first.",
        f"- Proposed durable filename: `{candidate.draft_filename}`",
    ]
    return "\n".join(lines).rstrip() + "\n"


def build_queue(tracked: Sequence[Dict[str, Any]]) -> str:
    grouped: Dict[str, List[Dict[str, Any]]] = {"developer": [], "qa": []}
    for item in tracked:
        grouped.setdefault(item["domain"], []).append(item)

    lines = [
        "---",
        "source: local phase26 developer-qa promotion drafting",
        "title: Developer QA Promotion Queue",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase26, developer, qa, promotion_queue",
        "topic: developer_qa_promotion_queue",
        "intent: maintenance, review, durable_note_promotion",
        "role: pinchy, developer, qa, reviewer, devops",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Developer QA promotion queue",
        "use_for: candidate_review, durable_memory_growth",
        "avoid_for: final_strategy_without_approval",
        "---",
        "",
        "# Developer QA Promotion Queue",
        "",
    ]
    for domain in ("developer", "qa"):
        rows = sorted(grouped.get(domain, []), key=lambda item: (-float(item["score"]), item["draft_filename"]))
        lines.append(f"## {DOMAIN_CONFIG[domain]['label']}")
        if not rows:
            lines.append("- No queued candidates.")
            lines.append("")
            continue
        for item in rows:
            lines.append(
                f"- `{item['draft_filename']}` | score={float(item['score']):.2f} | source={item['source_slug']} | suggested={item['routing']['suggested_note']}"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def tracked_candidates_from_state(state: Dict[str, Any], drafts_dir: Path) -> List[Dict[str, Any]]:
    tracked: List[Dict[str, Any]] = []
    for link, item in state.get("candidates", {}).items():
        draft_path = drafts_dir / item["draft_filename"]
        if not draft_path.exists():
            continue
        record = dict(item)
        record["link"] = link
        tracked.append(record)
    return sorted(tracked, key=lambda item: (-float(item["score"]), item["draft_filename"]))


def domain_candidates(
    skills_root: Path,
    domain: str,
    per_source: int,
    max_age_days: int,
    min_score: float,
    state_candidates: Dict[str, Dict[str, Any]],
) -> List[Candidate]:
    memory_root = skills_root / domain / "memory"
    notes = durable_notes(skills_root, domain)
    candidates: List[Candidate] = []
    for path in sorted(memory_root.glob("live-source-*.md")):
        if path.name.startswith("live-source-canon-"):
            continue
        meta, items = parse_live_items(path)
        source_slug = path.stem.removeprefix("live-source-")
        source_name = note_title(path).removeprefix("Live Knowledge Snapshot - ").strip()
        accepted = 0
        for published, title, link, summary in items:
            if link in state_candidates:
                continue
            score, fresh, signal, overlap = score_candidate(
                domain=domain,
                title=title,
                summary=summary,
                published=published,
                confidence=meta.get("confidence", ""),
                notes=notes,
                max_age_days=max_age_days,
            )
            if score < min_score or fresh <= 0.0:
                continue
            draft_filename = f"{source_slug}-{slugify(title)}.md"
            candidates.append(
                Candidate(
                    domain=domain,
                    source_slug=source_slug,
                    source_name=source_name,
                    source_topic=meta.get("topic", f"{domain}_external_signal"),
                    source_confidence=meta.get("confidence", "medium"),
                    roles=meta_list(meta, "role"),
                    intents=meta_list(meta, "intent"),
                    title=title,
                    link=link,
                    published=published,
                    summary=summary,
                    score=score,
                    freshness=fresh,
                    overlap=overlap,
                    signal_strength=signal,
                    draft_filename=draft_filename,
                    routing=suggest_routing(domain, meta.get("topic", ""), title, summary),
                )
            )
            accepted += 1
            if accepted >= per_source:
                break
    candidates.sort(key=lambda item: (-item.score, item.draft_filename))
    return candidates


def persist_candidates(
    candidates: Sequence[Candidate],
    drafts_dir: Path,
    state_path: Path,
    previous_state: Dict[str, Any],
) -> Dict[str, Any]:
    drafts_dir.mkdir(parents=True, exist_ok=True)
    stored = dict(previous_state.get("candidates", {}))
    for candidate in candidates:
        draft_path = drafts_dir / candidate.draft_filename
        draft_path.write_text(build_candidate_note(candidate), encoding="utf-8")
        stored[candidate.link] = {
            "domain": candidate.domain,
            "source_slug": candidate.source_slug,
            "source_name": candidate.source_name,
            "source_topic": candidate.source_topic,
            "source_confidence": candidate.source_confidence,
            "roles": candidate.roles,
            "intents": candidate.intents,
            "title": candidate.title,
            "published": candidate.published,
            "summary": candidate.summary,
            "score": candidate.score,
            "freshness": candidate.freshness,
            "overlap": candidate.overlap,
            "signal_strength": candidate.signal_strength,
            "draft_filename": candidate.draft_filename,
            "routing": candidate.routing,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "candidates": stored,
    }
    write_json(state_path, payload)
    return payload


def run(
    skills_root: Path,
    phase25_manifest: Path,
    phase26_dir: Path,
    state_path: Path,
    max_candidates: int,
    per_domain: int,
    per_source: int,
    max_age_days: int,
    min_score: float,
) -> Dict[str, Any]:
    manifest = load_json(phase25_manifest, {})
    if not manifest:
        raise SystemExit(f"Missing Phase 25 manifest: {phase25_manifest}")

    phase26_dir.mkdir(parents=True, exist_ok=True)
    drafts_dir = phase26_dir / "drafts"
    previous_state = load_json(state_path, {"candidates": {}})
    previous_candidates = previous_state.get("candidates", {})

    selected: List[Candidate] = []
    by_domain: Dict[str, int] = {"developer": 0, "qa": 0}
    by_source: Dict[Tuple[str, str], int] = {}
    domain_counts: Dict[str, int] = {"developer": 0, "qa": 0}
    source_counts: Dict[str, int] = {}

    combined: List[Candidate] = []
    for domain in ("developer", "qa"):
        domain_set = domain_candidates(skills_root, domain, per_source, max_age_days, min_score, previous_candidates)
        domain_counts[domain] = len(domain_set)
        combined.extend(domain_set)

    combined.sort(key=lambda item: (-item.score, item.domain, item.draft_filename))
    for candidate in combined:
        if len(selected) >= max_candidates:
            break
        if by_domain[candidate.domain] >= per_domain:
            continue
        key = (candidate.domain, candidate.source_slug)
        if by_source.get(key, 0) >= per_source:
            continue
        selected.append(candidate)
        by_domain[candidate.domain] += 1
        by_source[key] = by_source.get(key, 0) + 1
        source_counts[key[1]] = source_counts.get(key[1], 0) + 1

    state_payload = persist_candidates(selected, drafts_dir, state_path, previous_state)
    tracked = tracked_candidates_from_state(state_payload, drafts_dir)[:max_candidates]
    queue_path = phase26_dir / "promotion-queue.md"
    queue_path.write_text(build_queue(tracked), encoding="utf-8")

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase25_manifest": str(phase25_manifest),
        "phase26_dir": str(phase26_dir),
        "state_path": str(state_path),
        "drafts_dir": str(drafts_dir),
        "queue_path": str(queue_path),
        "candidate_count": len(selected),
        "tracked_candidates": tracked,
        "domain_candidate_counts": domain_counts,
        "source_candidate_counts": source_counts,
    }
    manifest_path = phase26_dir / f"phase26-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase26_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Queue: {result['queue_path']}")
    print(f"Candidates: {result['candidate_count']}")
    for item in result["tracked_candidates"]:
        print(f"- {item['draft_filename']} | domain={item['domain']} | score={float(item['score']):.2f}")


def main() -> int:
    args = parse_args()
    phase26_dir = Path(args.phase26_dir)
    state_path = Path(args.state_path)
    if state_path == DEFAULT_STATE and phase26_dir != DEFAULT_PHASE26_DIR:
        state_path = phase26_dir / "state.json"
    result = run(
        skills_root=Path(args.skills_root),
        phase25_manifest=Path(args.phase25_manifest),
        phase26_dir=phase26_dir,
        state_path=state_path,
        max_candidates=args.max_candidates,
        per_domain=args.per_domain,
        per_source=args.per_source,
        max_age_days=args.max_age_days,
        min_score=args.min_score,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
