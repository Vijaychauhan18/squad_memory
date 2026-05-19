---
source: https://dejan.ai/blog/sro-grounding-snippets/
title: SRO & Grounding Snippets
scraped: 2026-03-22
published_on: 2026-03-01
tags: live_feed, phase1_ingest, dejan, practitioner, reverse-engineering, grounding, archive_backfill, historical_source
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Archive backfill - DEJAN / Dan Petrovic
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# SRO & Grounding Snippets

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/sro-grounding-snippets/
Published: 2026-03-01
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Source: dejan.ai/blog/category/ai-seo/sro/Author: Dan Petrovic, DEJAN AIPosts analyzed: 5 (Sep 2025 – Feb 2026) What is SRO? SRO — Selection Rate Optimization — is a new discipline coined by DEJAN that addresses visibility in AI-powered search (Google AI Mode, Gemini Chat, AI Overviews). It is the AI-native successor to traditional SEO click-through-rate optimization. The core premise: […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Source: dejan.ai/blog/category/ai-seo/sro/ Author: Dan Petrovic, DEJAN AI Posts analyzed: 5 (Sep 2025 – Feb 2026)

SRO — Selection Rate Optimization — is a new discipline coined by DEJAN that addresses visibility in AI-powered search (Google AI Mode, Gemini Chat, AI Overviews). It is the AI-native successor to traditional SEO click-through-rate optimization.

The core premise: ranking #1 in traditional search is necessary but no longer sufficient. In AI search, your page content goes through a grounding pipeline that extracts only select sentences to feed to the generative model. If your content isn’t selected and grounded, you’re invisible — even if you rank.

Selection Rate (SR) measures how often an AI system selects and incorporates a specific source from the total set of grounding results it retrieves.

SR is the Gen AI equivalent of CTR. Unlike CTR, which requires a user click, SR captures the AI’s implicit selection behavior — what information actually influences outputs versus what gets retrieved but ignored.

DEJAN reverse-engineered Google’s Gemini grounding pipeline by examining raw groundingSupports and groundingChunks from the API. The pipeline operates in this sequence:

Key insight: Because snippets are query-dependent, the same page yields different extractions for different fanout queries.

Google uses extractive (not abstractive) summarization for grounding. This means it pulls exact sentences from your page — it does not rewrite or paraphrase your content for the grounding context.

DEJAN successfully fine-tuned microsoft/deberta-v3-large to produce results similar to Google’s extraction behavior.

A pivotal finding from analysis of 7,060 queries with 2,275 tokenized pages and 883,262 total snippets:

Each query operates under a fixed grounding budget of approximately 2,000 words total , distributed across sources by relevance rank.

This budget is remarkably consistent regardless of the number of sources used or the length of individual pages. The average grounding chunk is ~15.5 words.

The fixed budget is divided among sources based on relevance ranking:

The #1 source gets 2× the grounding of the #5 source. You’re competing for share of a fixed pie, not expanding it.

On average, only about one-third of a page’s content makes it through the AI search filter into the grounding context. But this varies dramatically by page length:

Grounding plateaus at ~540 words / ~3,500 characters. Pages over 2,000 words see sharply diminishing returns — more content dilutes your coverage percentage without increasing what gets selected.

Based on DEJAN’s annotated analysis of actual grounding extractions:

The primary bias affecting SR is the model’s internal relevance perception of the grounding entity (brand, site, source). This is essentially the model’s pre-existing “worldview” about how relevant a source is for a given topic — formed during training and fine-tuning.

If a brand is perceived as highly relevant for a topic (e.g., “custom cycling jerseys”), it’s much more likely to achieve a higher SR when supplied as a grounding source. A brand with low primary bias for that topic will be deprioritized even if it appears in the result set.

DEJAN developed a “Tree Walker” algorithm that walks the probability paths of what a model wants to say about a brand, identifying high-uncertainty spots — token positions where the model is least confident about associating a concept with the brand. These represent opportunities for brand-association strengthening.

Analysis of 158 grounding responses revealed a power-law relationship between snippet count and snippet length:

The exponent β ≈ 0.07 shows a weak but consistent compression effect : as more snippets are added, average snippet length decreases slightly. The system emphasizes coverage over brevity, compressing only mildly — a sign of balanced aggregation rather than aggressive summarization.

Total text volume remains relatively stable across responses, implying word-limit constraints operate at the response level rather than per snippet.
