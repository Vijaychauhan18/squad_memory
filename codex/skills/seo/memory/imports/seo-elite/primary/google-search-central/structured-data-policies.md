---
source: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
title: General structured data guidelines
scraped: 2026-05-18
tags: google, official, structured_data, rich_results, policies
topic: structured_data
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: structured data trust, quality, and compliance checks
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# General structured data guidelines

Source type: official_doc
Original URL: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
Page updated label: 2026-01-06 UTC

## Why This Matters
structured data trust, quality, and compliance checks

## Extracted Passages
- To be eligible for rich result appearance in Google Search results, structured data shouldn't violate the Content policies for Google Search (which include our spam policies ). In addition, this page details the general guidelines that apply to all structured data: they must be followed in order to be eligible for appearance as a rich result in Google Search.
- If your page contains a structured data issue , it can result in a manual action. A structured data manual action means that a page loses eligibility for appearance as a rich result; it doesn't affect how the page ranks in Google web search. To check if you have a manual action, open the Manual Actions report in Search Console .
- Important: Google does not guarantee that your structured data will show up in search results, even if your page is marked up correctly according to the Rich Results Test . Here are some common reasons why:
- You can test compliance with technical guidelines using the Rich Results Test and the URL Inspection tool , which catch most technical errors.
- In order to be eligible for rich results, mark up your site's pages using one of three supported formats :
- Don't block your structured data pages to Googlebot using robots.txt, noindex , or any other access control methods.
- These quality guidelines are not easily testable using an automated tool. Violating a quality guideline can prevent syntactically correct structured data from being displayed as a rich result in Google Search, or possibly cause it to be marked as spam .
- Your structured data must be a true representation of the page content. Here are some examples of irrelevant data:
- Multiple items on a page means that there is more than one kind of thing on a page. For example, a page could contain a recipe, a video that shows how to make that recipe, and breadcrumb information for how people can discover that recipe. All of this user-visible information can also be marked up with structured data, which makes it easier for search engines like Google Search to understand the information on a page. When you add more items that apply to a page, Google Search has a fuller picture of what the page is about and can display that page in different search features.
- Google Search understands multiple items on a page, whether you nest the items or specify each item individually:
- These examples are trimmed for brevity, and they don't include all the required and recommended properties for the features. For a full example, refer to the specific structured data type documentation .
- Here's an example of nested structured data, where Recipe is the main item, and aggregateRating and video are nested in the Recipe .
- Here's an example of individual items of structured data. There are two, distinct items: Recipe and BreadcrumbList .
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

