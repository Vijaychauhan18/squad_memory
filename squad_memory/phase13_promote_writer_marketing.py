#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE12 = BASE / "ingest" / "phase12" / "latest.json"
DEFAULT_PHASE13_DIR = BASE / "ingest" / "phase13"
DEFAULT_STATE = DEFAULT_PHASE13_DIR / "state.json"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
HEADING_RE = re.compile(r"^##\s+Core Concept\s*$", re.MULTILINE)
ITEM_RE = re.compile(r"^- (?P<published>[^|]+?) \| \[(?P<title>[^\]]+)\]\((?P<link>[^)]+)\)")
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_+\-]{1,}")
LOW_SIGNAL_PATTERNS = [
    re.compile(r"\binfographic\b", re.IGNORECASE),
    re.compile(r"\bstatistics?\b", re.IGNORECASE),
    re.compile(r"\bchart(s)?\b", re.IGNORECASE),
    re.compile(r"\bweekly\b", re.IGNORECASE),
    re.compile(r"\bupdate\b", re.IGNORECASE),
    re.compile(r"\bnews\b", re.IGNORECASE),
    re.compile(r"\btop \d+\b", re.IGNORECASE),
    re.compile(r"\bbest \d+\b", re.IGNORECASE),
]

DOMAIN_CONFIG: Dict[str, Dict[str, Any]] = {
    "writer": {
        "label": "Writer",
        "high_signal_terms": {
            "hook",
            "hooks",
            "opening",
            "lead",
            "headline",
            "copy",
            "copywriting",
            "cta",
            "landing",
            "email",
            "emails",
            "voice",
            "clarity",
            "readability",
            "structure",
            "message",
            "audience",
            "persuasion",
            "editing",
        },
        "suggested_bundle": "Plankton Bundle",
    },
    "marketing": {
        "label": "Marketing",
        "high_signal_terms": {
            "distribution",
            "channel",
            "channels",
            "social",
            "platform",
            "campaign",
            "launch",
            "followup",
            "follow-up",
            "email",
            "newsletter",
            "audience",
            "brand",
            "creator",
            "reporting",
            "measurement",
            "engagement",
            "demand",
            "positioning",
        },
        "suggested_bundle": "Current Bundle",
    },
}

TOPIC_ROUTING: Dict[str, Dict[str, Dict[str, str]]] = {
    "writer": {
        "copywriting_systems": {
            "note": "memory/hooks-and-structure.md",
            "reason": "This fills the hooks, openings, and persuasive structure lane.",
        },
        "editorial_strategy": {
            "note": "memory/brief-to-draft.md",
            "reason": "This supports the brief-to-draft and editorial planning workflow.",
        },
        "reader_first_writing": {
            "note": "memory/documentation-and-guides.md",
            "reason": "This strengthens clarity, readability, and reader-progress guidance.",
        },
        "message_framing": {
            "note": "memory/hooks-and-structure.md",
            "reason": "This improves framing and opening mechanics rather than format-specific delivery.",
        },
        "conversion_copywriting": {
            "note": "memory/landing-page-copy.md",
            "reason": "This belongs with conversion-focused copy and CTA structure.",
        },
    },
    "marketing": {
        "social_distribution": {
            "note": "memory/platform-native-posts.md",
            "reason": "This is a channel and platform adaptation signal.",
        },
        "campaign_operations": {
            "note": "memory/distribution-system.md",
            "reason": "This supports reusable rollout and campaign execution systems.",
        },
        "platform_changes": {
            "note": "memory/platform-native-posts.md",
            "reason": "This is primarily about adapting output to platform behavior.",
        },
        "brand_distribution": {
            "note": "memory/launch-and-followup.md",
            "reason": "This belongs with launch framing and post-publication amplification.",
        },
    },
}


@dataclass
class ExistingNote:
    rel_path: str
    title: str
    tokens: set[str]


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
    parser = argparse.ArgumentParser(description="Phase 13 writer and marketing durable promotion drafting")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase12-manifest", default=str(DEFAULT_PHASE12))
    parser.add_argument("--phase13-dir", default=str(DEFAULT_PHASE13_DIR))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--max-candidates", type=int, default=10)
    parser.add_argument("--per-domain", type=int, default=4)
    parser.add_argument("--per-source", type=int, default=1)
    parser.add_argument("--max-age-days", type=int, default=120)
    parser.add_argument("--min-score", type=float, default=0.52)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip().lower()] = value.strip()
    return meta, text[match.end() :]


def meta_list(meta: Dict[str, str], key: str) -> List[str]:
    return [item.strip() for item in meta.get(key, "").split(",") if item.strip()]


def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "item"


def note_title(path: Path) -> str:
    meta, body = parse_frontmatter(path.read_text())
    if meta.get("title"):
        return meta["title"]
    for raw in body.splitlines():
        if raw.startswith("# "):
            return raw[2:].strip()
    return path.stem


def extract_core_concept(text: str) -> str:
    meta, body = parse_frontmatter(text)
    match = HEADING_RE.search(body)
    if not match:
        lines = [line.strip() for line in body.splitlines() if line.strip() and not line.startswith("#")]
        return lines[0] if lines else meta.get("title", "")
    remainder = body[match.end() :].strip()
    return remainder.split("\n\n", 1)[0].strip() if remainder else meta.get("title", "")


def durable_notes(skills_root: Path, domain: str) -> List[ExistingNote]:
    memory_root = skills_root / domain / "memory"
    notes: List[ExistingNote] = []
    for path in sorted(memory_root.glob("*.md")):
        name = path.name
        if name.startswith("live-source-"):
            continue
        if name.startswith("live-external-source-monitor"):
            continue
        if "canon" in name:
            continue
        title = note_title(path)
        concept = extract_core_concept(path.read_text())
        notes.append(
            ExistingNote(
                rel_path=f"{domain}/memory/{name}",
                title=title,
                tokens=set(tokenize(f"{title}\n{concept}")),
            )
        )
    return notes


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


def clean_summary(summary: str) -> str:
    value = summary.replace("Read the full article at MarketingProfs", "").replace("Read more.", "").replace("Continue Reading", "").strip()
    value = re.sub(r"\s+", " ", value)
    return value.strip(" .")


def parse_date(value: str) -> date | None:
    raw = value.strip()[:10]
    if not raw:
        return None
    try:
        return date.fromisoformat(raw)
    except ValueError:
        return None


def confidence_weight(value: str) -> float:
    lowered = value.strip().lower()
    if lowered == "high":
        return 1.0
    if lowered == "medium":
        return 0.72
    if lowered == "low":
        return 0.45
    return 0.55


def freshness_score(published: str, max_age_days: int) -> float:
    parsed = parse_date(published)
    if parsed is None:
        return 0.35
    days_old = max((date.today() - parsed).days, 0)
    if days_old > max_age_days:
        return 0.0
    ratio = max(0.0, 1.0 - (days_old / max_age_days))
    return round(0.35 + ratio * 0.65, 4)


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


def signal_strength(domain: str, title: str, summary: str) -> float:
    terms = DOMAIN_CONFIG[domain]["high_signal_terms"]
    tokens = set(tokenize(f"{title}\n{summary}"))
    hits = len(tokens & terms)
    return round(min(hits / 4.0, 1.0), 4)


def low_signal_penalty(title: str) -> float:
    for pattern in LOW_SIGNAL_PATTERNS:
        if pattern.search(title):
            return 0.22
    return 0.0


def suggest_routing(domain: str, topic: str, title: str, summary: str) -> Dict[str, str]:
    mapping = TOPIC_ROUTING.get(domain, {}).get(topic)
    if mapping:
        note = mapping["note"]
        reason = mapping["reason"]
    else:
        tokens = set(tokenize(f"{title}\n{summary}"))
        if domain == "writer":
            if {"email", "emails", "newsletter"} & tokens:
                note = "memory/email-sequences.md"
                reason = "This looks closest to email sequencing and lifecycle writing."
            elif {"landing", "cta", "conversion"} & tokens:
                note = "memory/landing-page-copy.md"
                reason = "This is conversion-oriented and belongs with landing page copy guidance."
            else:
                note = "memory/hooks-and-structure.md"
                reason = "This mostly sharpens openings, framing, or editorial structure."
        else:
            if {"email", "newsletter"} & tokens:
                note = "memory/email-newsletter.md"
                reason = "This is closest to newsletter or email promotion workflow."
            elif {"launch", "followup", "follow-up", "campaign"} & tokens:
                note = "memory/launch-and-followup.md"
                reason = "This fits launch execution and follow-up sequencing."
            elif {"platform", "instagram", "linkedin", "tiktok", "social"} & tokens:
                note = "memory/platform-native-posts.md"
                reason = "This is primarily a channel or platform adaptation signal."
            else:
                note = "memory/distribution-system.md"
                reason = "This is best treated as a reusable distribution or campaign-system note."
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
        f"tags: phase13_promotion_candidate, {candidate.domain}, {candidate.source_slug}, external_sources",
        f"topic: {candidate.source_topic}",
        f"intent: {intents or 'research, monitoring'}",
        f"role: {roles or 'pinchy'}",
        f"confidence: {candidate.source_confidence or 'medium'}",
        "canonical: false",
        "canonical_group: Writer marketing external promotion candidates",
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
        f"- {candidate.summary or 'The article surfaces a reusable pattern worth checking against the existing canon.'}",
        f"- Best fit bundle: {candidate.routing['suggested_bundle']}",
        "",
        "## Suggested Placement",
        f"- Review against `{candidate.routing['suggested_note']}`.",
        f"- If approved, route it through `{candidate.routing['suggested_bundle']}` first.",
        f"- Proposed durable filename: `{candidate.draft_filename}`",
    ]
    return "\n".join(lines).rstrip() + "\n"


def build_queue(tracked: Sequence[Dict[str, Any]]) -> str:
    grouped: Dict[str, List[Dict[str, Any]]] = {"writer": [], "marketing": []}
    for item in tracked:
        grouped.setdefault(item["domain"], []).append(item)

    lines = [
        "---",
        "source: local phase13 writer-marketing promotion drafting",
        f"title: Writer Marketing Promotion Queue",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase13, writer, marketing, promotion_queue",
        "topic: writer_marketing_promotion_queue",
        "intent: maintenance, review, durable_note_promotion",
        "role: pinchy, writer, marketing, charles",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Writer marketing promotion queue",
        "use_for: candidate_review, durable_memory_growth",
        "avoid_for: final_strategy_without_approval",
        "---",
        "",
        "# Writer Marketing Promotion Queue",
        "",
    ]
    for domain in ("writer", "marketing"):
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
            score, fresh, signal, overlap = score_candidate(domain, title, summary, published, meta.get("confidence", ""), notes, max_age_days)
            if score < min_score or fresh <= 0.0:
                continue
            routing = suggest_routing(domain, meta.get("topic", ""), title, summary)
            candidate = Candidate(
                domain=domain,
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
            candidates.append(candidate)
            accepted += 1
            if accepted >= per_source:
                break
    return sorted(candidates, key=lambda item: (-item.score, item.draft_filename))


def run(
    skills_root: Path,
    phase12_manifest: Path,
    phase13_dir: Path,
    state_path: Path,
    max_candidates: int,
    per_domain: int,
    per_source: int,
    max_age_days: int,
    min_score: float,
) -> Dict[str, Any]:
    phase12 = load_json(phase12_manifest, {})
    phase13_dir.mkdir(parents=True, exist_ok=True)
    drafts_dir = phase13_dir / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)
    state = load_json(state_path, {"generated_at": "", "candidates": {}})
    state_candidates = dict(state.get("candidates", {}))

    requested_domains = [item["domain"] for item in phase12.get("domains", []) if item.get("domain") in DOMAIN_CONFIG]
    if not requested_domains:
        requested_domains = list(DOMAIN_CONFIG)

    new_candidates: List[Dict[str, Any]] = []
    for domain in requested_domains:
        selected = domain_candidates(skills_root, domain, per_source, max_age_days, min_score, state_candidates)[:per_domain]
        for candidate in selected:
            draft_path = drafts_dir / candidate.draft_filename
            draft_path.write_text(build_candidate_note(candidate))
            state_candidates[candidate.link] = {
                "domain": candidate.domain,
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
                    "domain": candidate.domain,
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
        "candidates": state_candidates,
    }
    write_json(state_path, state_payload)

    tracked = tracked_candidates_from_state(state_payload, drafts_dir)[:max_candidates]
    queue_path = phase13_dir / "promotion-queue.md"
    queue_path.write_text(build_queue(tracked))

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase12_manifest": str(phase12_manifest),
        "phase13_dir": str(phase13_dir),
        "queue_path": str(queue_path),
        "drafts_dir": str(drafts_dir),
        "new_candidates": new_candidates,
        "tracked_candidates": tracked,
        "domain_counts": {
            domain: len([item for item in tracked if item["domain"] == domain]) for domain in requested_domains
        },
    }
    manifest_path = phase13_dir / f"phase13-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase13_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Queue: {result['queue_path']}")
    for item in result["tracked_candidates"]:
        print(f"- {item['domain']}: {item['draft_filename']} score={float(item['score']):.2f}")


def main() -> int:
    args = parse_args()
    result = run(
        skills_root=Path(args.skills_root),
        phase12_manifest=Path(args.phase12_manifest),
        phase13_dir=Path(args.phase13_dir),
        state_path=Path(args.state_path),
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
