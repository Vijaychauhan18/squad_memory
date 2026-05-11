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


class Phase25ExternalDevQaE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase25_dir = self.root / "ingest" / "phase25"
        self.db_path = self.root / "squad_memory.db"
        self.config_path = self.root / "knowledge_sources_dev_qa.json"
        self.feeds_dir = self.root / "feeds"
        self.feeds_dir.mkdir(parents=True, exist_ok=True)

        developer_root = self.skills_root / "developer"
        qa_root = self.skills_root / "qa"
        (developer_root / "memory").mkdir(parents=True, exist_ok=True)
        (qa_root / "memory").mkdir(parents=True, exist_ok=True)

        (developer_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# Developer Memory Router",
                    "",
                    "## Canonical Notes",
                    "- Developer Operating Canon 2026: `memory/developer-operating-canon-2026.md`",
                    "",
                    "## Chitin Bundle",
                    "- `memory/developer-operating-canon-2026.md`",
                    "",
                    "## Barnacle Bundle",
                    "- `memory/developer-operating-canon-2026.md`",
                    "",
                    "## Reef Bundle",
                    "- `memory/developer-operating-canon-2026.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/developer-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (qa_root / "MEMORY.md").write_text(
            "\n".join(
                [
                    "# QA Memory Router",
                    "",
                    "## Canonical Notes",
                    "- QA Operating Canon 2026: `memory/qa-operating-canon-2026.md`",
                    "",
                    "## Reef Bundle",
                    "- `memory/qa-operating-canon-2026.md`",
                    "",
                    "## Chitin Bundle",
                    "- `memory/qa-operating-canon-2026.md`",
                    "",
                    "## Barnacle Bundle",
                    "- `memory/qa-operating-canon-2026.md`",
                    "",
                    "## Pinchy Bundle",
                    "- `memory/qa-operating-canon-2026.md`",
                    "",
                    "## Tide Bundle",
                    "- `memory/qa-operating-canon-2026.md`",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (developer_root / "memory" / "developer-operating-canon-2026.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: Developer Operating Canon 2026",
                    "topic: developer_core",
                    "canonical: true",
                    "confidence: high",
                    "---",
                    "",
                    "# Developer Operating Canon 2026",
                    "",
                    "## Core Concept",
                    "Base Chitin workflow.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (qa_root / "memory" / "qa-operating-canon-2026.md").write_text(
            "\n".join(
                [
                    "---",
                    "title: QA Operating Canon 2026",
                    "topic: qa_core",
                    "canonical: true",
                    "confidence: high",
                    "---",
                    "",
                    "# QA Operating Canon 2026",
                    "",
                    "## Core Concept",
                    "Base Reef workflow.",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        developer_feed = self.feeds_dir / "martin-fowler.xml"
        developer_feed.write_text(
            rss_feed(
                "Martin Fowler",
                "How to keep refactors small",
                "https://example.com/mf-refactor",
                "Thu, 19 Mar 2026 10:00:00 +0000",
                "Engineering decision and refactoring guidance.",
            ),
            encoding="utf-8",
        )
        qa_feed = self.feeds_dir / "playwright.xml"
        qa_feed.write_text(
            rss_feed(
                "Playwright Releases",
                "Playwright 1.55 release notes",
                "https://example.com/playwright-release",
                "Wed, 18 Mar 2026 09:00:00 +0000",
                "Testing framework release summary.",
            ),
            encoding="utf-8",
        )

        self.config_path.write_text(
            json.dumps(
                {
                    "name": "Phase 25 Fixture",
                    "sources": [
                        {
                            "domain": "developer",
                            "slug": "martin-fowler",
                            "name": "Martin Fowler",
                            "homepage": "https://martinfowler.com/",
                            "kind": "practitioner",
                            "strength": "software design and refactoring guidance",
                            "topic": "engineering_patterns",
                            "confidence": "high",
                            "roles": ["developer", "reviewer", "pinchy"],
                            "intent": ["research", "monitoring", "engineering_examples"],
                            "tags": ["martin-fowler", "fixture"],
                            "feed_urls": [developer_feed.as_uri()],
                        },
                        {
                            "domain": "qa",
                            "slug": "playwright-releases",
                            "name": "Playwright Releases",
                            "homepage": "https://github.com/microsoft/playwright/releases",
                            "kind": "release_notes",
                            "strength": "testing framework release updates",
                            "topic": "test_tooling",
                            "confidence": "high",
                            "roles": ["qa", "developer", "pinchy"],
                            "intent": ["research", "monitoring", "tooling_changes"],
                            "tags": ["playwright", "fixture"],
                            "feed_urls": [qa_feed.as_uri()],
                        },
                        {
                            "domain": "qa",
                            "slug": "disabled-source",
                            "name": "Disabled Source",
                            "homepage": "https://example.com/disabled",
                            "kind": "publication",
                            "strength": "should be skipped when disabled",
                            "topic": "testing_patterns",
                            "confidence": "medium",
                            "roles": ["qa", "pinchy"],
                            "intent": ["research", "monitoring"],
                            "tags": ["disabled", "fixture"],
                            "enabled": False,
                            "feed_urls": ["https://example.com/disabled/feed.xml"],
                        },
                    ],
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase25_ingests_and_fuses_dev_qa_external_sources(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase25_external_dev_qa.py"),
                "--config",
                str(self.config_path),
                "--skills-root",
                str(self.skills_root),
                "--phase25-dir",
                str(self.phase25_dir),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        domains = {item["domain"]: item for item in payload["domains"]}

        self.assertEqual(domains["developer"]["source_count"], 1)
        self.assertEqual(domains["qa"]["source_count"], 1)
        self.assertTrue((self.skills_root / "developer" / "memory" / "live-source-martin-fowler.md").exists())
        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-external-source-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "live-source-playwright-releases.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-external-source-canon-2026.md").exists())
        self.assertTrue((self.phase25_dir / "developer_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase25_dir / "qa_external_evidence_ledger.json").exists())
        self.assertTrue((self.phase25_dir / "developer_qa_external_sources_report.md").exists())

        developer_router = (self.skills_root / "developer" / "MEMORY.md").read_text(encoding="utf-8")
        qa_router = (self.skills_root / "qa" / "MEMORY.md").read_text(encoding="utf-8")
        developer_operating = (self.skills_root / "developer" / "memory" / "developer-operating-canon-2026.md").read_text(
            encoding="utf-8"
        )
        qa_operating = (self.skills_root / "qa" / "memory" / "qa-operating-canon-2026.md").read_text(encoding="utf-8")
        report_text = (self.phase25_dir / "developer_qa_external_sources_report.md").read_text(encoding="utf-8")

        self.assertIn("developer-external-source-canon-2026.md", developer_router)
        self.assertIn("qa-external-source-canon-2026.md", qa_router)
        self.assertIn("Phase 25 External Source Fusion", developer_operating)
        self.assertIn("Phase 25 External Source Fusion", qa_operating)
        self.assertIn("## Developer", report_text)
        self.assertIn("## QA", report_text)
        self.assertNotIn("Disabled Source", report_text)


if __name__ == "__main__":
    unittest.main()
