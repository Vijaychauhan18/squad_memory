---
source: https://dejan.ai/blog/training-a-query-fan-out-model/
title: Training a Query Fan
scraped: 2026-03-25
published_on: 2025-06-23
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

# Training a Query Fan

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/training-a-query-fan-out-model/
Published: 2025-06-23
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Google discovered how to generate millions of high-quality query reformulations without human input by literally traversing the mathematical space between queries and their target documents. Here’s How it Works This generated 863,307 training examples for a query suggestion model (qsT5) that outperforms all existing baselines. Query Decoder + Latent Space Traversal Step 1: Build a […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

This generated 863,307 training examples for a query suggestion model (qsT5) that outperforms all existing baselines.

First, they trained a T5 model to invert Google’s GTR search encoder. Feed it any embedding vector, and it generates the query that would produce that embedding. This achieved 96% cosine similarity on reconstruction, nearly perfect fidelity.

Example traversal from “average yearly return on stock market”:

Step 0: “average yearly return on stock market” [nDCG: 0.0] Step 5: “what is the average return in a stock market” [nDCG: 0.0] Step 12: “what is the average return on the s&p stock exchange” [nDCG: 0.36] Step 20: “what is the average annual return of the s&p stock exchange” [nDCG: 1.0]

Using this synthetic dataset, they fine-tuned T5-large with two variants:

Modern neural retrievers like GTR embed queries and documents in the same vector space where semantic similarity equals geometric proximity. The researchers’ insight: if relevant documents cluster in certain regions, then moving toward those regions should produce better queries.

Here’s the fascinating part: while training data comes from explicit geometric traversal, the final qsT5 model operates without any vector arithmetic. It has internalized the traversal patterns.

When qsT5 sees “python loops” + search results about programming:

The model essentially compresses thousands of traversal examples into an implicit understanding of how to navigate query space.

MQR Who created the Spiritual Gangster? Who created the “spiritual gangster” storyline? Who created the “spiritual gangster”?

RM3 who created spiritual gangster spiritual who created spiritual gangster modern who created spiritual gangster inspired

Sampling+QD who created gangster a spiritual & egantious who created spiritual gangster -gangster who created spiritual gangster

qsT5 who is the founder of spiritual gangsters who created the spiritual gangster ( spiritual yogi ) what is the spiritual gangster movement

qsT5-plain who are the founders of the gangster spirit band how many gangsters were formed in white supreme who was the members of the gangster supremes

The qsT5 model with PRF significantly outperforms the query-only version because:

The model learns to extract signals from initial results and incorporate them into reformulations, mimicking how human searchers refine queries after seeing preliminary results.

By framing query reformulation as navigation in latent space, this work opens new possibilities:

The key insight: instead of treating queries as fixed strings, we can view them as starting points for journeys through meaning space. The AI has learned to be an expert guide for these journeys.

[…] our previous post, Training a Query Fan-Out Model, we demonstrated how to generate millions of high-quality query reformulations without human […]

The research you put out is simply phenomenal. Thank you for making this public…

Thank you Brian! Love to see that the research clicks with people, it’s very exciting stuff.

This is really great and insightful. I’m more concerned on practicality does this show relevance to performant keywords. And thanks for sharing.

[…] have successfully replicated Google’s query fan-out approach following their research papers and this article describes the exact mechanics of […]

[…] query variations that a business might not yet rank for, or even be aware of. This is where our query fan-out model comes in. Using advanced language models to generate a vast array of related search queries […]

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
