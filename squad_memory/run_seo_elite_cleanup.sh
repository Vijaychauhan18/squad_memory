#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"
SKILLS_ROOT="$HOME/.codex/elite-skills"
MEMORY_DIR="$SKILLS_ROOT/seo-elite/memory"
RUNS_DIR="$BASE/ingest/seo_elite/live/runs"
STATE_PATH="$BASE/ingest/seo_elite/live/state.json"
DB_PATH="$BASE/seo_elite_memory.db"

mkdir -p "$LOG_DIR"
zsh "$BASE/sync_seo_elite_seed.sh"

python3 "$BASE/prune_seo_elite_live_sources.py" \
  --output-dir "$MEMORY_DIR" \
  --config "$BASE/knowledge_sources_seo_elite_live.json" \
  --state-path "$STATE_PATH" \
  --runs-dir "$RUNS_DIR" \
  --phase2-dir "$BASE/ingest/seo_elite/phase2" \
  --phase3-dir "$BASE/ingest/seo_elite/phase3" \
  --db-path "$DB_PATH" \
  --skills-root "$SKILLS_ROOT" \
  --memory-router "$SKILLS_ROOT/seo-elite/MEMORY.md" \
  --index-path "$MEMORY_DIR/INDEX.md" >> "$LOG_DIR/seo_elite_cleanup.log" 2>&1

zsh "$BASE/run_seo_elite_visual_refresh.sh"
