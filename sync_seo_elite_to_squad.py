#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set


HOME = Path("/Users/vijaychauhan")
BASE = HOME / "squad_memory"
DEFAULT_SOURCE_ROOT = HOME / ".codex" / "elite-skills" / "seo-elite" / "memory"
DEFAULT_TARGET_ROOT = HOME / ".codex" / "skills" / "seo" / "memory" / "imports" / "seo-elite"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_SQUAD_DB = BASE / "squad_memory.db"
DEFAULT_PHASE31_DIR = BASE / "ingest" / "phase31"
DEFAULT_RECENT_HOURS = 24 * 30
DEFAULT_MAX_RECENT_ARTICLES = 800


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync fresh SEO Elite notes into the main squad memory corpus")
    parser.add_argument("--source-root", default=str(DEFAULT_SOURCE_ROOT))
    parser.add_argument("--target-root", default=str(DEFAULT_TARGET_ROOT))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--squad-db", default=str(DEFAULT_SQUAD_DB))
    parser.add_argument("--phase31-dir", default=str(DEFAULT_PHASE31_DIR))
    parser.add_argument("--recent-hours", type=int, default=DEFAULT_RECENT_HOURS)
    parser.add_argument("--max-recent-articles", type=int, default=DEFAULT_MAX_RECENT_ARTICLES)
    parser.add_argument("--build-squad-db", action="store_true")
    parser.add_argument("--refresh-graph", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def iter_matches(root: Path, patterns: Sequence[str]) -> Iterable[Path]:
    for pattern in patterns:
        yield from root.glob(pattern)


def select_recent_articles(source_root: Path, recent_hours: int, max_articles: int) -> List[Path]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=recent_hours)
    candidates: List[Path] = []
    for pattern in ("articles/**/*.md", "archive/articles/**/*.md"):
        for path in source_root.glob(pattern):
            if not path.is_file():
                continue
            modified = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
            if modified >= cutoff:
                candidates.append(path)
    candidates.sort(key=lambda item: item.stat().st_mtime, reverse=True)
    return candidates[:max_articles]


def select_files(source_root: Path, recent_hours: int, max_recent_articles: int) -> List[Path]:
    selected: Set[Path] = set()
    static_patterns = (
        "live-knowledge-monitor.md",
        "live-source-*.md",
        "live-source-canon*.md",
        "live-source-cluster-report.md",
        "primary/**/*.md",
        "archive/live-archive-monitor.md",
        "archive/live-source-*.md",
        "archive/realtime-semrush-top30-monitor.md",
        "archive/bulk/bulk-backfill-monitor.md",
        "archive/bulk/bulk-source-*.md",
    )
    for path in iter_matches(source_root, static_patterns):
        if path.is_file():
            selected.add(path)
    selected.update(select_recent_articles(source_root, recent_hours, max_recent_articles))
    return sorted(selected)


def files_equal(source: Path, target: Path) -> bool:
    if not target.exists():
        return False
    if source.stat().st_size != target.stat().st_size:
        return False
    return source.read_bytes() == target.read_bytes()


def copy_selected_files(source_root: Path, target_root: Path, selected: Sequence[Path]) -> Dict[str, object]:
    target_root.mkdir(parents=True, exist_ok=True)
    desired_targets: Set[Path] = set()
    copied: List[str] = []
    unchanged = 0

    for source in selected:
        relative = source.relative_to(source_root)
        target = target_root / relative
        desired_targets.add(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        if files_equal(source, target):
            unchanged += 1
            continue
        shutil.copy2(source, target)
        copied.append(str(relative))

    generated = {
        target_root / "IMPORT_INDEX.md",
        target_root / "bridge-manifest.json",
    }
    desired_targets.update(generated)

    removed: List[str] = []
    for path in sorted(target_root.rglob("*")):
        if not path.is_file():
            continue
        if path not in desired_targets:
            removed.append(str(path.relative_to(target_root)))
            path.unlink()

    return {
        "copied": copied,
        "removed": removed,
        "unchanged": unchanged,
    }


def build_index_note(
    source_root: Path,
    selected: Sequence[Path],
    recent_hours: int,
    max_recent_articles: int,
) -> str:
    article_paths = [path for path in selected if "/articles/" in path.as_posix()]
    recent_preview = article_paths[:30]
    latest_source_update = max(
        datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc) for path in selected
    ) if selected else datetime.now(timezone.utc)
    lines = [
        "---",
        "source: seo elite import bridge",
        "title: SEO Elite Import Bridge",
        f"scraped: {latest_source_update.date().isoformat()}",
        "tags: seo-elite, import-bridge, vector-db, freshness, monitoring",
        "topic: seo_research, vector_memory, source_selection",
        "intent: monitoring, import_routing, research",
        "role: researcher, seo, pinchy, chitin",
        "confidence: high",
        "canonical: true",
        "canonical_group: SEO Elite import bridge",
        "use_for: loading fresh SEO Elite monitoring and recent article notes into squad memory",
        "avoid_for: assuming every elite note is mirrored here; this bridge intentionally prioritizes freshness",
        "---",
        "",
        "# SEO Elite Import Bridge",
        "",
        f"Source root: `{source_root}`",
        f"Imported markdown files: `{len(selected)}`",
        f"Recent article window: `{recent_hours}` hours",
        f"Recent article cap: `{max_recent_articles}`",
        f"Recent article notes included: `{len(article_paths)}`",
        f"Latest source update: `{latest_source_update.isoformat()}`",
        "",
        "## Included Layers",
        "- Live source monitors and canon notes",
        "- Primary-source research notes",
        "- Archive source monitors and bulk source summaries",
        "- Recent harvested article notes for freshness-weighted retrieval",
        "",
        "## Recent Article Preview",
    ]
    if recent_preview:
        for path in recent_preview:
            rel = path.relative_to(source_root)
            lines.append(f"- `{rel.as_posix()}`")
    else:
        lines.append("- No recent article notes matched the current freshness window.")
    lines.append("")
    return "\n".join(lines) + "\n"


def write_generated_files(
    target_root: Path,
    source_root: Path,
    selected: Sequence[Path],
    recent_hours: int,
    max_recent_articles: int,
    sync_result: Dict[str, object],
) -> bool:
    changed = False
    index_path = target_root / "IMPORT_INDEX.md"
    manifest_path = target_root / "bridge-manifest.json"

    index_body = build_index_note(source_root, selected, recent_hours, max_recent_articles)
    if not index_path.exists() or index_path.read_text() != index_body:
        index_path.write_text(index_body)
        changed = True

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(source_root),
        "target_root": str(target_root),
        "selected_files": [str(path.relative_to(source_root)) for path in selected],
        "copied": sync_result["copied"],
        "removed": sync_result["removed"],
        "unchanged": sync_result["unchanged"],
        "recent_hours": recent_hours,
        "max_recent_articles": max_recent_articles,
        "recent_article_files": len([path for path in selected if "/articles/" in path.as_posix()]),
        "latest_source_update": max(
            datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat() for path in selected
        ) if selected else "",
    }
    manifest_body = json.dumps(manifest, indent=2, ensure_ascii=True) + "\n"
    if not manifest_path.exists() or manifest_path.read_text() != manifest_body:
        manifest_path.write_text(manifest_body)
        changed = True

    return changed


def run_command(command: List[str]) -> Dict[str, object]:
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def require_success(result: Dict[str, object], label: str) -> None:
    if int(result["returncode"]) != 0:
        raise SystemExit(f"{label} failed: {result['stderr'] or result['stdout']}")


def main() -> int:
    args = parse_args()
    source_root = Path(args.source_root)
    target_root = Path(args.target_root)
    skills_root = Path(args.skills_root)
    squad_db = Path(args.squad_db)

    selected = select_files(source_root, args.recent_hours, args.max_recent_articles)
    sync_result = copy_selected_files(source_root, target_root, selected)
    generated_changed = write_generated_files(
        target_root,
        source_root,
        selected,
        args.recent_hours,
        args.max_recent_articles,
        sync_result,
    )

    changed = bool(sync_result["copied"] or sync_result["removed"] or generated_changed)
    build_result: Dict[str, object] | None = None
    graph_result: Dict[str, object] | None = None

    if changed and args.build_squad_db:
        build_result = run_command(
            [
                sys.executable,
                str(BASE / "squad_memory.py"),
                "build",
                "--root",
                str(skills_root),
                "--db",
                str(squad_db),
            ]
        )
        require_success(build_result, "squad_memory build")

    if changed and args.build_squad_db and args.refresh_graph:
        graph_result = run_command(
            [
                sys.executable,
                str(BASE / "phase31_memory_graph.py"),
                "build",
                "--db-path",
                str(squad_db),
                "--phase31-dir",
                str(Path(args.phase31_dir)),
            ]
        )
        require_success(graph_result, "phase31 graph build")

    payload = {
        "changed": changed,
        "selected_files": len(selected),
        "copied_files": len(sync_result["copied"]),
        "removed_files": len(sync_result["removed"]),
        "unchanged_files": int(sync_result["unchanged"]),
        "recent_hours": args.recent_hours,
        "max_recent_articles": args.max_recent_articles,
        "target_root": str(target_root),
        "build": build_result,
        "graph": graph_result,
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(f"SEO Elite import sync changed={str(changed).lower()} selected={len(selected)} copied={len(sync_result['copied'])} removed={len(sync_result['removed'])}")
        if build_result and build_result.get("stdout"):
            print(str(build_result["stdout"]))
        if graph_result and graph_result.get("stdout"):
            print(str(graph_result["stdout"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
