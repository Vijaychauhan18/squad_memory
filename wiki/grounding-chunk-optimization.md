---
title: Grounding Chunk Optimization
type: wiki
skill: dejan-ai-reverse-engineering
priority: p1
confidence: 0.90
last_updated: 2026-04-08
tags: [grounding, grounding_snippets, domdistiller, content_structure, machine_readability, dejan]
related: [[sro-selection-rate-optimization]], [[query-fan-out-mechanics]], [[ai-overview-ranking-factors]]
---

# Grounding Chunk Optimization

## What grounding actually is
Grounding is the process of supplying external retrieved content to an LLM at inference time. It is NOT the same as indexing. A page can be indexed, ranking well, and still never be grounded in an AI answer.

Grounding is also a **routing decision** — not every query triggers grounding. DEJAN's April 2025 work identified a grounding classifier that determines per-query whether grounding is beneficial. When debugging AI visibility, diagnose in this order:

1. Grounding eligibility (does this query trigger grounding at all?)
2. Retrieval quality (is your page in the retrieval pool?)
3. Snippet selection (does your specific text get selected from your page?)

## DomDistiller — the extraction layer
Google uses a DomDistiller-style extraction (Chrome's reader mode algorithm) before feeding content to the grounding model. What this strips:
- Navigation, headers, footers
- Ads and sidebars
- Hidden/collapsed content (tabs, accordions)
- JS-rendered blocks not in initial DOM
- Decorative and boilerplate text

**What survives: the main content block only. Approximately 1/3 of total page content.**

This is why content hidden behind UI interactions gets lower selection — it may not survive extraction at all.

## Grounding chunk size
DEJAN's Dec 2025 study on grounding chunk sizes: chunks are small, approximately 256–512 tokens. This means:
- A 2,000-word article ≈ 6-8 grounding chunks
- Each chunk competes independently for selection
- One poorly structured section can cost you a slot even if the rest of the page is excellent

## How to write grounding-optimized content

### Structure rules
- **One idea per chunk** (~300 words per section max)
- **Answer first** — front-load the claim or fact in the first sentence
- **Self-contained** — the section must make sense extracted alone, with no reference to "as mentioned above"
- **Explicit and factual** — precise claims beat vague summaries
- **No setup before the answer** — "Great question, in this article we'll explore..." = wasted grounding budget

### Technical rules
- Visible by default — no tabs, no accordions for primary content
- Clean HTML structure — headers, paragraphs, lists (all DomDistiller-friendly)
- FAQ schema — directly maps to grounding chunk structure, gets prioritized
- Avoid duplicate text clusters on same domain — splits selection weight

### Entity and brand rules
- Named entities should appear in the first sentence of a chunk
- Brand attribution matters for entity grounding: "According to [Author], a [credential]..." signals E-E-A-T to the extraction layer

## Grounding is transient — not permanent memory
DEJAN (2026-03-06): "Grounded content should not be treated as durable model memory."

Every query is re-grounded fresh. There is no persistent selection from previous grounding events. Optimize for immediate extraction quality on each request — not assumed retention.

The durable layer is primary bias (brand/entity associations in model weights). Grounding optimization and brand authority building are separate work streams.

## Debug checklist when you're not being grounded
- [ ] Does the query type trigger grounding? (factual/informational = yes, navigational = rarely)
- [ ] Is the page indexed and rendering correctly?
- [ ] Is primary content visible without JS execution?
- [ ] Are sections self-contained and front-loaded?
- [ ] Is there duplicate content splitting selection weight?
- [ ] Are there legacy visibility issues (hidden content, accordion-first layout)?

## Sources (DEJAN)
- What extraction method is Google using to build grounding snippets? (2026-02-24)
- How big are Google's grounding chunks? (2025-12-20)
- How much of your content survives the AI Search filter? (2025-11-08)
- Deconstructing DomDistiller: How Chrome's Reader Mode Algorithm Impacts Technical SEO (2025-09-22)
- How Google Decides When to Use Gemini Grounding for User Queries (2025-03-29)
- Grounding Is Also A Routing Decision — Introducing Grounding Classifier (2025-04-02)
