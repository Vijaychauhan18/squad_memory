---
title: "Google Patent US12189697 — Informational Grounding with Respect to a Generative Model"
skill: seo
type: patent
patent_id: US12189697
assignee: Google LLC
granted: 2025-01-07
priority: p1
confidence: 0.93
tags: [patents, grounding, llm_search, ai_overviews, retrieval, citation, rag]
related: [[google-patent-us11886828b1-generative-summaries]], [[google-patent-us20240289407a1-stateful-chat]]
---

# Google Patent US12189697 — Informational Grounding with Respect to a Generative Model

## What it covers
The core grounding loop for LLM-based search: the generative model generates an internal search query from user input, dispatches it to the retrieval engine, receives retrieved documents, and conditions its final output on a grounded prompt that embeds those results. Multi-turn support allows iterative re-grounding for follow-up responses.

## Core mechanism
1. User input → LLM generates internal query (may differ significantly from user's words)
2. Internal query dispatched to retrieval engine
3. Retrieved documents injected into a grounding prompt
4. LLM generates final response conditioned on grounded context
5. Follow-up turns: LLM can generate new internal queries to re-ground

## SEO signals
- **Content must survive the internal query step** — the LLM's internal query may rephrase your keyword entirely; entity clarity and semantic completeness matter more than exact keyword match
- **Passage extraction is the citation gate** — only content that cleanly maps to the grounding prompt window gets cited
- **Multi-turn re-grounding** — AI Mode follow-up questions may pull from different document sections; each section needs standalone value

## Practitioner implication
This is the patent that confirms why AI Overview citations don't always match the top-ranked page. The LLM's internal query determines what gets retrieved — not the user's keywords. Writing for entity and concept completeness (not keyword density) is the correct response.

## URL
https://patents.justia.com/patent/12189697
