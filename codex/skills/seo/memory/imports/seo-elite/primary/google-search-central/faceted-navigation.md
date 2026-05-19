---
source: https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation
title: Managing crawling of faceted navigation URLs
scraped: 2026-05-18
tags: google, official, faceted_navigation, crawl_efficiency, parameters
topic: faceted_navigation
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: parameterized URL control and faceted-navigation crawl management
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Managing crawling of faceted navigation URLs

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation
Page updated label: 2025-12-18 UTC

## Why This Matters
parameterized URL control and faceted-navigation crawl management

## Extracted Passages
- Faceted navigation is a common feature of websites that allows its visitors to change how items (for example, products, articles, or events) are displayed on a page. It's a popular and useful feature, however its most common implementation, which is based on URL parameters, can generate infinite URL spaces which harms the website in a couple ways:
- A typical faceted navigation URL may contain various parameters in the query string related to the properties of items they filter for. For example:
- Changing any of the URL parameters products , color , and size would show a different set of items on the underlying page. This often means a very large number of possible combinations of filters, which translates to a very large number of possible URLs. To save your resources, we recommend dealing with these URLs one of the following ways:
- If you want to save server resources and you don't need your faceted navigation URLs to show up in Google Search or other Google products, you can prevent crawling of these URLs with one of the following ways.
- Other ways to signal a preference of which faceted navigation URLs (not) to crawl is using rel="canonical" link element and the rel="nofollow" anchor attribute. However, these methods are generally less effective in the long term than the previously mentioned methods.
- If you need your faceted navigation URLs to be potentially crawled and indexed, ensure you're following these best practices to minimize the negative effects of crawling the large number of potential URLs on your site:
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

