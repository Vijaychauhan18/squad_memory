#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from phase7_merge_canon import run as run_phase7


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_PHASE6_DECISIONS = BASE / "ingest" / "phase6" / "decisions.json"
DEFAULT_PHASE7_REGISTRY = BASE / "ingest" / "phase7" / "canonical_registry.json"
DEFAULT_PHASE7_DIR = BASE / "ingest" / "phase7"
DEFAULT_PHASE8_DIR = BASE / "ingest" / "phase8"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = BASE / "squad_memory.db"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 8 canonical promotion for orphan primary notes")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--phase6-decisions", default=str(DEFAULT_PHASE6_DECISIONS))
    parser.add_argument("--phase7-registry", default=str(DEFAULT_PHASE7_REGISTRY))
    parser.add_argument("--phase7-dir", default=str(DEFAULT_PHASE7_DIR))
    parser.add_argument("--phase8-dir", default=str(DEFAULT_PHASE8_DIR))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true", help="Rebuild squad_memory after canonical promotion")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")


def parse_frontmatter(text: str) -> Tuple[List[str], str]:
    if not text.startswith("---\n"):
        return [], text
    end = text.find("\n---", 4)
    if end == -1:
        return [], text
    header = text[4:end].splitlines()
    body = text[end + 4 :].lstrip("\n")
    return header, body


def humanize_topic(topic: str) -> str:
    cleaned = topic.replace("__", "_").strip("_")
    if not cleaned:
        return "Canonical note"
    return cleaned.replace("_", " ").strip().capitalize()


def update_frontmatter(path: Path, updates: Dict[str, str]) -> bool:
    text = path.read_text()
    header_lines, body = parse_frontmatter(text)
    if not header_lines:
        header_lines = []
    key_index: Dict[str, int] = {}
    for idx, line in enumerate(header_lines):
        if ":" not in line:
            continue
        key = line.split(":", 1)[0].strip().lower()
        key_index[key] = idx

    changed = False
    for key, value in updates.items():
        line = f"{key}: {value}"
        if key in key_index:
            if header_lines[key_index[key]] != line:
                header_lines[key_index[key]] = line
                changed = True
        else:
            insert_at = len(header_lines)
            if "canonical_group" in key_index and key == "canonical":
                insert_at = key_index["canonical_group"]
            header_lines.insert(insert_at, line)
            changed = True
            key_index = {}
            for idx, row in enumerate(header_lines):
                if ":" in row:
                    key_index[row.split(":", 1)[0].strip().lower()] = idx

    if not changed:
        return False

    rebuilt = "---\n" + "\n".join(header_lines).rstrip() + "\n---\n\n" + body.lstrip("\n")
    path.write_text(rebuilt)
    return True


def run(
    output_dir: Path,
    phase6_decisions: Path,
    phase7_registry: Path,
    phase7_dir: Path,
    phase8_dir: Path,
    skills_root: Path,
    db_path: Path,
    build_db: bool,
) -> Dict[str, Any]:
    phase8_dir.mkdir(parents=True, exist_ok=True)
    registry = load_json(phase7_registry, {})
    note_states = registry.get("notes", {})
    changed: List[Dict[str, str]] = []
    skipped: List[Dict[str, str]] = []

    for rel_path, info in sorted(note_states.items()):
        if info.get("status") != "orphan_primary":
            continue
        topic = str(info.get("topic", "")).strip()
        if topic == "__untagged__" or not topic:
            skipped.append({"path": rel_path, "reason": "manual topic review required"})
            continue

        abs_path = output_dir / Path(rel_path).name
        if not abs_path.exists():
            skipped.append({"path": rel_path, "reason": "missing note file"})
            continue

        canonical_group = humanize_topic(topic)
        did_change = update_frontmatter(
            abs_path,
            {
                "canonical": "true",
                "canonical_group": canonical_group,
                "canonicalized_on": datetime.now(timezone.utc).date().isoformat(),
                "canonicalized_by": "phase8_promote_canon",
            },
        )
        if did_change:
            changed.append(
                {
                    "path": rel_path,
                    "topic": topic,
                    "canonical_group": canonical_group,
                }
            )

    refreshed_phase7 = run_phase7(output_dir=output_dir, phase6_decisions=phase6_decisions, phase7_dir=phase7_dir)

    build_result = None
    if build_db and changed:
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

    report_path = phase8_dir / "canonical_promotion_report.md"
    report_path.write_text(build_report(changed, skipped, refreshed_phase7))

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase8_dir": str(phase8_dir),
        "phase7_registry": str(phase7_registry),
        "changed": changed,
        "skipped": skipped,
        "report_path": str(report_path),
        "refreshed_phase7": refreshed_phase7,
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase8_dir / f"phase8-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase8_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def build_report(changed: List[Dict[str, str]], skipped: List[Dict[str, str]], refreshed_phase7: Dict[str, Any]) -> str:
    health = refreshed_phase7["health"]
    lines = [
        "---",
        "source: local phase8 canonical promotion",
        "title: Canonical Promotion Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase8_promote_canon, canonical_promotion, orphan_primary",
        "topic: canonical_promotion",
        "intent: maintenance, canonical_synthesis",
        "role: pinchy, researcher, seo",
        "confidence: high",
        "canonical: false",
        "canonical_group: Canonical promotion",
        "use_for: canonical_maintenance, phase8_review",
        "avoid_for: direct_strategy_without_note_review",
        "---",
        "",
        "# Canonical Promotion Report",
        "",
        f"Canonicalized notes this run: {len(changed)}",
        f"Skipped notes this run: {len(skipped)}",
        f"Healthy topics after refresh: {health['healthy_topics']}",
        f"Topics still needing canonical synthesis: {health['topics_needing_canonical']}",
        "",
        "## Canonicalized Notes",
    ]
    if not changed:
        lines.append("- No notes were canonicalized in this run.")
    for item in changed:
        lines.append(f"- `{item['path']}` -> `{item['canonical_group']}`")

    lines.extend(["", "## Skipped"])
    if not skipped:
        lines.append("- No notes were skipped.")
    for item in skipped:
        lines.append(f"- `{item['path']}` | reason={item['reason']}")
    return "\n".join(lines) + "\n"


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    print(f"Canonicalized: {len(result['changed'])}")
    print(f"Skipped: {len(result['skipped'])}")
    print(f"Healthy topics: {result['refreshed_phase7']['health']['healthy_topics']}")
    print(f"Topics needing canonical synthesis: {result['refreshed_phase7']['health']['topics_needing_canonical']}")
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
