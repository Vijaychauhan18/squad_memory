#!/usr/bin/env zsh
# Weekly memory compression — episodic→semantic, stale derank, dedup
# Cron: 30 3 * * 0 (Sunday 3:30 AM local / 10:00 PM Sat UTC = 3:30 AM IST)

set -euo pipefail

LOG="$HOME/squad_memory/logs/memory_compress_$(date +%Y%m%d).log"
DB="$HOME/squad_memory/squad_memory.db"
SNAPSHOT="$HOME/portable-repos/seo-vector-snapshot/db/squad_memory.db"

echo "[$(date)] Memory compress started" | tee -a "$LOG"

# Step 1: Stale chunk derank (freshness < 0.3 + older than 18 months)
python3 - <<'PYTHON' 2>&1 | tee -a "$LOG"
import sqlite3, datetime, os

db = os.path.expanduser("~/squad_memory/squad_memory.db")
conn = sqlite3.connect(db, timeout=30)

cutoff = (datetime.datetime.now() - datetime.timedelta(days=548)).strftime("%Y-%m-%d")

# Find stale chunks
stale = conn.execute("""
    SELECT chunk_id, skill, topics_json, published_on, freshness
    FROM chunks
    WHERE published_on < ?
      AND freshness < 0.3
      AND is_canonical = 0
    LIMIT 500
""", (cutoff,)).fetchall()

print(f"Stale chunks found: {len(stale)}")

# Derank stale chunks
deranked = 0
for (chunk_id, skill, topics, pub, freshness) in stale:
    conn.execute("UPDATE chunks SET freshness = 0.0 WHERE chunk_id = ?", (chunk_id,))
    deranked += 1

conn.commit()
print(f"Deranked: {deranked} stale chunks")

# Step 2: Dedup — same skill + same heading
dupes = conn.execute("""
    SELECT skill, heading, COUNT(*) as cnt, MIN(chunk_id) as keep_id
    FROM chunks
    WHERE heading != '' AND is_canonical = 0
    GROUP BY skill, heading
    HAVING cnt > 1
    LIMIT 200
""").fetchall()

print(f"Duplicate groups found: {len(dupes)}")

deduped = 0
for (skill, heading, cnt, keep_id) in dupes:
    # Derank all but the newest (highest freshness)
    result = conn.execute("""
        SELECT chunk_id FROM chunks
        WHERE skill = ? AND heading = ? AND chunk_id != ? AND is_canonical = 0
        ORDER BY freshness ASC
    """, (skill, heading, keep_id)).fetchall()

    for (dup_id,) in result:
        conn.execute("UPDATE chunks SET freshness = 0.01 WHERE chunk_id = ?", (dup_id,))
        deduped += 1

conn.commit()
print(f"Deduped: {deduped} duplicate chunks deranked")

# Step 3: Stats
total = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
active = conn.execute("SELECT COUNT(*) FROM chunks WHERE freshness > 0.05").fetchone()[0]
print(f"DB stats — total: {total:,} | active: {active:,} | noise: {total-active:,}")

conn.close()
PYTHON

# Step 4: Sync snapshot
echo "[$(date)] Syncing portable snapshot..." | tee -a "$LOG"
cp "$DB" "$SNAPSHOT"
SNAP_SIZE=$(du -sh "$SNAPSHOT" | cut -f1)
echo "[$(date)] Snapshot synced — size: $SNAP_SIZE" | tee -a "$LOG"

echo "[$(date)] Memory compress complete" | tee -a "$LOG"
