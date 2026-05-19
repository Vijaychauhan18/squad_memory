#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"

mkdir -p "$LOG_DIR"

python3 "$BASE/refresh_openclaw_memory.py" >> "$LOG_DIR/openclaw_sync.log" 2>&1
