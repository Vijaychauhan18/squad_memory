---
source: https://dejan.ai/blog/google-lens-modes/
title: Google Lens Modes
scraped: 2026-03-25
published_on: 2025-05-07
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

# Google Lens Modes

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/google-lens-modes/
Published: 2025-05-07
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
lns_mode is a parameter that classifies Google Lens queries into text, un (unimodal), or mu (multimodal). Google Lens has quietly become one of the most advanced visual search tools in the world. Behind the scenes, it works by constructing detailed, context-rich search queries that include a growing set of parameters. One of the newest additions […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

lns_mode is a parameter that classifies Google Lens queries into text , un (unimodal), or mu (multimodal).

Google Lens has quietly become one of the most advanced visual search tools in the world. Behind the scenes, it works by constructing detailed, context-rich search queries that include a growing set of parameters. One of the newest additions to this query structure is lns_mode , introduced on May 14, 2024 by Google engineer Jason Hu.

This article breaks down what lns_mode is, how it fits into the broader Google Lens ecosystem, and why it matters – especially as Lens evolves into a key component of Google’s new AI Mode .

The lns_mode parameter is a query string field appended to URLs generated during Lens-powered searches. It serves as a high-level indicator of the type of search being executed. Based on Chromium source files, the known values are:

This field complements others like q (query), gsc=1 , masfc=c , and hl (locale).

Inside Chromium, lns_mode is added in the Lens Overlay URL builder logic. Functions like BuildTextOnlySearchURL() and BuildLensSearchURL() select the mode dynamically based on the presence of OCR text, screenshots, or user-selected regions.

Below is a breakdown of the most common query parameters used in Google Lens search URLs:

These parameters are assembled automatically by Chrome and Lens-backed apps when performing visual search, with each field enabling a richer, more context-aware response from Google’s backend systems.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
