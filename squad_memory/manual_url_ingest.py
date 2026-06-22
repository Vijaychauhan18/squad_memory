#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import sqlite3
import subprocess
import sys
import threading
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from urllib.parse import urlparse

import knowledge_ingest


HOME = Path.home()
BASE = HOME / "squad_memory"
DEFAULT_SKILLS_ROOT = HOME / ".codex" / "skills"
DEFAULT_DB_PATH = BASE / "squad_memory.db"
DEFAULT_SNAPSHOT_DIR = BASE / "ingest" / "raw"
DEFAULT_RUNS_DIR = BASE / "ingest" / "runs"
DEFAULT_OUTPUT_ROOT = DEFAULT_SKILLS_ROOT / "seo" / "memory" / "articles" / "manual"
DEFAULT_MAX_HISTORY = 6
MANUAL_SOURCE_SLUG = "manual-url-ingest"
TARGET_DATASET_ID = "squad_memory"

ProgressCallback = Callable[[str, float, str, Optional[Dict[str, Any]]], None]
FetchHtmlFn = Callable[[str], str]
BuildDbFn = Callable[[Path, Path], Dict[str, Any]]
PerformIngestFn = Callable[..., Dict[str, Any]]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def now_local_iso() -> str:
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def build_run_id(now: Optional[datetime] = None) -> str:
    return (now or now_utc()).astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def validate_url(url: str) -> str:
    value = str(url or "").strip()
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Enter a valid http or https URL.")
    return value


def normalized_host(url: str) -> str:
    host = urlparse(url).netloc.lower().strip()
    if host.startswith("www."):
        host = host[4:]
    return host or "manual-source"


def host_slug(url: str) -> str:
    return knowledge_ingest.slugify(normalized_host(url))


def homepage_for_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}/"


def manual_source_config(url: str) -> Dict[str, Any]:
    host = normalized_host(url)
    slug = host_slug(url)
    return {
        "slug": slug,
        "name": host,
        "homepage": homepage_for_url(url),
        "domain": "seo",
        "kind": "manual_ingest",
        "strength": "On-demand dashboard URL capture for instant vector-memory enrichment.",
        "topic": "manual_ingest",
        "intent": ["research", "manual_ingest", "knowledge_capture", "chunk_growth"],
        "roles": ["researcher", "seo", "developer"],
        "tags": ["manual_ingest", "dashboard", "on_demand_capture", slug],
        "confidence": "medium",
        "paragraph_limit": 64,
    }


def safe_sqlite_counts(path: Path) -> Dict[str, int]:
    if not path.exists():
        return {"chunks": 0, "paths": 0}
    conn = sqlite3.connect(path)
    try:
        tables = {row[0] for row in conn.execute("select name from sqlite_master where type='table'")}
        if "chunks" not in tables:
            return {"chunks": 0, "paths": 0}
        row = conn.execute("select count(*), count(distinct path) from chunks").fetchone()
        return {"chunks": int(row[0] or 0), "paths": int(row[1] or 0)}
    finally:
        conn.close()


def manual_output_dir(skills_root: Path, url: str) -> Path:
    return skills_root / "seo" / "memory" / "articles" / "manual" / host_slug(url)


def article_url_hash(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]


def note_filename_for_url(url: str, title: str) -> str:
    return f"{knowledge_ingest.slugify(title)[:90]}-{article_url_hash(url)}.md"


def remove_prior_versions(output_dir: Path, url: str, keep_filename: str) -> None:
    suffix = f"-{article_url_hash(url)}.md"
    for candidate in output_dir.glob(f"*{suffix}"):
        if candidate.name == keep_filename:
            continue
        candidate.unlink(missing_ok=True)


def fallback_article_document(html: str, url: str, source_cfg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    title = (
        knowledge_ingest.extract_meta_content(html, "og:title", "twitter:title")
        or knowledge_ingest.first_heading_text(html)
        or knowledge_ingest.title_from_html(html)
    )
    title = title.strip()
    body_blocks = knowledge_ingest.extract_article_body_blocks(html, limit=96)
    paragraphs = [
        block
        for block in body_blocks
        if not block.startswith(("#", ">", "- ", "1. ", "2. ", "3. ", "4. ", "5. "))
    ]
    if not paragraphs:
        paragraphs = knowledge_ingest.extract_article_paragraphs(html, limit=64)
    summary = (
        knowledge_ingest.extract_meta_content(html, "description", "og:description", "twitter:description")
        or knowledge_ingest.extract_summary_from_block(html)
        or (paragraphs[0] if paragraphs else "")
    )
    if not title or len(title) < 8:
        return None
    if not paragraphs and not summary:
        return None
    headings = [knowledge_ingest.clean_extracted_text(block.lstrip("#").strip()) for block in body_blocks if block.startswith("#")]
    return {
        "title": title,
        "url": url,
        "published": knowledge_ingest.normalize_date(
            knowledge_ingest.extract_meta_content(html, "article:published_time", "og:published_time", "datePublished")
            or knowledge_ingest.extract_published_from_block(html)
        ),
        "summary": summary[:500],
        "paragraphs": paragraphs,
        "body_blocks": body_blocks or paragraphs,
        "headings": headings,
        "author": knowledge_ingest.extract_meta_content(html, "author", "article:author"),
        "schema_types": [],
        "source_name": source_cfg["name"],
        "domain": "seo",
    }


def extract_manual_article(html: str, url: str, source_cfg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    article = knowledge_ingest.extract_article_document(html, url, source_cfg)
    if article:
        return article
    return fallback_article_document(html, url, source_cfg)


def build_manual_article_note(
    source_cfg: Dict[str, Any],
    article: Dict[str, Any],
    run_id: str,
    db_path: Path,
) -> str:
    today = datetime.now(timezone.utc).date().isoformat()
    tags = ["manual_ingest", "dashboard", "on_demand_capture", host_slug(article["url"])]
    headings = [str(item).strip() for item in article.get("headings", []) if str(item).strip()]
    schema_types = [str(item).strip() for item in article.get("schema_types", []) if str(item).strip()]
    author = str(article.get("author", "")).strip()

    lines = [
        "---",
        f"source: {article['url']}",
        f"title: {article['title']}",
        f"scraped: {today}",
        f"published_on: {article.get('published', '')}",
        f"tags: {knowledge_ingest.yaml_list(tags)}",
        "topic: manual_ingest",
        "intent: research, manual_ingest, knowledge_capture, chunk_growth",
        "role: researcher, seo, developer",
        "confidence: medium",
        "canonical: false",
        "canonical_group: Manual URL Ingest - Dashboard",
        "use_for: rapid_knowledge_capture, vector_db_enrichment, article_retrieval",
        "avoid_for: final_strategy_without_manual_review",
        "---",
        "",
        f"# {article['title']}",
        "",
        "Source: Manual URL Ingest",
        f"Publisher Host: {source_cfg['name']}",
        f"Homepage: {source_cfg['homepage']}",
        f"Original URL: {article['url']}",
        f"Published: {article.get('published') or 'unknown'}",
        "Strength: Instant dashboard capture into durable squad memory.",
        "",
        "## Capture Context",
        f"- Run ID: `{run_id}`",
        f"- Target DB: `{db_path}`",
        f"- Capture Mode: `dashboard_manual_ingest`",
        "",
    ]

    if author or schema_types:
        lines.extend(
            [
                "## Metadata",
                *( [f"Author: {author}"] if author else [] ),
                *( [f"Schema types: {', '.join(schema_types)}"] if schema_types else [] ),
                "",
            ]
        )

    if headings:
        lines.extend(["## Section Outline"])
        for heading in headings[:14]:
            lines.append(f"- {heading}")
        lines.append("")

    lines.extend(
        [
            "## Summary",
            article.get("summary", "") or "No summary extracted.",
            "",
            "## Extracted Body",
        ]
    )
    body_blocks = article.get("body_blocks") or article.get("paragraphs", [])
    if not body_blocks:
        lines.append("- No body paragraphs extracted.")
    else:
        for block in body_blocks:
            lines.extend([str(block).strip(), ""])
    return "\n".join(lines).strip() + "\n"


def default_build_db(skills_root: Path, db_path: Path) -> Dict[str, Any]:
    completed = subprocess.run(
        [
            sys.executable,
            str(HOME / "squad_memory" / "squad_memory.py"),
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
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "db_path": str(db_path),
        "skills_root": str(skills_root),
    }


def perform_manual_ingest(
    url: str,
    *,
    skills_root: Path = DEFAULT_SKILLS_ROOT,
    db_path: Path = DEFAULT_DB_PATH,
    snapshot_dir: Path = DEFAULT_SNAPSHOT_DIR,
    runs_dir: Path = DEFAULT_RUNS_DIR,
    fetch_html_fn: FetchHtmlFn = knowledge_ingest.fetch_html,
    build_db_fn: BuildDbFn = default_build_db,
    progress_callback: Optional[ProgressCallback] = None,
) -> Dict[str, Any]:
    validated_url = validate_url(url)
    source_cfg = manual_source_config(validated_url)
    fetched_at = now_utc()
    run_id = build_run_id(fetched_at)
    counts_before = safe_sqlite_counts(db_path)

    def report(phase: str, percent: float, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        if progress_callback:
            progress_callback(phase, percent, message, extra or {})

    report(
        "fetching",
        12.0,
        "Fetching article HTML.",
        {
            "url": validated_url,
            "source_host": source_cfg["name"],
            "chunks_before": counts_before["chunks"],
            "paths_before": counts_before["paths"],
        },
    )
    html = fetch_html_fn(validated_url)

    report("extracting", 34.0, "Extracting structured article content.")
    article = extract_manual_article(html, validated_url, source_cfg)
    if not article:
        raise ValueError("Could not extract enough article content from that URL.")

    report("writing_note", 56.0, "Writing durable memory note.")
    output_dir = manual_output_dir(skills_root, validated_url)
    output_dir.mkdir(parents=True, exist_ok=True)
    snapshot_path = knowledge_ingest.save_article_snapshot(
        snapshot_dir,
        MANUAL_SOURCE_SLUG,
        validated_url,
        html,
        fetched_at,
    )
    note_filename = note_filename_for_url(validated_url, article["title"])
    remove_prior_versions(output_dir, validated_url, note_filename)
    note_path = output_dir / note_filename
    note_path.write_text(build_manual_article_note(source_cfg, article, run_id, db_path), encoding="utf-8")

    report(
        "building",
        74.0,
        "Rebuilding squad memory vector DB.",
        {
            "note_path": str(note_path),
            "snapshot_path": str(snapshot_path),
            "article_title": article["title"],
        },
    )
    build_summary = build_db_fn(skills_root, db_path)
    if int(build_summary.get("returncode", 1)) != 0:
        raise RuntimeError(build_summary.get("stderr") or build_summary.get("stdout") or "Vector DB rebuild failed.")

    counts_after = safe_sqlite_counts(db_path)
    manifest = {
        "run_id": run_id,
        "generated_at": fetched_at.isoformat(),
        "status": "ok",
        "url": validated_url,
        "source_host": source_cfg["name"],
        "output_dir": str(output_dir),
        "note_path": str(note_path),
        "note_filename": note_filename,
        "snapshot_path": str(snapshot_path),
        "db_path": str(db_path),
        "counts_before": counts_before,
        "counts_after": counts_after,
        "chunk_delta": counts_after["chunks"] - counts_before["chunks"],
        "path_delta": counts_after["paths"] - counts_before["paths"],
        "article": {
            "title": article["title"],
            "published": article.get("published", ""),
            "summary": article.get("summary", ""),
            "author": article.get("author", ""),
            "schema_types": list(article.get("schema_types", [])),
            "heading_count": len(article.get("headings", [])),
            "body_block_count": len(article.get("body_blocks", [])),
        },
        "build": build_summary,
        "target_dataset_id": TARGET_DATASET_ID,
    }
    manifest_path = runs_dir / f"manual-url-ingest-{run_id}.json"
    manifest["manifest_path"] = str(manifest_path)
    write_json(manifest_path, manifest)
    write_json(runs_dir / "manual-url-ingest-latest.json", manifest)

    report(
        "complete",
        100.0,
        "Knowledge captured and vector DB rebuilt.",
        {
            "note_path": str(note_path),
            "manifest_path": str(manifest_path),
            "chunks_after": counts_after["chunks"],
            "paths_after": counts_after["paths"],
            "chunk_delta": manifest["chunk_delta"],
            "path_delta": manifest["path_delta"],
        },
    )
    return manifest


class ManualUrlIngestManager:
    def __init__(
        self,
        *,
        skills_root: Path = DEFAULT_SKILLS_ROOT,
        db_path: Path = DEFAULT_DB_PATH,
        snapshot_dir: Path = DEFAULT_SNAPSHOT_DIR,
        runs_dir: Path = DEFAULT_RUNS_DIR,
        performer: PerformIngestFn = perform_manual_ingest,
        max_history: int = DEFAULT_MAX_HISTORY,
    ) -> None:
        self.skills_root = skills_root
        self.db_path = db_path
        self.snapshot_dir = snapshot_dir
        self.runs_dir = runs_dir
        self.performer = performer
        self.max_history = max_history
        self._lock = threading.Lock()
        self._current: Optional[Dict[str, Any]] = None
        self._history: List[Dict[str, Any]] = []

    def _copy(self, payload: Any) -> Any:
        return copy.deepcopy(payload)

    def _archive_current_locked(self) -> None:
        if not self._current:
            return
        archived = self._copy(self._current)
        self._history = [archived] + self._history
        self._history = self._history[: self.max_history]

    def _update_current(self, job_id: str, **fields: Any) -> None:
        with self._lock:
            if not self._current or self._current.get("id") != job_id:
                return
            self._current.update(fields)
            self._current["updated_at_iso"] = now_local_iso()

    def snapshot(self) -> Dict[str, Any]:
        with self._lock:
            current = self._copy(self._current)
            history = self._copy(self._history)
        return {
            "active": bool(current and current.get("status") == "running"),
            "can_start": not current or current.get("status") != "running",
            "target_dataset_id": TARGET_DATASET_ID,
            "target_db_path": str(self.db_path),
            "skills_root": str(self.skills_root),
            "current": current,
            "history": history,
        }

    def start(self, url: str) -> Dict[str, Any]:
        validated_url = validate_url(url)
        with self._lock:
            if self._current and self._current.get("status") == "running":
                raise RuntimeError("A manual URL ingest is already running. Wait for it to finish first.")
            if self._current:
                self._archive_current_locked()
            now_iso = now_local_iso()
            self._current = {
                "id": build_run_id(),
                "url": validated_url,
                "status": "running",
                "phase": "queued",
                "progress_percent": 0.0,
                "message": "Queued manual URL ingest.",
                "started_at_iso": now_iso,
                "updated_at_iso": now_iso,
                "target_dataset_id": TARGET_DATASET_ID,
                "target_db_path": str(self.db_path),
                "skills_root": str(self.skills_root),
                "source_host": normalized_host(validated_url),
            }
            job_id = str(self._current["id"])

        thread = threading.Thread(target=self._run_job, args=(job_id, validated_url), daemon=True)
        thread.start()
        return self.snapshot()

    def _run_job(self, job_id: str, url: str) -> None:
        def progress(phase: str, percent: float, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
            payload = {"phase": phase, "progress_percent": round(float(percent), 1), "message": message}
            if extra:
                payload.update(extra)
            self._update_current(job_id, **payload)

        try:
            result = self.performer(
                url,
                skills_root=self.skills_root,
                db_path=self.db_path,
                snapshot_dir=self.snapshot_dir,
                runs_dir=self.runs_dir,
                progress_callback=progress,
            )
            self._update_current(
                job_id,
                status="completed",
                phase="done",
                progress_percent=100.0,
                message="Knowledge captured and vector DB rebuilt.",
                result=result,
                note_path=result.get("note_path", ""),
                manifest_path=result.get("manifest_path", ""),
                snapshot_path=result.get("snapshot_path", ""),
                chunks_before=result.get("counts_before", {}).get("chunks", 0),
                chunks_after=result.get("counts_after", {}).get("chunks", 0),
                chunk_delta=result.get("chunk_delta", 0),
                paths_before=result.get("counts_before", {}).get("paths", 0),
                paths_after=result.get("counts_after", {}).get("paths", 0),
                path_delta=result.get("path_delta", 0),
                article_title=result.get("article", {}).get("title", ""),
            )
        except Exception as exc:
            self._update_current(
                job_id,
                status="error",
                phase="failed",
                message=str(exc),
                error_type=type(exc).__name__,
                traceback_excerpt=traceback.format_exc(limit=3),
            )
