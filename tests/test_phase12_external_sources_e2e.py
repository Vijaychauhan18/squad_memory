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


class Phase12ExternalSourcesE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase12_dir = self.root / "ingest" / "phase12"
        self.db_path = self.root / "squad_memory.db"
        self.config_path = self.root / "knowledge_sources_writer_marketing.json"
        self.feeds_dir = self.root / "feeds"
        self.feeds_dir.mkdir(parents=True, exist_ok=True)

        writer_root = self.skills_root / "writer"
        marketing_root = self.skills_root / "marketing"
        (writer_root / "memory").mkdir(parents=True, exist_ok=True)
        (marketing_root / "memory").mkdir(parents=True, exist_ok=True)

        (writer_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Writer Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Writer Operating Canon 2026: `memory/writer-operating-canon-2026.md`",
                    "",
                    "## Plankton Bundle",
                    "- `memory/writer-operating-canon-2026.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/writer-operating-canon-2026.md`",
                    "",
                    "## Current Bundle",
                    "- `memory/writer-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n"
        )
        (marketing_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Marketing Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Marketing Operating Canon 2026: `memory/marketing-operating-canon-2026.md`",
                    "",
                    "## Current Bundle",
                    "- `memory/marketing-operating-canon-2026.md`",
                    "",
                    "## Charles Bundle",
                    "- `memory/marketing-operating-canon-2026.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/marketing-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n"
        )

        (writer_root / "memory" / "writer-operating-canon-2026.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Writer Operating Canon 2026",
                    "topic: writer_core",
                    "canonical: true",
                    "confidence: high",
                    "---",
                    "",
                    "# Writer Operating Canon 2026",
                    "",
                    "## Core Concept",
                    "Base writing workflow.",
                    "",
                ]
            )
        )
        (marketing_root / "memory" / "marketing-operating-canon-2026.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Marketing Operating Canon 2026",
                    "topic: marketing_core",
                    "canonical: true",
                    "confidence: high",
                    "---",
                    "",
                    "# Marketing Operating Canon 2026",
                    "",
                    "## Core Concept",
                    "Base marketing workflow.",
                    "",
                ]
            )
        )

        writer_feed = self.feeds_dir / "copyblogger.xml"
        writer_feed.write_text(
            rss_feed(
                "Copyblogger",
                "How to tighten your opening paragraph",
                "https://example.com/copyblogger-opening",
                "Thu, 19 Mar 2026 10:00:00 +0000",
                "Hook and structure advice.",
            )
        )
        marketing_feed = self.feeds_dir / "buffer.xml"
        marketing_feed.write_text(
            rss_feed(
                "Buffer",
                "New social distribution checklist",
                "https://example.com/buffer-checklist",
                "Wed, 18 Mar 2026 09:00:00 +0000",
                "Distribution workflow update.",
            )
        )

        self.config_path.write_text(
            json.dumps(
                {
                    "name": "Phase 12 Fixture",
                    "sources": [
                        {
                            "domain": "writer",
                            "slug": "copyblogger",
                            "name": "Copyblogger",
                            "homepage": "https://copyblogger.com/",
                            "kind": "publication",
                            "strength": "hooks and copy structure",
                            "topic": "copywriting_systems",
                            "confidence": "high",
                            "roles": ["writer", "pinchy"],
                            "intent": ["research", "monitoring", "writing_examples"],
                            "tags": ["copyblogger", "fixture"],
                            "feed_urls": [writer_feed.as_uri()],
                        },
                        {
                            "domain": "marketing",
                            "slug": "buffer",
                            "name": "Buffer",
                            "homepage": "https://buffer.com/resources/",
                            "kind": "publication",
                            "strength": "distribution examples",
                            "topic": "social_distribution",
                            "confidence": "high",
                            "roles": ["marketing", "charles", "pinchy"],
                            "intent": ["research", "monitoring", "distribution_examples"],
                            "tags": ["buffer", "fixture"],
                            "feed_urls": [marketing_feed.as_uri()],
                        },
                        {
                            "domain": "marketing",
                            "slug": "blocked-source",
                            "name": "Blocked Source",
                            "homepage": "https://example.com/blocked",
                            "kind": "publication",
                            "strength": "should be skipped when disabled",
                            "topic": "campaign_operations",
                            "confidence": "medium",
                            "roles": ["marketing", "pinchy"],
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

    def test_phase12_ingests_and_fuses_external_sources(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase12_external_writer_marketing.py"),
                "--config",
                str(self.config_path),
                "--skills-root",
                str(self.skills_root),
                "--phase12-dir",
                str(self.phase12_dir),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(len(payload["domains"]), 2)
        self.assertTrue((self.skills_root / "writer" / "memory" / "live-source-copyblogger.md").exists())
        self.assertTrue((self.skills_root / "writer" / "memory" / "live-source-canon-copyblogger.md").exists())
        self.assertTrue((self.skills_root / "writer" / "memory" / "writer-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "marketing" / "memory" / "live-source-buffer.md").exists())
        self.assertTrue((self.skills_root / "marketing" / "memory" / "live-source-canon-buffer.md").exists())
        self.assertTrue((self.skills_root / "marketing" / "memory" / "marketing-external-source-canon-2026.md").exists())
        self.assertTrue((self.phase12_dir / "writer_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase12_dir / "marketing_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase12_dir / "writer_marketing_external_sources_report.md").exists())

        writer_router = (self.skills_root / "writer" / "MEMORY.md").read_text()
        marketing_router = (self.skills_root / "marketing" / "MEMORY.md").read_text()
        writer_operating = (self.skills_root / "writer" / "memory" / "writer-operating-canon-2026.md").read_text()
        marketing_operating = (self.skills_root / "marketing" / "memory" / "marketing-operating-canon-2026.md").read_text()
        report_text = (self.phase12_dir / "writer_marketing_external_sources_report.md").read_text()

        self.assertIn("writer-external-source-canon-2026.md", writer_router)
        self.assertIn("marketing-external-source-canon-2026.md", marketing_router)
        self.assertIn("Phase 12 External Source Fusion", writer_operating)
        self.assertIn("Phase 12 External Source Fusion", marketing_operating)
        self.assertIn("- Healthy sources: 1", report_text)
        self.assertIn("- Failed sources: 0", report_text)
        self.assertNotIn("Blocked Source", report_text)


if __name__ == "__main__":
    unittest.main()
