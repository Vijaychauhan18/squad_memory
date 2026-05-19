---
source: https://www.searchpilot.com/resources/case-studies/the-video-schema-results-that-surprised-seo-experts
title: The Video Schema Results That Surprised SEO Experts
scraped: 2026-03-22
published_on: December 5, 2025
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

# The Video Schema Results That Surprised SEO Experts

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/case-studies/the-video-schema-results-that-surprised-seo-experts
Published: December 5, 2025
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
In this case study, we take a look at a test series intended to fix invalid video schema. Is removing invalid schema a guaranteed SEO win?

## Extracted Body
If you aren't familiar with the fundamentals of how we run controlled SEO experiments that form the basis of all our case studies , then you might find it useful to start by reading the explanation at the end of this article before digesting the details of the case study below. If you'd like to get a new case study by email every two weeks, just enter your email address here .

In this week’s #SPQuiz, we asked our followers on LinkedIn and X (formerly Twitter) why our customer's videos weren't showing in search results even though they were on article pages that were indexed and ranking appropriately.

Most of our followers thought videos weren't showing on SERPs because there was no dedicated watch page. Others thought it was because of JS load issues or that there was too much content on the page.

How much does video schema matter? In this test series, our customer wanted to find out the full impact of video schema on their article pages. They had noticed that, while their articles had videos, those videos weren’t showing in search results, even though their competitors’ videos were appearing. Their article pages did have embedded videos and appropriate video schema, so it was strange that their videos were missing from search results.

When we checked out Google Search Console, we identified the first possible culprit. Even though the video section within their article schema was all parsing correctly (no double brackets or missing commas!), Google wasn’t considering the video schema valid because it was missing the fields ‘uploadDate’ and ‘thumbnailURL.’ This was an easy fix using SearchPilot’s platform.

We set up and ran the test, expecting an easy win. But what we saw was surprising.

We double-checked Google Search Console and confirmed that Google was indeed recognizing the new, valid schema on our variant pages. In spite of this, Google still wasn’t indexing all these videos. Nothing had changed in search results, so there was no impact on organic traffic.

These results were so surprising that the customer wanted to know whether video schema was doing anything at all for their article pages. So we set up a new test fully removing the video section of the structured data, leaving the article schema without a video portion entirely. We thought that an inconclusive test result would prove that the customer was safe removing their invalid, difficult-to-maintain video schema section from their article pages. But we were in for another surprise:

When we removed the video section from the article schema entirely, traffic plummeted, with an estimated loss of -9.4% organic sessions. We knew that nothing we had done had changed the user experience in SERPs, since the videos still weren’t showing as indexed in Google Search Console, and no queries were able to bring them up when we checked likely search terms. Nothing about the video schema’s presence or absence changed the keywords that pages should rank for. So why would invalid video schema help a page rank better than no video schema at all?

We dug into Google Search Console again and found that during the period of the second test, flags for ‘missing field: video schema’ went up across articles in our variant bucket. The video field isn’t considered a necessary part of article schema, since millions of article pages online don’t have associated videos. And yet, Google seemed to assign greater value to articles that referenced videos through schema markup than to those without such markup–even though it was flagging that video schema as invalid.

As a reminder, this test only modified the article schema. Even our variant pages with video schema removed still had videos on the page. They were only missing the schema pointing out to Google that they contained videos.

That was a fascinating finding. Plus, when we dug deeper into Google’s video indexing, we found out why our customer’s videos weren’t showing in search results. Google only shows videos in rich results when those videos appear on a “Watch” page . Watch pages are supposed to be primarily about the video they feature; a page can’t be considered a Watch page if it includes large amounts of images and text, as all of their helpful step-by-step articles do. So there was no way for these videos to ever be indexed by Google if they appeared only on article pages. The only way to get them indexed would be to pull them out into their own separate pages, potentially cannibalizing traffic to the actual article pages.

This experiment was a great example of how surprising SEO A/B testing can be, and how iterative testing is a crucial part of a testing program. If we’d only run the first test, it would have been easy to assume that the video schema wasn’t doing anything on article pages and was safe to remove. Our second test uncovered a truly unexpected quirk of Google’s rankings, and helped our customer make the right choice to preserve traffic to their article pages.

To receive more insights from our testing, sign up for our case study mailing list , and please feel free to get in touch if you want to learn more about this test or our split testing platform more generally.

The most important thing to know is that our case studies are based on controlled experiments with control and variant pages:
