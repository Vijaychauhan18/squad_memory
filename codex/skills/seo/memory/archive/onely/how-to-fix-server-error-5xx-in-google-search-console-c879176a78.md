---
source: https://www.onely.com/blog/server-error-5xx-google-search-console/
title: How To Fix “Server Error (5xx)” in Google Search Console
scraped: 2026-03-23
published_on: 2023-02-06
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

# How To Fix “Server Error (5xx)” in Google Search Console

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/server-error-5xx-google-search-console/
Published: 2023-02-06
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
"Server error (5xx)" prevents pages from appearing on search & may indicate server problems making website difficult to access. Let's fix it!

## Extracted Body
Google Search Console displays the “Server error (5xx)” status for URLs that Googlebot couldn’t access because your server indicated a malfunction. Without access to your content, Google cannot initiate the indexing process.

Being indexed by Google is an essential condition for your pages to appear in the search results and attract traffic to your business. By indexing a page, Google decides to retain its URL and information about its content in a vast database known as the Google Index. The indexing process is preceded by two steps:

As you can see, Google will not index a URL without understanding its content, which is why the crawling stage is so important. A Group 5xx server error significantly disrupts this process by preventing Googlebot from crawling the page.

As a result, Googlebot excludes the URL from indexing and may avoid your server to prevent causing additional load.

A 5xx server error is a type of HTTP status code that indicates a server’s inability to fulfill a client’s request to access a page.

These errors, also known as server-side errors, belong to the fifth class of HTTP status codes, which range from 1xx to 5xx. The first digit in the status code specifies the type of response the server is returning, with 5xx specifically indicating a server-side error.

These errors can stem from various factors, including outdated or corrupted caches and cookies or improper setup. For example, if a web server’s software or hardware is malfunctioning, it may return a 5xx error to clients attempting to access the website. Similarly, if an API server faces high traffic or technical difficulties, it may also return a 5xx error to software programs trying to access its services.

5xx errors indicate that the problem lies with the server rather than the client making the request. They are often temporary and can be resolved by the server administrator or the service provider.

Google Search Console doesn’t differentiate between the various errors in the 5xx group because, for Google, they all indicate the same issue. Additionally, the accuracy of specific 5xx status codes returned by your server depends solely on its configuration. This makes it difficult to get reliable information from the 5xx error codes reported by different servers.

However, it’s useful to know the most common responses from this group and understand their causes.

A messy server configuration is detrimental to organic traffic. Frequent 5xx server errors can significantly harm your SEO performance in several ways:

If your pages are often unavailable, it leads to a poor user experience. Users typically lack the patience to search through a site for a page that works.

Moreover, Google may avoid showing pages that are likely to deliver a bad experience.

Google has limited resources and does not crawl every piece of content it discovers. For each website, it allocates a “crawl budget,” which determines how often Googlebot visits a domain and how many URLs it crawls during these visits.

Pages that return 5xx status codes signal Google to reduce its crawling frequency to avoid overloading your server. Consequently, Googlebot’s interest in your site decreases, affecting both your existing and new content.

If Google crawls your site less often, your new content may be discovered too late when it’s no longer relevant. Additionally, any updates to your old content might go unnoticed, leading to the following:

Would you like to speed up the discovery of your content? Contact us for crawl budget optimization.

As mentioned earlier, Google won’t index a page that it can’t crawl. This is why you see the “Server error (5xx)” status in your Google Search Console (GSC), resulting in your pages not appearing in search results.

5xx server errors are problematic but fixable. Before discussing the best ways to address them, let’s look at where you can identify affected URLs.

The primary place to check is the Google Search Console’s Page Indexing report, which likely first alerted you to the problem. The “Server error (5xx)” status is one of several issues listed in this report.

By clicking on it and expanding it, you can view the list of affected URLs and a chart showing how their number was changing in time.

You can get additional information about each of them by running the URL Inspection Tool, as shown in the screenshot.

The list of URLs can be exported, which will certainly help you organize your work.

It’s a good idea to filter the pages so that you only see those that simultaneously return code 5xx status and are included in your sitemap (which means you care about them being indexed).

This way, you will quickly identify the URLs for which the problem is the most pressing.

Another helpful resource for quickly finding pages that return a 5xx response is Google Search Console’s Crawl Stats. To access this, scroll to the bottom of the left navigation bar and select “Settings.”

Scroll down to see the breakdown of crawl requests, then focus your attention on the report concerning server responses.

Just like in the Page Indexing report, you can select the status code you are interested in, expand it, and view the list of URLs that return Googlebot with such a response.

Your server’s log files record information about all requests made by users’ browsers or search engine crawlers. By examining these logs, you can discover:

A server log file contains the most valuable information about your server’s issues. If you want to quickly identify the causes of these problems, consider using Onely’s comprehensive server log analysis.

In the section above, I told you how to get a list of “Server error (5xx)” URLs. Now, let’s focus on troubleshooting them.

The first step you should take is effortless. Open the pages in your browser and see if the problem persists. To ensure you have an up-to-date overview of the situation, clear the cookies and cache files from your browser.

If the pages are available, Googlebot is most likely facing a temporary 503 error. This means that your server is easily overloaded and cannot cope with a large number of requests.

This situation puts your indexing and user experience at risk, so you may need to upgrade your server.

Switching to a more efficient server may be a short-term solution if your site is cluttered with uncompressed files. Contact Onely for web performance optimization to boost your SEO long-term.

If pages remain unavailable during your check, you may deal with deeper problems. You can try fixing it with the following methods:

Sometimes, users and crawlers requesting your pages see 5xx response due to outdated plugins in your Content Management System, e.g., WordPress.

If you can, try disabling your plugins individually and check if it solves the problem. Crawl your pages with a Googlebot user agent to see your website from its perspective and ensure the problem disappears.

It’s possible that your last server update caused some configuration issues and conflicts. Try going back to the previous software version to see if the issue is resolved.

The .htaccess file provides configuration changes to your server. Typically, your Content Management System creates it automatically.

If you suspect errors in this file, you can deactivate the old .htaccess file and create a new one with a few clicks.

The “Server error (5xx)” status in Google Search Console indicates unindexed URLs because they’re unavailable to Google’s crawler. This unavailability usually stems from issues like server overload or poor configuration.

To troubleshoot “Server error (5xx)” pages, consider upgrading your server, checking for bugs in your Content Management System, and contacting your hosting provider. Consider getting a technical SEO audit from Onely to prevent future indexing issues.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
