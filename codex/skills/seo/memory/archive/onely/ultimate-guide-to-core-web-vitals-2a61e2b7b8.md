---
source: https://www.onely.com/blog/ultimate-guide-to-core-web-vitals/
title: Ultimate Guide to Core Web Vitals
scraped: 2026-03-23
published_on: 2022-05-06
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

# Ultimate Guide to Core Web Vitals

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/ultimate-guide-to-core-web-vitals/
Published: 2022-05-06
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Core Web Vitals are now a Google ranking factor - read this guide to ensure your FID, CLS and LCP metrics pass Google's thresholds!

## Extracted Body
Ensuring your pages offer a great experience is fundamental to satisfying the users’ needs after landing on your page and completing your business goals.

That’s why since Google introduced Core Web Vitals in June 2021 as part of the Page Experience update, these metrics became a quantifiable way of evaluating user experience that actually goes beyond ranking in search.

This article explains what each Core Web Vitals metric measures, how to analyze your scores, and what to do to improve them as part of your SEO strategy in 2023.

Core Web Vitals are essential real-world web metrics that measure user experience on the web. The three metrics they consist of are Largest Contentful Paint (LCP) , First Input Delay (FID) , and Cumulative Layout Shift (CLS).

Core Web Vitals measure specific aspects of user experience:

To understand why Google introduced Core Web Vitals, you need to take a look at Google’s mission .

Google aims to serve its users accurate and useful results to help them fulfill their search intent. However, that should be understood not only content-wise but also from the technical SEO perspective.

Why? Because users may not fully satisfy their search intent when a given page can’t serve them what they’re looking for due to web performance issues. For example, if your page is slow or its elements move unexpectedly, users may leave it unsatisfied before they even get to the main content.

[…] Site speed is always an important aspect of the user experience, which is why Google introduced Core Web Vitals, a set of metrics that measure load performance, interactivity, and visual stability of web pages to gauge the real-world user experience.

That’s why Google understands that pages that significantly lag in performance should drop in rankings as they may not necessarily help users find what they search for.

Also, introducing CWV as ranking signals has brought the awareness of the Page Experience signals to the table. Since then, it has been clear not only to developers and SEOs that optimizing web performance contributes to a website’s overall health.

Except for highlighting the importance of Page Experience factors, CWV help:

In May 2020, Google announced that Core Web Vitals would become a ranking factor to evaluate Page Experience for a better Web.

Over one year later, in June 2021, Core Web Vitals was officially introduced as part of the Google Page Experience update.

Initially, the Page Experience signals were used only in mobile rankings. However, since another rollout in February 2022, the Page Experience update also impacts your rankings on desktop .

The metrics went live as part of the Page Experience update signals, including previously existing factors like mobile-friendliness, HTTPS, and no intrusive interstitials.

If you want to learn more on the topic of Page Experience and the rollout of the update, head to our article on Google Page Experience update .

Core Web Vitals are metrics determining user experience in specific, measurable ways.

Improved user experience means users can easily find what they are looking for when visiting your site, and it will be more likely for them to return.

As you know, Core Web Vitals are a confirmed Google ranking factor, but their impact on rankings isn’t crystal clear.

Here is John Mueller’s response from Google SEO Office Hours on February 26th, 2021, to a question about the influence of Core Web Vitals on search results:

[…] Relevance is still, by far, much more important. So just because your website is faster with regards to the Core Web Vitals than some competitor’s doesn’t necessarily mean that, come May, you will jump to position number one in the search results. […] It should make sense for us to show the site in the search results. Because as you can imagine, a really fast website might be one that’s completely empty. But that’s not very useful for users. So it’s useful to keep that in mind when it comes to Core Web Vitals. It is something that users notice. It is something that we will start using for ranking. But it’s not going to change everything completely. So it’s not going to destroy your site and remove it from the index if you have it wrong. It’s not going to catapult you from page 10 to number-one position if you get it right.

In a Twitter post, John attempted to show the influence of CWV scores in a bit more detail:

Measuring the impact of Core Web Vitals on rankings has been difficult for members of the SEO community. When the Page Experience update rolled out, many other updates occurred in search, like the spam updates and a core update in July 2021 .

This makes it tricky to separate the influence of CWV from other changes, and it’s when you should consider taking advantage of technical SEO services .

Also, how would one even go about isolating CWV as the direct cause of ranking changes, given all the other external factors, algorithm tweaks, and how long it takes Google the process the changes?

According to SISTRIX , pages that meet all of Google’s recommended thresholds for CWV metrics rank one percentage point better than the average, equal to a 37% improvement. Meanwhile, pages that failed at least one CWV metric ranked 3.7% worse on SISTRIX’s Visibility Index.

Moz found that the most significant impact of CWV metrics occurred for URLs that failed tests for all three metrics , which saw a drop by 1.15 positions:

Either way, the impact of Core Web Vitals goes well beyond simply being a ranking factor. User experience can influence your business’ success – for example, it could increase conversion rates.

[…] The other thing to keep in mind with core web vitals is that it’s more than a random ranking factor, it’s also something that affects your site’s usability after it ranks (when people actually visit). If you get more traffic (from other SEO efforts) and your conversion rate is low, that traffic is not going to be as useful as when you have a higher conversion rate (assuming UX/speed affects your conversion rate, which it usually does). CWV is a great way of recognizing and quantifying common user annoyances.

Working on improving CWV metrics is definitely an SEO aspect that shouldn’t be neglected.

But before you get your hands dirty in the optimization process, let’s take a closer look at each of these metrics.

LCP is a metric focused on how long the page’s main content takes to load.

In other words, LCP quantifies how long it takes for users to see what they’re looking for rendered on the screen.

Also, it’s usually true that the largest element in the viewport is the one that the user needs to see immediately. The examples of the main content’s largest elements will typically be the hero image, video, or large paragraph of text.

For an in-depth analysis of how to measure and improve LCP, follow our guide to Largest Contentful Paint .

FID measures how long it takes for a user to interact with the page.

That time is measured from when a user first interacts with a web page after entering it to when the browser can start processing that interaction.

An example of an FID situation is when you take action, and the browser reacts to your action with a significant delay.

It also means that FID helps you discover how long tasks running on the browser’s main thread result in a poor experience for your website’s users.

For an in-depth analysis of how to measure and improve FID, follow our guide to First Input Delay .

How much time the main thread on your pages is blocked from user interaction?

Learn how to measure it in the lab! Read our article about Total Blocking Time (TBT) and how it’s related to First Input Delay.

CLS determines how much elements on a page shift during page load, measuring the visual stability of content.

Your page elements should be as stable as possible to be easily clickable for users and ensure the layout shift doesn’t prevent them from completing the desired action.

To provide a more detailed description, a score of 0 means the page’s contents are fully static during the page’s lifecycle, while a higher score means the contents are moving. It’s recommended that you keep your CLS score under 0.1.

For an in-depth analysis of how to measure and improve CLS, follow our guide to Cumulative Layout Shift .

For each of the Core Web Vitals metrics, Google identified appropriate thresholds that correspond to different scores:
