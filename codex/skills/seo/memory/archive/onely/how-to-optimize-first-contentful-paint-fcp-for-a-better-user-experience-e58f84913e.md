---
source: https://www.onely.com/blog/first-contentful-paint/
title: How To Optimize First Contentful Paint (FCP) For a Better User Experience?
scraped: 2026-03-23
published_on: 2023-03-10
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

# How To Optimize First Contentful Paint (FCP) For a Better User Experience?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/first-contentful-paint/
Published: 2023-03-10
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
FCP measures how long it takes for the first element of a page to be rendered. Read the article to learn how to optimize it for better UX.

## Extracted Body
First Contentful Paint (FCP) is a web performance metric that measures how long it takes for the first element of a page to be rendered and visible in the user’s browser.

Although FCP is not a Core Web Vitals metric, you shouldn’t ignore it if you care about your user experience.

Why? Because fast FCP means that your users can see that your content is loading, and how fast it’s happening contributes to their satisfaction. And the more satisfied your users are, the more eager they are to stay on your page, explore your content, and convert.

Without further ado, learn how to measure and improve your FCP score to provide your website’s visitors with a positive experience.

First Contentful Paint (FCP) is a user-centric metric calculating the time it takes to render the first content element on a page that’s loading in a browser.

In other words, FCP tracks the time between when a page starts loading and when the first content element is visible in the user’s browser.

To be even more precise, FCP measures how long it takes to render the first Document Object Model (DOM) element that’s:

FCP is an important metric from the UX perspective as it measures how real users perceive the page load and decides on the first impression users have of your page.

For example, imagine users waiting too long for your page to load, seeing only the default background.

How long is ‘too long’ for users to get irritated and want to exit a page? Long enough is when users can already notice the delay.

Fast FCP indicates that ‘something’ is happening in the background. For your users, the first element being rendered on the screen reflects that:

From that perspective, FCP is a metric you shouldn’t ignore.

First Contentful Paint (FCP) can be analyzed based on field and lab data .

You may combine these two ways of measuring performance to ensure unbiased FCP results.

Lab data allows you to measure your FCP score in a test environment with predefined settings.

The following tools can help you track your FCP measured in a lab:

To measure FCP in Chrome DevTools , open the ‘Performance’ section and click the ‘Reload’ button to let the tool analyze your page.

To measure your FCP score in Lighthouse , head to Chrome DevTools and open the ‘Lighthouse’ tab to run a performance audit.

Lighthouse will gather the data and generate the report outlining your FCP score in the ‘Metrics’ section.

Moreover, Lighthouse provides specific suggestions on what you can improve for better FCP. To see them, all you need to do is to filter out the results for FCP above the ‘Opportunities’ and ‘Diagnostics’ sections.

To improve your FCP score for a better user experience, field data is an invaluable source of information as it shows how real users interact with websites on the web.

The important thing is that Google’s field data is based on the Chrome User Experience Report (CrUX), “used by Google Search to inform the page experience ranking factor.” This means that by tracking and optimizing the real user data collected in CrUX, you can directly impact Google’s assessment of how performant your pages are.

The following tools can help you track your FCP based on field data:

PageSpeed Insights combines lab and field data from Lighthouse and CrUX, respectively.

To measure FCP using PageSpeed Insights, you just need to insert the URL you want to analyze in the tool’s search bar.

Except for the Lighthouse lab data that you can see in the ‘Metrics’ section, PageSpeed Insights allows you to see how real users experience the analyzed page both on mobile and desktop devices.

Also, similarly to Lighthouse, PageSpeed Insights provides detailed recommendations on improving your FCP in the ‘Opportunities’ and ‘Diagnostics’ sections.

Chrome User Experience Report (CrUX) represents how real-world Chrome users experience websites on the web.

There are several ways to access the CrUX data for your website:

If you have some experience with using JavaScript, you can use the Paint Timing API to capture FCP in the page load.

However, how the actual FCP metric is calculated and what the API reflects may differ . That’s why, to avoid unnecessary confusion, Google recommends using the web-vitals JavaScript library for measuring FCP.

But remember that the web-vitals library also has its limitations . For example, it’s impossible to measure cross-origin iframes in JavaScript whereas to calculate FCP you need to be able to measure all iframes.

As FCP measures the time it takes for the first element of your page to render and be visible on the screen, the lower your score is, the better, so you provide your website’s visitors with a positive browsing experience.

It means you should aim for an FCP score of 1.8 seconds or less. To be even more precise, Google advises having an FCP score of 1.8 seconds or less for 75% of all your page views.

To ensure you’re hitting this target for most of your users, a good threshold to measure is the 75th percentile of page loads, segmented across mobile and desktop devices.

To get a better understanding of your FCP score, you should follow the thresholds developed by Google.

Each FCP threshold is marked with a different color, making it easier to interpret the score using various tools.

To determine your FCP score, Google compares your page’s results to the real websites’ data from the HTTP Archive .

The First Contentful Paint (FCP) score may be negatively affected by various factors contributing to how fast your resources can be loaded and rendered at the beginning of page load.

However, among the most common causes of the high FCP score, you can find:

Although understanding what aspects may contribute to poor FCP is essential, remember that analyzing your FCP score and identifying the potential causes of your issues is half the battle.

Why? Because only an in-depth diagnosis of your problems can help you efficiently optimize your FCP for better load speed and user experience.

To begin with, you may use the specific FCP recommendations included in the Lighthouse performance audit in the ‘Opportunities’ and ‘Diagnostics’ sections.

On the other hand, you may also want to know what aspects don’t need to be further optimized for a better FCP score. You can find this information in Lighthouse’s ‘Passed audits’ section.

But in general, according to Google’s official documentation , there are several ways of improving FCP for any website. Let’s dive in.

As you can see, there are numerous officially recommended ways by Google to optimize a poor FCP score.

However, as every website is unique, only an expert analysis of your specific performance issues may let you get to the real cause of your problems and improve your FCP score.

That’s why, if you don’t want to go through the optimization process by yourself, we can handle it for you.
