---
source: https://www.searchpilot.com/resources/blog/announcing-our-optimization-delivery-network
title: Announcing our Optimization Delivery Network
scraped: 2026-03-22
published_on: 2023-08-07T09:56:50+01
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

# Announcing our Optimization Delivery Network

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/announcing-our-optimization-delivery-network
Published: 2023-08-07T09:56:50+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
The original announcement (at the time on distilled.net) of the Optimization Delivery Network or ODN that would go on to become the SearchPilot platform.

## Extracted Body
[Editor’s note:] This post first appeared on distilled.net when we announced the platform that became SearchPilot which was initially built by Distilled before spinning out as an independent company before Distilled was acquired by Brainlabs .

There are two big problems with providing organic search consulting advice. The first is that it’s often exceptionally hard to get your recommendations implemented, and the second is that it’s often really hard to know how much of a difference your recommendations will make.

Today, I’d like to announce an early-stage product we are working on that is designed to alleviate both of these issues.

We are calling this type of platform an Optimization Delivery Network or ODN [Now: SearchPilot, Ed.]. It works like this:

It sits in your web stack like a content delivery network (or behind your content delivery network if you are using one).

It allows you to make arbitrary changes to the HTML (and HTTP headers) of any page or group of pages on your website - operating a little like a CMS over the output of your CMS and avoiding the need for a lengthy wait for your development backlog.

In addition, it makes it possible to make certain kinds of changes to subsets of pages in order to test to see what will work best - something that is surprisingly hard to do (does your CMS enable you to change just a set of pages within a wider group) and surprisingly hard to analyze (there’s only one Googlebot, so no CRO-style A/B testing here).

I talked about people who are doing this and some of the techniques and mathematical analysis at the end of my SearchLove London talk .

There’s an additional benefit here that it’s possible to do small-scale tests of things that may have a negative impact - but that you’d really like to be able to change - and only roll them out if you are confident you aren’t going to take a hit.

One of our core values [at Distilled, Ed.] is that we believe “it’s not our job to deliver reports. It’s our job to effect change” and so building this platform is exceptionally well-aligned with what we are trying to achieve. We have always believed in testing, and we think it is becoming more important as machine learning in the Google algorithm makes best practices less and less certain.
