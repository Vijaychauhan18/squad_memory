from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase24BootstrapDevQaE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase24_dir = self.root / "ingest" / "phase24"

        (self.skills_root / "developer").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "qa").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "SQUAD_MEMORY.md").write_text(
            "\n".join(
                [
                    "# Squad Memory Router",
                    "",
                    "### Pinchy Bundle",
                    "- skill `orchestrator-pinchy`",
                    "",
                    "### Chitin Bundle",
                    "- skill `developer`",
                    "",
                    "### Reef Bundle",
                    "- skill `qa`",
                    "",
                    "### Barnacle Bundle",
                    "- skill `reviewer`",
                    "",
                    "### Tide Bundle",
                    "- skill `devops`",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase24_bootstraps_developer_and_qa_memory(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase24_bootstrap_dev_qa.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase24-dir",
                str(self.phase24_dir),
                "--db-path",
                str(self.root / "memory.db"),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertTrue((self.skills_root / "developer" / "memory" / "developer-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "developer" / "memory" / "implementation-and-tdd-loop.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "qa-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "qa" / "memory" / "regression-gate-and-release-verdicts.md").exists())
        self.assertTrue((self.phase24_dir / "developer_evidence_ledger.json").exists())
        self.assertTrue((self.phase24_dir / "qa_evidence_ledger.json").exists())
        self.assertTrue((self.phase24_dir / "developer_qa_bootstrap_report.md").exists())

        developer_router = (self.skills_root / "developer" / "MEMORY.md").read_text(encoding="utf-8")
        qa_router = (self.skills_root / "qa" / "MEMORY.md").read_text(encoding="utf-8")
        squad_router = (self.skills_root / "SQUAD_MEMORY.md").read_text(encoding="utf-8")

        self.assertIn("Developer Operating Canon 2026", developer_router)
        self.assertIn("QA Operating Canon 2026", qa_router)
        self.assertIn("developer/MEMORY.md", squad_router)
        self.assertIn("qa/MEMORY.md", squad_router)
        self.assertEqual(payload["developer_note_count"], 4)
        self.assertEqual(payload["qa_note_count"], 4)


if __name__ == "__main__":
    unittest.main()
