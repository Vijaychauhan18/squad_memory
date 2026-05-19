#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase26_promote_dev_qa.py" \
  --skills-root "/Users/vijaychauhan/.codex/skills" \
  --phase25-manifest "$BASE/ingest/phase25/latest.json" \
  --phase26-dir "$BASE/ingest/phase26" >> "$LOG_DIR/phase26_promote_dev_qa.log" 2>&1
