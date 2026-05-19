#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
ARCHIVE_DIR="/Users/vijaychauhan/.codex/skills/seo/memory/archive"
RUNS_DIR="$BASE/ingest/archive/runs"
SNAPSHOT_DIR="$BASE/ingest/archive/raw"
STATE_PATH="$BASE/ingest/archive/state.json"

mkdir -p "$LOG_DIR" "$ARCHIVE_DIR" "$RUNS_DIR" "$SNAPSHOT_DIR"

python3 "$BASE/knowledge_ingest.py" run \
  --config "$BASE/knowledge_sources.json" \
  --output-dir "$ARCHIVE_DIR" \
  --summary-path "$ARCHIVE_DIR/live-archive-monitor.md" \
  --snapshot-dir "$SNAPSHOT_DIR" \
  --runs-dir "$RUNS_DIR" \
  --state-path "$STATE_PATH" \
  --top 12 \
  --source hobo \
  --source aleyda \
  --source search-engine-land \
  --source search-engine-journal \
  --source seroundtable \
  --build-db >> "$LOG_DIR/archive_backfill.log" 2>&1
