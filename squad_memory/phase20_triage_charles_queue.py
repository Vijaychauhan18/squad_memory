#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_PHASE19 = BASE / "ingest" / "phase19" / "latest.json"
DEFAULT_PHASE20_DIR = BASE / "ingest" / "phase20"
DEFAULT_DECISIONS = BASE / "ingest" / "phase19" / "decisions.json"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
HEADING_RE = re.compile(r"^## (?P<title>.+?)\s*$", re.MULTILINE)

LOW_SIGNAL_PATTERNS = [
    (re.compile(r"\bstatistics?\b", re.IGNORECASE), 0.22, "Stats-heavy list content is often weak as durable Charles memory unless it changes operating behavior."),
    (re.compile(r"\bneed to know\b", re.IGNORECASE), 0.16, "Generic 'need to know' framing usually signals broad listicle content."),
    (re.compile(r"\bweekly\b", re.IGNORECASE), 0.18, "Weekly or recap-style content tends to decay too fast for durable memory."),
    (re.compile(r"\bupdate\b", re.IGNORECASE), 0.12, "Short-term update framing often belongs in monitoring, not durable canon."),
    (re.compile(r"\bnews\b", re.IGNORECASE), 0.12, "News framing is usually too perishable for durable Charles notes."),
    (re.compile(r"\b\d+\+\b"), 0.08, "Number-heavy list framing can indicate a broad checklist rather than a durable operating principle."),
]

EVERGREEN_KEYWORDS = {
    "workflow",
    "system",
    "framework",
    "format",
    "formats",
    "platform",
    "platforms",
    "native",
    "posting",
    "repurposing",
    "creator",
    "engagement",
    "calendar",
    "trend",
    "trends",
    "adapt",
    "adaptation",
    "distribution",
}

STALE_FEATURE_KEYWORDS = {
    "verified business account",
    "local feed",
    "new feature",
    "feature",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 20 Charles queue triage suggestions")
    parser.add_argument("--phase19-manifest", default=str(DEFAULT_PHASE19))
    parser.add_argument("--decisions-path", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--phase20-dir", default=str(DEFAULT_PHASE20_DIR))
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


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


def extract_section(body: str, heading: str) -> str:
    matches = list(HEADING_RE.finditer(body))
    for index, match in enumerate(matches):
        if match.group("title") != heading:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        return body[start:end].strip()
    return ""


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9][a-z0-9+\-]{1,}", text.lower())


def parse_draft(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    return {
        "meta": meta,
        "source_signal": extract_section(body, "Source Signal"),
        "draft_summary": [line.strip("- ").strip() for line in extract_section(body, "Draft Summary").splitlines() if line.strip()],
        "why_queue": [line.strip("- ").strip() for line in extract_section(body, "Why This Candidate Is In Queue").splitlines() if line.strip()],
    }


def triage_item(item: Dict[str, Any], draft: Dict[str, Any]) -> Dict[str, Any]:
    title = str(item.get("title", ""))
    summary = " ".join(draft.get("draft_summary", [])[:2]) or draft.get("source_signal", "")
    source_topic = str(item.get("draft_topic", ""))
    base_score = float(item.get("score", 0.0) or 0.0)
    tokens = set(tokenize(f"{title}\n{summary}"))

    adjusted = base_score
    reasons: List[str] = [f"Base Phase 18 promotion score: {base_score:.2f}."]

    evergreen_hits = len(tokens & EVERGREEN_KEYWORDS)
    if evergreen_hits >= 3:
        adjusted += 0.08
        reasons.append("Strong evergreen operating keywords suggest reusable social workflow value.")
    elif evergreen_hits >= 1:
        adjusted += 0.03
        reasons.append("Some evergreen social-operation signals are present.")

    for pattern, penalty, reason in LOW_SIGNAL_PATTERNS:
        if pattern.search(title):
            adjusted -= penalty
            reasons.append(reason)

    lower_summary = summary.lower()
    if source_topic == "platform_changes" and any(keyword in lower_summary for keyword in STALE_FEATURE_KEYWORDS):
        adjusted -= 0.08
        reasons.append("Feature-specific platform detail may decay quickly and may belong in monitoring instead of durable memory.")

    if source_topic == "social_distribution" and {"format", "formats", "posting", "platform", "platforms", "creator"} & tokens:
        adjusted += 0.05
        reasons.append("This aligns directly with Charles platform-native execution and repurposing concerns.")

    adjusted = round(max(0.0, min(adjusted, 1.0)), 4)

    if adjusted >= 0.9:
        recommendation = "approve_suggested"
        priority = "high"
    elif adjusted <= 0.64:
        recommendation = "reject_suggested"
        priority = "high"
    else:
        recommendation = "hold"
        priority = "medium" if adjusted >= 0.76 else "low"

    return {
        "draft_filename": item.get("draft_filename", ""),
        "title": title,
        "source_slug": item.get("source_slug", ""),
        "current_status": item.get("status", "hold"),
        "recommendation": recommendation,
        "priority": priority,
        "triage_score": adjusted,
        "reasoning": reasons,
    }


def build_report(items: Sequence[Dict[str, Any]]) -> str:
    approve = [item for item in items if item["recommendation"] == "approve_suggested"]
    hold = [item for item in items if item["recommendation"] == "hold"]
    reject = [item for item in items if item["recommendation"] == "reject_suggested"]

    lines = [
        "---",
        "source: local phase20 charles queue triage",
        "title: Charles Queue Triage Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase20_triage, charles, queue_review",
        "topic: charles_queue_triage",
        "intent: maintenance, review, approval_support",
        "role: pinchy, charles, current, marketing",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Charles queue triage",
        "use_for: approval_support, queue_cleanup",
        "avoid_for: direct_auto_promotion",
        "---",
        "",
        "# Charles Queue Triage Report",
        "",
        f"- Approve suggested: {len(approve)}",
        f"- Hold: {len(hold)}",
        f"- Reject suggested: {len(reject)}",
        "",
        "## Approve Suggested",
    ]
    if not approve:
        lines.append("- No approve-suggested items.")
    for item in sorted(approve, key=lambda row: (-row["triage_score"], row["draft_filename"])):
        lines.append(f"- `{item['draft_filename']}` | triage={item['triage_score']:.2f} | priority={item['priority']}")
        for reason in item["reasoning"][:3]:
            lines.append(f"  {reason}")
    lines.extend(["", "## Hold"])
    if not hold:
        lines.append("- No hold items.")
    for item in sorted(hold, key=lambda row: (-row["triage_score"], row["draft_filename"])):
        lines.append(f"- `{item['draft_filename']}` | triage={item['triage_score']:.2f} | priority={item['priority']}")
        for reason in item["reasoning"][:3]:
            lines.append(f"  {reason}")
    lines.extend(["", "## Reject Suggested"])
    if not reject:
        lines.append("- No reject-suggested items.")
    for item in sorted(reject, key=lambda row: (row["triage_score"], row["draft_filename"])):
        lines.append(f"- `{item['draft_filename']}` | triage={item['triage_score']:.2f} | priority={item['priority']}")
        for reason in item["reasoning"][:3]:
            lines.append(f"  {reason}")
    return "\n".join(lines).rstrip() + "\n"


def run(phase19_manifest: Path, decisions_path: Path, phase20_dir: Path) -> Dict[str, Any]:
    manifest = load_json(phase19_manifest, {})
    decisions = load_json(decisions_path, {"items": []})
    if not manifest:
        raise SystemExit(f"Missing Phase 19 manifest: {phase19_manifest}")

    phase20_dir.mkdir(parents=True, exist_ok=True)
    phase18_dir = Path(str(manifest.get("phase18_manifest", ""))).parent if manifest.get("phase18_manifest") else phase20_dir.parent / "phase18"
    drafts_dir = phase18_dir / "drafts"

    triaged_items: List[Dict[str, Any]] = []
    updated_items: List[Dict[str, Any]] = []
    for item in decisions.get("items", []):
        enriched = dict(item)
        draft_path = drafts_dir / item.get("draft_filename", "")
        if item.get("status") == "hold" and draft_path.exists():
            draft = parse_draft(draft_path)
            triage = triage_item(item, draft)
            enriched["triage_recommendation"] = triage["recommendation"]
            enriched["triage_priority"] = triage["priority"]
            enriched["triage_score"] = triage["triage_score"]
            enriched["triage_reasoning"] = triage["reasoning"]
            enriched["triaged_at"] = datetime.now(timezone.utc).isoformat()
            triaged_items.append(triage)
        updated_items.append(enriched)

    decisions["items"] = updated_items
    decisions["triage_updated_at"] = datetime.now(timezone.utc).isoformat()
    write_json(decisions_path, decisions)

    triage_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase19_manifest": str(phase19_manifest),
        "decisions_path": str(decisions_path),
        "items": triaged_items,
    }
    triage_path = phase20_dir / "triage.json"
    write_json(triage_path, triage_payload)

    report_path = phase20_dir / "triage-report.md"
    report_path.write_text(build_report(triaged_items), encoding="utf-8")

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase19_manifest": str(phase19_manifest),
        "decisions_path": str(decisions_path),
        "phase20_dir": str(phase20_dir),
        "triage_path": str(triage_path),
        "report_path": str(report_path),
        "approve_suggested": len([item for item in triaged_items if item["recommendation"] == "approve_suggested"]),
        "hold": len([item for item in triaged_items if item["recommendation"] == "hold"]),
        "reject_suggested": len([item for item in triaged_items if item["recommendation"] == "reject_suggested"]),
        "items": triaged_items,
    }
    manifest_path = phase20_dir / f"phase20-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase20_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    print(f"Approve suggested: {result['approve_suggested']}")
    print(f"Hold: {result['hold']}")
    print(f"Reject suggested: {result['reject_suggested']}")


def main() -> int:
    args = parse_args()
    result = run(Path(args.phase19_manifest), Path(args.decisions_path), Path(args.phase20_dir))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
