#!/usr/bin/env python3
"""Reassemble split .db files from chunks.

Works on Windows, Mac, and Linux — no dependencies beyond Python 3.

Usage:
    python3 reassemble_dbs.py

Output:
    ../squad_memory.db
    ../seo_elite_memory.db
"""

import os
from pathlib import Path

HERE = Path(__file__).parent
OUT_DIR = HERE.parent


def reassemble(prefix: str, out_name: str) -> None:
    chunks = sorted(HERE.glob(f"{prefix}_*.bin"))
    if not chunks:
        print(f"[!] No chunks found for {prefix} — skipping")
        return

    out_path = OUT_DIR / out_name
    print(f"Reassembling {out_name} from {len(chunks)} parts...")
    with open(out_path, "wb") as out:
        for chunk in chunks:
            with open(chunk, "rb") as f:
                out.write(f.read())
            print(f"  + {chunk.name}")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print(f"  => {out_path} ({size_mb:.0f} MB)\n")


if __name__ == "__main__":
    reassemble("squad_memory", "squad_memory.db")
    reassemble("seo_elite", "seo_elite_memory.db")
    print("Done. Both databases are ready.")
    print("Run setup.sh (Mac/Linux) or setup.ps1 (Windows) to complete install.")
