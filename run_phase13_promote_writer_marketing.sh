#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase13_promote_writer_marketing.py" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --phase12-manifest "$BASE/ingest/phase12/latest.json" \
  --phase13-dir "$BASE/ingest/phase13" \
  --state-path "$BASE/ingest/phase13/state.json" >> "$LOG_DIR/phase13_promote_writer_marketing.log" 2>&1
