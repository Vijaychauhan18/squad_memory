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

from phase11_bootstrap_writer_marketing import build_frontmatter, parse_frontmatter, write_note, write_note_body


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE16_DIR = BASE / "ingest" / "phase16"
DEFAULT_DB_PATH = BASE / "squad_memory.db"

PHASE16_BEGIN = "<!-- phase16:begin -->"
PHASE16_END = "<!-- phase16:end -->"

CHARLES_NOTES: Dict[str, Dict[str, str]] = {
    "platform-native-posting-system.md": {
        "title": "Platform-Native Posting System",
        "topic": "social_platform_native_system",
        "intent": "social_creator, repurposing, distribution",
        "role": "charles, current, pinchy, writer",
        "use_for": "platform_native_posts, channel_adaptation, hook_variants, repurposing",
        "avoid_for": "paid_ads_without_approval, long_form_blog_writing",
        "canonical_group": "Charles platform-native posting",
    },
    "community-engagement-loop.md": {
        "title": "Community Engagement Loop",
        "topic": "community_engagement",
        "intent": "social_creator, engagement, response",
        "role": "charles, current, pinchy, support",
        "use_for": "comment_replies, dm_triage, engagement_loops, community_management",
        "avoid_for": "pr_crisis_handling, unverified_public_promises",
        "canonical_group": "Charles community engagement",
    },
    "social-calendar-and-trend-radar.md": {
        "title": "Social Calendar And Trend Radar",
        "topic": "social_calendar_trend_radar",
        "intent": "social_creator, planning, monitoring",
        "role": "charles, current, pinchy, kelp",
        "use_for": "weekly_posting_plan, trend_research, calendar_management, performance_review",
        "avoid_for": "product_roadmap_decisions, paid_media_planning",
        "canonical_group": "Charles planning and trend radar",
    },
}

ROUTER_NOTES = [
    ("Charles Operating Canon 2026", "memory/charles-operating-canon-2026.md"),
    ("Platform-Native Posting System", "memory/platform-native-posting-system.md"),
    ("Community Engagement Loop", "memory/community-engagement-loop.md"),
    ("Social Calendar And Trend Radar", "memory/social-calendar-and-trend-radar.md"),
]

ROUTER_BUNDLES = {
    "Charles": [
        "memory/charles-operating-canon-2026.md",
        "memory/platform-native-posting-system.md",
        "memory/community-engagement-loop.md",
    ],
    "Current": [
        "memory/charles-operating-canon-2026.md",
        "memory/social-calendar-and-trend-radar.md",
        "memory/community-engagement-loop.md",
    ],
    "Pinchy": [
        "memory/charles-operating-canon-2026.md",
        "memory/social-calendar-and-trend-radar.md",
    ],
    "Plankton": [
        "memory/platform-native-posting-system.md",
        "memory/charles-operating-canon-2026.md",
    ],
}

PHASE16_CONSENSUS = [
    "Charles should start from platform fit, not from generic reuse. Native delivery is part of the message, not a formatting afterthought.",
    "The hook, the engagement loop, and the posting rhythm belong to one operating system. Social quality falls apart when those three get separated.",
    "Charles works best when writer, marketing, and social execution stay connected but not collapsed into the same output.",
]

PHASE16_TENSION = [
    "The main tradeoff is speed versus fit: fast repurposing increases output, but lazy cross-posting weakens platform performance and brand trust.",
]

PHASE16_ACTION = (
    "Use the Charles operating canon first for social planning, then open the platform-native, engagement, or calendar note depending on whether the task is about execution, conversation, or cadence."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 16 Charles knowledge bootstrap")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase16-dir", default=str(DEFAULT_PHASE16_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def read_doc(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_platform_note() -> str:
    meta = CHARLES_NOTES["platform-native-posting-system.md"]
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
                "source": "local_charles_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "charles, social, platform native, posting system",
            }
        ).rstrip(),
        "# Platform-Native Posting System",
        "",
        "## Core Concept",
        "Charles should adapt the same idea differently by platform instead of copy-pasting one message everywhere.",
        "",
        "## Adaptation Rules",
        "- LinkedIn: stronger professional framing, clearer takeaway, softer CTA.",
        "- X: faster hook, shorter payoff, sharper reply bait.",
        "- Instagram and Reels: visual-first hook, simpler language, save/share CTA.",
        "- TikTok: hook in the first seconds, story or payoff quickly, comment CTA.",
        "",
        "## Hook Rules",
        "- The first line has to stop the scroll before the second line can teach anything.",
        "- The hook should usually create tension, surprise, contrast, or curiosity.",
        "- Reuse the idea, not the phrasing, when moving across channels.",
        "",
        "## Squad Use",
        "- **Charles**: Use this when repurposing or drafting channel-native post sets.",
        "- **Current**: Use this when planning distribution without flattening each channel into one format.",
        "- **Plankton**: Use this when handing a long-form asset over for social adaptation.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_community_note() -> str:
    meta = CHARLES_NOTES["community-engagement-loop.md"]
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
                "source": "local_charles_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "charles, social, engagement, community",
            }
        ).rstrip(),
        "# Community Engagement Loop",
        "",
        "## Core Concept",
        "Social is a conversation system. Charles should not stop at posting; replies, DMs, and follow-up signals are part of the work.",
        "",
        "## Response Loop",
        "1. Check comments, DMs, and mentions daily.",
        "2. Reply fast when the question is safe and brand-clear.",
        "3. Escalate product claims, PR risks, or sensitive issues immediately.",
        "4. Log useful objections, repeated questions, and winning reactions for future posts.",
        "",
        "## Escalation Rules",
        "- Do not improvise around PR, legal, or product promises.",
        "- Escalate trolls, inflammatory threads, or negative press instead of arguing in public.",
        "- Route support-style issues when the conversation becomes troubleshooting or billing.",
        "",
        "## Squad Use",
        "- **Charles**: Use this for day-to-day engagement quality and response discipline.",
        "- **Current**: Use this when turning engagement patterns into better campaigns or follow-up posts.",
        "- **Pinchy**: Use this when checking whether the social loop includes replies, not just publishing.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_calendar_note() -> str:
    meta = CHARLES_NOTES["social-calendar-and-trend-radar.md"]
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
                "source": "local_charles_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "charles, social, calendar, trends, planning",
            }
        ).rstrip(),
        "# Social Calendar And Trend Radar",
        "",
        "## Core Concept",
        "Charles should run a repeatable cadence system: daily awareness, weekly planning, and monthly pattern review.",
        "",
        "## Daily Loop",
        "- Check for new assets from writer, SEO, or marketing.",
        "- Scan mentions and trend opportunities that actually fit the brand.",
        "- Confirm scheduled posts and adjust if the context has changed.",
        "",
        "## Weekly Loop",
        "- Review top-performing hooks, formats, and channels.",
        "- Plan the next week around repeatable winners, not random variety.",
        "- Keep one slot open for reactive trend or conversation-led content.",
        "",
        "## Monthly Loop",
        "- Refresh content pillars and platform mix using actual performance.",
        "- Identify what should become a series, not just a one-off post.",
        "- Surface the strongest patterns back to Current and Pinchy.",
        "",
        "## Squad Use",
        "- **Charles**: Use this for posting cadence, trend selection, and calendar management.",
        "- **Current**: Use this when distribution planning needs stronger social sequencing.",
        "- **Kelp**: Use this when social planning needs trend or competitor research support.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_operating_canon() -> str:
    body = [
        build_frontmatter(
            {
                "title": "Charles Operating Canon 2026",
                "topic": "charles_core",
                "intent": "social_creator, engagement, planning, distribution",
                "role": "charles, current, pinchy, writer",
                "use_for": "social_briefing, platform_routing, creator_workflow, domain_canon",
                "avoid_for": "paid_ads_without_approval, pr_crisis_management",
                "confidence": "high",
                "canonical": "true",
                "canonical_group": "Charles operating canon",
                "source": "local_charles_role_pack",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": "charles, social, operating canon, creator workflow",
            }
        ).rstrip(),
        "# Charles Operating Canon 2026",
        "",
        "## Core Concept",
        "Charles owns social execution end to end: platform-native posts, engagement loops, trend-aware planning, and weekly feedback on what actually works.",
        "",
        "## Domain Rules",
        "- Platform fit is mandatory. The same asset should become different native outputs.",
        "- The first line carries the post. Hooks are not optional polish.",
        "- Engagement is part of the publishing system, not cleanup after posting.",
        "- Trend awareness helps only when it still fits the brand and content pillars.",
        "",
        "## Workflow Map",
        "1. Start with `memory/platform-native-posting-system.md` when the task is adaptation or repurposing.",
        "2. Open `memory/community-engagement-loop.md` when the task includes replies, DMs, comments, or audience interaction.",
        "3. Open `memory/social-calendar-and-trend-radar.md` when the task is planning cadence, monitoring trends, or weekly reporting.",
        "",
        "## Team Use",
        "- **Charles**: Start here for broad social execution before narrowing into the specific operating note.",
        "- **Current**: Use this to keep social distribution native instead of folding everything into generic promotion.",
        "- **Pinchy**: Use this when deciding whether the task needs social execution depth or only campaign-level planning.",
        "- **Plankton**: Use this when handing a long-form asset into a social-first adaptation workflow.",
    ]
    return "\n".join(body).rstrip() + "\n"


def build_phase16_block() -> str:
    lines = [
        "## Phase 16 Domain Fusion",
        "",
        "Evidence confidence: high",
        "Freshness status: current",
        "",
        "### Consensus",
    ]
    for row in PHASE16_CONSENSUS:
        lines.append(f"- {row}")
    lines.extend(["", "### Tension / Caveat"])
    for row in PHASE16_TENSION:
        lines.append(f"- {row}")
    lines.extend(
        [
            "",
            "### Supporting Notes",
            "- `platform-native-posting-system.md`: platform-specific adaptation and hooks.",
            "- `community-engagement-loop.md`: replies, DMs, escalation, and feedback capture.",
            "- `social-calendar-and-trend-radar.md`: daily cadence, weekly planning, and trend selection.",
            "",
            "### Squad Action",
            f"- {PHASE16_ACTION}",
        ]
    )
    return "\n".join(lines)


def replace_phase16_block(body: str, block: str) -> str:
    managed = f"{PHASE16_BEGIN}\n{block.rstrip()}\n{PHASE16_END}"
    pattern = re.compile(r"\n?<!-- phase16:begin -->.*?<!-- phase16:end -->\n?", re.DOTALL)
    if pattern.search(body):
        return pattern.sub("\n\n" + managed + "\n", body).rstrip() + "\n"
    return body.rstrip() + "\n\n" + managed + "\n"


def build_router_text() -> str:
    lines = ["# Charles Memory Router", "", "## Canonical Notes"]
    for label, rel_path in ROUTER_NOTES:
        lines.append(f"- {label}: `{rel_path}`")
    for bundle_name, bundle_paths in ROUTER_BUNDLES.items():
        lines.extend(["", f"## {bundle_name} Bundle"])
        for rel_path in bundle_paths:
            lines.append(f"- `{rel_path}`")
    return "\n".join(lines).rstrip() + "\n"


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
    for bundle_name in ("Pinchy", "Plankton", "Charles", "Current"):
        updated = ensure_bundle_reference(updated, bundle_name, "charles/MEMORY.md")
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def build_evidence_ledger() -> Dict[str, Any]:
    primary_paths: Dict[str, Dict[str, Any]] = {}
    topics = {
        "charles_core": {
            "topic": "charles_core",
            "domain": "charles",
            "primary_path": "charles/memory/charles-operating-canon-2026.md",
            "evidence_paths": [
                "charles/memory/charles-operating-canon-2026.md",
                "charles/memory/platform-native-posting-system.md",
                "charles/memory/community-engagement-loop.md",
                "charles/memory/social-calendar-and-trend-radar.md",
            ],
            "source_count": 1,
            "evidence_count": 4,
            "confidence_score": 0.9,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
            "consensus": PHASE16_CONSENSUS,
            "tension": PHASE16_TENSION,
            "squad_action": PHASE16_ACTION,
        },
        "social_platform_native_system": {
            "topic": "social_platform_native_system",
            "domain": "charles",
            "primary_path": "charles/memory/platform-native-posting-system.md",
            "evidence_paths": ["charles/memory/platform-native-posting-system.md", "charles/memory/charles-operating-canon-2026.md"],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.88,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "community_engagement": {
            "topic": "community_engagement",
            "domain": "charles",
            "primary_path": "charles/memory/community-engagement-loop.md",
            "evidence_paths": ["charles/memory/community-engagement-loop.md", "charles/memory/charles-operating-canon-2026.md"],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.86,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
        "social_calendar_trend_radar": {
            "topic": "social_calendar_trend_radar",
            "domain": "charles",
            "primary_path": "charles/memory/social-calendar-and-trend-radar.md",
            "evidence_paths": ["charles/memory/social-calendar-and-trend-radar.md", "charles/memory/charles-operating-canon-2026.md"],
            "source_count": 1,
            "evidence_count": 2,
            "confidence_score": 0.86,
            "confidence_label": "high",
            "freshness_score": 1.0,
            "freshness_label": "current",
        },
    }
    for topic, evidence in topics.items():
        primary_paths[evidence["primary_path"]] = evidence
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topics": topics,
        "primary_paths": primary_paths,
    }


def build_report(result: Dict[str, Any]) -> str:
    lines = [
        "---",
        "source: local phase16 charles bootstrap",
        "title: Charles Bootstrap Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase16_bootstrap, charles, social, creator",
        "topic: charles_bootstrap",
        "intent: maintenance, routing, canon_bootstrap",
        "role: charles, current, pinchy, plankton",
        "confidence: high",
        "canonical: false",
        "canonical_group: Charles bootstrap",
        "use_for: charles_bootstrap, social_routing",
        "avoid_for: seo_strategy",
        "---",
        "",
        "# Charles Bootstrap Report",
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


def run(skills_root: Path, phase16_dir: Path, db_path: Path, build_db: bool) -> Dict[str, Any]:
    charles_root = skills_root / "charles"
    memory_root = charles_root / "memory"
    memory_root.mkdir(parents=True, exist_ok=True)
    phase16_dir.mkdir(parents=True, exist_ok=True)

    notes_payload = {
        "platform-native-posting-system.md": build_platform_note(),
        "community-engagement-loop.md": build_community_note(),
        "social-calendar-and-trend-radar.md": build_calendar_note(),
        "charles-operating-canon-2026.md": build_operating_canon(),
    }
    note_paths: List[str] = []
    changed_notes: List[str] = []
    for filename, text in notes_payload.items():
        path = memory_root / filename
        note_paths.append(f"charles/memory/{filename}")
        if write_note(path, text):
            changed_notes.append(f"charles/memory/{filename}")

    canon_path = memory_root / "charles-operating-canon-2026.md"
    if write_note_body(canon_path, lambda body: replace_phase16_block(body, build_phase16_block())):
        if "charles/memory/charles-operating-canon-2026.md" not in changed_notes:
            changed_notes.append("charles/memory/charles-operating-canon-2026.md")

    router_path = charles_root / "MEMORY.md"
    router_changed = write_note(router_path, build_router_text())

    squad_router_path = skills_root / "SQUAD_MEMORY.md"
    squad_router_changed = update_squad_router(squad_router_path)

    ledger = build_evidence_ledger()
    ledger_path = phase16_dir / "charles_evidence_ledger.json"
    write_json(ledger_path, ledger)

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase16_dir": str(phase16_dir),
        "router_path": str(router_path),
        "notes": note_paths,
        "changed_notes": changed_notes,
        "router_changed": router_changed,
        "squad_router_changed": squad_router_changed,
        "ledger_path": str(ledger_path),
    }

    report_path = phase16_dir / "charles_bootstrap_report.md"
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

    manifest_path = phase16_dir / f"phase16-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase16_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    print(f"Router: {result['router_path']}")
    print(f"Notes: {len(result['notes'])}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = run(Path(args.skills_root), Path(args.phase16_dir), Path(args.db_path), args.build_db)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
