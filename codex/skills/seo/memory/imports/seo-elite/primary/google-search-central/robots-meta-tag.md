---
source: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
title: Robots meta tag, data-nosnippet , and X-Robots-Tag specifications
scraped: 2026-05-18
tags: google, official, robots_meta, x_robots_tag, nosnippet
topic: robots_controls
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: page-level and resource-level control over indexing, snippets, and AI-use boundaries
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Robots meta tag, data-nosnippet , and X-Robots-Tag specifications

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
Page updated label: 2026-03-24 UTC

## Why This Matters
page-level and resource-level control over indexing, snippets, and AI-use boundaries

## Extracted Passages
- This document details how the page- and text-level settings can be used to adjust how Google presents your content in search results. You can specify page-level settings by including a meta tag on HTML pages or in an HTTP header. You can specify text-level settings with the data-nosnippet attribute on HTML elements within a page.
- Keep in mind that these settings can be read and followed only if crawlers are allowed to access the pages that include these settings.
- The rule applies to search engine crawlers. To block non-search crawlers, such as AdsBot-Google , you might need to add rules targeted to the specific crawler (for example, ).
- The robots meta tag lets you use a granular, page-specific approach to controlling how an individual HTML page should be indexed and served to users in Google Search results. Place the robots meta tag in the section of a given page, like this:
- If you use a CMS, such as Wix, WordPress, or Blogger , you might not be able to edit your HTML directly, or you might prefer not to. Instead, your CMS might have a search engine settings page or some other mechanism to tell search engines about meta tags.
- If you want to add a meta tag to your website, search for instructions about modifying the of your page on your CMS (for example, search for "wix add meta tags").
- In this example, the robots meta tag instructs search engines not to show the page in search results. The value of the name attribute ( robots ) specifies that the rule applies to all crawlers. Both the name and the content attributes are case-insensitive. To address a specific crawler, replace the robots value of the name attribute with the user agent token of the crawler that you are addressing. Google supports two user agent tokens in the robots meta tag; other values are ignored:
- For example, to instruct Google specifically not to show a snippet in its search results, you can specify googlebot as the name of the meta tag:
- To show a full snippet in Google's web search results, but no snippet in Google News, specify googlebot-news as the name of the meta tag:
- Note: Google Search doesn't enforce placement of meta robots in the HTML head and will respect robots meta tags in the body section of an HTML document as well.
- To block indexing of non-HTML resources, such as PDF files, video files, or image files, use the X-Robots-Tag response header instead.
- The X-Robots-Tag can be used as an element of the HTTP header response for a given URL. Any rule that can be used in a robots meta tag can also be specified as an X-Robots-Tag . Here's an example of an HTTP response with an X-Robots-Tag instructing crawlers not to index a page:
- Multiple X-Robots-Tag headers can be combined within the HTTP response, or you can specify a comma-separated list of rules. Here's an example of an HTTP header response which has a noimageindex X-Robots-Tag combined with an unavailable_after X-Robots-Tag .
- The X-Robots-Tag may optionally specify a user agent before the rules. For instance, the following set of X-Robots-Tag HTTP headers can be used to conditionally allow showing of a page in search results for different search engines:
- Rules specified without a user agent are valid for all crawlers. The HTTP header, the user agent name, and the specified values are not case sensitive.
- Conflicting robots rules: In the case of conflicting robots rules, the more restrictive rule applies. For example, if a page has both max-snippet:50 and nosnippet rules, the nosnippet rule will apply.
- The following rules, also available in machine-readable format , can be used to control indexing and serving of a snippet with the robots meta tag and the X-Robots-Tag . Each value represents a specific rule. Multiple rules may be combined in a comma-separated list or in separate meta tags. These rules are case-insensitive.
- Do not show this page, media, or resource in search results. If you don't specify this rule, the page, media, or resource may be indexed and shown in search results.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

