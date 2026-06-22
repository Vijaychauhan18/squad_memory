#!/bin/zsh
set -eu

BASE="$HOME/squad_memory"
LOG_DIR="$BASE/logs"
MODE="${1:-fast}"
LOG_PATH="$LOG_DIR/codex_local_seo_ops.log"

mkdir -p "$LOG_DIR"

timestamp() {
  date +"[%Y-%m-%d %H:%M:%S]"
}

append_log() {
  print -- "$(timestamp) $1" >> "$LOG_PATH"
}

run_optional_status() {
  append_log "step=report_status start"
  if python3 "$BASE/report_seo_elite_status.py" >> "$LOG_PATH" 2>&1; then
    append_log "step=report_status rc=0"
  else
    append_log "step=report_status rc=1 continue=true"
  fi
}

run_refresh() {
  append_log "step=refresh_openclaw_automation start"
  python3 "$BASE/refresh_openclaw_seo_automation.py" --json >> "$LOG_PATH" 2>&1
  append_log "step=refresh_openclaw_automation rc=0"
}

case "$MODE" in
  fast)
    run_optional_status
    run_refresh
    ;;
  full)
    run_optional_status
    append_log "step=refresh_openclaw_memory start"
    python3 "$BASE/refresh_openclaw_memory.py" --json >> "$LOG_PATH" 2>&1
    append_log "step=refresh_openclaw_memory rc=0"
    run_refresh
    ;;
  *)
    echo "usage: $0 [fast|full]" >&2
    exit 2
    ;;
esac
