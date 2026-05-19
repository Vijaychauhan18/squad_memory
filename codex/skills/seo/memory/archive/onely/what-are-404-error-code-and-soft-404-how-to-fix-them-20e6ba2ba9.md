---
source: https://www.onely.com/blog/not-found-404-vs-soft-404/
title: What Are 404 Error Code and Soft 404? How To Fix Them?
scraped: 2026-03-23
published_on: 2022-12-14
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

# What Are 404 Error Code and Soft 404? How To Fix Them?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/not-found-404-vs-soft-404/
Published: 2022-12-14
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Find out the differences between 404 error code and soft 404, how they impact your SEO and how to get rid of them!

## Extracted Body
“Not found (404)” and “Soft 404” are Google Search Console statuses that may describe some of your unindexed pages. They are named very similarly, and both can profoundly hurt your SEO but have entirely different causes:

The way you approach “Not found (404) and “Soft 404” pages may be essential for your user experience, crawl budget optimization, and indexing strategy.

Let’s explore their differences further and learn how to address them.

In simple words “Not found (404)” error happens when you or a web crawlers tries to visit a page on a website, but that page isn’t there anymore. So, the website tells you it can’t find the page you are looking for with a 404 error message. From the website owner’s point of view, it also means that Google won’t index pages with 404 errors because it does not deliver any valuable content.

If you see “Not found (404)” in the Page indexing (Index Coverage) report in Google Search Console, it means that:

Servers communicate with crawlers and browsers through status codes. Whenever you’re able to view a page without any problems, the server most likely responds to your browser’s request with the 200 status code.

There are also many status codes referring to possible errors, because of which the server cannot grant you access to a page. The 404 status code is one of them. It means that the page is not available because the server couldn’t find it.

Google doesn’t index 404 pages because they present no value to users.

However, the possible reasons why the server responds with the 404 status code may differ:

Managing a website, it may happen that you accidentally remove a page. If it’s a crucial page with many links pointing to it, it may contribute to a significant traffic loss for your website.

There’s nothing wrong with removing the page that doesn’t bring business value to your website or may harm its SEO.

And as long as you can’t address your issues in any other way (e.g., modify or redirect your content), feel free to set up the 404 status code.

Your website is constantly changing, so it’s normal for some URL addresses to change with time.

But remember that if the link pointing to a page is incorrect, the server won’t provide users with the requested content because it can’t find it.

Another case is when you make a typo in a URL when manually adding links or typing to enter a given page.

The change may seem insignificant from your perspective. However, for search engine bots, even a minor difference in the URL address is interpreted as a different URL.

Even though having some “Not found (404)” pages is inevitable, leaving them unoptimized may contribute to further issues on your website.

Most likely, no matter how users entered your “Not found (404)” URL, they weren’t looking for a blank page.

Seeing no content on a target page may create a negative user experience. And how users feel about your website directly influences your conversion rates.

Therefore, you need to ensure your visitors don’t feel lost when encountering 404 pages on your website.

A good practice is to create a custom 404 page that is not only visually attractive but, most of all, informs users:

By creating a sound 404 page, you can encourage users to stay on your website even though they can’t explore the exact page they want to.

Learn how to create a custom 404 page for your website by reading my colleague’s article.

Google doesn’t have infinite resources to crawl everything on the Web.

If bots can freely crawl your “Not found (404)” pages, they may never get to the more valuable pages on your site before your crawl budget is wasted.

If you think that might be your case, go for crawl budget optimization services to unlock your website’s full crawling potential.

If you have many internal and external links pointing to your 404 pages, the accumulated PageRank goes to waste.

First, browse the list of affected pages in the Page indexing (Index Coverage) report to check if they are the consequence of your deliberate decision.

Also, if you manage a large website, navigating your 404 pages is easier with an SEO crawler like Screaming Frog or WebSite Auditor.

Another thing you need to check is to ensure your XML sitemap doesn’t include any “Not found (404)” pages.” You can filter your affected URLs in the upper left corner to ‘All submitted pages’ on the status page.

Ideally, as your sitemap file should only include pages responding with the 200 status code, you shouldn’t find any URLs on the list of ‘All submitted pages’ (or, as it was in the past – within the “Submitted URL Not found (404)” status.)

Ensure you update your sitemaps every time you make changes on your side.

And remember that even though you implemented your changes, they won’t be immediately picked up. Check your ‘All submitted pages’ report again when Google recrawls your sitemap.

If you confirm that your “Not found (404) pages shouldn’t exist and they don’t contribute to other issues, you can ignore the “Not found (404) status.

However, if that’s not the case for you or you aren’t sure how the “Not found (404) URLs may affect your website, read on for further steps.

In the perfect scenario, after the proper redirect (and after Google recrawled the URL) , the “Not found (404)” page will change its status to “ Page with redirect “ in Google Search Console.

However, remember that you shouldn’t rush to redirect your “Not found (404)” pages to contextually unrelated pages just for the sake of redirecting. Otherwise, it may contribute to other issues on your website, like the “Soft 404” error we’re going to discuss below.

Are you about to redirect your 404 page? Dive into our ultimate guide to redirects to explore the topic further and avoid possible redirect errors .

When you think a given page shouldn’t exist so it’s correctly returning the 404 HTTP status code, ensure it isn’t extensively linked throughout your website and from external resources.

You can replace your internal linking to 404 pages with links to the related pages that respond with the 200 status code.

When it comes to external linking, you may contact the websites linking to you and ask them to update the no longer existing link. However, I understand that’s not always possible, especially if there are thousands of backlinks pointing to your page.

In this case, make a 301 redirect to an existing page (or consider creating new related content you can redirect to), or set up the 410 HTTP status code.

Soft 404 doesn’t occur when the server responds with the 404 error. Google labels pages as soft 404s when they meet two conditions:

In other words, Google thinks that a given URL should return the 404 status code despite providing a 200 response. On this basis, it concludes that the page should not be indexed.

You can find your pages affected by the “Soft 404” status in the Page Indexing report. It’s easy to access from the left navigation bar in your Google Search Console.

You can gain more information about those pages by clicking on the status name. It’ll show a graph presenting how the number of affected pages has changed over time and a list of URLs. You can export the list using the button located in the upper right corner.

According to what John Mueller said on SEO Office Hours in July 2021, Google Search Console reports only those soft 404 pages that are considered as such on mobile. If some desktop pages are labeled as soft 404, but their mobile versions aren’t affected by the problem, you may not be able to see them in GSC.

To detect desktop soft 404s invisible in the GSC report, your website needs a technical SEO audit.
