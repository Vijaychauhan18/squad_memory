---
source: https://dejan.ai/blog/from-hallucinations-to-clicks/
title: From Hallucinations to Clicks
scraped: 2026-03-25
published_on: 2025-06-02
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

# From Hallucinations to Clicks

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/from-hallucinations-to-clicks/
Published: 2025-06-02
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Anastasia Kotsiubynska proposed a method to repurpose LLM-hallucinated URLs and set up redirects from hallucinated 404 instances with more than one session to most similar valid 200 pages. I really like this, but since I work on websites with many millions of pages where volumes of hallucinated URLs are typically beyond the scope of manual […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Anastasia Kotsiubynska proposed a method to repurpose LLM-hallucinated URLs and set up redirects from hallucinated 404 instances with more than one session to most similar valid 200 pages.

I really like this, but since I work on websites with many millions of pages where volumes of hallucinated URLs are typically beyond the scope of manual human work I decided to automate this process by auto-mapping hallucinations to valid pages.

Other than taking the initial look at the server log files to get the idea of the types and volume of hallucinated URLs I’m really not keen on using it as a part of the pipeline as I’m aiming for simplicity.

The above is one hallucination instance from dejan.ai log files and the key bits of information I need are:

So for each 404 instance where a referral is https://chatgpt.com/ I can use both keyword and semantic similarity to map to the best existing page on the site. Keyword based matching can be extended by Levenshtein‐style fuzzy matching on top of keyword hits.

Semantic similarity obviously requires vector embeddings, and this requires careful consideration. Reasonable candidates for text embeddings include:

In most cases URL-extracted keywords are the best choice. I say most cases because not all sites have meaningful, descriptive URLs.

It’s because of one important quirk associated with cosine similarity. It’s biased by input text length due to additional semantic context and keyword diversity. This means that when selecting between two perfectly reasonable semantic matches it will always pick a shorter one as a better match.

Assume the hallucinated URL is: https://dejan.ai/ labs/interactive-demo and since there’s no page content or meta data we go by URL keyword extraction and end up with labs, interactive, and demo .

We’ll test them with text variants as potential matching targets:

I’m currently working on a 25 million page website and embedding generation takes about 24 hours to complete.

I’ve opted in for a custom, binary compression on my embeddings so the final output will be only around 30GB.

Note: In most cases this is complete overengineering and you can probably get by keyword matching, but I have further uses for vector embeddings (e.g. internal link optimisation) and it makes sense to do this. For small sites, manual mapping is a perfectly reasonable way to go.

What happens next is up to you. Personally, I will not implement any redirects – too risky. Cosine similarity is blind to common sense and will find whatever is closest matching which could include explicit, illegal and embarrassing things.

My choice is to keep 404 pages and either recommend top related pages or render the page content or snipped as part of the 404 page. This provides user with a place to go while avoiding unwanted associations.

Cosine similarity is probably not the way to go for the reasons you mentioned, so an implementation that ignores semantic similarity is probably safer. Fuzzy matching with a dictionary of known good slugs wouldn’t handle every situation, but handle enough to be valuable. I don’t know enough about it to think of the specifics, but I’ve seen it in action for things like URL case handling.

Semantic similarity can be used as a helping metric, but not a deciding factor.

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
