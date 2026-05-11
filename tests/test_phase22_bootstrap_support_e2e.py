from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase22BootstrapSupportE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase22_dir = self.root / "ingest" / "phase22"
        support_root = self.skills_root / "support-anemone"
        support_root.mkdir(parents=True, exist_ok=True)
        (support_root / "MEMORY.md").write_text(
            "# MEMORY.md — Customer Support\n\n## FAQ\n| Question | Answer | Last Updated |\n|----------|--------|-------------|\n| — | — | — |\n",
            encoding="utf-8",
        )
        (self.skills_root / "SQUAD_MEMORY.md").write_text(
            "\n".join(
                [
                    "# Squad Memory Router",
                    "",
                    "### Pinchy Bundle",
                    "- skill `orchestrator-pinchy`",
                    "",
                    "### Anemone Bundle",
                    "- skill `support-anemone`",
                    "",
                    "### Urchin Bundle",
                    "- skill `operations`",
                    "",
                    "### Chitin Bundle",
                    "- skill `developer`",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase22_bootstraps_support_memory(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase22_bootstrap_support.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase22-dir",
                str(self.phase22_dir),
                "--db-path",
                str(self.root / "memory.db"),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "anemone-operating-canon-2026.md").exists())
        self.assertTrue((self.skills_root / "support-anemone" / "memory" / "fast-first-response-and-severity-triage.md").exists())
        self.assertTrue((self.phase22_dir / "support_evidence_ledger.json").exists())
        self.assertTrue((self.phase22_dir / "support_bootstrap_report.md").exists())
        router_text = (self.skills_root / "support-anemone" / "MEMORY.md").read_text(encoding="utf-8")
        squad_text = (self.skills_root / "SQUAD_MEMORY.md").read_text(encoding="utf-8")
        self.assertIn("Anemone Operating Canon 2026", router_text)
        self.assertIn("support-anemone/MEMORY.md", squad_text)
        self.assertEqual(payload["squad_router_changed"], True)


if __name__ == "__main__":
    unittest.main()
