---
title: "Google Patent US11769017B1 — Generative Summaries for Search Results (v1)"
skill: seo
type: patent
patent_id: US11769017B1
assignee: Google LLC
granted: 2023-09-26
filed: 2023-03-20
priority: p1
confidence: 0.90
tags: [patents, ai_overviews, generative_summaries, grounding, llm_search, foundational]
related: [[google-patent-us11886828b1-generative-summaries]], [[google-patent-us12189697-informational-grounding]]
---

# Google Patent US11769017B1 — Generative Summaries for Search Results (v1)

## What it covers
Earlier sibling to US11886828B1 — describes the core LLM-based summary generation architecture that became AI Overviews. Covers personalisation by user context and addresses specification-level inaccuracies in LLM outputs by grounding outputs in retrieved search result documents.

## Core mechanism
1. Search query processed by standard ranking pipeline
2. Top results passed to LLM summary generator
3. LLM produces natural language summary grounded in those results
4. Summary personalised by user context (expertise, location, history)
5. Accuracy guardrails: summary must be supportable by at least one retrieved document

## SEO signals
- **Grounding accuracy requirement** — summaries must be attributable to retrieved documents; unsupported claims don't appear
- **User context personalisation** — the same page may be cited for novice queries but not for expert ones if the language is mismatched
- **Retrieved documents ≠ ranked documents** — the retrieval step for summary generation may differ from standard blue-link ranking

## Why this matters alongside US11886828B1
Together these two patents show AI Overviews was architecturally planned in 2023 Q1, with the second patent adding multi-query retrieval and history-based personalisation. The grounding requirements in the first patent established the passage-extraction constraint that the second patent refined.

## URL
https://patents.google.com/patent/US11769017B1
