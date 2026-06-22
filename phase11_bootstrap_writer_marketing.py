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
from typing import Any, Dict, List, Tuple


HOME = Path("/Users/vijaychauhan")
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_PHASE11_DIR = HOME / "squad_memory" / "ingest" / "phase11"
DEFAULT_DB_PATH = HOME / "squad_memory" / "squad_memory.db"
BASE = HOME / "squad_memory"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
HEADING_RE = re.compile(r"^##\s+Core Concept\s*$", re.MULTILINE)

DOMAIN_CONFIG = {
    "writer": {
        "router": "MEMORY.md",
        "canon_filename": "writer-operating-canon-2026.md",
        "title": "Writer Operating Canon 2026",
        "topic": "writer_core",
        "intent": "writing, drafting, revision, editorial",
        "role": "plankton, pinchy, current",
        "use_for": "writer_briefing, editorial_routing, domain_canon",
        "avoid_for": "seo_audits, code_implementation",
        "canonical_group": "Writer operating canon",
        "domain_label": "Writer",
        "consensus": [
            "The writer system starts from the brief, not from improvisation.",
            "Strong openings, visible structure, and format-fit editing matter as much as the underlying idea.",
            "Different writing formats change pacing and delivery, but clarity and reader progress stay constant across all of them.",
        ],
        "tension": [
            "The main tradeoff is depth versus speed: landing-page and email work need compression, while guides and blog drafts need enough structure to carry complexity without losing readability.",
        ],
        "action": "Use this canon first for general writing tasks, then open the specific note for the target format or revision problem.",
        "bundle_roles": ["Plankton", "Pinchy", "Current"],
    },
    "marketing": {
        "router": "MEMORY.md",
        "canon_filename": "marketing-operating-canon-2026.md",
        "title": "Marketing Operating Canon 2026",
        "topic": "marketing_core",
        "intent": "distribution, promotion, launch, reporting",
        "role": "current, charles, pinchy",
        "use_for": "marketing_briefing, rollout_routing, domain_canon",
        "avoid_for": "technical_seo, engineering_specs",
        "canonical_group": "Marketing operating canon",
        "domain_label": "Marketing",
        "consensus": [
            "Distribution is part of the work, not a post-publication afterthought.",
            "The same asset should become multiple native outputs instead of one recycled post.",
            "Launches and reporting loops matter because promotion quality improves only when the team captures patterns and reuses them.",
        ],
        "tension": [
            "The main tradeoff is reach versus fit: more channels can increase exposure, but weak platform adaptation lowers the value of that reach.",
        ],
        "action": "Use this canon first for rollout, repurposing, or launch work, then open the format-specific note for the channel or reporting layer.",
        "bundle_roles": ["Current", "Charles", "Pinchy"],
    },
}


@dataclass
class NoteDoc:
    rel_path: str
    abs_path: Path
    title: str
    meta: Dict[str, str]
    body: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 11 writer and marketing canon bootstrap")
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--phase11-dir", default=str(DEFAULT_PHASE11_DIR))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--build-db", action="store_true", help="Rebuild squad_memory after phase 11 changes")
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


def build_frontmatter(meta: Dict[str, str]) -> str:
    return "---\n" + "\n".join(f"{key}: {value}" for key, value in meta.items()) + "\n---\n\n"


def extract_title(meta: Dict[str, str], body: str, fallback: str) -> str:
    if meta.get("title", "").strip():
        return meta["title"].strip()
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


def read_note(path: Path) -> NoteDoc:
    text = path.read_text()
    meta, body = parse_frontmatter(text)
    title = extract_title(meta, body, path.stem.replace("-", " "))
    return NoteDoc(
        rel_path=f"{path.parents[1].name}/memory/{path.name}",
        abs_path=path,
        title=title,
        meta=meta,
        body=body,
    )


def extract_core_concept(body: str) -> str:
    match = HEADING_RE.search(body)
    if not match:
        lines = [line.strip() for line in body.splitlines() if line.strip() and not line.startswith("#")]
        return lines[0] if lines else ""
    remainder = body[match.end() :].strip()
    if not remainder:
        return ""
    return remainder.split("\n\n", 1)[0].strip()


def parse_router_note_paths(router_path: Path) -> List[str]:
    lines = router_path.read_text().splitlines()
    in_canon = False
    paths: List[str] = []
    for raw in lines:
        line = raw.strip()
        if line == "## Canonical Notes":
            in_canon = True
            continue
        if in_canon and line.startswith("## "):
            break
        if in_canon and "`memory/" in line and line.endswith("`"):
            rel = line.split("`memory/", 1)[1][:-1]
            paths.append(rel)
    return paths


def replace_canonical_notes_block(router_path: Path, canon_filename: str) -> bool:
    text = router_path.read_text()
    lines = text.splitlines()
    in_canon = False
    start = end = None
    block: List[str] = []
    existing = False
    for idx, raw in enumerate(lines):
        line = raw.strip()
        if line == "## Canonical Notes":
            in_canon = True
            start = idx + 1
            continue
        if in_canon and line.startswith("## "):
            end = idx
            break
    if start is None:
        return False
    if end is None:
        end = len(lines)
    current = lines[start:end]
    for row in current:
        if canon_filename in row:
            existing = True
        if row.strip():
            block.append(row)
    if existing:
        return False
    label = canon_filename.replace(".md", "").replace("-", " ").title()
    new_block = [f"- {label}: `memory/{canon_filename}`", *block]
    updated = lines[:start] + new_block + lines[end:]
    router_path.write_text("\n".join(updated).rstrip() + "\n")
    return True


def replace_bundle_block(router_path: Path, role_name: str, canon_filename: str) -> bool:
    text = router_path.read_text()
    lines = text.splitlines()
    header = f"## {role_name} Bundle"
    start = end = None
    for idx, raw in enumerate(lines):
        if raw.strip() == header:
            start = idx + 1
            continue
        if start is not None and raw.strip().startswith("## "):
            end = idx
            break
    if start is None:
        return False
    if end is None:
        end = len(lines)
    block = lines[start:end]
    insert_line = f"- `memory/{canon_filename}`"
    if any(row.strip() == insert_line for row in block):
        return False
    updated_block = [insert_line] + [row for row in block if row.strip()]
    updated = lines[:start] + updated_block + lines[end:]
    router_path.write_text("\n".join(updated).rstrip() + "\n")
    return True


def build_domain_canon(domain: str, notes: List[NoteDoc], cfg: Dict[str, str]) -> str:
    lines = [
        build_frontmatter(
            {
                "title": cfg["title"],
                "topic": cfg["topic"],
                "intent": cfg["intent"],
                "role": cfg["role"],
                "use_for": cfg["use_for"],
                "avoid_for": cfg["avoid_for"],
                "confidence": "high",
                "canonical": "true",
                "canonical_group": cfg["canonical_group"],
                "source": "local_" + domain + "_memory",
                "scraped": datetime.now(timezone.utc).date().isoformat(),
                "tags": f"{domain}, operating canon, local memory, squad",
            }
        ).rstrip(),
        f"# {cfg['title']}",
        "",
        "## Core Concept",
        " ".join(cfg["consensus"][:2]),
        "",
        "## Domain Rules",
    ]
    for note in notes:
        summary = extract_core_concept(note.body).rstrip(".")
        lines.append(f"- **{note.title}**: {summary}.")
    lines.extend(
        [
            "",
            "## Workflow Map",
        ]
    )
    for idx, note in enumerate(notes, start=1):
        lines.append(f"{idx}. Open `{note.rel_path.split('/', 1)[1]}` when the task specifically needs {note.meta.get('use_for', note.title).replace('_', ' ')}.")
    lines.extend(
        [
            "",
            "## Team Use",
            f"- **{cfg['domain_label']} specialist**: Start here for broad domain work before narrowing into format-specific notes.",
            "- **Pinchy**: Use this canon when choosing the right specialist and deciding whether the task is broad workflow work or a narrow format problem.",
            "- **Cross-functional squad**: Use the linked notes only when the task moves from general planning into execution for a specific format or channel.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_domain_evidence(domain: str, canon_rel_path: str, notes: List[NoteDoc], cfg: Dict[str, str]) -> Dict[str, Any]:
    return {
        "topic": cfg["topic"],
        "primary_path": canon_rel_path,
        "evidence_paths": [canon_rel_path, *[note.rel_path for note in notes]],
        "distinct_sources": [f"Local {cfg['domain_label']} memory"],
        "source_count": 1,
        "evidence_count": len(notes) + 1,
        "freshness_score": 1.0,
        "freshness_label": "current",
        "confidence_score": 0.9,
        "confidence_label": "high",
        "consensus": cfg["consensus"],
        "tension": cfg["tension"],
        "squad_action": cfg["action"],
        "source_signals": [
            {
                "source": f"Local {cfg['domain_label']} memory",
                "path": note.rel_path,
                "summary": extract_core_concept(note.body) or note.title,
            }
            for note in notes
        ],
    }


def build_phase11_block(evidence: Dict[str, Any]) -> str:
    lines = [
        "## Phase 11 Domain Fusion",
        "",
        f"Evidence confidence: {evidence['confidence_label']}",
        f"Freshness status: {evidence['freshness_label']}",
        "",
        "### Consensus",
    ]
    for row in evidence["consensus"]:
        lines.append(f"- {row}")
    lines.extend(["", "### Tension / Caveat"])
    for row in evidence["tension"]:
        lines.append(f"- {row}")
    lines.extend(["", "### Supporting Notes"])
    for item in evidence["source_signals"][:8]:
        lines.append(f"- `{Path(item['path']).name}`: {item['summary'].rstrip('.')}.")
    lines.extend(["", "### Squad Action", f"- {evidence['squad_action']}"])
    return "\n".join(lines)


def replace_phase11_block(body: str, block: str) -> str:
    begin = "<!-- phase11:begin -->"
    end = "<!-- phase11:end -->"
    managed = f"{begin}\n{block.rstrip()}\n{end}"
    pattern = re.compile(r"\n?<!-- phase11:begin -->.*?<!-- phase11:end -->\n?", re.DOTALL)
    if pattern.search(body):
        return pattern.sub("\n\n" + managed + "\n", body).rstrip() + "\n"
    return body.rstrip() + "\n\n" + managed + "\n"


def write_note(path: Path, text: str) -> bool:
    if path.exists() and path.read_text() == text:
        return False
    path.write_text(text)
    return True


def write_note_body(path: Path, transform) -> bool:
    text = path.read_text()
    meta, body = parse_frontmatter(text)
    new_body = transform(body)
    if new_body == body:
        return False
    rebuilt = build_frontmatter(meta) + new_body.lstrip("\n")
    path.write_text(rebuilt)
    return True


def bootstrap_domain(skills_root: Path, phase11_dir: Path, domain: str, cfg: Dict[str, str]) -> Dict[str, Any]:
    domain_root = skills_root / domain
    router_path = domain_root / cfg["router"]
    memory_root = domain_root / "memory"
    canon_path = memory_root / cfg["canon_filename"]

    router_note_paths = parse_router_note_paths(router_path)
    notes = [read_note(memory_root / Path(rel).name) for rel in router_note_paths if Path(rel).name != cfg["canon_filename"]]

    canon_text = build_domain_canon(domain, notes, cfg)
    canon_changed = write_note(canon_path, canon_text)

    router_changed = replace_canonical_notes_block(router_path, cfg["canon_filename"])
    bundle_changes = []
    for role_name in cfg["bundle_roles"]:
        changed = replace_bundle_block(router_path, role_name, cfg["canon_filename"])
        if changed:
            bundle_changes.append(role_name)

    canon_rel = f"{domain}/memory/{cfg['canon_filename']}"
    evidence = build_domain_evidence(domain, canon_rel, notes, cfg)
    ledger_path = phase11_dir / f"{domain}_evidence_ledger.json"
    write_json(ledger_path, {"generated_at": datetime.now(timezone.utc).isoformat(), "topics": {cfg["topic"]: evidence}, "primary_paths": {canon_rel: evidence}})

    phase11_changed = write_note_body(canon_path, lambda body, evidence=evidence: replace_phase11_block(body, build_phase11_block(evidence)))

    return {
        "domain": domain,
        "canon_path": str(canon_path),
        "ledger_path": str(ledger_path),
        "canon_changed": canon_changed,
        "router_changed": router_changed,
        "bundle_changes": bundle_changes,
        "note_count": len(notes),
        "primary_path": canon_rel,
    }


def build_report(results: List[Dict[str, Any]]) -> str:
    lines = [
        "---",
        "source: local phase11 writer-marketing bootstrap",
        "title: Writer Marketing Bootstrap Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase11_bootstrap, writer, marketing, domain_canon",
        "topic: writer_marketing_bootstrap",
        "intent: maintenance, routing, canon_bootstrap",
        "role: pinchy, plankton, current, charles",
        "confidence: high",
        "canonical: false",
        "canonical_group: Writer marketing bootstrap",
        "use_for: domain_bootstrap, writer_marketing_routing",
        "avoid_for: seo_strategy",
        "---",
        "",
        "# Writer Marketing Bootstrap Report",
        "",
    ]
    for item in results:
        lines.extend(
            [
                f"## {item['domain'].title()}",
                f"- Canon note: `{item['primary_path']}`",
                f"- Memory notes linked: {item['note_count']}",
                f"- Canon updated: {item['canon_changed']}",
                f"- Router updated: {item['router_changed']}",
                f"- Bundles updated: {', '.join(item['bundle_changes']) if item['bundle_changes'] else 'none'}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def run(skills_root: Path, phase11_dir: Path, db_path: Path, build_db: bool) -> Dict[str, Any]:
    phase11_dir.mkdir(parents=True, exist_ok=True)
    results = [bootstrap_domain(skills_root, phase11_dir, domain, cfg) for domain, cfg in DOMAIN_CONFIG.items()]

    report_path = phase11_dir / "writer_marketing_bootstrap_report.md"
    report_path.write_text(build_report(results))

    build_result = None
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
        build_result = {
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "db_path": str(db_path),
        }

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase11_dir": str(phase11_dir),
        "report_path": str(report_path),
        "domains": results,
    }
    if build_result:
        result["build"] = build_result

    manifest_path = phase11_dir / f"phase11-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(manifest_path, result)
    write_json(phase11_dir / "latest.json", result)
    result["manifest_path"] = str(manifest_path)
    return result


def print_result(result: Dict[str, Any]) -> None:
    print(f"Report: {result['report_path']}")
    for item in result["domains"]:
        print(f"{item['domain']}: canon={item['primary_path']} notes={item['note_count']}")
    if result.get("build"):
        print(f"Build DB: rc={result['build']['returncode']} db={result['build']['db_path']}")
        if result["build"]["stdout"]:
            print(result["build"]["stdout"])


def main() -> int:
    args = parse_args()
    result = run(
        skills_root=Path(args.skills_root),
        phase11_dir=Path(args.phase11_dir),
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
