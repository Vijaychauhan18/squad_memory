#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"
SKILLS_ROOT="$HOME/.codex/elite-skills"
ARCHIVE_DIR="$SKILLS_ROOT/seo-elite/memory/archive"
RUNS_DIR="$BASE/ingest/seo_elite/archive/runs"
SNAPSHOT_DIR="$BASE/ingest/seo_elite/archive/raw"
STATE_PATH="$BASE/ingest/seo_elite/archive/state.json"
DB_PATH="$BASE/seo_elite_memory.db"
DEFER_BUILD="${SEO_ELITE_DEFER_BUILD:-0}"
DEFER_VISUAL_REFRESH="${SEO_ELITE_DEFER_VISUAL_REFRESH:-0}"

mkdir -p "$LOG_DIR" "$ARCHIVE_DIR" "$RUNS_DIR" "$SNAPSHOT_DIR"
zsh "$BASE/sync_seo_elite_seed.sh"

archive_cmd=(
  python3 "$BASE/knowledge_ingest.py" run
  --config "$BASE/knowledge_sources_seo_elite_archive.json" \
  --output-dir "$ARCHIVE_DIR" \
  --summary-path "$ARCHIVE_DIR/live-archive-monitor.md" \
  --snapshot-dir "$SNAPSHOT_DIR" \
  --runs-dir "$RUNS_DIR" \
  --state-path "$STATE_PATH" \
  --top 50 \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH"
)
"${archive_cmd[@]}" >> "$LOG_DIR/seo_elite_archive_backfill.log" 2>&1

semrush_cmd=(
  python3 "$BASE/refresh_semrush_top30.py"
  --config "$BASE/knowledge_sources_seo_elite_archive.json" \
  --output-dir "$ARCHIVE_DIR" \
  --note-path "$ARCHIVE_DIR/live-source-semrush.md" \
  --summary-path "$ARCHIVE_DIR/realtime-semrush-top30-monitor.md" \
  --snapshot-dir "$BASE/ingest/seo_elite/realtime/semrush/raw" \
  --runs-dir "$BASE/ingest/seo_elite/realtime/semrush/runs" \
  --state-path "$STATE_PATH" \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH" \
  --top 30
)
"${semrush_cmd[@]}" >> "$LOG_DIR/seo_elite_archive_backfill.log" 2>&1

if [[ "$DEFER_BUILD" != "1" ]]; then
  python3 "$BASE/squad_memory.py" build \
    --root "$SKILLS_ROOT" \
    --db "$DB_PATH" >> "$LOG_DIR/seo_elite_archive_backfill.log" 2>&1
fi

if [[ "$DEFER_VISUAL_REFRESH" != "1" ]]; then
  zsh "$BASE/run_seo_elite_visual_refresh.sh"
fi
