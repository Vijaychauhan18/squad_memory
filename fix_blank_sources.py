#!/usr/bin/env python3
"""
Fix blank source fields in squad_memory.db
Infers source from path, skill, heading, and text content.
Updates all 57,369+ chunks with empty source fields.
"""

import sqlite3
import re
import os
from urllib.parse import urlparse

DB_PATH = os.path.expanduser("~/squad_memory/squad_memory.db")

# ── Source inference rules ────────────────────────────────────────────────────

# Path prefix → source (checked first, most reliable)
PATH_RULES = [
    # External content archives
    (r"charles/memory/archive/buffer/", "buffer"),
    (r"charles/memory/archive/hubspot/", "hubspot"),
    (r"charles/memory/archive/sprout", "sprout-social"),
    (r"charles/memory/archive/hootsuite", "hootsuite"),
    (r"charles/memory/archive/later", "later"),
    (r"charles/memory/archive/semrush", "semrush"),
    (r"charles/memory/archive/moz", "moz"),
    (r"charles/memory/archive/backlinko", "backlinko"),
    (r"charles/memory/archive/searchengineland", "searchengineland"),
    (r"charles/memory/archive/searchenginejournal", "searchenginejournal"),
    (r"charles/memory/archive/neilpatel", "neilpatel"),
    (r"charles/memory/archive/contentmarketinginstitute", "cmi"),
    (r"charles/memory/archive/", "charles-archive"),

    # Skill files
    (r"^ahrefs/", "ahrefs"),
    (r"^dejan/", "dejan"),
    (r"^hobo/", "hobo"),
    (r"^semrush/", "semrush"),
    (r"^moz/", "moz"),
    (r"^backlinko/", "backlinko"),
    (r"^google/", "google"),

    # System files
    (r"^\.system/openai-docs/", "openai"),
    (r"^\.system/skill-creator/", "squad-system"),
    (r"^\.system/skill-installer/", "squad-system"),
    (r"^\.system/", "squad-system"),

    # Agent skill files
    (r"^blank-agent-kit/", "squad-kit"),
    (r"^SQUAD_MEMORY", "squad-system"),

    # Squad agent files (skill-based)
    (r"^charles/", "charles"),
    (r"^coral/", "coral"),
    (r"^plankton/", "plankton"),
    (r"^kelp/", "kelp"),
    (r"^chitin/", "chitin"),
    (r"^reef/", "reef"),
    (r"^tide/", "tide"),
    (r"^urchin/", "urchin"),
    (r"^krill/", "krill"),
    (r"^anemone/", "anemone"),
    (r"^pinchy/", "pinchy"),
    (r"^current/", "current"),
]

# Skill → source fallback (when path gives no hint)
SKILL_SOURCE_MAP = {
    "seo":                     "squad-seo",
    "support-anemone":         "squad-support",
    "marketing":               "squad-marketing",
    "writer":                  "squad-writer",
    "qa":                      "squad-qa",
    "charles":                 "charles",
    "developer":               "squad-dev",
    "multi-agent-reef":        "squad-qa",
    "operations":              "squad-ops",
    "finance":                 "squad-finance",
    "emily":                   "squad-internal",
    "devops":                  "squad-devops",
    "devops-tide":             "squad-devops",
    "reviewer":                "squad-review",
    "orchestrator-pinchy":     "squad-orchestrator",
    "operations-urchin":       "squad-ops",
    "finance-krill":           "squad-finance",
    "squad_router":            "squad-system",
    "marketing-current":       "squad-marketing",
    "dejan-ai-reverse-engineering": "dejan",
    ".system":                 "squad-system",
}

# Domain extraction from URLs in text
URL_PATTERN = re.compile(r'https?://(?:www\.)?([a-zA-Z0-9\-]+\.[a-zA-Z]{2,})')

KNOWN_DOMAINS = {
    "hobo-web.co.uk": "hobo",
    "ahrefs.com": "ahrefs",
    "semrush.com": "semrush",
    "moz.com": "moz",
    "backlinko.com": "backlinko",
    "searchengineland.com": "searchengineland",
    "searchenginejournal.com": "searchenginejournal",
    "neilpatel.com": "neilpatel",
    "hubspot.com": "hubspot",
    "buffer.com": "buffer",
    "sproutsocial.com": "sprout-social",
    "hootsuite.com": "hootsuite",
    "later.com": "later",
    "dejan.ai": "dejan",
    "google.com": "google",
    "developers.google.com": "google",
    "search.google.com": "google",
    "openai.com": "openai",
    "anthropic.com": "anthropic",
    "contentmarketinginstitute.com": "cmi",
    "marketingprofs.com": "marketingprofs",
}


def infer_source(path: str, skill: str, text: str) -> str:
    """Infer source from path → skill → text URL."""
    path = path or ""
    skill = skill or ""
    text = text or ""

    # 1. Path rules (most reliable)
    for pattern, source in PATH_RULES:
        if re.search(pattern, path, re.IGNORECASE):
            return source

    # 2. Skill map fallback
    if skill in SKILL_SOURCE_MAP:
        return SKILL_SOURCE_MAP[skill]

    # 3. URL extraction from text
    matches = URL_PATTERN.findall(text[:500])
    for domain in matches:
        domain_lower = domain.lower()
        for known, source in KNOWN_DOMAINS.items():
            if known in domain_lower:
                return source

    # 4. Skill partial match
    skill_lower = skill.lower()
    for key, source in SKILL_SOURCE_MAP.items():
        if key in skill_lower:
            return source

    return "squad-internal"


def run():
    conn = sqlite3.connect(DB_PATH, timeout=60)

    # Count blank sources
    total_blank = conn.execute(
        "SELECT COUNT(*) FROM chunks WHERE (source IS NULL OR source = '')"
    ).fetchone()[0]
    print(f"Blank source chunks to fix: {total_blank:,}")

    # Load all blank-source chunks
    rows = conn.execute("""
        SELECT chunk_id, path, skill, text
        FROM chunks
        WHERE (source IS NULL OR source = '')
    """).fetchall()

    # Build updates
    updates = []
    source_counts = {}
    for chunk_id, path, skill, text in rows:
        source = infer_source(path or "", skill or "", text or "")
        updates.append((source, chunk_id))
        source_counts[source] = source_counts.get(source, 0) + 1

    # Bulk update in batches of 5000
    BATCH = 5000
    for i in range(0, len(updates), BATCH):
        batch = updates[i:i+BATCH]
        conn.executemany("UPDATE chunks SET source = ? WHERE chunk_id = ?", batch)
        conn.commit()
        print(f"  Updated {min(i+BATCH, len(updates)):,}/{len(updates):,}")

    print(f"\nDone. Fixed {len(updates):,} chunks.")
    print("\nSource distribution:")
    for src, cnt in sorted(source_counts.items(), key=lambda x: -x[1])[:20]:
        print(f"  {src:<35} {cnt:>6,}")

    # Verify
    remaining = conn.execute(
        "SELECT COUNT(*) FROM chunks WHERE (source IS NULL OR source = '')"
    ).fetchone()[0]
    print(f"\nRemaining blank: {remaining:,}")

    conn.close()


if __name__ == "__main__":
    run()
