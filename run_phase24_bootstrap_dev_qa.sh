#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase24_bootstrap_dev_qa.py" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --phase24-dir "$BASE/ingest/phase24" \
  --db-path "$BASE/squad_memory.db" \
  --build-db >> "$LOG_DIR/phase24_bootstrap_dev_qa.log" 2>&1
