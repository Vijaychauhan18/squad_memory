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


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_PHASE13 = BASE / "ingest" / "phase13" / "latest.json"
DEFAULT_PHASE14_DIR = BASE / "ingest" / "phase14"
DEFAULT_DECISIONS = DEFAULT_PHASE14_DIR / "decisions.json"
DEFAULT_STATE = DEFAULT_PHASE14_DIR / "state.json"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

STATUS_VALUES = {"approve", "reject", "hold"}
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
HEADING_RE = re.compile(r"^## (?P<title>.+?)\s*$", re.MULTILINE)
SOURCE_ARTICLE_RE = re.compile(r"^Source article: \[(?P<title>[^\]]+)\]\((?P<link>[^)]+)\)\s*$", re.MULTILINE)
SOURCE_CANON_RE = re.compile(r"^Source canon: `(?P<link>[^`]+)`\s*$", re.MULTILINE)
PUBLISHED_RE = re.compile(r"^Published: (?P<value>.+?)\s*$", re.MULTILINE)
DOMAIN_RE = re.compile(r"^Domain: (?P<value>.+?)\s*$", re.MULTILINE)
SOURCE_TOPIC_RE = re.compile(r"^Source topic: (?P<value>.+?)\s*$", re.MULTILINE)

MEMORY_BEGIN = "<!-- BEGIN AUTO APPROVED EXTERNAL PROMOTIONS -->"
MEMORY_END = "<!-- END AUTO APPROVED EXTERNAL PROMOTIONS -->"

DOMAIN_LABELS = {
    "writer": "Writer",
    "marketing": "Marketing",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 14 reviewed promotion of approved writer and marketing drafts")
    parser.add_argument("--phase13-manifest", default=str(DEFAULT_PHASE13))
    parser.add_argument("--phase14-dir", default=str(DEFAULT_PHASE14_DIR))
    parser.add_argument("--decisions-path", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--state-path", default=str(DEFAULT_STATE))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--approve", action="append", default=[])
    parser.add_argument("--reject", action="append", default=[])
    parser.add_argument("--hold", action="append", default=[])
    parser.add_argument("--build-db", action="store_true")
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
    raw = meta.get(key, "")
    return [item.strip() for item in raw.split(",") if item.strip()]


def build_frontmatter(meta: Dict[str, str]) -> str:
    return "---\n" + "\n".join(f"{key}: {value}" for key, value in meta.items()) + "\n---\n\n"


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
    phase13_manifest: Dict[str, Any],
    decisions_path: Path,
    approve: Sequence[str],
    reject: Sequence[str],
    hold: Sequence[str],
) -> Dict[str, Any]:
    tracked = phase13_manifest.get("tracked_candidates", [])
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
                "domain": candidate.get("domain", prior.get("domain", "")),
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
                "routing": candidate.get("routing", prior.get("routing", {})),
                "tracked": True,
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
    items = sorted(merged.values(), key=lambda item: (item.get("domain", ""), item.get("status", "hold"), item.get("draft_filename", "")))

    payload = {
        "generated_at": now,
        "phase13_manifest": phase13_manifest.get("manifest_path") or phase13_manifest.get("phase13_dir", ""),
        "defaults": {"status": "hold"},
        "items": items,
    }
    write_json(decisions_path, payload)
    return payload


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


def parse_draft(path: Path) -> Dict[str, Any]:
    text = path.read_text()
    meta, body = parse_frontmatter(text)
    article_match = SOURCE_ARTICLE_RE.search(body)
    canon_match = SOURCE_CANON_RE.search(body)
    title = article_match.group("title").strip() if article_match else meta.get("title", path.stem)
    link = article_match.group("link").strip() if article_match else meta.get("source", "")
    return {
        "meta": meta,
        "title": title,
        "link": link,
        "canon_path": canon_match.group("link").strip() if canon_match else "",
        "published": inline_value(PUBLISHED_RE, body),
        "domain": inline_value(DOMAIN_RE, body),
        "source_topic": inline_value(SOURCE_TOPIC_RE, body),
        "source_signal": extract_section(body, "Source Signal"),
        "draft_summary": [line.strip("- ").strip() for line in extract_section(body, "Draft Summary").splitlines() if line.strip()],
        "why_queue": [line.strip("- ").strip() for line in extract_section(body, "Why This Candidate Is In Queue").splitlines() if line.strip()],
        "placement": [line.strip("- ").strip() for line in extract_section(body, "Suggested Placement").splitlines() if line.strip()],
    }


def build_promoted_note(draft_path: Path, decision: Dict[str, Any], approved_at: str) -> str:
    draft = parse_draft(draft_path)
    meta = draft["meta"]
    domain = decision.get("domain") or draft["domain"]
    label = DOMAIN_LABELS.get(domain, domain.title() if domain else "Domain")
    title = draft["title"]
    topic = meta.get("topic", decision.get("draft_topic", "external_signal"))
    use_for = meta.get("use_for", "durable_note_review, source_selection")
    roles = meta.get("role", "pinchy")
    tags = [
        "durable_note",
        f"{domain}_pipeline_promoted",
        decision.get("source_slug", ""),
        topic,
    ]

    lines = [
        "---",
        f"source: {draft['link']}",
        f"title: {title}",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        f"tags: {', '.join([tag for tag in tags if tag])}",
        f"topic: {topic}",
        f"intent: {meta.get('intent', 'research, monitoring')}",
        f"role: {roles}",
        f"confidence: {meta.get('confidence', 'medium')}",
        "canonical: false",
        f"canonical_group: {label} approved external promotions",
        f"use_for: {use_for}",
        "avoid_for: blind_reuse_without_source_check",
        f"promoted_from: phase13/{draft_path.name}",
        "promotion_status: approved",
        f"approved_on: {approved_at[:10]}",
        "---",
        "",
        f"# {title}",
        "",
        f"Source article: [{title}]({draft['link']})",
    ]
    if draft["canon_path"]:
        lines.append(f"Source canon: `{draft['canon_path']}`")
    lines.extend(
        [
            f"Published: {draft['published'] or decision.get('published', '')}",
            f"Domain: {domain}",
            f"Promoted from draft: `{draft_path.name}`",
            f"Approved at: {approved_at}",
            "",
            "## Core Update",
            draft["source_signal"] or "Open the source article directly before leaning on this note.",
            "",
            "## Why It Matters",
        ]
    )
    for item in draft["draft_summary"] or [f"Fresh durable signal for `{topic}`."]:
        if item.strip():
            lines.append(f"- {item.strip()}")
    lines.extend(["", "## Promotion Context"])
    for item in draft["why_queue"] or ["Approved after Phase 13 review."]:
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
            f"- Use this note when the external {label.lower()} signal is strong enough to influence durable memory.",
            "- Pair it with the source canon note first if you need freshness, chronology, or broader source context.",
            "- Revisit the source article directly if the claim becomes a major planning input.",
        ]
    )
    return "\n".join(lines) + "\n"


def promotion_record(decision: Dict[str, Any], final_path: Path, approved_at: str) -> Dict[str, Any]:
    return {
        "draft_filename": decision["draft_filename"],
        "domain": decision.get("domain", ""),
        "final_filename": final_path.name,
        "final_path": str(final_path),
        "title": decision.get("title", final_path.stem),
        "topic": decision.get("draft_topic", ""),
        "source_slug": decision.get("source_slug", ""),
        "link": decision.get("link", ""),
        "suggested_note": decision.get("routing", {}).get("suggested_note", ""),
        "suggested_bundle": decision.get("routing", {}).get("suggested_bundle", ""),
        "promoted_at": approved_at,
        "status": "approved",
    }


def insert_or_replace(text: str, begin: str, end: str, block: str, anchor: str) -> str:
    wrapped = f"{begin}\n{block.rstrip()}\n{end}"
    if begin in text and end in text:
        start = text.index(begin)
        finish = text.index(end, start) + len(end)
        return text[:start] + wrapped + text[finish:]
    if anchor in text:
        return text.replace(anchor, f"{wrapped}\n\n{anchor}", 1)
    return text.rstrip() + "\n\n" + wrapped + "\n"


def memory_block(domain: str, approved_records: Sequence[Dict[str, Any]]) -> str:
    label = DOMAIN_LABELS[domain]
    lines = [
        f"## Approved {label} Promotions",
        "",
        "### Durable Notes Promoted From External Sources",
    ]
    if not approved_records:
        lines.append(f"- No approved {domain} promotions yet.")
    for item in approved_records[:20]:
        lines.append(
            f"- {item['title']}: `memory/{item['final_filename']}` | source={item.get('source_slug', '')} | topic={item.get('topic', '')}"
        )
    lines.extend(
        [
            "",
            "Use these notes only after the promotion gate has been explicitly approved.",
        ]
    )
    return "\n".join(lines)


def refresh_router_blocks(skills_root: Path, approved_records: Sequence[Dict[str, Any]]) -> None:
    for domain in DOMAIN_LABELS:
        router_path = skills_root / domain / "MEMORY.md"
        if not router_path.exists():
            continue
        records = [item for item in approved_records if item.get("domain") == domain]
        text = router_path.read_text()
        if records or (MEMORY_BEGIN in text and MEMORY_END in text):
            text = insert_or_replace(text, MEMORY_BEGIN, MEMORY_END, memory_block(domain, records), "## Routing Guide")
            router_path.write_text(text)


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
        "source: local phase14 promotion review",
        "title: Writer Marketing Promotion Review",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase14_promote, promotion_review, approval_gate, writer, marketing",
        "topic: writer_marketing_durable_promotion",
        "intent: review, approval, durable_promotion",
        "role: pinchy, writer, marketing, charles",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Writer marketing promotion review",
        "use_for: approval_state, promoted_notes, review_summary",
        "avoid_for: direct_strategy_without_note_review",
        "---",
        "",
        "# Writer Marketing Promotion Review",
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
        lines.append(f"- `{item['final_filename']}` | domain={item.get('domain', '')} | source={item.get('source_slug', '')}")

    lines.extend(["", "## Approved Durable Library"])
    if not approved_records:
        lines.append("- No approved durable notes yet.")
    for item in approved_records[:20]:
        lines.append(f"- `{item['final_filename']}` | domain={item.get('domain', '')} | promoted_at={item.get('promoted_at', '')}")

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


def promote_approved(
    phase13_manifest: Dict[str, Any],
    phase14_dir: Path,
    decisions_path: Path,
    state_path: Path,
    skills_root: Path,
    db_path: Path,
    build_db: bool,
    approve: Sequence[str],
    reject: Sequence[str],
    hold: Sequence[str],
) -> Dict[str, Any]:
    phase14_dir.mkdir(parents=True, exist_ok=True)
    decisions = sync_decisions(phase13_manifest, decisions_path, approve, reject, hold)
    state = load_json(state_path, {"promoted_drafts": {}})
    promoted_drafts: Dict[str, Dict[str, Any]] = state.get("promoted_drafts", {})

    drafts_dir = Path(phase13_manifest.get("phase13_dir", phase14_dir.parent / "phase13")) / "drafts"
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

        domain = decision.get("domain", "")
        if domain not in DOMAIN_LABELS:
            skipped.append({"draft_filename": draft_filename, "reason": "missing or invalid domain"})
            continue

        output_dir = skills_root / domain / "memory"
        output_dir.mkdir(parents=True, exist_ok=True)
        final_filename = decision.get("final_filename") or draft_filename
        final_path = output_dir / final_filename

        existing = promoted_drafts.get(draft_filename)
        if existing and Path(existing["final_path"]) == final_path and final_path.exists():
            skipped.append({"draft_filename": draft_filename, "reason": "already promoted"})
            continue
        if final_path.exists() and not existing:
            conflicts.append({"draft_filename": draft_filename, "reason": "final file already exists"})
            continue

        approved_at = datetime.now(timezone.utc).isoformat()
        final_path.write_text(build_promoted_note(draft_path, decision, approved_at))
        record = promotion_record(decision, final_path, approved_at)
        promoted_drafts[draft_filename] = record
        decision["promoted_path"] = str(final_path)
        decision["reviewed_at"] = approved_at
        promoted_now.append(record)

    state["promoted_drafts"] = promoted_drafts
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_json(state_path, state)
    write_json(decisions_path, decisions)

    approved_records = sorted(promoted_drafts.values(), key=lambda item: item.get("promoted_at", ""), reverse=True)
    refresh_router_blocks(skills_root, approved_records)

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
        "phase13_manifest": phase13_manifest.get("manifest_path", str(DEFAULT_PHASE13)),
        "phase14_dir": str(phase14_dir),
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
        "review_note": str(write_review_note(phase14_dir / "review-status.md", decisions, approved_records, promoted_now, skipped, conflicts)),
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase14_dir / f"phase14-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase14_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Review note: {result['review_note']}")
    print(f"Promoted now: {len(result['promoted_now'])}")
    print(f"Approved total: {result['approved_total']}")
    if result.get("build"):
        print(result["build"]["stdout"])
    for item in result["promoted_now"]:
        print(f"- {item['title']} | domain={item.get('domain', '')} | final={item['final_filename']}")


def main() -> int:
    args = parse_args()
    phase13_manifest = load_json(Path(args.phase13_manifest), {})
    if not phase13_manifest:
        raise SystemExit(f"Missing Phase 13 manifest: {args.phase13_manifest}")
    result = promote_approved(
        phase13_manifest=phase13_manifest,
        phase14_dir=Path(args.phase14_dir),
        decisions_path=Path(args.decisions_path),
        state_path=Path(args.state_path),
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
