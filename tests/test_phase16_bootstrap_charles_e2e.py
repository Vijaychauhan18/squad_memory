from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")


class Phase16BootstrapCharlesE2ETest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.skills_root = self.root / "skills"
        self.phase16_dir = self.root / "ingest" / "phase16"
        self.db_path = self.root / "squad_memory.db"

        (self.skills_root / "charles").mkdir(parents=True, exist_ok=True)
        (self.skills_root / "SQUAD_MEMORY.md").write_text(
            "\n".join(
                [
                    "# Squad Memory Router",
                    "",
                    "## Role Bundles",
                    "",
                    "### Pinchy Bundle",
                    "- `writer/MEMORY.md`",
                    "",
                    "### Plankton Bundle",
                    "- `writer/MEMORY.md`",
                    "",
                    "### Charles Bundle",
                    "- `marketing/MEMORY.md`",
                    "",
                    "### Current Bundle",
                    "- `marketing/MEMORY.md`",
                    "",
                ]
            )
            + "\n"
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_phase16_bootstraps_charles_canon_and_router(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE / "phase16_bootstrap_charles.py"),
                "--skills-root",
                str(self.skills_root),
                "--phase16-dir",
                str(self.phase16_dir),
                "--db-path",
                str(self.db_path),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(len(payload["notes"]), 4)
        self.assertTrue((self.phase16_dir / "charles_evidence_ledger.json").exists())
        self.assertTrue((self.phase16_dir / "charles_bootstrap_report.md").exists())

        charles_canon = (self.skills_root / "charles" / "memory" / "charles-operating-canon-2026.md").read_text()
        self.assertIn("canonical: true", charles_canon)
        self.assertIn("Phase 16 Domain Fusion", charles_canon)
        self.assertIn("platform-native-posting-system.md", charles_canon)

        charles_router = (self.skills_root / "charles" / "MEMORY.md").read_text()
        self.assertIn("charles-operating-canon-2026.md", charles_router)
        self.assertIn("## Charles Bundle", charles_router)

        squad_router = (self.skills_root / "SQUAD_MEMORY.md").read_text()
        self.assertIn("### Charles Bundle", squad_router)
        self.assertIn("charles/MEMORY.md", squad_router)


if __name__ == "__main__":
    unittest.main()
