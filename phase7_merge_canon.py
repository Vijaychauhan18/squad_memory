#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import json
import re
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE6_DECISIONS = BASE / "ingest" / "phase6" / "decisions.json"
DEFAULT_PHASE7_DIR = BASE / "ingest" / "phase7"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_\-]{1,}")
ISO_DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
SIMILARITY_THRESHOLD = 0.16

CATEGORY_ORDER = {
    "canonical_note": 5,
    "promoted_live_note": 4,
    "durable_note": 3,
    "monitor_canon": 2,
    "monitor_raw": 1,
    "legacy_live_feed": 0,
}
CONFIDENCE_ORDER = {"high": 3, "medium": 2, "low": 1, "": 0}
SOURCE_PRIORITY = {
    "ahrefs": 9,
    "dejan": 9,
    "hobo": 8,
    "google": 8,
    "gsqi": 7,
    "ipullrank": 7,
    "jono": 6,
    "search-engine-land": 4,
    "search-engine-journal": 4,
    "seroundtable": 3,
}


@dataclasses.dataclass
class NoteRecord:
    rel_path: str
    abs_path: Path
    filename: str
    title: str
    topic: str
    source_slug: str
    confidence: str
    canonical: bool
    canonical_group: str
    category: str
    promotion_status: str
    key_date: str
    tokens: set[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 7 canonical synthesis and memory decay control")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase6-decisions", default=str(DEFAULT_PHASE6_DECISIONS))
    parser.add_argument("--phase7-dir", default=str(DEFAULT_PHASE7_DIR))
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
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


def meta_bool(meta: Dict[str, str], key: str) -> bool:
    return meta.get(key, "").strip().lower() in {"1", "true", "yes", "y"}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "item"


def tokenize(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def extract_heading(body: str) -> str:
    match = HEADING_RE.search(body)
    return match.group(1).strip() if match else ""


def infer_source_slug(filename: str, meta: Dict[str, str]) -> str:
    source_value = meta.get("source", "").lower()
    if filename.startswith("ahrefs-") or "ahrefs.com" in source_value:
        return "ahrefs"
    if filename.startswith("hobo-") or "hobo-web.co.uk" in source_value:
        return "hobo"
    if filename.startswith("dejan-") or "dejan.ai" in source_value or "dejanmarketing.com" in source_value:
        return "dejan"
    if filename.startswith("gsqi-") or "gsqi.com" in source_value:
        return "gsqi"
    if filename.startswith("ipullrank-") or "ipullrank.com" in source_value:
        return "ipullrank"
    if filename.startswith("jono-") or "jonoalderson.com" in source_value:
        return "jono"
    if filename.startswith("search-engine-land-") or "searchengineland.com" in source_value:
        return "search-engine-land"
    if filename.startswith("search-engine-journal-") or "searchenginejournal.com" in source_value:
        return "search-engine-journal"
    if filename.startswith("seroundtable-") or "seroundtable.com" in source_value:
        return "seroundtable"
    if "developers.google.com" in source_value or filename.startswith("google-"):
        return "google"
    return slugify(source_value) if source_value else "unknown"


def infer_category(filename: str, meta: Dict[str, str]) -> str:
    if filename.startswith("live-seo-feed-") or filename == "live-seo-feed-monitor.md":
        return "legacy_live_feed"
    if filename.startswith("live-source-canon") or filename in {"live-knowledge-monitor.md", "live-source-cluster-report.md"}:
        return "monitor_canon"
    if filename.startswith("live-source-"):
        return "monitor_raw"
    if meta.get("promotion_status", "").strip().lower() == "approved" or meta.get("canonical_group", "").strip() == "Live approved promotions":
        return "promoted_live_note"
    if meta_bool(meta, "canonical"):
        return "canonical_note"
    return "durable_note"


def extract_key_date(meta: Dict[str, str], body: str) -> str:
    candidates: List[str] = []
    for key in ("approved_on", "scraped", "published"):
        value = meta.get(key, "").strip()
        if value:
            match = ISO_DATE_RE.search(value)
            if match:
                candidates.append(match.group(1))
    candidates.extend(ISO_DATE_RE.findall(body))
    parsed: List[date] = []
    for value in candidates:
        try:
            parsed.append(date.fromisoformat(value))
        except ValueError:
            continue
    return max(parsed).isoformat() if parsed else ""


def note_record(output_dir: Path, path: Path) -> Optional[NoteRecord]:
    if path.name == "INDEX.md":
        return None
    text = path.read_text(errors="ignore")
    meta, body = parse_frontmatter(text)
    title = meta.get("title", "").strip() or extract_heading(body) or path.stem.replace("-", " ")
    topic = meta.get("topic", "").strip().lower()
    category = infer_category(path.name, meta)
    token_text = " ".join(
        part
        for part in (
            title,
            meta.get("tags", ""),
            meta.get("use_for", ""),
            body[:2500],
        )
        if part
    )
    return NoteRecord(
        rel_path=f"seo/memory/{path.name}",
        abs_path=path,
        filename=path.name,
        title=title,
        topic=topic,
        source_slug=infer_source_slug(path.name, meta),
        confidence=meta.get("confidence", "").strip().lower(),
        canonical=meta_bool(meta, "canonical"),
        canonical_group=meta.get("canonical_group", "").strip(),
        category=category,
        promotion_status=meta.get("promotion_status", "").strip().lower(),
        key_date=extract_key_date(meta, body),
        tokens=tokenize(token_text),
    )


def collect_notes(output_dir: Path) -> List[NoteRecord]:
    notes: List[NoteRecord] = []
    for path in sorted(output_dir.glob("*.md")):
        record = note_record(output_dir, path)
        if record is not None:
            notes.append(record)
    return notes


def similarity(left: NoteRecord, right: NoteRecord) -> float:
    if not left.tokens or not right.tokens:
        return 0.0
    intersection = len(left.tokens & right.tokens)
    union = len(left.tokens | right.tokens)
    return intersection / union if union else 0.0


def sort_notes(notes: Iterable[NoteRecord]) -> List[NoteRecord]:
    return sorted(
        notes,
        key=lambda note: (
            CATEGORY_ORDER.get(note.category, 0),
            1 if note.canonical else 0,
            CONFIDENCE_ORDER.get(note.confidence, 0),
            SOURCE_PRIORITY.get(note.source_slug, 0),
            note.key_date,
            note.filename,
        ),
        reverse=True,
    )


def durable_candidates(notes: List[NoteRecord]) -> List[NoteRecord]:
    return [note for note in notes if note.category in {"canonical_note", "promoted_live_note", "durable_note"}]


def topic_cluster(topic: str, notes: List[NoteRecord]) -> Dict[str, Any]:
    sorted_notes = sort_notes(notes)
    canonical_notes = [note for note in sorted_notes if note.category == "canonical_note"]
    candidate_notes = durable_candidates(sorted_notes)
    monitor_notes = [note for note in sorted_notes if note.category in {"monitor_canon", "monitor_raw"}]
    stale_notes = [note for note in sorted_notes if note.category == "legacy_live_feed"]

    primary = canonical_notes[0] if canonical_notes else (candidate_notes[0] if candidate_notes else None)
    topic_status = "monitor_only"
    if primary is not None:
        topic_status = "healthy" if primary.canonical else "needs_canonical"
    elif stale_notes:
        topic_status = "legacy_only"

    note_states: Dict[str, Dict[str, Any]] = {}
    merge_candidates: List[str] = []
    supporting: List[str] = []
    orphan_paths: List[str] = []

    for note in sorted_notes:
        merge_target = ""
        similarity_to_primary = 0.0
        if primary is not None and note.rel_path != primary.rel_path:
            similarity_to_primary = similarity(note, primary)

        if note.category == "legacy_live_feed":
            status = "stale_legacy_feed"
            reason = "Legacy live SEO feed note superseded by the live-source pipeline."
        elif note.category == "monitor_raw":
            status = "monitor_raw"
            reason = "Raw live-source snapshot retained for freshness checks, not primary retrieval."
        elif note.category == "monitor_canon":
            status = "monitor_canon"
            reason = "Freshness-first monitoring note for current source routing."
        elif primary is not None and note.rel_path == primary.rel_path:
            if primary.canonical:
                status = "canonical_primary"
                reason = "Primary canonical note for this topic."
            else:
                status = "orphan_primary"
                reason = "Best durable note for this topic but still missing canonical metadata."
                orphan_paths.append(note.rel_path)
        elif note.canonical:
            status = "canonical_secondary"
            reason = "Additional canonical note in the same topic cluster."
        elif primary is not None and similarity_to_primary >= SIMILARITY_THRESHOLD:
            status = "merge_candidate"
            merge_target = primary.rel_path
            reason = f"High-overlap durable note that should be merged into {primary.rel_path}."
            merge_candidates.append(note.rel_path)
        elif primary is not None:
            status = "supporting"
            reason = "Supporting note under an existing canonical or primary topic note."
            supporting.append(note.rel_path)
        else:
            status = "orphan_supporting"
            reason = "Durable note without a canonical topic owner yet."
            orphan_paths.append(note.rel_path)

        note_states[note.rel_path] = {
            "topic": topic,
            "status": status,
            "category": note.category,
            "primary_topic_note": primary.rel_path if primary else "",
            "merge_target": merge_target,
            "similarity_to_primary": round(similarity_to_primary, 4),
            "reason": reason,
            "source_slug": note.source_slug,
        }

    recommended_actions: List[str] = []
    if topic_status == "needs_canonical" and primary is not None:
        recommended_actions.append(f"Promote {primary.rel_path} to canonical metadata or fold it into a new canonical topic note.")
    if merge_candidates and primary is not None:
        recommended_actions.append(f"Merge {len(merge_candidates)} supporting note(s) into {primary.rel_path}.")
    if stale_notes:
        recommended_actions.append(f"Retire {len(stale_notes)} legacy live feed note(s) from active retrieval.")

    return {
        "topic": topic,
        "topic_status": topic_status,
        "primary_path": primary.rel_path if primary else "",
        "canonical_paths": [note.rel_path for note in canonical_notes],
        "supporting_paths": supporting,
        "merge_candidate_paths": merge_candidates,
        "orphan_paths": orphan_paths,
        "monitor_paths": [note.rel_path for note in monitor_notes],
        "stale_paths": [note.rel_path for note in stale_notes],
        "recommended_actions": recommended_actions,
        "note_states": note_states,
    }


def build_registry(output_dir: Path, phase6_decisions: Path) -> Dict[str, Any]:
    notes = collect_notes(output_dir)
    decisions = load_json(phase6_decisions, {"items": []})

    topics: Dict[str, List[NoteRecord]] = defaultdict(list)
    note_states: Dict[str, Dict[str, Any]] = {}

    for note in notes:
        topic_key = note.topic or "__untagged__"
        topics[topic_key].append(note)

    topic_entries: List[Dict[str, Any]] = []
    for topic in sorted(topics):
        cluster = topic_cluster(topic, topics[topic])
        topic_entries.append({key: value for key, value in cluster.items() if key != "note_states"})
        note_states.update(cluster["note_states"])

    approved_count = sum(1 for item in decisions.get("items", []) if item.get("status") == "approve")
    rejected_count = sum(1 for item in decisions.get("items", []) if item.get("status") == "reject")
    held_count = sum(1 for item in decisions.get("items", []) if item.get("status") == "hold")

    state_counter = Counter(entry["status"] for entry in note_states.values())
    health = {
        "topics_total": len(topic_entries),
        "healthy_topics": sum(1 for entry in topic_entries if entry["topic_status"] == "healthy"),
        "topics_needing_canonical": sum(1 for entry in topic_entries if entry["topic_status"] == "needs_canonical"),
        "monitor_only_topics": sum(1 for entry in topic_entries if entry["topic_status"] == "monitor_only"),
        "legacy_only_topics": sum(1 for entry in topic_entries if entry["topic_status"] == "legacy_only"),
        "note_status_counts": dict(sorted(state_counter.items())),
        "approved_promotions": approved_count,
        "rejected_promotions": rejected_count,
        "held_promotions": held_count,
    }

    recommended_actions: List[str] = []
    for entry in topic_entries:
        recommended_actions.extend(entry["recommended_actions"])

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(output_dir),
        "phase6_decisions": str(phase6_decisions),
        "health": health,
        "topics": topic_entries,
        "notes": note_states,
        "recommended_actions": recommended_actions[:30],
    }


def build_health_report(registry: Dict[str, Any]) -> str:
    health = registry["health"]
    lines = [
        "---",
        "source: local phase7 canonical synthesis",
        "title: SEO Memory Health Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase7_merge_canon, memory_health, canonical_registry",
        "topic: memory_health",
        "intent: maintenance, canonical_synthesis, decay_control",
        "role: pinchy, researcher, seo",
        "confidence: high",
        "canonical: false",
        "canonical_group: Memory health",
        "use_for: memory_maintenance, canonical_review, decay_control",
        "avoid_for: direct_strategy_without_note_review",
        "---",
        "",
        "# SEO Memory Health Report",
        "",
        f"Topics total: {health['topics_total']}",
        f"Healthy topics: {health['healthy_topics']}",
        f"Topics needing canonical synthesis: {health['topics_needing_canonical']}",
        f"Monitor-only topics: {health['monitor_only_topics']}",
        f"Legacy-only topics: {health['legacy_only_topics']}",
        f"Approved promotions: {health['approved_promotions']}",
        f"Rejected promotions: {health['rejected_promotions']}",
        f"Held promotions: {health['held_promotions']}",
        "",
        "## Status Counts",
    ]
    for status, count in sorted(health["note_status_counts"].items()):
        lines.append(f"- {status}: {count}")

    lines.extend(["", "## Priority Actions"])
    actions = registry.get("recommended_actions", [])
    if not actions:
        lines.append("- No urgent canonical synthesis actions were detected.")
    else:
        for action in actions[:12]:
            lines.append(f"- {action}")

    lines.extend(["", "## Topics Needing Canonical Synthesis"])
    topic_rows = [entry for entry in registry["topics"] if entry["topic_status"] == "needs_canonical"]
    if not topic_rows:
        lines.append("- No topics are currently missing a canonical durable note.")
    else:
        for entry in topic_rows[:12]:
            lines.append(f"- `{entry['topic']}` -> primary candidate `{entry['primary_path']}`")

    lines.extend(["", "## Legacy Decay Targets"])
    stale_rows = [entry for entry in registry["topics"] if entry["stale_paths"]]
    if not stale_rows:
        lines.append("- No legacy live-feed decay targets detected.")
    else:
        for entry in stale_rows[:12]:
            lines.append(f"- `{entry['topic']}` -> {len(entry['stale_paths'])} stale legacy note(s)")

    return "\n".join(lines) + "\n"


def run(output_dir: Path, phase6_decisions: Path, phase7_dir: Path) -> Dict[str, Any]:
    phase7_dir.mkdir(parents=True, exist_ok=True)
    registry = build_registry(output_dir, phase6_decisions)

    registry_path = phase7_dir / "canonical_registry.json"
    report_path = phase7_dir / "memory_health_report.md"
    write_json(registry_path, registry)
    report_path.write_text(build_health_report(registry))

    result = {
        "generated_at": registry["generated_at"],
        "phase7_dir": str(phase7_dir),
        "registry_path": str(registry_path),
        "report_path": str(report_path),
        "health": registry["health"],
        "topics": len(registry["topics"]),
    }
    manifest_path = phase7_dir / f"phase7-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase7_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Registry: {result['registry_path']}")
    print(f"Report: {result['report_path']}")
    print(f"Topics: {result['topics']}")
    print(f"Healthy topics: {result['health']['healthy_topics']}")
    print(f"Topics needing canonical synthesis: {result['health']['topics_needing_canonical']}")


def main() -> int:
    args = parse_args()
    result = run(
        output_dir=Path(args.output_dir),
        phase6_decisions=Path(args.phase6_decisions),
        phase7_dir=Path(args.phase7_dir),
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
