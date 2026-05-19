---
source: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
title: Understand the JavaScript SEO basics
scraped: 2026-05-18
tags: google, official, javascript_seo, rendering, wrs
topic: javascript_seo
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: JavaScript SEO baseline, rendering constraints, and implementation guidance
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Understand the JavaScript SEO basics

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
Page updated label: 2026-03-04 UTC

## Why This Matters
JavaScript SEO baseline, rendering constraints, and implementation guidance

## Extracted Passages
- JavaScript is an important part of the web platform because it provides many features that turn the web into a powerful application platform. Making your JavaScript-powered web applications discoverable via Google Search can help you find new users and re-engage existing users as they search for the content your web app provides. While Google Search runs JavaScript with an evergreen version of Chromium , there are a few things that you can optimize .
- This guide describes how Google Search processes JavaScript and best practices for improving JavaScript web apps for Google Search.
- Googlebot queues pages for both crawling and rendering. It is not immediately obvious when a page is waiting for crawling and when it is waiting for rendering. When Googlebot fetches a URL from the crawling queue by making an HTTP request, it first checks if you allow crawling. Googlebot reads the robots.txt file. If it marks the URL as disallowed, then Googlebot skips making an HTTP request to this URL and skips the URL. Google Search won't render JavaScript from blocked files or on blocked pages.
- Googlebot then parses the response for other URLs in the href attribute of HTML links and adds the URLs to the crawl queue. To prevent link discovery, use the nofollow mechanism .
- Crawling a URL and parsing the HTML response works well for classical websites or server-side rendered pages where the HTML in the HTTP response contains all content. Some JavaScript sites may use the app shell model where the initial HTML does not contain the actual content and Google needs to execute JavaScript before being able to see the actual page content that JavaScript generates.
- Googlebot queues all pages with a 200 HTTP status code for rendering, unless a robots meta tag or header tells Google not to index the page. The page may stay on this queue for a few seconds, but it can take longer than that. Once Google's resources allow, a headless Chromium renders the page and executes the JavaScript. Googlebot parses the rendered HTML for links again and queues the URLs it finds for crawling. Google also uses the rendered HTML to index the page.
- Keep in mind that server-side or pre-rendering is still a great idea because it makes your website faster for users and crawlers, and not all bots can run JavaScript.
- Unique, descriptive elements and meta descriptions help users quickly identify the best result for their goal. You can use JavaScript to set or change the meta description as well as the element.
- The rel="canonical" link tag helps Google find the canonical version of a page. You can use JavaScript to set the canonical URL, but keep in mind that you shouldn't use JavaScript to change the canonical URL to something else than the URL you specified as the canonical URL in the original HTML. The best way to set the canonical URL is to use HTML, but if you have to use JavaScript, make sure that you always set the canonical URL to the same value as the original HTML. If you can't set the canonical URL in the HTML, then you can use JavaScript to set the canonical URL and leave it out of the original HTML.
- Browsers offer many APIs and JavaScript is a quickly-evolving language. Google has some limitations regarding which APIs and JavaScript features it supports. To make sure your code is compatible with Google, follow our guidelines for troubleshooting JavaScript problems .
- We recommend using differential serving and polyfills if you feature-detect a missing browser API that you need. Since some browser features cannot be polyfilled, we recommend that you check the polyfill documentation for potential limitations.
- Googlebot uses HTTP status codes to find out if something went wrong when crawling the page.
- To tell Googlebot if a page can't be crawled or indexed, use a meaningful status code, like a 404 for a page that could not be found or a 401 code for pages behind a login. You can use HTTP status codes to tell Googlebot if a page has moved to a new URL, so that the index can be updated accordingly.
- In client-side rendered single-page apps, routing is often implemented as client-side routing. In this case, using meaningful HTTP status codes can be impossible or impractical. To avoid soft 404 errors when using client-side rendering and routing, use one of the following strategies:
- For single-page applications with client-side routing, use the History API to implement routing between different views of your web app. To ensure that Googlebot can parse and extract your URLs, don't use fragments to load different page content. The following example is a bad practice, because Googlebot can't reliably resolve the URLs:
- Instead, you can make sure your URLs are accessible to Googlebot by implementing the History API:
- While we don't recommend using JavaScript for this, it is possible to inject a rel="canonical" link tag with JavaScript. Google Search will pick up the injected canonical URL when rendering the page. Here is an example to inject a rel="canonical" link tag with JavaScript:
- You can prevent Google from indexing a page or following links through the robots meta tag. For example, adding the following meta tag to the top of your page blocks Google from indexing the page:

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

