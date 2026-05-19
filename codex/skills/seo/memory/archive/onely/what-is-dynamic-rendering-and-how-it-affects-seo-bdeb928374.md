---
source: https://www.onely.com/blog/what-is-dynamic-rendering-and-how-it-affects-seo/
title: What Is Dynamic Rendering and How It Affects SEO
scraped: 2026-03-23
published_on: 2023-02-22
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# What Is Dynamic Rendering and How It Affects SEO

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/what-is-dynamic-rendering-and-how-it-affects-seo/
Published: 2023-02-22
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Dynamic rendering allows you to serve Googlebot with as much content as possible while not asking it to render any JavaScript on its end. Read the article to learn how it may affect your SEO.

## Extracted Body
Dynamic rendering is a relatively new approach among the various ways of serving your content to search engine crawlers. Today, we’ll delve into dynamic rendering and how it affects SEO.

Dynamic rendering is one of the possible server configurations for serving your website’s content to users and bots. It consists of the following:

Dynamic rendering allows you to serve Googlebot with as much content as possible while not asking it to render any JavaScript on its end. At the same time, you’re still serving human users with the full experience of your JavaScript-powered content.

It makes dynamic rendering possibly beneficial for SEO as you shouldn’t rely on Google always having the resources to render JavaScript on the spot . By sending Googlebot an HTML version of your pages, you ensure your content gets crawled and indexed as quickly as possible.

In short, using two separate serving mechanisms, dynamic rendering serves the same content to human users and bots.

Dynamic rendering may be a viable solution for JavaScript-powered websites if you don’t want to implement full server-side rendering.

Dynamic rendering is a workaround for indexable, public JavaScript-generated content that changes rapidly or content that uses JavaScript features that aren’t supported by the crawlers you care about.

Most modern websites use JavaScript to some extent to render specific dynamically injected content sections for visual effects or traffic analytics. While Googlebot doesn’t need to see your analytics scripts or flashy animations on your website, it needs to discover any relevant content to surface it on Google Search.

Google has been able to render JavaScript for many years now. Still, our research shows that JavaScript content often gets crawled and indexed with a significant delay and, in extreme cases, doesn’t get discovered at all. Moreover, Googlebot may struggle with the rendering of some bleeding-edge JavaScript features.

In principle, dynamic rendering is not recommended to anyone any longer as a viable long-term solution, according to the updated documentation from Google :

Dynamic rendering is a workaround and not a long-term solution for problems with JavaScript-generated content in search engines.

We have a separate article about why dynamic rendering is not recommended as a default rendering solution for JavaScript-powered websites.

Similar to server-side rendering, dynamic rendering ensures that search engine crawlers are able to access and index content on JavaScript-heavy sites. That means more pages can be included in the index and receive traffic from the organic search.

It can also make Google crawl and index your content faster as you’re removing the cost of rendering JavaScript , which sometimes makes Google need more time to process JS-powered websites.

With more of your pages fully indexed on Google, more of them will appear in the SERPs. Simple as that.

Google is vocal about its stance on dynamic rendering. It encourages webmasters to use it in some instances, but only when “absolutely necessary.”

When Google made recommendations for dynamic rendering in 2018, it was immediately reported that the concept was only a temporary workaround to the problems crawlers have had with rendering JavaScript. Google also clarified that the solution is recommended for websites where a large amount of content is generated using JavaScript – making it potentially inaccessible to search engine robots.

In 2022, Google updated the documentation to say that dynamic rendering is not a long-term solution for websites with JavaScript-generated content. Google recommends other configurations, such as server-side rendering. Server-side rendering provides better performance, is easier to maintain, and yields more consistent results.

Other solutions, such as static rendering or hydration, can also be used.

Dynamic rendering is not cloaking as long as it produces (roughly) the same content for users and crawlers.

Furthermore, error pages produced during dynamic rendering will not be considered a form of cloaking but rather treated as other error pages. In terms of serving different content to users and crawlers, if a website displays a page about Italy to visitors while delivering a page about Spain to search engines, this could be deemed an act of cloaking.

Dynamic rendering can solve some JavaScript-related challenges and inconveniences. These include errors while Google is trying to render the page, taking more time to index the content, scripts that may load incorrectly, and a large number of fetch requests for Googlebot, which could result in a more rapid depletion of the crawl budget .

Dynamic rendering is something to consider if your website is JavaScript-heavy and Google doesn’t index your content as quickly or thoroughly as you’d expect. When used correctly, at least temporarily, dynamic rendering can help address the crawling and indexing issues that crawlers may have with your website.

However, Google emphasizes that dynamic rendering is only a temporary solution, and other methods, such as server-side rendering, should be chosen over dynamic rendering when possible. Therefore, if you decide to use dynamic rendering, consult our technical SEO consultants , who will advise you on the best way to proceed.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
