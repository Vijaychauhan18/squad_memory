---
source: https://dejan.ai/blog/grounding-classifier/
title: Introducing Grounding Classifier
scraped: 2026-03-25
published_on: 2025-04-02
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

# Introducing Grounding Classifier

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/grounding-classifier/
Published: 2025-04-02
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Using the same tech behind AI Rank, we prompted Google’s latest Gemini 2.5 Pro model with search grounding enabled in the API request. A total of 10,000 prompts were collected and analysed to determine the grounding status of the prompt. The resulting data was then used to train a replica of Google’s internal classifier which […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Using the same tech behind AI Rank , we prompted Google’s latest Gemini 2.5 Pro model with search grounding enabled in the API request. A total of 10,000 prompts were collected and analysed to determine the grounding status of the prompt. The resulting data was then used to train a replica of Google’s internal classifier which determines if query deserves grounding .

This is a commercial-grade model we now use as part of our machine learning toolkit and various data processing pipelines. The model’s capability is demonstrated in our QDG tool .

The discovery of Gemini’s grounding in a live production environment matches the official Google documentation for developers. The default dynamic retrieval threshold for determining whether user query requires grounding is 0.3 and the responses to user queries can be drastically different when grounded.

To see the difference in raw output between the two, click on the example prompts to expand for full detail:

Parsing the raw output enabled us to determine the label for each of the 10,000 prompts and generate a robust training dataset based on the decisions made by Google’s own classifier.

In order to address the class imbalance between grounded and ungrounded responses (0 and 1) in the original dataset we also generated synthetic training data. To do so, an entire classification corpus was supplied to Gemini as a system prompt and it was instructed to generate additional examples in the minority class to pad the training dataset.

We fine-tuned Microsoft’s DeBERTaV3 (large) model for binary text classification task using a 90:10 dataset split for training and validation and evaluated model performance by monitoring training loss, validation loss, precision, recall, accuracy and F1, which was also used to select the best model.

The model was trained for 5 epochs on a single RTX4090 using a batch size of 24 samples, checkpointing/validating every 500 steps and logging to Weights and Biases every 10 steps.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
