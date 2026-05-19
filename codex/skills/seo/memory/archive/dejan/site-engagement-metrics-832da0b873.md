---
source: https://dejan.ai/blog/site-engagement-metrics/
title: Site Engagement Metrics
scraped: 2026-03-25
published_on: 2024-11-29
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

# Site Engagement Metrics

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/site-engagement-metrics/
Published: 2024-11-29
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
To access the feature in Chrome visit: chrome://site-engagement/ Google Site Engagement Metrics Framework plays a crucial role in assessing and analyzing user engagement with websites. This framework leverages detailed metrics, such as user interactions and engagement scores, to provide insights into browsing behavior. Here’s a breakdown of how this system works, based on the Site […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

To access the feature in Chrome visit: chrome://site-engagement/

Google Site Engagement Metrics Framework plays a crucial role in assessing and analyzing user engagement with websites. This framework leverages detailed metrics, such as user interactions and engagement scores, to provide insights into browsing behavior. Here’s a breakdown of how this system works, based on the Site Engagement Metrics implementation.

Chromium uses a combination of pre-defined histograms and specialized functions to record and process engagement data. Here are some key functions within the framework:

INP, TBT, and other related metrics clearly indicate that user engagement metrics are being used, including the DOJ leaks, which help verify this. The document explains how Chrome engineers might measure engagement metrics, which is a valuable contribution from Dejan. Thank you for creating this insightful resource.

Any indication that this is being transmitted home to the mothership?

The docs are unclear about privacy aspects – there’s a mention of “Site Engagement clients” but I’d expect that this to be analogous to cookies – a website would only be able to access the engagement metric for its own domain. That could be a very wonky assumption. Very strange that the docs don’t describe who can access this data.

I find it too hard to follow the breadcrumbs but I know for a fact there’s a link to UKM / histograms.

https://web.dev/articles/persistent-storage#how_is_permission_granted

Respekt. Danke für den Artikel. Das klingt sehr interessant. 👍

This is an interesting take from pasting the code into ChatGPT. This system is used internally by Chromium-based browsers to personalise user experiences. For example:

* Suggesting frequently visited sites. * Prioritising notifications for highly engaged sites. * Enforcing browser policies or limits on sites with low engagement.

Astute! But I did a bit more than that, I have a whole chromium repo on my machine sifting through it in my spare time. It’s real fun!

Hi Dan, Thanks for breaking breaking down Google’s Site Engagement Metrics Framework so thoroughly. It’s crazy to see how detailed these metrics are in capturing user interactions.

What do you think is the most underrated engagement factor among these metrics that webmasters should prioritize but often overlook?

When a user agrees to install the website app. That one carries a lot of weight.

Hi Dan, I assume you are still running this. Any notable changes/learnings in the last year?

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
