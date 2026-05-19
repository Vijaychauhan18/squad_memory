---
source: https://www.onely.com/blog/googles-rendering-delay-5-seconds/
title: Google's Rendering Delay is Now 5 Seconds BUT...
scraped: 2026-03-23
published_on: 2019-11-26
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

# Google's Rendering Delay is Now 5 Seconds BUT...

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/googles-rendering-delay-5-seconds/
Published: 2019-11-26
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Google's rendering delay time is 5 seconds now! But what does it mean for indexing JavaScript content? See Onely's research!

## Extracted Body
. . . Onely’s research reveals that the delay in indexing JavaScript content is still very much there.

In May 2018 during the Google I/O conference, Tom Greenaway, a developer advocate at Google, said:

“So if the page has JavaScript in it, the rendering is actually deferred until we have the resources ready to render the client-side content , and then we index the content further. So Googlebot might index a page before rendering is complete and the final render can actually arrive several days later, and when that final render does arrive, then we perform another wave of indexing on that client-side rendered content .”

Then John Mueller, Webmaster Trends Analyst at Google, confirmed this in a tweet:

A year before, in 2017, Bartosz Góralewicz, the CEO of Onely, conducted research that showed how Google was struggling with crawling and indexing JavaScript content , and it took many SEOs by surprise. It turned out that Google couldn’t find and follow links placed within content injected with JavaScript, regardless of the framework used to build the test pages.

However, the research conducted and announced by Onely is one thing; an official admission by Google is something else entirely.

Google’s announcements resonated throughout the industry and the “two waves of indexing” has since become the go-to phrase that SEOs use to caution their clients about using JavaScript.

Google has since made huge improvements in rendering JavaScript.

We definitely noticed that when trying to reproduce the results of our 2017 experiment – Google fully rendered and indexed all the JavaScript-powered websites that we fed it without breaking a sweat.

We were eagerly waiting for Google to announce how much of a technical leap had been made, and it finally came during Chrome Developer Summit in November 2019.

Splitt said this in regard to crawling and indexing JavaScript content:

“(…) last year Tom [Greenaway] and I were on this stage and telling you, “Well, you know, it can take up to a week, we are very sorry for this.” Forget this, okay? Because the new numbers look a lot better. So we actually went over the numbers and found that, it turns out that at median, the time we spent between crawling and actually having rendered these results is – on median – it’s five seconds!”

This is truly an amazing score for Google to have achieved, especially when contrasted with the issues Googlebot had with rendering JavaScript just a year ago.

Struggling with rendering issues? Go for Rendering SEO services to unleash your full search visibility.

Onely conducted additional research and, as much as we hate to rain on everyone’s parade, it turned out that things are still far from perfect.

When we put together what both Greenaway and Splitt said, the second wave of indexing should now occur after a median of 5 seconds, right? Our article on how much content was not indexed by Google shows that even though the median rendering delay may be virtually non-existent for new websites, the delay in indexing JavaScript content is still very much there.

One of our tools, The Google Indexing Forecast (TGIF) , quantifies the average delay between when a JavaScript-powered page is added to a website’s sitemap and when its JavaScript content finds its way into Google’s index.

Depending on the sample, an average of 5-50% of the newly added pages we’re tracking have JavaScript elements that remain unindexed after 2 weeks from being added to the sitemap!

“So there’s a whole lot of stuff happening in between these two points [crawling and indexing] (…) But that means that if we are only coming around crawling every now and then, and then like certain things happen on our site that you don’t have to worry about, it might take a while until you actually see things in the index. But that doesn’t mean that JavaScript held them back. ”

So, in contrast to what Greenaway said in May 2018, delayed rendering is not the only factor that contributes to the delayed indexing of JavaScript.

We all know that the crawl budget is correlated with indexing – there’s no indexing without crawling.

In many cases where a website isn’t fully indexed, we can see that one of the correlating factors is often an improper use of JavaScript.

tell me more! How Much Content is Not Indexed in Google in 2019?

But JavaScript itself isn’t to blame – it’s the influence it potentially has on the crawl budget.

Every JavaScript file that Google’s crawler has to download means a separate request sent to the server. And if JavaScript files are consolidated, they may be too heavy and result in timeouts. It takes a lot of experience to maintain a balance between the number of external files that need to be fetched and their size.

Another aspect that comes into play is wasting the crawl budget on crawling thin content.

Many websites, particularly e-commerce stores, struggle from duplicate content , infinite spaces, and other structural issues caused by unoptimized JavaScript. These factors were outlined back in 2017 by Gary Ilyes, a member of the Google Search team .

When Googlebot has to go through such thin content, it loses interest in the entire website. It’s a vicious cycle.

It’s great news that Google has gotten so much better with rendering JavaScript. However, we have hard data showing that many websites still suffer from significant delays in indexing their JavaScript content.

You can read more about the subject at “ JavaScript Indexing Delays Are Still an Issue for Google ” which was written by Tomek Rudzki, Onely’s Head of R&D.

Also, reach out to us to find out how we can help you with our JavaScript SEO audit .
