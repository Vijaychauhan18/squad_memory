#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_PHASE27 = BASE / "ingest" / "phase27" / "latest.json"
DEFAULT_PHASE28_DIR = BASE / "ingest" / "phase28"
DEFAULT_DECISIONS = BASE / "ingest" / "phase27" / "decisions.json"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
HEADING_RE = re.compile(r"^## (?P<title>.+?)\s*$", re.MULTILINE)
VERSION_RE = re.compile(r"\bv?\d+\.\d+(?:\.\d+)?\b", re.IGNORECASE)

LOW_SIGNAL_PATTERNS: List[Tuple[re.Pattern[str], float, str]] = [
    (
        re.compile(r"\bfragments?\b", re.IGNORECASE),
        0.18,
        "Digest or fragments framing is usually weaker as durable developer memory.",
    ),
    (
        re.compile(r"\bweekly\b|\broundup\b|\brecap\b", re.IGNORECASE),
        0.18,
        "Recap-style content tends to decay too fast for durable engineering memory.",
    ),
    (
        re.compile(r"\bcopied a prompt\b|\bborrowed idea\b", re.IGNORECASE),
        0.14,
        "Prompt anecdote framing can be interesting, but it is often too personal or situational for durable canon.",
    ),
    (
        re.compile(r"\bmentorship\b", re.IGNORECASE),
        0.05,
        "Mentorship essays can help context, but they are often softer than implementation or QA operating notes.",
    ),
]

DOMAIN_EVERGREEN: Dict[str, set[str]] = {
    "developer": {
        "architecture",
        "code",
        "design",
        "implementation",
        "maintainability",
        "pattern",
        "patterns",
        "refactor",
        "refactoring",
        "review",
        "reliability",
        "safe",
        "small",
        "tdd",
        "testing",
        "workflow",
    },
    "qa": {
        "automation",
        "coverage",
        "e2e",
        "edge",
        "flake",
        "matrix",
        "mcp",
        "playwright",
        "quality",
        "regression",
        "release",
        "repro",
        "test",
        "testing",
        "tooling",
        "trace",
        "verification",
    },
}

DOMAIN_APPROVE_SIGNALS: Dict[str, set[str]] = {
    "developer": {
        "code",
        "design",
        "implementation",
        "maintainability",
        "patterns",
        "refactor",
        "review",
        "tdd",
        "workflow",
    },
    "qa": {
        "assistant",
        "cloud",
        "coverage",
        "mcp",
        "regression",
        "test",
        "testing",
        "tooling",
        "trace",
        "verification",
    },
}

DOMAIN_RELEASE_SIGNALS: Dict[str, set[str]] = {
    "developer": {"release", "releases", "version", "versions"},
    "qa": {"browser", "fix", "patch", "release", "releases", "version", "versions"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 28 developer and QA queue triage suggestions")
    parser.add_argument("--phase27-manifest", default=str(DEFAULT_PHASE27))
    parser.add_argument("--decisions-path", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--phase28-dir", default=str(DEFAULT_PHASE28_DIR))
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
        "placement": [line.strip("- ").strip() for line in extract_section(body, "Suggested Placement").splitlines() if line.strip()],
    }


def triage_item(item: Dict[str, Any], draft: Dict[str, Any]) -> Dict[str, Any]:
    title = str(item.get("title", ""))
    domain = str(item.get("domain", "")).strip().lower()
    source_topic = str(item.get("draft_topic", ""))
    base_score = float(item.get("score", 0.0) or 0.0)
    summary = " ".join(draft.get("draft_summary", [])[:2]) or draft.get("source_signal", "")
    tokens = set(tokenize(f"{title}\n{summary}"))
    adjusted = base_score
    reasons: List[str] = [f"Base Phase 26 promotion score: {base_score:.2f}."]

    evergreen_hits = len(tokens & DOMAIN_EVERGREEN.get(domain, set()))
    if evergreen_hits >= 4:
        adjusted += 0.08
        reasons.append("Strong evergreen operating keywords suggest durable engineering workflow value.")
    elif evergreen_hits >= 2:
        adjusted += 0.04
        reasons.append("Some durable engineering workflow signals are present.")

    approve_hits = len(tokens & DOMAIN_APPROVE_SIGNALS.get(domain, set()))
    if source_topic in {"engineering_patterns", "testing_patterns"} and approve_hits >= 2:
        adjusted += 0.06
        reasons.append("The source topic and keywords align directly with durable implementation or QA practice.")
    elif domain == "qa" and {"assistant", "mcp", "trace", "runs"} & tokens:
        adjusted += 0.08
        reasons.append("This looks like a reusable testing workflow shift, not just a one-off release note.")

    for pattern, penalty, reason in LOW_SIGNAL_PATTERNS:
        if pattern.search(title):
            adjusted -= penalty
            reasons.append(reason)

    if domain == "qa" and source_topic == "test_tooling":
        if VERSION_RE.search(title):
            adjusted -= 0.16
            reasons.append("Pure versioned release notes usually belong in monitoring, not durable QA canon.")
        elif len(tokens & DOMAIN_RELEASE_SIGNALS["qa"]) >= 2:
            adjusted -= 0.08
            reasons.append("Release-focused QA notes often need stronger workflow implications before promotion.")

    if domain == "developer" and source_topic == "engineering_systems":
        if {"mentorship", "maintainers", "open", "source"} & tokens:
            adjusted -= 0.04
            reasons.append("This is broader systems thinking and may need a clearer implementation angle before promotion.")

    adjusted = round(max(0.0, min(adjusted, 1.0)), 4)
    if adjusted >= 0.86:
        recommendation = "approve_suggested"
        priority = "high"
    elif adjusted <= 0.63:
        recommendation = "reject_suggested"
        priority = "high"
    else:
        recommendation = "hold"
        priority = "medium" if adjusted >= 0.74 else "low"

    return {
        "draft_filename": item.get("draft_filename", ""),
        "domain": domain,
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
        "source: local phase28 developer-qa queue triage",
        "title: Developer QA Queue Triage Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase28_triage, developer, qa, queue_review",
        "topic: developer_qa_queue_triage",
        "intent: maintenance, review, approval_support",
        "role: pinchy, developer, qa, reviewer, devops",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Developer QA queue triage",
        "use_for: approval_support, queue_cleanup",
        "avoid_for: direct_auto_promotion",
        "---",
        "",
        "# Developer QA Queue Triage Report",
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
        lines.append(
            f"- `{item['draft_filename']}` | domain={item['domain']} | triage={item['triage_score']:.2f} | priority={item['priority']}"
        )
        for reason in item["reasoning"][:3]:
            lines.append(f"  {reason}")
    lines.extend(["", "## Hold"])
    if not hold:
        lines.append("- No hold items.")
    for item in sorted(hold, key=lambda row: (-row["triage_score"], row["draft_filename"])):
        lines.append(
            f"- `{item['draft_filename']}` | domain={item['domain']} | triage={item['triage_score']:.2f} | priority={item['priority']}"
        )
        for reason in item["reasoning"][:3]:
            lines.append(f"  {reason}")
    lines.extend(["", "## Reject Suggested"])
    if not reject:
        lines.append("- No reject-suggested items.")
    for item in sorted(reject, key=lambda row: (row["triage_score"], row["draft_filename"])):
        lines.append(
            f"- `{item['draft_filename']}` | domain={item['domain']} | triage={item['triage_score']:.2f} | priority={item['priority']}"
        )
        for reason in item["reasoning"][:3]:
            lines.append(f"  {reason}")
    return "\n".join(lines).rstrip() + "\n"


def run(phase27_manifest: Path, decisions_path: Path, phase28_dir: Path) -> Dict[str, Any]:
    manifest = load_json(phase27_manifest, {})
    decisions = load_json(decisions_path, {"items": []})
    if not manifest:
        raise SystemExit(f"Missing Phase 27 manifest: {phase27_manifest}")

    phase28_dir.mkdir(parents=True, exist_ok=True)
    phase26_dir = Path(str(manifest.get("phase26_manifest", ""))).parent if manifest.get("phase26_manifest") else phase28_dir.parent / "phase26"
    drafts_dir = phase26_dir / "drafts"

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
        "phase27_manifest": str(phase27_manifest),
        "decisions_path": str(decisions_path),
        "items": triaged_items,
    }
    triage_path = phase28_dir / "triage.json"
    write_json(triage_path, triage_payload)

    report_path = phase28_dir / "triage-report.md"
    report_path.write_text(build_report(triaged_items), encoding="utf-8")

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase27_manifest": str(phase27_manifest),
        "decisions_path": str(decisions_path),
        "phase28_dir": str(phase28_dir),
        "triage_path": str(triage_path),
        "report_path": str(report_path),
        "approve_suggested": len([item for item in triaged_items if item["recommendation"] == "approve_suggested"]),
        "hold": len([item for item in triaged_items if item["recommendation"] == "hold"]),
        "reject_suggested": len([item for item in triaged_items if item["recommendation"] == "reject_suggested"]),
        "items": triaged_items,
    }
    manifest_path = phase28_dir / f"phase28-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase28_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    print(f"Approve suggested: {result['approve_suggested']}")
    print(f"Hold: {result['hold']}")
    print(f"Reject suggested: {result['reject_suggested']}")


def main() -> int:
    args = parse_args()
    result = run(Path(args.phase27_manifest), Path(args.decisions_path), Path(args.phase28_dir))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
