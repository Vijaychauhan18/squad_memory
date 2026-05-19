#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
MEMORY_DIR="/Users/vijaychauhan/.codex/skills/seo/memory"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase3_cluster_refresh.py" \
  --output-dir "$MEMORY_DIR" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --db-path "$BASE/squad_memory.db" \
  --fixtures "$BASE/evals/fixtures.json" \
  --phase2-manifest "$BASE/ingest/phase2/latest.json" \
  --phase3-dir "$BASE/ingest/phase3" >> "$LOG_DIR/phase3_cluster_refresh.log" 2>&1
