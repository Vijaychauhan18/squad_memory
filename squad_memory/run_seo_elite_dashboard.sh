#!/bin/zsh
set -eu

PORT="${1:-8791}"

python3 $HOME/squad_memory/seo_elite_dashboard.py serve --host 127.0.0.1 --port "$PORT"
