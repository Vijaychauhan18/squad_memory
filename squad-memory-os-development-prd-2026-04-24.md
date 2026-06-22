# Squad Memory OS Development PRD

Date created: Apr 24, 2026
Status: In progress
Last Mod: Apr 24, 2026

## Recommend

Vijay Chauhan + Codex

## Approve

Vijay + Platform Engineering

## Perform (design/eng)

Platform Engineering

## Input (optional)

SEO Ops + Research + Automation

## Decide

Vijay + Platform Engineering

## = reviewed/approved

Pending

## 0. Delivery Status

Current implementation track:

- Phase 1 has started
- first shipped slice: dataset truth layer for the live SEO Elite dashboard
- Phase 2 has started
- first shipped slice: universal MCP access layer for Codex and Claude clients
- second shipped slice: MCP prompts and MCP resources for reusable local workflows and inspectable context
- third shipped slice: local MCP delta/history and run-ledger layer for explainability and pipeline state
- fourth shipped slice: live patent-backed website audit flow for real-site SEO diagnosis
- next build target: roots-aware workspace scoping, elicitation, and warm local caching/runtime

## 1. Objective

Build the next version of the current SEO memory stack as an engineering-grade platform:

**Squad Memory OS**

The purpose of this PRD is not to describe a business dashboard.
The purpose is to define the software changes needed to make the current system:

- easier to trust
- easier to operate
- easier to extend
- more intelligent
- better at turning memory into action

This PRD is implementation-focused. It maps the current codebase to a phased development plan with technical requirements, file targets, schema changes, APIs, and acceptance criteria.

## 2. Current System

### 2.1 Current code surfaces

The current system is already substantial and working, but it is split across multiple Python entrypoints and multiple databases.

Key modules:

- [`squad_memory.py`](/Users/vijaychauhan/squad_memory/squad_memory.py)
  Purpose: index build, query, retrieval ranking, feedback, training, task-pack execution, outcome learning, workspace contexts, episodes, and reports
- [`report_seo_elite_status.py`](/Users/vijaychauhan/squad_memory/report_seo_elite_status.py)
  Purpose: builds the SEO Elite status payload and writes status files used by the dashboard
- [`seo_elite_dashboard.py`](/Users/vijaychauhan/squad_memory/seo_elite_dashboard.py)
  Purpose: serves the status dashboard on `8788`
- [`phase31_memory_graph.py`](/Users/vijaychauhan/squad_memory/phase31_memory_graph.py)
  Purpose: builds and serves the graph surface on `8765`
- [`refresh_local_seo_stack.py`](/Users/vijaychauhan/squad_memory/refresh_local_seo_stack.py)
  Purpose: stack discovery across local SEO tooling and memory stores

### 2.2 Current databases

Validated on Apr 24, 2026:

| Dataset | Path | Chunks | Distinct paths |
| --- | --- | ---: | ---: |
| SEO Elite DB | `/Users/vijaychauhan/squad_memory/seo_elite_memory.db` | `52,709` | `8,658` |
| Squad Memory DB | `/Users/vijaychauhan/squad_memory/squad_memory.db` | `70,200` | `9,657` |
| Portable snapshot DB | `/Users/vijaychauhan/portable-repos/seo-vector-snapshot/db/squad_memory.db` | `63,670` | `8,973` |

### 2.3 Current DB capabilities

Both `seo_elite_memory.db` and `squad_memory.db` already contain advanced tables, including:

- `chunks`
- `chunks_fts`
- `chunk_vectors`
- `token_vectors`
- `query_log`
- `feedback`
- `training_runs`
- `pack_runs`
- `pack_run_steps`
- `pack_run_handoffs`
- `pack_run_blockers`
- `task_outcomes`
- `task_result_scorecards`
- `episodes`
- `workspace_contexts`

This matters because the next version should reuse existing learning and execution primitives instead of inventing a parallel system.

### 2.4 Current strengths

- hybrid lexical and semantic retrieval already exists
- role-aware routing already exists
- task-pack and execution-run infrastructure already exists
- scorecard learning already exists
- live status generation already exists
- graph export already exists

### 2.5 Current engineering problems

The system has grown into a strong engine, but it still feels like several tools stitched together.

Current engineering problems:

1. **Dataset identity is implicit**
   The UI and scripts do not make it obvious which corpus is being shown.

2. **Control plane is fragmented**
   Status, graph, retrieval, run management, and stack health live in separate entrypoints.

3. **The monolith is too large**
   [`squad_memory.py`](/Users/vijaychauhan/squad_memory/squad_memory.py) contains indexing, ranking, training, execution tracking, and reporting in one large file.

4. **Delta explainability is weak**
   Chunk counts can change, but the system does not yet expose path-level and source-level reasons in a first-class way.

5. **Cross-corpus reasoning is missing**
   We have multiple corpora, but not a smart federated query or corpus selection layer.

6. **Action intelligence is still shallow**
   The system stores knowledge well, but it does not yet consistently transform state into ranked recommendations, briefs, and missions.

7. **Operations rely too much on wrappers**
   There are many shell runners, but not enough structured orchestration, retries, lineage, and inspectable run state.

## 3. Problem Statement

The current system is good at storing and retrieving memory, but not yet great at:

- clarifying which memory layer is active
- explaining what changed and why
- automatically choosing the right corpus for a task
- turning retrieval and system state into prioritized action
- helping the operator run the full stack from one place

The system is already valuable.
The next leap is not "more content."
The next leap is **better platform intelligence**.

## 4. Goals

### 4.1 Primary engineering goals

1. Create one canonical control plane for all memory datasets.
2. Introduce explicit dataset identity and lineage everywhere.
3. Modularize the monolith without breaking existing flows.
4. Add federated and explainable retrieval across corpora.
5. Add structured run orchestration and count-delta explainability.
6. Add an intelligence layer that can recommend actions, not just show state.

### 4.2 Non-goals

- replacing SQLite in Phase 1
- rewriting the whole system from scratch
- deleting existing dashboards before the new control plane exists
- prioritizing visual redesign over platform correctness

## 4.3 Research-Backed Direction

Research pass completed on Apr 24, 2026:

- memory note: [`local-first-squad-memory-product-research-2026-04-24.md`](/Users/vijaychauhan/.codex/memories/local-first-squad-memory-product-research-2026-04-24.md)

The strongest conclusions from current official docs and protocol references are:

1. MCP should remain the universal contract for local interoperability.
2. Product behavior should increasingly live in MCP prompts and resources, not only raw tools.
3. Local packaging matters: Claude Desktop extensions and install helpers materially improve product feel.
4. Skills are still useful, but cannot be the primary cross-surface contract because custom skills do not sync cleanly across surfaces.
5. Workspace-aware scoping and structured user input should be built using MCP roots and elicitation rather than custom prompt conventions.
6. Speed is now a product requirement: local caching and warm services are necessary for premium operator experience.

## 5. Product Scope for Engineering

The next version of the system must include the following subsystems.

### 5.1 Dataset Registry

Create a canonical dataset registry used by dashboards, APIs, jobs, and agents.

Required dataset entries:

- `seo_elite`
- `squad_memory`
- `portable_snapshot`
- `openclaw_main`
- `openclaw_seo`

Each dataset entry must define:

- dataset id
- label
- DB path
- purpose
- owner
- update source
- dashboard surfaces
- refresh command
- health command
- expected count band
- import/export relationships

### 5.2 Unified Control Plane API

Create a new backend surface that exposes:

- `/api/datasets`
- `/api/datasets/:id`
- `/api/datasets/:id/history`
- `/api/datasets/:id/delta`
- `/api/runs`
- `/api/runs/:id`
- `/api/query/federated`
- `/api/stack/health`
- `/api/actions/recommendations`

This API becomes the stable internal contract for dashboards and agent-facing surfaces.

### 5.3 Count and Delta Engine

Every build or refresh must persist:

- before and after chunk counts
- before and after path counts
- added paths
- removed paths
- modified paths
- source-level contribution counts
- corpus-level impact summary

### 5.4 Federated Retrieval

Add a federated query engine that can:

- query one corpus
- query all corpora
- compare corpora
- rank by corpus suitability
- explain why a corpus was chosen

### 5.5 Intelligence Layer

Add a decision layer that can:

- classify the query or task
- choose the best corpus or corpus combination
- detect anomalies in ingestion and corpus state
- rank action opportunities
- generate briefs or mission-ready outputs

### 5.6 Run Orchestration

Introduce a structured run engine with:

- run ids
- named jobs
- explicit dependencies
- lock visibility
- retries
- structured logs
- resumable failures
- end-of-run summaries

## 6. Proposed Architecture

### 6.1 High-level architecture

```text
UI / Dashboards / Agents
        |
        v
Unified Control Plane API
        |
        +-- Dataset Registry
        +-- Federated Query Router
        +-- Run Orchestrator
        +-- Delta / Lineage Engine
        +-- Action Intelligence Engine
        |
        +-- seo_elite_memory.db
        +-- squad_memory.db
        +-- portable snapshot db
        +-- OpenClaw memory dbs
```

### 6.2 Proposed package structure

Introduce a new package layout under `/Users/vijaychauhan/squad_memory/platform/`.

Proposed modules:

- `platform/datasets/registry.py`
- `platform/datasets/models.py`
- `platform/datasets/service.py`
- `platform/deltas/service.py`
- `platform/runs/service.py`
- `platform/runs/orchestrator.py`
- `platform/query/federated.py`
- `platform/query/explain.py`
- `platform/intelligence/classifier.py`
- `platform/intelligence/recommendations.py`
- `platform/intelligence/anomaly.py`
- `platform/api/server.py`
- `platform/api/handlers/*.py`
- `platform/ui/` for the future unified dashboard frontend

### 6.3 Refactor direction for current files

#### `squad_memory.py`

Keep as a compatibility CLI initially, but begin extracting:

- schema and DB helpers
- build logic
- retrieval ranking
- report generation
- training logic
- run-tracking logic

Target outcome:

- `squad_memory.py` becomes a thin CLI facade over reusable modules

#### `report_seo_elite_status.py`

Refactor into:

- dataset-specific status collectors
- reusable dataset summary contracts
- control-plane-ready output schema

#### `seo_elite_dashboard.py`

Phase 1:

- keep alive
- add dataset identity banners
- display DB path and corpus id visibly
- consume registry-backed dataset metadata

Later:

- rehome into the unified control plane as one dataset-specific view

#### `phase31_memory_graph.py`

Keep alive, but shift to control-plane integration:

- graph becomes a tab in the unified platform
- node overlays should support dataset lineage and delta context

## 7. Data Model Changes

### 7.1 New metadata registry

Introduce either:

- `dataset_registry.json`

or:

- a `datasets` SQLite table in the canonical platform DB

Recommended:

- start with `dataset_registry.json`
- mirror core fields into SQLite later if needed

### 7.2 New tables

Add the following to the primary operational DB for the control plane:

- `dataset_builds`
- `dataset_build_deltas`
- `dataset_path_deltas`
- `dataset_source_deltas`
- `orchestrator_runs`
- `orchestrator_run_steps`
- `query_federation_log`
- `query_explanations`
- `action_recommendations`
- `dataset_health_snapshots`

### 7.3 Required fields

#### `dataset_builds`

- `build_id`
- `dataset_id`
- `status`
- `started_at`
- `finished_at`
- `trigger`
- `command`
- `source`
- `notes`

#### `dataset_build_deltas`

- `build_id`
- `before_chunks`
- `after_chunks`
- `delta_chunks`
- `before_paths`
- `after_paths`
- `delta_paths`
- `added_paths`
- `removed_paths`
- `modified_paths`

#### `query_explanations`

- `query_id`
- `query_text`
- `dataset_rankings_json`
- `winning_dataset_id`
- `reasoning_summary`
- `signals_json`

#### `action_recommendations`

- `recommendation_id`
- `dataset_id`
- `category`
- `priority`
- `title`
- `summary`
- `evidence_json`
- `created_at`
- `status`

## 8. Intelligence Upgrades

### 8.1 Corpus Router

Build a classifier that decides which corpus should answer a request.

Initial routing classes:

- freshness-first SEO news
- durable SEO canon
- broader squad execution knowledge
- OpenClaw workspace context
- cross-corpus comparison

Signals should include:

- query vocabulary
- requested task type
- source recency requirements
- desired answer style
- previous feedback and successful outcomes

### 8.2 Retrieval Explainability

For each federated query, expose:

- lexical score
- semantic score
- vector seed contribution
- learned priors
- outcome priors
- result priors
- why the winning corpus won

### 8.3 Anomaly Detection

The system should detect:

- sudden chunk drops
- path drops above threshold
- stale dataset refreshes
- silent bridge failures
- long-running jobs
- repeated source failures

Each anomaly should generate:

- severity
- probable cause
- impacted datasets
- recommended operator action

### 8.4 Action Recommendations

The system should synthesize current state into ranked actions.

Examples:

- "SEO Elite dataset rebuilt but bridge sync is stale by 3 days"
- "Portable snapshot is lagging behind elite corpus by 8,000+ chunks"
- "Patent corpus expanded; rebuild primary note summaries"
- "High source freshness, but low action output generation"

## 9. UI Requirements

### 9.1 Phase 1 UI changes

Minimal but mandatory:

- visible dataset name on every dashboard
- visible DB path on every dashboard
- "Powered by" label
- last successful build timestamp
- current count vs previous count
- direct link to delta explanation

### 9.2 Unified control plane views

Required views:

- Overview
- Datasets
- Runs
- Retrieval Lab
- Graph
- Alerts
- Actions

### 9.3 Overview requirements

Must show:

- all corpora side by side
- chunk counts
- paths
- freshness
- active jobs
- alerts
- top recommended actions

### 9.4 Datasets view requirements

Must show:

- dataset details
- lineage
- refresh commands
- history chart
- last delta summary
- import/export relationships

### 9.5 Retrieval Lab requirements

Must support:

- one query across all corpora
- side-by-side result comparison
- explanation for winning corpus
- feedback buttons

## 10. API Requirements

### 10.1 Dataset endpoints

- `GET /api/datasets`
- `GET /api/datasets/{dataset_id}`
- `GET /api/datasets/{dataset_id}/history`
- `GET /api/datasets/{dataset_id}/delta/latest`

### 10.2 Run endpoints

- `GET /api/runs`
- `GET /api/runs/{run_id}`
- `POST /api/runs/refresh`
- `POST /api/runs/rebuild`

### 10.3 Query endpoints

- `POST /api/query/federated`
- `POST /api/query/explain`
- `POST /api/query/feedback`

### 10.4 Intelligence endpoints

- `GET /api/actions/recommendations`
- `GET /api/alerts`
- `GET /api/stack/health`

## 11. Development Phases

### Phase 1: Dataset Truth Layer

Goal:

- eliminate ambiguity about what each surface is showing

Build:

- dataset registry
- dataset comparison service
- delta tracking for builds
- dataset banners in `8788`
- API for dataset identity and counts

Files to create:

- `platform/datasets/registry.py`
- `platform/datasets/models.py`
- `platform/datasets/service.py`
- `platform/deltas/service.py`

Files to modify:

- [`seo_elite_dashboard.py`](/Users/vijaychauhan/squad_memory/seo_elite_dashboard.py)
- [`report_seo_elite_status.py`](/Users/vijaychauhan/squad_memory/report_seo_elite_status.py)

Acceptance criteria:

- every dashboard explicitly names its dataset
- every dataset shows DB path and last build timestamp
- operator can compare SEO Elite, Squad, and portable snapshot counts from one API
- every rebuild writes a structured delta artifact

### Phase 2: Unified Control Plane Backend

Goal:

- create one backend contract for all dashboards and agents

Build:

- unified control plane API
- dataset endpoints
- run endpoints
- health endpoints

Files to create:

- `platform/api/server.py`
- `platform/api/handlers/datasets.py`
- `platform/api/handlers/runs.py`
- `platform/api/handlers/health.py`

Acceptance criteria:

- new API serves all dataset and run metadata from one place
- existing `8788` dashboard can consume API-backed dataset metadata
- graph server can optionally consume control-plane metadata

### Phase 3: Orchestrator and Run Ledger

Goal:

- make pipeline execution observable and recoverable

Build:

- run engine
- step engine
- retries and locks
- structured run summaries

Files to create:

- `platform/runs/orchestrator.py`
- `platform/runs/service.py`
- `platform/runs/models.py`

Acceptance criteria:

- refreshes have stable run ids
- failures are resumable or restartable with context
- operator can inspect step-level status without reading raw logs

### Phase 4: Federated Retrieval and Explainability

Goal:

- make multi-corpus retrieval smart and transparent

Build:

- federated query router
- query explanation payloads
- corpus suitability scoring

Files to create:

- `platform/query/federated.py`
- `platform/query/explain.py`
- `platform/intelligence/classifier.py`

Acceptance criteria:

- one query can hit all corpora
- returned results include corpus-level explanation
- operator can see why one corpus beat another

### Phase 5: Intelligence and Action Engine

Goal:

- transform memory state into recommendations and briefs

Build:

- anomaly detector
- recommendation engine
- brief generator

Files to create:

- `platform/intelligence/anomaly.py`
- `platform/intelligence/recommendations.py`
- `platform/intelligence/actions.py`

Acceptance criteria:

- system emits ranked recommendations from current state
- anomalies are visible and actionable
- recommendation payloads can be written into OpenClaw or Codex outputs

### Phase 6: UI Unification

Goal:

- unify status, graph, and retrieval into one operator shell

Build:

- new control plane UI
- Overview, Datasets, Runs, Retrieval Lab, Alerts, Graph tabs

Acceptance criteria:

- operator no longer needs separate mental models for `8788` and `8765`
- the graph and status surfaces are linked by dataset identity and build context

## 12. Acceptance Criteria for the Full Initiative

The initiative is successful when:

1. the operator can identify which DB powers any metric in under 10 seconds
2. the operator can explain a count change in under 30 seconds
3. all refreshes produce structured run and delta artifacts
4. federated retrieval can compare corpora in one query flow
5. the system emits useful ranked action recommendations daily or on demand
6. the stack can be operated from one control plane rather than shell-memory and file-path memory

## 13. Risks

### Risk 1: Too much refactor, not enough shipping

Mitigation:

- keep the old CLI and dashboards running while extracting reusable modules underneath

### Risk 2: Schema growth without discipline

Mitigation:

- add new platform tables in a controlled migration layer

### Risk 3: Intelligence layer becomes opaque

Mitigation:

- require explanations for routing and recommendations from day one

### Risk 4: More dashboards create more confusion

Mitigation:

- treat the unified control plane as the home surface and legacy dashboards as scoped subviews

## 14. Recommended Build Order

Do not start by redesigning the graph.

Start in this order:

1. Dataset registry
2. Count-delta engine
3. Dashboard identity banners
4. Unified control plane API
5. Orchestrator run ledger
6. Federated retrieval
7. Action intelligence
8. UI unification

## 15. Phase 1 Start Recommendation

After this PRD is accepted, start with **Phase 1: Dataset Truth Layer**.

Reason:

- it solves the trust problem immediately
- it is low-risk compared with monolith surgery
- it gives every later phase a stable identity model
- it makes future intelligence work usable because users will trust the underlying numbers

The first concrete output after PRD approval should be:

- one `dataset_registry` implementation
- one `GET /api/datasets` endpoint
- one dashboard patch that shows dataset id, DB path, current count, previous count, and delta
