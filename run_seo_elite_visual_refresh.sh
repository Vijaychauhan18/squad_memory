#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
DB_PATH="$BASE/seo_elite_memory.db"
STATUS_JSON="/Users/vijaychauhan/.codex/elite-skills/seo-elite/status/latest-status.json"
STATE_DIR="$BASE/ingest/seo_elite/visual_refresh"
STAMP_PATH="$STATE_DIR/last_graph_stamp.txt"
GRAPH_LOG="$LOG_DIR/seo_elite_visual_refresh.log"

mkdir -p "$LOG_DIR" "$STATE_DIR"

python3 "$BASE/report_seo_elite_status.py" >> "$LOG_DIR/seo_elite_status_ping.log" 2>&1

db_stamp=$(stat -f %m "$DB_PATH" 2>/dev/null || echo 0)
status_stamp=$(stat -f %m "$STATUS_JSON" 2>/dev/null || echo 0)
combined_stamp="${db_stamp}:${status_stamp}"

previous_stamp=""
if [[ -f "$STAMP_PATH" ]]; then
  previous_stamp=$(cat "$STAMP_PATH")
fi

if [[ "$combined_stamp" == "$previous_stamp" ]]; then
  exit 0
fi

if python3 "$BASE/phase31_memory_graph.py" build --db-path "$DB_PATH" >> "$GRAPH_LOG" 2>&1; then
  printf '%s\n' "$combined_stamp" > "$STAMP_PATH"
else
  printf '[%s] WARN: phase31 graph refresh failed for stamp %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" "$combined_stamp" >> "$GRAPH_LOG"
fi
