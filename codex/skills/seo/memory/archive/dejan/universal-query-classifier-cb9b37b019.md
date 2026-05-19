---
source: https://dejan.ai/blog/universal-query-classifier/
title: Universal Query Classifier
scraped: 2026-03-25
published_on: 2025-06-13
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

# Universal Query Classifier

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/universal-query-classifier/
Published: 2025-06-13
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Generalist, Open‑Set Classification for Any Label Taxonomy We’ve developed a search query classifier that takes any list of labels you hand it at inference time and tells you which ones match each search query. No retraining, ever. Just swap in new labels as they appear. Old workflow Pain New workflow Build + label data + retrain […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

We’ve developed a search query classifier that takes any list of labels you hand it at inference time and tells you which ones match each search query. No retraining, ever. Just swap in new labels as they appear.

For each pair [math] (q,\,\ell) [/math], we define a binary relevance loss:

[math]\mathcal{L} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log \sigma(s_i) + (1 – y_i) \log \left(1 – \sigma(s_i) \right) \right][/math],

where [math]s_i[/math] is the scalar score from the linear head and [math]\sigma[/math] is the sigmoid.

This formulation trains the model to assign high scores to semantically relevant (query, label) pairs and low scores to irrelevant ones, regardless of whether the labels have been seen during training.

Optimizer = AdamW(2 e‑5) with linear warm‑up; FP16 and early stopping on dev‑F1.

Overall Performance : 85% accuracy (85/100 queries correctly classified) Average Confidence : 0.814 (81.4%)

The Universal Query Classifier demonstrates strong performance with room for targeted improvements, particularly in distinguishing between navigational and transactional queries.

Large Model Performance : 91.8% accuracy (101/110 queries correctly classified) Improvement over Base Model : +5.5 percentage points (from 86.4% to 91.8%) Average Confidence : 0.935 (vs 0.814 for Base model)

The Large model shows significant improvement over the Base model, particularly excelling in Commercial Investigation and Transactional categories while maintaining perfect performance in Local queries.

After the testing feedback, the training dataset was augmented to 130,000 training samples.

In addition to geographic, navigational and login confusion we also introduce adult, pornography, contraband and illegal item queries.

Of particular interest was being able to distinguish between a genuine adult product commonly sold on eCommerce websites and pure porn queries (e.g. videos, channels, websites and actor names).

After analyzing 550 individual predictions from epoch_7 across 5 datasets, the model demonstrates EXCELLENT calibration with a confidently wrong rate of only 2.4%.

•Very High Confidence (≥0.9): 97.2% accuracy (380/391 correct)

•Very Low Confidence (<0.6): 50.0% accuracy (63/126 correct)

Pattern Identified: Most errors involve confusing Commercial Investigation with Local queries

•”Best restaurants reviews” → Predicted: Local, True: Commercial Investigation (0.837 confidence)

•”Top rated hotels reviews” → Predicted: Local, True: Commercial Investigation (0.970 confidence)

•”Top rated pizza places” → Predicted: Local, True: Commercial Investigation (0.998 confidence)

•”How to lose weight fast” → Correct: Informational (0.317 confidence)

Analysis: These low-confidence correct predictions show the model is appropriately cautious on borderline cases.

Key Insight: Dataset_4 shows the strongest confidence-accuracy correlation (0.773), while Dataset_1 shows the weakest (0.294) despite highest accuracy.

•Confidence-Accuracy Correlation: 0.605 (Strong positive correlation)

•Confidently Wrong Rate: 2.4% (Excellent – industry standard is <5%)

•0.9-1.0: 391 predictions, 99.3% avg confidence, 97.2% accuracy (Error: 2.1%)

•0.8-0.9: 16 predictions, 86.1% avg confidence, 87.5% accuracy (Error: 1.4%)

•0.0-0.5: 118 predictions, 8.6% avg confidence, 48.3% accuracy (Error: 39.7%)

Note: The high error in the 0.0-0.5 bin is expected and acceptable – these are cases where the model is very uncertain.

1.Strong Correlation (0.605): Confidence scores reliably predict accuracy

3.Appropriate Uncertainty: Low confidence on genuinely difficult cases

4.Consistent Performance: Good calibration across all datasets

5.Clear Confidence Patterns: Distinct accuracy levels for different confidence ranges

•Queries about “best/top rated [location-based service] reviews”

•Model sees location keywords and predicts Local instead of Commercial Investigation

The model’s confidence scores are highly trustworthy and can be relied upon for production deployment.

Query classification is about assigning meaning to a search query by mapping it to an intent, topic, or category .

Group keywords by intent or topic first, then by semantics. Don’t lump “how to fix iphone” with “iphone 15 price” just because they contain “iphone.”

→ Outcome: Clearer content maps, more focused pages, less keyword cannibalization.

Classify and filter keywords with “purchase” or “urgent” signals.

→ Outcome: Prioritize content that drives revenue or conversions.

Classify by SERP feature presence (via tools or scraping) and adjust content:

→ Outcome: Tighter ad groups = higher quality score and lower CPC.

→ Outcome: Smart bidding logic (bid up for “buy” queries, down on “compare”).

Imagine doing all of this — but with the exact categories or intents that matter to your business. You’re no longer stuck with someone else’s idea of ‘transactional.’ You define it yourself, and the model follows.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
