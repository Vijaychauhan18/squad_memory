---
source: https://www.oncrawl.com/technical-seo/diagnosing-javascript-issues-in-search/
title: Diagnosing JavaScript Issues In Search - Oncrawl
scraped: 2026-03-23
published_on: 2020-05-19
tags: live_feed, phase1_ingest, oncrawl, publication, technical-seo, ai-visibility, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Oncrawl
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Diagnosing JavaScript Issues In Search - Oncrawl

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/diagnosing-javascript-issues-in-search/
Published: 2020-05-19
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
JavaScript and SEO have experienced a huge amount of change over the past year with search engines being better than ever before at crawling and indexing your content.

## Extracted Body
JavaScript and SEO have experienced a huge amount of change over the past year with search engines being better than ever before at crawling and indexing your content. With these changes, there is still the need to be able to diagnose common issues and answer the most common JavaScript SEO question: “can a search engine see this?” In this post, I explore the process behind finding an issue using your browser and the free tools available to any user.

A key part of diagnosing issues is understanding the difference between the first delivery of HTML and the rendered HTML.

The first set of HTML is raw HTML which hasn’t had any client-side scripts applied. This code is often much lighter, especially so within JavaScript framework websites where the majority of the work is done as the DOM loads in.

The rendered HTML is where the browser has started to run the client-side JavaScript and began to load in all of the content of the page.

We know that search engines are good at rendering JavaScript . This means if you are looking to audit a JavaScript heavy website, we would recommend the following process.

Using Foot Asylum as an example, we can see where the COVID-19 message isn’t available in the source but is present when the DOM has loaded.

While this isn’t an error, it’s always good to get an understanding of what the JavaScript is doing when the code is rendered. At this point, we now understand which parts of the page are loaded in as the DOM completes.

The mobile-friendly test allows you to crawl your website with the full (almost) smartphone Googlebot to see if there are any rendering issues or code being missed out. We know that Google is great at rendering JavaScript but not perfect, so let’s continue to use the Foot Asylum example to understand how it’s being handled. Here we will look for the H2 tag which says ‘Shop the latest’.

After running the website through the tester we can see the validation messaging on the left and the rendered website on the right. The first thing that jumps out is that the image in the tester doesn’t match what we see on a mobile device:

The tester is never perfect as it doesn’t seem to go through the full rendering process that the actual Smartphone bot would, so the next step here is to look at the code available within the mobile-friendly tester to see if the HTML has been picked up. Let’s look for this heading tag:

To do this, we can search the HTML returned in the tester for the text to see if it was picked up by the Smartphone bot:

The content was not found in the mobile-friendly tester. This highlights that there could possibly be an issue with this content so we need to investigate further.

By looking at the cache, we can see if Google has managed to indexed this content:

This highlights how this method isn’t foolproof as Google doesn’t seem to give anywhere near as much rendering time for JavaScript to fire than it would with a normal crawl, which makes sense as it would be costly to run this tool!

Any page within a property you’re verified against can be tested within Google Search Console to see the code that’s in Google’s index. You can compare this against the rendered code from your browsers as well as the Mobile-Friendly Tester to spot any issues:

By clicking the ‘View Crawled Page’ button after inspecting a URL, you can open up the code which Google has for that page in the index. This allows you to look for pieces of content which are heavily reliant on JavaScript to understand if Google has indexed them.

This is an awesome way to see if the content on the page has been successfully indexed where you don’t have to be verified in Search Console. If you take any page you’re looking to audit, you can add site: to the front of it and wrap the content you suspect of having issues in quote marks at the end. Let’s look for some content far down on our own About Us page.

site: https://www.impression.co.uk ‘supporting growth in our local community’

Below you can see the content has been pulled through from the page, from here it’s safe to say that this content is indexed and Google has been able to render it.

If you ever suspect that something isn’t indexed, then this is a really powerful way to check quickly.

JavaScript is a complex subject with many facets. While many SEO’s aren’t comfortable with editing or implementing it, what we can do is make sure we understand how it impacts the websites we are working with.

Using the above methods, you should be able to audit any JavaScript website and be able to spot any issues with how the content can be understood by search engines.
