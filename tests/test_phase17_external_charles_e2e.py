from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


def rss_feed(title: str, item_title: str, item_link: str, published: str, description: str) -> str:
    return "\n".join(
        [
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
            "<rss version=\"2.0\">",
            "<channel>",
            f"<title>{title}</title>",
            f"<item><title>{item_title}</title><link>{item_link}</link><pubDate>{published}</pubDate><description>{description}</description></item>",
            "</channel>",
            "</rss>",
            "",
        ]
    )


class Phase17ExternalCharlesE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase17_dir = self.root / "ingest" / "phase17"
        self.db_path = self.root / "squad_memory.db"
        self.config_path = self.root / "knowledge_sources_charles.json"
        self.feeds_dir = self.root / "feeds"
        self.feeds_dir.mkdir(parents=True, exist_ok=True)

        charles_root = self.skills_root / "charles"
        (charles_root / "memory").mkdir(parents=True, exist_ok=True)
        (charles_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Charles Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Charles Operating Canon 2026: `memory/charles-operating-canon-2026.md`",
                    "",
                    "## Charles Bundle",
                    "- `memory/charles-operating-canon-2026.md`",
                    "",
                    "## Current Bundle",
                    "- `memory/charles-operating-canon-2026.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/charles-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n"
        )
        (charles_root / "memory" / "charles-operating-canon-2026.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Charles Operating Canon 2026",
                    "topic: charles_core",
                    "canonical: true",
                    "confidence: high",
                    "---",
                    "",
                    "# Charles Operating Canon 2026",
                    "",
                    "## Core Concept",
                    "Base Charles workflow.",
                    "",
                ]
            )
        )

        buffer_feed = self.feeds_dir / "buffer.xml"
        buffer_feed.write_text(
            rss_feed(
                "Buffer",
                "Best creator posting pattern this week",
                "https://example.com/buffer-creator",
                "Thu, 19 Mar 2026 10:00:00 +0000",
                "Creator workflow update.",
            )
        )
        hootsuite_feed = self.feeds_dir / "hootsuite.xml"
        hootsuite_feed.write_text(
            rss_feed(
                "Hootsuite",
                "What changed on LinkedIn this week",
                "https://example.com/hootsuite-linkedin",
                "Wed, 18 Mar 2026 09:00:00 +0000",
                "Platform change summary.",
            )
        )

        self.config_path.write_text(
            json.dumps(
                {
                    "name": "Phase 17 Fixture",
                    "sources": [
                        {
                            "slug": "buffer",
                            "name": "Buffer",
                            "homepage": "https://buffer.com/resources/",
                            "kind": "publication",
                            "strength": "creator workflows and social distribution",
                            "topic": "social_distribution",
                            "confidence": "high",
                            "roles": ["charles", "current", "pinchy"],
                            "intent": ["research", "monitoring", "creator_examples"],
                            "tags": ["buffer", "fixture"],
                            "feed_urls": [buffer_feed.as_uri()],
                        },
                        {
                            "slug": "hootsuite",
                            "name": "Hootsuite",
                            "homepage": "https://blog.hootsuite.com/",
                            "kind": "publication",
                            "strength": "platform changes and channel tactics",
                            "topic": "platform_changes",
                            "confidence": "high",
                            "roles": ["charles", "current", "pinchy"],
                            "intent": ["research", "monitoring", "platform_changes"],
                            "tags": ["hootsuite", "fixture"],
                            "feed_urls": [hootsuite_feed.as_uri()],
                        },
                        {
                            "slug": "blocked-source",
                            "name": "Blocked Source",
                            "homepage": "https://example.com/blocked",
                            "kind": "publication",
                            "strength": "should be skipped when disabled",
                            "topic": "platform_changes",
                            "confidence": "medium",
                            "roles": ["charles", "pinchy"],
                            "intent": ["research", "monitoring"],
                            "tags": ["blocked", "fixture"],
                            "enabled": False,
                            "feed_urls": ["https://example.com/blocked/feed.xml"],
                        },
                    ],
                },
                indent=2,
            )
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase17_ingests_and_fuses_external_sources(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase17_external_charles.py"),
                "--config",
                str(self.config_path),
                "--skills-root",
                str(self.skills_root),
                "--phase17-dir",
                str(self.phase17_dir),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["source_count"], 2)
        self.assertTrue((self.skills_root / "charles" / "memory" / "live-source-buffer.md").exists())
        self.assertTrue((self.skills_root / "charles" / "memory" / "live-source-canon-buffer.md").exists())
        self.assertTrue((self.skills_root / "charles" / "memory" / "charles-external-source-canon-2026.md").exists())
        self.assertTrue((self.phase17_dir / "charles_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase17_dir / "charles_external_sources_report.md").exists())

        charles_router = (self.skills_root / "charles" / "MEMORY.md").read_text()
        charles_operating = (self.skills_root / "charles" / "memory" / "charles-operating-canon-2026.md").read_text()
        report_text = (self.phase17_dir / "charles_external_sources_report.md").read_text()

        self.assertIn("charles-external-source-canon-2026.md", charles_router)
        self.assertIn("Phase 17 External Source Fusion", charles_operating)
        self.assertIn("- Healthy sources: 2", report_text)
        self.assertIn("- Failed sources: 0", report_text)
        self.assertNotIn("Blocked Source", report_text)


if __name__ == "__main__":
    unittest.main()
