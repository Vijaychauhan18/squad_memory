#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase28_triage_dev_qa_queue.py" \
  --phase27-manifest "$BASE/ingest/phase27/latest.json" \
  --decisions-path "$BASE/ingest/phase27/decisions.json" \
  --phase28-dir "$BASE/ingest/phase28" >> "$LOG_DIR/phase28_triage_dev_qa_queue.log" 2>&1
