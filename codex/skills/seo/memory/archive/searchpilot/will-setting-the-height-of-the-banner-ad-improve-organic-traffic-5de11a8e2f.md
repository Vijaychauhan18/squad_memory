---
source: https://www.searchpilot.com/resources/case-studies/set-banner-height-for-cls
title: Will setting the height of the banner ad improve organic traffic?
scraped: 2026-03-22
published_on: August 15, 2024
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

# Will setting the height of the banner ad improve organic traffic?

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/set-banner-height-for-cls
Published: August 15, 2024
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
In this week's #SPQuiz, one of our customers tested setting a specific height for their banner ads to minimize cumulative layout shift (CLS).

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

For this week's #SPQuiz , we asked our followers how setting a specific height for a customer’s banner ads would affect organic traffic. The goal of this change was to minimize cumulative layout shift (CLS).

The majority of voters on X/Twitter and LinkedIn thought that the results would be inconclusive, but it is interesting that no one thought this test would have a negative result.

Cumulative Layout Shift (CLS) is a measurement of how much the elements above the fold shift as the page loads, and is an integral metric of overall page performance. Being one of the three pillars of Google’s Core Web Vitals (CWV), it is used as a part of Google’s ranking algorithm.

Ads are notorious for negatively impacting the CLS score because they are typically rendered by JavaScript, causing other elements to shift up and down the page. One of our customers in the e-commerce space wanted to see if predetermining the height of their banner ad would reduce its negative impact on CLS and increase their rankings as a result. Keep reading to see if they were right!

This test resulted in an inconclusive impact on organic traffic. This likely happened because the layout shift caused by the ad banner had a less significant effect on the CLS score than we initially believed. While the banner did cause some degree of layout shift, it was not substantial enough to significantly influence our rankings.

Despite this result being inconclusive, improving CLS is a change that we might consider default to deploy . The hypothesis around specifying a banner height to improve CWV scores is strong, the change is easy to implement, and as we can see from the result it is more likely to be positive than negative. By deploying this change we can capture uplifts that might be too small for us to measure, but these uplifts will compound over time. After all we are doing business, not science .

We generally test CWV hypotheses less because they usually involve dev support to make a change to the page that improves performance. That being said, CWV are no less valuable than any other branch of SEO and with SearchPilot’s request modification capabilities they are easier than ever to test.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
