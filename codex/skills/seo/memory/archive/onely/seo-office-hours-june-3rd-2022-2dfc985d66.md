---
source: https://www.onely.com/blog/seo-office-hours-june-3rd-2022/
title: SEO Office Hours, June 3rd, 2022
scraped: 2026-03-23
published_on: 2022-07-04
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

# SEO Office Hours, June 3rd, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-june-3rd-2022/
Published: 2022-07-04
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on June 3rd, 2022.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on June 3rd, 2022.

1:22 “[…] It’s theoretically possible to have two different HTTP result codes on a page, but what will Google do with those two codes? Will Google even see them? And if yes, what will Google do? For example, a 503 plus a 302.”

John’s response was: “[…] With the HTTP result codes, you can include lots of different things. Google will look at the first HTTP result code and essentially process that.

And you can theoretically still have two HTTP result codes or more there if they are redirects leading to some final page. So for example, you could have a redirect from one page to another page. That’s one result code. And then on that other page, you could serve a different result code. So that could be a 301 redirect to a 404 page […]. And from our point of view, in those chain situations where we can follow the redirect to get a final result, we will essentially just focus on that final result.

And if that final result has content, then that’s something we might be able to use for canonicalization. If that final result is an error page, then it’s an error page. And that’s fine for us too.”

2:50 “[…] We get the majority of our traffic from a specific country. We hosted our website on a server located in that country. Do you suggest putting our entire website behind a CDN to improve page speed for users globally, or is that not required in our case?”

John answered: “ I don’t think it would have a big effect on Google at all with regards to SEO.

The only effect where I could imagine that something might happen is what users end up seeing. […] If the majority of your users are already seeing a very fast website because your server is located there, then you’re […] doing the right thing. But of course, if users in other locations are seeing a very slow result, because perhaps the connection to your country is not that great, then that’s something where you might have some opportunities to improve that.

[…] If there’s something that you can do to improve things globally for your website, I think that’s a good idea. I don’t think it’s critical […]. But it is something that you can do to […] grow your website past just your current country.

Maybe one thing I should clarify, if Google’s crawling is really, really slow, then of course that can affect how much we can crawl and index from the website […]. I haven’t really seen this as being a problem with regards to any website that isn’t millions and millions of pages large […].

You can double-check how fast Google is crawling in Search Console, and the crawl stats. And if that looks reasonable, even if that’s not super fast, then I wouldn’t really worry about that.”

If you want to expand your website internationally, find out how with our Ultimate Guide to International SEO.

5:20 “[…] Our site currently spends about 20% of the crawl budget on the API subdomain, another 20% on image thumbnails of videos. Neither of these subdomains have content which are part of our SEO strategy. Should we disallow these subdomains from crawling, or how are the API endpoints discovered or used?”

As John said, “[…] In many cases, API endpoints end up being used by JavaScript on a website , and we will render your pages. And if they access an API that is on your website, then we’ll try to load the content from that API and use that for rendering of the page.

And depending on how your API is set up and how your JavaScript is set up, it might be that it’s hard for us to cache those API results, which means that maybe we crawl a lot of these API requests to try to get a rendered version of your pages so that we can use those for indexing. So that’s usually the place where this is discovered. And that’s something you can help by making sure that the API results can be cached, that you don’t inject any timestamps into URLs […] when you’re using JavaScript for the API […].

If you don’t care about the content that’s returned with these API endpoints, then of course you can block this whole subdomain from being crawled with the robots.txt file. And that will essentially block all of those API requests from happening.

[…] You first of all need to figure out, are these API results […] part of […] critical content that I want to have indexed from Google? And if so, then probably you should not block crawling. But if […] it’s […] generating something […] that’s not critical for your pages […], then it might be worthwhile to double-check what it looks like when they’re blocked.

And one way you could double-check this is if you could create a separate test page that doesn’t call the API or that uses a broken URL for the API endpoint. […] You can see how does this page actually render in my browser? How does it render for Google?”

8:05 “Is it appropriate to use a nofollow attribute on internal links to avoid unnecessary crawler requests to URLs which we don’t wish to be crawled or indexed?”

Here is how John responded: “[…] I think, for the most part, it makes very little sense to use nofollow on internal links. But if that’s something that you want to do, go for it.

In the most cases, I will try to do something like using the rel=canonical to point at URLs that you do want to have indexed or using the robots.txt for things that you really don’t want to have crawled.

Try to figure out, is it more like a subtle thing […] that you prefer to have indexed and then use rel=canonical for that? Or is it something where you say– actually, when Googlebot accesses these URLs, it causes problems for my server. It causes a large load. It makes everything really slow. It’s expensive or what have you.

And for those cases, I would just disallow crawling of those URLs. […] With the rel=canonical, obviously, we’ll first have to crawl that page to see the rel=canonical. But over time, we will focus on the canonical that you’ve defined. And we’ll use that one primarily for crawling and indexing.”

16:02 “Is there any strategy by which desired pages can appear as a site link in Google Search results?”

John clarified that “[…] There is no meta tag or structured data that you can use to enforce a site link to be shown .

[…] Our systems try to figure out what is […] related or relevant for users when they’re looking at this one web page […]? […] Our recommendation is essentially to have a good website structure, to have clear internal links so that it’s easy for us to recognize which pages are related to those pages, and to have clear titles that we can use and […] show as a site link.

[…] It’s not that there’s a guarantee that any of this will be shown like that. But it kind of helps us to figure out what is related. And if we do think it makes sense to show a site link, then it’ll be a lot easier for us to actually choose one based on that information.”

17:14 “Our website uses iframes and a script to embed PDF files onto our pages and our website. Is there any advantage to taking the OCR text of the PDF and pasting it somewhere into the document’s HTML for SEO purposes, or will Google simply parse the PDF contents with the same weight and relevance to index the content?”

John responded: “[…] It sounds like you want to take the text of the PDF and […] hide it in the HTML for SEO purposes. And that’s something I would definitely not recommend doing. If you want to have the content indexable, then make it visible on the page.

[…] We do try to take the text out of the PDFs and index that for the PDFs themselves. From a practical point of view, what happens with a PDF is as one of the first steps, we convert it into an HTML page and we try to index that like an HTML page. […] What you’re doing is […] iframing an indirect HTML page. And when it comes to iframes, we can take that content into account for indexing within the primary page. But it can also happen that we index the PDF separately anyway. […] I would turn the question around and frame it as what do you want to have happen?

And if you want your normal web pages to be indexed with the content of the PDF file, then make it so that that content is immediately visible on the HTML page. So instead of embedding the PDF as a primary piece of content, make the HTML content the primary piece and link to the PDF file.

And then there is a question of do you want those PDFs indexed separately or not? Sometimes you do want to have PDFs indexed separately. And if you do want to have them indexed separately, then linking to them is great.

If you don’t want to have them indexed separately, then using robots.txt to block their indexing is also fine. You can also use the noindex [? x-robots ?] HTTP header. It’s a little bit more complicated because you have to serve that as a header for the PDF files if you want to have those PDF files available in the iframe, but not actually indexed.”

23:24 “Does Google crawl URLs located in structured data markup or does Google just store the data?”

John explained that “For the most part, when we look at HTML pages, if we see something that looks like a link, we might go off and try that URL out as well. […] If we find a URL in JavaScript, we can try to pick that up and try to use it. If we find a link in a text file on a site, we can try to crawl that and use it. But it’s not really a normal link.

[…] If you want Google to go off and crawl that URL, make sure that there’s a natural HTML link to that URL , with a clear anchor text as well, that you give some information about the destination page.

If you don’t want Google to crawl that specific URL, then maybe block it with robots.txt or on that page, use a rel=canonical pointing to your preferred version, anything like that. […] I would not blindly assume that just because it’s in structured data it will not be found, nor would I blindly assume that just because it’s in structured data it will be found.

[…] I would instead focus on what you want to have happen there. If you want to have it seen as a link, then make it a link. If you don’t want to have it crawled or indexed, then block crawling or indexing […].”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
