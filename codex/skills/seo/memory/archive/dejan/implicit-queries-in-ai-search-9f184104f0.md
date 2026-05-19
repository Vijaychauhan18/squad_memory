---
source: https://dejan.ai/blog/implicit-queries-in-ai-search/
title: Implicit Queries in AI Search
scraped: 2026-03-22
published_on: 2026-02-24
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

# Implicit Queries in AI Search

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/implicit-queries-in-ai-search/
Published: 2026-02-24
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Back in 2015 I wrote about Google’s reliance of user behaviours signals for ranking purposes. In that article I already covered their use of implicit signals, but now there’s an update! While investigating Google’s grounding pipeline (the system that feeds web content to Gemini before it generates an answer) I came across the same patent […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Back in 2015 I wrote about Google’s reliance of user behaviours signals for ranking purposes. In that article I already covered their use of implicit signals , but now there’s an update!

While investigating Google’s grounding pipeline (the system that feeds web content to Gemini before it generates an answer) I came across the same patent most of us already looked at ( US11769017B1 ), titled “Generative summaries for search results” , filed March 2023 and assigned to Google LLC. Most of it describes the AI Overview pipeline we already know: select search result documents, extract content, feed it to an LLM, generate a summary, linkify portions back to sources. Standard grounding architecture.

But buried in the system description are two components that skipped my attention: the Context Engine and the Implied Input Engine .

The patent describes a client-side system architecture with named components. Here’s what it outlines, in Google’s own words:

The client device 110 can include a context engine 113 that is configured to determine a context (e.g., current or recent context) of the client device 110 and/or of a user of the client device 110.

The client device 110 can include an implied input engine 114 that is configured to: generate an implied query independent of any user input directed to formulating the implied query; to submit an implied query, optionally independent of any user input that requests submission of the implied query; and/or to cause rendering of result(s) for an implied query, optionally independent of any user input that requests rendering of the result(s).

The implied query can be “patent news” based on profile data indicating interest in patents, the implied query periodically submitted, and a corresponding NL based summary result automatically rendered. It is noted that the provided NL based summary result can vary over time in view of e.g., presence of new/fresh search result document(s) over time.

So the system profiles your interests, generates a standing query, resubmits it at intervals, and auto-renders updated AI summaries as new content appears on the web. A personalised, recurring, AI-curated news feed, driven entirely by inferred intent.

The context engine doesn’t just know what app you’re using. It knows what you’re looking at inside the app :

The context engine 113 can determine a current context based on which application is active in the foreground of the client device 110, a current or recent state of the active application, and/or content currently or recently rendered by the active application.

And it uses this to rewrite your actual queries or generate entirely new ones:

A context determined by the context engine 113 can be utilized, for example, in supplementing or rewriting a query that is formulated based on user input, in generating an implied query (e.g., a query formulated independent of user input), and/or in determining to submit an implied query and/or to render result(s) (e.g., an NL based summary) for an implied query.

The implied input engine 114 can automatically push result(s) to the implied query to cause them to be automatically rendered or can automatically push a notification of the result(s), such as a selectable notification that, when selected, causes rendering of the result(s).

This isn’t a search engine anymore. It’s an anticipatory information system. The shift is fundamental:

Traditional search: User has intent → types query → receives results.

This patent: Device observes behaviour → system infers intent → generates query → retrieves results → pushes AI summary.

The user never searches. The system decides what information to deliver, when to deliver it, and how to present it, all wrapped in an LLM-generated natural language summary grounded in real search results.

For those following our grounding research , this patent describes the full architecture behind what we’ve been reverse-engineering from the API side:

This maps directly to the grounding metadata structure we’ve observed: source indices, snippets, confidence scores, and the redirect URLs through vertexaisearch.cloud.google.com .

A portion with a high confidence measure can be annotated in a first color (e.g., green), a portion with a medium confidence measure can be annotated in a second color (e.g., orange), and a portion with a low confidence measure can be annotated in a third color (e.g., red).

And it uses confidence to decide whether to even show you the AI summary at all, or fall back to traditional search results:

If confidence measure(s) for portion(s) and/or a confidence measure for the NL based summary as a whole satisfies upper threshold(s) most indicative of confidence, the NL based summary can be rendered responsive to the query and without any initial rendering of any additional search results .

When confidence is high, search results are suppressed entirely. Only the AI summary appears.
