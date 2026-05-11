#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


HOME = Path("/Users/vijaychauhan")
DEFAULT_OUTPUT = HOME / ".codex" / "skills" / "seo" / "memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB = HOME / "squad_memory" / "squad_memory.db"
DEFAULT_FIXTURES = HOME / "squad_memory" / "evals" / "fixtures.json"
DEFAULT_PHASE2 = HOME / "squad_memory" / "ingest" / "phase2" / "latest.json"
DEFAULT_PHASE3_DIR = HOME / "squad_memory" / "ingest" / "phase3"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 3 clustering, freshness, and eval gate")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--skills-root", default=str(DEFAULT_SKILLS_ROOT))
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--fixtures", default=str(DEFAULT_FIXTURES))
    parser.add_argument("--phase2-manifest", default=str(DEFAULT_PHASE2))
    parser.add_argument("--phase3-dir", default=str(DEFAULT_PHASE3_DIR))
    parser.add_argument("--min-primary-accuracy", type=float, default=90.0)
    parser.add_argument("--min-top3-hit", type=float, default=95.0)
    parser.add_argument("--min-top5-path", type=float, default=95.0)
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
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    header = text[4:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta: Dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip().lower()] = value.strip()
    return meta, body


def meta_list(meta: Dict[str, str], key: str) -> List[str]:
    value = meta.get(key, "")
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_latest_published(body: str) -> str:
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("Latest published date:"):
            return line.split(":", 1)[1].strip()
    return ""


def freshness_score(iso_date: str) -> float:
    if not iso_date:
        return 0.0
    try:
        published = date.fromisoformat(iso_date)
    except ValueError:
        return 0.0
    age_days = max((date.today() - published).days, 0)
    if age_days <= 1:
        return 1.0
    if age_days <= 7:
        return 0.85
    if age_days <= 30:
        return 0.65
    if age_days <= 90:
        return 0.4
    return 0.2


def canonical_notes(output_dir: Path) -> List[Path]:
    return sorted(path for path in output_dir.glob("live-source-canon-*.md") if path.name != "live-source-canon.md")


def load_note_stats(path: Path) -> Dict[str, Any]:
    meta, body = parse_frontmatter(path.read_text())
    latest = parse_latest_published(body)
    topic = meta.get("topic", "live_source_ingest")
    confidence = meta.get("confidence", "medium")
    return {
        "path": str(path),
        "filename": path.name,
        "title": meta.get("title", path.stem),
        "topic": topic,
        "confidence": confidence,
        "latest_published": latest,
        "freshness": freshness_score(latest),
        "roles": meta_list(meta, "role"),
        "intent": meta_list(meta, "intent"),
    }


def build_cluster_report(note_stats: Sequence[Dict[str, Any]], gate: Dict[str, Any]) -> str:
    clusters: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for item in note_stats:
        clusters[item["topic"]].append(item)

    lines = [
        "---",
        "source: local phase3 cluster refresh",
        "title: Live Source Cluster Report",
        f"scraped: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: phase3_cluster_refresh, freshness, eval_gate",
        "topic: live_source_clusters",
        "intent: monitoring, routing, promotion_gate",
        "role: researcher, seo, pinchy",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Live source cluster report",
        "use_for: freshness, promotion_gate, source_selection",
        "avoid_for: final_strategy_without_supporting_memory",
        "---",
        "",
        "# Live Source Cluster Report",
        "",
        f"Eval gate: {'approved' if gate['approved'] else 'blocked'}",
        f"Primary accuracy: {gate['primary_accuracy']:.2f}",
        f"Top-3 skill hit: {gate['top3_skill_hit']:.2f}",
        f"Top-5 path hit: {gate['top5_path_hit']:.2f}",
        "",
        "## Freshest Notes",
    ]
    for item in sorted(note_stats, key=lambda row: (-row["freshness"], row["filename"]))[:8]:
        lines.append(
            f"- [{item['filename']}](./{item['filename']}) | topic={item['topic']} | latest={item['latest_published'] or 'unknown'} | freshness={item['freshness']:.2f}"
        )

    lines.extend(["", "## Topic Clusters"])
    for topic, rows in sorted(clusters.items()):
        avg_freshness = sum(item["freshness"] for item in rows) / max(len(rows), 1)
        freshest = max(rows, key=lambda row: row["freshness"])
        lines.append(f"### {topic}")
        lines.append(
            f"- sources={len(rows)} | avg_freshness={avg_freshness:.2f} | freshest=[{freshest['filename']}](./{freshest['filename']})"
        )
        for item in sorted(rows, key=lambda row: (-row["freshness"], row["filename"])):
            lines.append(f"  - {item['filename']} | latest={item['latest_published'] or 'unknown'} | confidence={item['confidence']}")
    return "\n".join(lines) + "\n"


def parse_eval_metrics(stdout: str) -> Dict[str, float]:
    metrics = {
        "primary_accuracy": 0.0,
        "top3_skill_hit": 0.0,
        "top5_path_hit": 0.0,
    }
    for line in stdout.splitlines():
        line = line.strip()
        if line.startswith("Primary skill accuracy:"):
            metrics["primary_accuracy"] = float(line.split(":", 1)[1].strip().rstrip("%"))
        elif line.startswith("Top-3 skill hit rate:"):
            metrics["top3_skill_hit"] = float(line.split(":", 1)[1].strip().rstrip("%"))
        elif line.startswith("Top-5 path hit rate:"):
            metrics["top5_path_hit"] = float(line.split(":", 1)[1].strip().rstrip("%"))
    return metrics


def run_phase3(
    output_dir: Path,
    skills_root: Path,
    db_path: Path,
    fixtures: Path,
    phase2_manifest: Path,
    phase3_dir: Path,
    min_primary_accuracy: float,
    min_top3_hit: float,
    min_top5_path: float,
) -> Dict[str, Any]:
    _ = load_json(phase2_manifest, {})
    note_stats = [load_note_stats(path) for path in canonical_notes(output_dir)]

    build_cmd = [sys.executable, str(HOME / "squad_memory" / "squad_memory.py"), "build", "--root", str(skills_root), "--db", str(db_path)]
    build_run = subprocess.run(build_cmd, check=False, capture_output=True, text=True)
    if build_run.returncode != 0:
        raise SystemExit(build_run.returncode)

    eval_cmd = [sys.executable, str(HOME / "squad_memory" / "squad_memory.py"), "eval", "--db", str(db_path), "--fixtures", str(fixtures)]
    eval_run = subprocess.run(eval_cmd, check=False, capture_output=True, text=True)
    if eval_run.returncode != 0:
        raise SystemExit(eval_run.returncode)

    metrics = parse_eval_metrics(eval_run.stdout)
    approved = (
        metrics["primary_accuracy"] >= min_primary_accuracy
        and metrics["top3_skill_hit"] >= min_top3_hit
        and metrics["top5_path_hit"] >= min_top5_path
    )
    gate = {
        **metrics,
        "approved": approved,
        "thresholds": {
            "primary_accuracy": min_primary_accuracy,
            "top3_skill_hit": min_top3_hit,
            "top5_path_hit": min_top5_path,
        },
        "build_stdout": build_run.stdout.strip(),
        "eval_stdout": eval_run.stdout.strip(),
    }

    cluster_note = output_dir / "live-source-cluster-report.md"
    cluster_note.write_text(build_cluster_report(note_stats, gate))

    clusters: Dict[str, Dict[str, Any]] = {}
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for item in note_stats:
        grouped[item["topic"]].append(item)
    for topic, rows in grouped.items():
        clusters[topic] = {
            "note_count": len(rows),
            "avg_freshness": round(sum(item["freshness"] for item in rows) / max(len(rows), 1), 4),
            "freshest_note": max(rows, key=lambda row: row["freshness"])["filename"],
            "notes": [item["filename"] for item in sorted(rows, key=lambda row: (-row["freshness"], row["filename"]))],
        }

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    manifest = {
        "run_id": run_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "db_path": str(db_path),
        "fixtures": str(fixtures),
        "cluster_note": str(cluster_note),
        "gate": gate,
        "clusters": clusters,
        "notes": note_stats,
    }
    write_json(phase3_dir / f"phase3-{run_id}.json", manifest)
    write_json(phase3_dir / "latest.json", manifest)
    return manifest


def print_manifest(manifest: Dict[str, Any]) -> None:
    gate = manifest["gate"]
    print(f"Run ID: {manifest['run_id']}")
    print(f"Cluster note: {manifest['cluster_note']}")
    print(f"Gate: {'approved' if gate['approved'] else 'blocked'}")
    print(
        f"Metrics: primary={gate['primary_accuracy']:.2f} top3={gate['top3_skill_hit']:.2f} top5={gate['top5_path_hit']:.2f}"
    )
    for topic, item in sorted(manifest["clusters"].items()):
        print(f"- {topic}: notes={item['note_count']} freshest={item['freshest_note']} avg_freshness={item['avg_freshness']:.2f}")


def main() -> int:
    args = parse_args()
    manifest = run_phase3(
        output_dir=Path(args.output_dir),
        skills_root=Path(args.skills_root),
        db_path=Path(args.db_path),
        fixtures=Path(args.fixtures),
        phase2_manifest=Path(args.phase2_manifest),
        phase3_dir=Path(args.phase3_dir),
        min_primary_accuracy=args.min_primary_accuracy,
        min_top3_hit=args.min_top3_hit,
        min_top5_path=args.min_top5_path,
    )
    if args.json:
        print(json.dumps(manifest, indent=2, ensure_ascii=True))
    else:
        print_manifest(manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
