---
source: https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget
title: Optimize your crawl budget
scraped: 2026-05-18
tags: google, official, crawl_budget, large_sites, discovery
topic: crawl_budget
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: large-site crawling strategy, crawl demand, and crawl-efficiency work
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Optimize your crawl budget

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget
Page updated label: 2025-12-19 UTC

## Why This Matters
large-site crawling strategy, crawl demand, and crawl-efficiency work

## Extracted Passages
- This guide describes how to optimize Google's crawling of very large and frequently updated sites.
- If your site doesn't have a large number of pages that change rapidly, or if your pages seem to be crawled the same day that they are published, you don't need to read this guide. For Google Search specifically, merely keeping your sitemap up to date and checking your index coverage regularly is adequate.
- While the recommendations in this guide are generally good practices, this is an advanced guide intended primarily for the following types of sites:
- The web is a nearly infinite space, exceeding Google's ability to explore and index every available URL. As a result, there are limits to how much time Google's crawlers can spend crawling any single site, where a site is defined by the hostname. For example, https://www.example.com/ and https://code.example.com/ are two different hostnames, and therefore have separate crawl budgets. The amount of time and resources that Google devotes to crawling a site is commonly called the site's crawl budget and it's determined by two main elements: crawl capacity limit and crawl demand .
- Google wants to crawl your site without overwhelming your servers. To prevent this, Google's crawlers calculate a crawl capacity limit , which is the maximum number of simultaneous parallel connections that Google can use to crawl a site, as well as the time delay between fetches. This is calculated to provide coverage of all your important content without overloading your servers.
- Each crawler has its own "demand" when it comes to crawling the web. For example, AdsBot generally has a higher demand when a site is running dynamic ad targets, Google Shopping has a higher demand for products you have in your merchant feeds, and Googlebot's demand varies based on a site's size, update frequency, page quality, and relevance, compared to other sites.
- Additionally, site-wide events like site moves may trigger an increase in crawl demand in order to reprocess the content under the new URLs.
- Taking crawl capacity and crawl demand together, Google defines a site's crawl budget as the set of URLs that Google can and wants to crawl. Even if the crawl capacity limit isn't reached, if crawl demand is low, Google will crawl your site less.
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

