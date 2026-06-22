#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE5 = BASE / "ingest" / "phase5" / "latest.json"
DEFAULT_PHASE6_DIR = BASE / "ingest" / "phase6"
DEFAULT_DECISIONS = DEFAULT_PHASE6_DIR / "decisions.json"
DEFAULT_STATE = DEFAULT_PHASE6_DIR / "state.json"
DEFAULT_MEMORY_ROUTER = HOME / ".codex" / "skills" / "seo" / "MEMORY.md"
DEFAULT_INDEX = DEFAULT_OUTPUT / "INDEX.md"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

MEMORY_BEGIN = "<!-- BEGIN AUTO PROMOTED DRAFTS -->"
MEMORY_END = "<!-- END AUTO PROMOTED DRAFTS -->"
INDEX_BEGIN = "<!-- BEGIN AUTO PROMOTED DRAFTS -->"
INDEX_END = "<!-- END AUTO PROMOTED DRAFTS -->"

HEADING_RE = re.compile(r"^## (?P<title>.+?)\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
SOURCE_ARTICLE_RE = re.compile(r"^Source article: \[(?P<title>[^\]]+)\]\((?P<link>[^)]+)\)\s*$", re.MULTILINE)
SOURCE_CANON_RE = re.compile(r"^Source canon: \[(?P<label>[^\]]+)\]\((?P<link>[^)]+)\)\s*$", re.MULTILINE)
PUBLISHED_RE = re.compile(r"^Published: (?P<value>.+?)\s*$", re.MULTILINE)
SOURCE_TOPIC_RE = re.compile(r"^Source topic: (?P<value>.+?)\s*$", re.MULTILINE)
STATUS_VALUES = {"approve", "reject", "hold"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 6 reviewed promotion of approved durable notes")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase5-manifest", default=str(DEFAULT_PHASE5))
    parser.add_argument("--phase6-dir", default=str(DEFAULT_PHASE6_DIR))
    parser.add_argument("--decisions-path", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--memory-router", default=str(DEFAULT_MEMORY_ROUTER))
    parser.add_argument("--index-path", default=str(DEFAULT_INDEX))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--approve", action="append", default=[], help="Approve a draft filename for promotion")
    parser.add_argument("--reject", action="append", default=[], help="Reject a draft filename")
    parser.add_argument("--hold", action="append", default=[], help="Set a draft filename back to hold")
    parser.add_argument("--build-db", action="store_true", help="Rebuild squad_memory after promoting notes")
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


def meta_list(meta: Dict[str, str], key: str) -> List[str]:
    raw = meta.get(key, "")
    return [item.strip() for item in raw.split(",") if item.strip()]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "item"


def extract_section(body: str, heading: str) -> str:
    matches = list(HEADING_RE.finditer(body))
    for index, match in enumerate(matches):
        if match.group("title") != heading:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        return body[start:end].strip()
    return ""


def inline_value(pattern: re.Pattern[str], text: str) -> str:
    match = pattern.search(text)
    return match.group("value").strip() if match else ""


def normalize_status(value: str) -> str:
    lowered = value.strip().lower()
    if lowered not in STATUS_VALUES:
        return "hold"
    return lowered


def decision_index(items: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {item["draft_filename"]: dict(item) for item in items if item.get("draft_filename")}


def apply_status_overrides(items: Dict[str, Dict[str, Any]], approve: Sequence[str], reject: Sequence[str], hold: Sequence[str]) -> None:
    for status, filenames in (("approve", approve), ("reject", reject), ("hold", hold)):
        for filename in filenames:
            record = items.get(filename)
            if record is None:
                continue
            record["status"] = status


def sync_decisions(
    phase5_manifest: Dict[str, Any],
    decisions_path: Path,
    approve: Sequence[str],
    reject: Sequence[str],
    hold: Sequence[str],
) -> Dict[str, Any]:
    tracked = phase5_manifest.get("tracked_candidates", [])
    existing = load_json(decisions_path, {"items": []})
    existing_index = decision_index(existing.get("items", []))

    synced: List[Dict[str, Any]] = []
    seen: set[str] = set()
    now = datetime.now(timezone.utc).isoformat()

    for candidate in tracked:
        draft_filename = candidate["draft_filename"]
        prior = existing_index.get(draft_filename, {})
        synced.append(
            {
                "draft_filename": draft_filename,
                "title": candidate.get("title", prior.get("title", draft_filename)),
                "link": candidate.get("link", prior.get("link", "")),
                "published": candidate.get("published", prior.get("published", "")),
                "source_slug": candidate.get("source_slug", prior.get("source_slug", "")),
                "draft_topic": candidate.get("draft_topic", prior.get("draft_topic", "")),
                "score": candidate.get("score", prior.get("score", 0.0)),
                "status": normalize_status(prior.get("status", "hold")),
                "final_filename": prior.get("final_filename", draft_filename),
                "review_notes": prior.get("review_notes", ""),
                "promoted_path": prior.get("promoted_path", ""),
                "tracked": True,
                "routing": candidate.get("routing", prior.get("routing", {})),
                "updated_at": now,
            }
        )
        seen.add(draft_filename)

    for draft_filename, prior in existing_index.items():
        if draft_filename in seen:
            continue
        preserved = dict(prior)
        preserved["tracked"] = False
        preserved["status"] = normalize_status(prior.get("status", "hold"))
        preserved["updated_at"] = now
        synced.append(preserved)

    merged = decision_index(synced)
    apply_status_overrides(merged, approve, reject, hold)
    items = sorted(merged.values(), key=lambda item: (item.get("status", "hold"), item.get("draft_filename", "")))

    payload = {
        "generated_at": now,
        "phase5_manifest": phase5_manifest.get("manifest_path") or phase5_manifest.get("phase5_dir", ""),
        "defaults": {"status": "hold"},
        "items": items,
    }
    write_json(decisions_path, payload)
    return payload


def insert_or_replace(text: str, begin: str, end: str, block: str, anchor: str) -> str:
    wrapped = f"{begin}\n{block.rstrip()}\n{end}"
    if begin in text and end in text:
        start = text.index(begin)
        finish = text.index(end, start) + len(end)
        return text[:start] + wrapped + text[finish:]
    if anchor in text:
        return text.replace(anchor, f"{wrapped}\n\n{anchor}", 1)
    return text.rstrip() + "\n\n" + wrapped + "\n"


def parse_draft(path: Path) -> Dict[str, Any]:
    text = path.read_text()
    meta, body = parse_frontmatter(text)

    source_article = SOURCE_ARTICLE_RE.search(body)
    source_canon = SOURCE_CANON_RE.search(body)
    promoted_title = meta.get("title", path.stem).removeprefix("Promotion Candidate - ").strip()
    title = source_article.group("title").strip() if source_article else promoted_title
    link = source_article.group("link").strip() if source_article else meta.get("source", "")
    canon_name = source_canon.group("label").strip() if source_canon else ""
    published = inline_value(PUBLISHED_RE, body)
    source_topic = inline_value(SOURCE_TOPIC_RE, body)

    draft_summary_lines = [line.strip("- ").strip() for line in extract_section(body, "Draft Summary").splitlines() if line.strip()]
    source_signal = extract_section(body, "Source Signal")
    why_queue = [line.strip("- ").strip() for line in extract_section(body, "Why This Candidate Is In Queue").splitlines() if line.strip()]
    placement = [line.strip("- ").strip() for line in extract_section(body, "Suggested Placement").splitlines() if line.strip()]

    return {
        "meta": meta,
        "title": title,
        "link": link,
        "canon_name": canon_name,
        "published": published,
        "source_topic": source_topic,
        "draft_summary": draft_summary_lines,
        "source_signal": source_signal,
        "why_queue": why_queue,
        "placement": placement,
    }


def build_promoted_note(
    draft_path: Path,
    decision: Dict[str, Any],
    approved_at: str,
) -> str:
    draft = parse_draft(draft_path)
    meta = draft["meta"]
    title = draft["title"]
    topic = meta.get("topic", decision.get("draft_topic", "source_canon"))
    intents = meta.get("intent", "research, monitoring")
    roles = meta.get("role", "researcher, seo, pinchy")
    use_for = meta.get("use_for", "source_backed_strategy")
    confidence = meta.get("confidence", "medium")
    tags = [
        "durable_note",
        "live_pipeline_promoted",
        decision.get("source_slug", slugify(topic)),
        slugify(topic),
    ]
    if "source_selection" not in use_for:
        use_for = f"{use_for}, source_selection"

    lines = [
        "---",
        f"source: {draft['link']}",
        f"title: {title}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: {', '.join(dict.fromkeys(tags))}",
        f"topic: {topic}",
        f"intent: {intents}",
        f"role: {roles}",
        f"confidence: {confidence}",
        "canonical: false",
        "canonical_group: Live approved promotions",
        f"use_for: {use_for}",
        "avoid_for: blind_reuse_without_source_check",
        f"promoted_from: phase5/{draft_path.name}",
        f"promotion_status: approved",
        f"approved_on: {approved_at[:10]}",
        "---",
        "",
        f"# {title}",
        "",
        f"Source article: [{title}]({draft['link']})",
    ]
    if draft["canon_name"]:
        lines.append(f"Source canon: [{draft['canon_name']}](./{draft['canon_name']})")
    lines.extend(
        [
            f"Published: {draft['published'] or decision.get('published', '')}",
            f"Promoted from draft: `{draft_path.name}`",
            f"Approved at: {approved_at}",
            "",
            "## Core Update",
            draft["source_signal"] or "Review the source article directly before relying on this note.",
            "",
            "## Why It Matters",
        ]
    )

    draft_summary = draft["draft_summary"] or [
        f"Core update: {title}",
        f"Why it matters: adds a fresh durable angle for `{topic}`.",
    ]
    for item in draft_summary:
        cleaned = item.strip()
        if cleaned:
            lines.append(f"- {cleaned}")

    lines.extend(["", "## Promotion Context"])
    for item in draft["why_queue"] or ["Approved after Phase 5 review."]:
        lines.append(f"- {item}")

    lines.extend(["", "## Routing Hints"])
    for item in draft["placement"]:
        lines.append(f"- {item}")
    if decision.get("review_notes"):
        lines.extend(["", "## Review Notes", decision["review_notes"]])

    lines.extend(
        [
            "",
            "## Squad Use",
            "- Use this note when the live source signal is strong enough to influence durable SEO strategy.",
            "- Pair it with the source canon note first if you need freshness or chronology.",
            "- Revisit the source article directly if the claim becomes a major planning input.",
        ]
    )
    return "\n".join(lines) + "\n"


def promotion_record(decision: Dict[str, Any], final_path: Path, approved_at: str) -> Dict[str, Any]:
    return {
        "draft_filename": decision["draft_filename"],
        "final_filename": final_path.name,
        "final_path": str(final_path),
        "title": decision.get("title", final_path.stem),
        "topic": decision.get("draft_topic", ""),
        "source_slug": decision.get("source_slug", ""),
        "link": decision.get("link", ""),
        "suggested_index_section": decision.get("routing", {}).get("suggested_index_section", ""),
        "suggested_bundle": decision.get("routing", {}).get("suggested_bundle", ""),
        "promoted_at": approved_at,
        "status": "approved",
    }


def promote_approved(
    output_dir: Path,
    phase5_manifest: Dict[str, Any],
    phase6_dir: Path,
    decisions_path: Path,
    state_path: Path,
    memory_router: Path,
    index_path: Path,
    skills_root: Path,
    db_path: Path,
    build_db: bool,
    approve: Sequence[str],
    reject: Sequence[str],
    hold: Sequence[str],
) -> Dict[str, Any]:
    phase6_dir.mkdir(parents=True, exist_ok=True)
    decisions = sync_decisions(phase5_manifest, decisions_path, approve, reject, hold)
    state = load_json(state_path, {"promoted_drafts": {}})
    promoted_drafts: Dict[str, Dict[str, Any]] = state.get("promoted_drafts", {})

    drafts_dir = Path(phase5_manifest.get("phase5_dir", phase6_dir.parent / "phase5")) / "drafts"
    promoted_now: List[Dict[str, Any]] = []
    skipped: List[Dict[str, Any]] = []
    conflicts: List[Dict[str, Any]] = []

    for decision in decisions.get("items", []):
        status = normalize_status(decision.get("status", "hold"))
        draft_filename = decision.get("draft_filename", "")
        if status != "approve" or not draft_filename:
            continue
        draft_path = drafts_dir / draft_filename
        if not draft_path.exists():
            skipped.append({"draft_filename": draft_filename, "reason": "missing draft"})
            continue

        final_filename = decision.get("final_filename") or draft_filename
        final_path = output_dir / final_filename
        existing = promoted_drafts.get(draft_filename)
        if existing and Path(existing["final_path"]) == final_path and final_path.exists():
            skipped.append({"draft_filename": draft_filename, "reason": "already promoted", "final_filename": final_filename})
            continue
        if final_path.exists() and not existing:
            conflicts.append({"draft_filename": draft_filename, "reason": "final file already exists", "final_filename": final_filename})
            continue

        approved_at = datetime.now(timezone.utc).isoformat()
        final_text = build_promoted_note(draft_path, decision, approved_at)
        final_path.write_text(final_text)

        record = promotion_record(decision, final_path, approved_at)
        promoted_drafts[draft_filename] = record
        decision["promoted_path"] = str(final_path)
        decision["reviewed_at"] = approved_at
        promoted_now.append(record)

    state["promoted_drafts"] = promoted_drafts
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_json(state_path, state)
    write_json(decisions_path, decisions)

    approved_records = sorted(
        promoted_drafts.values(),
        key=lambda item: item.get("promoted_at", ""),
        reverse=True,
    )
    refresh_router_blocks(memory_router, index_path, approved_records)

    build_result: Optional[Dict[str, Any]] = None
    if build_db and promoted_now:
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

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase5_manifest": phase5_manifest.get("manifest_path", str(DEFAULT_PHASE5)),
        "phase6_dir": str(phase6_dir),
        "decisions_path": str(decisions_path),
        "state_path": str(state_path),
        "promoted_now": promoted_now,
        "approved_total": len(approved_records),
        "skipped": skipped,
        "conflicts": conflicts,
        "queue": {
            "approved": sum(1 for item in decisions.get("items", []) if item.get("status") == "approve"),
            "rejected": sum(1 for item in decisions.get("items", []) if item.get("status") == "reject"),
            "held": sum(1 for item in decisions.get("items", []) if item.get("status") == "hold"),
        },
        "review_note": str(write_review_note(phase6_dir / "review-status.md", decisions, approved_records, promoted_now, skipped, conflicts)),
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase6_dir / f"phase6-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase6_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def memory_block(approved_records: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "## Approved Live Promotions",
        "",
        "### Durable Notes Promoted From The Live Pipeline",
    ]
    if not approved_records:
        lines.append("- No approved live promotions yet.")
    for item in approved_records[:20]:
        lines.append(
            f"- {item['title']}: `memory/{item['final_filename']}` | source={item.get('source_slug', '')} | topic={item.get('topic', '')}"
        )
    lines.extend(
        [
            "",
            "Use these notes after the promotion gate has been explicitly approved.",
        ]
    )
    return "\n".join(lines)


def index_block(approved_records: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "## Approved Live Promotions",
        f"- Last refresh: {datetime.now(timezone.utc).isoformat()}",
        f"- Approved durable notes: {len(approved_records)}",
        "",
        "| File | Topic | Source | Suggested Section |",
        "|------|-------|--------|-------------------|",
    ]
    if not approved_records:
        lines.append("| None | - | - | - |")
    for item in approved_records[:30]:
        lines.append(
            f"| [{item['final_filename']}](./{item['final_filename']}) | {item.get('topic', '')} | {item.get('source_slug', '')} | {item.get('suggested_index_section', '')} |"
        )
    return "\n".join(lines)


def refresh_router_blocks(memory_router: Path, index_path: Path, approved_records: Sequence[Dict[str, Any]]) -> None:
    memory_text = memory_router.read_text()
    index_text = index_path.read_text()

    if approved_records or (MEMORY_BEGIN in memory_text and MEMORY_END in memory_text):
        memory_text = insert_or_replace(memory_text, MEMORY_BEGIN, MEMORY_END, memory_block(approved_records), "## Routing Guide")
        memory_router.write_text(memory_text)

    if approved_records or (INDEX_BEGIN in index_text and INDEX_END in index_text):
        index_text = insert_or_replace(index_text, INDEX_BEGIN, INDEX_END, index_block(approved_records), "## AI Search & Visibility")
        index_path.write_text(index_text)


def write_review_note(
    path: Path,
    decisions: Dict[str, Any],
    approved_records: Sequence[Dict[str, Any]],
    promoted_now: Sequence[Dict[str, Any]],
    skipped: Sequence[Dict[str, Any]],
    conflicts: Sequence[Dict[str, Any]],
) -> Path:
    lines = [
        "---",
        "source: local phase6 promotion review",
        "title: Durable Memory Promotion Review",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase6_promote, promotion_review, approval_gate",
        "topic: durable_memory_promotion",
        "intent: review, approval, durable_promotion",
        "role: pinchy, researcher, seo",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Promotion review",
        "use_for: approval_state, promoted_notes, review_summary",
        "avoid_for: direct_strategy_without_note_review",
        "---",
        "",
        "# Durable Memory Promotion Review",
        "",
        f"Approved decisions: {sum(1 for item in decisions.get('items', []) if item.get('status') == 'approve')}",
        f"Rejected decisions: {sum(1 for item in decisions.get('items', []) if item.get('status') == 'reject')}",
        f"Held decisions: {sum(1 for item in decisions.get('items', []) if item.get('status') == 'hold')}",
        f"Total promoted durable notes: {len(approved_records)}",
        "",
        "## Promoted This Run",
    ]
    if not promoted_now:
        lines.append("- No new durable notes were promoted in this run.")
    for item in promoted_now:
        lines.append(f"- `{item['final_filename']}` | source={item.get('source_slug', '')} | topic={item.get('topic', '')}")

    lines.extend(["", "## Approved Durable Library"])
    if not approved_records:
        lines.append("- No approved durable notes yet.")
    for item in approved_records[:20]:
        lines.append(f"- `{item['final_filename']}` | promoted_at={item.get('promoted_at', '')}")

    lines.extend(["", "## Skipped"])
    if not skipped:
        lines.append("- No skipped approvals in this run.")
    for item in skipped[:20]:
        lines.append(f"- `{item.get('draft_filename', '')}` | reason={item.get('reason', '')}")

    lines.extend(["", "## Conflicts"])
    if not conflicts:
        lines.append("- No conflicts in this run.")
    for item in conflicts[:20]:
        lines.append(f"- `{item.get('draft_filename', '')}` | reason={item.get('reason', '')}")

    path.write_text("\n".join(lines) + "\n")
    return path


def print_result(result: Dict[str, Any]) -> None:
    print(f"Review note: {result['review_note']}")
    print(f"Promoted now: {len(result['promoted_now'])}")
    print(f"Approved total: {result['approved_total']}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])
    for item in result["promoted_now"]:
        print(f"- {item['title']} | final={item['final_filename']} | source={item.get('source_slug', '')}")


def main() -> int:
    args = parse_args()
    phase5_manifest = load_json(Path(args.phase5_manifest), {})
    if not phase5_manifest:
        raise SystemExit(f"Missing Phase 5 manifest: {args.phase5_manifest}")
    result = promote_approved(
        output_dir=Path(args.output_dir),
        phase5_manifest=phase5_manifest,
        phase6_dir=Path(args.phase6_dir),
        decisions_path=Path(args.decisions_path),
        state_path=Path(args.state_path),
        memory_router=Path(args.memory_router),
        index_path=Path(args.index_path),
        skills_root=Path(args.skills_root),
        db_path=Path(args.db_path),
        build_db=args.build_db,
        approve=args.approve,
        reject=args.reject,
        hold=args.hold,
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
