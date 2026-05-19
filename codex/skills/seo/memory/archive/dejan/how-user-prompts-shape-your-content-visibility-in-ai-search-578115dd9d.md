---
source: https://dejan.ai/blog/how-user-prompts-shape-your-content-visibility-in-ai-search/
title: How user prompts shape your content visibility in AI search.
scraped: 2026-03-25
published_on: 2025-12-13
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

# How user prompts shape your content visibility in AI search.

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/how-user-prompts-shape-your-content-visibility-in-ai-search/
Published: 2025-12-13
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
A single article. Seven different queries. Radically different passages surfaced. This isn’t a bug. It’s the ranker doing exactly what it’s supposed to do—and it reveals something important about how content actually gets discovered in AI search. The Data We ran seven query variations against one health article about teas for ulcerative colitis. The article […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

A single article. Seven different queries. Radically different passages surfaced.

This isn’t a bug. It’s the ranker doing exactly what it’s supposed to do—and it reveals something important about how content actually gets discovered in AI search.

We ran seven query variations against one health article about teas for ulcerative colitis. The article has two distinct content zones: detailed information about four specific teas (~80% of content), and a general tips section about trigger foods, hydration, and smoothies (~20%).

Here’s what the ranker surfaced for extractive summarization:

Six queries hit the tips section exclusively. One query—the most specific one—surfaced the article’s primary content.

The ranker evaluates semantic alignment between query and passage. It’s not broken. It’s doing its job.

“Lifestyle changes” and “dietary changes” are semantically closest to content about trigger foods, hydration strategies, and smoothies. That IS lifestyle and dietary guidance. The tea content is about specific beverages with specific compounds—a narrower semantic space.

The system correctly matched broad queries to broad content.

The revealing case is the mesalamine query: “What is the best diet to follow while taking mesalamine for ulcerative colitis?”

Mesalamine isn’t mentioned anywhere in the article. But this query surfaced the tea content that six other queries missed. Why?

1. “Best” signals recommendation-seeking intent. The user wants specific guidance, not general principles. The ranker surfaces passages that make specific recommendations—the tea content does exactly this.

2. The medication context implies an informed user. Someone mentioning their UC medication is past the “what is this condition” stage. They want actionable specifics. The detailed tea recommendations match this intent better than generic tips.

The query’s specificity unlocked a different semantic layer of the same document.

Another subtle finding: “Which foods should I avoid” pulled caffeine-related warnings from the tea sections that other queries missed.

The ranker found passages containing avoidance language: “caffeine is ideally skipped in a flare,” “caffeine is a stimulant and may lead to GI symptoms.”

Same document. Same tea content. But a negatively-framed query surfaced negative guidance that positively-framed queries (“what helps,” “what’s best”) did not.

Query framing isn’t just about topic—it’s about the polarity of the information need.

Your content exists as semantic topography. Different regions of your document live at different semantic coordinates. A query is a point in that space, and the ranker finds the nearest content.

If your article has a detailed core and a summarized tips section, users asking broad questions will get the tips. This isn’t a failure—it’s alignment. But it means your deep expertise only surfaces for users who ask with matching specificity.

The gap between what you wrote and what gets surfaced is often a gap in query specificity, not content quality.

The article we tested has clear structural separation: tea content in the body, tips in a dedicated section. This creates distinct semantic regions.

If the tea recommendations had been interleaved with actionable lifestyle framing—”Add peppermint tea to your routine because…”—they might have competed for lifestyle queries. Structure determines discoverability.

A single article serves users at different stages of information-seeking:

Each group hits different semantic zones. The question is whether your content has something relevant at each coordinate—and whether it’s structured to be found there.

Audit your content for semantic coverage. Map the query intents your article should serve. Then check: does each intent have a semantically-aligned passage? Or does all your detail live in one zone that only specific queries reach?

Bridge your specifics to broader frames. If you want your detailed recommendations to surface for general queries, the passages need to include general framing. “Lifestyle changes for UC include specific tea choices—peppermint tea helps because…” bridges the semantic gap.

Consider polarity in your phrasing. If users commonly search with avoidance framing (“what to avoid,” “what not to eat”), ensure your content includes passages with that polarity. Positive-only framing may miss negatively-framed queries.

Specificity begets specificity. Your most detailed content surfaces for your most detailed queries. If your audience asks generically, they’ll get your generic layer. This might be fine—or it might mean your expertise is structurally invisible to most of your traffic.

This data shows the ranker working correctly. But “working correctly” means query-passage semantic matching—not “surfacing your best content.”

These are different objectives. The system optimizes for relevance to the query as asked. It has no model of what you, the content creator, consider your most valuable contribution.

The burden of alignment falls on content structure. If you want specific expertise to surface for general queries, the content itself needs to bridge that semantic distance.

The ranker isn’t ignoring your best content. Your users’ queries might be.

Analysis based on passage ranking patterns observed across query variations on a single source document.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
