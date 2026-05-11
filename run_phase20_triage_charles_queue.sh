#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase20_triage_charles_queue.py" \
  --phase19-manifest "$BASE/ingest/phase19/latest.json" \
  --decisions-path "$BASE/ingest/phase19/decisions.json" \
  --phase20-dir "$BASE/ingest/phase20" >> "$LOG_DIR/phase20_triage_charles_queue.log" 2>&1
