# SEO Elite + Squad Memory Next-Level PRD

Date created: Apr 24, 2026
Status: Draft
Last Mod: Apr 24, 2026

## Recommend

Vijay Chauhan + Codex

## Approve

Vijay + SEO Ops + Platform Engineering

## Perform (design/eng)

Platform Engineering + SEO Systems

## Input (optional)

SEO + Research + Ops + Automation

## Decide

Vijay + Platform Engineering

## = reviewed/approved

Pending

## Problem

### Definition

The current SEO memory stack is already powerful, but it behaves more like a collection of advanced subsystems than one coherent product.

Today the system includes:

- a freshness-first SEO Elite corpus and dashboard
- a broader Squad Memory corpus and routing engine
- a portable SEO vector snapshot used by MCP tooling
- a Phase 31 graph surface
- OpenClaw bridge sync and SEO automation outputs
- more than 30 memory pipeline phases and multiple shell runners

The system works, but the operator experience has four structural problems:

1. there is no single source of truth for "the current memory system"
2. dashboards and APIs are attached to different databases with similar names
3. pipeline state is observable, but not always explainable
4. the system can answer questions, but it cannot yet function as a first-class operating system for SEO research, decisioning, and action

The immediate symptom is trust friction.

On Apr 24, 2026, the local dashboard on `http://127.0.0.1:8788/` showed a lower chunk count than expected. The root cause was not a total data loss. The root cause was that the dashboard reads `seo_elite_memory.db`, while the operator was mentally comparing it to a broader memory database.

Current validated counts on Apr 24, 2026:

| Dataset | Path | Chunks | Distinct paths |
| --- | --- | ---: | ---: |
| SEO Elite dashboard DB | `/Users/vijaychauhan/squad_memory/seo_elite_memory.db` | `52,709` | `8,658` |
| Squad Memory DB | `/Users/vijaychauhan/squad_memory/squad_memory.db` | `70,200` | `9,657` |
| Portable SEO snapshot DB | `/Users/vijaychauhan/portable-repos/seo-vector-snapshot/db/squad_memory.db` | `63,670` | `8,973` |

The `8788` dashboard history itself never reached `72K`. Its recorded max in the current history log is `52,709` on Apr 24, 2026 at `17:02 IST`.

That means the real product problem is bigger than one dashboard number:

- dataset identity is ambiguous
- data lineage is not obvious from the UI
- the operator cannot immediately tell which surface reflects which corpus
- system health is visible, but system truth is not yet legible

### Target user

Primary user:

- Vijay as the system owner and operator who needs one trusted control plane for SEO memory, research ops, and agent automation

Secondary users:

- internal SEO agents and skills that depend on the right memory corpus
- platform maintainers debugging ingestion, sync, and rebuild issues
- future teammates or operators who need to run the stack without tribal knowledge

### Hypothesis

IF the current stack is turned into one named platform with a canonical data registry, unified control plane, explainable dataset boundaries, and action-oriented workflows,

THEN the operator will trust the system faster, debug it faster, and use it for higher-value planning rather than low-value count reconciliation,

AND this matters because the current system already has enough data, automation, and retrieval quality to become a real SEO operating system once the platform layer catches up.

### Impact

Choose: High

Why:

- the system already contains production-grade research assets
- operator trust issues block adoption more than data scarcity
- small platform improvements unlock much larger compounding value across ingestion, retrieval, and automation

Primary metric:

- `time to trusted answer for system health and corpus status`

Secondary metrics:

- `time to identify which database powers a given dashboard`
- `time to explain a chunk-count delta`
- `time to recover from a failed or partial refresh`
- `freshness lag from source discovery to indexed availability`
- `retrieval precision on key SEO tasks`
- `automation output usefulness as rated by the operator`

Safety metrics:

- `count mismatch incidents between UI and underlying DB`
- `stale dashboard snapshots served as fresh`
- `jobs running without ownership or lock visibility`
- `broken bridge syncs between SEO Elite and Squad Memory`
- `silent rebuild failures`

### Confidence

Choose: High for the platform problem, Medium-High for the solution shape

Evidence:

- the stack currently spans at least three materially different memory databases
- the main operator has already experienced confusion about chunk counts
- current dashboard code points to one DB while support tooling and bridge logs refer to others
- there are already enough logs, status files, and pipeline phases to justify a true control plane instead of more shell wrappers

## Solution

### Product vision

Turn the current memory stack into **Squad Memory OS**:

"one platform for trusted SEO intelligence, memory operations, agent routing, and action delivery."

This is not a request for prettier charts.

This is a platformization effort with four goals:

1. one source of truth for every memory dataset
2. one operator-grade control plane for state, lineage, and action
3. one orchestrated job system instead of scattered shell-driven workflows
4. one intelligence layer that can move from raw memory to ranked action

### What "next level" means

The next-level version of this system should let the operator answer the following questions in under 30 seconds:

- Which corpus am I looking at right now?
- Why did the chunk count change?
- Which pipeline run caused the change?
- Which sources, files, or imports were added or removed?
- What is stale, blocked, or broken?
- What are the highest-value SEO actions the system recommends right now?

It should also let the operator take the following actions from one place:

- refresh a dataset
- rebuild a corpus
- compare datasets
- inspect a run
- inspect a source
- inspect a query result
- publish a brief or mission output

### Product goals

#### Goal 1: Canonical Dataset Identity

Every DB, index, bridge import, and dashboard must have a stable identity, explicit label, and visible purpose.

#### Goal 2: Trusted Control Plane

The system must present current truth, historical truth, and delta explanations in one UI.

#### Goal 3: Orchestrated Operations

The system must move from shell wrappers plus implicit ordering to explicit jobs, dependencies, retries, and run artifacts.

#### Goal 4: Actionable Intelligence

The system must evolve from "memory and dashboards" to "memory, reasoning, prioritization, and action outputs."

### Non-goals

- replacing SQLite in the first milestone
- building a public multi-tenant SaaS product
- replacing all current pipelines before operator trust is fixed
- prioritizing visual polish over data clarity

## Current-State Readout

Validated on Apr 24, 2026:

- `seo_elite_memory.db`: `52,709` chunks
- `squad_memory.db`: `70,200` chunks
- portable snapshot `squad_memory.db`: `63,670` chunks
- `seo_elite` import corpus inside broader squad DB: `5,827` chunks
- Google patent-related chunks in SEO Elite DB: `92`

Current architectural shape:

- `seo_elite_memory.db` powers the SEO Elite status dashboard
- `squad_memory.db` powers broader role-routing and reusable task-pack memory
- the portable snapshot DB powers local MCP retrieval
- OpenClaw automation consumes outputs from the SEO Elite layer
- bridge sync moves SEO Elite content into the wider squad ecosystem

Current product gap:

- the system has a data plane
- the system has a workflow plane
- the system has a partial UI plane
- the system does not yet have a coherent platform plane

## Experience Principles

1. Truth over theater
2. Every number must have lineage
3. Every dataset must have a name and owner
4. Every refresh must produce an inspectable run artifact
5. Every UI card should answer "what changed?" or "what should I do?"
6. Operators should not need to remember file paths to understand state

## Core User Journeys

### Journey 1: Explain the Number

As the operator, I want to click a chunk count and immediately see:

- which DB it comes from
- how it changed versus the last run
- which paths, sources, or imports drove the delta
- whether the change was expected, suspicious, or destructive

### Journey 2: Run the Stack

As the operator, I want one command or button to run a full refresh plan with:

- job ordering
- locks
- retries
- visible progress
- structured outputs
- failure reasons

### Journey 3: Inspect Retrieval

As the operator, I want to test a query against each corpus and understand:

- why the result ranked
- which boosts fired
- which corpus should answer which class of question

### Journey 4: Publish Action

As the operator, I want the system to turn fresh evidence into:

- a same-day watchtower brief
- an opportunity radar
- a daily ops plan
- optional mission payloads for OpenClaw or Codex

## Requirements

### 1. Canonical Memory Registry

The platform must introduce a canonical dataset registry.

Each dataset entry must include:

- dataset id
- human label
- DB path
- purpose
- owner
- primary dashboards
- ingestion sources
- refresh command
- last build metadata
- expected count ranges

Required initial datasets:

- `seo_elite`
- `squad_memory`
- `portable_snapshot`
- `openclaw_main`
- `openclaw_seo`

### 2. Unified Control Plane

Create a new control plane dashboard that becomes the default entrypoint.

Required views:

- Overview
- Datasets
- Runs
- Sources
- Retrieval Lab
- Automation
- Graph
- Alerts

#### Overview view

Must show:

- all datasets side by side
- chunk counts, path counts, DB size, freshness, and status
- current active jobs
- last successful runs
- pending and failed items
- top actions to take now

#### Datasets view

Must show:

- dataset cards with exact DB paths
- purpose and ownership
- count history
- drift alerts
- import and export relationships
- "why this number changed" drilldown

#### Runs view

Must show:

- every executed refresh or build
- run id
- start and end timestamps
- dataset target
- phase breakdown
- outputs
- warnings
- failures

#### Retrieval Lab

Must support:

- one query across multiple corpora
- ranked results with lexical and semantic score components
- highlighted boosts and priors
- corpus recommendation for the query class

### 3. Run Orchestration Layer

Replace implicit shell choreography with a structured run engine.

Required capabilities:

- DAG-style job definitions
- run manifests
- idempotent execution
- resumable failed runs
- explicit locks
- retry policies
- structured logs
- run summaries

Initial orchestration targets:

- live sync
- primary refresh
- article harvest
- bulk backfill
- bridge sync
- graph rebuild
- status refresh

### 4. Count and Delta Explainability

Every build must write structured count deltas.

Required artifacts:

- before and after chunk counts
- before and after path counts
- added paths
- removed paths
- modified paths
- promoted notes
- imported notes
- source-level contribution counts

The dashboard must show destructive or suspicious events, including:

- large negative chunk swings
- path removals above threshold
- cross-dataset divergence
- stale snapshot serving

### 5. Source Lifecycle Management

The platform must treat source freshness as a first-class concept.

Required source states:

- healthy
- stale
- blocked
- throttled
- failing
- intentionally paused

Required source tooling:

- source scorecards
- freshness timers
- failure reasons
- retry history
- source-level diff summaries

### 6. Retrieval Quality and Evaluation

The platform must ship with built-in evals for core query classes.

Initial evaluation tracks:

- SEO diagnosis
- AI visibility and source canon routing
- patent and primary-source retrieval
- writer and marketing routing
- support and developer queue routing

Required outputs:

- precision-at-k
- accepted vs rejected memory paths
- over-ranked notes
- underused notes
- task-pack hit rates

### 7. Action Layer

The system must generate operator-grade outputs, not just status pages.

Required action artifacts:

- watchtower brief
- opportunity radar
- daily ops plan
- source anomaly brief
- retrieval quality report
- memory drift report

### 8. OpenClaw and MCP Integration

The platform must expose a stable way for agents and MCP servers to understand which dataset to use.

Required capabilities:

- dataset-aware MCP responses
- query routing recommendations
- explicit bridge sync health
- mission-ready output generation
- reusable task packs driven by current system state

### 9. Reliability and Recovery

The platform must support operator-grade reliability.

Required capabilities:

- health endpoints for every dashboard and dataset
- lock visibility
- last-known-good snapshot
- rollback or restore guidance for failed rebuilds
- alerts for stalled jobs and stale datasets

## Technical Direction

### Proposed architecture

1. Keep SQLite-backed datasets in the short term.
2. Add a `dataset_registry.json` or equivalent canonical registry.
3. Add a `runs` table or run ledger for all refreshes and rebuilds.
4. Add a `count_deltas` table keyed by run id and dataset id.
5. Serve one new control plane UI with all datasets visible.
6. Keep existing `8788` and `8765` surfaces initially, but make them subordinate views under the new control plane.

### Proposed command model

Introduce a single operator entrypoint such as:

```bash
python3 /Users/vijaychauhan/squad_memory/platform.py status
python3 /Users/vijaychauhan/squad_memory/platform.py refresh --dataset seo_elite
python3 /Users/vijaychauhan/squad_memory/platform.py refresh --dataset all
python3 /Users/vijaychauhan/squad_memory/platform.py compare --left seo_elite --right squad_memory
python3 /Users/vijaychauhan/squad_memory/platform.py explain-count --dataset seo_elite
```

## Rollout Plan

### Phase 1: Trust Layer

Goal:

- remove ambiguity about what each dashboard is showing

Deliverables:

- canonical dataset registry
- dataset labels and owners
- dashboard banners with DB path and dataset id
- dataset comparison page
- count delta artifacts

Exit criteria:

- the operator can explain any displayed chunk count in under 30 seconds

### Phase 2: Control Plane

Goal:

- create one operator entrypoint for all datasets and runs

Deliverables:

- new unified control plane UI
- run ledger
- structured logs and alerts
- one refresh command for each dataset and for the full stack

Exit criteria:

- the operator no longer needs to remember file paths or shell wrappers for routine status checks

### Phase 3: Retrieval Intelligence

Goal:

- make retrieval inspectable and optimizable

Deliverables:

- Retrieval Lab
- ranking explainability
- evaluation scorecards
- query routing recommendations

Exit criteria:

- the operator can compare corpora and understand why a result ranked

### Phase 4: Action OS

Goal:

- move from memory platform to SEO operating system

Deliverables:

- action prioritization engine
- outbox generation from control-plane state
- mission handoff into OpenClaw or Codex
- configurable brief generation

Exit criteria:

- the system can produce useful, prioritized operator output daily without manual stitching

## Risks

### Risk 1: More surfaces, more confusion

Mitigation:

- build the unified control plane before adding net-new dashboards

### Risk 2: Data model drift across DBs

Mitigation:

- enforce dataset registry, schema checks, and explicit bridge manifests

### Risk 3: Platform work delays source growth

Mitigation:

- keep ingestion running while platform work focuses first on visibility and explainability

### Risk 4: Trust remains low if numbers still disagree

Mitigation:

- treat count delta explainability as a launch blocker, not a nice-to-have

## Success Metrics

### Product success

- `90%` of dashboard interactions should expose dataset identity without extra clicks
- operator can identify the correct DB behind a metric in under `10` seconds
- operator can explain a chunk delta in under `30` seconds
- full-stack refresh success rate above `95%`
- retrieval eval pass rate improves on tracked SEO task suites

### Business and workflow success

- daily or weekly outputs are used as the default SEO ops starting point
- platform time spent debugging count confusion drops materially
- platform time spent on action generation increases

## Open Questions

1. Should the canonical source of truth become `squad_memory.db`, with `seo_elite_memory.db` as a filtered product view?
2. Should the portable snapshot stay a separate DB, or become a replicated profile from the canonical corpus?
3. Should the unified control plane replace `8788`, or should `8788` remain the SEO Elite detail view under a broader home surface?
4. Which agent workflows deserve first-class action generation in Phase 4?

## Recommended First 30 Days

1. Ship a dataset registry and surface DB identity in every dashboard.
2. Add count-delta artifacts to every rebuild.
3. Build a minimal compare page for `seo_elite`, `squad_memory`, and `portable_snapshot`.
4. Introduce a structured run ledger with run ids.
5. Rename or relabel `8788` in the UI as "SEO Elite Dataset Dashboard" so it cannot be mistaken for the full platform.
6. Create the first unified control plane shell with Overview, Datasets, and Runs only.

## Recommendation

Do not start with a redesign.

Start with trust, identity, and explainability.

The current system already has enough intelligence to feel impressive.
What it needs now is enough product structure to feel dependable.
