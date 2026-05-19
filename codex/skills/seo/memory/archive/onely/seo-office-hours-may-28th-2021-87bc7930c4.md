---
source: https://www.onely.com/blog/seo-office-hours-may-28th-2021/
title: SEO Office Hours - May 28th, 2021
scraped: 2026-03-23
published_on: 2021-05-31
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

# SEO Office Hours - May 28th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-may-28th-2021/
Published: 2021-05-31
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on May 28th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on May 28th, 2021.

0:44 – “Suppose I want to launch a site in Germany. Is it required that I get a .de domain?”

John says this is not required. “If you want to use geo-targeting, there are two ways to do that. One is to use the top-level country domains […] The other is to use a generic top-level domain and to use the geo-targeting setting in Search Console.”

“The hosting location is also not required.” This was relevant before the setting in Search Console was available.

Get a deeper insight into geo-targeting with our International SEO article.

02:50 – “I have an English website. I want to make a German website. Suppose I use a translator like Google Translate. Will Google see this as duplicate content?”

According to John, translated content is not duplicate content.

“Translated content is unique content. It’s different words, different letters on the page. Depending on how you translate that, it would be more of a quality issue. If you use an automatic translating tool to translate the whole website automatically into a different website, then we would probably see that as a low-quality website. Often, the translations are not that good.”

John even warns that if the content is of really low quality, the webspam team might penalize it for being automatically generated content.

On the other hand, “if you take a translation tool, and then you rework it with translators who know the language, and you create a better version, then that’s perfectly fine”.

Google Search Console notified you about indexing problems due to duplicate content? Read our guides and fix:

Yes. “We use the sitemap to help us to crawl better, but it doesn’t replace crawling. So if your sitemap is old and your content is updated, we will crawl your website normally in addition to the sitemap. But if you tell us in a sitemap file that [changes were made], then we can crawl more efficiently.”

“On the one hand, we can find the link, so it’s not problematic, but we do get a lot of value from the context of individual links. In particular, we look at the anchor text length, we look at the before and after the links as well, so with a superscript, you are essentially just listing the URL and taking the URL out of the context of the rest of the page. That makes it a lot harder for us to understand the connection between your content and what you’re linking to.”

John recommends avoiding using superscript links if possible.

20:48 – “We’ve made a few recent large changes to our sitemap (both adding and removing pages) in an effort to improve our SEO. To our surprise, each change significantly reduced our impressions and/or clicks. Does Google penalize – directly or indirectly – for large sitemap changes? On the other hand, does Google boost more long-standing content?”

According to John, no. “Sitemap file changes are perfectly fine. Some websites have a lot of sitemap changes that they do because they make changes to their pages a lot. The sitemap file helps us to crawl more efficiently. The sitemap file is not a ranking factor. […] We don’t boost long-standing content […] Sometimes you want something like a stable reference to find more information about your topic, sometimes people want to find the newest updates on a specific topic. That intent can change over time. ”

27:51 – ”If we have a blog post about the finances of a company, which is only relevant for a few months/year (until their next report comes out), is it better to update that blog post or create a new one in terms of SEO for Google? Does it hurt the SEO to have a page change every month or 3 months?”

“Assuming you want the financial pages to show up in search […] the approach is to have one stable URL for this content, and usually you would want to keep the older versions and archive them.”

“You can apply the same technique to anything that you update regularly.”

31:12 – “My site has a page with multiple iframes which are updated monthly. The source is graphs that I make with Plotly (JavaScript), which I then host on web pages (that are not available throughout the website anywhere else). Should I put a no-follow on those pages, so they don’t get ranked?”

John recommends using a rel=”canonical” on the iframe content to point back to your general page. You can’t put a no-follow on an iframe.

42:37 – “Does getting more Google reviews or responding to them increase your SEO ranking in any way? If so, could you explain how?”

John says, “As far as I know, no”. It may affect something on the Google My Business side, in local listings, or in map search. “At least from an SEO point of view, we don’t look at the number of Google reviews you have.”

43:12 – “I have implemented a custom tracking for my website that is triggered by JavaScript on page load and hits a subdomain. Seeing crawl stats for my domain property, I identified that 1/3 of all crawls are on that tracking subdomain. Could this be interfering in the crawling of the main subdomain? What would be the best approach to avoid this tracking subdomain to be crawled?”

“First of all, if it’s a tracking script, and it’s not necessary for your content, you can block it by robots.txt […] My guess is that this wouldn’t be negatively affecting your website anyway. It’s very possible that you’re seeing this as something that is visible in the reports, but not necessarily something that is causing issues on your website.”

“In particular, if we can crawl your normal content quickly enough […] then I would not worry about this.”

Are your pages “ Blocked by robots.txt ” in Google Search Console?

Read our article to ensure you blocked the crawling of your URLs on purpose.

45:06 – “GSC Mobile usability report says ‘text too small to read’. What is the minimum font size we should maintain?”

“I don’t think we have the exact font size documented. However, in the Lighthouse tool, where there’s also a mobile-friendliness test that you can do, it looks out for 12.5”.

Especially if this is an issue across some URLs, not the entire website, this may be “triggered when the CSS for your pages can’t be loaded properly.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
