---
source: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
title: How to specify a canonical URL with rel="canonical" and other methods
scraped: 2026-05-18
tags: google, official, rel_canonical, redirects, sitemaps
topic: canonical_methods
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: canonical implementation methods and signal stacking
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# How to specify a canonical URL with rel="canonical" and other methods

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
Page updated label: 2026-03-27 UTC

## Why This Matters
canonical implementation methods and signal stacking

## Extracted Passages
- To specify a canonical URL for duplicate or very similar pages to Google Search, you can indicate your preference using a number of methods. These are, in order of how strongly they can influence canonicalization:
- Keep in mind that these methods can stack and thus become more effective when combined. This means that when you use two or more of the methods, that will increase the chance of your preferred canonical URL appearing in search results.
- While we encourage you to use these methods, none of them are required; your site will likely do just fine without specifying a canonical preference. That's because if you don't specify a canonical URL, Google will identify which version of the URL is objectively the best version to show to users in Search .
- While it's generally not critical to specify a canonical preference for your URLs, there are a number of reasons why you would want to explicitly tell Google about a canonical page in a set of duplicate or similar pages:
- The following table compares the different canonicalization methods, highlighting their strengths and weaknesses when it comes to maintenance and efficacy in different scenarios.
- Google supports explicit rel canonical link annotations as described in RFC 6596 . rel="canonical" annotations that suggest alternate versions of a page are ignored; specifically, rel="canonical" annotations with hreflang , lang , media , and type attributes are not used for canonicalization. Instead, use the appropriate link annotations to specify alternate versions of a page; for example, link rel="alternate" hreflang for language and country annotations.
- We recommend that you choose one of these and go with that; while supported, using both methods at the same time is more error prone (for example, you might provide one URL in the HTTP header, and another URL in the rel="canonical" link element).
- A rel="canonical" link element (also known as a canonical element ) is an element used in the head section of HTML to indicate that another page is representative of the content on the page.
- Suppose you want https://example.com/dresses/green-dresses to be the canonical URL, even though a variety of URLs can access this content. Indicate this URL as canonical with these steps:
- Use absolute paths rather than relative paths with the rel="canonical" link element. Even though relative paths are supported by Google, they can cause problems in the long run (for example, if you unintentionally allow your testing site to be crawled) and thus we don't recommend them.
- The rel="canonical" link element is only accepted if it appears in the section of the HTML, so make sure at least the section is valid HTML .
- If you use JavaScript to add the rel="canonical" link element, make sure to inject the canonical link element properly .
- If you can change the configuration of your server, you can use a link HTTP response header with a rel="canonical" target attribute as defined by RFC5988 rather than an HTML element to indicate the canonical URL for a document supported by Search, including non-HTML documents such as PDF files.
- If you publish content in many file formats, such as PDF or Microsoft Word, each on their own URL, you can return a rel="canonical" HTTP header to tell Googlebot what is the canonical URL for the non-HTML files. For example, to indicate that the PDF version of the .docx version should be canonical, you might add this HTTP header for the .docx version of the content:
- As with the rel="canonical" link element, use absolute URLs in the rel="canonical" HTTP header.
- Pick a canonical URL for each of your pages and submit them in a sitemap . All pages listed in a sitemap are suggested as canonicals; Google will decide which pages (if any) are duplicates, based on similarity of content.
- Supplying the preferred canonical URLs in the sitemaps is a straightforward way of defining canonicals for a large site, and sitemaps are a useful way to tell Google which pages you consider most important on your site.
- Use this method when you want to get rid of existing duplicate pages. All permanent redirection methods have the same effect on Google Search, however the time it takes for search engines to notice the different redirect methods may differ.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

