# Squad AI — Windows Setup Script (PowerShell)
# Usage: Right-click PowerShell > Run as Administrator, then: .\setup.ps1
# Requires: Python 3.10+, Node.js, Claude Code CLI

$ErrorActionPreference = "Stop"
$ExportDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$HomeDir = $env:USERPROFILE

function Info  { Write-Host "[OK] $args" -ForegroundColor Green }
function Warn  { Write-Host "[!]  $args" -ForegroundColor Yellow }
function Err   { Write-Host "[X]  $args" -ForegroundColor Red; exit 1 }

Write-Host ""
Write-Host "  Squad AI Setup — Windows" -ForegroundColor Cyan
Write-Host "  ========================" -ForegroundColor Cyan
Write-Host ""

# ── 1. Prerequisites ──────────────────────────────────────────────────────────
Write-Host "Checking prerequisites..."

if (-not (Get-Command python -ErrorAction SilentlyContinue)) { Err "Python 3 not found. Install from https://python.org (add to PATH)" }
$pyVer = python -c "import sys; print(sys.version_info.minor)"
if ([int]$pyVer -lt 10) { Err "Python 3.10+ required (found 3.$pyVer)" }
Info "Python 3.$pyVer found"

if (-not (Get-Command node -ErrorAction SilentlyContinue)) { Err "Node.js not found. Install from https://nodejs.org" }
Info "Node.js found"

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Warn "Claude Code CLI not found."
    Write-Host "  Install: npm install -g @anthropic-ai/claude-code"
    Read-Host "Press Enter once Claude Code is installed"
}
Info "Claude Code found"

# ── 2. Python dependencies ────────────────────────────────────────────────────
Write-Host ""
Write-Host "Installing Python dependencies..."
pip install -q requests beautifulsoup4 lxml 2>$null
Info "Python deps installed"

# ── 3. Claude config files ────────────────────────────────────────────────────
Write-Host ""
Write-Host "Installing agent config files..."
$claudeDir = "$HomeDir\.claude\agents"
New-Item -ItemType Directory -Force -Path $claudeDir | Out-Null

$claudeMd = "$HomeDir\.claude\CLAUDE.md"
if (Test-Path $claudeMd) { Copy-Item $claudeMd "$claudeMd.bak"; Warn "Backed up existing CLAUDE.md" }
Copy-Item "$ExportDir\claude\CLAUDE.md" $claudeMd
Info "CLAUDE.md installed"

Copy-Item "$ExportDir\claude\agents\*.md" $claudeDir
Info "Agent files installed"

# ── 4. squad_memory pipeline ──────────────────────────────────────────────────
Write-Host ""
Write-Host "Installing squad_memory pipeline..."
$sqDir = "$HomeDir\squad_memory"
New-Item -ItemType Directory -Force -Path "$sqDir\logs","$sqDir\mcp","$sqDir\status" | Out-Null

Copy-Item "$ExportDir\squad_memory\*.py"   $sqDir -ErrorAction SilentlyContinue
Copy-Item "$ExportDir\squad_memory\*.json" $sqDir -ErrorAction SilentlyContinue
Copy-Item "$ExportDir\squad_memory\mcp\*"  "$sqDir\mcp\" -ErrorAction SilentlyContinue
Info "Pipeline scripts installed"

# ── 5. Copy or build vector DBs ──────────────────────────────────────────────
Write-Host ""
$dbSrc = "$ExportDir\squad_memory\squad_memory.db"
if (Test-Path $dbSrc) {
    Write-Host "Copying pre-built memory databases..."
    Copy-Item $dbSrc "$sqDir\squad_memory.db"
    Info "squad_memory.db installed"
    $eliteSrc = "$ExportDir\squad_memory\seo_elite_memory.db"
    if (Test-Path $eliteSrc) {
        Copy-Item $eliteSrc "$sqDir\seo_elite_memory.db"
        Info "seo_elite_memory.db installed"
    }
} else {
    Write-Host "No pre-built DBs found — building from knowledge notes (2-5 min)..."
    python "$sqDir\squad_memory.py" build --root "$HomeDir\.codex\skills" --db "$sqDir\squad_memory.db"
    Info "Memory index built"
}

# ── 6. Codex knowledge base ───────────────────────────────────────────────────
Write-Host ""
Write-Host "Installing SEO knowledge base..."
New-Item -ItemType Directory -Force -Path "$HomeDir\.codex\skills" | Out-Null
if (Test-Path "$ExportDir\codex\skills\seo") {
    Copy-Item -Recurse "$ExportDir\codex\skills\seo" "$HomeDir\.codex\skills\" -Force
    Info "SEO knowledge notes installed"
}

# Elite skills
New-Item -ItemType Directory -Force -Path "$HomeDir\.codex\elite-skills" | Out-Null
foreach ($src in @("$ExportDir\codex\elite-skills\seo-elite","$ExportDir\codex\mcps\elite-skills\seo-elite")) {
    if (Test-Path $src) { Copy-Item -Recurse $src "$HomeDir\.codex\elite-skills\" -Force; Info "Elite skills installed"; break }
}

# All Codex skills
if (Test-Path "$ExportDir\codex\skills") {
    Copy-Item -Recurse "$ExportDir\codex\skills\*" "$HomeDir\.codex\skills\" -Force
    Info "Codex skill packs installed"
}

# ── 7. settings.json ──────────────────────────────────────────────────────────
Write-Host ""
Write-Host "Configuring settings.json..."
$settingsSrc = "$ExportDir\settings.template.json"
$settingsDst = "$HomeDir\.claude\settings.json"

if (Test-Path $settingsDst) { Copy-Item $settingsDst "$settingsDst.bak"; Warn "Backed up existing settings.json" }
$content = Get-Content $settingsSrc -Raw
# Replace $HOME and /Users/vijaychauhan with Windows-style home path (forward slashes for JSON)
$winHome = $HomeDir -replace '\\', '/'
$content = $content -replace '\$HOME', $winHome
$content = $content -replace '/Users/vijaychauhan', $winHome
Set-Content $settingsDst $content
Info "settings.json installed"

Warn "Fill in API keys in: $settingsDst"
Write-Host "  Replace: YOUR_AHREFS_API_KEY, YOUR_SEOMCP_API_KEY, YOUR_GA4_PROPERTY_ID etc."

# ── 8. Codex config ───────────────────────────────────────────────────────────
Write-Host ""
Write-Host "Setting up Codex..."
$codexCfgSrc = "$ExportDir\codex\config.toml"
$codexCfgDst = "$HomeDir\.codex\config.toml"
if (Test-Path $codexCfgDst) { Copy-Item $codexCfgDst "$codexCfgDst.bak"; Warn "Backed up Codex config" }
if (Test-Path $codexCfgSrc) {
    $cfg = Get-Content $codexCfgSrc -Raw
    $winHome = $HomeDir -replace '\\', '/'
    $cfg = $cfg -replace '\$HOME', $winHome
    $cfg = $cfg -replace '/Users/vijaychauhan', $winHome
    Set-Content $codexCfgDst $cfg
    Info "Codex config.toml installed"
}

# Global npm MCPs
Write-Host "  Installing global npm MCP packages..."
npm install -g mcp-server-gsc mcp-server-ga4 mcp-remote --silent 2>$null
Info "npm MCP packages installed"

# ── Done ──────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  Setup complete!" -ForegroundColor Green
Write-Host "  ─────────────────────────────────────────────────"
Write-Host "  1. Fill in API keys: $settingsDst"
Write-Host "  2. Open Claude Code and type: Morning briefing"
Write-Host "  3. Dashboards (run manually):"
Write-Host "     python $sqDir\seo_elite_dashboard.py serve --port 8791"
Write-Host "     python $sqDir\phase31_memory_graph.py serve --port 8765"
Write-Host ""
Write-Host "  NOTE: .sh shell scripts are macOS/Linux only."
Write-Host "  On Windows, run the equivalent python3 commands directly." -ForegroundColor Yellow
Write-Host ""
