#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


HOME = Path("/Users/vijaychauhan")
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE3 = HOME / "squad_memory" / "ingest" / "phase3" / "latest.json"
DEFAULT_PHASE5_DIR = HOME / "squad_memory" / "ingest" / "phase5"
DEFAULT_STATE = DEFAULT_PHASE5_DIR / "state.json"

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_+\-]{1,}")
ITEM_RE = re.compile(r"^- (?P<published>[^|]+?) \| \[(?P<title>[^\]]+)\]\((?P<link>[^)]+)\)")
HIGH_SIGNAL_TERMS = {
    "ai",
    "chatgpt",
    "gemini",
    "grounding",
    "fanout",
    "fan-out",
    "selection",
    "snippet",
    "snippets",
    "query",
    "queries",
    "intent",
    "decay",
    "ranking",
    "rank",
    "citation",
    "citations",
    "brand",
    "brands",
    "content",
    "spam",
    "rufus",
    "prompt",
    "prompts",
    "reverse",
    "overview",
    "overviews",
    "search",
    "quality",
}
LOW_SIGNAL_PATTERNS = [
    re.compile(r"\bconferences?\b", re.IGNORECASE),
    re.compile(r"\bevents?\b", re.IGNORECASE),
    re.compile(r"\bwebinars?\b", re.IGNORECASE),
    re.compile(r"\btop \d+\b", re.IGNORECASE),
    re.compile(r"\bbest .*conferences?\b", re.IGNORECASE),
]

TOPIC_ROUTING = {
    "ai_reverse_engineering": {
        "suggested_index_section": "AI Search & Visibility",
        "suggested_bundle": "AI Search Bundle",
        "suggested_router_anchor": "Use the Dejan reverse-engineering pack when the task is about:",
    },
    "seo_research": {
        "suggested_index_section": "AI Search & Visibility",
        "suggested_bundle": "Execution Bundle",
        "suggested_router_anchor": "Use the Ahrefs notes when the task is about:",
    },
    "quality_systems": {
        "suggested_index_section": "Google Leak Systems & Architecture",
        "suggested_bundle": "Leak Systems Bundle",
        "suggested_router_anchor": "Use the Hobo notes when the task is about:",
    },
    "official_guidance": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Source Canon Bundle",
        "suggested_router_anchor": "Use the Google note when the task is about:",
    },
    "industry_news": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "AI Search Bundle",
        "suggested_router_anchor": "Use the industry monitoring note when the task is about:",
    },
    "daily_monitoring": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "AI Search Bundle",
        "suggested_router_anchor": "Use the industry monitoring note when the task is about:",
    },
    "relevance_engineering": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Expert Bundle",
        "suggested_router_anchor": "Use the Mike note when the task is about:",
    },
    "technical_architecture": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Expert Bundle",
        "suggested_router_anchor": "Use the Jono note when the task is about:",
    },
    "operations_and_international": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Expert Bundle",
        "suggested_router_anchor": "Use the Aleyda note when the task is about:",
    },
    "trust_and_rag": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Trust & E-E-A-T Bundle",
        "suggested_router_anchor": "Use the Lily note when the task is about:",
    },
    "rollout_and_qrg": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "AI Search Bundle",
        "suggested_router_anchor": "Use the Marie note when the task is about:",
    },
    "reporting_and_serp_features": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Expert Bundle",
        "suggested_router_anchor": "Use the Brodie note when the task is about:",
    },
    "serp_observation": {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "Expert Bundle",
        "suggested_router_anchor": "Use the Cindy note when the task is about:",
    },
}


@dataclass
class ExistingNote:
    path: str
    title: str
    tokens: set[str]


@dataclass
class LiveItem:
    source_slug: str
    source_name: str
    source_topic: str
    source_confidence: str
    source_roles: List[str]
    source_intents: List[str]
    source_strength: str
    source_note_path: str
    canonical_note_path: str
    canonical_title: str
    published: str
    title: str
    link: str
    summary: str
    freshness: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 5 durable note promotion and synthesis")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase3-manifest", default=str(DEFAULT_PHASE3))
    parser.add_argument("--phase5-dir", default=str(DEFAULT_PHASE5_DIR))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--max-candidates", type=int, default=12)
    parser.add_argument("--per-source", type=int, default=2)
    parser.add_argument("--max-age-days", type=int, default=45)
    parser.add_argument("--min-freshness", type=float, default=0.4)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")


def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "item"


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    header = text[4:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta: Dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip().lower()] = value.strip()
    return meta, body


def meta_list(meta: Dict[str, str], key: str) -> List[str]:
    value = meta.get(key, "")
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_live_items(path: Path) -> Tuple[Dict[str, str], str, List[Tuple[str, str, str, str]]]:
    meta, body = parse_frontmatter(path.read_text())
    items: List[Tuple[str, str, str, str]] = []
    lines = body.splitlines()
    for index, raw in enumerate(lines):
        line = raw.strip()
        match = ITEM_RE.match(line)
        if not match:
            continue
        summary = ""
        if index + 1 < len(lines):
            next_line = lines[index + 1].strip()
            if next_line and not next_line.startswith("- "):
                summary = next_line
        items.append(
            (
                match.group("published").strip(),
                match.group("title").strip(),
                match.group("link").strip(),
                summary,
            )
        )
    return meta, body, items


def note_title(path: Path) -> str:
    meta, body = parse_frontmatter(path.read_text())
    if meta.get("title"):
        return meta["title"]
    for raw in body.splitlines():
        if raw.startswith("# "):
            return raw[2:].strip()
    return path.stem


def durable_notes(output_dir: Path) -> List[ExistingNote]:
    notes: List[ExistingNote] = []
    for path in sorted(output_dir.glob("*.md")):
        name = path.name
        if name in {"INDEX.md", "live-knowledge-monitor.md"}:
            continue
        if name.startswith("live-source-"):
            continue
        if name.startswith("live-seo-feed-"):
            continue
        if name.startswith("promotion-queue"):
            continue
        title = note_title(path)
        notes.append(
            ExistingNote(
                path=f"seo/memory/{name}",
                title=title,
                tokens=set(tokenize(title)),
            )
        )
    return notes


def parse_iso_date(value: str) -> Optional[date]:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    intersection = len(left & right)
    union = len(left | right)
    return intersection / union if union else 0.0


def overlap_score(item: LiveItem, existing: ExistingNote) -> float:
    title_tokens = set(tokenize(item.title))
    summary_tokens = set(tokenize(item.summary))
    existing_tokens = existing.tokens
    title_overlap = jaccard(title_tokens, existing_tokens)
    summary_overlap = jaccard(summary_tokens, existing_tokens) * 0.6
    return max(title_overlap, summary_overlap)


def strategic_score(item: LiveItem, max_age_days: int) -> Tuple[float, List[str]]:
    reasons: List[str] = []
    score = 0.0
    age_days = max_age_days + 1
    published = parse_iso_date(item.published)
    if published is not None:
        age_days = max((date.today() - published).days, 0)
        if age_days <= 7:
            score += 0.25
            reasons.append("fresh within 7 days")
        elif age_days <= max_age_days:
            score += 0.12
            reasons.append("fresh within promotion window")
        else:
            score -= 0.35
            reasons.append("outside promotion window")

    if item.freshness >= 0.85:
        score += 0.2
        reasons.append("source freshness is high")
    elif item.freshness >= 0.4:
        score += 0.08
        reasons.append("source freshness is usable")

    text = f"{item.title} {item.summary}".lower()
    keyword_hits = sorted({term for term in HIGH_SIGNAL_TERMS if term in text})
    if keyword_hits:
        bonus = min(0.5, 0.08 * len(keyword_hits))
        score += bonus
        reasons.append(f"high-signal terms: {', '.join(keyword_hits[:6])}")

    if item.source_confidence == "high":
        score += 0.12
        reasons.append("high-confidence source")
    elif item.source_confidence == "medium":
        score += 0.05
        reasons.append("medium-confidence source")

    if item.source_topic in {"ai_reverse_engineering", "seo_research", "quality_systems", "official_guidance"}:
        score += 0.15
        reasons.append(f"priority topic: {item.source_topic}")

    for pattern in LOW_SIGNAL_PATTERNS:
        if pattern.search(item.title):
            score -= 0.55
            reasons.append(f"low-signal pattern: {pattern.pattern}")
            break

    return score, reasons


def load_live_items(output_dir: Path, phase3_manifest: Path, min_freshness: float) -> List[LiveItem]:
    manifest = load_json(phase3_manifest, {})
    notes = manifest.get("notes", [])
    items: List[LiveItem] = []
    for note in notes:
        if note.get("freshness", 0.0) < min_freshness:
            continue
        canonical_path = output_dir / note["filename"]
        slug = note["filename"].replace("live-source-canon-", "").removesuffix(".md")
        source_note_path = output_dir / f"live-source-{slug}.md"
        if not source_note_path.exists():
            continue
        meta, _body, parsed_items = parse_live_items(source_note_path)
        for published, title, link, summary in parsed_items:
            items.append(
                LiveItem(
                    source_slug=slug,
                    source_name=note["title"].replace("Live Source Canon - ", ""),
                    source_topic=note["topic"],
                    source_confidence=note.get("confidence", meta.get("confidence", "medium")),
                    source_roles=meta_list(meta, "role"),
                    source_intents=meta_list(meta, "intent"),
                    source_strength=meta.get("strength", ""),
                    source_note_path=str(source_note_path),
                    canonical_note_path=str(canonical_path),
                    canonical_title=note["title"],
                    published=published,
                    title=title,
                    link=link,
                    summary=summary,
                    freshness=float(note.get("freshness", 0.0)),
                )
            )
    return items


def candidate_filename(item: LiveItem) -> str:
    return f"{item.source_slug}-{slugify(item.title)}.md"


def derive_topic(item: LiveItem) -> str:
    title = item.title.lower()
    if "chatgpt" in title or "ai mode" in title or "overview" in title:
        return "ai_visibility"
    if "grounding" in title or "fanout" in title or "fan-out" in title or "selection" in title:
        return "ai_reverse_engineering"
    if "keyword intent" in title or "keywords" in title:
        return "keyword_research"
    if "content decay" in title:
        return "content_strategy"
    return item.source_topic


def derive_use_for(item: LiveItem) -> List[str]:
    text = f"{item.title} {item.summary}".lower()
    uses: List[str] = []
    if "chatgpt" in text or "ai mode" in text or "overview" in text:
        uses.extend(["ai_visibility_strategy", "citation_diagnostics"])
    if "grounding" in text or "fanout" in text or "fan-out" in text or "selection" in text:
        uses.extend(["grounding_diagnostics", "selection_rate", "fanout_analysis"])
    if "keyword intent" in text:
        uses.extend(["keyword_intent", "briefing"])
    if "content decay" in text:
        uses.extend(["content_decay", "refresh_workflows"])
    if not uses:
        uses.append("monitoring_follow_up")
    return sorted(set(uses))


def derive_intents(item: LiveItem) -> List[str]:
    intents = list(item.source_intents)
    text = f"{item.title} {item.summary}".lower()
    if "how to" in text or "what is" in text:
        intents.append("execution")
    if "data" in text or "study" in text:
        intents.append("measurement")
    if "prompt" in text or "reverse" in text:
        intents.append("reverse_engineering")
    return sorted(set(intents))


def routing_suggestions(item: LiveItem) -> Dict[str, str]:
    defaults = {
        "suggested_index_section": "Source Canon & Monitoring",
        "suggested_bundle": "AI Search Bundle",
        "suggested_router_anchor": "Use the source canon notes when the task is about:",
    }
    return {**defaults, **TOPIC_ROUTING.get(item.source_topic, {})}


def build_draft_note(item: LiveItem, score: float, overlap: float, overlap_match: Optional[ExistingNote], reasons: Sequence[str]) -> str:
    draft_topic = derive_topic(item)
    use_for = derive_use_for(item)
    intents = derive_intents(item)
    routing = routing_suggestions(item)
    confidence = "high" if item.source_confidence == "high" and score >= 0.7 else "medium"
    overlap_label = overlap_match.path if overlap_match else "none"

    lines = [
        "---",
        f"source: {item.link}",
        f"title: Promotion Candidate - {item.title}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: promotion_candidate, phase5_promote, {item.source_slug}, {slugify(draft_topic)}",
        f"topic: {draft_topic}",
        f"intent: {', '.join(intents)}",
        f"role: {', '.join(item.source_roles or ['researcher', 'seo', 'pinchy'])}",
        f"confidence: {confidence}",
        "canonical: false",
        "canonical_group: Promotion candidates",
        f"use_for: {', '.join(use_for)}",
        "avoid_for: final_strategy_without_review",
        "---",
        "",
        f"# Promotion Candidate - {item.title}",
        "",
        f"Source article: [{item.title}]({item.link})",
        f"Source canon: [{Path(item.canonical_note_path).name}](../{Path(item.canonical_note_path).name})",
        f"Published: {item.published}",
        f"Source topic: {item.source_topic}",
        "",
        "## Why This Candidate Is In Queue",
    ]
    for reason in reasons:
        lines.append(f"- {reason}")

    lines.extend(
        [
            "",
            "## Source Signal",
            item.summary or "No summary was available in the live source note. Review the source article directly before final promotion.",
            "",
            "## Proposed Durable Angle",
            f"Treat this as a candidate durable note that could extend the library around `{draft_topic}` with a fresh source-backed angle.",
            "",
            "## Suggested Placement",
            f"- Index section: {routing['suggested_index_section']}",
            f"- Memory bundle: {routing['suggested_bundle']}",
            f"- Router anchor: {routing['suggested_router_anchor']}",
            "",
            "## Overlap Check",
            f"- Best overlap score: {overlap:.2f}",
            f"- Best overlap match: {overlap_label}",
            "",
            "## Draft Summary",
            f"- Core update: {item.title}",
            f"- Why it matters: This source appears to add a fresh angle for `{draft_topic}` that is not strongly covered by the current durable library.",
            f"- Suggested team use: Start with the live source canon note, validate the article, then convert the strongest claim into a durable memory note if it survives review.",
            "",
            "## Promotion Gate",
            "- This is a draft-only candidate. Do not move it into the live SEO memory library without review.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_queue_note(result: Dict[str, Any]) -> str:
    lines = [
        "---",
        "source: local phase5 promotion queue",
        "title: Durable Memory Promotion Queue",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase5_promote, promotion_queue, review",
        "topic: durable_memory_promotion",
        "intent: review, promotion_gate, source_to_memory",
        "role: pinchy, researcher, seo",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Promotion queue",
        "use_for: review_queue, promotion_candidates, overlap_checks",
        "avoid_for: direct retrieval_without_review",
        "---",
        "",
        "# Durable Memory Promotion Queue",
        "",
        f"New drafts this run: {len(result['new_candidates'])}",
        f"Drafts still tracked: {len(result['tracked_candidates'])}",
        "",
        "## New Drafts",
    ]
    if not result["new_candidates"]:
        lines.append("- No new promotion candidates passed the gate in this run.")
    for item in result["new_candidates"]:
        lines.append(
            f"- [{item['draft_filename']}](./drafts/{item['draft_filename']}) | {item['title']} | topic={item['draft_topic']} | score={item['score']:.2f}"
        )

    lines.extend(["", "## Skipped Signals"])
    for item in result["skipped"][:20]:
        lines.append(f"- {item['title']} | source={item['source_slug']} | reason={item['reason']}")
    return "\n".join(lines) + "\n"


def promote(
    output_dir: Path,
    phase3_manifest: Path,
    phase5_dir: Path,
    state_path: Path,
    max_candidates: int,
    per_source: int,
    max_age_days: int,
    min_freshness: float,
) -> Dict[str, Any]:
    phase5_dir.mkdir(parents=True, exist_ok=True)
    drafts_dir = phase5_dir / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)

    state = load_json(state_path, {"drafted_links": {}, "drafted_files": []})
    drafted_links: Dict[str, Dict[str, Any]] = state.get("drafted_links", {})

    existing = durable_notes(output_dir)
    live_items = load_live_items(output_dir, phase3_manifest, min_freshness)

    source_counts: Dict[str, int] = defaultdict(int)
    new_candidates: List[Dict[str, Any]] = []
    skipped: List[Dict[str, Any]] = []

    sorted_items = sorted(live_items, key=lambda item: (item.published, item.source_slug, item.title), reverse=True)
    for item in sorted_items:
        if len(new_candidates) >= max_candidates:
            break
        if source_counts[item.source_slug] >= per_source:
            skipped.append({"source_slug": item.source_slug, "title": item.title, "reason": "per-source cap reached"})
            continue
        if item.link in drafted_links:
            skipped.append({"source_slug": item.source_slug, "title": item.title, "reason": "already drafted"})
            continue

        score, reasons = strategic_score(item, max_age_days=max_age_days)
        if score < 0.35:
            skipped.append({"source_slug": item.source_slug, "title": item.title, "reason": f"low strategic score {score:.2f}"})
            continue

        overlap_match: Optional[ExistingNote] = None
        overlap = 0.0
        for note in existing:
            score_here = overlap_score(item, note)
            if score_here > overlap:
                overlap = score_here
                overlap_match = note
        if overlap >= 0.52:
            skipped.append(
                {
                    "source_slug": item.source_slug,
                    "title": item.title,
                    "reason": f"overlaps {overlap_match.path if overlap_match else 'existing note'} at {overlap:.2f}",
                }
            )
            continue

        draft_filename = candidate_filename(item)
        draft_path = drafts_dir / draft_filename
        draft_topic = derive_topic(item)
        draft_text = build_draft_note(item, score, overlap, overlap_match, reasons)
        draft_path.write_text(draft_text)
        routing = routing_suggestions(item)
        record = {
            "source_slug": item.source_slug,
            "source_name": item.source_name,
            "title": item.title,
            "link": item.link,
            "published": item.published,
            "draft_filename": draft_filename,
            "draft_path": str(draft_path),
            "draft_topic": draft_topic,
            "score": round(score, 4),
            "overlap": round(overlap, 4),
            "overlap_match": overlap_match.path if overlap_match else "",
            "routing": routing,
        }
        new_candidates.append(record)
        drafted_links[item.link] = record
        source_counts[item.source_slug] += 1

    state["drafted_links"] = drafted_links
    state["drafted_files"] = sorted({item["draft_filename"] for item in drafted_links.values()})
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_json(state_path, state)

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase3_manifest": str(phase3_manifest),
        "phase5_dir": str(phase5_dir),
        "state_path": str(state_path),
        "new_candidates": new_candidates,
        "tracked_candidates": list(drafted_links.values()),
        "skipped": skipped,
        "approval_gate": {
            "mode": "draft_only",
            "status": "review_required",
        },
    }
    queue_path = phase5_dir / "promotion-queue.md"
    queue_path.write_text(build_queue_note(result))
    result["queue_note"] = str(queue_path)

    manifest_path = phase5_dir / f"phase5-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase5_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Queue note: {result['queue_note']}")
    print(f"New candidates: {len(result['new_candidates'])}")
    print(f"Tracked candidates: {len(result['tracked_candidates'])}")
    for item in result["new_candidates"]:
        print(
            f"- {item['title']} | draft={item['draft_filename']} | topic={item['draft_topic']} | score={item['score']:.2f}"
        )


def main() -> int:
    args = parse_args()
    result = promote(
        output_dir=Path(args.output_dir),
        phase3_manifest=Path(args.phase3_manifest),
        phase5_dir=Path(args.phase5_dir),
        state_path=Path(args.state_path),
        max_candidates=args.max_candidates,
        per_source=args.per_source,
        max_age_days=args.max_age_days,
        min_freshness=args.min_freshness,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
