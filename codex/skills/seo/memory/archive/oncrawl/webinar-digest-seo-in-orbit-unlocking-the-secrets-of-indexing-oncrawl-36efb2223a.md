---
source: https://www.oncrawl.com/technical-seo/unlocking-secrets-indexing/
title: [Webinar Digest] SEO in Orbit: Unlocking the secrets of indexing - Oncrawl
scraped: 2026-03-23
published_on: 2019-11-06
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

# [Webinar Digest] SEO in Orbit: Unlocking the secrets of indexing - Oncrawl

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/unlocking-secrets-indexing/
Published: 2019-11-06
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
The webinar "Unlocking the secrets of indexing" with Kevin Indig is a part of the SEO in Orbit series, and aired on June 12th, 2019.

## Extracted Body
The webinar Unlocking the secrets of indexing is a part of the SEO in Orbit series, and aired on June 12th, 2019. In this episode, Kevin Indig shares his thoughts on getting pages indexed, how the pages indexed for a site influence site-wide rankings, and what pages shouldn’t be indexed. What is the right approach towards this intermediary step between getting pages discovered and getting them to appear on SERPs?

SEO in Orbit is the first webinar series sending SEO into space. Throughout the series, we discussed the present and the future of technical SEO with some of the finest SEO specialists and sent their top tips into space on June 27th, 2019.

Kevin Indig has helped startups acquire +100M users over the last 10 years. He is VP SEO & CONTENT @ G2, a mentor for Growth @ GermanAccelerator, and ran SEO @ Atlassian and Dailymotion previously. His specialty is user acquisition, brand building, and user retention. Companies Kevin worked with include eBay, Eventbrite, Bosch, Samsung, Pinterest, Columbia, UBS, and many others. He also runs the curated technical marketing newsletter, Tech Bound .

This episode was hosted by Rebecca Berbel, the Content Manager at Oncrawl. Fascinated by NLP and machine models of language in particular, and by systems and how they work in general, Rebecca is never at a loss for technical SEO subjects to get excited about. She believes in evangelizing tech and using data to understand website performance on search engines.

One of the reasons it’s important to talk about indexing is that it’s a complex topic. Many SEOs struggle with indexing and how to influence it.

You create a new page. Which of the following will keep it out of Google’s index?

A. Meta robots noindex B. Robots.txt block C. Giving the page meta noindex *and* blocking it in robots.txt

Crawling in simple terms is the technical discovery process of search engines understanding a web page and all of its components.

This helps Google find all of the URLs that it can then go back and render, and then index and eventually rank.

Crawling is part of Google’s 3-step process that leads up to being able to create search results:

These are technically different processes, handled by different programs, or parts of the search engine.

Indexing is the process of Google adding URLs to it’s long “list” of possible results. If Kevin has to avoid the word “index” in a definition of indexing, he’d prefer to talk about a metaphorical “list”: Google has a “list” of URLs that it can use to rank and show as best results to users.

Web servers keep a history any time anyone or anything asks for a page or a resource on the server.

Kevin is really passionate about log files as a source of truth when it comes to understanding how Google crawls and renders your site.

In the logs, we can find server information as to how often Google visits your site and what it does there, in very plain and simple terms. Log files contain individual records of each visit to the site.

When Kevin started out in SEO about 10 years ago, he would see what pages on his site were indexed by running “site:” searches on Google. While he still uses this sometimes, it’s no longer a reliable way to find out whether a URL is indexed.

More recently, he asked John Mueller about this strategy; he verified that this is no longer recommended way to check what Google has or hasn’t indexed.

John Mueller instead recommends using the URL Inspection Tool in the Search Console to check what has been indexed.

The cached page is not always representative of what’s indexed, and it’s generally only the static HTML that was fetched (if there’s JavaScript on it, it usually doesn’t run within the cached hosting). I’d focus more on the URL inspection tool.

Submitting an XML sitemap in the Search Console is one way to check a batch of your URLs and then check the sitemap in the Coverage Report in search console.

As mentioned, there’s a 3-step process in which Google crawls, renders, and indexes a page. It’s very important to distinguish between each of these steps. As the web becomes more sophisticated, Google has had to adapt, separating and improving these processes individually.

Multiple Googlebots are used by Google to crawl and render websites. You have different types of resources: images, videos, news, text… Google uses different Googlebots to understand each type of content.

Google announced about a month ago that they upgraded their rendering engine to run on evergreen Googlebot and the latest Chromium engine.

This is important, as crawling and rendering are necessary steps that lead up to indexing.

For indexing purposes, Google used to crawl with the desktop Googlebot. That has been changed; they now use the smartphone Googlebot for indexing purposes.

Mobile-First indexing will be imposed starting in July 2019 for all new sites, and is coming up for all known existing sites if they haven’t already been switched.

As the first step in the process leading up to indexing, to make sure your pages get indexed correctly and quickly, you need to make sure that your crawling is “safe and sound”.

Google prioritizes which sites its crawls, and how often. This is often referred to as “crawl budget”.

There was an article in the Google Webmaster blog about crawl budget that gave a few ideas as to how Google prioritizes which sites to crawl.

One of the points established by this article is that PageRank is a main driver behind indexing speed and volume for a website.

Backlinks, of course, are a major component of PageRank, and therefore have an influence on crawl rate and indexing.

Status codes are also taken into account. For example, if you have a lot of 404 pages on your site, that will likely lead Google to reduce the frequency of crawls.

If your site is organized in a way that wastes a lot of crawl budget, Google might reduce how much time it spends on your site.

Crawl budget it also impacted by page speed and server response time. Google doesn’t want to DDoS your site; if it sees that your server has a hard time providing pages and resources at the rate it requests them, it will adjust to what your server can handle in terms of crawling.

The Caffeine update that came out a few years ago was basically an update to Google’s rendering structure.

There are different archives of indexes that Google uses to return different results. It’s reasonable to imagine that there are different clusters in the index for news results, and another for image results, etc.

Finally, indexed URLs are ranked–but this is a totally different algorithm.

Both getting pages indexed faster and getting more pages indexed are heavily influenced by PageRank and therefore by backlinks. But the strategies to improving each one are different.

If you want pages to get indexed faster, you want to optimize the first two steps (crawling and rendering). This will include components like:

If you want to get more pages indexed, that’s where the crawling aspect is more important. You will want to make it easier for Google find all of your pages. This is simple on a small website with a thousand URLs, but is much harder on a larger site with millions of URLs.

For example, G2 has a ton of pages of different page types. Kevin’s SEO team wants to make sure that Google is able to find all pages, no matter the crawl depth and no matter how many pages of that type exist; this is a major challenge that has to be approached from different angles.

Based on the type of page, Kevin often finds different crawl rates by Google. This often depends on the URL’s backlink profile and internal linking. This is where he finds the most use of log files.

He segments his site by page type in order to understand where the site lacks crawl efficiency or where crawl efficiency is too high.

Kevin has absolutely observed definite correlations between crawl rate, indexing speed, and rank for each type of pages. This has been true not only across the sites that he has worked with, but also in correspondence with other SEOs in the industry.

Without positing a causality between crawl, indexing, and ranking, similar elements that drive indexing also appear to be taken into account when it comes to ranking a page. For example, if you have a ton of backlinks to a certain page template for a given type of page (example: landing pages), what you will find in your log files is that if Google has a higher crawl rate on these pages across your site, Google also indexes these pages faster and usually ranks these pages higher than other pages.

It’s hard to make universal statements that are valid for all sites, but Kevin encourages everyone to check their log files to see if this is also true on their own site. Oncrawl has also found this to be the case across many different sites they have analyzed.

This is part of what he tried to outline with the TIPR model of internal linking that he came up with.

To measure crawl rate, you want to answer the question: how often does a given Googlebot come to visit a certain URL?
