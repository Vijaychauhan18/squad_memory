---
source: https://www.onely.com/blog/seo-office-hours-april-23-2021/
title: SEO Office Hours - April 23rd, 2021
scraped: 2026-03-23
published_on: 2021-04-26
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

# SEO Office Hours - April 23rd, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-april-23-2021/
Published: 2021-04-26
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 23, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 23, 2021.

03:32 – Why does the number of pages reported in the Core Web Vitals report of Google Search Console change?

John said, “Basically, what happens in the aggregate reports is that we show the information from a significant sample of the pages of the website […] and that sample can change over time. So, for example, when you’re looking at speed, if your pages do not change with regards to speed, you might still see the number of pages going up and down there, and that’s just based on us using a slightly different sample”.

John recommended watching out for errors mentioned in the report and working off of that instead of focusing on the sample size .

Struggling with your Core Web Vitals report? Check out our Core Web Vitals services to see how we can help you!

06:03 – “I have implemented a 301 redirect for a page, and it’s working fine. The page is being redirected to the new URL, but Google is not selecting the new one as a canonical, and it is indexing both of the pages.” How do you help Google choose the right canonical URL?

John said, “When it comes to canonicals, we essentially recognize that these two pages are equivalent, and then we try to pick one of them to show in the search results. There is no ranking advantage from having this one or the other one shown […] So, it’s not super critical”.

Google uses redirects as one signal, but there are others, like, internal linking, sitemaps, annotations, and that can all play into what is shown in search.

“The way that you can help us to switch that over is to just make sure that everything is aligned, that all of your internal links are pointing at the new URL, your external links are pointing at the new URL, in the sitemap file, and all of the annotations that you have you always point to the new URL.”

08:14 – Does answering questions on forums like Quora help in building the authority of a website?

According to John, “In general, many sites that use user-generated content use a nofollow on all of their links. So it’s rare that you would get any kind of advantage out of that. It’s also something where, over the years, we’ve seen that people try to abuse this for link-building and that they’ll go to forums and just add random unrelated comments and add their links there, and that’s something that we would recognize as being […] borderline spammy behavior.”

14:25 Based on Google’s blog post on the product reviews, it would seemingly make sense to describe products in a unique way beyond what the manufacturer says. Is this just as important when publishing product listings?

Google will always try to show the most relevant results, so if the unique aspect of your page is, for example, the location, and searches do include that information in their queries, then regardless of whether some other page has the same description, your result will be the most relevant.

John said, “If you can make unique descriptions, that’s always worthwhile, but depending on the type of shop that you have, the number of people that you have working there, sometimes it’s just not realistic to do that for everything.”

17:44 – What are the best practices for using JavaScript to serve customized content to users based on how they came to your site?

John said, “I think the cloaking guidance is definitely worthwhile to look at. I believe we have some guidance on A/B testing in general.”

“With regards to JavaScript-based A/B testing, we don’t necessarily differentiate between javascript and other kinds of A/B testing […] We can render some JavaScript, so it’s possible that we would fall into one of these A/B tests and then just see that version and use it for indexing.”

John also recommends watching out that Google has a “persistent” way of looking at pages. If the page changes every time the bot crawls it, this might make indexing and ranking more difficult. John suggests putting Google into one of the buckets to make sure the page version stays pretty consistent.

“Shifting things around like call-to-actions, changing colors, designs, things like that, that’s absolutely no problem. If you were to significantly change the focus or the purpose of the page, then I think that would be something that would fall more into the cloaking area”.

“The other thing to mention is Googlebot doesn’t keep a referrer, so if you’re doing an A/B test based on referrer, we would just not send anything there.”

Looking for best practices for using JavaScript? Read the ultimate guide to JavaScript SEO on our blog.

25:57 – Does making frequent changes to a site or page hurt the rankings?

John said, “If you make changes on your website, then, in search, we will try to reflect that. If our systems, when they look at the new website, see that everything is better than before, we will try to rank it better, but if they see that things are maybe not as good as they were before, then it can happen that it goes down in ranking as well.”

28:40 – “What contact information is it better to indicate on the Authors page: social network accounts, email addresses, or both? If we can choose only one option, what is more preferable?”

When it comes to authors or any entities behind a website, Google’s systems recognize what that entity is based on several factors. This includes external links but also the visual information on the page.

John recommends “to at least link to […] a central place, where everything comes together for this author, which could be something like a social network profile page, for example. And use that across the different author pages that you have when you’re writing, so that when our systems look at an article, and they see an author page associated with that, they can recognize that this is the same author as the person who wrote something else.”

31:51 – “Google is showing the right title tag but the wrong description and automatically fetching data from my website. How can I correct that?”

Google tries to use the information that you have on your pages when it comes to titles and descriptions. Still, when their systems recognize that the information is not as useful to users as possible, different titles and descriptions may be used.

What’s more, those can also be different for different queries, to provide the most useful information every time.

According to John, “The best way to [make sure] Google does take into account your title and description is to make sure that you’re following Google’s guidelines […] In particular, making sure to avoid keyword stuffing.”

37:40 – “Is it common to see URLs of images in the “Crawled – currently not indexed” report in GSC? The URLs return the correct file header for .jpeg, but they don’t contain a .jpeg extension.”

John said, “We have some heuristics in place to recognize when you’re linking to images and when we can tell that a link goes to an image then we will say oh, this is probably an image and we will process it in image search and we won’t even look at it for web search.

However, if we can’t recognize that it’s an image, then we’ll try to crawl that URL for web search, and then the crawler will say, actually, there was no web page here and [we] weren’t able to index this page”.

This is not necessarily a problem, just information that Google tried to crawl those URLs, and they failed to find a web page.

Here’s the takeaway: “If you’re seeing issues with regards to your images being indexed and you know they don’t have image extensions, then it might be worthwhile to swap those around and make it at least look like they have image extensions so that we can process them immediately with Google Images.”

“We can rank a website that consists of a single page. My general recommendation when you’re working on a website is to try to build out one website and make it as strong as possible and to kind of grow that over time, rather than to create a bunch of disconnected single page websites, but sometimes you just want something completely separate […], and that can absolutely appear in the search results, it can absolutely rank fairly well”.

45:11 – “My mobile URLs have an LCP problem but not in the AMP version. The mobile search results already have AMP URLs, so can I just ignore the LCP issue?”

John said, “We use the page that is actually shown to users as the basis for tracking these things, so if you have valid AMP pages and we’re always showing the valid AMP version to users when they search on mobile, then that’s what we will take into account. If you have an AMP version, but it’s not a valid AMP version, then sometimes we don’t show it as an AMP version in the search results. Then we would take whatever page that users see in the search results and use that as the basis.”

50:17 – “We receive traffic from three devices: tablet, mobile, and desktop. Will Google consider tablet data in the rankings or not?”

John said, “Especially for the Core Web Vitals , we only differentiate between mobile and desktop and we only, or we plan on, only using mobile, at least for the moment.”
