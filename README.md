# Squad Memory

Local hybrid retriever for Codex skills and memory.

## SEO Elite Dashboard

Run the local realtime control room for the elite SEO memory system:

```bash
zsh /Users/vijaychauhan/squad_memory/run_seo_elite_dashboard.sh 8791
```

Then open:

```text
http://127.0.0.1:8791
```

The dashboard shows:
- chunk growth and path growth over time
- active jobs and pipeline status
- pending harvest queue and top pending sources
- source snapshot coverage and top article sources
- recent knowledge landing in live, archive, and primary memory
- log tails for bulk backfill, article harvest, and primary refresh

## OpenClaw SEO Automation

The shell cron layer keeps the SEO Elite data engine fresh, and the OpenClaw layer turns that live status into internal SEO briefs inside the OpenClaw SEO workspace.

Refresh the OpenClaw SEO automation artifacts:

```bash
python3 /Users/vijaychauhan/squad_memory/refresh_openclaw_seo_automation.py
```

Install the managed OpenClaw SEO cron jobs:

```bash
python3 /Users/vijaychauhan/squad_memory/install_openclaw_seo_cron.py
```

Generated workspace paths:
- `~/.openclaw/workspace/squad/seo/automation/data/latest-status.json`
- `~/.openclaw/workspace/squad/seo/automation/digest/latest.md`
- `~/.openclaw/workspace/squad/seo/automation/outbox/watchtower-latest.md`
- `~/.openclaw/workspace/squad/seo/automation/outbox/opportunity-radar.md`
- `~/.openclaw/workspace/squad/seo/automation/outbox/daily-ops-plan.md`

## What It Does

- Runs a 30-phase knowledge factory and control-plane pipeline for trusted SEO and squad-content sources
- Stores raw feed snapshots, run manifests, and ingestion state for reproducible source monitoring
- Indexes installed skills and memory notes from `~/.codex/skills`
- Stores chunks in SQLite FTS5 for fast text search
- Adds a dependency-free sparse TF-IDF reranker
- Adds a stored semantic vector layer built from corpus co-occurrence embeddings
- Chunks notes by semantic sections such as concepts, frameworks, stats, and checklists
- Reads structured note frontmatter such as `topic`, `intent`, `role`, `use_for`, `avoid_for`, `confidence`, and `canonical`
- Supports role-aware boosts and bundle metadata using:
  - `seo/MEMORY.md` for SEO memory routing
  - `SQUAD_MEMORY.md` for cross-skill role bundles and skill tags
- Tracks sources like Ahrefs, Hobo, and DEJAN for better retrieval and routing
- Helps Pinchy suggest which skills and memory to use for a task
- Resolves reusable task packs for recurring squad workflows
- Builds execution plans with checklists, deliverables, handoffs, and escalation rules
- Logs retrieval usage and accepts feedback for future tuning
- Learns path and skill priors from repeated usage patterns
- Suggests frontmatter improvements from real squad behavior
- Rebuilds atomically so live queries do not hit a half-built database

## Commands

Run the Phase 1 ingest pipeline:

```bash
python3 /Users/vijaychauhan/squad_memory/knowledge_ingest.py run \
  --config /Users/vijaychauhan/squad_memory/knowledge_sources.json \
  --output-dir /Users/vijaychauhan/.codex/skills/seo/memory \
  --summary-path /Users/vijaychauhan/.codex/skills/seo/memory/live-knowledge-monitor.md \
  --snapshot-dir /Users/vijaychauhan/squad_memory/ingest/raw \
  --runs-dir /Users/vijaychauhan/squad_memory/ingest/runs \
  --state-path /Users/vijaychauhan/squad_memory/ingest/state.json \
  --top 10 \
  --build-db
```

Inspect the latest ingest state:

```bash
python3 /Users/vijaychauhan/squad_memory/knowledge_ingest.py report --json
```

Run Phase 2 canonicalization:

```bash
python3 /Users/vijaychauhan/squad_memory/phase2_canonicalize.py
```

Run Phase 3 clustering and eval gate:

```bash
python3 /Users/vijaychauhan/squad_memory/phase3_cluster_refresh.py
```

Run Phase 4 router refresh and rebuild:

```bash
python3 /Users/vijaychauhan/squad_memory/phase4_router_refresh.py \
  --build-db
```

Run Phase 5 durable-note promotion drafting:

```bash
python3 /Users/vijaychauhan/squad_memory/phase5_promote_memory.py
```

Run Phase 6 approved promotion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase6_promote_approved.py
```

Run Phase 7 canonical synthesis and decay control:

```bash
python3 /Users/vijaychauhan/squad_memory/phase7_merge_canon.py
```

Run Phase 8 orphan-primary canonical promotion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase8_promote_canon.py
```

Run Phase 9 topic redistribution and canonical summary merge:

```bash
python3 /Users/vijaychauhan/squad_memory/phase9_merge_summaries.py
```

Run Phase 10 cross-source evidence fusion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase10_fuse_evidence.py
```

Run Phase 11 writer and marketing canon bootstrap:

```bash
python3 /Users/vijaychauhan/squad_memory/phase11_bootstrap_writer_marketing.py
```

Run Phase 12 writer and marketing external source fusion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase12_external_writer_marketing.py \
  --config /Users/vijaychauhan/squad_memory/knowledge_sources_writer_marketing.json
```

Run Phase 13 writer and marketing durable-promotion drafting:

```bash
python3 /Users/vijaychauhan/squad_memory/phase13_promote_writer_marketing.py \
  --phase12-manifest /Users/vijaychauhan/squad_memory/ingest/phase12/latest.json
```

Run Phase 14 writer and marketing approved promotion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase14_promote_writer_marketing_approved.py \
  --phase13-manifest /Users/vijaychauhan/squad_memory/ingest/phase13/latest.json
```

Run Phase 15 real-task telemetry and outcome learning:

```bash
python3 /Users/vijaychauhan/squad_memory/phase15_outcome_telemetry.py
```

Run Phase 16 Charles canon bootstrap:

```bash
python3 /Users/vijaychauhan/squad_memory/phase16_bootstrap_charles.py
```

Run Phase 17 Charles external source fusion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase17_external_charles.py \
  --config /Users/vijaychauhan/squad_memory/knowledge_sources_charles.json
```

Run Phase 18 Charles durable-promotion drafting:

```bash
python3 /Users/vijaychauhan/squad_memory/phase18_promote_charles.py \
  --phase17-manifest /Users/vijaychauhan/squad_memory/ingest/phase17/latest.json
```

Run Phase 19 Charles approved promotion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase19_promote_charles_approved.py \
  --phase18-manifest /Users/vijaychauhan/squad_memory/ingest/phase18/latest.json
```

Run Phase 20 Charles queue triage:

```bash
python3 /Users/vijaychauhan/squad_memory/phase20_triage_charles_queue.py \
  --phase19-manifest /Users/vijaychauhan/squad_memory/ingest/phase19/latest.json
```

Run Phase 21 control-plane report:

```bash
python3 /Users/vijaychauhan/squad_memory/phase21_control_plane.py report
```

Apply queue actions from the control plane:

```bash
python3 /Users/vijaychauhan/squad_memory/phase21_control_plane.py queue-action \
  --domain charles \
  --approve buffer-best-content-format-on-social-platforms-in-2026-45m-posts-analyzed.md \
  --build-db
```

Retrain learning priors and refresh the control-plane report:

```bash
python3 /Users/vijaychauhan/squad_memory/phase21_control_plane.py retrain
```

Run Phase 22 support bootstrap:

```bash
python3 /Users/vijaychauhan/squad_memory/phase22_bootstrap_support.py
```

Run Phase 23 support external-source fusion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase23_external_support.py
```

Run Phase 24 developer and QA bootstrap:

```bash
python3 /Users/vijaychauhan/squad_memory/phase24_bootstrap_dev_qa.py
```

Run Phase 25 developer and QA external-source fusion:

```bash
python3 /Users/vijaychauhan/squad_memory/phase25_external_dev_qa.py
```

Run Phase 26 developer and QA promotion drafting:

```bash
python3 /Users/vijaychauhan/squad_memory/phase26_promote_dev_qa.py
```

Run Phase 27 developer and QA approval gate:

```bash
python3 /Users/vijaychauhan/squad_memory/phase27_promote_dev_qa_approved.py
```

Run Phase 28 developer and QA queue triage:

```bash
python3 /Users/vijaychauhan/squad_memory/phase28_triage_dev_qa_queue.py
```

Run Phase 29 task result evaluation:

```bash
python3 /Users/vijaychauhan/squad_memory/phase29_task_result_eval.py
```

Run Phase 30 scorecard-driven learning:

```bash
python3 /Users/vijaychauhan/squad_memory/phase30_scorecard_learning.py
```

Build the 3D squad graph snapshot against the SEO elite DB:

```bash
python3 /Users/vijaychauhan/squad_memory/phase31_memory_graph.py build
```

Serve the live 3D squad graph locally on the SEO elite DB:

```bash
python3 /Users/vijaychauhan/squad_memory/phase31_memory_graph.py serve --port 8765
```

Run the full locked pipeline wrapper:

```bash
python3 /Users/vijaychauhan/squad_memory/phase_pipeline.py
```

Build the index:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py build
```

Query memory:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py query "ai visibility brand mentions" --role pinchy --top 8
```

Recommend skills for a task:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py decide "Need a plan for AI visibility, brand mentions, and AIO traffic loss" --role pinchy --top 5
```

Produce a Pinchy-style plan:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py pinchy "Need a plan for AI visibility, brand mentions, and AIO traffic loss" --top 5
```

Resolve the best task pack:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py task-pack "Need to coordinate writer, SEO, and marketing for a launch and keep the handoffs clean" --role pinchy --top 5
```

Build an execution plan from that pack:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py execute-plan "Need a regression test plan and pass-fail gate before deployment" --top 5
```

Record the outcome of a completed pack:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py complete-task "Need a regression test plan and pass-fail gate before deployment" --status accepted --user-rating 5 --completion-minutes 18
```

Record feedback:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py feedback "Need a plan for AI visibility" "seo/memory/ahrefs-ai-visibility-guide.md" --rating useful
```

Inspect recent logs:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py logs --limit 20
```

Train learned priors from logs and feedback:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py train
```

Show usage-learning report:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py report --limit 10
```

Train pack priors from completed task outcomes:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py pack-train
```

Show pack outcome report:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py pack-report --limit 10
```

Train outcome priors from completed tasks:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py outcome-train
```

Show outcome telemetry report:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py outcome-report --limit 10
```

Train scorecard-driven priors from reviewed task-result scorecards:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py result-train
```

Suggest metadata updates from usage:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py suggest-metadata --limit 8
```

Run the evaluation fixtures:

```bash
python3 /Users/vijaychauhan/squad_memory/squad_memory.py eval
```

Run the ingestion E2E test:

```bash
python3 -m unittest /Users/vijaychauhan/squad_memory/tests/test_knowledge_ingest_e2e.py
```

## Knowledge Factory Pipeline

The pipeline is split into 31 phases:

- [knowledge_ingest.py](/Users/vijaychauhan/squad_memory/knowledge_ingest.py)
- [phase2_canonicalize.py](/Users/vijaychauhan/squad_memory/phase2_canonicalize.py)
- [phase3_cluster_refresh.py](/Users/vijaychauhan/squad_memory/phase3_cluster_refresh.py)
- [phase4_router_refresh.py](/Users/vijaychauhan/squad_memory/phase4_router_refresh.py)
- [phase5_promote_memory.py](/Users/vijaychauhan/squad_memory/phase5_promote_memory.py)
- [phase6_promote_approved.py](/Users/vijaychauhan/squad_memory/phase6_promote_approved.py)
- [phase7_merge_canon.py](/Users/vijaychauhan/squad_memory/phase7_merge_canon.py)
- [phase8_promote_canon.py](/Users/vijaychauhan/squad_memory/phase8_promote_canon.py)
- [phase9_merge_summaries.py](/Users/vijaychauhan/squad_memory/phase9_merge_summaries.py)
- [phase10_fuse_evidence.py](/Users/vijaychauhan/squad_memory/phase10_fuse_evidence.py)
- [phase11_bootstrap_writer_marketing.py](/Users/vijaychauhan/squad_memory/phase11_bootstrap_writer_marketing.py)
- [phase12_external_writer_marketing.py](/Users/vijaychauhan/squad_memory/phase12_external_writer_marketing.py)
- [phase13_promote_writer_marketing.py](/Users/vijaychauhan/squad_memory/phase13_promote_writer_marketing.py)
- [phase14_promote_writer_marketing_approved.py](/Users/vijaychauhan/squad_memory/phase14_promote_writer_marketing_approved.py)
- [phase15_outcome_telemetry.py](/Users/vijaychauhan/squad_memory/phase15_outcome_telemetry.py)
- [phase16_bootstrap_charles.py](/Users/vijaychauhan/squad_memory/phase16_bootstrap_charles.py)
- [phase17_external_charles.py](/Users/vijaychauhan/squad_memory/phase17_external_charles.py)
- [phase18_promote_charles.py](/Users/vijaychauhan/squad_memory/phase18_promote_charles.py)
- [phase19_promote_charles_approved.py](/Users/vijaychauhan/squad_memory/phase19_promote_charles_approved.py)
- [phase20_triage_charles_queue.py](/Users/vijaychauhan/squad_memory/phase20_triage_charles_queue.py)
- [phase21_control_plane.py](/Users/vijaychauhan/squad_memory/phase21_control_plane.py)
- [phase22_bootstrap_support.py](/Users/vijaychauhan/squad_memory/phase22_bootstrap_support.py)
- [phase23_external_support.py](/Users/vijaychauhan/squad_memory/phase23_external_support.py)
- [phase24_bootstrap_dev_qa.py](/Users/vijaychauhan/squad_memory/phase24_bootstrap_dev_qa.py)
- [phase25_external_dev_qa.py](/Users/vijaychauhan/squad_memory/phase25_external_dev_qa.py)
- [phase26_promote_dev_qa.py](/Users/vijaychauhan/squad_memory/phase26_promote_dev_qa.py)
- [phase27_promote_dev_qa_approved.py](/Users/vijaychauhan/squad_memory/phase27_promote_dev_qa_approved.py)
- [phase28_triage_dev_qa_queue.py](/Users/vijaychauhan/squad_memory/phase28_triage_dev_qa_queue.py)
- [phase29_task_result_eval.py](/Users/vijaychauhan/squad_memory/phase29_task_result_eval.py)
- [phase30_scorecard_learning.py](/Users/vijaychauhan/squad_memory/phase30_scorecard_learning.py)
- [phase31_memory_graph.py](/Users/vijaychauhan/squad_memory/phase31_memory_graph.py)
- [phase_pipeline.py](/Users/vijaychauhan/squad_memory/phase_pipeline.py)
- [knowledge_sources.json](/Users/vijaychauhan/squad_memory/knowledge_sources.json)
- [knowledge_sources_writer_marketing.json](/Users/vijaychauhan/squad_memory/knowledge_sources_writer_marketing.json)
- [knowledge_sources_charles.json](/Users/vijaychauhan/squad_memory/knowledge_sources_charles.json)
- [knowledge_sources_support.json](/Users/vijaychauhan/squad_memory/knowledge_sources_support.json)
- [knowledge_sources_dev_qa.json](/Users/vijaychauhan/squad_memory/knowledge_sources_dev_qa.json)

What each phase does:

1. Phase 1 fetches trusted RSS or Atom sources, stores raw snapshots, and writes live source notes
2. Phase 2 turns live notes into source-level canonical notes and agent checklists
3. Phase 3 clusters those notes by topic, scores freshness, rebuilds the DB, and runs the eval gate
4. Phase 4 promotes approved live notes into `seo/MEMORY.md` and `seo/memory/INDEX.md`, then rebuilds the DB again
5. Phase 5 compares fresh live-source signals against the durable memory library, drafts promotion candidates into a staging area, and keeps a review queue with overlap checks and router suggestions
6. Phase 6 syncs a review file from Phase 5, promotes only explicitly approved drafts into the durable SEO memory library, refreshes dedicated router blocks, and rebuilds the DB only when new durable notes are added
7. Phase 7 builds a canonical topic registry, flags stale legacy notes, surfaces merge candidates, and writes a memory health report for ongoing decay control
8. Phase 8 auto-canonicalizes safe `orphan_primary` notes, skips manual-review edge cases, refreshes Phase 7, and rebuilds the DB so canonical metadata starts influencing retrieval immediately
9. Phase 9 reassigns old untagged durable notes into real topics, reruns Phase 8 if new safe orphan canon notes appear, and refreshes managed synthesis blocks on the primary canonical notes
10. Phase 10 builds a topic-level evidence ledger, fuses cross-source signals into canonical notes, and gives retrieval a stronger preference for high-confidence canon over raw overlap notes
11. Phase 11 bootstraps writer and marketing operating canon notes from the existing local memory so non-SEO retrieval gets the same canon-first behavior as SEO
12. Phase 12 ingests trusted writer and marketing external sources, writes live source canons, fuses those signals into domain external canons, and updates the operating canon with fresh-source guidance
13. Phase 13 compares fresh writer and marketing source signals against the current durable library, drafts strong candidates into a review queue, and keeps durable growth separate from raw feed monitoring
14. Phase 14 syncs a review file from Phase 13, promotes only explicitly approved writer and marketing drafts into durable memory, refreshes router blocks, and rebuilds the DB only when the durable library changes
15. Phase 15 retrains telemetry from real completed tasks, writes an outcome ledger, flags over-ranked and underused notes, and produces a human-readable report for pack and note performance
16. Phase 16 bootstraps Charles into a dedicated social-domain canon, adds a Charles router plus squad-router bundle references, and writes a Charles evidence ledger so social retrieval stops leaning on marketing by default
17. Phase 17 ingests trusted Charles external sources, writes source canons plus a Charles external canon, and fuses fresh creator and platform signals into the Charles operating canon
18. Phase 18 compares fresh Charles source signals against the durable Charles library, drafts high-signal candidates into a review queue, and keeps durable growth separate from raw social-source monitoring
19. Phase 19 syncs a review file from Phase 18, promotes only explicitly approved Charles drafts into durable memory, refreshes a Charles approved-promotions router block, and rebuilds the DB only when new durable notes are added
20. Phase 20 triages the held Charles queue into `approve_suggested`, `hold`, or `reject_suggested`, writes recommendation metadata back into the review state, and keeps approval support separate from the actual approval gate
21. Phase 21 aggregates queues, source health, memory health, and learning signals into one control-plane report and exposes queue actions plus retraining from a single entry point
22. Phase 22 bootstraps Anemone into a dedicated support canon, adds a support router plus squad-router bundle references, and writes a support evidence ledger so support retrieval stops leaning on generic docs by default
23. Phase 23 ingests trusted support external sources, writes source canons plus a support external canon, and fuses fresh support-system and help-center signals into the Anemone operating canon
24. Phase 24 bootstraps Chitin and Reef into dedicated developer and QA canons, creates domain routers plus squad-router references, and writes evidence ledgers so implementation and QA retrieval stop leaning only on generic role-pack docs
25. Phase 25 ingests trusted developer and QA external sources, writes source canons plus developer and QA external canons, and fuses fresh engineering and testing signals into the Chitin and Reef operating canons
26. Phase 26 compares fresh developer and QA source signals against the durable library, drafts strong candidates into a shared review queue, and keeps durable growth separate from raw engineering and testing monitoring
27. Phase 27 syncs a review file from Phase 26, promotes only explicitly approved developer and QA drafts into durable memory, refreshes router blocks, and rebuilds the DB only when new durable notes are added
28. Phase 28 triages the held developer and QA queue into `approve_suggested`, `hold`, or `reject_suggested`, writes recommendation metadata back into the review state, and keeps approval support separate from the actual approval gate
29. Phase 29 syncs structured scorecard suggestions onto completed tasks, writes a pending-review queue for manual output scoring, and surfaces output-quality trends by pack, path, and skill
30. Phase 30 trains pack, path, and skill priors from structured scorecards, writes a scorecard-learning report, and lets reviewed output quality start affecting retrieval and pack choice

Current source registry includes:

- Ahrefs
- Hobo
- DEJAN
- Google Search Central
- Search Engine Land
- Search Engine Roundtable
- Search Engine Journal
- Brodie Clark
- GSQi
- Marie Haynes
- Lily Ray
- Cindy Krum / MobileMoxie
- iPullRank
- Aleyda Solis
- Jono Alderson

Phase 12 external source registry includes:

- Copyblogger
- Content Marketing Institute
- Ann Handley
- Seth's Blog
- Copyhackers
- Buffer
- HubSpot Marketing Blog
- Social Media Examiner
- MarketingProfs
- Hootsuite

Phase 17 Charles source registry includes:

- Buffer
- Hootsuite
- Social Media Examiner

Phase 23 support source registry includes:

- Help Scout
- Intercom
- Zendesk

Phase 25 developer and QA source registry includes:

- Martin Fowler
- thoughtbot
- GitHub Engineering
- Playwright Releases
- Cypress Releases
- Cypress Blog

## Cron

Cron assets live in [cron](/Users/vijaychauhan/squad_memory/cron).

- Reference phase schedules: [phase1_ingest.cron](/Users/vijaychauhan/squad_memory/cron/phase1_ingest.cron), [phase2_canonicalize.cron](/Users/vijaychauhan/squad_memory/cron/phase2_canonicalize.cron), [phase3_cluster_refresh.cron](/Users/vijaychauhan/squad_memory/cron/phase3_cluster_refresh.cron), [phase4_router_refresh.cron](/Users/vijaychauhan/squad_memory/cron/phase4_router_refresh.cron), [phase5_promote_memory.cron](/Users/vijaychauhan/squad_memory/cron/phase5_promote_memory.cron), [phase6_promote_approved.cron](/Users/vijaychauhan/squad_memory/cron/phase6_promote_approved.cron), [phase7_merge_canon.cron](/Users/vijaychauhan/squad_memory/cron/phase7_merge_canon.cron), [phase8_promote_canon.cron](/Users/vijaychauhan/squad_memory/cron/phase8_promote_canon.cron), [phase9_merge_summaries.cron](/Users/vijaychauhan/squad_memory/cron/phase9_merge_summaries.cron), [phase10_fuse_evidence.cron](/Users/vijaychauhan/squad_memory/cron/phase10_fuse_evidence.cron), [phase11_bootstrap_writer_marketing.cron](/Users/vijaychauhan/squad_memory/cron/phase11_bootstrap_writer_marketing.cron), [phase12_external_sources.cron](/Users/vijaychauhan/squad_memory/cron/phase12_external_sources.cron), [phase13_promote_writer_marketing.cron](/Users/vijaychauhan/squad_memory/cron/phase13_promote_writer_marketing.cron), [phase14_promote_writer_marketing_approved.cron](/Users/vijaychauhan/squad_memory/cron/phase14_promote_writer_marketing_approved.cron), [phase15_outcome_telemetry.cron](/Users/vijaychauhan/squad_memory/cron/phase15_outcome_telemetry.cron), [phase16_bootstrap_charles.cron](/Users/vijaychauhan/squad_memory/cron/phase16_bootstrap_charles.cron), [phase17_external_charles.cron](/Users/vijaychauhan/squad_memory/cron/phase17_external_charles.cron), [phase18_promote_charles.cron](/Users/vijaychauhan/squad_memory/cron/phase18_promote_charles.cron), [phase19_promote_charles_approved.cron](/Users/vijaychauhan/squad_memory/cron/phase19_promote_charles_approved.cron), [phase20_triage_charles_queue.cron](/Users/vijaychauhan/squad_memory/cron/phase20_triage_charles_queue.cron), [phase21_control_plane.cron](/Users/vijaychauhan/squad_memory/cron/phase21_control_plane.cron), [phase22_bootstrap_support.cron](/Users/vijaychauhan/squad_memory/cron/phase22_bootstrap_support.cron), [phase23_external_support.cron](/Users/vijaychauhan/squad_memory/cron/phase23_external_support.cron), [phase24_bootstrap_dev_qa.cron](/Users/vijaychauhan/squad_memory/cron/phase24_bootstrap_dev_qa.cron), [phase25_external_dev_qa.cron](/Users/vijaychauhan/squad_memory/cron/phase25_external_dev_qa.cron), [phase26_promote_dev_qa.cron](/Users/vijaychauhan/squad_memory/cron/phase26_promote_dev_qa.cron), [phase27_promote_dev_qa_approved.cron](/Users/vijaychauhan/squad_memory/cron/phase27_promote_dev_qa_approved.cron), [phase28_triage_dev_qa_queue.cron](/Users/vijaychauhan/squad_memory/cron/phase28_triage_dev_qa_queue.cron), [phase29_task_result_eval.cron](/Users/vijaychauhan/squad_memory/cron/phase29_task_result_eval.cron), [phase30_scorecard_learning.cron](/Users/vijaychauhan/squad_memory/cron/phase30_scorecard_learning.cron)
- Combined crontab: [phase_pipeline.crontab](/Users/vijaychauhan/squad_memory/cron/phase_pipeline.crontab)

Runnable wrappers live at:

- [run_phase1_ingest.sh](/Users/vijaychauhan/squad_memory/run_phase1_ingest.sh)
- [run_phase2_canonicalize.sh](/Users/vijaychauhan/squad_memory/run_phase2_canonicalize.sh)
- [run_phase3_cluster_refresh.sh](/Users/vijaychauhan/squad_memory/run_phase3_cluster_refresh.sh)
- [run_phase4_router_refresh.sh](/Users/vijaychauhan/squad_memory/run_phase4_router_refresh.sh)
- [run_phase5_promote_memory.sh](/Users/vijaychauhan/squad_memory/run_phase5_promote_memory.sh)
- [run_phase6_promote_approved.sh](/Users/vijaychauhan/squad_memory/run_phase6_promote_approved.sh)
- [run_phase7_merge_canon.sh](/Users/vijaychauhan/squad_memory/run_phase7_merge_canon.sh)
- [run_phase8_promote_canon.sh](/Users/vijaychauhan/squad_memory/run_phase8_promote_canon.sh)
- [run_phase9_merge_summaries.sh](/Users/vijaychauhan/squad_memory/run_phase9_merge_summaries.sh)
- [run_phase10_fuse_evidence.sh](/Users/vijaychauhan/squad_memory/run_phase10_fuse_evidence.sh)
- [run_phase11_bootstrap_writer_marketing.sh](/Users/vijaychauhan/squad_memory/run_phase11_bootstrap_writer_marketing.sh)
- [run_phase12_external_sources.sh](/Users/vijaychauhan/squad_memory/run_phase12_external_sources.sh)
- [run_phase13_promote_writer_marketing.sh](/Users/vijaychauhan/squad_memory/run_phase13_promote_writer_marketing.sh)
- [run_phase14_promote_writer_marketing_approved.sh](/Users/vijaychauhan/squad_memory/run_phase14_promote_writer_marketing_approved.sh)
- [run_phase15_outcome_telemetry.sh](/Users/vijaychauhan/squad_memory/run_phase15_outcome_telemetry.sh)
- [run_phase16_bootstrap_charles.sh](/Users/vijaychauhan/squad_memory/run_phase16_bootstrap_charles.sh)
- [run_phase17_external_charles.sh](/Users/vijaychauhan/squad_memory/run_phase17_external_charles.sh)
- [run_phase18_promote_charles.sh](/Users/vijaychauhan/squad_memory/run_phase18_promote_charles.sh)
- [run_phase19_promote_charles_approved.sh](/Users/vijaychauhan/squad_memory/run_phase19_promote_charles_approved.sh)
- [run_phase20_triage_charles_queue.sh](/Users/vijaychauhan/squad_memory/run_phase20_triage_charles_queue.sh)
- [run_phase21_control_plane.sh](/Users/vijaychauhan/squad_memory/run_phase21_control_plane.sh)
- [run_phase22_bootstrap_support.sh](/Users/vijaychauhan/squad_memory/run_phase22_bootstrap_support.sh)
- [run_phase23_external_support.sh](/Users/vijaychauhan/squad_memory/run_phase23_external_support.sh)
- [run_phase24_bootstrap_dev_qa.sh](/Users/vijaychauhan/squad_memory/run_phase24_bootstrap_dev_qa.sh)
- [run_phase25_external_dev_qa.sh](/Users/vijaychauhan/squad_memory/run_phase25_external_dev_qa.sh)
- [run_phase26_promote_dev_qa.sh](/Users/vijaychauhan/squad_memory/run_phase26_promote_dev_qa.sh)
- [run_phase27_promote_dev_qa_approved.sh](/Users/vijaychauhan/squad_memory/run_phase27_promote_dev_qa_approved.sh)
- [run_phase28_triage_dev_qa_queue.sh](/Users/vijaychauhan/squad_memory/run_phase28_triage_dev_qa_queue.sh)
- [run_phase29_task_result_eval.sh](/Users/vijaychauhan/squad_memory/run_phase29_task_result_eval.sh)
- [run_phase30_scorecard_learning.sh](/Users/vijaychauhan/squad_memory/run_phase30_scorecard_learning.sh)
- [run_phase_pipeline.sh](/Users/vijaychauhan/squad_memory/run_phase_pipeline.sh)
- [run_openclaw_sync.sh](/Users/vijaychauhan/squad_memory/run_openclaw_sync.sh)

The active cron setup now uses the locked wrapper:

- `17 */6 * * *` [run_phase_pipeline.sh](/Users/vijaychauhan/squad_memory/run_phase_pipeline.sh)

That wrapper now runs the thirty memory phases and then refreshes OpenClaw memory by mirroring the Codex SEO corpus into `~/.openclaw/workspace/memory/imports/codex` and backfilling `main.sqlite` plus `seo.sqlite`.

## Launchd Backup

macOS backup scheduler assets live here:

- [com.vijaychauhan.squad-memory.pipeline.plist](/Users/vijaychauhan/squad_memory/launchd/com.vijaychauhan.squad-memory.pipeline.plist)

Installed target:

- `/Users/vijaychauhan/Library/LaunchAgents/com.vijaychauhan.squad-memory.pipeline.plist`

The LaunchAgent runs:

- at login via `RunAtLoad`
- every day at `00:18`, `06:18`, `12:18`, and `18:18`

Both cron and launchd call the same locked wrapper, so duplicate executions are skipped safely.

Shared pipeline log:

- `/Users/vijaychauhan/squad_memory/logs/phase_pipeline.log`

## Phase 5 Promotion Queue

Phase 5 writes draft-only promotion candidates into:

- `/Users/vijaychauhan/squad_memory/ingest/phase5/drafts`
- `/Users/vijaychauhan/squad_memory/ingest/phase5/promotion-queue.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase5/latest.json`

Important:

- Phase 5 does not auto-insert drafted notes into the live SEO memory library.
- It stages them with overlap checks, router suggestions, and a review-required gate.
- That keeps the library clean while still allowing the system to grow itself.

## Phase 6 Approval Gate

Phase 6 turns approved Phase 5 drafts into durable notes:

- `/Users/vijaychauhan/squad_memory/ingest/phase6/decisions.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase6/review-status.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase6/latest.json`

Important:

- Phase 6 is safe by default and does nothing to the live durable library until a draft is explicitly marked `approve`.
- Once approved, it writes the final durable note into `~/.codex/skills/seo/memory`, updates dedicated promoted-note router blocks, and rebuilds the DB.

## Phase 7 Canonical Synthesis

Phase 7 writes control-plane outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase7/canonical_registry.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase7/memory_health_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase7/latest.json`

Important:

- Phase 7 does not overwrite durable notes.
- It classifies notes into canonical, supporting, merge-candidate, monitor, orphan, and stale states.
- `squad_memory.py` reads this registry during ranking so stale legacy feed notes are demoted and canonical topic notes are preferred more reliably.

## Phase 8 Canonical Promotion

Phase 8 writes promotion outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase8/canonical_promotion_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase8/latest.json`

Important:

- Phase 8 only auto-canonicalizes `orphan_primary` notes that already have a real topic.
- It skips ambiguous notes like `__untagged__` topics for manual review.
- After any changes, it refreshes Phase 7 and rebuilds the DB so the new canonical metadata affects ranking immediately.

## Phase 9 Canonical Summary Merge

Phase 9 writes synthesis outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase9/canonical_summary_merge_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase9/latest.json`

Important:

- Phase 9 reassigns old untagged durable notes into existing topic clusters using local heuristics plus similarity to healthy canonical primaries.
- It reuses Phase 8 automatically if those topic reassignments create new safe orphan primaries.
- It refreshes managed `phase9` digest blocks on the primary canonical notes so overlapping supporting notes get compressed into the canon layer.

## Phase 10 Evidence Fusion

Phase 10 writes evidence outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase10/evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase10/evidence_fusion_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase10/latest.json`

Important:

- Phase 10 builds a topic-level evidence ledger from the healthy canonical registry.
- It writes managed `phase10` fusion blocks onto the primary canonical notes with cross-source signals, consensus, tension, and squad action guidance.
- `squad_memory.py` reads the ledger during ranking so high-confidence fused canon notes get a small additional boost over raw overlap notes.

## Phase 11 Writer + Marketing Bootstrap

Phase 11 writes bootstrap outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase11/writer_evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase11/marketing_evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase11/writer_marketing_bootstrap_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase11/latest.json`

Important:

- Phase 11 creates domain-level canon notes for `writer` and `marketing` from the existing local memory.
- It updates [writer/MEMORY.md](/Users/vijaychauhan/.codex/skills/writer/MEMORY.md) and [marketing/MEMORY.md](/Users/vijaychauhan/.codex/skills/marketing/MEMORY.md) so those canon notes become the first routing entry points.
- `squad_memory.py` reads the Phase 11 ledgers during ranking so broad writing and marketing tasks can hit the new domain canon before narrower format notes.

## Phase 12 Writer + Marketing External Sources

Phase 12 writes external-source outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase12/writer_external_evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase12/marketing_external_evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase12/writer_marketing_external_sources_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase12/latest.json`

Important:

- Phase 12 fetches trusted writer and marketing feeds, writes live source notes and source canons into the `writer` and `marketing` memory folders, and creates domain-level external source canons.
- It updates the Phase 11 operating canons with managed `phase12` external-source fusion blocks so the squad knows when to use fresh examples without replacing the base workflow.
- `squad_memory.py` reads the Phase 12 ledgers during ranking so queries asking for fresh examples, recent patterns, or source-backed ideas can hit the new external canons first.

## Phase 13 Writer + Marketing Promotion Queue

Phase 13 writes durable-promotion outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase13/promotion-queue.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase13/drafts/`
- `/Users/vijaychauhan/squad_memory/ingest/phase13/latest.json`

Important:

- Phase 13 reads the Phase 12 live source notes, scores freshness, novelty, and durable signal strength, then drafts only the strongest writer and marketing candidates into a review queue.
- It compares those candidates against the existing durable format notes so obvious overlap does not keep getting re-drafted.
- This keeps fresh external monitoring separate from durable knowledge growth, which is the same protection pattern the SEO side uses.

## Phase 14 Writer + Marketing Approved Promotion

Phase 14 writes approval outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase14/decisions.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase14/review-status.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase14/latest.json`

Important:

- Phase 14 defaults every Phase 13 draft to `hold`.
- It promotes only explicitly approved writer and marketing drafts into the live durable memory folders.
- It refreshes the relevant router blocks in [writer/MEMORY.md](/Users/vijaychauhan/.codex/skills/writer/MEMORY.md) and [marketing/MEMORY.md](/Users/vijaychauhan/.codex/skills/marketing/MEMORY.md) only after a promotion actually clears review.

## Phase 15 Outcome Telemetry

Phase 15 writes telemetry outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase15/outcome_telemetry_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase15/outcome_telemetry_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase15/latest.json`

Important:

- Phase 15 retrains outcome priors from real completed tasks.
- It surfaces strongest notes, weak notes, over-ranked paths, underused winners, strong skill stacks, and high-revision packs.
- It gives the wrapper a durable telemetry phase instead of leaving outcome learning trapped inside ad hoc CLI calls.

## Phase 16 Charles Bootstrap

Phase 16 writes Charles bootstrap outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase16/charles_evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase16/charles_bootstrap_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase16/latest.json`

Important:

- Phase 16 creates a dedicated `charles/memory` operating canon instead of relying on marketing notes alone.
- It writes [charles/MEMORY.md](/Users/vijaychauhan/.codex/skills/charles/MEMORY.md) and updates [SQUAD_MEMORY.md](/Users/vijaychauhan/.codex/skills/SQUAD_MEMORY.md) bundle references for Pinchy, Plankton, Charles, and Current.
- Retrieval reads the Charles evidence ledger so social, engagement, posting, and calendar queries get a small domain-specific boost toward Charles canon notes.

## Phase 17 Charles External Sources

Phase 17 writes Charles external-source outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase17/charles_external_evidence_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase17/charles_external_sources_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase17/latest.json`

Important:

- Phase 17 creates [charles-external-source-canon-2026.md](/Users/vijaychauhan/.codex/skills/charles/memory/charles-external-source-canon-2026.md) from trusted social and creator sources.
- It writes live source notes and live source canons inside [charles/memory](/Users/vijaychauhan/.codex/skills/charles/memory), then updates [charles-operating-canon-2026.md](/Users/vijaychauhan/.codex/skills/charles/memory/charles-operating-canon-2026.md) with a managed Phase 17 fusion block.
- Retrieval reads the Charles external evidence ledger so fresh-example and platform-change queries can prefer Charles external canon before generic marketing examples.

## Phase 18 Charles Promotion Drafting

Phase 18 writes Charles promotion-drafting outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase18/promotion-queue.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase18/drafts/`
- `/Users/vijaychauhan/squad_memory/ingest/phase18/latest.json`

Important:

- Phase 18 reads the fresh Charles live-source notes created by Phase 17 and compares them against the existing durable Charles library.
- It stages high-signal social or creator candidates into a review queue without modifying the live durable Charles memory.
- It suggests placement against [platform-native-posting-system.md](/Users/vijaychauhan/.codex/skills/charles/memory/platform-native-posting-system.md), [community-engagement-loop.md](/Users/vijaychauhan/.codex/skills/charles/memory/community-engagement-loop.md), or [social-calendar-and-trend-radar.md](/Users/vijaychauhan/.codex/skills/charles/memory/social-calendar-and-trend-radar.md).

## Phase 19 Charles Approved Promotion

Phase 19 writes Charles approval outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase19/decisions.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase19/review-status.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase19/latest.json`

Important:

- Phase 19 defaults every Phase 18 draft to `hold`.
- It promotes only explicitly approved Charles drafts into the live durable Charles memory folder.
- It refreshes a dedicated approved-promotions block inside [charles/MEMORY.md](/Users/vijaychauhan/.codex/skills/charles/MEMORY.md) only after a promotion actually clears review.

## Phase 20 Charles Queue Triage

Phase 20 writes Charles triage outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase20/triage.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase20/triage-report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase20/latest.json`

Important:

- Phase 20 does not change `status` in the approval gate.
- It annotates held queue items in [decisions.json](/Users/vijaychauhan/squad_memory/ingest/phase19/decisions.json) with `triage_recommendation`, `triage_priority`, `triage_score`, and reasoning.
- It is intentionally opinionated about queue hygiene, so generic stats/news/listicle social items can be marked `reject_suggested` while stronger workflow or platform-pattern notes get `approve_suggested`.

## Phase 28 Developer and QA Queue Triage

Phase 28 writes Developer + QA triage outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase28/triage.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase28/triage-report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase28/latest.json`

Important:

- Phase 28 does not change `status` in the approval gate.
- It annotates held queue items in [decisions.json](/Users/vijaychauhan/squad_memory/ingest/phase27/decisions.json) with `triage_recommendation`, `triage_priority`, `triage_score`, and reasoning.
- It is intentionally opinionated about queue hygiene, so durable workflow and testing-pattern notes can be marked `approve_suggested` while narrow release notes, digests, or anecdotal items can be marked `reject_suggested`.

## Phase 29 Task Result Evaluation

Phase 29 writes task result scoring outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase29/task_result_eval_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase29/task_result_eval_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase29/scorecard_review_queue.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase29/latest.json`

Important:

- Phase 29 syncs `suggested` scorecards onto completed tasks that do not already have a manual scorecard.
- It does not overwrite `manual` scorecards.
- It gives the squad a pending-review queue for output-quality evaluation by pack, path, and skill.

## Phase 30 Scorecard Learning

Phase 30 writes scorecard-learning outputs into:

- `/Users/vijaychauhan/squad_memory/ingest/phase30/scorecard_learning_ledger.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase30/scorecard_learning_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase30/latest.json`

Important:

- Phase 30 trains learned pack, path, and skill priors from structured task-result scorecards.
- `manual` scorecards have more weight than `suggested` scorecards.
- The resulting priors feed retrieval and pack selection so reviewed output quality can change future routing.

## Phase 31 Memory Graph

Phase 31 writes the 3D graph snapshot into:

- `/Users/vijaychauhan/squad_memory/ingest/phase31/memory_graph.json`
- `/Users/vijaychauhan/squad_memory/ingest/phase31/memory_graph_report.md`
- `/Users/vijaychauhan/squad_memory/ingest/phase31/latest.json`

Important:

- Phase 31 turns the live squad state into a graph payload of domains, queues, packs, skills, canon topics, primary notes, recent outcomes, and alerts.
- The default Phase 31 graph now points at `/Users/vijaychauhan/squad_memory/seo_elite_memory.db`.
- The local viewer lives in `/Users/vijaychauhan/squad_memory/memory_graph_ui`.
- Serve it with `python3 /Users/vijaychauhan/squad_memory/phase31_memory_graph.py serve --port 8765`.
- SEO elite runners now call `/Users/vijaychauhan/squad_memory/run_seo_elite_visual_refresh.sh`, which refreshes both the status dashboard and the Phase 31 graph in parallel after memory updates.

## MCP Wrapper

Codex can now call squad memory directly through the `squad_memory` MCP server configured in [config.toml](/Users/vijaychauhan/.codex/config.toml).

Available MCP tools:

- `memory_build`
- `memory_query`
- `memory_decide`
- `memory_pinchy`
- `memory_feedback`
- `memory_logs`
- `memory_train`
- `memory_report`
- `memory_complete_task`
- `memory_score_task`
- `memory_pack_train`
- `memory_pack_report`
- `memory_outcome_train`
- `memory_outcome_report`
- `memory_task_result_report`
- `memory_result_train`
- `memory_suggest_metadata`
- `memory_task_pack`
- `memory_execute_plan`

## Universal MCP Layer

The stack now also ships with a portable, vendor-neutral MCP server at [universal_memory_mcp_server.py](/Users/vijaychauhan/squad_memory/mcp/universal_memory_mcp_server.py).

This server is the next step toward a single memory/control-plane surface for:

- Codex CLI
- Claude Code
- Claude Desktop

Available tools:

- `memory_registry_overview`
- `memory_dataset_inspect`
- `memory_dataset_history`
- `memory_dataset_delta`
- `memory_run_ledger`
- `seo_patent_live_audit`
- `memory_federated_query`
- `memory_route_task`
- `memory_execution_plan`

Available prompts:

- `dataset_audit`
- `federated_analysis`
- `delta_explainer`
- `run_triage`
- `live_patent_site_audit`
- `system_improvement_brief`

Available resources:

- `memory://registry/overview`
- `memory://runs/ledger`
- `memory://prd/squad-memory-os`
- `memory://dataset/seo_elite`
- `memory://dataset/squad_memory`
- `memory://dataset/portable_snapshot`
- `memory://dataset/openclaw_main`
- `memory://dataset/openclaw_seo`
- `memory://dataset/{dataset_id}/history`
- `memory://dataset/{dataset_id}/delta`

What it does:

- exposes the dataset registry so clients can see which DB is being used
- exposes dataset history and explainable deltas so clients can answer what changed and compared to what
- exposes a live local run ledger so clients can inspect active jobs, recent fetch health, and linked stack state
- runs a live website audit over a smart page sample and maps findings to patent-backed SEO lenses
- auto-selects the best queryable dataset when no dataset is specified
- supports federated retrieval across `seo_elite`, `squad_memory`, and `portable_snapshot`
- turns routed tasks into reusable execution plans from the selected dataset
- exposes reusable prompts for recurring local workflows
- exposes inspectable resources so clients can browse the registry, PRD, dataset summaries, deltas, histories, and run state as first-class context

Manual live-audit entrypoint:

```bash
python3 /Users/vijaychauhan/squad_memory/live_patent_seo_audit.py https://example.com --json
```

Install helpers and config examples live in [/Users/vijaychauhan/squad_memory/mcp](/Users/vijaychauhan/squad_memory/mcp):

- [install_universal_mcp_for_codex.sh](/Users/vijaychauhan/squad_memory/mcp/install_universal_mcp_for_codex.sh)
- [install_universal_mcp_for_claude.sh](/Users/vijaychauhan/squad_memory/mcp/install_universal_mcp_for_claude.sh)
- [codex.config.toml.example](/Users/vijaychauhan/squad_memory/mcp/codex.config.toml.example)
- [claude-code.mcp.json.example](/Users/vijaychauhan/squad_memory/mcp/claude-code.mcp.json.example)
- [claude-desktop.mcp.json.example](/Users/vijaychauhan/squad_memory/mcp/claude-desktop.mcp.json.example)

## Design

This is intentionally hybrid, not vector-only:

1. SQLite FTS5 handles lexical recall
2. Pure-Python sparse TF-IDF reranks candidates
3. Router metadata from `seo/MEMORY.md` and `SQUAD_MEMORY.md` adds role, bundle, skill-tag, and canonical boosts
4. Corpus-trained token vectors create chunk-level semantic vectors for broader matching
5. Source, freshness, section-kind, and note frontmatter metadata refine ranking
6. Rebuilds use a temp DB + atomic swap and preserve `feedback` and `query_log`
7. Query-intent expansion improves paraphrase handling for tasks like AI visibility, reverse engineering, and support triage
8. Evaluation fixtures provide a repeatable quality benchmark
9. Usage training turns `query_log` + `feedback` into learned path and skill priors
10. Metadata suggestions turn repeated usage patterns into frontmatter upgrade proposals
11. Data-driven task packs turn recurring jobs into reusable operating workflows
12. Structured task-result scorecards separate output-quality review from raw outcome telemetry so the squad can learn from deliverable quality explicitly
12. Completed task outcomes train pack-level priors, path patterns, and skill patterns
13. Phase 7 canonical registry adds decay control and topic-level note-state adjustments during ranking
14. Phase 8 promotes safe orphan primaries into canonical notes so the registry can converge over time instead of staying in review mode
15. Phase 9 redistributes legacy untagged notes into real topics and refreshes managed summary digests on canonical primaries
16. Phase 10 fuses topic evidence across sources and nudges retrieval toward the strongest canonical note before raw overlap notes
17. Phase 11 bootstraps writer and marketing domain canon so non-SEO work also gets canon-first retrieval and routing
18. Phase 12 adds trusted external source ingest and canon fusion for writer and marketing so fresh examples and recent patterns route cleanly without polluting the core operating canons
19. Phase 13 adds a writer and marketing promotion queue so strong fresh source signals can move toward durable memory without auto-polluting the live library
20. Phase 14 adds the explicit approval gate for writer and marketing durable notes so the new domains get the same safe promotion model as SEO
21. Phase 15 turns completed task history into explicit outcome telemetry so real accepted vs revised work can influence note and skill learning over time
22. Phase 16 gives Charles a dedicated social canon and evidence ledger so creator-style social execution can route independently from generic marketing memory
23. Phase 17 gives Charles a trusted external-source layer so fresh creator examples, platform changes, and social research route through Charles instead of defaulting back to broad marketing canon
24. Phase 18 gives Charles a safe draft queue so strong fresh social-source signals can move toward durable Charles memory without auto-polluting the live library
25. Phase 19 adds the explicit approval gate for Charles durable notes so social-domain growth stays reviewed instead of being auto-promoted from fresh source noise
26. Phase 20 adds a recommendation layer on top of the Charles approval gate so the held queue stays high-signal without removing explicit human approval
27. Phase 21 adds a control plane so queue state, source health, memory health, and learning signals are inspectable from one place
28. Phase 22 bootstraps support canon so Anemone gets canon-first retrieval instead of leaning on generic docs
29. Phase 23 adds trusted support external-source fusion so fresh support-system and help-center signals route through Anemone cleanly
30. Phase 24 bootstraps developer and QA canon so Chitin and Reef stop leaning on generic role-pack docs for core implementation and validation tasks
31. Phase 25 adds trusted developer and QA external-source fusion so fresh engineering and testing signals route cleanly without displacing the core Chitin and Reef operating canons
32. Phase 26 adds a shared developer and QA promotion queue so strong external engineering and testing signals move toward durable memory without polluting the live library by default
33. Phase 27 adds the explicit approval gate for those developer and QA promotions so durable Dev/QA memory growth stays reviewed instead of auto-promoted
34. Phase 28 adds a triage layer on top of the held Dev/QA queue so stronger engineering and QA candidates are easier to approve without removing explicit human review
35. Phase 29 adds a real task-result scorecard layer so completed outputs can be reviewed for quality explicitly instead of relying only on status, revisions, and user rating
36. Phase 30 turns those scorecards into learned pack, path, and skill priors so reviewed output quality feeds future routing
37. Phase 31 projects the live squad state into a 3D graph surface so domains, queues, packs, topics, outcomes, and alerts can be inspected visually instead of only through reports

That makes it fast, inspectable, and dependency-free.

## Task Packs

Task packs live in [task_packs.json](/Users/vijaychauhan/squad_memory/task_packs.json). Each pack defines:

- primary skill
- supporting skills
- pack intents and keywords
- memory-focus terms
- execution checklist
- deliverables
- output sections
- handoff plan
- escalation rules

Current packs include:

- `ai_visibility_audit`
- `content_brief`
- `article_draft`
- `social_repurpose`
- `launch_coordination`
- `support_triage`
- `fact_check_brief`
- `code_review`
- `regression_gate`
- `incident_response`

Task outcomes are stored separately from retrieval feedback so the squad can learn from:

- `accepted`, `revised`, and `failed` runs
- revision counts
- completion time
- user rating
- paths and skills actually used inside the pack

## Frontmatter

High-value notes can declare structured retrieval hints in simple single-line frontmatter fields:

```yaml
---
topic: ai_visibility
intent: strategy, measurement, reporting
role: pinchy, coral, current
use_for: citations, brand_mentions, dashboards
avoid_for: customer_support, code_implementation
confidence: high
canonical: true
canonical_group: AI visibility strategy
---
```

These fields are used during:

1. candidate generation
2. sparse/vector ranking
3. canonical clustering
4. Pinchy theme extraction
5. metadata suggestion and cleanup workflows

## Next Upgrades

- Let historical feedback influence candidate generation, not just reranking
- Add parent-child chunk summaries and cross-links
- Add real embedding vectors on top of the current hybrid retriever
- Expand structured frontmatter beyond the current high-value note set
- Grow the evaluation fixtures until they cover every major squad workflow
