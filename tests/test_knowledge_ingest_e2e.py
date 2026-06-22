from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
SCRIPT = BASE / "knowledge_ingest.py"
FIXTURES = BASE / "tests" / "fixtures" / "feeds"


class KnowledgeIngestE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.output_dir = self.skills_root / "seo" / "memory"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.skills_root / "seo" / "SKILL.md").write_text("# SEO\n")
        (self.skills_root / "seo" / "MEMORY.md").write_text("# SEO Memory\n")
        self.snapshot_dir = self.root / "ingest" / "raw"
        self.runs_dir = self.root / "ingest" / "runs"
        self.state_path = self.root / "ingest" / "state.json"
        self.summary_path = self.output_dir / "live-knowledge-monitor.md"
        self.db_path = self.root / "squad_memory.db"
        self.config_path = self.root / "knowledge_sources.json"
        self.config_path.write_text(json.dumps(self._fixture_config(), indent=2))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _fixture_config(self) -> dict:
        return {
            "name": "Fixture Knowledge Source Monitor",
            "sources": [
                {
                    "slug": "ahrefs",
                    "name": "Ahrefs Blog",
                    "homepage": "https://ahrefs.com/blog/",
                    "kind": "publication",
                    "strength": "data studies and AI visibility",
                    "topic": "seo_research",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring"],
                    "tags": ["ahrefs", "fixture"],
                    "feed_urls": [(FIXTURES / "ahrefs.xml").as_uri()],
                },
                {
                    "slug": "hobo",
                    "name": "Hobo Web",
                    "homepage": "https://www.hobo-web.co.uk/",
                    "kind": "publication",
                    "strength": "quality systems",
                    "topic": "quality_systems",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring"],
                    "tags": ["hobo", "fixture"],
                    "feed_urls": [(FIXTURES / "hobo.xml").as_uri()],
                },
                {
                    "slug": "dejan",
                    "name": "DEJAN / Dan Petrovic",
                    "homepage": "https://dejan.ai/blog/",
                    "kind": "practitioner",
                    "strength": "reverse engineering",
                    "topic": "ai_reverse_engineering",
                    "confidence": "high",
                    "roles": ["researcher", "seo", "pinchy"],
                    "intent": ["research", "monitoring"],
                    "tags": ["dejan", "fixture"],
                    "feed_urls": [(FIXTURES / "dejan.xml").as_uri()],
                },
            ],
        }

    def _run(self, *extra: str) -> subprocess.CompletedProcess[str]:
        cmd = [
            sys.executable,
            str(SCRIPT),
            "run",
            "--config",
            str(self.config_path),
            "--output-dir",
            str(self.output_dir),
            "--summary-path",
            str(self.summary_path),
            "--snapshot-dir",
            str(self.snapshot_dir),
            "--runs-dir",
            str(self.runs_dir),
            "--state-path",
            str(self.state_path),
            "--skills-root",
            str(self.skills_root),
            "--db-path",
            str(self.db_path),
            "--json",
        ]
        cmd.extend(extra)
        return subprocess.run(cmd, check=True, capture_output=True, text=True)

    def test_run_creates_notes_snapshots_manifests_and_db(self) -> None:
        first = self._run("--top", "2", "--build-db")
        payload = json.loads(first.stdout)

        self.assertEqual(len(payload["results"]), 3)
        self.assertTrue(self.summary_path.exists())
        self.assertTrue(self.state_path.exists())
        self.assertTrue(Path(payload["manifest_path"]).exists())
        self.assertTrue((self.runs_dir / "latest.json").exists())
        self.assertTrue(self.db_path.exists())

        for result in payload["results"]:
            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["new_item_count"], 2)
            self.assertTrue(Path(result["note_path"]).exists())
            self.assertTrue(Path(result["snapshot_path"]).exists())

        state = json.loads(self.state_path.read_text())
        self.assertEqual(sorted(state["sources"].keys()), ["ahrefs", "dejan", "hobo"])

        con = sqlite3.connect(str(self.db_path))
        try:
            live_note_chunks = con.execute(
                "SELECT COUNT(*) FROM chunks WHERE path LIKE 'seo/memory/live-source-%' OR path = 'seo/memory/live-knowledge-monitor.md'"
            ).fetchone()[0]
        finally:
            con.close()
        self.assertGreaterEqual(live_note_chunks, 4)

        second = self._run("--top", "2")
        second_payload = json.loads(second.stdout)
        for result in second_payload["results"]:
            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["new_item_count"], 0)

        report = subprocess.run(
            [sys.executable, str(SCRIPT), "report", "--state-path", str(self.state_path), "--json"],
            check=True,
            capture_output=True,
            text=True,
        )
        report_payload = json.loads(report.stdout)
        self.assertEqual(report_payload["last_run_id"], second_payload["run_id"])
        self.assertEqual(report_payload["sources"]["ahrefs"]["last_status"], "ok")

    def test_run_discovers_feed_from_homepage_and_parses_malformed_xml(self) -> None:
        feed_dir = self.root / "extra_feeds"
        feed_dir.mkdir(parents=True, exist_ok=True)
        homepage = feed_dir / "homepage.html"
        discovered_feed = feed_dir / "discovered.xml"
        missing_feed = feed_dir / "missing.xml"

        homepage.write_text(
            "\n".join(
                [
                    "<html>",
                    "<head>",
                    f'<link rel="alternate" type="application/rss+xml" href="{discovered_feed.name}">',
                    "</head>",
                    "<body>Feed home</body>",
                    "</html>",
                    "",
                ]
            )
        )
        discovered_feed.write_text(
            "\n".join(
                [
                    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
                    "<rss version=\"2.0\">",
                    "<channel>",
                    "<title>Discovered Feed</title>",
                    "<item>",
                    "<title>Fresh copy tip</title>",
                    "<link>https://example.com/fresh-copy-tip</link>",
                    "<pubDate>Thu, 19 Mar 2026 10:00:00 +0000</pubDate>",
                    "<description>Use voice & structure to keep readers moving.</description>",
                    "</item>",
                    "</channel>",
                    "</rss>",
                    "",
                ]
            )
        )

        self.config_path.write_text(
            json.dumps(
                {
                    "name": "Discovery Fixture",
                    "sources": [
                        {
                            "slug": "writer-source",
                            "name": "Writer Source",
                            "homepage": homepage.as_uri(),
                            "kind": "publication",
                            "strength": "writing examples",
                            "topic": "editorial_strategy",
                            "confidence": "high",
                            "roles": ["writer", "pinchy"],
                            "intent": ["research", "monitoring"],
                            "tags": ["writer", "fixture"],
                            "feed_urls": [missing_feed.as_uri()],
                        }
                    ],
                },
                indent=2,
            )
        )

        completed = self._run("--top", "1")
        payload = json.loads(completed.stdout)
        self.assertEqual(len(payload["results"]), 1)

        result = payload["results"][0]
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["new_item_count"], 1)
        self.assertEqual(result["fetched_from"], discovered_feed.as_uri())
        self.assertIn(discovered_feed.as_uri(), result["discovered_urls"])
        self.assertTrue(Path(result["note_path"]).exists())
        self.assertTrue(Path(result["snapshot_path"]).exists())

        note_text = Path(result["note_path"]).read_text()
        self.assertIn("Fresh copy tip", note_text)

    def test_run_falls_back_to_html_listing_when_feed_is_blocked(self) -> None:
        listing_dir = self.root / "listing"
        listing_dir.mkdir(parents=True, exist_ok=True)
        listing_page = listing_dir / "blog.html"
        blocked_feed = listing_dir / "blocked.xml"

        listing_page.write_text(
            "\n".join(
                [
                    "<html>",
                    "<head><title>SparkToro Blog</title></head>",
                    "<body>",
                    "<h1>SparkToro Blog</h1>",
                    "<article>",
                    "<div>Marketing March 16, 2026</div>",
                    '<h2><a href="https://example.com/sparktoro-linkedin">Why LinkedIn Might Have Two Algorithms</a></h2>',
                    "<p>Fresh platform analysis and audience implications.</p>",
                    "</article>",
                    "<article>",
                    "<time datetime=\"2026-03-11\">March 11, 2026</time>",
                    '<h2><a href="https://example.com/sparktoro-ai">New AI Prompt Topic Research</a></h2>',
                    "<p>Audience research and AI usage patterns.</p>",
                    "</article>",
                    "</body>",
                    "</html>",
                    "",
                ]
            )
        )

        self.config_path.write_text(
            json.dumps(
                {
                    "name": "Listing Fallback Fixture",
                    "sources": [
                        {
                            "slug": "sparktoro",
                            "name": "SparkToro Blog",
                            "homepage": listing_page.as_uri(),
                            "kind": "publication",
                            "strength": "audience research",
                            "topic": "audience_research",
                            "confidence": "high",
                            "roles": ["marketing", "pinchy"],
                            "intent": ["research", "monitoring"],
                            "tags": ["sparktoro", "fixture"],
                            "listing_fallback": True,
                            "listing_urls": [listing_page.as_uri()],
                            "feed_urls": [blocked_feed.as_uri()],
                        }
                    ],
                },
                indent=2,
            )
        )

        completed = self._run("--top", "2")
        payload = json.loads(completed.stdout)
        self.assertEqual(len(payload["results"]), 1)

        result = payload["results"][0]
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["fetched_from"], listing_page.as_uri())
        self.assertEqual(result["new_item_count"], 2)
        self.assertEqual(result["item_count"], 2)

        note_text = Path(result["note_path"]).read_text()
        self.assertIn("Why LinkedIn Might Have Two Algorithms", note_text)
        self.assertIn("New AI Prompt Topic Research", note_text)


if __name__ == "__main__":
    unittest.main()
