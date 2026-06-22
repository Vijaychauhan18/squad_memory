#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from phase11_bootstrap_writer_marketing import build_frontmatter, write_note, write_note_body


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE22_DIR = BASE / "ingest" / "phase22"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

PHASE22_BEGIN = "<!-- phase22:begin -->"
PHASE22_END = "<!-- phase22:end -->"

SUPPORT_NOTES: Dict[str, Dict[str, str]] = {
    "fast-first-response-and-severity-triage.md": {
        "title": "Fast First Response And Severity Triage",
        "topic": "support_triage_system",
        "intent": "support_triage, severity, response",
        "role": "support-anemone, pinchy, operations, support",
        "use_for": "first_response, severity_assignment, queue_splitting, sla_routing",
        "avoid_for": "feature_promises, engineering_implementation",
        "canonical_group": "Anemone first response and triage",
    },
    "bug-escalation-and-engineering-handoff.md": {
        "title": "Bug Escalation And Engineering Handoff",
        "topic": "support_bug_handoff",
        "intent": "support_triage, escalation, handoff",
        "role": "support-anemone, pinchy, developer, qa, devops",
        "use_for": "bug_reports, escalation, reproduction_notes, customer_etas",
        "avoid_for": "direct_code_fixes, public_root_cause_without_confirmation",
        "canonical_group": "Anemone bug escalation and handoff",
    },
    "patterns-faq-and-doc-gaps.md": {
        "title": "Patterns FAQ And Documentation Gaps",
        "topic": "support_pattern_logging",
        "intent": "support_triage, documentation, knowledge_base",
        "role": "support-anemone, writer, operations, pinchy",
        "use_for": "faq_updates, repeated_issue_tracking, doc_gap_detection, macro_creation",
        "avoid_for": "one_off_edge_cases_without_pattern",
        "canonical_group": "Anemone pattern logging and docs",
    },
}

ROUTER_NOTES = [
    ("Anemone Operating Canon 2026", "memory/anemone-operating-canon-2026.md"),
    ("Fast First Response And Severity Triage", "memory/fast-first-response-and-severity-triage.md"),
    ("Bug Escalation And Engineering Handoff", "memory/bug-escalation-and-engineering-handoff.md"),
    ("Patterns FAQ And Documentation Gaps", "memory/patterns-faq-and-doc-gaps.md"),
]

ROUTER_BUNDLES = {
    "Anemone": [
        "memory/anemone-operating-canon-2026.md",
        "memory/fast-first-response-and-severity-triage.md",
        "memory/bug-escalation-and-engineering-handoff.md",
    ],
    "Pinchy": [
        "memory/anemone-operating-canon-2026.md",
        "memory/bug-escalation-and-engineering-handoff.md",
    ],
    "Urchin": [
        "memory/anemone-operating-canon-2026.md",
        "memory/patterns-faq-and-doc-gaps.md",
    ],
    "Chitin": [
        "memory/bug-escalation-and-engineering-handoff.md",
        "memory/anemone-operating-canon-2026.md",
    ],
}

PHASE22_CONSENSUS = [
    "Support quality starts with speed plus clarity. A fast, honest first response is part of the fix, not admin overhead.",
    "Severity, reproduction, and escalation belong in one system. Weak support handoffs create weak engineering handoffs.",
    "Repeated questions are a memory and documentation signal. Support should turn repeated pain into FAQ, macro, and product feedback updates.",
]

PHASE22_TENSION = [
    "The main tradeoff is empathy versus precision: vague reassurance feels good briefly, but customers trust faster when support explains status, next step, and owner clearly.",
]

PHASE22_ACTION = (
    "Use the Anemone operating canon first for customer-facing support work, then narrow into triage, escalation, or documentation notes based on the task shape."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 22 support knowledge bootstrap")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase22-dir", default=str(DEFAULT_PHASE22_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def build_triage_note() -> str:
    meta = SUPPORT_NOTES["fast-first-response-and-severity-triage.md"]
    body = [
        build_frontmatter(
            {
                "title": meta["title"],
                "topic": meta["topic"],
                "intent": meta["intent"],
                "role": meta["role"],
                "use_for": meta["use_for"],
                "avoid_for": meta["avoid_for"],
                "confidence": "high",
                "canonical": "true",
                "canonical_group": meta["canonical_group"],
                "source": "local_support_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "support, anemone, triage, severity, first response",
            }
        ).rstrip(),
        "# Fast First Response And Severity Triage",
        "",
        "## Core Concept",
        "Support should acknowledge fast, classify severity clearly, and tell the customer what happens next in the same first reply whenever possible.",
        "",
        "## First Response Rules",
        "- Confirm the issue in plain language so the customer knows they were understood.",
        "- Give the next concrete step or update window, not vague reassurance.",
        "- Ask only the minimum diagnostic questions needed to classify the issue.",
        "",
        "## Severity Rules",
        "- `P0`: service down or broad outage. Escalate immediately to Pinchy and Tide.",
        "- `P1`: broken core feature with active customer impact. Open an engineering handoff and communicate ETA discipline.",
        "- `P2`: contained bug or degraded workflow. Queue with reproduction notes and keep the customer updated.",
        "- `P3`: question, guidance, or low-risk issue. Resolve directly and capture the pattern if it repeats.",
        "",
        "## Squad Use",
        "- **Anemone**: Start here for inbound ticket triage, severity classification, and response timing.",
        "- **Pinchy**: Use this when deciding whether support needs product, engineering, or ops involvement.",
        "- **Urchin**: Use this when queue health or response-time discipline is slipping.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_handoff_note() -> str:
    meta = SUPPORT_NOTES["bug-escalation-and-engineering-handoff.md"]
    body = [
        build_frontmatter(
            {
                "title": meta["title"],
                "topic": meta["topic"],
                "intent": meta["intent"],
                "role": meta["role"],
                "use_for": meta["use_for"],
                "avoid_for": meta["avoid_for"],
                "confidence": "high",
                "canonical": "true",
                "canonical_group": meta["canonical_group"],
                "source": "local_support_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "support, escalation, handoff, developer, qa",
            }
        ).rstrip(),
        "# Bug Escalation And Engineering Handoff",
        "",
        "## Core Concept",
        "Support should not throw raw frustration over the wall. The handoff has to include impact, reproduction, expected behavior, and what the customer has already tried.",
        "",
        "## Handoff Contents",
        "- customer summary and severity",
        "- exact steps to reproduce",
        "- expected result versus actual result",
        "- customer impact and frequency",
        "- screenshots, IDs, or timestamps if available",
        "",
        "## Escalation Rules",
        "- Escalate outages or production incidents to Pinchy plus Tide immediately.",
        "- Pull in Reef when reproduction or regression scope is unclear.",
        "- Do not promise fixes or dates until the owner confirms them.",
        "",
        "## Customer Communication Rules",
        "- Tell the customer the issue is escalated and who owns the next step.",
        "- Give the next update window even when the fix window is unknown.",
        "- Close the loop after the fix and confirm resolution instead of assuming it.",
        "",
        "## Squad Use",
        "- **Anemone**: Use this for reproducible bugs, broken flows, and P1/P2 issues.",
        "- **Chitin**: Use this when translating customer pain into a clean engineering ticket.",
        "- **Reef**: Use this when the handoff needs clearer validation steps.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_patterns_note() -> str:
    meta = SUPPORT_NOTES["patterns-faq-and-doc-gaps.md"]
    body = [
        build_frontmatter(
            {
                "title": meta["title"],
                "topic": meta["topic"],
                "intent": meta["intent"],
                "role": meta["role"],
                "use_for": meta["use_for"],
                "avoid_for": meta["avoid_for"],
                "confidence": "high",
                "canonical": "true",
                "canonical_group": meta["canonical_group"],
                "source": "local_support_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "support, faq, documentation, patterns",
            }
        ).rstrip(),
        "# Patterns FAQ And Documentation Gaps",
        "",
        "## Core Concept",
        "When the same support question appears repeatedly, the real problem is often unclear product messaging, a missing doc, or a weak onboarding moment.",
        "",
        "## Pattern Rules",
        "- Track repeated questions, repeated confusion, and repeated workaround explanations.",
        "- Convert stable answers into FAQ entries, macros, or documentation updates.",
        "- Surface product friction separately from simple education gaps.",
        "",
        "## Update Loop",
        "1. Capture repeated issue patterns weekly.",
        "2. Group them into FAQ, bug, onboarding, or product-feedback buckets.",
        "3. Hand the right bucket to Writer, Chitin, or Pinchy.",
        "4. Check whether the repeated volume drops after the fix or doc update.",
        "",
        "## Squad Use",
        "- **Anemone**: Use this when support volume starts repeating around the same topics.",
        "- **Plankton**: Use this when a repeated support answer should become durable documentation.",
        "- **Urchin**: Use this for queue-level pattern reviews and operational follow-up.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_operating_canon() -> str:
    body = [
        build_frontmatter(
            {
                "title": "Anemone Operating Canon 2026",
                "topic": "support_core",
                "intent": "support_triage, escalation, knowledge_base, customer_response",
                "role": "support-anemone, pinchy, operations, developer, writer",
                "use_for": "support_briefing, triage_routing, escalation_routing, domain_canon",
                "avoid_for": "direct_feature_promises, unauthorized_refunds",
                "confidence": "high",
                "canonical": "true",
                "canonical_group": "Anemone operating canon",
                "source": "local_support_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "support, anemone, operating canon, customer operations",
            }
        ).rstrip(),
        "# Anemone Operating Canon 2026",
        "",
        "## Core Concept",
        "Anemone owns customer support quality end to end: first response speed, severity routing, bug handoff quality, and turning repeated friction into clearer docs and feedback loops.",
        "",
        "## Domain Rules",
        "- Respond quickly, even if the first answer is only the next committed step.",
        "- Severity and ownership must be clear before the ticket leaves support.",
        "- Never promise timelines, refunds, or product commitments without the right owner.",
        "- Repeated issues are system signals. Do not treat the same confusion as isolated tickets forever.",
        "",
        "## Workflow Map",
        "1. Start with `memory/fast-first-response-and-severity-triage.md` for inbound tickets and queue triage.",
        "2. Open `memory/bug-escalation-and-engineering-handoff.md` when the issue is reproducible, technical, or needs engineering involvement.",
        "3. Open `memory/patterns-faq-and-doc-gaps.md` when the task is recurring questions, macros, FAQ growth, or documentation gaps.",
        "",
        "## Team Use",
        "- **Anemone**: Start here for broad support work before narrowing into triage, escalation, or documentation flow.",
        "- **Pinchy**: Use this when support needs orchestration across product, engineering, ops, or comms.",
        "- **Urchin**: Use this when queue patterns or SLA discipline need operational control.",
        "- **Plankton**: Use this when repeated support answers should become durable docs.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_phase22_block() -> str:
    lines = [
        "## Phase 22 Domain Fusion",
        "",
        "Evidence confidence: high",
        "Freshness status: current",
        "",
        "### Consensus",
    ]
    for row in PHASE22_CONSENSUS:
        lines.append(f"- {row}")
    lines.extend(["", "### Tension / Caveat"])
    for row in PHASE22_TENSION:
        lines.append(f"- {row}")
    lines.extend(
        [
            "",
            "### Supporting Notes",
            "- `fast-first-response-and-severity-triage.md`: first response speed, severity, and routing.",
            "- `bug-escalation-and-engineering-handoff.md`: reproducible bug handoffs and customer update discipline.",
            "- `patterns-faq-and-doc-gaps.md`: repeated issue capture, FAQ updates, and documentation loops.",
            "",
            "### Squad Action",
            f"- {PHASE22_ACTION}",
        ]
    )
    return "\n".join(lines)


def replace_phase22_block(body: str, block: str) -> str:
    managed = f"{PHASE22_BEGIN}\n{block.rstrip()}\n{PHASE22_END}"
    pattern = re.compile(r"\n?<!-- phase22:begin -->.*?<!-- phase22:end -->\n?", re.DOTALL)
    if pattern.search(body):
        return pattern.sub("\n\n" + managed + "\n", body).rstrip() + "\n"
    return managed + "\n\n" + body.lstrip()


def build_router_header() -> str:
    lines = ["# Support / Anemone Memory Router", "", "## Canonical Notes"]
    for label, rel_path in ROUTER_NOTES:
        lines.append(f"- {label}: `{rel_path}`")
    for bundle_name, bundle_paths in ROUTER_BUNDLES.items():
        lines.extend(["", f"## {bundle_name} Bundle"])
        for rel_path in bundle_paths:
            lines.append(f"- `{rel_path}`")
    return "\n".join(lines).rstrip() + "\n"


def replace_router_block(text: str, block: str) -> str:
    managed = f"{PHASE22_BEGIN}\n{block.rstrip()}\n{PHASE22_END}"
    pattern = re.compile(r"\n?<!-- phase22:begin -->.*?<!-- phase22:end -->\n?", re.DOTALL)
    if pattern.search(text):
        return pattern.sub(managed + "\n\n", text, count=1).rstrip() + "\n"
    return managed + "\n\n" + text.lstrip()


def update_squad_router(path: Path) -> bool:
    if not path.exists():
        return False
    original = path.read_text(encoding="utf-8")
    updated = original
    for bundle_name in ("Pinchy", "Anemone", "Urchin", "Chitin"):
        updated = ensure_bundle_reference(updated, bundle_name, "support-anemone/MEMORY.md")
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def ensure_bundle_reference(text: str, bundle_name: str, rel_path: str) -> str:
    lines = text.splitlines()
    header = f"### {bundle_name} Bundle"
    start = end = None
    for idx, raw in enumerate(lines):
        if raw.strip() == header:
            start = idx + 1
            continue
        if start is not None and raw.strip().startswith("### "):
            end = idx
            break
    insert_line = f"- `{rel_path}`"
    if start is None:
        if lines and lines[-1].strip():
            lines.append("")
        lines.extend([header, insert_line])
        return "\n".join(lines).rstrip() + "\n"
    if end is None:
        end = len(lines)
    block = [row for row in lines[start:end] if row.strip()]
    if insert_line not in {row.strip() for row in block}:
        block.append(insert_line)
    updated = lines[:start] + block + lines[end:]
    return "\n".join(updated).rstrip() + "\n"


def build_evidence_ledger() -> Dict[str, Any]:
    topics = {
        "support_core": {
            "topic": "support_core",
            "domain": "support-anemone",
            "primary_path": "support-anemone/memory/anemone-operating-canon-2026.md",
            "evidence_paths": [
                "support-anemone/memory/anemone-operating-canon-2026.md",
                "support-anemone/memory/fast-first-response-and-severity-triage.md",
                "support-anemone/memory/bug-escalation-and-engineering-handoff.md",
                "support-anemone/memory/patterns-faq-and-doc-gaps.md",
            ],
            "source_count": 1,
            "evidence_count": 4,
            "confidence_score": 0.9,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
            "consensus": PHASE22_CONSENSUS,
            "tension": PHASE22_TENSION,
            "squad_action": PHASE22_ACTION,
        },
        "support_triage_system": {
            "topic": "support_triage_system",
            "domain": "support-anemone",
            "primary_path": "support-anemone/memory/fast-first-response-and-severity-triage.md",
            "evidence_paths": [
                "support-anemone/memory/fast-first-response-and-severity-triage.md",
                "support-anemone/memory/anemone-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.88,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "support_bug_handoff": {
            "topic": "support_bug_handoff",
            "domain": "support-anemone",
            "primary_path": "support-anemone/memory/bug-escalation-and-engineering-handoff.md",
            "evidence_paths": [
                "support-anemone/memory/bug-escalation-and-engineering-handoff.md",
                "support-anemone/memory/anemone-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.87,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "support_pattern_logging": {
            "topic": "support_pattern_logging",
            "domain": "support-anemone",
            "primary_path": "support-anemone/memory/patterns-faq-and-doc-gaps.md",
            "evidence_paths": [
                "support-anemone/memory/patterns-faq-and-doc-gaps.md",
                "support-anemone/memory/anemone-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.86,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
    }
    primary_paths = {row["primary_path"]: row for row in topics.values()}
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topics": topics,
        "primary_paths": primary_paths,
    }


def build_report(result: Dict[str, Any]) -> str:
    lines = [
        "---",
        "source: local phase22 support bootstrap",
        "title: Support Bootstrap Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase22_bootstrap, support, anemone",
        "topic: support_bootstrap",
        "intent: maintenance, routing, canon_bootstrap",
        "role: support-anemone, pinchy, operations, writer",
        "confidence: high",
        "canonical: false",
        "canonical_group: Support bootstrap",
        "use_for: support_bootstrap, support_routing",
        "avoid_for: seo_strategy",
        "---",
        "",
        "# Support Bootstrap Report",
        "",
        f"- Router path: `{result['router_path']}`",
        f"- Squad router updated: {result['squad_router_changed']}",
        f"- Notes created or updated: {len(result['notes'])}",
        "",
        "## Notes",
    ]
    for note in result["notes"]:
        lines.append(f"- `{note}`")
    return "\n".join(lines).rstrip() + "\n"


def run(skills_root: Path, phase22_dir: Path, db_path: Path, build_db: bool) -> Dict[str, Any]:
    support_root = skills_root / "support-anemone"
    memory_root = support_root / "memory"
    memory_root.mkdir(parents=True, exist_ok=True)
    phase22_dir.mkdir(parents=True, exist_ok=True)

    notes_payload = {
        "fast-first-response-and-severity-triage.md": build_triage_note(),
        "bug-escalation-and-engineering-handoff.md": build_handoff_note(),
        "patterns-faq-and-doc-gaps.md": build_patterns_note(),
        "anemone-operating-canon-2026.md": build_operating_canon(),
    }

    note_paths: List[str] = []
    changed_notes: List[str] = []
    for filename, text in notes_payload.items():
        path = memory_root / filename
        rel_path = f"support-anemone/memory/{filename}"
        note_paths.append(rel_path)
        if write_note(path, text):
            changed_notes.append(rel_path)

    canon_path = memory_root / "anemone-operating-canon-2026.md"
    if write_note_body(canon_path, lambda body: replace_phase22_block(body, build_phase22_block())):
        if "support-anemone/memory/anemone-operating-canon-2026.md" not in changed_notes:
            changed_notes.append("support-anemone/memory/anemone-operating-canon-2026.md")

    router_path = support_root / "MEMORY.md"
    original_router = router_path.read_text(encoding="utf-8") if router_path.exists() else "# Support / Anemone Memory Router\n"
    router_changed = write_note(router_path, replace_router_block(original_router, build_router_header()))

    squad_router_path = skills_root / "SQUAD_MEMORY.md"
    squad_router_changed = update_squad_router(squad_router_path)

    ledger = build_evidence_ledger()
    ledger_path = phase22_dir / "support_evidence_ledger.json"
    write_json(ledger_path, ledger)

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase22_dir": str(phase22_dir),
        "router_path": str(router_path),
        "notes": note_paths,
        "changed_notes": changed_notes,
        "squad_router_changed": squad_router_changed,
        "ledger_path": str(ledger_path),
    }

    report_path = phase22_dir / "support_bootstrap_report.md"
    report_path.write_text(build_report(result), encoding="utf-8")
    result["report_path"] = str(report_path)

    if build_db:
        completed = subprocess.run(
            [sys.executable, str(BASE / "squad_memory.py"), "build", "--root", str(skills_root), "--db", str(db_path)],
            check=False,
            capture_output=True,
            text=True,
        )
        result["build"] = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
        }
        if completed.returncode != 0:
            raise SystemExit(completed.stderr.strip() or completed.stdout.strip())

    latest_path = phase22_dir / "latest.json"
    write_json(latest_path, result)
    return result


def main() -> int:
    args = parse_args()
    result = run(Path(args.skills_root), Path(args.phase22_dir), Path(args.db_path), args.build_db)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
