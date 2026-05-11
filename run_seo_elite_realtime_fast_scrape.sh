#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
SKILLS_ROOT="/Users/vijaychauhan/.codex/elite-skills"
ARCHIVE_DIR="$SKILLS_ROOT/seo-elite/memory/archive"
DB_PATH="$BASE/seo_elite_memory.db"
DEFER_BUILD="${SEO_ELITE_DEFER_BUILD:-0}"
DEFER_VISUAL_REFRESH="${SEO_ELITE_DEFER_VISUAL_REFRESH:-0}"

REALTIME_ROOT="$BASE/ingest/seo_elite/realtime/semrush"
SUMMARY_PATH="$ARCHIVE_DIR/realtime-semrush-top30-monitor.md"
SNAPSHOT_DIR="$REALTIME_ROOT/raw"
RUNS_DIR="$REALTIME_ROOT/runs"
STATE_PATH="$BASE/ingest/seo_elite/archive/state.json"

mkdir -p "$LOG_DIR" "$SNAPSHOT_DIR" "$RUNS_DIR"

primary_cmd=(python3 "$BASE/refresh_seo_elite_primary_sources.py")
if [[ "$DEFER_BUILD" == "1" ]]; then
  primary_cmd+=(--skip-build)
fi
"${primary_cmd[@]}" >> "$LOG_DIR/seo_elite_realtime_fast_scrape.log" 2>&1

semrush_cmd=(
  python3 "$BASE/refresh_semrush_top30.py"
  --config "$BASE/knowledge_sources_seo_elite_archive.json" \
  --output-dir "$ARCHIVE_DIR" \
  --note-path "$ARCHIVE_DIR/live-source-semrush.md" \
  --summary-path "$SUMMARY_PATH" \
  --snapshot-dir "$SNAPSHOT_DIR" \
  --runs-dir "$RUNS_DIR" \
  --state-path "$STATE_PATH" \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH" \
  --top 30
)
"${semrush_cmd[@]}" >> "$LOG_DIR/seo_elite_realtime_fast_scrape.log" 2>&1

python3 "$BASE/harvest_seo_elite_articles.py" \
  --memory-dir "$SKILLS_ROOT/seo-elite/memory" \
  --archive-dir "$SKILLS_ROOT/seo-elite/memory/archive" \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH" \
  --state-path "$BASE/ingest/seo_elite/article_harvest/state.json" \
  --runs-dir "$BASE/ingest/seo_elite/article_harvest/runs" \
  --limit-per-run 300 >> "$LOG_DIR/seo_elite_realtime_fast_scrape.log" 2>&1

if [[ "$DEFER_BUILD" != "1" ]]; then
  python3 "$BASE/squad_memory.py" build \
    --root "$SKILLS_ROOT" \
    --db "$DB_PATH" >> "$LOG_DIR/seo_elite_realtime_fast_scrape.log" 2>&1
fi

if [[ "$DEFER_VISUAL_REFRESH" != "1" ]]; then
  zsh "$BASE/run_seo_elite_visual_refresh.sh"
fi
