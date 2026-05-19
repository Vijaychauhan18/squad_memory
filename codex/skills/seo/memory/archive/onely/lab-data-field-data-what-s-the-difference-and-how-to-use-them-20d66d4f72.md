---
source: https://www.onely.com/blog/measuring-web-performance-lab-vs-field-data/
title: Lab Data & Field Data: what's the difference and how to use them
scraped: 2026-03-23
published_on: 2021-02-11
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

# Lab Data & Field Data: what's the difference and how to use them

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/measuring-web-performance-lab-vs-field-data/
Published: 2021-02-11
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Find out the differences between Lab and Field data to measure web performance properly! But first, you need to know what to measure and why.

## Extracted Body
You may already be familiar with Google’s tools like PageSpeed Insights, Lighthouse, or the CrUX Dashboard in Google Looker Studio (Data Studio). Or maybe you’re still looking for a solution.

To make the right choice, you should first know what you want to measure and why.

While most of these tools use similar metrics, they often rely on different data sources. And the essential distinction you need to make is between lab data and field data in web performance.

In this article, I’ll go through the differences between lab and field data to help you make the right choice.

This is because the quality of data you use to optimize your website’s performance will determine how successful you are.

The concept of lab and field data wasn’t invented to measure web performance. It’s been used in various scientific tests to distinguish between the experiments conducted in a laboratory and those conducted outside of it.

Lab data is collected in a controlled environment and uses predefined device and network specifications. This process is called synthetic monitoring.

So, when you measure your web performance with lab tools, they load your website using a predetermined device and connection speed and measure how performant it is.

When it comes to measuring web performance, lab data is useful in reproducing and debugging possible performance issues. While it doesn’t give you insight into your users’ experience, it’s viable if you don’t have access to real-user measurements.

Field data reflects the browsing experience of real users who use your website. It is affected by the connection and device they’re using while browsing. Field data often unearths the issues that are hard to capture in a lab environment.

Field data is also known as real user monitoring (RUM), real user metrics, real user measurement, or end-user experience monitoring. Google usually uses the term field data.

It’s normal for lab and field data to show different values for the same metrics. T hey simply measure web performance based on various sources.

This is how Google’s Martin Splitt described the difference between lab and field data during a Google JavaScript SEO Office Hours on June 10th, 2020:

Field data is coming from real users, whereas lab data comes from a quite strong machine with probably good internet from somewhere around the world. So you might not see the same results.

That’s why when for lab data you may see, e.g., one simulated device and network connection, field data is based on the distribution of how all users experience your website. It means that there may be users browsing your website on different devices and both fast and slow Internet connection speed, and field data reflects all that.

In other words, with lab data based on predefined settings and field data focused on how real users interact with your website, it’s completely normal that you may see some discrepancies in the metrics.

But I understand it might be confusing, especially when lab data shows nothing to improve and the field data indicates the opposite.

Here is our short summary of characteristics unique to field vs. lab data that you may find useful to understand the difference between them:

However, lab and field data don’t only come from different sources. You may also collect them using different tools.

So now, let’s get practical and learn how to collect web performance data.

One method of collecting web performance data is to use the relevant JavaScript libraries. By setting up tracking on your own, you get more freedom to precisely choose what you’re trying to measure, and you can send the aggregated results straight to your analytics tool.

However, setting up your own tracking is time-consuming and requires you to have advanced knowledge of JavaScript.

Various third-party services offer to measure your web performance, but most of them also require you to implement code on your end, and they tend to be expensive.

So my recommended method is to use the free tools created by Google.

Tools like Lighthouse and PageSpeed Insights run a quick lab test of your page. They’re easy to use and are convenient when you need a brief overview of your lab performance.

When it comes to field data, Google collects it from Chrome users and stores it in the Chrome User Experience Report (CrUX).

The data from the CrUX report is accessible through several tools and APIs, which you can choose depending on your specific needs.

While it’s important to note that CrUX doesn’t give you information about your users on other browsers, I still think CrUX is the ultimate source of web performance data. If you know that many people access your website on different browsers, you may implement additional tracking methods afterward, but CrUX is the best place to start.

Moreover, CrUX contains the same data that Google uses to rank websites after the Page Experience update went live in 2021. Since then, Core Web Vitals became a part of the ranking algorithm, and these three metrics (LCP, CLS, and FID) now influence your rankings.

Want to optimize your FID, LCP, and CLS for better rankings?

Reach out to us for Web Performance services to drive more organic traffic to your website.

To sum up, using Google’s tools allows you to get a mix of lab and field data that you need to get a thorough understanding of your web performance .

Field data gathered by Google can be accessed via Chrome User Experience Report (also known as CrUX). The report’s data is aggregated from Google Chrome users who have opted-in to syncing their browsing history, have not set up a Sync passphrase, and have usage statistic reporting enabled.

The list of web performance metrics you can collect from CrUX is impressive:

In December 2020, the CrUX database included over 8M origins , and it continues to grow.

We hope to add more metrics and dimensions, both to provide more insight into loading and other critical factors that most affect user experience.

Based on that, we can expect more metrics to be added to CrUX in the future.

If you’re just starting, using the Search Console, Google Looker Studio, or PageSpeed Insights is the way to go – these tools are easy to use, although they only give you a sneak peek into what CrUX can offer.

By using Google BigQuery or one of the APIs, you can access more metrics and look at your performance in specific countries, on particular devices, and connection types.

Lab data is artificially collected in the test environment. It doesn’t come from real users but is simulated on a single device with a predefined location and network connection.

The examples of metrics that you can exclusively measure in the lab are Total Blocking Time and Time To Interactive .

If you want to know how real users are experiencing your website, field data is the right choice.

Field data is probably a better indicator for how real users are experiencing your website than lab data. Because lab data is literally just someone’s server making a request to your thing. And then if that server happens to be quite beefy then you get pretty good-looking numbers, but then the real world isn’t as beefy and nice.

So, field data is what you should be monitoring to know if your website’s users around the world have a positive browsing experience.

For search rankings, we use field data, as this is what your site’s users have experienced over time. This makes the data more representative for your site, taking into account where your users are located and how they access your website.

However, if you are in the process of actively optimizing your site, you have no choice but to rely on lab data – it allows you to evaluate your improvements without having to wait for the real user data to come in.

That being said, there’s no need to decide that one approach is superior and more useful than the other. Your course of action should always depend on why you need the data.

For example, you can use field data to define where your users are, how fast their internet connection is, and what device they use. With this information, you can simulate your user with lab tools when optimizing your pages and verify how much the changes you’re implementing affect the results.
