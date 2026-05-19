---
source: https://www.onely.com/blog/how-to-fix-discovered-currently-not-indexed-in-google-search-console/
title: How To Fix “Discovered ‐ Currently Not Indexed” in GSC
scraped: 2026-03-23
published_on: 2026-03-13
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

# How To Fix “Discovered ‐ Currently Not Indexed” in GSC

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/how-to-fix-discovered-currently-not-indexed-in-google-search-console/
Published: 2026-03-13
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
You can fix “Discovered – currently not indexed” in a few steps. Check our guide and boost your rankings!

## Extracted Body
“Discovered – currently not indexed” in Google Search Console means Google knows the URL exists but has not crawled it yet. The page may have been found through internal links or your XML sitemap, but Google has not fetched it, so it cannot be indexed yet. In Search Console, these URLs usually have no last crawl date.

This guide explains when this status is normal, when it signals a real indexing problem, and what to fix first.

In 2025, content quality became the dominant indexing factor. According to mariehaynes.com’s study – Google’s May 2025 quality review actively removed a significant volume of pages from its index, making it more urgent than ever to diagnose and fix this status.

Every day a page stays unindexed is a day it is invisible, not only to traditional organic search but also to Google’s AI Overviews.

Safaridigital.com.au states that AI Overviews now appear on approximately 21% of all Google searches broadly, and according to almcorp.com up to 48% of tracked queries as of early 2026, with informational queries triggering them at the highest rates (approximately 57.9%).

Unindexed pages cannot appear in AI Overviews, because Google’s AI system draws exclusively from indexed content.

“Discovered – currently not indexed” in Google Search Console means Google knows the URL exists, but has not crawled it yet.

Typically, Google wanted to crawl the URL but this was expected to overload the site; therefore Google rescheduled the crawl. This is why the last crawl date is empty on the report.

That is also why the last crawl date is usually empty for URLs in this state.

Important: This status is not necessarily an error. It means the URL is in Google’s discovery and crawl queue, but Google has not fetched it yet. For a small number of low-priority or non-essential URLs, that can be normal. Google may still return to crawl and index the page later without any action on your part.

In practical terms, this status tells you more about crawl timing and crawl priority than about page-level quality.

Because Google has not crawled the page yet, it has not fully processed the page content itself.

If the status persists on important URLs, the usual next checks are internal linking, sitemap quality, duplicate or low-value URL patterns, and server or crawl-efficiency constraints.

That diagnostic framing is consistent with Google’s explanation that crawl rescheduling is often tied to load management and with its broader guidance that not all discovered URLs are crawled immediately.

You can find this status in Google Search Console → Indexing → Pages → Why pages aren’t indexed . There, “Discovered – currently not indexed” appears as one of the “Not indexed” reasons in the Page Indexing report.

It may, but Google rescheduling the crawl is only one of several possible reasons for this problem.

“Discovered – currently not indexed” and “Crawled – currently not indexed” are different Google Search Console statuses, and they point to different stages in Google’s indexing pipeline:

Because the page reached a different stage in each case, the diagnosis and fix priorities are different.

A page can move from “Discovered – currently not indexed” to “ Crawled – currently not indexed ” before it is fully indexed. That usually means Google has now fetched the page, so the problem has shifted from crawl timing to indexing evaluation. If that happens, stop treating it as a discovery problem and switch to a “Crawled – currently not indexed” diagnosis.

Now that the difference is clear, the next step is to assess the severity of the issue on your site: how many URLs are affected, whether they are important pages, and whether the pattern points to a crawl-priority issue or a broader site-level indexing problem.

Before you start fixing anything, first determine whether “Discovered – currently not indexed” is a minor queue state or a real indexing problem.

A small number of affected URLs on low-priority pages can be normal. But if important pages are affected, if the count is rising, or if the affected URLs follow a pattern, you likely need a deeper diagnosis. Google’s own guidance makes clear that not every discovered URL is crawled immediately, and crawl-budget work is mainly relevant for very large or frequently updated sites.

A quick severity check helps you decide whether to monitor or investigate.

Before diagnosing the issue, confirm that the page is actually still in the “Discovered – currently not indexed” state. Search Console reports are not always fully up to date, and a URL may already have been crawled or indexed since the report was generated.

If the page is already indexed or has recently been crawled, the issue may already be resolving and no further action is needed.

This quick verification step prevents you from spending time diagnosing a problem that may already be fixed.

In Google Search Console’s Page Indexing report, compare the number of URLs in “Discovered – currently not indexed” with the total number of important URLs on your site or in the affected section.

A small count on low-value pages may simply reflect normal crawl scheduling. A larger cluster, a rising trend, or any concentration on pages you actually need indexed is a stronger signal that something is wrong.

Review a representative set of URLs manually. Look for patterns such as:

Pattern detection matters because Google’s crawling guidance repeatedly emphasizes crawl efficiency, duplicate URL management, and discoverability. Faceted and parameter-heavy URLs can slow discovery of useful pages by consuming crawl resources.

Use the pattern, not guesswork, to decide where to investigate next:

Google recommends checking whether Googlebot is encountering availability issues, whether important pages are not being crawled, and whether crawl efficiency can be improved.

If the affected URLs are revenue-generating pages, high-value landing pages, product/category pages, or core editorial assets, treat the issue as urgent. If the affected URLs are low-value utility pages, filtered listings, duplicates, or pages that do not need to rank, monitoring or deindexing/consolidation may be the better response.

If this severity check suggests a real problem, start with crawl priority and discovery signals first: internal linking, sitemap quality, duplicate URL patterns, faceted navigation, and server behavior.

The right fix depends on why Google has not crawled the page yet.

Work through the checks in order, starting with discovery and crawl-priority signals before moving to deeper technical causes below.

One of the foundational factors to address when diagnosing “Discovered – currently not indexed” is how Google allocates its crawling resources to your site.

It is crucial to define what “crawl budget” actually means. According to Google, you generally don’t need to worry about crawl budget unless your site has over 1 million unique pages , or you have a moderately sized site (10,000+ pages) with content that changes rapidly every day. If your site is smaller than this, your “Discovered” issue is almost certainly due to crawl demand (overall site quality and popularity), not a technical crawl capacity limit.

A crawl budget is the total number of pages Googlebot can and wants to crawl on your website. It is determined by two factors:

“Discovered ‐ currently not indexed” is a classic symptom of a crawl budget or demand bottleneck. If Google’s demand is low, or its capacity is throttled, URLs simply sit in the queue.

Let’s look at how to resolve the technical factors draining your crawl resources first.

Allowing Googlebot to roam your website without restrictions has two major negative consequences for your indexing pipeline.

First, it wastes your crawl capacity . Googlebot may get trapped crawling infinite URL variations before it ever reaches your essential, revenue-generating pages. Second, it destroys your crawl demand . If Google repeatedly encounters low-quality or duplicate URLs, it will view your entire domain as lower quality, creating a vicious cycle where it simply stops trying to discover new content.

The pages draining your crawl resources typically fall into two categories:

How to control the crawl: Before applying technical band-aids, assess whether these pages actually need to exist. If they are obsolete or unnecessary, consolidate them or remove them entirely by returning a 404 (Not Found) or 410 (Gone) HTTP status code.

If the pages must remain for user experience (like filtering options), you must manage how Google interacts with them. It is critical to understand the technical difference between crawling and indexing here:

To preserve crawl budget and get your “Discovered” pages processed, use robots.txt to ruthlessly block infinite URL spaces and parameter traps, forcing Googlebot to focus its energy on your core canonical pages.

Need to decide on your indexing strategy? Check out our article on how to create an indexing strategy for your website.
