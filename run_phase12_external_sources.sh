#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase12_external_writer_marketing.py" \
  --config "$BASE/knowledge_sources_writer_marketing.json" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --phase12-dir "$BASE/ingest/phase12" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase12_external_sources.log" 2>&1
