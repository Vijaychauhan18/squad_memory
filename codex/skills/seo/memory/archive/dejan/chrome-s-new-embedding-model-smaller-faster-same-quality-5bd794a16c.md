---
source: https://dejan.ai/blog/chromes-new-embedding-model/
title: Chrome’s New Embedding Model: Smaller, Faster, Same Quality
scraped: 2026-03-25
published_on: 2025-04-19
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

# Chrome’s New Embedding Model: Smaller, Faster, Same Quality

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/chromes-new-embedding-model/
Published: 2025-04-19
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
TL;DR Discovery and Extraction During routine analysis of Chrome’s binary components, I discovered a new version of the embedding model in the browser’s optimization guide directory. This model is used for history clustering and semantic search. Model directory: Technical Analysis Methodology To analyze the models, I developed a multi-faceted testing approach: Key Findings 1. Architecture […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

During routine analysis of Chrome’s binary components, I discovered a new version of the embedding model in the browser’s optimization guide directory. This model is used for history clustering and semantic search.

To analyze the models, I developed a multi-faceted testing approach:

Both models maintain identical architecture with similar tensor counts (611 vs. 606) and identical input/output shapes ([1,64] input and [1,768] output). This suggests they were derived from the same base model, likely a transformer-based embedding architecture similar to BERT.

The primary difference is in the embedding matrix, which stores token representations:

This single tensor accounts for approximately 47MB of the total 46.77MB size reduction. The model contains 58 pseudo-quantized tensors in both versions, but the critical embedding matrix was converted from float32 to int8.

Despite internal quantization, the new model’s output embeddings maintain full float32 precision:

Intriguingly, the new model shows slightly higher effective precision, suggesting sophisticated quantization-aware training techniques.

Testing on diverse queries (e.g. “climate solutions”, “machine learning applications”, “travel documents”) showed:

This optimization represents a significant achievement in model compression for edge devices. By selectively quantizing the largest tensor while preserving the architecture and output precision, Chrome’s engineers have achieved a substantial size reduction without compromising semantic search quality.

The approach demonstrates how selective quantization of specific model components can be more effective than blanket quantization strategies. This technique is particularly valuable for browsers and other edge applications where storage efficiency is critical but performance cannot be sacrificed.

The slightly higher effective precision in the output layer suggests the quantization process may have included fine-tuning to compensate for potential precision loss, resulting in a model that maintains or even slightly improves embedding quality.

This optimization delivers several tangible benefits for Chrome users:

This article is AI augmented using Claude for both code and writing with human direction and curation.

Tensor Name: arith.constant Index: 1 Shape: [2] Data Type: Statistics: Min: 1.0 Max: 64.0 Mean: 32.5 Std: 31.5 Data Sample (first few values):

Tensor Name: arith.constant1 Index: 2 Shape: [2] Data Type: Statistics: Min: 0.0 Max: 0.0 Mean: 0.0 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant2 Index: 3 Shape: [] Data Type: Statistics: Min: 0.5 Max: 0.5 Mean: 0.5 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant3 Index: 4 Shape: [] Data Type: Statistics: Min: 1.0 Max: 1.0 Mean: 1.0 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant4 Index: 5 Shape: [] Data Type: Statistics: Min: 0.7978845834732056 Max: 0.7978845834732056 Mean: 0.7978845834732056 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant5 Index: 6 Shape: [] Data Type: Statistics: Min: 0.044714998453855515 Max: 0.044714998453855515 Mean: 0.044714998453855515 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant6 Index: 7 Shape: [ 1 1 64 64] Data Type: Statistics: Min: -10000000000.0 Max: -10000000000.0 Mean: -10000001024.0 Std: 1024.0 Data Sample (first few values):

Tensor Name: arith.constant7 Index: 8 Shape: [ 1 1 64 64] Data Type: Statistics: Min: 0.0 Max: 0.0 Mean: 0.0 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant8 Index: 9 Shape: [] Data Type: Statistics: Min: 9.999999974752427e-07 Max: 9.999999974752427e-07 Mean: 9.999999974752427e-07 Std: 0.0 Data Sample (first few values):

Tensor Name: arith.constant9 Index: 10 Shape: [] Data Type: Statistics: Min: 512.0 Max: 512.0 Mean: 512.0 Std: 0.0 Data Sample (first few values):

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
