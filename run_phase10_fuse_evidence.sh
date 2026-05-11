#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase10_fuse_evidence.py" \
  --output-dir "/Users/vijaychauhan/.codex/skills/seo/memory" \
  --phase7-registry "$BASE/ingest/phase7/canonical_registry.json" \
  --phase10-dir "$BASE/ingest/phase10" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase10_fuse_evidence.log" 2>&1
