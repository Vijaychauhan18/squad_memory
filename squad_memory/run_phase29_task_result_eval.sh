#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/phase29_task_result_eval.py" \
  --phase29-dir "$BASE/ingest/phase29" \
  --db-path "$BASE/squad_memory.db" \
  --packs-file "$BASE/task_packs.json" >> "$LOG_DIR/phase29_task_result_eval.log" 2>&1
