---
title: "Google Patent US11886828B1 — Generative Summaries for Search Results"
skill: seo
type: patent
patent_id: US11886828B1
assignee: Google LLC
granted: 2024-01-30
filed: 2023-08-22
priority: p1
confidence: 0.92
tags: [patents, ai_overviews, generative_summaries, grounding, llm_search, ranking]
related: [[google-patent-us11769017b1-generative-summaries-v1]], [[google-patent-us12189697-informational-grounding]], [[ai-overview-ranking-factors]]
---

# Google Patent US11886828B1 — Generative Summaries for Search Results

## What it covers
Primary architectural patent behind AI Overviews. An LLM generates natural-language search summaries grounded in fresh retrieved documents, conditioned on the original query, related queries, and recent user query history. Personalises by user expertise level. Addresses LLM accuracy issues by anchoring output in retrieved content.

## Core mechanism
1. Query fan-out: original query + related queries + user history → multiple sub-queries
2. Document retrieval per sub-query
3. LLM generates summary conditioned on retrieved content
4. Freshness and source trust filter applied before summary generation

## SEO signals
- **Passage-level extractability is required** — if content cannot be cleanly extracted at the passage level, it will not be cited regardless of ranking position
- **Author trust and freshness affect citation selection** — stale or low-trust sources are deprioritised at summary-generation time
- **Query-history personalisation** — returning users with established topic history may see differently-grounded summaries

## Practitioner implication
Write in extractable, self-contained paragraphs. Each section should answer a question independently. Dense prose blocks that require full-article context to make sense will be skipped.

## URL
https://patents.google.com/patent/US11886828B1
