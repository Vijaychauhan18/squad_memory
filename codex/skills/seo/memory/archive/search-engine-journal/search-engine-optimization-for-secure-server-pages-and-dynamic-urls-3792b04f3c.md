---
source: https://www.searchenginejournal.com/search-engine-optimization-for-secure-server-pages-and-dynamic-urls/462/
title: Search Engine Optimization for Secure Server Pages and Dynamic URLs
scraped: 2026-03-23
published_on: -0001-11-30T00:00:00+00:00
tags: live_feed, phase1_ingest, search-engine-journal, searchenginejournal, publication, industry-news, archive_backfill, historical_source
topic: industry_news
intent: monitoring, research, source_selection
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Search Engine Journal
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Search Engine Optimization for Secure Server Pages and Dynamic URLs

Source: Search Engine Journal
Homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/search-engine-optimization-for-secure-server-pages-and-dynamic-urls/462/
Published: -0001-11-30T00:00:00+00:00
Strength: broad SEO coverage, platform updates, practitioner commentary

## Summary
Search engines do have the ability to spider secure-server-hosted pages, but often these pages require either that a visitor fill out a form or log in

## Extracted Body
Search engines do have the ability to spider secure-server-hosted pages, but often these pages require either that a visitor fill out a form or log in with a password and user name before being allowed past a certain point. If any page requires filling out of forms or passwords to reach, search engine robots will simply leave. They can’t log in because they can’t fill out forms, leave email addresses or enter passwords.

A Webmaster for a 4,500-page ecommerce web site contacted me. He wondered why search engines were ignoring such a large site. I asked for the URL of the site and visited the home page. I noted that upon loading, there was an immediate passing of the URL http://anybusiness.com site to a secure httpS://anybusiness.com page. This has two immediate faults that may be a problem — the forwarding method and different server. If the instant forward is by JavaScript, then it’s bad news.

First, search engines often either penalize or downgrade sites that use immediate URL forwarding, especially from a home page. URL forwarding suggests doorway pages (a search engine no-no) or affiliate URLs forwarding to an affiliate program site, or the worst of all scenarios, cloaking software on your server. You may not be doing any of these things, but the robots don’t know, don’t care, and don’t index your site, plain and simple.

Secondly, secure servers are very often a separate web site, meaning that the secure server is actually a different machine and is an entirely different site from the non-secure server site unless your site is hosted on a dedicated server on its own IP address, with a security certificate at the same domain. This can happen when secure shopping carts are hosted by a third-party host so that a small ecommerce site needn’t purchase a security certificate or set up complex shopping carts.

For example, if your shopping cart is hosted by Yahoo stores or other application service providers (ASPs), pages hosted in the shopping cart don’t reside on your domain and can’t be recognized as pages on YOUR site unless you also host your domain with the same company. Unfortunately, many shopping cart ASPs use dynamic IP addresses (IP address is different each time you visit) and use database-generated dynamic pages.

The process of serving dynamic pages is not the problem. The problem is simply that the URL of those pages contains several characters that either stop or severely curtail search engine spiders. Question marks (?) are the biggest culprit, followed by ampersands (&), equal signs (=), percent symbols (%) and plus signs (+) in the URLs of dynamic pages.

These symbols serve as alarm bells to the spiders and either turn them away entirely or dramatically slow the indexing of your pages. This is stated simply in the Google “Information for Webmasters” page at :

“Your pages are dynamically generated. We are able to index dynamically generated pages. However, because our web crawler can easily overwhelm and crash sites serving dynamic content, we limit the amount of dynamic pages we index.”

Just because your site is dynamically generated, creating long URLs full of question marks, equal signs and ampersands like www.domain.com/category.asp?ct=this+%28that+other%29&l=thing doesn’t mean you are in search engine limbo. There are simple solutions available for your Webmaster. Here are a couple of articles explaining an elegant solution called “mod_rewrite.”

http://alistapart.com/articles/urls/ http://alistapart.com/articles/succeed/

This technique is simply creating a set of instructions for your web server to present URLs in a different form that replaces those “bad” question marks and ampersands with slash marks (/) instead. The method will require that your Webmaster is a bit more technically savvy than most home-business CEOs who created their own web site. Some hosts will help here by simply turning on the “mod_rewrite” for shared hosting clients.

Don’t play hide and seek with the search engines! Tell them exactly where to find every page on your site — and if there’s any question that they will find every page on your site, give them a map.

Hard-code those dynamic URLs for most subcategories within the categories of different sections of your web site into your comprehensive site map. As long as those dynamic links (even those that include ?=+%& symbols) are hard-coded into a site map, the spiders will follow them. Clearly those 4,500 pages mentioned earlier would be too much for a site map listing. But the main category pages could be provided for the engines.

I visited the site map page of the Webmaster mentioned above and saw 14 pages listed on the site map. That explains why they have 14 pages, not 4,500, indexed by Google.

How to find out how many pages of your site are indexed? Go to Google Search and type “allinurl:www.domain.com” (without the quotes, replacing “domain” in the above example with your own domain name). This query operator will return a list of every page of your site. Look in the blue bar across the top of the Google results page and you’ll see the number of pages indexed at your site!
