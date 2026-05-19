---
source: https://www.onely.com/blog/5-mistakes-to-avoid-in-your-sitemaps/
title: 5 Mistakes To Avoid in Your Sitemaps
scraped: 2026-03-23
published_on: 2022-03-15
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# 5 Mistakes To Avoid in Your Sitemaps

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/5-mistakes-to-avoid-in-your-sitemaps/
Published: 2022-03-15
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Create a great sitemap that helps search engine bots find your indexable URLs - here are 5 key mistakes that you should avoid.

## Extracted Body
We’ve built a tool that lets us check how many pages on a given site are indexed in Google .

So far, we checked hundreds of websites and the tool helped us diagnose SEO issues that our clients were dealing with, such as ones connected to the crawl budget and indexing.

We often encounter data anomalies when investigating these problems and see many websites with severe mistakes in their sitemaps.

If your sitemap is not implemented properly, Googlebot can spend a lot of time crawling low-quality URLs, which is a waste of crawl budget. As a result, many valuable URLs on your website may not be indexed in Google , because it won’t have sufficient resources to crawl them.

What mistakes are popular websites making in their sitemaps, and how do you avoid them to ensure Google is not wasting the crawl budget on irrelevant content?

First, let me explain what crawl budget is and how exactly it’s relevant for website indexing.

Google is able to crawl a lot of content, but its resources are not infinite – so it needs to make choices with the resources it has.

That’s why Googlebot defines a crawl budget for all websites – the number of URLs it can and wants to crawl.

If the site slows down or responds with server errors, the limit goes down and Googlebot crawls less. source: Google's documentation

Because of Googlebot’s limited capabilities, you should plan which URLs Googlebot crawls on your website.

The key to adjusting which URLs are crawled is explained in Google’s documentation:

Manage your URL inventory: Use the appropriate tools to tell Google which pages to crawl and which not to crawl. If Google spends too much time crawling URLs that aren’t appropriate for the index, Googlebot might decide that it’s not worth the time to look at the rest of your site. source: Google's documentation

With tons of low-quality URLs for Google to crawl, Googlebot may lose lots of time on crawling them and may not be able to crawl many high-quality URLs on your website.

This holds the most weight for large or rapidly changing websites because they need to be crawled often and extensively in order to attract traffic.

As I’ve explained, optimizing your crawl budget is an extremely important step for your site’s indexing.

One of the ways to manage your URL inventory is by creating and maintaining a well-optimized sitemap.

A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them […]. A sitemap tells Google which pages and files you think are important in your site, and also provides valuable information about these files. For example, when the page was last updated and any alternate language versions of the page. source: Google’s documentation

However, tons of websites fail to create well-optimized sitemaps. Luckily, we can learn from their mistakes.

I analyzed many popular sites and found that a lot of them make mistakes in their sitemaps that negatively affect their crawl budget, which could lead to issues with their Index Coverage.

Here is my breakdown of mistakes to avoid when creating a sitemap.

One of the mistakes I discovered concerned the structure of URLs in sitemaps.

When I saw statistics collected by our software, I was stunned: it showed that 0% of whisky.de’s pages submitted in sitemaps were indexed in Google.

I knew this couldn’t be true, so I investigated the data further.

But then I noticed that all the URLs had double slashes following the top-level domain – take a look at this sample:

The double slash seems like an obvious programmatic mistake while generating sitemaps and one that’s easy to fix.

However, the pages included in sitemaps have canonical tags pointing to respective URLs – their correct versions with a single slash.

As a result, it’s highly probable that Google is visiting twice as many URLs as intended: the URLs with the single slashes and double slashes.

Google has mechanisms to spot faulty patterns in URLs, and technically speaking, it’s possible that Google spotted the mistake. So, it could be crawling whisky.de accordingly and indexing the correctly structured URLs. But there’s no way for us to check that without access to the website’s Google Search Console account or server logs.

In practice, you shouldn’t rely on Google’s algorithms to fix your mistakes – practices like the one I described can put a strain on your crawl budget and even keep your pages out of Google’s index.

Want to optimize your crawl budget? Reach out to us for crawl budget optimization services.

There is a plague of websites that include thin content pages in their sitemaps.

I discovered this mistake on AnnTaylor.com, a top-rated store with women’s clothing.

I wanted to check how many of their product categories were indexed in Google, so I investigated their sitemap dedicated to category pages.

The initial check showed that only 46% of the category pages were indexed in Google.

So, I looked into this in more detail and learned that most of their category pages were soft 404s.

The next logical step was to exclude soft 404s from my sample. For that purpose, I checked the indexing status of the same sitemap, but used a trigger that excluded pages containing the phrase “We stylishly searched and no luck” as exemplified in the image above.

It turned out that after excluding soft 404 URLs, as much as 82% of the pages in their category sitemap are indexed.

Still, 18% of category pages aren’t indexed in Google – that is what their SEOs should focus on investigating.

As I mentioned already, sitemaps help Google understand your website better and crawl it more intelligently.

However, I noticed many websites don’t include their most valuable URLs in sitemaps.

I checked a general sample (taken from all URLs from sitemaps ) for GoodReads and found out that just 35% of them were indexed.

I was very surprised, as I know that it’s a very high-quality website. I know I’m not the only one who visits GoodReads to read reviews and learn if a particular book is worth reading.

Then, I saw the sample we checked had no URLs with books included. So I decided to download all their sitemaps.

There is a risk that Google prioritizes URLs found in sitemaps and somehow, skips visiting product pages.

Disclaimer: GoodReads is not our client. So, technically speaking, it is possible that they have a private sitemap submitted to Google Search Console.

One of the parameters you can include in your sitemap file is <lastmod>, specifying the last time a page has been updated. This way, Google can easily pick URLs that changed recently.

However, some websites overuse this technique. And doing it could have adverse effects because, as we read in Google’s guidelines, “ Google uses the <lastmod> value if it’s consistently and verifiably (for example by comparing to the last modification of the page) accurate.”

Let’s look at an example of a site that overuses the <lastmod> parameter.
