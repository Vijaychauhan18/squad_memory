#!/bin/zsh
set -eu

BASE="/Users/vijaychauhan/squad_memory"
LOG_DIR="$BASE/logs"
STOP_FILE="$BASE/seo_elite_2h_sprint_stop_at.txt"
MARKER="codex-seo-elite-2h-sprint"
LOCK_DIR="$BASE/locks/seo_elite_2h_sprint.lock"
LOG_FILE="$LOG_DIR/seo_elite_2h_sprint.log"
BRIDGE_LOG="$LOG_DIR/seo_elite_to_squad.log"
SKILLS_ROOT="/Users/vijaychauhan/.codex/elite-skills"
DB_PATH="$BASE/seo_elite_memory.db"

mkdir -p "$LOG_DIR" "$BASE/locks"

cleanup_cron() {
  tmp_file="$(mktemp)"
  if crontab -l > "$tmp_file" 2>/dev/null; then
    filtered_file="${tmp_file}.filtered"
    grep -v "$MARKER" "$tmp_file" > "$filtered_file" || true
    if [[ -s "$filtered_file" ]]; then
      crontab "$filtered_file"
    else
      crontab -r || true
    fi
    rm -f "$filtered_file"
  fi
  rm -f "$tmp_file"
}

if [[ -f "$STOP_FILE" ]]; then
  stop_at="$(cat "$STOP_FILE")"
  now_epoch="$(date +%s)"
  if [[ "$now_epoch" -gt "$stop_at" ]]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] sprint window ended; removing cron marker" >> "$LOG_FILE"
    cleanup_cron
    rm -f "$STOP_FILE"
    exit 0
  fi
fi

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] sprint cycle skipped; lock active" >> "$LOG_FILE"
  exit 0
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT

echo "[$(date '+%Y-%m-%d %H:%M:%S')] sprint cycle start" >> "$LOG_FILE"

export SEO_ELITE_DEFER_BUILD=1
export SEO_ELITE_DEFER_VISUAL_REFRESH=1

zsh "$BASE/run_seo_elite_live_sync.sh" >> "$LOG_FILE" 2>&1 || true
zsh "$BASE/run_seo_elite_archive_backfill.sh" >> "$LOG_FILE" 2>&1 || true
zsh "$BASE/run_seo_elite_primary_priority_scrape.sh" >> "$LOG_FILE" 2>&1 || true
zsh "$BASE/run_seo_elite_bulk_backfill.sh" >> "$LOG_FILE" 2>&1 || true

python3 "$BASE/squad_memory.py" build \
  --root "$SKILLS_ROOT" \
  --db "$DB_PATH" >> "$LOG_FILE" 2>&1 || true

python3 "$BASE/sync_seo_elite_to_squad.py" \
  --build-squad-db \
  --refresh-graph >> "$BRIDGE_LOG" 2>&1 || true

unset SEO_ELITE_DEFER_BUILD
unset SEO_ELITE_DEFER_VISUAL_REFRESH

zsh "$BASE/run_seo_elite_visual_refresh.sh" >> "$LOG_FILE" 2>&1 || true

echo "[$(date '+%Y-%m-%d %H:%M:%S')] sprint cycle end" >> "$LOG_FILE"
