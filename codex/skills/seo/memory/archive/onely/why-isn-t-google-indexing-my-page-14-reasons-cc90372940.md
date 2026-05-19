---
source: https://www.onely.com/blog/why-isnt-google-indexing-my-page-14-reasons/
title: Why isn’t Google indexing my page? 14 reasons
scraped: 2026-03-23
published_on: 2023-05-22
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

# Why isn’t Google indexing my page? 14 reasons

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/why-isnt-google-indexing-my-page-14-reasons/
Published: 2023-05-22
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Let's take a look at the most common reasons why pages are not indexed by Google. Maybe one of them applies to your situation.

## Extracted Body
Technical issues, such as crawling and indexing problems, restrictions set in the robots.txt file, and incorrect use of the ‘noindex’ directive, can prevent pages from being indexed on Google Search Console. Additionally, inaccessible or blocked pages, broken internal links, and poor content quality can also hinder indexing. Ensuring that your website is technically sound, with a correct robots.txt file, accessible pages, and high-quality content, can help resolve ‘not indexed’ issues and improve your website’s visibility on Google.

There are various reasons why your website may not show up in Google search results. Before you take any action, it’s crucial to understand the cause of your indexing troubles. You can do so by using the following three methods.

This will show you a list of pages that Google has indexed. Be careful though! Using search operators does not give you the full picture and this method might not show all pages.

Let’s take a look at the most common reasons why pages are not indexed by Google. Maybe one of them applies to your situation.

This means that Google was unable to find the page on the website. When Google is not able to discover a page, it cannot be indexed and will not appear in the search results. There are three main reasons why Google might struggle to find your page.

Internal links play a crucial role in a website’s indexation by search engines like Google. When search engines’ bots crawl a website, they follow links to discover and index new pages. Internal links, which are links that connect pages within the same website, help robots like Googlebot navigate a website and understand its structure.

If a website lacks internal links, search engines’ bots may have difficulty discovering all of its pages, and this can result in some pages not being indexed.

Want to know more? Check out our Ultimate Guide to Internal Linking in SEO !

A sitemap is a file that lists a website’s most important indexable pages (or all of them in some cases). Search engine robots can use this file to discover and index the website’s content.

When a page is not included in the sitemap, it does not mean that it won’t be indexed by search engines. However, not including a page in the sitemap can make it harder for search engine robots to discover and crawl it. If a page is not included in the sitemap, it may be perceived as less important or lower in the hierarchy. In some cases, this situation can result in some pages not being discovered, even with internal linking in place.

On the other hand, including a page in the sitemap can help search engines in two ways. It’s easier to discover the page, and its presence in the sitemap serves as a clue that this particular page is important and should be indexed.

Find out more by reading our article: Ultimate Guide to XML Sitemaps for SEO!

When Googlebot crawls a website to index its content, it has a limited amount of time to do so. When a website is both large and to make matters worse, slow to load, crawling it can present a challenge for search engine bots. As a result, robots like Googlebot may be unable to index all pages within the given time limit. This can cause issues for your website because any pages that are not indexed do not appear in the search results and do not work for your website’s visibility.

When bots crawl a website, they discover new pages and content that can be added to Google’s index. This process is essential to ensure that pages are visible in the search results. However, if a page isn’t crawled, it won’t be added to the search engine’s index. There are several reasons why a page might not be crawled by a search engine; these include a low crawl budget, errors, or the fact that the page is disallowed in robots.txt .

The robots.txt file is a text file used to instruct search engine robots which pages or directories on their site to crawl or not to crawl. Website admin. can optimize the robots.txt to show search engines which content should be accessible to crawl .

As a general rule, if a page is disallowed in the robots.txt file, search engine bots should not be able to crawl and index that page. However, there are exceptions to this. For example, if a page is linked from an external resource, it can get indexed even though it’s blocked in robots.txt . Another common mistake is treating robots.txt as a tool to block indexing. If you disallow the page in robots.txt , it will prohibit Googlebot from crawling it, but if a page was indexed before – it will remain indexed.

However – most of the time, the page will not be accessible for crawling and indexing if you block it in robots.txt . And if you discover that your page wasn’t crawled at all, it might be because you accidentally blocked it with a robots.txt file.

If you are not sure what to do in this situation, feel free to reach out to an SEO specialist who will be able to help.

The crawl budget refers to the number of pages or URLs that Google’s bots will crawl and index within a given timeframe. When the crawl budget allocated to a website is too low, it means that the search engine’s crawler won’t be able to crawl and index all the pages right away. This means that some of the website’s pages may not show up in the search results.

This is a simplified definition, but if you’d like to learn more – check out our guide:

Remember that you can have an impact on your crawl budget. It is typically determined by the search engine based on several factors. There are many problems that may negatively affect your crawl budget, the most common being:

If you believe your website has issues with the crawl budget, you should try to find the cause of this situation. An experienced SEO Specialist will definitely help you with that.

When Googlebot tries to crawl a web page, it sends a request to the server hosting the website to retrieve the page’s content. If the server encounters an issue, it will respond with a server error code, indicating that it could not provide the requested content. Googlebot interprets this as a temporary unavailability or as an issue with the website; this might slow down crawling .

As a result, some of your pages may not be indexed by the search engine. Furthermore, if this happens repeatedly and the website keeps returning consistent server errors, it might lead to pages getting dropped from the index.

If your website has significant server problems, you can review these issues in one of GSC’s reports.

More information and recommendations on how to fix that problem:

If you want to check how particular status codes (including server errors) affect Googlebot’s behavior, you can learn about it in Google’s official documentation: How HTTP status codes, and network and DNS errors affect Google Search .

If Google doesn’t index a page or deindexes a previously indexed one, the page won’t appear in the search results. It can be caused by technical problems, low-quality content, guideline violations, or even manual actions.

If a page on a website has a noindex meta tag, it instructs Google not to index the page. This means that the page will not appear in the search results .

In some instances, meta tags may inadvertently be set to “ noindex, nofollow” due to a development error. Consequently, the page may get removed from the index. If this is later combined with a robots.txt blockade, a page might not get crawled and indexed again. In some cases, it might be intended and could be a solution to some kind of index bloat issue. However, we recommend being extremely careful with any actions that may disturb crawling and indexing.

Read our articles and learn how to get rid of unnecessary noindex:

A canonical tag on a website’s page instructs search engines to treat the canonical URL as the preferred URL for that page’s content. This tag is used when the page’s content is a duplicate or variation of another page on the site. If the canonical tag is not implemented correctly, it can cause indexation issues.

For the purpose of this article, please remember that all original pages should have a self-referencing canonical tag. A page might end up not getting indexed if it has a canonical to another URL.

When a page on a website is a duplicate or near duplicate of another page, it can cause indexation and ranking issues. If a page is a duplicate of another one, Googlebot may not index it. And even if such a page is indexed , search engines usually will not allow duplicate content to rank well.

Duplicate content can also affect a website’s crawl budget. Googlebot needs to crawl each URL to identify if they have the same content, which can consume more time and resources. As a result, Googlebot has less capacity for crawling other, more valuable pages.

While there is no specific “duplicate content penalty” from Google, there are penalties related to having the same content as another site. Actions such as scraping content from other sites or republishing content without adding additional value are not welcome in the world of SEO, and may even hurt your rankings.

Do you struggle with duplicate content? Check out our guide to fix it:

Google aims to provide the best possible user experience by ranking pages with high-quality content higher in search results. If the content on the page has poor quality, Google may not consider it valuable to users and may not index it . Additionally, poor-quality content can lead to a high bounce rate, which is when users quickly leave the page without interacting with it. This can signal to Google that the page is irrelevant or not valuable to users, resulting in not indexing it.

The HTTP status code is part of a response that a server sends to a client, after receiving a request to access a webpage. The HTTP status code 200 OK indicates that the server has successfully responded to the request, and the page is accessible.

If a page returns an HTTP status code other than 200 OK , it won’t get indexed. As for why, it depends on the particular status code. For example, a 404 error status code indicates that the requested page is not found, and a 500 error status code indicates that there was an internal server error. If Googlebot encounters these errors while crawling a page, it may assume that said page is not available or not functional, and it will not index it. And if a non-200 HTTP status code persists for a long time, a page may be removed from the index.

When a page is in the indexing queue, it means that Google has not yet indexed it. This process can take some time, especially for new or low-traffic websites, and it can be delayed further if the website has technical issues, a low crawl budget, or robots.txt blockades and other restrictions.

Additionally, if the website has a lot of pages, Google may not be able to index all of them at once. As a result, some pages may remain in the indexing queue longer. This is a common problem which may get resolved with time, but if it doesn’t – it might be necessary to analyze it further and take action.

When Googlebot crawls a page, it not only retrieves the HTML content but also renders the page like a browser does. If Googlebot encounters issues while rendering the page, it may not be able to properly understand the content of the page. If Google can’t render the page, it may not be able to identify certain elements, such as JavaScript-generated content or structured data, that are important for indexing and ranking.

As Google admits in their article Understand the JavaScript SEO basics :

“If the content isn’t visible in the rendered HTML, Google won’t be able to index it.”

In some cases, this can affect the indexing of the URL. If a significant part of your page isn’t rendered, it won’t be visible to Google. A page like this will likely be considered a duplicate or low quality, and may end up not getting indexed.

Sometimes, when clients ask us “why isn’t Google indexing my page” the answer is that a page takes too long to load. That might be also your case!

If Googlebot is crawling a website that loads slowly, it may not be able to crawl and index all of the pages on the site within the allocated crawl budget.
