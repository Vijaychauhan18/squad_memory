#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"
STOP_FILE="$BASE/seo_expert_feed_stop_at.txt"
MARKER="codex-seo-expert-feed"
MEMORY_DIR="$HOME/.codex/skills/seo/memory"

mkdir -p "$LOG_DIR"

if [[ -f "$STOP_FILE" ]]; then
  stop_at="$(cat "$STOP_FILE")"
  now_epoch="$(date +%s)"
  if [[ "$now_epoch" -gt "$stop_at" ]]; then
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
    exit 0
  fi
fi

python3 "$BASE/seo_expert_feed_sync.py" run \
  --config "$BASE/seo_expert_sources.json" \
  --output-dir "$MEMORY_DIR" \
  --summary-path "$MEMORY_DIR/live-seo-feed-monitor.md" \
  --top 8 \
  --build-db >> "$LOG_DIR/seo_expert_feed.log" 2>&1
