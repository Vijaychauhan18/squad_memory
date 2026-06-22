#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from phase7_merge_canon import run as run_phase7
from phase8_promote_canon import run as run_phase8


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE6_DECISIONS = BASE / "ingest" / "phase6" / "decisions.json"
DEFAULT_PHASE7_REGISTRY = BASE / "ingest" / "phase7" / "canonical_registry.json"
DEFAULT_PHASE7_DIR = BASE / "ingest" / "phase7"
DEFAULT_PHASE8_DIR = BASE / "ingest" / "phase8"
DEFAULT_PHASE9_DIR = BASE / "ingest" / "phase9"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_\-]{1,}")
HEADING_RE = re.compile(r"^##\s+(Core Concept|Core Update)\s*$", re.MULTILINE)
PHASE9_BEGIN = "<!-- phase9:begin -->"
PHASE9_END = "<!-- phase9:end -->"

TOPIC_RULES: Dict[str, Dict[str, float]] = {
    "ai_visibility": {
        "ai visibility": 0.28,
        "geo": 0.18,
        "aeo": 0.18,
        "answer engine": 0.18,
        "ai search": 0.16,
        "chatgpt": 0.10,
        "citation": 0.10,
        "citations": 0.10,
        "ai seo": 0.14,
    },
    "ai_overviews": {
        "ai overview": 0.28,
        "ai overviews": 0.28,
        "featured snippet": 0.10,
        "featured snippets": 0.10,
    },
    "aio_click_loss": {
        "zero-click": 0.28,
        "zero click": 0.28,
        "ctr": 0.16,
        "click loss": 0.18,
        "traffic loss": 0.18,
        "position study": 0.14,
    },
    "brand_visibility": {
        "brand visibility": 0.28,
        "brand marketing": 0.24,
        "brand guide": 0.20,
        "entity": 0.12,
        "brand voice": 0.12,
    },
    "brand_mentions": {
        "brand mentions": 0.26,
        "pr campaign": 0.18,
        "online reputation": 0.18,
        "backlink": 0.16,
        "backlinks": 0.16,
        "link building": 0.16,
        "youtube": 0.10,
    },
    "multisurface_visibility": {
        "brand radar": 0.30,
        "multisurface": 0.22,
        "search demand": 0.12,
        "sales channel": 0.12,
        "topic association": 0.12,
    },
    "keyword_research": {
        "keyword": 0.18,
        "keywords": 0.18,
        "intent": 0.16,
        "grouping": 0.16,
        "buyer intent": 0.22,
        "youtube keyword": 0.20,
    },
    "content_strategy": {
        "content decay": 0.28,
        "blog post": 0.16,
        "product page": 0.14,
        "ecommerce": 0.10,
        "content strategy": 0.16,
    },
    "technical_architecture": {
        "mobile-first": 0.24,
        "wordpress": 0.18,
        "plugin": 0.12,
        "plugins": 0.12,
        "core web vitals": 0.10,
        "technical": 0.10,
    },
    "seo_research": {
        "enterprise seo": 0.22,
        "competitive analysis": 0.20,
        "competitor analysis": 0.20,
        "niche market": 0.18,
        "alternative search engines": 0.18,
        "seo visibility": 0.14,
    },
    "seo_execution": {
        "seo checklist": 0.18,
        "wordpress seo": 0.18,
        "how to write": 0.14,
    },
    "ai_reverse_engineering": {
        "query fan-out": 0.30,
        "fan-out": 0.22,
        "fanout": 0.22,
        "reverse prompting": 0.22,
        "selection rate": 0.18,
        "grounding": 0.16,
    },
    "click_behavior_systems": {
        "craps": 0.30,
        "navboost": 0.26,
        "perdocdata": 0.20,
        "popularity signal": 0.18,
    },
    "document_quality_system": {
        "page quality": 0.28,
        "content effort": 0.24,
        "compositedoc": 0.22,
        "compressedqualitysignals": 0.22,
        "document quality": 0.18,
    },
    "site_trust_system": {
        "quality raters": 0.20,
        "e-e-a-t": 0.16,
        "eeat": 0.16,
        "quality score": 0.18,
        "linkbuilding after leak": 0.18,
        "google updates": 0.16,
    },
    "relevance_system": {
        "topical authority": 0.28,
        "on-page seo": 0.18,
        "topicality": 0.18,
        "relevance": 0.12,
    },
    "scaled_abuse_risk": {
        "scaled abuse": 0.28,
        "firefly": 0.22,
        "goldmine": 0.18,
    },
}

FILENAME_TOPIC_OVERRIDES: Dict[str, str] = {
    "ahrefs-74-percent-new-content-is-ai-generated.md": "seo_research",
    "ahrefs-ai-citations-vs-impressions-study.md": "brand_mentions",
    "ahrefs-ai-overview-citations.md": "ai_overviews",
    "ahrefs-ai-overviews-position-study.md": "ai_overviews",
    "ahrefs-ai-search-traffic-by-page-type.md": "ai_visibility",
    "ahrefs-alternative-search-engines.md": "ai_search_monitoring",
    "ahrefs-answer-engine-optimization.md": "ai_visibility",
    "ahrefs-best-ai-marketing-tools.md": "ai_visibility",
    "ahrefs-black-hat-link-building.md": "brand_mentions",
    "ahrefs-brand-radar-multisurface.md": "multisurface_visibility",
    "ahrefs-buyer-intent-keywords.md": "keyword_research",
    "ahrefs-competitive-analysis-guide.md": "seo_research",
    "ahrefs-ecommerce-product-page-seo.md": "content_strategy",
    "ahrefs-enterprise-seo.md": "seo_execution",
    "ahrefs-fast-link-building.md": "brand_mentions",
    "ahrefs-featured-snippets-study.md": "ai_overviews",
    "ahrefs-high-quality-backlinks.md": "brand_mentions",
    "ahrefs-how-long-seo-takes.md": "seo_research",
    "ahrefs-how-long-to-rank.md": "seo_research",
    "ahrefs-how-to-write-blog-post.md": "content_strategy",
    "ahrefs-insights-from-55-point-8m-ai-overviews.md": "ai_overviews",
    "ahrefs-keyword-grouping.md": "keyword_research",
    "ahrefs-loss-of-seo-visibility.md": "seo_execution",
    "ahrefs-mobile-first-indexing.md": "technical_architecture",
    "ahrefs-new-features-january-2026.md": "seo_execution",
    "ahrefs-niche-market-examples.md": "seo_research",
    "ahrefs-online-reputation-management.md": "brand_mentions",
    "ahrefs-pr-campaign-examples.md": "brand_mentions",
    "ahrefs-query-fan-out.md": "ai_reverse_engineering",
    "ahrefs-seo-brand-marketing.md": "brand_visibility",
    "ahrefs-seo-competitor-analysis.md": "seo_research",
    "ahrefs-what-ai-means-for-seo.md": "ai_visibility",
    "ahrefs-wordpress-seo-plugins.md": "technical_architecture",
    "ahrefs-youtube-keyword-research.md": "keyword_research",
    "hobo-compositedoc.md": "document_quality_system",
    "hobo-compressedqualitysignals.md": "document_quality_system",
    "hobo-content-effort.md": "document_quality_system",
    "hobo-core-web-vitals.md": "technical_architecture",
    "hobo-craps.md": "click_behavior_systems",
    "hobo-goldmine.md": "document_quality_system",
    "hobo-google-updates-mapping.md": "ranking_architecture",
    "hobo-human-quality-raters.md": "site_trust_system",
    "hobo-linkbuilding-after-leak.md": "site_trust_system",
    "hobo-on-page-seo.md": "relevance_system",
    "hobo-page-quality-rating.md": "document_quality_system",
    "hobo-perdocdata.md": "ranking_architecture",
    "hobo-popularity-signal.md": "click_behavior_systems",
    "hobo-topical-authority.md": "relevance_system",
    "hobo-zero-click-marketing.md": "aio_click_loss",
}

SOURCE_PRIORITY = {
    "ahrefs": 9,
    "dejan": 9,
    "hobo": 8,
    "google": 8,
    "gsqi": 7,
    "ipullrank": 7,
    "jono": 6,
}


@dataclass
class NoteDoc:
    rel_path: str
    abs_path: Path
    filename: str
    title: str
    meta: Dict[str, str]
    body: str
    tokens: set[str]
    source_slug: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 9 canonical synthesis and topic redistribution")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase6-decisions", default=str(DEFAULT_PHASE6_DECISIONS))
    parser.add_argument("--phase7-registry", default=str(DEFAULT_PHASE7_REGISTRY))
    parser.add_argument("--phase7-dir", default=str(DEFAULT_PHASE7_DIR))
    parser.add_argument("--phase8-dir", default=str(DEFAULT_PHASE8_DIR))
    parser.add_argument("--phase9-dir", default=str(DEFAULT_PHASE9_DIR))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true", help="Rebuild squad_memory after phase 9 changes")
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


def tokenize(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "item"


def humanize_topic(topic: str) -> str:
    cleaned = topic.replace("__", "_").strip("_")
    return cleaned.replace("_", " ").strip().capitalize() if cleaned else "Canonical note"


def infer_source_slug(filename: str, source_value: str) -> str:
    source_value = source_value.lower()
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
    if "developers.google.com" in source_value or filename.startswith("google-"):
        return "google"
    return slugify(source_value) if source_value else "unknown"


def extract_title(meta: Dict[str, str], body: str, filename: str) -> str:
    if meta.get("title", "").strip():
        return meta["title"].strip()
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return filename.replace("-", " ").replace(".md", "")


def read_note(path: Path) -> Optional[NoteDoc]:
    if path.name == "INDEX.md" or path.name.startswith("live-source-") or path.name.startswith("live-seo-feed-"):
        return None
    text = path.read_text(errors="ignore")
    meta, body = parse_frontmatter(text)
    title = extract_title(meta, body, path.name)
    token_text = " ".join(
        part
        for part in (title, meta.get("tags", ""), meta.get("use_for", ""), body[:2500])
        if part
    )
    return NoteDoc(
        rel_path=f"seo/memory/{path.name}",
        abs_path=path,
        filename=path.name,
        title=title,
        meta=meta,
        body=body,
        tokens=tokenize(token_text),
        source_slug=infer_source_slug(path.name, meta.get("source", "")),
    )


def similarity(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    intersection = len(left & right)
    union = len(left | right)
    return intersection / union if union else 0.0


def build_topic_profiles(output_dir: Path, registry: Dict[str, Any]) -> Dict[str, set[str]]:
    profiles: Dict[str, set[str]] = {}
    for entry in registry.get("topics", []):
        if entry.get("topic_status") != "healthy":
            continue
        primary_path = str(entry.get("primary_path", "")).strip()
        if not primary_path:
            continue
        abs_path = output_dir / Path(primary_path).name
        if not abs_path.exists():
            continue
        note = read_note(abs_path)
        if note is None:
            continue
        topic = str(entry.get("topic", "")).strip()
        if topic:
            profiles[topic] = note.tokens | tokenize(topic)
    return profiles


def heuristic_scores(note: NoteDoc) -> Dict[str, float]:
    haystack = " ".join(
        part
        for part in (note.title, note.meta.get("tags", ""), note.body[:2000])
        if part
    ).lower()
    scores: Dict[str, float] = {}
    for topic, patterns in TOPIC_RULES.items():
        score = 0.0
        for phrase, weight in patterns.items():
            if phrase in haystack:
                score += weight
        if score:
            scores[topic] = score
    return scores


def default_topic_for(note: NoteDoc) -> str:
    title = f"{note.title} {note.meta.get('tags', '')}".lower()
    if "keyword" in title or "intent" in title:
        return "keyword_research"
    if "content" in title or "blog" in title:
        return "content_strategy"
    if "brand" in title:
        return "brand_visibility"
    if "link" in title or "backlink" in title or "reputation" in title:
        return "brand_mentions"
    if "technical" in title or "wordpress" in title or "mobile-first" in title:
        return "technical_architecture"
    if note.source_slug == "hobo":
        return "relevance_system"
    if note.source_slug == "ahrefs":
        return "seo_research"
    return "seo_execution"


def infer_topic(note: NoteDoc, profiles: Dict[str, set[str]]) -> Tuple[str, float, str]:
    override = FILENAME_TOPIC_OVERRIDES.get(note.filename)
    if override:
        return override, 1.0, "filename_override"
    scores = heuristic_scores(note)
    for topic, profile_tokens in profiles.items():
        sim = similarity(note.tokens, profile_tokens)
        if sim:
            scores[topic] = scores.get(topic, 0.0) + sim
    if not scores:
        fallback = default_topic_for(note)
        return fallback, 0.01, "fallback"
    topic, score = max(scores.items(), key=lambda item: item[1])
    reason = "heuristic+profile" if topic in heuristic_scores(note) else "profile"
    if score < 0.10:
        fallback = default_topic_for(note)
        return fallback, score, "fallback"
    return topic, score, reason


def update_frontmatter(path: Path, updates: Dict[str, str]) -> bool:
    text = path.read_text()
    meta, body = parse_frontmatter(text)
    header_lines = []
    for key, value in meta.items():
        header_lines.append(f"{key}: {value}")
    key_index: Dict[str, int] = {}
    for idx, line in enumerate(header_lines):
        if ":" in line:
            key_index[line.split(":", 1)[0].strip().lower()] = idx

    changed = False
    for key, value in updates.items():
        new_line = f"{key}: {value}"
        if key in key_index:
            idx = key_index[key]
            if header_lines[idx] != new_line:
                header_lines[idx] = new_line
                changed = True
        else:
            header_lines.append(new_line)
            changed = True
            key_index[key] = len(header_lines) - 1

    if not changed:
        return False
    rebuilt = "---\n" + "\n".join(header_lines).rstrip() + "\n---\n\n" + body.lstrip("\n")
    path.write_text(rebuilt)
    return True


def replace_managed_block(body: str, block: str) -> str:
    managed = f"{PHASE9_BEGIN}\n{block.rstrip()}\n{PHASE9_END}"
    pattern = re.compile(r"\n?<!-- phase9:begin -->.*?<!-- phase9:end -->\n?", re.DOTALL)
    if pattern.search(body):
        updated = pattern.sub("\n\n" + managed + "\n", body).rstrip() + "\n"
        return updated
    return body.rstrip() + "\n\n" + managed + "\n"


def write_note_body(path: Path, body_transform) -> bool:
    text = path.read_text()
    meta, body = parse_frontmatter(text)
    new_body = body_transform(body)
    if new_body == body:
        return False
    if meta:
        header = "---\n" + "\n".join(f"{key}: {value}" for key, value in meta.items()) + "\n---\n\n"
        path.write_text(header + new_body.lstrip("\n"))
    else:
        path.write_text(new_body)
    return True


def extract_core_concept(body: str) -> str:
    match = HEADING_RE.search(body)
    if not match:
        lines: List[str] = []
        for raw_line in body.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            line = re.sub(r"^#+\s*", "", line)
            if line.lower().startswith(("source article:", "source canon:", "published:", "promoted from draft:", "approved at:")):
                continue
            lines.append(line)
        return lines[0] if lines else ""
    remainder = body[match.end() :].strip()
    if not remainder:
        return ""
    paragraph = remainder.split("\n\n", 1)[0].strip()
    return re.sub(r"\s+", " ", paragraph)


def primary_sort_key(note: NoteDoc) -> Tuple[int, int, str]:
    canonical = 1 if note.meta.get("canonical", "").lower() in {"true", "yes", "1"} else 0
    source_priority = SOURCE_PRIORITY.get(note.source_slug, 0)
    return (canonical, source_priority, note.filename)


def collect_notes(output_dir: Path) -> Dict[str, NoteDoc]:
    notes: Dict[str, NoteDoc] = {}
    for path in sorted(output_dir.glob("*.md")):
        note = read_note(path)
        if note is not None:
            notes[note.rel_path] = note
    return notes


def infer_topics_for_untagged(output_dir: Path, registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    notes = collect_notes(output_dir)
    profiles = build_topic_profiles(output_dir, registry)
    changes: List[Dict[str, Any]] = []
    for note in sorted(notes.values(), key=lambda item: item.filename):
        has_topic = bool(note.meta.get("topic", "").strip())
        phase9_owned = note.meta.get("topic_assigned_by", "").strip() == "phase9_merge_summaries"
        if has_topic and not phase9_owned:
            continue
        inferred_topic, score, reason = infer_topic(note, profiles)
        current_topic = note.meta.get("topic", "").strip()
        did_change = update_frontmatter(
            note.abs_path,
            {
                "topic": inferred_topic,
                "topic_assigned_by": "phase9_merge_summaries",
                "topic_assigned_on": datetime.now(timezone.utc).date().isoformat(),
            },
        )
        if did_change or current_topic != inferred_topic:
            changes.append(
                {
                    "path": note.rel_path,
                    "title": note.title,
                    "previous_topic": current_topic,
                    "topic": inferred_topic,
                    "score": round(score, 4),
                    "reason": reason,
                }
            )
    return changes


def build_synthesis_block(topic_entry: Dict[str, Any], notes: Dict[str, NoteDoc]) -> str:
    merge_paths = list(topic_entry.get("merge_candidate_paths", []))
    supporting_paths = list(topic_entry.get("supporting_paths", []))
    related_paths = merge_paths + supporting_paths
    limited_paths = related_paths[:8]
    lines = [
        "## Canonical Synthesis",
        "",
        f"This canonical note is reinforced by {len(merge_paths)} merge candidate(s) and {len(supporting_paths)} supporting note(s) in the local memory library.",
        "",
        "### Supporting Note Digest",
    ]
    if not limited_paths:
        lines.append("- No supporting notes are currently linked to this canonical topic.")
    for rel_path in limited_paths:
        note = notes.get(rel_path)
        if note is None:
            continue
        summary = extract_core_concept(note.body) or note.title
        summary = summary.rstrip(".")
        lines.append(f"- `{Path(rel_path).name}`: {summary}.")
    remaining = len(related_paths) - len(limited_paths)
    if remaining > 0:
        lines.append(f"- `{remaining}` more supporting note(s) remain attached to this topic in the canonical registry.")
    lines.extend(
        [
            "",
            "### Retrieval Guidance",
            "- Start with this note for the topic baseline and open the supporting notes only when you need source-specific evidence or edge cases.",
            "- Use the attached digest to avoid re-reading overlapping notes during planning and research.",
        ]
    )
    return "\n".join(lines)


def refresh_synthesis_blocks(output_dir: Path, registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    notes = collect_notes(output_dir)
    changes: List[Dict[str, Any]] = []
    for entry in registry.get("topics", []):
        if entry.get("topic_status") != "healthy":
            continue
        if not entry.get("merge_candidate_paths") and not entry.get("supporting_paths"):
            continue
        primary_path = str(entry.get("primary_path", "")).strip()
        if not primary_path:
            continue
        note = notes.get(primary_path)
        if note is None:
            continue
        block = build_synthesis_block(entry, notes)
        did_change = write_note_body(note.abs_path, lambda body, block=block: replace_managed_block(body, block))
        if did_change:
            changes.append(
                {
                    "topic": entry["topic"],
                    "primary_path": primary_path,
                    "merge_candidates": len(entry.get("merge_candidate_paths", [])),
                    "supporting": len(entry.get("supporting_paths", [])),
                }
            )
    return changes


def build_report(
    topic_changes: List[Dict[str, Any]],
    phase8_result: Dict[str, Any],
    synthesis_updates: List[Dict[str, Any]],
    registry: Dict[str, Any],
) -> str:
    health = registry["health"]
    lines = [
        "---",
        "source: local phase9 canonical synthesis",
        "title: Canonical Summary Merge Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase9_merge_summaries, topic_inference, canonical_synthesis",
        "topic: canonical_synthesis",
        "intent: maintenance, canonical_synthesis, routing_cleanup",
        "role: pinchy, researcher, seo",
        "confidence: high",
        "canonical: false",
        "canonical_group: Canonical synthesis",
        "use_for: memory_maintenance, canonical_cleanup, summary_refresh",
        "avoid_for: direct_strategy_without_note_review",
        "---",
        "",
        "# Canonical Summary Merge Report",
        "",
        f"Topic assignments updated: {len(topic_changes)}",
        f"Phase 8 canonical promotions triggered: {len(phase8_result.get('changed', []))}",
        f"Canonical synthesis blocks refreshed: {len(synthesis_updates)}",
        f"Healthy topics after refresh: {health['healthy_topics']}",
        f"Topics needing canonical synthesis: {health['topics_needing_canonical']}",
        "",
        "## Topic Reassignments",
    ]
    if not topic_changes:
        lines.append("- No untagged durable notes required reassignment in this run.")
    for item in topic_changes[:30]:
        lines.append(f"- `{item['path']}` -> `{item['topic']}` | score={item['score']:.4f} | reason={item['reason']}")

    lines.extend(["", "## Phase 8 Canonical Promotions"])
    if not phase8_result.get("changed"):
        lines.append("- No new canonical promotions were needed after topic reassignment.")
    else:
        for item in phase8_result["changed"]:
            lines.append(f"- `{item['path']}` -> `{item['canonical_group']}`")

    lines.extend(["", "## Canonical Notes Refreshed"])
    if not synthesis_updates:
        lines.append("- No canonical synthesis blocks were updated.")
    for item in synthesis_updates:
        lines.append(
            f"- `{item['primary_path']}` | topic=`{item['topic']}` | merge={item['merge_candidates']} | supporting={item['supporting']}"
        )
    return "\n".join(lines) + "\n"


def run(
    output_dir: Path,
    phase6_decisions: Path,
    phase7_registry: Path,
    phase7_dir: Path,
    phase8_dir: Path,
    phase9_dir: Path,
    skills_root: Path,
    db_path: Path,
    build_db: bool,
) -> Dict[str, Any]:
    phase9_dir.mkdir(parents=True, exist_ok=True)
    initial_registry = load_json(phase7_registry, {"topics": [], "notes": {}, "health": {}})

    topic_changes = infer_topics_for_untagged(output_dir, initial_registry)
    refreshed_phase7 = run_phase7(output_dir=output_dir, phase6_decisions=phase6_decisions, phase7_dir=phase7_dir)
    refreshed_registry = load_json(phase7_dir / "canonical_registry.json", {"topics": [], "notes": {}, "health": {}})

    phase8_result = run_phase8(
        output_dir=output_dir,
        phase6_decisions=phase6_decisions,
        phase7_registry=phase7_dir / "canonical_registry.json",
        phase7_dir=phase7_dir,
        phase8_dir=phase8_dir,
        skills_root=skills_root,
        db_path=db_path,
        build_db=False,
    )
    post_phase8_registry = load_json(phase7_dir / "canonical_registry.json", refreshed_registry)
    synthesis_updates = refresh_synthesis_blocks(output_dir, post_phase8_registry)

    build_result = None
    if build_db and (topic_changes or phase8_result.get("changed") or synthesis_updates):
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

    report_path = phase9_dir / "canonical_summary_merge_report.md"
    report_path.write_text(build_report(topic_changes, phase8_result, synthesis_updates, post_phase8_registry))

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase9_dir": str(phase9_dir),
        "report_path": str(report_path),
        "topic_changes": topic_changes,
        "phase7": refreshed_phase7,
        "phase8": {
            "changed": phase8_result.get("changed", []),
            "skipped": phase8_result.get("skipped", []),
            "report_path": phase8_result.get("report_path", ""),
        },
        "synthesis_updates": synthesis_updates,
        "health": post_phase8_registry.get("health", {}),
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase9_dir / f"phase9-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase9_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    print(f"Topic changes: {len(result['topic_changes'])}")
    print(f"Phase 8 promotions: {len(result['phase8']['changed'])}")
    print(f"Synthesis updates: {len(result['synthesis_updates'])}")
    print(f"Healthy topics: {result['health'].get('healthy_topics', 0)}")
    print(f"Topics needing canonical synthesis: {result['health'].get('topics_needing_canonical', 0)}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = run(
        output_dir=Path(args.output_dir),
        phase6_decisions=Path(args.phase6_decisions),
        phase7_registry=Path(args.phase7_registry),
        phase7_dir=Path(args.phase7_dir),
        phase8_dir=Path(args.phase8_dir),
        phase9_dir=Path(args.phase9_dir),
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
