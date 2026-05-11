#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase16_bootstrap_charles.py" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --phase16-dir "$BASE/ingest/phase16" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase16_bootstrap_charles.log" 2>&1
