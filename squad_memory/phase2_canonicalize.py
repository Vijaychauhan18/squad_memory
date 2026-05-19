#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


HOME = Path("/Users/vijaychauhan")
DEFAULT_CONFIG = HOME / "squad_memory" / "knowledge_sources.json"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_RUNS_DIR = HOME / "squad_memory" / "ingest" / "runs"
DEFAULT_STATE_PATH = HOME / "squad_memory" / "ingest" / "state.json"
DEFAULT_PHASE2_DIR = HOME / "squad_memory" / "ingest" / "phase2"

NOTE_PATTERNS = ("live-source-*.md", "live-seo-feed-*.md")
ITEM_RE = re.compile(r"^- (?P<published>[^|]+?) \| \[(?P<title>[^\]]+)\]\((?P<link>[^)]+)\)")
FIELD_RE = re.compile(r"^(?P<key>[A-Za-z ]+): (?P<value>.+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 2 canonicalization for knowledge ingestion")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    parser.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR))
    parser.add_argument("--phase2-dir", default=str(DEFAULT_PHASE2_DIR))
    parser.add_argument("--top", type=int, default=5)
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


def meta_list(meta: Dict[str, str], *keys: str) -> List[str]:
    for key in keys:
        value = meta.get(key)
        if not value:
            continue
        return [item.strip() for item in value.split(",") if item.strip()]
    return []


def load_config(path: Path) -> Dict[str, Dict[str, Any]]:
    payload = load_json(path, {"sources": []})
    return {item["slug"]: item for item in payload.get("sources", []) if item.get("slug")}


def candidate_live_notes(output_dir: Path) -> List[Path]:
    notes: List[Path] = []
    for pattern in NOTE_PATTERNS:
        notes.extend(sorted(output_dir.glob(pattern)))
    by_slug: Dict[str, Path] = {}
    for path in notes:
        if path.name.endswith("-monitor.md"):
            continue
        if path.name.startswith("live-source-canon"):
            continue
        if path.name == "live-source-cluster-report.md":
            continue
        if path.name == "live-knowledge-monitor.md":
            continue
        slug = slug_from_note(path)
        existing = by_slug.get(slug)
        if existing is None:
            by_slug[slug] = path
            continue
        existing_is_fresh = existing.name.startswith("live-source-")
        current_is_fresh = path.name.startswith("live-source-")
        if current_is_fresh and not existing_is_fresh:
            by_slug[slug] = path
    return [by_slug[key] for key in sorted(by_slug)]


def slug_from_note(path: Path) -> str:
    name = path.stem
    if name.startswith("live-source-"):
        return name[len("live-source-") :]
    if name.startswith("live-seo-feed-"):
        return name[len("live-seo-feed-") :]
    return name


def parse_live_note(path: Path) -> Dict[str, Any]:
    meta, body = parse_frontmatter(path.read_text())
    fields: Dict[str, str] = {}
    items: List[Dict[str, str]] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        match = FIELD_RE.match(line)
        if match:
            fields[match.group("key").strip().lower()] = match.group("value").strip()
            continue
        item_match = ITEM_RE.match(line)
        if item_match:
            items.append(
                {
                    "published": item_match.group("published").strip(),
                    "title": item_match.group("title").strip(),
                    "link": item_match.group("link").strip(),
                }
            )
    return {
        "meta": meta,
        "body": body,
        "fields": fields,
        "items": items,
    }


def topic_focus(topic: str) -> str:
    mapping = {
        "seo_research": "Use for large-sample studies, benchmark framing, and data-backed SEO operations.",
        "quality_systems": "Use for quality-system interpretation, ranking architecture, and trust diagnostics.",
        "ai_reverse_engineering": "Use for grounding, selection-rate, fan-out, and machine-readability diagnostics.",
        "official_guidance": "Use for policy boundaries, Search Console changes, and official Google guidance.",
        "industry_news": "Use for fast monitoring, rollout chronology, and broad industry coverage.",
        "daily_monitoring": "Use for same-day change detection and confirmation of search rollout chatter.",
        "relevance_engineering": "Use for retrieval, embeddings, semantic competition, and AI search systems.",
        "technical_architecture": "Use for rendering, structured data, performance, and information architecture.",
        "operations_and_international": "Use for international SEO operations, planning, and market-by-market adaptation.",
        "trust_and_rag": "Use for trust interpretation, grounding quality, and AI answer reliability.",
        "rollout_and_qrg": "Use for rollout timing, QRG implications, and AI content policy interpretation.",
    }
    return mapping.get(topic, "Use for live monitoring, source selection, and deciding what deserves a durable note.")


def agent_checklist(source_cfg: Dict[str, Any], latest_titles: Sequence[str]) -> List[str]:
    topic = source_cfg.get("topic", "")
    shared = [
        "Capture the strongest new claim or data point before using the source in strategy advice.",
        "Map the update to an existing canonical note or create a new durable note if the signal is material.",
        "Use this source for freshness first, then cross-check with canonical memory before giving final guidance.",
    ]
    specific: List[str]
    if topic == "ai_reverse_engineering":
        specific = [
            "Extract any new terms around grounding, selection rate, or query fan-out.",
            "Convert any diagnostic workflow into a checklist or experiment hypothesis.",
        ]
    elif topic in {"quality_systems", "trust_and_rag", "rollout_and_qrg"}:
        specific = [
            "Link the update to quality systems, trust interpretation, or rater-guideline implications.",
            "Check whether the source changes how Coral or Pinchy should explain ranking behavior.",
        ]
    elif topic in {"official_guidance", "technical_architecture"}:
        specific = [
            "Flag any official requirement, eligibility rule, or technical implementation constraint.",
            "Prioritize exact dates and product names when policy or reporting changes are involved.",
        ]
    else:
        specific = [
            "Watch for studies, tooling changes, or market shifts that should influence reporting and prioritization.",
            "Pull out one reusable workflow or metric change if the update is operationally meaningful.",
        ]
    if latest_titles:
        specific.append(f"Start with the newest title: {latest_titles[0]}")
    return specific + shared


def build_canonical_note(
    slug: str,
    source_cfg: Dict[str, Any],
    parsed: Dict[str, Any],
    note_path: Path,
    top_n: int,
) -> str:
    meta = parsed["meta"]
    fields = parsed["fields"]
    items = parsed["items"][:top_n]
    title = source_cfg.get("name") or meta.get("title", slug)
    topic = source_cfg.get("topic") or meta.get("topic", "live_source_ingest")
    roles = source_cfg.get("roles") or meta_list(meta, "role", "roles") or ["researcher", "seo", "pinchy"]
    intent = source_cfg.get("intent") or meta_list(meta, "intent", "intents") or ["monitoring", "research", "source_selection"]
    confidence = source_cfg.get("confidence") or meta.get("confidence", "medium")
    strengths = source_cfg.get("strength", "")
    latest_titles = [item["title"] for item in items]
    checklist = agent_checklist(source_cfg, latest_titles)

    lines = [
        "---",
        f"source: {source_cfg.get('homepage', meta.get('source', ''))}",
        f"title: Live Source Canon - {title}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: live_source_canon, phase2_canonical, {slug}",
        f"topic: {topic}",
        f"intent: {', '.join(intent)}",
        f"role: {', '.join(roles)}",
        f"confidence: {confidence}",
        "canonical: true",
        "canonical_group: Live source canon",
        "use_for: freshness, source_selection, summary_first, monitoring",
        "avoid_for: final_strategy_without_supporting_memory",
        "---",
        "",
        f"# Live Source Canon - {title}",
        "",
        f"Source note: [{note_path.name}](./{note_path.name})",
        f"Homepage: {source_cfg.get('homepage', '')}",
        f"Source kind: {source_cfg.get('kind', 'publication')}",
        f"Latest published date: {fields.get('latest published date', items[0]['published'] if items else 'unknown')}",
        f"New items since last run: {fields.get('new items since last run', 'unknown')}",
        "",
        "## Best Use",
        topic_focus(topic),
        "",
        "## Source Strength",
        strengths or "Use this source for live monitoring and route it into a durable note only when the update is materially new.",
        "",
        "## Latest Signals",
    ]

    if not items:
        lines.append("- No recent items were parsed from the live source note.")
    for item in items:
        lines.append(f"- {item['published']} | [{item['title']}]({item['link']})")

    lines.extend(["", "## Agent Checklist"])
    for bullet in checklist:
        lines.append(f"- {bullet}")

    lines.extend(["", "## Promotion Rule"])
    lines.append(
        "- Promote a new durable memory note only if the update adds a new method, metric, product change, or interpretation not already covered by the canonical library."
    )
    return "\n".join(lines) + "\n"


def build_monitor_note(results: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "---",
        "source: local phase2 canonicalizer",
        "title: Live Source Canon Monitor",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: live_source_canon, phase2_canonical, monitoring",
        "topic: live_source_monitor",
        "intent: monitoring, routing, source_selection",
        "role: researcher, seo, pinchy",
        "confidence: medium",
        "canonical: true",
        "canonical_group: Live source canon",
        "use_for: source_selection, freshness, overview",
        "avoid_for: final_strategy_without_supporting_memory",
        "---",
        "",
        "# Live Source Canon Monitor",
        "",
        "Use this note to choose which live source canon note to open first.",
        "",
        "## Current Canon Notes",
    ]
    for item in results:
        lines.append(
            f"- [{item['canonical_filename']}](./{item['canonical_filename']}) | {item['name']} | latest={item['latest_published'] or 'unknown'} | items={item['item_count']}"
        )
    return "\n".join(lines) + "\n"


def canonicalize(config_path: Path, output_dir: Path, state_path: Path, runs_dir: Path, phase2_dir: Path, top_n: int) -> Dict[str, Any]:
    config = load_config(config_path)
    state = load_json(state_path, {"sources": {}})
    notes = candidate_live_notes(output_dir)
    phase2_dir.mkdir(parents=True, exist_ok=True)

    results: List[Dict[str, Any]] = []
    for note_path in notes:
        slug = slug_from_note(note_path)
        source_cfg = config.get(slug, {"slug": slug, "name": slug.replace("-", " ").title(), "topic": "live_source_ingest", "roles": ["researcher", "seo", "pinchy"], "intent": ["monitoring", "research"], "confidence": "medium"})
        parsed = parse_live_note(note_path)
        canonical_filename = f"live-source-canon-{slug}.md"
        canonical_path = output_dir / canonical_filename
        canonical_path.write_text(build_canonical_note(slug, source_cfg, parsed, note_path, top_n))
        source_state = state.get("sources", {}).get(slug, {})
        results.append(
            {
                "slug": slug,
                "name": source_cfg.get("name", slug),
                "live_note": str(note_path),
                "canonical_filename": canonical_filename,
                "canonical_path": str(canonical_path),
                "latest_published": source_state.get("latest_published", parsed["fields"].get("latest published date", "")),
                "item_count": len(parsed["items"]),
                "topic": source_cfg.get("topic", "live_source_ingest"),
            }
        )

    monitor_filename = "live-source-canon.md"
    monitor_path = output_dir / monitor_filename
    monitor_path.write_text(build_monitor_note(results))

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    manifest = {
        "run_id": run_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(output_dir),
        "state_path": str(state_path),
        "results": results,
        "monitor_note": str(monitor_path),
    }
    write_json(phase2_dir / f"phase2-{run_id}.json", manifest)
    write_json(phase2_dir / "latest.json", manifest)
    return manifest


def print_manifest(manifest: Dict[str, Any]) -> None:
    print(f"Run ID: {manifest['run_id']}")
    print(f"Monitor note: {manifest['monitor_note']}")
    for item in manifest["results"]:
        print(
            f"- {item['name']}: canonical={Path(item['canonical_path']).name} latest={item['latest_published'] or 'unknown'} items={item['item_count']}"
        )


def main() -> int:
    args = parse_args()
    manifest = canonicalize(
        config_path=Path(args.config),
        output_dir=Path(args.output_dir),
        state_path=Path(args.state_path),
        runs_dir=Path(args.runs_dir),
        phase2_dir=Path(args.phase2_dir),
        top_n=args.top,
    )
    if args.json:
        print(json.dumps(manifest, indent=2, ensure_ascii=True))
    else:
        print_manifest(manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
