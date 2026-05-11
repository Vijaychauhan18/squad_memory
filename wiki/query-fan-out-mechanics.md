---
title: Query Fan-Out Mechanics
type: wiki
skill: dejan-ai-reverse-engineering
priority: p1
confidence: 0.89
last_updated: 2026-04-08
tags: [fan_out, query_expansion, ai_mode, grounding, dejan, implicit_queries]
related: [[sro-selection-rate-optimization]], [[grounding-chunk-optimization]], [[ai-overview-ranking-factors]]
---

# Query Fan-Out Mechanics

## What it is
When a user types one query, Google/Gemini decompose it into multiple hidden sub-queries running in parallel behind the scenes. DEJAN calls this "fan-out." The visible prompt is just the entry point — the actual retrieval system runs 10+ sub-queries the user never sees.

This is not theory. DEJAN trained a replica fan-out model (qsT5) on 863K synthetic examples and 15M training samples across 70 hours. Fan-out is a reconstructable, observable production system.

## Why this matters for SEO
You cannot optimize for one query intent and win AI Overviews. The system is simultaneously asking:
- The explicit question
- Related sub-topics
- Comparison variants
- Entity verification queries
- Follow-up questions the user might ask next

**If your page only covers the surface query, it will be selected for fewer sub-queries = lower effective SRO.**

## The fan-out pipeline (DEJAN's reconstruction)
```
User query
    ↓
Query decomposition (fan-out model)
    ↓
10+ hidden sub-queries generated
    ↓
Each sub-query → independent retrieval → grounding candidates
    ↓
Selected chunks merged → LLM synthesizes answer
    ↓
Citations = pages that won ≥1 sub-query slot
```

## Practical implications
1. **Content gap is really a sub-query gap** — find the hidden sub-queries your page misses
2. **Ranking for the head query ≠ selected for sub-queries** — you can rank #1 and still not be cited
3. **Test with prompt variants** — different phrasings activate different fan-out paths
4. **Cover adjacent sub-topics on the same page** — visa process, pricing, best time to visit = separate sub-queries that can all land on one comprehensive page
5. **Separate retrieval failures from routing failures** — if you're not cited, diagnose which fan-out slot you're missing, not just your main keyword

## DEJAN's reverse-engineering method
- Capture the visible prompt → infer the hidden task graph (sub-queries)
- Use multiple prompt variants to map which sub-queries your page wins
- Track grounding citation position per variant — not just final ranking
- When a behavior is measurable, build a narrow replica evaluator rather than doing manual analysis repeatedly

## Fan-out as an agent workflow
DEJAN also models fan-out as an executable agentic workflow — observable intermediate steps with a sub-query graph. This makes it debuggable. The intermediate research steps are not invisible; they have structure.

## Sources (DEJAN)
- Implicit Queries in AI Search (2026-02-24)
- Google's Query Fan-Out System — A Technical Overview (2025-08-09)
- Query Fan-Out Prompt Implementation in Google's Open-Source Agentic Framework (2025-06-04)
- Fan-Out Query Search Volume Prediction Using Deep Learning (2025-08-30)
- Training a Query Fan-Out Model (2025-06-24)
