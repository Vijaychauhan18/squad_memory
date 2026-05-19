---
source: https://dejan.ai/blog/hacking-gemini/
title: Revealed: The exact search result data sent to Google’s AI.
scraped: 2026-03-25
published_on: 2025-03-14
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

# Revealed: The exact search result data sent to Google’s AI.

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/hacking-gemini/
Published: 2025-03-14
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
UPDATE: Addressing guardrails, hallucinations and context size. 1. People are reporting difficulties in recreating the output due to guardrails and hallucinations. 2. Snippet context sometimes grows to several chunks. Guardrails Google attempts (and in many cases) succeeds at blocking these requests, but it does so in a very clumsy way so that we actually get […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

UPDATE: Addressing guardrails, hallucinations and context size. 1. People are reporting difficulties in recreating the output due to guardrails and hallucinations. 2. Snippet context sometimes grows to several chunks.

Google attempts (and in many cases) succeeds at blocking these requests, but it does so in a very clumsy way so that we actually get hold of the partial output and can verify it is not a hallucination but it comes from actual search index.

The titles and descriptions supplied were recent and accurate and cannot possibly be part of model pre-training based internal world knowledge:

I’ve tested this in AI Studio with both Gemini 1.5 Pro and Gemini 2.0 Flash (both grounded) and it’s consistent with what I’m seeing in the Gemini App .

In the above screenshot we see grounding link which links to this URL , which redirects to vertex URL which then resolves to actual target URL for the query. No hallucinations, no broken links, real-time and up-to-date snippet information.

Some of you have been reporting hallucinations. This is nothing new or unusual, models do hallucinate, but this doesn’t disprove the non-hallucinated responses with verifiable real-time details.

Well, that’s not a correct way to phrase it to be fair. There’s something called “Dynamic retrieval” and is based on “confidence score” in Google’s search grounding API . Its role is to help developers determine whether grounding is required or not.

Gemini App is not aware of this context which is most likely abstracted away from it in a step before it receives actual grounding for example:

So as a result is the model is “confident” enough it will not be supplied with grounding context. It may answer in a way that makes sense but it is unlikely to get exact snippet information and URLs right and may results in 404 links and weird statements.

Over the last 3 months I’ve collected many thousands of grounding responses which are stored in the airank.dejan.ai database. So far I haven’t seen a single instance of grounded context that goes beyond query + title + short snippet format. Some of you have pushed back saying that we cannot be sure whether Gemini receives only a short snippet or maybe gets more than that.

I simply could not recreate any output that shows more than a short snippet in the last 90 days and so could not speculate on what I’m not able to test empirically and decided to reach out to Google for a statement.

Hey Logan, people giving me hard time when I say that Gemini App gets the same grounding as API users do: 1. Query 2. URL 3. Snippet (4) Confidence scores abstracted away. No page content or anything fancy. Is this a fair assessment?

And so as improbable as it is, this morning I run the modified query:

And the snippet suddenly switches to a multi-paragraph mode:

The above has been verified as genuine website copy and not any form of hallucination. I haven’t been able to replicate this in the Gemini App though.

I find this amusing because I feel for the model’s classic confidently wrong answers when being probed about the context size. To be fair the model had no actual knowledge that its tool is in fact able to supply larger context so it didn’t lie on purpose. I’m grateful for the skeptical SEO community to press me on this matter and discover the multi-passage grounding capability.

That said it’s unclear how often this rich context is actually supplied to the model as most of what I’ve seen so far was the skinny version.

JR Oakes made an interesting comment about this which I believe to be true:

A clear application of the grounding mechanism is immediately obvious in Google’s AI Mode :

Observe the summarisation in the snippet. It looks very much like what was later supplied as “additional_info” now known to be Gemini’s own summarisation rather than supplied to it by Google’s search index context.

Google’s Gemini model gets to take a peek at Google’s search results when chatting to users. This is called grounding. Grounded AI chat sessions are a type of retrieval augmented generation (RAG) where model no longer relies on its internal world knowledge alone, but also gets to see fresh and up-to-date information from a more dynamic system such as Google’s search index .

The above prompt works for Flash 2.0 Thinking Experimental with Apps.

My objective was to ascertain the level of brand-to entity-association between “Owayo” and “custom cycling jerseys” which I already track in AI Rank as described in this Search Engine Land article and in more technical detail here .

The following data was provided to Gemini alongside my query as added context:

In the above json, a set of results is supplied for the query including:

The significance of this is obvious and it highlights the importance of SEO in the context of AI driven brand, product and service discovery. Google relies on retrieval augmented generation (RAG) to enrich and update its model’s internal world knowledge.

It’s fascinating to see the exact format of the grounding data but I’d like to bring to your attention one particular aspect of this data. The text provided as part of the additional_info doesn’t appear to be coming from website copy, metadata nor any other external web asset.

We’re looking at Google’s own “quantized” impression of the brand. This summarisation essentially reveals what the brand has been reduced down to. If this doesn’t quite match the intended representation of your brand then you may have some content optimisation work to do.

Update : “The additional_info is a lightweight, snippet-based summarization. It’s intended to be helpful as a quick indicator, but it should not be considered a deeply analyzed or fully reliable representation of the linked webpage’s content. It’s definitely not a substitute for actually visiting and reading the page.” In short, Gemini sees url, title, query and snippet. It then generates that summary from it. Very shallow. Baffling in fact.

It’s also worth pointing out that the results were influenced by my location resulting in Gemini receiving Australian SERP grounding json which further influences model’s output.

This little exploit may work for a while but will almost certainly be patched up in the future.

If you’d like to get a sense for what AI models know about your brand and what competing brands it returns for queries that matter to you then do the following:

The tool is free in the demo mode with limit of 10 queries per project. There are currently 1,000 active users with a total of 4,000 tracked entities and 230,000 rank tracking datapoints. New features and insights from the collected data are expected to arrive almost weekly.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
