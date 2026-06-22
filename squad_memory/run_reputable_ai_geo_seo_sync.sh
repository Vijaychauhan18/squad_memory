#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"
MEMORY_DIR="$HOME/.codex/skills/seo/memory"
RUNS_DIR="$BASE/ingest/reputable/runs"
SNAPSHOT_DIR="$BASE/ingest/reputable/raw"
STATE_PATH="$BASE/ingest/reputable/state.json"

mkdir -p "$LOG_DIR" "$RUNS_DIR" "$SNAPSHOT_DIR"

python3 "$BASE/knowledge_ingest.py" run \
  --config "$BASE/knowledge_sources.json" \
  --output-dir "$MEMORY_DIR" \
  --summary-path "$MEMORY_DIR/live-knowledge-monitor.md" \
  --snapshot-dir "$SNAPSHOT_DIR" \
  --runs-dir "$RUNS_DIR" \
  --state-path "$STATE_PATH" \
  --top 8 \
  --source google-search-central \
  --source ahrefs \
  --source dejan \
  --source gsqi \
  --source marie \
  --source lily \
  --source mobilemoxie \
  --source brodie \
  --source ipullrank \
  --source jono \
  --build-db >> "$LOG_DIR/reputable_ai_geo_seo_sync.log" 2>&1
