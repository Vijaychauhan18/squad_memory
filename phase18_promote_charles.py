#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from phase13_promote_writer_marketing import (
    ITEM_RE,
    FRONTMATTER_RE,
    HEADING_RE,
    clean_summary,
    confidence_weight,
    durable_notes,
    extract_core_concept,
    load_json,
    low_signal_penalty,
    max_overlap,
    meta_list,
    note_title,
    parse_date,
    parse_frontmatter,
    slugify,
    tokenize,
    write_json,
)


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE17 = BASE / "ingest" / "phase17" / "latest.json"
DEFAULT_PHASE18_DIR = BASE / "ingest" / "phase18"
DEFAULT_STATE = DEFAULT_PHASE18_DIR / "state.json"

HIGH_SIGNAL_TERMS = {
    "creator",
    "creators",
    "social",
    "platform",
    "platforms",
    "posting",
    "post",
    "posts",
    "hook",
    "hooks",
    "engagement",
    "comment",
    "comments",
    "reply",
    "replies",
    "community",
    "calendar",
    "trend",
    "trends",
    "linkedin",
    "instagram",
    "tiktok",
    "reels",
    "youtube",
    "shorts",
    "threads",
    "repurpose",
    "repurposing",
    "audience",
    "channel",
    "channels",
    "native",
}

TOPIC_ROUTING: Dict[str, Dict[str, str]] = {
    "social_distribution": {
        "note": "memory/platform-native-posting-system.md",
        "reason": "This is primarily about channel-native packaging and adapting one idea across platforms.",
    },
    "platform_changes": {
        "note": "memory/social-calendar-and-trend-radar.md",
        "reason": "This belongs with trend tracking, platform shifts, and planning cadence.",
    },
}


@dataclass
class Candidate:
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
    parser = argparse.ArgumentParser(description="Phase 18 Charles durable-promotion drafting")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase17-manifest", default=str(DEFAULT_PHASE17))
    parser.add_argument("--phase18-dir", default=str(DEFAULT_PHASE18_DIR))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--max-candidates", type=int, default=8)
    parser.add_argument("--per-source", type=int, default=1)
    parser.add_argument("--max-age-days", type=int, default=120)
    parser.add_argument("--min-score", type=float, default=0.52)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


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
    days_old = max((datetime.now(timezone.utc).date() - parsed).days, 0)
    if days_old > max_age_days:
        return 0.0
    ratio = max(0.0, 1.0 - (days_old / max_age_days))
    return round(0.35 + ratio * 0.65, 4)


def signal_strength(title: str, summary: str) -> float:
    tokens = set(tokenize(f"{title}\n{summary}"))
    hits = len(tokens & HIGH_SIGNAL_TERMS)
    return round(min(hits / 4.0, 1.0), 4)


def suggest_routing(topic: str, title: str, summary: str) -> Dict[str, str]:
    mapping = TOPIC_ROUTING.get(topic)
    if mapping:
        return {
            "suggested_note": mapping["note"],
            "suggested_bundle": "Charles Bundle",
            "reason": mapping["reason"],
        }

    tokens = set(tokenize(f"{title}\n{summary}"))
    if {"comment", "comments", "reply", "replies", "community", "dm", "dms", "engagement"} & tokens:
        note = "memory/community-engagement-loop.md"
        reason = "This is closest to engagement handling and response discipline."
    elif {"calendar", "trend", "trends", "weekly", "plan", "planning"} & tokens:
        note = "memory/social-calendar-and-trend-radar.md"
        reason = "This is mainly about cadence, monitoring, or planning patterns."
    else:
        note = "memory/platform-native-posting-system.md"
        reason = "This is best treated as a platform-native posting and repurposing signal."
    return {
        "suggested_note": note,
        "suggested_bundle": "Charles Bundle",
        "reason": reason,
    }


def score_candidate(
    title: str,
    summary: str,
    published: str,
    confidence: str,
    notes,
    max_age_days: int,
) -> Tuple[float, float, float, float]:
    fresh = freshness_score(published, max_age_days)
    conf = confidence_weight(confidence)
    signal = signal_strength(title, summary)
    tokens = set(tokenize(f"{title}\n{summary}"))
    overlap = max_overlap(tokens, notes)
    novelty = 1.0 - overlap
    score = (fresh * 0.32) + (conf * 0.22) + (signal * 0.26) + (novelty * 0.2) - low_signal_penalty(title)
    return round(max(0.0, min(score, 1.0)), 4), fresh, signal, overlap


def build_candidate_note(candidate: Candidate) -> str:
    roles = ", ".join(candidate.roles)
    intents = ", ".join(candidate.intents)
    lines = [
        "---",
        f"source: {candidate.link}",
        f"title: Promotion Candidate - {candidate.title}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: phase18_promotion_candidate, charles, {candidate.source_slug}, external_sources",
        f"topic: {candidate.source_topic}",
        f"intent: {intents or 'research, monitoring'}",
        f"role: {roles or 'charles, pinchy'}",
        f"confidence: {candidate.source_confidence or 'medium'}",
        "canonical: false",
        "canonical_group: Charles external promotion candidates",
        "use_for: durable_note_review, external_signal_triage",
        "avoid_for: final_strategy_without_review",
        "---",
        "",
        f"# Promotion Candidate - {candidate.title}",
        "",
        f"Source article: [{candidate.title}]({candidate.link})",
        f"Source canon: `charles/memory/live-source-canon-{candidate.source_slug}.md`",
        f"Published: {candidate.published}",
        "Domain: charles",
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
        "- Freshness and confidence are strong enough to justify review for the Charles durable library.",
        f"- Suggested destination: `{candidate.routing['suggested_note']}`.",
        f"- Routing rationale: {candidate.routing['reason']}",
        "",
        "## Draft Summary",
        f"- {candidate.title}",
        f"- {candidate.summary or 'The article surfaces a reusable creator, platform, or engagement pattern worth checking against the existing Charles canon.'}",
        f"- Best fit bundle: {candidate.routing['suggested_bundle']}",
        "",
        "## Suggested Placement",
        f"- Review against `{candidate.routing['suggested_note']}`.",
        f"- If approved, route it through `{candidate.routing['suggested_bundle']}` first.",
        f"- Proposed durable filename: `{candidate.draft_filename}`",
    ]
    return "\n".join(lines).rstrip() + "\n"


def build_queue(tracked: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "---",
        "source: local phase18 charles promotion drafting",
        f"title: Charles Promotion Queue",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase18, charles, promotion_queue",
        "topic: charles_promotion_queue",
        "intent: maintenance, review, durable_note_promotion",
        "role: pinchy, charles, current, marketing",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Charles promotion queue",
        "use_for: candidate_review, durable_memory_growth",
        "avoid_for: final_strategy_without_approval",
        "---",
        "",
        "# Charles Promotion Queue",
        "",
        "## Charles",
    ]
    if not tracked:
        lines.append("- No queued candidates.")
    else:
        for item in sorted(tracked, key=lambda row: (-float(row["score"]), row["draft_filename"])):
            lines.append(
                f"- `{item['draft_filename']}` | score={float(item['score']):.2f} | source={item['source_slug']} | suggested={item['routing']['suggested_note']}"
            )
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


def find_candidates(
    skills_root: Path,
    per_source: int,
    max_age_days: int,
    min_score: float,
    state_candidates: Dict[str, Dict[str, Any]],
) -> List[Candidate]:
    memory_root = skills_root / "charles" / "memory"
    notes = durable_notes(skills_root, "charles")
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
            score, fresh, signal, overlap = score_candidate(title, summary, published, meta.get("confidence", ""), notes, max_age_days)
            if score < min_score or fresh <= 0.0:
                continue
            routing = suggest_routing(meta.get("topic", ""), title, summary)
            candidates.append(
                Candidate(
                    source_slug=source_slug,
                    source_name=source_name,
                    source_topic=meta.get("topic", ""),
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
                    draft_filename=f"{source_slug}-{slugify(title)}.md",
                    routing=routing,
                )
            )
            accepted += 1
            if accepted >= per_source:
                break
    return sorted(candidates, key=lambda item: (-item.score, item.draft_filename))


def run(
    skills_root: Path,
    phase17_manifest: Path,
    phase18_dir: Path,
    state_path: Path,
    max_candidates: int,
    per_source: int,
    max_age_days: int,
    min_score: float,
) -> Dict[str, Any]:
    phase17 = load_json(phase17_manifest, {})
    phase18_dir.mkdir(parents=True, exist_ok=True)
    drafts_dir = phase18_dir / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)
    state = load_json(state_path, {"generated_at": "", "candidates": {}})
    state_candidates = dict(state.get("candidates", {}))

    selected = find_candidates(skills_root, per_source, max_age_days, min_score, state_candidates)
    new_candidates: List[Dict[str, Any]] = []
    for candidate in selected:
        draft_path = drafts_dir / candidate.draft_filename
        draft_path.write_text(build_candidate_note(candidate), encoding="utf-8")
        state_candidates[candidate.link] = {
            "domain": "charles",
            "source_slug": candidate.source_slug,
            "source_name": candidate.source_name,
            "draft_filename": candidate.draft_filename,
            "title": candidate.title,
            "published": candidate.published,
            "score": candidate.score,
            "draft_topic": candidate.source_topic,
            "routing": candidate.routing,
            "summary": candidate.summary,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        new_candidates.append(
            {
                "domain": "charles",
                "source_slug": candidate.source_slug,
                "draft_filename": candidate.draft_filename,
                "title": candidate.title,
                "link": candidate.link,
                "published": candidate.published,
                "score": candidate.score,
                "draft_topic": candidate.source_topic,
                "routing": candidate.routing,
            }
        )

    state_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase17_manifest": str(phase17_manifest),
        "candidates": state_candidates,
    }
    write_json(state_path, state_payload)

    tracked = tracked_candidates_from_state(state_payload, drafts_dir)[:max_candidates]
    queue_path = phase18_dir / "promotion-queue.md"
    queue_path.write_text(build_queue(tracked), encoding="utf-8")

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase17_manifest": str(phase17_manifest),
        "phase17_report": phase17.get("report_path", ""),
        "phase18_dir": str(phase18_dir),
        "queue_path": str(queue_path),
        "drafts_dir": str(drafts_dir),
        "new_candidates": new_candidates,
        "tracked_candidates": tracked,
        "charles_count": len(tracked),
    }
    manifest_path = phase18_dir / f"phase18-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase18_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Queue: {result['queue_path']}")
    for item in result["tracked_candidates"]:
        print(f"- charles: {item['draft_filename']} score={float(item['score']):.2f}")


def main() -> int:
    args = parse_args()
    result = run(
        skills_root=Path(args.skills_root),
        phase17_manifest=Path(args.phase17_manifest),
        phase18_dir=Path(args.phase18_dir),
        state_path=Path(args.state_path),
        max_candidates=args.max_candidates,
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
