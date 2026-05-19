#!/bin/zsh
set -eu

PORT="${1:-8791}"

python3 /Users/vijaychauhan/squad_memory/seo_elite_dashboard.py serve --host 127.0.0.1 --port "$PORT"
