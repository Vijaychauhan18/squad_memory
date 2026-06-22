#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase23_external_support.py" \
  --config "$BASE/knowledge_sources_support.json" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --phase23-dir "$BASE/ingest/phase23" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase23_external_support.log" 2>&1
