---
source: https://developers.google.com/search/docs/crawling-indexing/robots/intro
title: Introduction to robots.txt
scraped: 2026-05-18
tags: google, official, robots_txt, crawling, discovery
topic: robots_txt
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: robots.txt behavior, crawl blocking, and crawl-directive reasoning
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Introduction to robots.txt

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/robots/intro
Page updated label: 2025-12-10 UTC

## Why This Matters
robots.txt behavior, crawl blocking, and crawl-directive reasoning

## Extracted Passages
- A robots.txt file tells search engine crawlers which URLs the crawler can access on your site. This is used mainly to avoid overloading your site with requests; it is not a mechanism for keeping a web page out of Google . To keep a web page out of Google, block indexing with noindex or password-protect the page.
- If you use a CMS, such as Wix or Blogger , you might not need to (or be able to) edit your robots.txt file directly. Instead, your CMS might expose a search settings page or some other mechanism to tell search engines whether or not to crawl your page.
- If you want to hide or unhide one of your pages from search engines, search for instructions about modifying your page visibility in search engines on your CMS (for example, search for "wix hide page from search engines").
- A robots.txt file is used primarily to manage crawler traffic to your site, and usually to keep a file off Google, depending on the file type:
- You can use a robots.txt file for web pages (HTML, PDF, or other non-media formats that Google can read ), to manage crawling traffic if you think your server will be overwhelmed by requests from Google's crawler, or to avoid crawling unimportant or similar pages on your site.
- Warning : Don't use a robots.txt file as a means to hide your web pages (including PDFs and other text-based formats supported by Google) from Google Search results.
- If other pages point to your page with descriptive text, Google could still index the URL without visiting the page. If you want to block your page from search results, use another method such as password protection or noindex .
- If your web page is blocked with a robots.txt file , its URL can still appear in search results, but the search result won't have a description . Image files, video files, PDFs, and other non-HTML files embedded in the blocked page will be excluded from crawling, too, unless they're referenced by other pages that are allowed for crawling. If you see this search result for your page and want to fix it, remove the robots.txt entry blocking the page. If you want to hide the page completely from Search, use another method .
- Use a robots.txt file to manage crawl traffic, and also to prevent image, video, and audio files from appearing in Google Search results. This won't prevent other pages or users from linking to your image, video, or audio file.
- Before you create or edit a robots.txt file, you should know the limits of this URL blocking method. Depending on your goals and situation, you might want to consider other mechanisms to ensure your URLs are not findable on the web.
- If you decided that you need one, learn how to create a robots.txt file . Or if you already have one, learn how to update it .
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

