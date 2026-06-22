#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
SKILLS_ROOT="/Users/vijaychauhan/.codex/elite-skills"
MEMORY_DIR="$SKILLS_ROOT/seo-elite/memory"
RUNS_DIR="$BASE/ingest/seo_elite/live/runs"
SNAPSHOT_DIR="$BASE/ingest/seo_elite/live/raw"
STATE_PATH="$BASE/ingest/seo_elite/live/state.json"
DB_PATH="$BASE/seo_elite_memory.db"
DEFER_BUILD="${SEO_ELITE_DEFER_BUILD:-0}"
DEFER_VISUAL_REFRESH="${SEO_ELITE_DEFER_VISUAL_REFRESH:-0}"

mkdir -p "$LOG_DIR" "$MEMORY_DIR" "$RUNS_DIR" "$SNAPSHOT_DIR"
zsh "$BASE/sync_seo_elite_seed.sh"

knowledge_cmd=(
  python3 "$BASE/knowledge_ingest.py" run
  --config "$BASE/knowledge_sources_seo_elite_live.json" \
  --output-dir "$MEMORY_DIR" \
  --summary-path "$MEMORY_DIR/live-knowledge-monitor.md" \
  --snapshot-dir "$SNAPSHOT_DIR" \
  --runs-dir "$RUNS_DIR" \
  --state-path "$STATE_PATH" \
  --top 40 \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH"
)
"${knowledge_cmd[@]}" >> "$LOG_DIR/seo_elite_live_sync.log" 2>&1

prune_cmd=(
  python3 "$BASE/prune_seo_elite_live_sources.py"
  --output-dir "$MEMORY_DIR" \
  --config "$BASE/knowledge_sources_seo_elite_live.json" \
  --state-path "$STATE_PATH" \
  --runs-dir "$RUNS_DIR" \
  --phase2-dir "$BASE/ingest/seo_elite/phase2" \
  --phase3-dir "$BASE/ingest/seo_elite/phase3" \
  --db-path "$DB_PATH" \
  --skills-root "$SKILLS_ROOT" \
  --memory-router "$SKILLS_ROOT/seo-elite/MEMORY.md" \
  --index-path "$MEMORY_DIR/INDEX.md"
)
"${prune_cmd[@]}" >> "$LOG_DIR/seo_elite_live_sync.log" 2>&1

if [[ "$DEFER_BUILD" != "1" ]]; then
  python3 "$BASE/squad_memory.py" build \
    --root "$SKILLS_ROOT" \
    --db "$DB_PATH" >> "$LOG_DIR/seo_elite_live_sync.log" 2>&1
fi

if [[ "$DEFER_VISUAL_REFRESH" != "1" ]]; then
  zsh "$BASE/run_seo_elite_visual_refresh.sh"
fi
