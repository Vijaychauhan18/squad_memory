---
source: https://dejan.ai/blog/ai-reveal/
title: Using GPT-5 Structured Output Markers to Detect AI
scraped: 2026-03-25
published_on: 2025-09-27
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

# Using GPT-5 Structured Output Markers to Detect AI

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/ai-reveal/
Published: 2025-09-27
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
When you populate your website with language model–generated text, you inherit a subtle but real risk: AI-specific artifacts may leak into the published content. These markers aren’t always obvious to human readers, but they can be highly visible to search engines, researchers, and competitors. One such artifact is the structured output marker that GPT-5 (and […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

When you populate your website with language model–generated text, you inherit a subtle but real risk: AI-specific artifacts may leak into the published content . These markers aren’t always obvious to human readers, but they can be highly visible to search engines, researchers, and competitors.

One such artifact is the structured output marker that GPT-5 (and related systems) use internally to trace their tool calls and search results. Handles like turn0search21 are intended for machine-side traceability, not for publication. But when responses are used verbatim in production content – without careful editing or filtering – these strings can surface in the final page copy.

A quick Google search for turn0search21 illustrates the problem: you’ll see multiple live websites indexed with this artifact intact. These aren’t fringe blogs either – examples include major brands such as BigW , where the marker has been accidentally published on a product page.

Blindly copy-pasting LLM output into production is dangerous. If you use AI for drafting, always clean and human-review content before publishing. Specifically, scrub structured markers ( turnNsearchM , etc.) to avoid leaving behind tell-tale AI artifacts.

Here’s the complete set of turn{n}{type}{m} handles GPT-5 can emit:

When a model cites sources, you may see internal handles such as turn0search3 or turn2click1 . These identifiers are structured in a consistent way to trace exactly where a piece of information came from.

Imagine the assistant gets asked: “What’s the weather in Paris and the stock price of Google?”

These handles are not for end users to read directly – they’re traceability markers . They let developers (and debugging tools) map citations back to the exact retrieved item. In a UI, you would replace turn0search3 with a friendly citation like:

“Source: The Guardian , 2025-09-27 (search result #3 in turn 0).”

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
