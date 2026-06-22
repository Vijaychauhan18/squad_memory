#!/bin/zsh
set -euo pipefail

python3 /Users/vijaychauhan/squad_memory/phase31_memory_graph.py build \
  --db-path /Users/vijaychauhan/squad_memory/seo_elite_memory.db \
  "$@"
