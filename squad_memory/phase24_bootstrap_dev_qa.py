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

from phase11_bootstrap_writer_marketing import build_frontmatter, write_note


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE24_DIR = BASE / "ingest" / "phase24"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

PHASE24_BEGIN = "<!-- phase24:begin -->"
PHASE24_END = "<!-- phase24:end -->"

DEVELOPER_NOTES: Dict[str, Dict[str, str]] = {
    "implementation-and-tdd-loop.md": {
        "title": "Implementation And TDD Loop",
        "topic": "developer_tdd_loop",
        "intent": "implementation, feature_work, testing",
        "role": "developer, developer-chitin, pinchy, qa, reviewer",
        "use_for": "tdd_execution, feature_building, test_first_changes, clean_handoffs",
        "avoid_for": "architecture_without_spec, deploy_decisions",
        "canonical_group": "Chitin implementation and TDD loop",
    },
    "bug-reproduction-and-fix-workflow.md": {
        "title": "Bug Reproduction And Fix Workflow",
        "topic": "developer_bugfix_loop",
        "intent": "bugfix, debugging, testing",
        "role": "developer, developer-chitin, qa, reviewer, pinchy",
        "use_for": "bug_reproduction, fix_scoping, regression_safety, patch_handoff",
        "avoid_for": "speculative_refactors_without_bug_scope, production_incident_comms",
        "canonical_group": "Chitin bug reproduction and fix workflow",
    },
    "small-prs-and-safe-refactors.md": {
        "title": "Small PRs And Safe Refactors",
        "topic": "developer_safe_change_system",
        "intent": "implementation, refactor, review_readiness",
        "role": "developer, developer-chitin, reviewer, qa, pinchy",
        "use_for": "small_prs, safe_refactors, reviewability, scope_control",
        "avoid_for": "large_unbounded_rewrites, hidden_behavior_changes",
        "canonical_group": "Chitin small PRs and safe refactors",
    },
}

QA_NOTES: Dict[str, Dict[str, str]] = {
    "test-matrix-and-edge-case-coverage.md": {
        "title": "Test Matrix And Edge Case Coverage",
        "topic": "qa_edge_matrix",
        "intent": "qa_validation, edge_cases, test_design",
        "role": "qa, qa-reef, developer, reviewer, pinchy",
        "use_for": "test_matrixes, edge_case_design, functional_coverage, boundary_checks",
        "avoid_for": "implementation_decisions, release_signoff_without_execution",
        "canonical_group": "Reef test matrix and edge coverage",
    },
    "regression-gate-and-release-verdicts.md": {
        "title": "Regression Gate And Release Verdicts",
        "topic": "qa_regression_gate",
        "intent": "qa_validation, regression, pass_fail",
        "role": "qa, qa-reef, devops, developer, pinchy",
        "use_for": "release_gates, regression_checks, pass_fail_verdicts, deployment_readiness",
        "avoid_for": "feature_implementation, rollback_execution",
        "canonical_group": "Reef regression gate and verdicts",
    },
    "bug-report-quality-and-repro-discipline.md": {
        "title": "Bug Report Quality And Repro Discipline",
        "topic": "qa_bug_reporting",
        "intent": "qa_validation, bug_reports, reproduction",
        "role": "qa, qa-reef, developer, reviewer, support-anemone",
        "use_for": "bug_reports, repro_steps, severity_calls, fix_verification",
        "avoid_for": "quick_opinions_without_repro, vague_quality_feedback",
        "canonical_group": "Reef bug report and repro quality",
    },
}

DEVELOPER_ROUTER_NOTES = [
    ("Developer Operating Canon 2026", "memory/developer-operating-canon-2026.md"),
    ("Implementation And TDD Loop", "memory/implementation-and-tdd-loop.md"),
    ("Bug Reproduction And Fix Workflow", "memory/bug-reproduction-and-fix-workflow.md"),
    ("Small PRs And Safe Refactors", "memory/small-prs-and-safe-refactors.md"),
]

DEVELOPER_ROUTER_BUNDLES = {
    "Chitin": [
        "memory/developer-operating-canon-2026.md",
        "memory/implementation-and-tdd-loop.md",
        "memory/bug-reproduction-and-fix-workflow.md",
    ],
    "Barnacle": [
        "memory/developer-operating-canon-2026.md",
        "memory/small-prs-and-safe-refactors.md",
    ],
    "Reef": [
        "memory/bug-reproduction-and-fix-workflow.md",
        "memory/developer-operating-canon-2026.md",
    ],
    "Pinchy": [
        "memory/developer-operating-canon-2026.md",
        "memory/small-prs-and-safe-refactors.md",
    ],
}

QA_ROUTER_NOTES = [
    ("QA Operating Canon 2026", "memory/qa-operating-canon-2026.md"),
    ("Test Matrix And Edge Case Coverage", "memory/test-matrix-and-edge-case-coverage.md"),
    ("Regression Gate And Release Verdicts", "memory/regression-gate-and-release-verdicts.md"),
    ("Bug Report Quality And Repro Discipline", "memory/bug-report-quality-and-repro-discipline.md"),
]

QA_ROUTER_BUNDLES = {
    "Reef": [
        "memory/qa-operating-canon-2026.md",
        "memory/test-matrix-and-edge-case-coverage.md",
        "memory/regression-gate-and-release-verdicts.md",
    ],
    "Chitin": [
        "memory/qa-operating-canon-2026.md",
        "memory/bug-report-quality-and-repro-discipline.md",
    ],
    "Barnacle": [
        "memory/qa-operating-canon-2026.md",
        "memory/regression-gate-and-release-verdicts.md",
    ],
    "Pinchy": [
        "memory/qa-operating-canon-2026.md",
        "memory/regression-gate-and-release-verdicts.md",
    ],
    "Tide": [
        "memory/regression-gate-and-release-verdicts.md",
        "memory/qa-operating-canon-2026.md",
    ],
}

PHASE24_CONSENSUS = {
    "developer": [
        "Developer quality starts with read-first implementation, a tight test loop, and changes small enough to reason about.",
        "Bug fixes are not complete when the symptom disappears. Chitin needs reproduction, a scoped fix, and regression protection.",
        "Review quality improves upstream when implementation scope, tests, and PR size stay disciplined before Barnacle ever looks at the patch.",
    ],
    "qa": [
        "QA quality starts with a repeatable test matrix, not with ad-hoc clicking.",
        "Regression confidence comes from explicit gates, edge-case coverage, and reproducible evidence, not from intuition.",
        "Reef is strongest when bug reports are specific enough for Chitin to act on quickly and specific enough for Barnacle to trust.",
    ],
}

PHASE24_TENSION = {
    "developer": [
        "The main tradeoff is speed versus change safety: large rushed changes may feel efficient, but small test-backed iterations reduce review friction and regression risk.",
    ],
    "qa": [
        "The main tradeoff is coverage versus throughput: Reef should test what matters most, but shallow smoke passes are not a release gate.",
    ],
}

PHASE24_ACTION = {
    "developer": "Use the developer operating canon first for implementation work, then narrow into TDD, bugfix, or safe-change notes based on the task shape.",
    "qa": "Use the QA operating canon first for test planning and signoff work, then narrow into matrix, regression, or bug-report notes based on the task shape.",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 24 developer and QA knowledge bootstrap")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase24-dir", default=str(DEFAULT_PHASE24_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def build_developer_tdd_note() -> str:
    meta = DEVELOPER_NOTES["implementation-and-tdd-loop.md"]
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
                "source": "local_developer_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "developer, chitin, tdd, implementation, tests",
            }
        ).rstrip(),
        "# Implementation And TDD Loop",
        "",
        "## Core Concept",
        "Chitin should start from the expected behavior, write the failing test, implement the smallest working change, then rerun the suite before calling the task stable.",
        "",
        "## Loop",
        "1. Read the spec and the surrounding code first.",
        "2. Write or identify the test that proves the expected behavior.",
        "3. Confirm the test fails for the right reason.",
        "4. Implement the smallest change that makes the test pass.",
        "5. Run nearby tests, then the broader suite if the surface area grew.",
        "",
        "## Guardrails",
        "- Avoid speculative abstractions before the behavior is working.",
        "- Keep the fix inside the current scope instead of rewriting the subsystem.",
        "- Make tests describe behavior, not just internal implementation details.",
        "",
        "## Squad Use",
        "- **Chitin**: Start here for new features and scoped implementation tasks.",
        "- **Reef**: Use this when verifying whether the dev handoff actually has test coverage.",
        "- **Barnacle**: Use this when review quality depends on seeing a clear implementation loop.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_developer_bugfix_note() -> str:
    meta = DEVELOPER_NOTES["bug-reproduction-and-fix-workflow.md"]
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
                "source": "local_developer_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "developer, chitin, bugfix, reproduction, regression",
            }
        ).rstrip(),
        "# Bug Reproduction And Fix Workflow",
        "",
        "## Core Concept",
        "A bug fix starts with reproducing the actual failure, not guessing at the likely code path. Chitin should prove the bug, prove the fix, and prove the regression is covered.",
        "",
        "## Workflow",
        "- Capture the failing behavior and the narrowest reproducible case.",
        "- Identify whether the fix belongs in validation, business logic, integration code, or state handling.",
        "- Add the regression test that would have caught the bug earlier.",
        "- Verify nearby behavior so the patch does not shift the bug elsewhere.",
        "",
        "## Handoff Rules",
        "- Document the root symptom, not just the line that changed.",
        "- Call out any remaining risk, follow-up cleanup, or monitoring need.",
        "- Make the patch easy for Reef and Barnacle to validate quickly.",
        "",
        "## Squad Use",
        "- **Chitin**: Use this for production bugs, flaky flows, and patch work.",
        "- **Reef**: Use this when checking whether the bug is actually reproducible and verifiable.",
        "- **Pinchy**: Use this when the team needs a clean bugfix workflow instead of noisy patch churn.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_developer_safe_change_note() -> str:
    meta = DEVELOPER_NOTES["small-prs-and-safe-refactors.md"]
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
                "source": "local_developer_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "developer, chitin, refactor, reviewability, small prs",
            }
        ).rstrip(),
        "# Small PRs And Safe Refactors",
        "",
        "## Core Concept",
        "Small, reviewable changes keep risk visible. Safe refactors separate structural cleanup from behavior changes whenever possible.",
        "",
        "## Rules",
        "- Prefer one concern per patch instead of mixing feature work, refactor, and cleanup together.",
        "- Split pure refactors from behavior changes if review or rollback would be cleaner.",
        "- Leave a clear trail for Barnacle and Reef: what changed, why, and how to validate it.",
        "",
        "## Warning Signs",
        "- The patch touches too many unrelated files.",
        "- Tests only pass after broad unrelated adjustments.",
        "- The PR description has to explain multiple independent intentions.",
        "",
        "## Squad Use",
        "- **Chitin**: Use this when implementation scope starts to sprawl.",
        "- **Barnacle**: Use this when review quality depends on safer PR boundaries.",
        "- **Pinchy**: Use this when the team needs discipline around scope and handoff quality.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_developer_operating_canon() -> str:
    body = [
        build_frontmatter(
            {
                "title": "Developer Operating Canon 2026",
                "topic": "developer_core",
                "intent": "implementation, bugfix, testing, refactor",
                "role": "developer, developer-chitin, reviewer, qa, pinchy",
                "use_for": "implementation_briefing, bugfix_routing, test_backed_changes, domain_canon",
                "avoid_for": "architecture_without_spec, deploy_authority, product_strategy",
                "confidence": "high",
                "canonical": "true",
                "canonical_group": "Chitin operating canon",
                "source": "local_developer_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "developer, chitin, canon, implementation, squad",
            }
        ).rstrip(),
        "# Developer Operating Canon 2026",
        "",
        "## Core Concept",
        PHASE24_CONSENSUS["developer"][0] + " " + PHASE24_CONSENSUS["developer"][1],
        "",
        "## Domain Rules",
        f"- **Implementation And TDD Loop**: {PHASE24_CONSENSUS['developer'][0]}",
        f"- **Bug Reproduction And Fix Workflow**: {PHASE24_CONSENSUS['developer'][1]}",
        f"- **Small PRs And Safe Refactors**: {PHASE24_CONSENSUS['developer'][2]}",
        "",
        "## Workflow Map",
        "1. Start here for general implementation, bugfix, or refactor work.",
        "2. Open `memory/implementation-and-tdd-loop.md` when the task is new build work or test-first implementation.",
        "3. Open `memory/bug-reproduction-and-fix-workflow.md` when the task is a bugfix or patch handoff.",
        "4. Open `memory/small-prs-and-safe-refactors.md` when scope control, reviewability, or safe cleanup matters.",
        "",
        "## Tension / Caveat",
        f"- {PHASE24_TENSION['developer'][0]}",
        "",
        "## Squad Action",
        f"- {PHASE24_ACTION['developer']}",
        "",
        "## Team Use",
        "- **Chitin**: Start here for broad implementation work before narrowing into the execution note that matches the task shape.",
        "- **Barnacle**: Use this when review quality depends on disciplined implementation scope and clean tests.",
        "- **Reef**: Use this when QA needs to understand what a good development handoff should include.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_qa_matrix_note() -> str:
    meta = QA_NOTES["test-matrix-and-edge-case-coverage.md"]
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
                "source": "local_qa_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "qa, reef, edge cases, test matrix, validation",
            }
        ).rstrip(),
        "# Test Matrix And Edge Case Coverage",
        "",
        "## Core Concept",
        "Reef should turn requirements into a test matrix that covers happy path, edge cases, invalid input, state transitions, and likely regression zones before deciding whether the change is safe.",
        "",
        "## Matrix Rules",
        "- Always cover the expected success path first, then the highest-risk failure paths.",
        "- Include empty, null, max-length, malformed, permission, and sequencing cases where they matter.",
        "- Make it explicit which areas are verified manually, automatically, or still blocked.",
        "",
        "## Coverage Checks",
        "- Does the change work on first run and after a prior error?",
        "- Does the system fail clearly when input or dependencies are wrong?",
        "- Did the change alter any nearby behavior that now needs a regression check?",
        "",
        "## Squad Use",
        "- **Reef**: Start here for test planning and edge-case coverage.",
        "- **Chitin**: Use this when the fix needs clearer test shape before handoff.",
        "- **Pinchy**: Use this when quality planning needs to be explicit instead of assumed.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_qa_regression_note() -> str:
    meta = QA_NOTES["regression-gate-and-release-verdicts.md"]
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
                "source": "local_qa_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "qa, reef, regression, release gate, verdict",
            }
        ).rstrip(),
        "# Regression Gate And Release Verdicts",
        "",
        "## Core Concept",
        "A release gate is a verdict backed by executed checks, known risk, and clear blockers. Reef should make PASS, FAIL, and BLOCKED decisions explicit enough for Tide and Pinchy to act on.",
        "",
        "## Gate Rules",
        "- PASS means the verified scope is clear and the known risk is acceptable.",
        "- FAIL means the change is not ready and the bugs are reproducible enough to return to Chitin.",
        "- BLOCKED means the team lacks an environment, dependency, or clarity needed for a real verdict.",
        "",
        "## Regression Focus",
        "- Re-run the tests most likely to be impacted by the change, not just the new behavior.",
        "- Note what was not tested so the decision is honest.",
        "- Tie the verdict to evidence, not confidence language.",
        "",
        "## Squad Use",
        "- **Reef**: Use this for release gates, regression passes, and QA signoff.",
        "- **Tide**: Use this when deciding whether deployment is safe to proceed.",
        "- **Pinchy**: Use this when risk needs to be summarized clearly across the rollout.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_qa_bug_report_note() -> str:
    meta = QA_NOTES["bug-report-quality-and-repro-discipline.md"]
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
                "source": "local_qa_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "qa, reef, bug reports, reproduction, severity",
            }
        ).rstrip(),
        "# Bug Report Quality And Repro Discipline",
        "",
        "## Core Concept",
        "A useful bug report gives Chitin a reproducible failure, gives Barnacle a believable risk picture, and gives Pinchy enough clarity to prioritize without guessing.",
        "",
        "## Report Rules",
        "- Include steps to reproduce, expected behavior, actual behavior, and severity.",
        "- Capture environment or state assumptions when they matter.",
        "- Separate one reproducible issue from a pile of loosely related observations.",
        "",
        "## Verification Rules",
        "- Re-run the repro after the fix instead of assuming the patch solved it.",
        "- Confirm whether the bug is isolated or symptomatic of a larger regression area.",
        "- Mark uncertainty explicitly when the repro is partial or environment-dependent.",
        "",
        "## Squad Use",
        "- **Reef**: Use this when filing bugs or retesting fixes.",
        "- **Chitin**: Use this when a QA report is too vague to act on quickly.",
        "- **Anemone**: Use this when customer-reported issues need to become clear engineering bugs.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_qa_operating_canon() -> str:
    body = [
        build_frontmatter(
            {
                "title": "QA Operating Canon 2026",
                "topic": "qa_core",
                "intent": "qa_validation, regression, bug_reports, signoff",
                "role": "qa, qa-reef, developer, reviewer, devops, pinchy",
                "use_for": "qa_briefing, regression_routing, verdicts, domain_canon",
                "avoid_for": "implementation_without_handoff, release_decisions_without_evidence",
                "confidence": "high",
                "canonical": "true",
                "canonical_group": "Reef operating canon",
                "source": "local_qa_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "qa, reef, canon, testing, squad",
            }
        ).rstrip(),
        "# QA Operating Canon 2026",
        "",
        "## Core Concept",
        PHASE24_CONSENSUS["qa"][0] + " " + PHASE24_CONSENSUS["qa"][1],
        "",
        "## Domain Rules",
        f"- **Test Matrix And Edge Case Coverage**: {PHASE24_CONSENSUS['qa'][0]}",
        f"- **Regression Gate And Release Verdicts**: {PHASE24_CONSENSUS['qa'][1]}",
        f"- **Bug Report Quality And Repro Discipline**: {PHASE24_CONSENSUS['qa'][2]}",
        "",
        "## Workflow Map",
        "1. Start here for broad QA planning, regression, or signoff work.",
        "2. Open `memory/test-matrix-and-edge-case-coverage.md` when the task is about coverage shape or edge cases.",
        "3. Open `memory/regression-gate-and-release-verdicts.md` when the task is about PASS/FAIL/BLOCKED calls or release readiness.",
        "4. Open `memory/bug-report-quality-and-repro-discipline.md` when the task is about bug quality, repro steps, or fix verification.",
        "",
        "## Tension / Caveat",
        f"- {PHASE24_TENSION['qa'][0]}",
        "",
        "## Squad Action",
        f"- {PHASE24_ACTION['qa']}",
        "",
        "## Team Use",
        "- **Reef**: Start here for broad QA work before narrowing into the note that matches the task shape.",
        "- **Chitin**: Use this when dev work needs a clearer QA handoff or bug-verification standard.",
        "- **Tide**: Use this when release readiness depends on an explicit QA gate instead of assumption.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_router_block(title: str, notes: List[tuple[str, str]], bundles: Dict[str, List[str]]) -> str:
    lines = [f"# {title}", "", "## Canonical Notes"]
    for label, rel_path in notes:
        lines.append(f"- {label}: `{rel_path}`")
    for bundle_name, bundle_paths in bundles.items():
        lines.extend(["", f"## {bundle_name} Bundle"])
        for rel_path in bundle_paths:
            lines.append(f"- `{rel_path}`")
    return "\n".join(lines).rstrip() + "\n"


def replace_router_block(text: str, block: str) -> str:
    managed = f"{PHASE24_BEGIN}\n{block.rstrip()}\n{PHASE24_END}"
    pattern = re.compile(r"\n?<!-- phase24:begin -->.*?<!-- phase24:end -->\n?", re.DOTALL)
    if pattern.search(text):
        return pattern.sub(managed + "\n\n", text, count=1).rstrip() + "\n"
    return managed + "\n\n" + text.lstrip()


def write_router(path: Path, block: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    updated = replace_router_block(existing, block)
    if existing == updated:
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


def update_squad_router(path: Path) -> bool:
    if not path.exists():
        return False
    original = path.read_text(encoding="utf-8")
    updated = original
    updates = {
        "Pinchy": ["developer/MEMORY.md", "qa/MEMORY.md"],
        "Chitin": ["developer/MEMORY.md", "qa/MEMORY.md"],
        "Reef": ["qa/MEMORY.md", "developer/MEMORY.md"],
        "Barnacle": ["developer/MEMORY.md", "qa/MEMORY.md"],
        "Tide": ["qa/MEMORY.md"],
    }
    for bundle_name, rel_paths in updates.items():
        for rel_path in rel_paths:
            updated = ensure_bundle_reference(updated, bundle_name, rel_path)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def build_ledger_payload() -> Dict[str, Any]:
    topics: Dict[str, Dict[str, Any]] = {
        "developer_core": {
            "topic": "developer_core",
            "domain": "developer",
            "primary_path": "developer/memory/developer-operating-canon-2026.md",
            "evidence_paths": [
                "developer/memory/developer-operating-canon-2026.md",
                "developer/memory/implementation-and-tdd-loop.md",
                "developer/memory/bug-reproduction-and-fix-workflow.md",
                "developer/memory/small-prs-and-safe-refactors.md",
            ],
            "source_count": 1,
            "evidence_count": 4,
            "confidence_score": 0.9,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "developer_tdd_loop": {
            "topic": "developer_tdd_loop",
            "domain": "developer",
            "primary_path": "developer/memory/implementation-and-tdd-loop.md",
            "evidence_paths": [
                "developer/memory/implementation-and-tdd-loop.md",
                "developer/memory/developer-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.88,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "developer_bugfix_loop": {
            "topic": "developer_bugfix_loop",
            "domain": "developer",
            "primary_path": "developer/memory/bug-reproduction-and-fix-workflow.md",
            "evidence_paths": [
                "developer/memory/bug-reproduction-and-fix-workflow.md",
                "developer/memory/developer-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.88,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "developer_safe_change_system": {
            "topic": "developer_safe_change_system",
            "domain": "developer",
            "primary_path": "developer/memory/small-prs-and-safe-refactors.md",
            "evidence_paths": [
                "developer/memory/small-prs-and-safe-refactors.md",
                "developer/memory/developer-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.86,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "qa_core": {
            "topic": "qa_core",
            "domain": "qa",
            "primary_path": "qa/memory/qa-operating-canon-2026.md",
            "evidence_paths": [
                "qa/memory/qa-operating-canon-2026.md",
                "qa/memory/test-matrix-and-edge-case-coverage.md",
                "qa/memory/regression-gate-and-release-verdicts.md",
                "qa/memory/bug-report-quality-and-repro-discipline.md",
            ],
            "source_count": 1,
            "evidence_count": 4,
            "confidence_score": 0.9,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "qa_edge_matrix": {
            "topic": "qa_edge_matrix",
            "domain": "qa",
            "primary_path": "qa/memory/test-matrix-and-edge-case-coverage.md",
            "evidence_paths": [
                "qa/memory/test-matrix-and-edge-case-coverage.md",
                "qa/memory/qa-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.88,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "qa_regression_gate": {
            "topic": "qa_regression_gate",
            "domain": "qa",
            "primary_path": "qa/memory/regression-gate-and-release-verdicts.md",
            "evidence_paths": [
                "qa/memory/regression-gate-and-release-verdicts.md",
                "qa/memory/qa-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.88,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "qa_bug_reporting": {
            "topic": "qa_bug_reporting",
            "domain": "qa",
            "primary_path": "qa/memory/bug-report-quality-and-repro-discipline.md",
            "evidence_paths": [
                "qa/memory/bug-report-quality-and-repro-discipline.md",
                "qa/memory/qa-operating-canon-2026.md",
            ],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.86,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
    }
    primary_paths = {value["primary_path"]: value for value in topics.values()}
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topics": topics,
        "primary_paths": primary_paths,
    }


def build_report(result: Dict[str, Any]) -> str:
    lines = [
        "---",
        "source: local phase24 developer qa bootstrap",
        "title: Developer And QA Bootstrap Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase24_bootstrap, developer, qa, canon, squad",
        "topic: developer_qa_bootstrap",
        "intent: maintenance, routing, canon_bootstrap",
        "role: pinchy, developer, qa, reviewer, devops",
        "confidence: high",
        "canonical: false",
        "canonical_group: Developer and QA bootstrap report",
        "use_for: phase24_reporting, routing_checks",
        "avoid_for: seo_strategy",
        "---",
        "",
        "# Developer And QA Bootstrap Report",
        "",
        f"- Developer router changed: {result['developer_router_changed']}",
        f"- QA router changed: {result['qa_router_changed']}",
        f"- Squad router changed: {result['squad_router_changed']}",
        f"- Developer notes: {result['developer_note_count']}",
        f"- QA notes: {result['qa_note_count']}",
        f"- Evidence ledgers: `{result['developer_ledger_path']}`, `{result['qa_ledger_path']}`",
    ]
    if result.get("build"):
        lines.append(f"- DB rebuild: rc={result['build']['returncode']}")
    return "\n".join(lines).rstrip() + "\n"


def run(skills_root: Path, phase24_dir: Path, db_path: Path, build_db: bool) -> Dict[str, Any]:
    developer_root = skills_root / "developer"
    developer_memory = developer_root / "memory"
    qa_root = skills_root / "qa"
    qa_memory = qa_root / "memory"
    developer_memory.mkdir(parents=True, exist_ok=True)
    qa_memory.mkdir(parents=True, exist_ok=True)
    phase24_dir.mkdir(parents=True, exist_ok=True)

    developer_changes = [
        write_note(developer_memory / "implementation-and-tdd-loop.md", build_developer_tdd_note()),
        write_note(developer_memory / "bug-reproduction-and-fix-workflow.md", build_developer_bugfix_note()),
        write_note(developer_memory / "small-prs-and-safe-refactors.md", build_developer_safe_change_note()),
        write_note(developer_memory / "developer-operating-canon-2026.md", build_developer_operating_canon()),
    ]
    qa_changes = [
        write_note(qa_memory / "test-matrix-and-edge-case-coverage.md", build_qa_matrix_note()),
        write_note(qa_memory / "regression-gate-and-release-verdicts.md", build_qa_regression_note()),
        write_note(qa_memory / "bug-report-quality-and-repro-discipline.md", build_qa_bug_report_note()),
        write_note(qa_memory / "qa-operating-canon-2026.md", build_qa_operating_canon()),
    ]

    developer_router_changed = write_router(
        developer_root / "MEMORY.md",
        build_router_block("Developer / Chitin Memory Router", DEVELOPER_ROUTER_NOTES, DEVELOPER_ROUTER_BUNDLES),
    )
    qa_router_changed = write_router(
        qa_root / "MEMORY.md",
        build_router_block("QA / Reef Memory Router", QA_ROUTER_NOTES, QA_ROUTER_BUNDLES),
    )

    squad_router_path = skills_root / "SQUAD_MEMORY.md"
    squad_router_changed = update_squad_router(squad_router_path)

    ledger_payload = build_ledger_payload()
    developer_ledger = {
        "generated_at": ledger_payload["generated_at"],
        "topics": {k: v for k, v in ledger_payload["topics"].items() if v["domain"] == "developer"},
        "primary_paths": {k: v for k, v in ledger_payload["primary_paths"].items() if v["domain"] == "developer"},
    }
    qa_ledger = {
        "generated_at": ledger_payload["generated_at"],
        "topics": {k: v for k, v in ledger_payload["topics"].items() if v["domain"] == "qa"},
        "primary_paths": {k: v for k, v in ledger_payload["primary_paths"].items() if v["domain"] == "qa"},
    }
    developer_ledger_path = phase24_dir / "developer_evidence_ledger.json"
    qa_ledger_path = phase24_dir / "qa_evidence_ledger.json"
    write_json(developer_ledger_path, developer_ledger)
    write_json(qa_ledger_path, qa_ledger)

    result: Dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase24_dir": str(phase24_dir),
        "developer_router_changed": developer_router_changed,
        "qa_router_changed": qa_router_changed,
        "squad_router_changed": squad_router_changed,
        "developer_note_count": 4,
        "qa_note_count": 4,
        "developer_ledger_path": str(developer_ledger_path),
        "qa_ledger_path": str(qa_ledger_path),
        "changed_note_count": sum(1 for item in developer_changes + qa_changes if item),
    }

    report_path = phase24_dir / "developer_qa_bootstrap_report.md"
    report_path.write_text(build_report(result), encoding="utf-8")
    result["report_path"] = str(report_path)

    if build_db:
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
        result["build"] = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
        }

    manifest_path = phase24_dir / f"phase24-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase24_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    print(f"Developer router changed: {result['developer_router_changed']}")
    print(f"QA router changed: {result['qa_router_changed']}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = run(
        skills_root=Path(args.skills_root),
        phase24_dir=Path(args.phase24_dir),
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
