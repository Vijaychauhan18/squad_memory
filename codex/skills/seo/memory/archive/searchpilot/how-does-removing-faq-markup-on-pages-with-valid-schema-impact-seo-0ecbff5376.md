---
source: https://www.searchpilot.com/resources/case-studies/removing-valid-faq-schema
title: How does removing FAQ markup on pages with valid schema impact SEO?
scraped: 2026-03-25
published_on: November 20, 2024
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

# How does removing FAQ markup on pages with valid schema impact SEO?

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/removing-valid-faq-schema
Published: November 20, 2024
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
In this week's #SPQuiz, one of our ecommerce customers conducted a test on the impact of removing valid FAQ markup on their category pages.

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

For this week's #SPQuiz , we asked our followers on X/Twitter and LinkedIn what they believed the impact was on organic traffic when we removed valid FAQ markup on an ecommerce customer's PLPs.

Our followers were roughly evenly split between those who thought removing the valid FAQ markup would be beneficial and those who thought it would be harmful, with a slightly larger group predicting that it would not impact organic traffic.

For some time, FAQ schema markup held a valuable place in SEO as Google's inclusion of these snippets under search listings helped these pages enhance visibility and user engagement.

However, as of August 2023, Google has decided to stop displaying FAQ snippets in the search engine results pages for websites unless they are well-known or authoritative, such as government and health sites.

This change raises an important question: Does FAQ schema markup still contribute to SEO, or could it potentially harm performance?

In light of this update, we tested the microdata FAQ schema on an ecommerce customer's product listing pages (PLPs) by removing the attributes itemprop , itemscope , and itemtype from the in-line FAQ within the SEO content block.

Removing valid FAQ schema alone had no statistically significant impact on organic traffic. Based on our test, this suggests that since snippets no longer appear in the SERP, the FAQ schema doesn't influence traffic positively or negatively.

Though our data does not indicate that removing FAQ schema will lead to increased organic traffic, companies may choose to remove it anyway, as eliminating code makes maintenance easier - primarily when it is implemented via microdata, which is more difficult to QA visually than JSON-LD. Other businesses may choose to leave their FAQ markup in place and only remove it in the future when the page type is eventually refactored.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
