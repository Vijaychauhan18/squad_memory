---
source: https://moz.com/blog/num-100-and-changing-serp-lengths-in-moz-pro
title: Google &num= and Changing SERP lengths in Moz Pro
scraped: 2026-03-22
published_on: 2025-10-14
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

# Google &num= and Changing SERP lengths in Moz Pro

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/num-100-and-changing-serp-lengths-in-moz-pro
Published: 2025-10-14
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Raise your local SEO visibility with complete local SEO management.

## Extracted Body
September 2025 saw some major disruptions in the SEO tools and data industry with the removal of a widely used Google parameter &num= . We’ve been able to deliver consistent and unaffected data in Moz Pro and the Moz API so far, thanks to prior preparation and the resilience of our systems. That said, we wanted to share our thoughts, and our plan going forward.

Virtually every SEO tool is powered by scraped search results. In order to get more insight from each scrape—and thus keep costs down for end users—tools generally use this parameter to force extended search results on the first page, instead of the typically 10 regular organic results a user would see by default. Moz Pro, for example, has for a long time standardized on &num=50 – so 5 “pages” of results per scrape.

This parameter had actually been deprecated for many years, but continued to be unofficially supported. In mid-September, it started to slowly stop working, forcing SEO tools to seek alternative methods. Some tools–including Moz and STAT–prepared an alternative we call “stitching”, where we piece together a series of paginated results, 10 at a time, into one longer set of results. There are various difficulties with this approach, many of which can be mitigated or avoided, but the main implication is cost, which ends up being significantly higher, to the point of being unsustainable in many cases.

This should also be seen in the context of SERP data costs generally increasing in recent years, as tools are forced to mimic real browsers more and more closely in order to get accurate, representative rankings.

The rankings that SEOs should care most about are clearly those on the first 1-2 pages of results. Very few users are scrolling down to position 40. That said, deeper SEO analysis and metrics do benefit greatly from the information gained from these deeper results. This includes tools like Keyword Explorer and our link index.

We want to strike a balance between providing a good value, accessible product, and providing the best data possible to our users. As such, for Moz Pro and Moz APIs, we are taking a hybrid approach, starting from 20th October, 2025:

For STAT, we are pursuing a more flexible approach, which will provide clients with a range of options to suit their diverse needs.

Many have speculated that this might be an attempt by Google to sabotage ChatGPT, which is powered to a large degree by scraped Google search results. This explanation is appealing but has a couple of issues:

Perhaps Google is happy to accept a war of attrition on this front. Another likely explanation is that this long-deprecated parameter simply stopped working as part of another update. Perhaps the same update that seems to have changed how impressions are measured in Google Search Console in the last few weeks (we don’t think bots can have been driving enough traffic per term to drive the impression changes that many sites are seeing).

We’ll continue to strive to provide reliable, consistent, and accurate data to our customers, as we have done throughout this period. If you are a Moz Pro customer and have any questions, feel free to contact support .

Come chat with the Moz and STAT team at Brighton SEO this month. I’ll also be speaking on Friday afternoon , swing by and say hi!

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
