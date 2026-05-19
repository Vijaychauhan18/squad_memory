---
source: https://moz.com/blog/state-of-web-and-core-web-vitals-part-one
title: Are We There Yet? The State of the Web & Core Web Vitals [Part 1]
scraped: 2026-03-23
published_on: 2021-10-05
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Are We There Yet? The State of the Web & Core Web Vitals [Part 1]

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/state-of-web-and-core-web-vitals-part-one
Published: 2021-10-05
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
In part one of a new series on Core Web Vitals, Tom explores what has gone wrong with Google's new metrics, where we stand now, and why you still need to care.

## Extracted Body
No, please, do read on. This is a post about what has gone wrong with Core Web Vitals and where we stand now, but also why you still need to care. I also have some data along the way, showing how many sites are hitting the minimum level, both now and back at the original intended launch date.

At the time of writing, it’s nearly a year and a half since Google told us that they were once again going to pull their usual trick: tell us something is a ranking factor in advance, so that we improve the web. To be fair, it’s quite a noble goal all told (albeit one they have a significant stake in). It’s a well trodden playbook at this point, too, most notably with “ mobilegeddon ” and HTTPS in recent years.

Both of those recent examples felt a little underwhelming when we hit zero-day, but the “Page Experience Update”, as Core Web Vitals’ rollout has been named, has felt not just underwhelming, but more than a little fumbled. This post is part of a 3-part series, where we’ll cover where we stand now, how to understand it, and what to do next.

Google was initially vague, telling us back in May 2020 that the update would be “in 2021”. Then, in November 2020, they told us it’d be in May 2021 — an unusually long total lead time, but so far, so good.

The surprise came in April, when we were told the update was delayed to June. And then in June, when it started rolling out “very slowly”. Finally, at the start of September, after some 16 months, we were told it was done.

So, why do I care? I think the delays (and the repeated clarifications and contradictions along the way) suggest that Google’s play didn’t quite work out this time. They told us that we should improve our websites’ performance because it was going to be a ranking factor. But for whatever reason, perhaps we didn’t improve them, and their data was a mess anyhow, so Google was left to downplay their own update as a “ tiebreaker ”. This is confusing and disorientating for businesses and brands, and detracts from the overall message that yes, come what may, they should work on their site performance.

As John Mueller said , “we really want to make sure that search remains useful after all”. This is the underlying bluff in Google’s pre-announced updates: they can’t make changes that cause the websites people expect to see, to not rank.

You may be familiar with our lord and savior, Mozcast , Moz’s Google algorithm monitoring report. Mozcast is based on a corpus of 10,000 competitive keywords, and back in May I decided to look at every URL ranking top 20 for all of these keywords, on desktop or on mobile, as tracked from a random location in the suburban USA.

This was some 400,000 results, and (surprisingly, I felt) ~210,000 unique URLs.

At the time, only 29% of these URLs had any CrUX data — this is data collected from real users in Google Chrome, and the basis of Core Web Vitals as a ranking factor. It’s possible for a URL to not have CrUX data because a certain sample size is needed before Google can work with the data, and for many lower traffic URLs, there is not enough Chrome traffic to fill out this sample size. This 29% is an especially depressingly low number when you consider that these are, by definition, higher traffic pages than most — they rank top 20 for competitive terms, after all.

Google has made various equivocations around generalizing/guesstimating results based on page similarity for pages that don’t have CrUX data, and I can imagine this working for large, templated sites with long tails, but less so smaller sites. In any case, in my experience working on large, templated sites, two pages on the same template often had vastly different performance, particularly if one was more heavily trafficked, and therefore more thoroughly cached.

Anyhow, leaving that rabbit hole to one side for a moment, you might be wondering what the Core Web Vitals outlook actually was for this 29% of URLs.

Some of these stats are quite impressive, but the real issue here is that “all 3” category. Again Google has gone and contradicted itself back and forth on whether you need to pass a threshold for all three metrics to get a performance boost, or indeed whether you need to pass any threshold at all. Still, what they have told us concretely is that we should try to meet these thresholds, and what we haven’t done is hit that bar.

30.75% passed all thresholds, of the 29% that even had data in the first place. 30.75% of 29% roughly equals 9%, 9% of URLs or thereabouts can concretely be said to be doing alright. Applying any significant ranking boost to 9% of URLs probably isn’t good news for the quality of Google’s results — especially as household name brands are very, very likely to be rife among the 91% left out.

So this was the situation in May, which (I hypothesize) led Google to postpone the update. What about August, when they finally rolled it out?

CrUX data availability increased from 29% to 38% between May and August 2021.

The rate of URLs with CrUX data passing all three CWV thresholds increased from 30.75% to 36.3% between May and August 2021.

So, the new multiplication (36.3% of 38%) leaves us at 14% - a marked increase over the previous 9%. Partly driven by Google collecting more data, partly by websites getting their stuff together. Presumably this trend will only increase, and Google will be able to turn up the dial on Core Web Vitals as a ranking factor, right?

In the meantime, if you're curious about where you stand for your site's CWV thresholds, Moz has a tool for it currently in beta with the official launch coming later this year.

And if you really want to nerd out, see how you score against the industry at large on these distribution charts from the August data:

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
