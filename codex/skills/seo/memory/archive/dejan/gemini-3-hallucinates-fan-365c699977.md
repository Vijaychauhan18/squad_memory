---
source: https://dejan.ai/blog/gemini-3-hallucinates-fan-out-queries/
title: Gemini 3 hallucinates fan
scraped: 2026-03-25
published_on: 2025-11-22
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

# Gemini 3 hallucinates fan

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/gemini-3-hallucinates-fan-out-queries/
Published: 2025-11-22
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
TL;DR: Gemini 3 made up the fan-out queries used to answer a prompt. Today I was testing the updated API response from Gemini 3 (thanks Mike!) and found it to be as unreliable as its predecessors when it comes to hallucinations. Not only did it lie to me, but it also attempted to cover up […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Today I was testing the updated API response from Gemini 3 ( thanks Mike! ) and found it to be as unreliable as its predecessors when it comes to hallucinations. Not only did it lie to me, but it also attempted to cover up the lie as well.

Note: The part which says <… 7 more items …> is the actual part of the response.

When instructed to list the queries used it filled the blanks for the 7 missing queries by fabricating them and returned a list of 12.

The funny thing is this wasn’t even a real grounding call. It was a complete simulation and I controlled every aspect of it. The entire grounding context was placed in the system prompt and the model prompted via an API call with grounding disabled.

This behaviour is not new and is consistent with how models operate. Sharing this to raise awareness in case there are people out there who still take AI model’s output as facts.

If you want reliable data you have to parse the API call itself avoiding any form of model-based data interpretation.

Hey Dan, I know you mentioned the above was a simulation – however are you seeing any difference in the actual query fan outs from the grounding API with Gemini 3?

From my understanding there is only a handful of queries returned and I was wondering if this had improved at all?

Yes I’ve upgraded https://queryfanout.ai/ to Gemini 3 and for whatever reason the fanout appears to be more generous.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
