---
source: https://dejan.ai/blog/resource-efficient-binary-vector-embeddings-with-matryoshka-representation-learning/
title: Resource
scraped: 2026-03-25
published_on: 2024-09-05
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

# Resource

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/resource-efficient-binary-vector-embeddings-with-matryoshka-representation-learning/
Published: 2024-09-05
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
When conducting an advanced SEO analysis, I frequently utilise vector embeddings for text feature extraction, similarity searches, clustering, retrieval, ranking and so on. One of the main burdens on top of compute is storage space, as these files tends go into terabytes for very large websites. Today I did a deep analysis and realised I’ve […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

When conducting an advanced SEO analysis, I frequently utilise vector embeddings for text feature extraction , similarity searches, clustering, retrieval, ranking and so on. One of the main burdens on top of compute is storage space, as these files tends go into terabytes for very large websites. Today I did a deep analysis and realised I’ve been wasting time, money and hard drive space this whole time.

I started with a SOTA embedding model and tested the quality of vector embeddings after applying:

a. Matryoshka Representation Learning (MRL) b. Binary Embeddings c. Combined Both

Y = cosine spearman on MTEB/STS12 dataset. X = embedding dimensionality reduction via MRL.

Here’s how much hard drive space I need for each vector embedding, binary vs float, at each reduced dimension.

After 256 dimensions I hit true diminishing returns. Arguable we may lose finesse of semantic context through dimensionality reduction, but isn’t that what PCA is all about anyway? I’ve made a switch. Going forward lean a mean!

The OG BERT is at 30.87 on MTEB leaderboard which puts it on par with a binary 8-dimensional embedding of a modern embedding model. Ridiculous!

Here I apply my research to make a simple search engine using binary embeddings with dimensionality reduction to 256 using matryoshka representation learning method.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
