from __future__ import annotations

import importlib.util
import sqlite3
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

MODULE_SPEC = importlib.util.spec_from_file_location("manual_url_ingest", BASE / "manual_url_ingest.py")
MANUAL_URL_INGEST = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
MODULE_SPEC.loader.exec_module(MANUAL_URL_INGEST)


class ManualUrlIngestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.snapshot_dir = self.root / "snapshots"
        self.runs_dir = self.root / "runs"
        self.db_path = self.root / "squad_memory.db"
        self._init_db()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _init_db(self) -> None:
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("create table chunks (path text)")
            conn.execute("insert into chunks(path) values (?)", ("seed/doc.md",))
            conn.commit()
        finally:
            conn.close()

    def test_perform_manual_ingest_writes_note_snapshot_and_manifest(self) -> None:
        html = """
        <html>
          <head>
            <title>Useful Travel SEO Field Notes</title>
            <meta name="description" content="Fresh field notes from a real travel SEO investigation." />
            <meta property="article:published_time" content="2026-04-25T12:00:00Z" />
          </head>
          <body>
            <article>
              <h1>Useful Travel SEO Field Notes</h1>
              <h2>What changed</h2>
              <p>We analyzed a live travel page, compared the extractable passages, and documented what made the page more citable in AI search.</p>
              <p>The key difference was not length. It was better evidence, cleaner sectioning, and clearer brand-level trust reinforcement around the page.</p>
            </article>
          </body>
        </html>
        """

        def fake_fetch_html(url: str) -> str:
            self.assertEqual(url, "https://example.com/articles/travel-seo-field-notes")
            return html

        def fake_build_db(_skills_root: Path, path: Path) -> dict[str, object]:
            conn = sqlite3.connect(path)
            try:
                conn.execute("insert into chunks(path) values (?)", ("seo/memory/articles/manual/example-com/useful.md",))
                conn.commit()
            finally:
                conn.close()
            return {
                "returncode": 0,
                "stdout": "Built index with 2 chunks",
                "stderr": "",
                "db_path": str(path),
                "skills_root": str(_skills_root),
            }

        manifest = MANUAL_URL_INGEST.perform_manual_ingest(
            "https://example.com/articles/travel-seo-field-notes",
            skills_root=self.skills_root,
            db_path=self.db_path,
            snapshot_dir=self.snapshot_dir,
            runs_dir=self.runs_dir,
            fetch_html_fn=fake_fetch_html,
            build_db_fn=fake_build_db,
        )

        self.assertEqual(manifest["counts_before"]["chunks"], 1)
        self.assertEqual(manifest["counts_after"]["chunks"], 2)
        self.assertEqual(manifest["chunk_delta"], 1)
        self.assertTrue(Path(manifest["note_path"]).exists())
        self.assertTrue(Path(manifest["snapshot_path"]).exists())
        self.assertTrue(Path(manifest["manifest_path"]).exists())

        note_text = Path(manifest["note_path"]).read_text(encoding="utf-8")
        self.assertIn("Manual URL Ingest - Dashboard", note_text)
        self.assertIn("Useful Travel SEO Field Notes", note_text)
        self.assertIn("## Capture Context", note_text)
        self.assertIn("## Extracted Body", note_text)

    def test_validate_url_rejects_non_http_input(self) -> None:
        with self.assertRaises(ValueError):
            MANUAL_URL_INGEST.validate_url("not-a-url")

    def test_manager_blocks_parallel_runs(self) -> None:
        started = threading.Event()
        release = threading.Event()

        def fake_performer(url: str, **_kwargs: object) -> dict[str, object]:
            self.assertEqual(url, "https://example.com/one")
            started.set()
            release.wait(timeout=2)
            return {
                "note_path": "/tmp/note.md",
                "manifest_path": "/tmp/manifest.json",
                "snapshot_path": "/tmp/snapshot.html",
                "counts_before": {"chunks": 10, "paths": 5},
                "counts_after": {"chunks": 11, "paths": 6},
                "chunk_delta": 1,
                "path_delta": 1,
                "article": {"title": "Example"},
                "source_host": "example.com",
            }

        manager = MANUAL_URL_INGEST.ManualUrlIngestManager(
            skills_root=self.skills_root,
            db_path=self.db_path,
            snapshot_dir=self.snapshot_dir,
            runs_dir=self.runs_dir,
            performer=fake_performer,
        )

        manager.start("https://example.com/one")
        self.assertTrue(started.wait(timeout=1))
        with self.assertRaises(RuntimeError):
            manager.start("https://example.com/two")

        release.set()
        deadline = time.time() + 2
        while time.time() < deadline:
            if not manager.snapshot()["active"]:
                break
            time.sleep(0.02)

        snapshot = manager.snapshot()
        self.assertFalse(snapshot["active"])
        self.assertEqual(snapshot["current"]["status"], "completed")


if __name__ == "__main__":
    unittest.main()
