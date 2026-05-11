from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


BASE = Path("/Users/vijaychauhan/squad_memory")
MODULE_SPEC = importlib.util.spec_from_file_location("squad_memory", BASE / "squad_memory.py")
SQUAD_MEMORY = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC and MODULE_SPEC.loader
sys.modules[MODULE_SPEC.name] = SQUAD_MEMORY
MODULE_SPEC.loader.exec_module(SQUAD_MEMORY)


class SquadMemoryChunkingE2ETest(unittest.TestCase):
    def test_chunk_section_splits_long_paragraphs_on_sentence_boundaries(self) -> None:
        long_paragraph = " ".join(
            f"Sentence {index} explains how durable entity memory improves retrieval quality across SEO research workflows."
            for index in range(1, 45)
        )

        chunks = SQUAD_MEMORY.chunk_section(
            path=BASE / "tmp.md",
            rel_path="seo/memory/archive/example.md",
            skill="seo",
            file_type="memory_note",
            heading="Extracted Body",
            text=long_paragraph,
            tags=["seo_memory"],
            roles=["researcher"],
            topics=["archive_backfill"],
            intents=["research"],
            use_for=["historical_patterns"],
            avoid_for=[],
            confidence="high",
            is_canonical=False,
            canonical_group="",
            source="example",
            published_on="2026-03-22",
            freshness=0.03,
        )

        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk.text) <= 980 for chunk in chunks))
        self.assertTrue(all(chunk.text.strip().endswith(".") for chunk in chunks))


if __name__ == "__main__":
    unittest.main()
