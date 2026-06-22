#!/bin/zsh
set -eu

SOURCE_DIR="/Users/vijaychauhan/.codex/skills/seo/memory"
TARGET_DIR="/Users/vijaychauhan/.codex/elite-skills/seo-elite/memory"
MANIFEST="/Users/vijaychauhan/squad_memory/seo_elite_seed_manifest.txt"

mkdir -p "$TARGET_DIR"

while IFS= read -r note; do
  [[ -z "$note" ]] && continue
  if [[ -f "$SOURCE_DIR/$note" ]]; then
    cp "$SOURCE_DIR/$note" "$TARGET_DIR/$note"
  fi
done < "$MANIFEST"
