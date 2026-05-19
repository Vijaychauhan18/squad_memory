---
source: https://www.onely.com/blog/how-to-fix-blocked-due-to-unauthorized-request-401/
title: Why my page got “Blocked due to unauthorized request (401)"?
scraped: 2026-03-23
published_on: 2022-12-02
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

# Why my page got “Blocked due to unauthorized request (401)"?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/how-to-fix-blocked-due-to-unauthorized-request-401/
Published: 2022-12-02
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Learn the possible causes of “Blocked due to unauthorized request (401)" error and how to fix it to index your important pages!

## Extracted Body
The “Blocked due to unauthorized request (401)” status describes unindexed pages in Google Search Console. It means that:

“Blocked due to unauthorized request (401)” is a problem worth addressing because pages with this status eat up your website’s crawl budget. In addition, this error may keep some of your valuable pages out of the Google Index.

One of the ways servers communicate with browsers and crawlers is by using status codes. Status codes are standardized three-digit numbers carrying information about the page requested by the browser or crawler.

The 401 status code is returned for pages that require login credentials to be viewed when those credentials were not provided by the requesting party.

If the content of your page is password-protected, Google cannot crawl it. And crawling is, in most cases, a necessary step for indexing.

Explore other 4xx client error statuses in Google Search Console by reading our articles on:

To find your pages affected by the “Blocked due to unauthorized request (401)” status, open your Google Search Console. View the Page Indexing report accessible from the left navigation bar in your Google Search Console.

After clicking on the status name, you will see a graph showing how the number of affected pages has changed over time and a list of URLs. The list can be exported and filtered to the most interesting areas.

Knowing the pages that return status code 401 to Googlebot, decide which should be indexed and which should not.

Let me show you how to make such a decision and troubleshoot the “Blocked due to unauthorized request (401)” pages in both situations. I’ll talk about what to do to get them indexed and what to do to prevent them from sabotaging your crawling.

Not all pages on your domain need to be indexed. Websites are unlikely to achieve 100% index coverage, and what goes into the index should be a strategic decision.

This rule applies in particular to your pages secured by a login wall. But in some cases, you may actually want them to be indexed on Google.

Sometimes a password-protected page should be displayed among the search results and generate clicks.

For example, you might run a paid news site that just published an interesting article. You want internet users to be able to find it and buy a subscription if they wish to access the full content. In this case, the page with the article should both require login credentials from users and be indexed by Google.

Pages with the content of no use to visitors who aren’t already users of your site should be treated differently. There is no reason for those URLs to be on Search and in the Google Index.

As long as you’re working on staging environment pages, you don’t want them to be public and rank in search results.

Does this mean that the “Blocked due to unauthorized request (401)” status is appropriate for staging pages or password-protected pages that should stay out of the Google Index?

Unfortunately not, because Googlebot’s attempts to crawl them waste your crawl budget. With limited resources, Google must be picky about how often, how many, and which URLs it crawls. A messy unoptimized crawl budget means that your valuable pages get less attention from search engine crawlers.

Be free from crawling worries thanks to Onely’s crawl budget optimization services!

Distinguishing between indexable and non-indexable pages will be easier if you filter the pages to those submitted in your sitemap.

The URLs you have included in your sitemap are strategically important to your site and should be included in Google’s index to generate organic traffic.

Once you decide where your 401 pages belong, you can use one of the troubleshooting methods below.

For the 401 pages you want to index, you need to change the server settings so that Googlebot can visit and crawl their URLs. This means that your server will have to treat Googlebot differently than users’ browsers.

Usually, showing different content to Google than to your user isn’t welcome and may trigger a manual penalty for cloaking. That’s why it’s important to signal to the crawler why you decided on such a solution. You can do so by applying structured data to your paywalled pages. Google’s guidelines can instruct you on what structured data to add to your subscription pages.

And what should you do with 401 pages that don’t belong in the Google index? You can block them from being crawled in your robots.txt file. This file contains directives that tell crawlers which parts of the site they can visit.

The Disallow directive used in relation to exclusive and non-indexable or staging pages will stop Googlebot from wasting the crawl budget on these pages.

It’s a good idea to investigate how Googlebot came across your 401 pages that you don’t want to be indexed. To do this, use the URL Inspection Tool, which you can run from the list of affected pages by clicking on the magnifying glass icon.

From the information available in the URL inspection tool, you will learn what links led the crawler to a given 401 page.

You may want to edit those referring pages and remove the links if they are unnecessary and generate chaos on your site. To discover all internal links that lead to your 401 pages, use an SEO crawler.

The solutions described above will help index the pages crucial to your business and improve how your website’s crawl budget is allocated. However, if the “Blocked due to unauthorized request (401)” status appeared due to errors on your server, these methods can’t guarantee that indexing issues won’t return.

Like any website, your domain can benefit from regular technical SEO reviews. Such audits allow you to eliminate threats to your visibility before any harm happens.

In case of the “Blocked due to unauthorized request (401)” issue, use Onely’s comprehensive server log analysis and check if your server is having trouble communicating with crawlers.

The “Blocked due to unauthorized request (401)” error occurs when Googlebot tries to crawl your pages, but your server requests login credentials the crawler can’t provide.

To ensure that the problem does not return in the future, contact Onely and let our technical SEO experts take care of your website.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
