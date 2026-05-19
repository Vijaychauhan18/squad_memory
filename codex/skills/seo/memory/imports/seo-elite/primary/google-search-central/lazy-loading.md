---
source: https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading
title: Fix lazy-loaded content
scraped: 2026-05-18
tags: google, official, lazy_loading, javascript, pagination
topic: lazy_loading
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: preventing lazy-loading from hiding content from Google
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Fix lazy-loaded content

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading
Page updated label: 2025-12-10 UTC

## Why This Matters
preventing lazy-loading from hiding content from Google

## Extracted Passages
- Deferring loading of non-critical or non-visible content, also commonly known as "lazy-loading", is a common performance and UX best practice. For more information, see web.dev's resources on lazy-loading images and video . However, if not implemented correctly, this technique can inadvertently hide content from Google. This document explains how to make sure Google can crawl and index lazy-loaded content.
- To ensure that Google sees all content on your page, make sure that your lazy-loading implementation loads all relevant content whenever it is visible in the viewport. Here are a few methods to implement lazy-loading:
- The methods mentioned don't rely on user actions, such as scrolling or clicking, to load content, which is important as Google Search does not interact with your page.
- Don't add lazy-loading to content that is likely to be immediately visible when a user opens a page. That might cause content to take longer to load and show up in the browser, which will be very noticeable to the user.
- At a high level, infinite scroll is a technique that loads more content, more distinct pages, as the user scrolls down a long page. This could be one long article that's split into multiple chunks, or a collection of items that's similarly split into chunks. To implement infinite scroll in an indexable way, make sure your website supports paginated loading of these chunks by doing the following:
- After you set up your implementation, make sure it works correctly. You can use the URL Inspection Tool in Search Console to see if all content was loaded. Check the rendered HTML to make sure your content is in the rendered HTML by looking for it in URL Inspection Tool. If your image or video URLs appear in the src attribute on the or elements in the rendered HTML, your setup works correctly.
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

