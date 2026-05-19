---
source: https://moz.com/blog/how-to-find-all-existing-and-archived-urls-on-a-website
title: How to Find All Existing and Archived URLs on a Website
scraped: 2026-03-23
published_on: 2025-01-06
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How to Find All Existing and Archived URLs on a Website

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/how-to-find-all-existing-and-archived-urls-on-a-website
Published: 2025-01-06
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Need to find all current and historic URLs on a website? Discover essential tools and tips to build a complete list of URLs for migrations, audits, and recovery.

## Extracted Body
There are many reasons you might need to find all the URLs on a website, but your exact goal will determine what you’re searching for. For instance, you may want to:

In each scenario, a single tool won’t give you everything you need. Unfortunately, Google Search Console isn’t exhaustive, and a “site:example.com” search is limited and difficult to extract data from.

In this post, I’ll walk you through some tools to build your URL list and before deduplicating the data using a spreadsheet or Jupyter Notebook, depending on your website’s size.

If you’re looking for URLs that disappeared from the live site recently, there’s a chance someone on your team may have saved a sitemap file or a crawl export before the changes were made. If you haven’t already, check for these files; they can often provide what you need. But, if you’re reading this, you probably did not get so lucky.

Archive.org is an invaluable tool for SEO tasks , funded by donations. If you search for a domain and select the “URLs” option, you can access up to 10,000 listed URLs.

To bypass the lack of an export button, use a browser scraping plugin like Dataminer.io. However, these limitations mean Archive.org may not provide a complete solution for larger sites. Also, Archive.org doesn’t indicate whether Google indexed a URL—but if Archive.org found it, there’s a good chance Google did, too.

While you might typically use a link index to find external sites linking to you, these tools also discover URLs on your site in the process.

How to use it: Export your inbound links in Moz Pro to get a quick and easy list of target URLs from your site. If you’re dealing with a massive website, consider using the Moz API to export data beyond what’s manageable in Excel or Google Sheets.

It’s important to note that Moz Pro doesn’t confirm if URLs are indexed or discovered by Google. However, since most sites apply the same robots.txt rules to Moz’s bots as they do to Google’s, this method generally works well as a proxy for Googlebot’s discoverability .

Google Search Console offers several valuable sources for building your list of URLs.

Similar to Moz Pro, the Links section provides exportable lists of target URLs. Unfortunately, these exports are capped at 1,000 URLs each. You can apply filters for specific pages, but since filters don’t apply to the export, you might need to rely on browser scraping tools—limited to 500 filtered URLs at a time. Not ideal.

This export gives you a list of pages receiving search impressions. While the export is limited, you can use Google Search Console API for larger datasets. There are also free Google Sheets plugins that simplify pulling more extensive data.

This section provides exports filtered by issue type, though these are also limited in scope.

The Engagement → Pages and Screens default report in GA4 is an excellent source for collecting URLs, with a generous limit of 100,000 URLs .

Even better, you can apply filters to create different URL lists, effectively surpassing the 100k limit. For example, if you want to export only blog URLs, follow these steps:

Step 3: Define the segment with a narrower URL pattern, such as URLs containing /blog/

Note: URLs found in Google Analytics might not be discoverable by Googlebot or indexed by Google, but they offer valuable insights.

Server or CDN log files are perhaps the ultimate tool at your disposal. These logs capture an exhaustive list of every URL path queried by users, Googlebot, or other bots during the recorded period.

Once you’ve gathered URLs from all these sources, it’s time to combine them. If your site is small enough, use Excel or, for larger datasets, tools like Google Sheets or Jupyter Notebook. Ensure all URLs are consistently formatted, then deduplicate the list.

And voilà—you now have a comprehensive list of current, old, and archived URLs. Good luck!

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

Is AI helping your SEO or sabotaging it? Discover the hidden risks of LLMs and the practical strategies to protect your brand visibility.

Frustrated by technical SEO tickets that never get fixed? In this episode of Whiteboard Friday, Gus Pelogia explains how adopting a "product mindset" can bridge the gap between SEOs and developers. Learn how to leverage sprint planning and discovery meetings, bundle tasks into larger projects, and build MVPs to prove value and get your initiatives prioritized.

In this Whiteboard Friday, learn about headless CMSs, the advantages of using them, and the differences in your approach to SEO.
