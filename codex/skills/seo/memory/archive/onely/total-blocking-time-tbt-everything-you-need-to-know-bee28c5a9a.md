---
source: https://www.onely.com/blog/total-blocking-time/
title: Total Blocking Time (TBT) ‒ Everything You Need To Know
scraped: 2026-03-23
published_on: 2023-02-17
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

# Total Blocking Time (TBT) ‒ Everything You Need To Know

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/total-blocking-time/
Published: 2023-02-17
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
TBT measures how long the main thread was blocked between FCP and TTI. Read the article to learn how improve your website’s responsiveness.

## Extracted Body
Total Blocking Time (TBT) is a web performance metric that measures for how long the main thread is blocked from responding to user interaction during the page loading process. TBT is calculated between First Contentful Paint (FCP) and Time To Interactive (TTI) and measured in milliseconds.

Although it may be less recognizable than Core Web Vitals , TBT is still an important metric that correlates to them and, consequently, can indirectly affect your rankings on Google.

Get ready to take notes — here’s everything you need to learn about TBT to improve your website’s responsiveness.

Total Blocking Time (TBT) is a lab metric that calculates the amount of time when the main thread was blocked between First Contentful Paint (FCP) and Time To Interactive (TTI) , lowering a page’s responsiveness.

During a page load, beginning from the moment when the page starts loading, the main thread is responsible for dealing with different tasks like parsing HTML or processing JavaScript files.

However, some tasks take long enough for users to experience a noticeable delay. That’s why any task above 50ms is considered ‘long.’ This might seem like an arbitrary threshold, but it’s based on the RAIL performance model .

When a long task is being processed, the browser simply can’t pause it and respond to a user action, like clicking, that occurred while the long task was ongoing.

On the contrary, the browser must wait for the currently ongoing task to end so it can respond to user interaction.

A part of that task that exceeds the 50ms threshold is considered the blocking time.

If the task in the main thread runs for, e.g., 60ms, the blocking time for the long task would equal 10ms.

TBT is the sum of the main thread’s blocking time for all long tasks.

For the sake of an example, let’s do some math. If you have two long tasks taking 60ms and 80ms, you need to add up the blocking time for both, which is 10ms and 30ms, respectively. The sum of them is 40ms, constituting your TBT.

Total Blocking Time (TBT) and Time To Interactive (TTI) are both lab metrics that measure load responsiveness.

They closely correlate with each other, and when properly used within the optimization process, they may bring significant results to a page’s responsiveness, interactivity, and usability.

TBT is a great companion metric for TTI because it helps quantify the severity of how non-interactive a page is prior it to becoming reliably interactive.

Although they share similar goals, TBT and TTI differ in tracking various aspects of a website’s responsiveness.

TBT calculates how long the main thread was blocked from responding to user interactions, and TTI measures how long it takes for a page to become fully interactive.

To be more precise, TTI measures the time since First Contentful Paint to the moment of a page’s full interactivity when event handlers are registered for most elements, and the page responds to user interaction within 50ms. On the other hand, TBT focuses on blocking time for all long tasks between First Contentful Paint and Time To Interactive.

Another vital difference is that TBT is measured in milliseconds while TTI is in seconds.

Although TBT is not a Core Web Vital metric, TBT closely correlates with one of them — First Input Delay (FID.)

TBT and FID both measure how responsive your page is, meaning they focus on how long it takes for necessary resources to be loaded and executed so that your page’s elements can quickly respond to any user interactions.

TBT and FID also differ in that they measure load responsiveness with lab and field data , respectively.

According to Google’s official documentation , although FID is a field metric, improving it relates to the recommendations for optimizing TBT that can be measured in the lab.

To help predict FID in the lab, we recommend Total Blocking Time (TBT) . They measure different things, but improvements in TBT usually correspond to improvements in FID.

In other words, if you optimize your TBT, you’ll also improve your FID score.

It’s also worth noting that since Core Web Vitals were introduced as part of the Page Experience update in June 2021, FID became an official ranking factor.

It means that improving TBT works as a proxy metric to optimize your FID score and indirectly affect your rankings.

Read our article on optimizing First Input Delay (FID) and learn why it’s important for your website’s SEO and user experience.

TBT doesn’t only relate to FID in theory. Here’s an example of how TBT was optimized for outstanding FID results.

MercadoLibre is a leading e-commerce platform in Latin America. Using Total Blocking Time as a proxy metric , the team at MercadoLibre managed to improve their website’s First Input Delay and overall interactivity.

Since First Input Delay cannot be simulated with a lab test, they used TBT to find long tasks blocking the main thread.

Once they determined which tasks needed shortening, they used techniques such as tree shaking (getting rid of unused yet imported code), deferred hydration , and code splitting (splitting code into smaller files) to reduce the size of the code bundles used on the site.

The result was a 90% reduction in Max Potential FID in Lighthouse and a 9% improvement in FID in Chrome User Experience Report.

As TBT reflects the time it takes for a page to become responsive, the lower your score is, the better, because your users will be able to interact with your content immediately.

To be more precise, you should aim for a TBT score of less than 200ms.

Here’s what the exact thresholds for TBT look like and how you should analyze them in 2023:

An important thing to note is that along with the Google Lighthouse 8.0 update in June 2021 , the Total Blocking Time (TBT) scoring became stricter.

For example, for the Lighthouse 6.0 version, a score of 290ms was still considered good. However, since Lighthouse 8.0, good TBT ends above 200ms.

However, you can expect this metric to be refined as Google regularly researches its metrics and analyzes their impact on web performance . Also, Google engineers believe there’s still room for improvement in the TBT score after the 8.0 version update:

But we think these as our control points would be too jarring and aggressive for now. Still, there’s room to improve, so we’re doing a small shift of TBT being scored more strictly.

If you weren’t aware of these Lighthouse updates, Google introduced a Lighthouse Scoring Calculator where you can check the differences between the current version and previous ones and see how the TBT scores changed over time.

Total Blocking Time (TBT) should be analyzed based on the lab data.

Although, in theory, measuring TBT in the field is possible, you shouldn’t do that.

Why? Because in the case of TBT tested in the field, there may be too many confounding factors to consider. Also, there are better metrics to measure your website’s responsiveness and interactiveness in the field.

While it is possible to measure TBT in the field, it’s not recommended as user interaction can affect your page’s TBT in ways that lead to lots of variance in your reports. To understand a page’s interactivity in the field, you should measure First Input Delay (FID) and Interaction to Next Paint (INP) .

Focusing on that perspective, here are the lab tools to check and analyze your TBT score:

If you’re using Google Chrome as your go-to browser, you can use Chrome DevTools to measure your TBT score and easily identify all long tasks that affect it.

Here’s a step-by-step guide on how to measure TBT in Chrome DevTools :
