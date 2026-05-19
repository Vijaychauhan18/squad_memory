---
source: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-redirecting-trailing-slash-urls
title: Does redirecting trailing slash URLs to the non
scraped: 2026-03-22
published_on: January 12, 2023
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

# Does redirecting trailing slash URLs to the non

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-redirecting-trailing-slash-urls
Published: January 12, 2023
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
For the first #SPQuiz of 2023 we looked at whether redirecting trailing slash URLs to the non-trailing slash URL had any impact on organic performance. These pages already had a canonical to the non-trailing slash URL, but got a small amount of organic traffic. We asked our followers on both Twitter and LinkedIn what they thought the impact would be on organic traffic. Here is what they thought: T﻿witter Poll Most of our Twitter followers thought this test wouldn’t have an impact on traffic that

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

For the first #SPQuiz of 2023 we looked at whether redirecting trailing slash URLs to the non-trailing slash URL had any impact on organic performance. These pages already had a canonical to the non-trailing slash URL, but got a small amount of organic traffic.

We asked our followers on both Twitter and LinkedIn what they thought the impact would be on organic traffic.

Most of our Twitter followers thought this test wouldn’t have an impact on traffic that we’d be able to detect, with almost a quarter thinking it would have a negative effect.

No detectable impact was also what the majority of our LinkedIn followers predicted would be the result, while only a handful thought it would have a detrimental impact.

As it turns out, those who voted inconclusive got it right. Read on to find out the details.

​​We know that having multiple versions of the same page on different URLs can cause issues with duplicated content, which can impact SEO in several ways. For example, creating cannibalised content in the search engine results pages, leading crawlers to not know which version of the page should be indexed and displayed in the search results.

There is also the question around link, trust, and authority signals, and whether these are directed to just one version of the page, or shared between all versions. This is something to be particularly mindful of if various versions of the URL are used within redirects, internal links, sitemaps, and backlinks.

One of our e-commerce customers had two versions of their pages with the same content:

Despite having a canonical pointing to the non-trailing slash URL, the trailing slash pages still received a small amount of organic traffic.

Given that both the trailing and non-trailing slash pages were receiving organic traffic, the customer saw this as an indication that there were two versions of certain pages being indexed in search results. Therefore, our customer wanted to use this test to see if there was an improvement to the organic traffic of the non-trailing slash URLs, by redirecting the trailing slash version to it with a 301 redirect.

We know that Google sees canonical tags as a hint, and may choose to ignore the one that is set or define their own based on a number of factors, such as internal links and sitemaps. On the other hand, redirects are directives, meaning Google must follow the instructions given by the site. Adding a redirect will therefore ensure, without any confusion, that only one version of the page will be indexed and consolidate all of the preferred signals.

Upon running this experiment, we saw an expected decrease of organic sessions to the pages that we redirected. While the non-trailing slash URLs did see a marginally positive impact, the result remained inconclusive at a statistically significant percentage:

Due to the strong hypothesis of this test, the fact that removing duplicate pages is best practice and that the change was not trending negatively, our customer decided to take a default to deploy approach. Despite not being statistically significant, there was evidence that our customer saw benefits by adding 301 redirects from trailing slash URLs to non-trailing slash URLs site-wide. Implementing this change is a simple task within the SearchPilot platform, and on some CMS systems, this redirect can be a relatively low-effort fix. However, for some websites the level of effort to implement is something to consider, particularly if a canonical tag is already in place.

Even though our customer likely saw some positive impact, it was not large enough to justify a high level of effort, despite being a standard SEO best practice recommendation. It’s also worth reviewing whether the duplicated pages receive any traffic or are appearing within SERPs as an indication as to whether implementing redirects would be worthwhile.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
