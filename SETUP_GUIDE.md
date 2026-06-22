# Squad AI — Manager Setup Guide

Everything you need to install Vijay's SEO agent stack on your machine.
Estimated time: **15–20 minutes**.

---

## Before You Start — Get These from Vijay

Vijay will send these separately (not in the repo):

| What | Where to use it |
|------|----------------|
| Ahrefs API key | `~/.claude/settings.json` after setup |
| SEO MCP API key | `~/.claude/settings.json` after setup |
| Firehose keys | `~/.claude/settings.json` after setup |
| SEOGets bearer token | `~/.codex/config.toml` after setup |
| Google Service Account JSON file | Save anywhere on your machine, note the path |
| GA4 Property ID | `~/.claude/settings.json` after setup |
| GSC site URLs | `~/.claude/settings.json` after setup |

---

## Step 1 — Install Prerequisites

### Windows
- **Python 3.10+** — https://python.org (check "Add to PATH" during install)
- **Node.js** — https://nodejs.org
- **Git** — https://git-scm.com
- **Claude Code CLI** — open PowerShell and run: `npm install -g @anthropic-ai/claude-code`

### Mac
- **Python:** `brew install python@3.11` or https://python.org
- **Node.js:** `brew install node` or https://nodejs.org
- **Claude Code CLI:** `npm install -g @anthropic-ai/claude-code`

Verify:
```bash
python3 --version   # needs 3.10+
node --version
claude --version
```

---

## Step 2 — Clone the Repo

```bash
git clone https://github.com/Vijaychauhan18/squad_memory.git
cd squad_memory
```

---

## Step 3 — Reassemble the Databases

The vector databases ship split into chunks (GitHub's 100MB file limit). Reassemble them first:

```bash
# Windows
cd squad_memory\db_chunks
python reassemble_dbs.py
cd ..\..

# Mac / Linux
cd squad_memory/db_chunks && python3 reassemble_dbs.py && cd ../..
```

This creates `squad_memory.db` (~825MB) and `seo_elite_memory.db` (~559MB) one folder up.

---

## Step 4 — Run Setup

### Windows (PowerShell as Admin)
```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```

### Mac / Linux
```bash
zsh setup.sh
```

The script automatically:
1. Checks Python, Node, Claude Code
2. Installs Python dependencies
3. Installs 24 Claude agent files → `~/.claude/`
4. Copies pipeline scripts → `~/squad_memory/`
5. Copies SEO knowledge base (3,988 notes) → `~/.codex/skills/`
6. Copies the reassembled databases → `~/squad_memory/`
7. Installs `settings.json` template → `~/.claude/`
8. Installs Codex MCPs, plugins, and config

---

## Step 5 — Fill in API Keys

Open the settings file:

- **Windows:** `notepad %USERPROFILE%\.claude\settings.json`
- **Mac:** `open ~/.claude/settings.json`

Replace each placeholder with the values Vijay sent you:

| Placeholder | Replace with |
|-------------|-------------|
| `YOUR_AHREFS_API_KEY` | Ahrefs API key |
| `YOUR_SEOMCP_API_KEY` | SEO MCP API key |
| `YOUR_FIREHOSE_MANAGEMENT_KEY` | Firehose management key |
| `YOUR_FIREHOSE_TAP_TOKEN` | Firehose tap token |
| `YOUR_GOOGLE_SERVICE_ACCOUNT_JSON_BASE64` | Base64-encoded service account JSON |
| `YOUR_GA4_PROPERTY_ID` | GA4 property ID |
| `YOUR_GA4_PROPERTY_IDS_COMMA_SEPARATED` | Same ID(s), comma-separated |
| `YOUR_GSC_SITE_URLS_COMMA_SEPARATED` | GSC site URLs |
| `YOUR_GOOGLE_SERVICE_ACCOUNT_KEY_PATH` | Full path to your service account JSON file |

Also open `~/.codex/config.toml` and replace:

| Placeholder | Replace with |
|-------------|-------------|
| `YOUR_AHREFS_API_KEY` | Ahrefs API key |
| `YOUR_SEOMCP_API_KEY` | SEO MCP API key |
| `YOUR_SEOGETS_BEARER_TOKEN` | SEOGets bearer token |

**To base64-encode the Google Service Account JSON:**
- **Mac:** `base64 -i ~/path/to/google-service-account.json | pbcopy`
- **Windows PowerShell:** `[Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\path\to\google-service-account.json")) | clip`

---

## Step 6 — Restart Claude Code

Close and reopen Claude Code. Type `Morning briefing` to verify everything is working.

---

## Dashboards (Mac / Linux only — Windows: skip for now)

```bash
cd ~/squad_memory
nohup python3 seo_elite_dashboard.py serve --host 127.0.0.1 --port 8791 > logs/dashboard_8791.log 2>&1 &
nohup python3 phase31_memory_graph.py serve --host 127.0.0.1 --port 8765 --db-path squad_memory.db > logs/dashboard_8765.log 2>&1 &
nohup python3 vector_scraper_watch_dashboard.py --host 127.0.0.1 --port 8794 > logs/dashboard_8794.log 2>&1 &
```

| Dashboard | URL |
|-----------|-----|
| SEO Brain | http://127.0.0.1:8791 |
| Memory Graph | http://127.0.0.1:8765 |
| Scraper Watch | http://127.0.0.1:8794 |

---

## Verification Checklist

```bash
# Mac / Linux
ls ~/.claude/agents/ | wc -l          # should be 24+
ls ~/.codex/skills/seo/ | wc -l       # should be 3,988+
du -sh ~/squad_memory/*.db            # ~825MB and ~559MB

# Windows PowerShell
(Get-ChildItem "$env:USERPROFILE\.claude\agents\").Count   # 24+
(Get-ChildItem "$env:USERPROFILE\.codex\skills\seo\").Count
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Permission denied` on .sh files (Mac) | `chmod +x ~/squad_memory/*.sh` |
| Python not found on Windows | Reinstall Python, check "Add to PATH" |
| `npm install` failed | Run PowerShell as Administrator |
| Dashboard won't start | Check `~/squad_memory/logs/` for error logs |
| MCPs not showing in Claude Code | Restart Claude Code; check `~/.claude/settings.json` is valid JSON |
| `reassemble_dbs.py` says no chunks found | Make sure you're inside `squad_memory/db_chunks/` when running it |

---

Questions? Contact Vijay at vijay.chauhan@busbud.com
