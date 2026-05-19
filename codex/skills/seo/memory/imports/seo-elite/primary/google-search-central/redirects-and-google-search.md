---
source: https://developers.google.com/search/docs/crawling-indexing/301-redirects
title: Redirects and Google Search
scraped: 2026-05-18
tags: google, official, redirects, site_moves, canonicalization
topic: redirects
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: redirect behavior, migration handling, and URL transition reasoning
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Redirects and Google Search

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/301-redirects
Page updated label: 2026-04-14 UTC

## Why This Matters
redirect behavior, migration handling, and URL transition reasoning

## Extracted Passages
- Redirecting URLs is the practice of resolving an existing URL to a different one, effectively telling your visitors and Google Search that a page has a new location. Redirects are particularly useful in the following circumstances:
- While your users generally won't be able to tell the difference between the different types of redirects, Google Search uses certain types of redirects as a signal that the redirect target should be canonical. Choosing a redirect depends on how long you expect the redirect will be in place and what page you want Google Search to show in search results:
- The following table explains the various ways you can use to set up permanent and temporary redirects, ordered by how likely Google is able to interpret correctly (for example, a server side redirect has the highest chance of being interpreted correctly by Google). Choose the redirect type that works for your situation and site:
- Googlebot follows the redirect, and the indexing pipeline uses the redirect as a signal that the redirect target should be canonical .
- Googlebot follows the redirect, but the indexing pipeline doesn't use the redirect as a signal that the redirect target should be canonical. The target page might still be indexed if other canonicalization signals are present.
- Setting up server-side redirects requires access to the server configuration files (for example, the .htaccess file on Apache) or setting the redirect headers with server-side scripts (for example, PHP). You can create both permanent and temporary redirects on the server side.
- If you need to change the URL of a page as it is shown in search engine results, we recommend that you use a permanent server-side redirect whenever possible. This is the best way to ensure that Google Search and people are directed to the correct page. The 301 and 308 status codes mean that a page has permanently moved to a new location.
- If you just want to send users to a different page temporarily, use a temporary redirect. This will also ensure that Google isn't influenced by the redirect which may help keep the old URL in its Search results. For example, if a service your site offers is temporarily unavailable, you can set up a temporary redirect to send users to a page that explains what's happening, without compromising the original URL in search results.
- The implementation of server-side redirects depends on your hosting and server environment, or the scripting language of your site's backend.
- To set up a permanent redirect with PHP, use the header() function. You must set the headers before sending anything to the screen:
- If you have access to your web server configuration files, you may be able to write the redirect rules yourself. Follow your web server's guides:
- Apache: Consult the Apache .htaccess Tutorial , the Apache URL Rewriting Guide , and the Apache mod_alias documentation . For example, you can use mod_alias to set up the simplest form of redirects:
- NGINX: Read about Creating NGINX Rewrite Rules on the NGINX blog. As with Apache, you have multiple choices to create redirects. For example:
- If server-side redirects aren't possible to implement on your platform, meta refresh redirects may be a viable alternative. Google differentiates between two kinds of meta refresh redirects:
- Place the meta refresh redirect either in the element in the HTML or in the HTTP header with server-side code. For example, here's an instant meta refresh redirect in the element in the HTML:
- Here's an example of the HTTP header equivalent, which you can inject with server-side scripts:
- To create a delayed redirect, which is interpreted as a temporary redirect by Google, set the content attribute to the number of seconds that the redirect should be delayed:
- Google Search interprets and executes JavaScript using the Web Rendering Service once crawling of the URL has completed.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

