---
source: https://www.searchpilot.com/resources/blog/internal-linking-tests
title: How to test internal links for SEO
scraped: 2026-03-22
published_on: 2025-04-07T18:33:51+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How to test internal links for SEO

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/internal-linking-tests
Published: 2025-04-07T18:33:51+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Someone born in the year I started Distilled would be learning to drive in the next year, and I still don’t really understand internal linking. I don’t think I’m alone. So we need to test! The big difference between regular on-page tests and internal linking tests is that the hypothesis can be about effects on the page where you are making the change (the “source” of the link) and on the pages receiving the new links (the “destination” of the links).

## Extracted Body
Someone born in the year I started Distilled would be learning to drive in the next year, and I still don’t really understand internal linking.

Part of the problem, of course, is that Google doesn’t tell us exactly how they think about links at all, never mind how they think about internal links, but as I’ve written about before , I don’t think that really matters. Even if they just used basic PageRank ( explainer here ), or if they published the exact algorithms they use to evaluate links, we wouldn’t be much better off, because the scale of the link graph is so far beyond human comprehension.

If you would like to see me talk through the issues and thoughts in this post, I recorded a video:

Bring the scale back to one we can comprehend and we don’t do much better - in a quiz about a toy model of basic PageRank and a tiny site, fewer than 25% of respondents got the correct answer:

(The right answer is that it loses (a lot) less than the PR of the new page ).

It’s easy to fall back on simple heuristics like “more interlinking is better” or “minimise the number of clicks from the homepage to reach any page, without adding more than X links per page” but it’s very unlikely that any of these actually give the best answer.

Although adding individual links always feels likely to be a good idea, there is a trade-off between directing authority to most important pages vs crawl depth and crawl paths - there has to be a limit somewhere - you can’t link to every page on your website from every other page and expect it to be a good idea.

The big difference between regular on-page tests and internal linking tests is that the hypothesis can be about effects on the page where you are making the change (the “source” of the link) and on the pages receiving the new links (the “destination” of the links).

To run these tests we typically define a measurement section where we look for statistically significant effects. Sometimes we measure the impact separately on the source and destination pages, sometimes those are the same things.

We have a process we call salt shaking that evaluates a load of statistical features within a site section to choose groups of statistically similar pages for control and variant. That’s how we can reliably attribute measured uplifts to the changes we are testing for on-page changes, and it’s a similar process for linking tests.

The nature of internal linking changes, as explained at the outset, is that the effects can be felt widely across the site. The most advanced level of internal linking test measures all of:

This third kind of experimental design relies on working with a site with a strong category / sub-category structure, but should capture the effect of the dilution of internal linking within the site section when new links are added into some of the pages within the section.

Of course, if you build an experiment like this, you will get data about the likely impact for each of the groups of pages, and will need to evaluate its performance in each area and consider the net effect and statistical significance individually and as a group.

We also have a write-up coming soon of a test measuring the impact of updating the anchor text of some existing internal links . Make sure you’re on our email list to get the case study as soon as it’s published.

A publisher customer experimented with adding more links to related articles and found an uplift on the “donor” pages (the source of the links), but no conclusive evidence either way for the recipient pages . It’s possible that, in that case, the UX impact or the on-page impact was bigger than the linking impact or at least more measurable.

A customer with ~8,000 regional pages across the USA tested adding links to the 6 nearest geographic regions and saw a 7% uplift in organic traffic on the pages receiving new links .

A travel customer tested expanding their homepage footer . Normally, you can’t include the homepage in a split test, but because in this case, our hypothesis was about the impact on the destination pages, we were able to use our modelling to compare the impact of the pages receiving new links to a control group that didn’t receive new links. The pages that received links from the homepage footer saw a 5% uplift in organic traffic compared to a control group of pages that didn’t receive new links.

In a case study that we haven’t published yet, a customer tested changing the anchor text of internal links that already existed. They didn’t add or remove any links - just changed the text to include more contextual keywords, but measured the impact in the same way as for other internal linking tests.

This was significantly positive for the destination pages , just by changing the anchor text. Subscribe here to be the first to know when we publish the full details of this test .
