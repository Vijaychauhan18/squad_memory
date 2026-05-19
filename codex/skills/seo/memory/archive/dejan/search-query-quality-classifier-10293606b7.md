---
source: https://dejan.ai/blog/search-query-quality-classifier/
title: Search Query Quality Classifier
scraped: 2026-03-25
published_on: 2024-08-30
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

# Search Query Quality Classifier

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/search-query-quality-classifier/
Published: 2024-08-30
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
We build on the work by Manaal Faruqui and Dipanjan Das from Google AI Language team to train a search query classifier of well-formed search queries. Our model offers a 10% improvement over Google’s classifier by utilising ALBERT architecture instead of LSTM. With accuracy of 80%, the model is production ready and has already been […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

We build on the work by Manaal Faruqui and Dipanjan Das from Google AI Language team to train a search query classifier of well-formed search queries . Our model offers a 10% improvement over Google’s classifier by utilising ALBERT architecture instead of LSTM. With accuracy of 80% , the model is production ready and has already been deployed in Dejan AI’s query processing pipeline. The role of the model is to help identify query expansion candidates by flagging ambiguous queries retrieved via Google Search Console API.

For training we use Google’s training dataset and partially data provided by Owayo .

You can see the model in action by trying natural question versus keyword-based queries.

Have started using your query expansion classifier. However I am unable to the benefit of Well formedness Factor as the result. Could you please elaborate on this.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
