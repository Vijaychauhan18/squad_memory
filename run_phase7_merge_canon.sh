#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase7_merge_canon.py" \
  --output-dir "/Users/vijaychauhan/.codex/skills/seo/memory" \
  --phase6-decisions "$BASE/ingest/phase6/decisions.json" \
  --phase7-dir "$BASE/ingest/phase7" >> "$LOG_DIR/phase7_merge_canon.log" 2>&1
