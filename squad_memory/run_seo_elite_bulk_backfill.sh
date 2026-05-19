#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
SKILLS_ROOT="/Users/vijaychauhan/.codex/elite-skills"
DB_PATH="$BASE/seo_elite_memory.db"
DEFER_BUILD="${SEO_ELITE_DEFER_BUILD:-0}"
DEFER_VISUAL_REFRESH="${SEO_ELITE_DEFER_VISUAL_REFRESH:-0}"

mkdir -p "$LOG_DIR"

python3 "$BASE/bulk_backfill_seo_elite.py" \
  --bulk-dir "$SKILLS_ROOT/seo-elite/memory/archive/bulk" \
  --summary-path "$SKILLS_ROOT/seo-elite/memory/archive/bulk/bulk-backfill-monitor.md" \
  --snapshot-dir "$BASE/ingest/seo_elite/bulk/raw" \
  --runs-dir "$BASE/ingest/seo_elite/bulk/runs" \
  --items-per-note 1200 >> "$LOG_DIR/seo_elite_bulk_backfill.log" 2>&1

python3 "$BASE/harvest_seo_elite_articles.py" \
  --memory-dir "$SKILLS_ROOT/seo-elite/memory" \
  --archive-dir "$SKILLS_ROOT/seo-elite/memory/archive" \
  --skills-root "$SKILLS_ROOT" \
  --db-path "$DB_PATH" \
  --state-path "$BASE/ingest/seo_elite/article_harvest/state.json" \
  --runs-dir "$BASE/ingest/seo_elite/article_harvest/runs" \
  --limit-per-run 16000 \
  --max-workers 32 >> "$LOG_DIR/seo_elite_bulk_backfill.log" 2>&1

if [[ "$DEFER_BUILD" != "1" ]]; then
  python3 "$BASE/squad_memory.py" build \
    --root "$SKILLS_ROOT" \
    --db "$DB_PATH" >> "$LOG_DIR/seo_elite_bulk_backfill.log" 2>&1
fi

if [[ "$DEFER_VISUAL_REFRESH" != "1" ]]; then
  zsh "$BASE/run_seo_elite_visual_refresh.sh" >> "$LOG_DIR/seo_elite_bulk_backfill.log" 2>&1 || true
fi
