---
source: https://www.oncrawl.com/technical-seo/using-devtools-to-identify-traffic-drops/
title: Using DevTools to Identify Traffic Drops - Oncrawl
scraped: 2026-03-23
published_on: 2020-03-05
tags: live_feed, phase1_ingest, oncrawl, publication, technical-seo, ai-visibility, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Oncrawl
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Using DevTools to Identify Traffic Drops - Oncrawl

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/using-devtools-to-identify-traffic-drops/
Published: 2020-03-05
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
For any webmaster, witnessing either a sudden or gradual decline in organic traffic isn’t a great experience.This is where DevTools can come in handy and complement your suite of third-party tools.

## Extracted Body
For any webmaster, witnessing either a sudden or gradual decline in organic traffic isn’t a great experience.

This is where DevTools can come in handy and complement your suite of third-party tools.

To open DevTools, you can right-click on a webpage and click on “inspect”, or by clicking on the three-dot burger menu in the top right-hand corner of the browser, and selecting More Tools > Developer Tools.

We’ll look at three ways to use DevTools for diagnosing traffic drops.

Being able to emulate search results from various locations, especially if your client has physical bricks-and-mortar stores, and specifically being able to emulate local search results from various locations can prove invaluable.

Location spoofing can also prove useful for eCommerce businesses, as product-related “buy intent” search queries can have multiple common interpretations, and sometimes a product can be available locally. By location spoofing in different towns and cities, you can get an idea for how local Google is treating the query, and if you’re potentially losing out on traffic to SERP elements like the Map Pack.

DevTools comes with a predefined list of locations, but you can also add custom locations via GPS coordinates.

You can find GPS coordinates from third-party websites, such as LatLong , or through Google Maps .

Whilst this issue isn’t commonplace, it has reared its ugly head on a couple of traffic drop audits I’ve done in the past 18 months. Once resolved, it has correlated with improved performance.

From the Network tab in DevTools, you can easily identify which JavaScript and CSS resources are “render-blocking”, e.g. being loaded before the DOM (Document Object Model).

You can also identify non-critical CSS and JavaScript through the Coverage tab (found in Sources):

Google Lighthouse identifies three types of blocking resources:

Via DevTools you can check webpages (and parts thereof) for differences between the DOM and the source code, which can be very useful for checking if the webpage (or part of it) has been pre-rendered successfully.

View Source shows you the HTML that makes up a webpage and is the HTML that has been delivered from the origin server to the browser. But this isn’t always the case.

The HTML served by your origin server can be manipulated by JavaScript, by the CDN or middleware (e.g. edge SEO ), and even by the browser. Through the DevTools you can view the DOM after:

A good example of this is the browser correcting an invalid HTML syntax. For example, the below code snippet you would see through view-source:

But via DevTools, you’ll find that the syntax error on line 7 has actually been corrected by the browser:

Depending on the auditing tool you use, if any, this may not get picked up if the tool renders the page and DOM via a headless browser, and this issue is self-corrected.

Assessing a traffic drop is never an easy task as there is very rarely a single needle within the haystack and an exact solution. But as we’re experiencing what feels like a more regular change schedule from Google, being able to effectively analyze and audit both internal and external factors affecting your website is crucial.

DevTools gives you a free and straightforward way to examine individual web pages within the browser, providing a look at crucial technical elements that can affect SEO performance.
