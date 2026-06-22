#!/usr/bin/env zsh
# Squad AI — One-command setup script
# Usage: zsh setup.sh
set -euo pipefail

EXPORT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOME_DIR="$HOME"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
info()  { echo "${GREEN}[✓]${NC} $1"; }
warn()  { echo "${YELLOW}[!]${NC} $1"; }
error() { echo "${RED}[✗]${NC} $1"; exit 1; }
ask()   { echo "${YELLOW}[?]${NC} $1"; }

echo ""
echo "  Squad AI Setup — Vijay Chauhan's SEO Agent Stack"
echo "  ================================================="
echo ""

# ── 1. Prerequisites ──────────────────────────────────────────────────────────
echo "Checking prerequisites..."

command -v python3 >/dev/null 2>&1 || error "Python 3 required. Install from https://python.org"
PY_VER=$(python3 -c "import sys; print(sys.version_info.minor)")
[[ "$PY_VER" -ge 10 ]] || error "Python 3.10+ required (found 3.${PY_VER})"
info "Python 3.${PY_VER} found"

command -v node >/dev/null 2>&1 || error "Node.js required. Install from https://nodejs.org"
info "Node.js found"

if ! command -v claude >/dev/null 2>&1; then
  warn "Claude Code CLI not found."
  echo "  Install it from: https://claude.ai/code"
  echo "  Or via: npm install -g @anthropic-ai/claude-code"
  ask "Press Enter once Claude Code is installed, or Ctrl+C to exit..."
  read -r
fi
info "Claude Code found"

# ── 2. Python dependencies ────────────────────────────────────────────────────
echo ""
echo "Installing Python dependencies..."
pip3 install -q requests beautifulsoup4 lxml 2>/dev/null || warn "Some pip packages failed — non-critical"
info "Python deps installed"

# ── 3. Copy Claude config files ───────────────────────────────────────────────
echo ""
echo "Installing agent config files..."

mkdir -p "$HOME_DIR/.claude/agents"

if [[ -f "$HOME_DIR/.claude/CLAUDE.md" ]]; then
  warn "CLAUDE.md already exists — backing up to CLAUDE.md.bak"
  cp "$HOME_DIR/.claude/CLAUDE.md" "$HOME_DIR/.claude/CLAUDE.md.bak"
fi
cp "$EXPORT_DIR/claude/CLAUDE.md" "$HOME_DIR/.claude/CLAUDE.md"
info "CLAUDE.md installed"

cp "$EXPORT_DIR/claude/agents/"*.md "$HOME_DIR/.claude/agents/"
info "$(ls "$EXPORT_DIR/claude/agents/" | wc -l | tr -d ' ') agent files installed"

# ── 4. Install squad_memory pipeline ─────────────────────────────────────────
echo ""
echo "Installing squad_memory pipeline..."
mkdir -p "$HOME_DIR/squad_memory/logs" "$HOME_DIR/squad_memory/mcp" "$HOME_DIR/squad_memory/status"

cp "$EXPORT_DIR/squad_memory/"*.py "$HOME_DIR/squad_memory/"
cp "$EXPORT_DIR/squad_memory/"*.sh "$HOME_DIR/squad_memory/"
cp "$EXPORT_DIR/squad_memory/"*.json "$HOME_DIR/squad_memory/"
cp "$EXPORT_DIR/squad_memory/mcp/"* "$HOME_DIR/squad_memory/mcp/"
chmod +x "$HOME_DIR/squad_memory/"*.sh

# Fix all hardcoded /Users/vijaychauhan paths in squad_memory scripts
find "$HOME_DIR/squad_memory" -name "*.sh" -o -name "*.py" -o -name "*.json" | \
  xargs -I{} sed -i '' "s|/Users/vijaychauhan|$HOME_DIR|g" {} 2>/dev/null || \
  find "$HOME_DIR/squad_memory" -name "*.sh" -o -name "*.py" -o -name "*.json" | \
  xargs -I{} sed -i "s|/Users/vijaychauhan|$HOME_DIR|g" {}
info "Pipeline scripts installed (paths fixed for this machine)"

# ── 5. Copy Codex knowledge base ─────────────────────────────────────────────
echo ""
echo "Installing SEO knowledge base (this may take a moment)..."
mkdir -p "$HOME_DIR/.codex/skills"
cp -r "$EXPORT_DIR/codex/skills/seo" "$HOME_DIR/.codex/skills/"
info "$(find "$EXPORT_DIR/codex/skills" -name '*.md' | wc -l | tr -d ' ') knowledge notes installed"

# ── 6. Copy or build the vector DBs ──────────────────────────────────────────
echo ""
if [[ -f "$EXPORT_DIR/squad_memory/squad_memory.db" ]]; then
  echo "Pre-built memory databases found — copying (faster than rebuilding)..."
  cp "$EXPORT_DIR/squad_memory/squad_memory.db" "$HOME_DIR/squad_memory/squad_memory.db"
  info "squad_memory.db installed ($(du -sh "$HOME_DIR/squad_memory/squad_memory.db" | cut -f1))"
  if [[ -f "$EXPORT_DIR/squad_memory/seo_elite_memory.db" ]]; then
    cp "$EXPORT_DIR/squad_memory/seo_elite_memory.db" "$HOME_DIR/squad_memory/seo_elite_memory.db"
    info "seo_elite_memory.db installed ($(du -sh "$HOME_DIR/squad_memory/seo_elite_memory.db" | cut -f1))"
  fi
else
  echo "No pre-built DBs found — building memory index from knowledge notes..."
  echo "  This takes 2-5 minutes..."
  cd "$HOME_DIR/squad_memory" && python3 squad_memory.py build \
    --root "$HOME_DIR/.codex/skills" \
    --db "$HOME_DIR/squad_memory/squad_memory.db" \
    2>&1 | tail -3
  info "Memory index built"
fi

# ── 7. Configure settings.json ───────────────────────────────────────────────
echo ""
echo "Configuring API keys..."
echo ""
warn "You will need the following credentials from Vijay:"
echo "  1. Ahrefs API key"
echo "  2. SEO MCP API key"
echo "  3. Google Service Account JSON (for GSC + GA4)"
echo "  4. GA4 Property ID"
echo ""

SETTINGS_SRC="$EXPORT_DIR/settings.template.json"
SETTINGS_DST="$HOME_DIR/.claude/settings.json"

if [[ -f "$SETTINGS_DST" ]]; then
  warn "settings.json already exists — backing up to settings.json.bak"
  cp "$SETTINGS_DST" "$SETTINGS_DST.bak"
fi

cp "$SETTINGS_SRC" "$SETTINGS_DST"
# Replace $HOME placeholder with actual home directory
sed -i '' "s|\$HOME|$HOME_DIR|g" "$SETTINGS_DST" 2>/dev/null || sed -i "s|\$HOME|$HOME_DIR|g" "$SETTINGS_DST"
info "settings.json installed (API keys need to be filled in)"

echo ""
echo "  Edit $SETTINGS_DST and replace these placeholders:"
echo "  • YOUR_AHREFS_API_KEY"
echo "  • YOUR_SEOMCP_API_KEY"
echo "  • YOUR_GOOGLE_SERVICE_ACCOUNT_JSON_BASE64"
echo "  • YOUR_GA4_PROPERTY_IDS_COMMA_SEPARATED"
echo "  • YOUR_GSC_SITE_URLS_COMMA_SEPARATED"
echo "  • YOUR_GA4_PROPERTY_ID"
echo "  • YOUR_GOOGLE_SERVICE_ACCOUNT_KEY_PATH"

# ── 8. Codex setup ───────────────────────────────────────────────────────────
echo ""
echo "Setting up Codex..."

# 8a. Codex MCP node packages
mkdir -p "$HOME_DIR/.codex/mcps"
MCP_ZIP="$EXPORT_DIR/codex/mcps/codex_mcps.zip"
if [[ -f "$MCP_ZIP" ]]; then
  unzip -qo "$MCP_ZIP" -d "$HOME_DIR/.codex/mcps/"
  info "MCP source files extracted from zip"
fi
for mcp in enterprise-seo-mcp squad-memory-mcp lumar-mcp; do
  DST="$HOME_DIR/.codex/mcps/$mcp"
  SRC="$EXPORT_DIR/codex/mcps/$mcp"
  # Fall back to directory copy if zip wasn't present or MCP dir missing
  if [[ ! -d "$DST/src" ]] && [[ -d "$SRC" ]]; then
    mkdir -p "$DST"
    cp -r "$SRC/src" "$DST/"
    cp "$SRC/package.json" "$DST/"
    [[ -f "$SRC/package-lock.json" ]] && cp "$SRC/package-lock.json" "$DST/"
  fi
  if [[ -d "$DST/src" ]]; then
    # Fix hardcoded paths in MCP source files
    find "$DST/src" -name "*.js" | \
      xargs -I{} sed -i '' "s|/Users/vijaychauhan|$HOME_DIR|g" {} 2>/dev/null || \
      find "$DST/src" -name "*.js" | \
      xargs -I{} sed -i "s|/Users/vijaychauhan|$HOME_DIR|g" {}
    cd "$DST" && npm install --silent 2>/dev/null && cd "$EXPORT_DIR"
    info "$mcp installed"
  fi
done

# 8b. Install global npm MCP binaries
echo "  Installing global MCP npm packages..."
npm install -g mcp-server-gsc mcp-server-ga4 mcp-remote --silent 2>/dev/null \
  && info "mcp-server-gsc + mcp-server-ga4 installed globally" \
  || warn "npm global install failed — install manually: npm install -g mcp-server-gsc mcp-server-ga4 mcp-remote"

# 8c. Copy elite-skills knowledge base
# Checks both codex/elite-skills/ and codex/mcps/elite-skills/ — Drive uploads sometimes nest into mcps/
mkdir -p "$HOME_DIR/.codex/elite-skills"
for _elite_src in "$EXPORT_DIR/codex/elite-skills/seo-elite" "$EXPORT_DIR/codex/mcps/elite-skills/seo-elite"; do
  if [[ -d "$_elite_src" ]] && [[ -n "$(ls -A "$_elite_src" 2>/dev/null)" ]]; then
    cp -r "$_elite_src" "$HOME_DIR/.codex/elite-skills/"
    info "Elite skills memory installed ($(find "$_elite_src" -name '*.md' | wc -l | tr -d ' ') notes)"
    break
  fi
done

# 8d. Copy all Codex skills
if [[ -d "$EXPORT_DIR/codex/skills" ]]; then
  mkdir -p "$HOME_DIR/.codex/skills"
  cp -r "$EXPORT_DIR/codex/skills/"* "$HOME_DIR/.codex/skills/"
  info "$(ls "$EXPORT_DIR/codex/skills/" | wc -l | tr -d ' ') Codex skill packs installed"
fi

# 8e. Copy Codex automations (micro agents)
if [[ -d "$EXPORT_DIR/codex/automations" ]]; then
  mkdir -p "$HOME_DIR/.codex/automations"
  cp -r "$EXPORT_DIR/codex/automations/"* "$HOME_DIR/.codex/automations/"
  # Fix hardcoded paths in automation.toml files
  find "$HOME_DIR/.codex/automations" -name "automation.toml" | \
    xargs -I{} sed -i '' "s|/Users/vijaychauhan|$HOME_DIR|g" {} 2>/dev/null || \
    find "$HOME_DIR/.codex/automations" -name "automation.toml" | \
    xargs -I{} sed -i "s|/Users/vijaychauhan|$HOME_DIR|g" {}
  info "$(ls "$EXPORT_DIR/codex/automations/" | wc -l | tr -d ' ') Codex automations installed (paths fixed)"
fi

# 8f. Copy Codex rules
if [[ -d "$EXPORT_DIR/codex/rules" ]]; then
  mkdir -p "$HOME_DIR/.codex/rules"
  cp "$EXPORT_DIR/codex/rules/default.rules" "$HOME_DIR/.codex/rules/"
  info "Codex default.rules installed"
fi

# 8g. Copy local plugins
mkdir -p "$HOME_DIR/plugins"
PLUGINS_ZIP="$EXPORT_DIR/codex/plugins/codex_plugins.zip"
if [[ -f "$PLUGINS_ZIP" ]]; then
  unzip -qo "$PLUGINS_ZIP" -d "$HOME_DIR/"
  info "Plugins extracted from zip"
elif [[ -d "$EXPORT_DIR/codex/plugins" ]]; then
  cp -r "$EXPORT_DIR/codex/plugins/"* "$HOME_DIR/plugins/"
fi
# Fallback: plugins may also be in codex/mcps/plugins/ if Drive upload nested them there
if [[ -d "$EXPORT_DIR/codex/mcps/plugins" ]]; then
  for _pdir in "$EXPORT_DIR/codex/mcps/plugins"/*/; do
    [[ -d "$_pdir" ]] && cp -r "$_pdir" "$HOME_DIR/plugins/"
  done
fi
# Fix hardcoded paths in plugin config files
find "$HOME_DIR/plugins" -name "*.json" -o -name "*.toml" | \
  xargs -I{} sed -i '' "s|/Users/vijaychauhan|$HOME_DIR|g" {} 2>/dev/null || \
  find "$HOME_DIR/plugins" -name "*.json" -o -name "*.toml" | \
  xargs -I{} sed -i "s|/Users/vijaychauhan|$HOME_DIR|g" {}
# Install npm deps for any plugin that has a package.json
for plugin_dir in "$HOME_DIR/plugins"/*/; do
  if [[ -f "$plugin_dir/package.json" ]]; then
    cd "$plugin_dir" && npm install --silent 2>/dev/null && cd "$EXPORT_DIR" \
      && info "npm install done for $(basename "$plugin_dir")" \
      || warn "npm install failed for $(basename "$plugin_dir") — install manually: cd ~/plugins/$(basename "$plugin_dir") && npm install"
  fi
done
info "Plugins installed → ~/plugins/ (paths fixed)"
warn "busbud-seo-ops plugin: update BUSBUD_GSC_CREDENTIALS path in ~/plugins/busbud-seo-ops/.mcp.json to point to your google-service-account.json"

# 8h. Copy Lumar credentials
if [[ -f "$HOME_DIR/squad_ai_config_export/lumar_credentials.json" ]]; then
  cp "$HOME_DIR/squad_ai_config_export/lumar_credentials.json" "$HOME_DIR/.codex/lumar_credentials.json"
  info "Lumar credentials installed"
fi

# 8i. Install Codex config.toml
CODEX_CFG_SRC="$EXPORT_DIR/codex/config.toml"
CODEX_CFG_DST="$HOME_DIR/.codex/config.toml"
if [[ -f "$CODEX_CFG_DST" ]]; then
  warn "Codex config.toml exists — backing up to config.toml.bak"
  cp "$CODEX_CFG_DST" "$CODEX_CFG_DST.bak"
fi
cp "$CODEX_CFG_SRC" "$CODEX_CFG_DST"
sed -i '' "s|\$HOME|$HOME_DIR|g" "$CODEX_CFG_DST" 2>/dev/null || sed -i "s|\$HOME|$HOME_DIR|g" "$CODEX_CFG_DST"
info "Codex config.toml installed — all MCPs wired up"

# ── 9. Start dashboards ───────────────────────────────────────────────────────
echo ""
ask "Start dashboards now? (y/n) — opens at http://127.0.0.1:8791, :8765, :8794"
read -r START_DASH
if [[ "$START_DASH" == "y" ]]; then
  cd "$HOME_DIR/squad_memory"
  nohup zsh run_seo_elite_dashboard.sh 8791 > logs/dashboard_8791.log 2>&1 &
  nohup python3 phase31_memory_graph.py serve --host 127.0.0.1 --port 8765 --db-path squad_memory.db > logs/dashboard_8765.log 2>&1 &
  nohup python3 vector_scraper_watch_dashboard.py --host 127.0.0.1 --port 8794 > logs/dashboard_8794.log 2>&1 &
  sleep 3
  info "Dashboards started:"
  echo "  • SEO Dashboard:  http://127.0.0.1:8791"
  echo "  • Memory Graph:   http://127.0.0.1:8765"
  echo "  • Scraper Watch:  http://127.0.0.1:8794"
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "  Setup complete!"
echo "  ─────────────────────────────────────────────────"
echo "  1. Fill in API keys in: ~/.claude/settings.json"
echo "  2. Open Claude Code and start with: 'Morning briefing'"
echo "  3. All 24 Claude agents + 37 Codex skills are ready"
echo "  4. 3 Codex automations (weekly-gsc-wins, nightly-gsc-intel, seo-action-board) active"
echo "  5. Dashboards: http://127.0.0.1:8791 (SEO) | :8765 (Graph) | :8794 (Scraper)"
echo ""
