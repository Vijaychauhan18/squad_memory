---
source: https://www.onely.com/blog/time-to-interactive-tti/
title: Time to Interactive
scraped: 2026-03-23
published_on: 2023-02-24
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

# Time to Interactive

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/time-to-interactive-tti/
Published: 2023-02-24
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
TTI is a vital metric that measures page interactivity. By monitoring it, you can optimize website speed and responsiveness.

## Extracted Body
Web performance is a crucial factor in determining the success of any website. Slow-loading pages, unresponsive interfaces, and other performance issues can significantly impact user experience, leading to decreased engagement, higher bounce rates, and lost revenue.

To start taking back control over your website performance , you need to monitor it using the appropriate metrics. TTI, which stands for Time To Interactive, is one such metric that tells you how long it takes for your page to be fully interactive for your users.

Time To Interactive (TTI) is a performance metric used to evaluate how long it takes for a page to become fully interactive to the user.

It’s vital to understand that TTI doesn’t just measure the load time of your page; it goes beyond that. TTI focuses on interactivity.

Load time and interactivity are different but related aspects of web performance. Load time describes the time it takes to load a website’s content. In contrast, interactivity describes the time it takes for a website to become responsive.

It may sound like comparing two synonyms, but the difference is quite vital.

Imagine getting up early on Monday morning. You woke up with the alarm, yawned, and there was nothing more to load before starting your day. It doesn’t mean, however, that you’re ready for the call from your boss. You’re going to need some coffee to become fully responsive.

TTI is a user-centric metric focused on assessing web performance from the practical perspective of your potential customer.

To keep users on a website, four essential moments must happen in quick succession during page loading.

You can think of TTI as a way to check how long it takes your website to provide users with a truly satisfying experience in terms of perceived speed. By controlling that time, you can lower your bounce rate and leave a good impression on your users.

The short answer is no. Core Web Vitals are a set of three metrics that measure different aspects of user experience. Largest Contentful Paint measures perceived load speed, First Input Delay measures responsiveness, and Cumulative Layout Shift measures visual stability. These three metrics are considered essential for evaluating a website’s user experience.

Other web vital metrics aren’t considered “core” but provide additional information about your website’s speed.

TTI may not be a candidate Core Web Vitals metric and may not impact your rankings on Google. But it’s still worthwhile to use this metric. A good TTI score can lead to a lower CLS, and TTI remains a relevant measure of how users perceive your website early in the visit.

TTI is measured in seconds , and calculating it for your page requires identifying the First Contentful Paint and a first 5-second quiet window. In this window, the browser should not process any tasks on the main thread that take more than 50 milliseconds and should not wait for more than two server response requests.

TTI is a point in time between FCP and the quiet window which occurs just as the final long task before the quiet window is completed.

I know that it may seem complicated, so let me explain it in simpler terms. I’ll start by defining what FCP is and then show you how your page loads using a timeline visualization.

First Contentful Paint is a metric that designates the first point in the page load timeline when the user can view anything on the screen. A swift FCP helps to give the user a sense that the page is loading properly.

It’s important not to confuse FCP with LCP (Largest Contentful Paint). LCP is a performance metric that determines when the largest element on a web page becomes visible in the user’s browser.

LCP is always ready before your page is fully interactive, but it doesn’t affect the calculation of the TTI metric.

Imagine the timeline of your page’s loading process. The user browser executes many scripts. Some of those tasks take longer than 50 milliseconds and are relevant for measuring TTI. The browser also asynchronously sends resource requests to your server, and each of the requests stays “open” until it gets its response.

There is a moment when the browser can take a break that we call a “quiet window.” It’s the first time that, for at least five seconds, it doesn’t have to perform any long task on the main thread, and it has no more than 2 resource requests open.

You can be certain that FCP will always occur prior to the quiet window. FCP and the commencement of the quiet window define the time frame within which you can identify your TTI.

Focusing just on that time scope, you should look for a moment when the browser finishes the last long task before the quiet window.

If FCP wasn’t followed by any task longer than 50ms, your TTI equals your FCP.

It can be confusing to tell apart the calculation of Time to Interactive and the measurement of First Input Delay.

Remember that First Input Delay measures the time it takes for a web page to respond to user interaction between First Contentful Paint and Time to Interactive. This way, it’s different from TTI, which measures the time until the page is fully interactive and not how long it takes for the page to react to a user action.

Your goal should be a Time to Interactive of under 5 seconds to ensure a satisfying user experience. This is a good TTI score according to Lighthouse.

For a long time, the best way to measure TTI was to run a Lighthouse performance audit on your site.

However, currently, Google is changing its Lighthouse 10 tool by removing TTI and giving its score weight to CLS (Cumulative Layout Shift). CLS will now account for 25% of the overall performance score, and TTI will constitute 10% of that quarter.

Google’s PageSpeed Insights retrieves its data from Lighthouse, so it’s possible that we’ll witness similar changes to its working in the future. However, as of the writing of this article, measuring TTI using PageSpeed Insights is possible and incredibly easy.

All it takes is copying and pasting the URL address of a page you’re interested in testing and clicking “Analyze.”

As you can see, you can compare how your page is doing on mobile and desktop devices.

Your TTI score will be displayed in the “Diagnose performance issues” section. You may need to scroll down to see it after the report is ready.

If you want to see the Time to Interactive (TTI) score, you need to press the “Plot Full Results” button as it is not shown on the first results screen.

Slow TTI is primarily caused by the massive amounts of JavaScript used commonly used by modern websites. Long JavaScript tasks, those taking more than 50ms, can delay TTI by taking up a considerable amount of time on the main thread.

Since browsers depend on the main thread to complete various tasks, long tasks can make the page unresponsive until the task is done.

As soon as a user lands on a website, their browser begins downloading and executing JavaScript code. However, if this code is unoptimized and results in long tasks, it can cause delays in TTI.

Long tasks prevent the browser’s main thread from carrying out other crucial tasks, such as page rendering or responding to user actions.

In SEO, it’s commonly understood that while JavaScript can enhance a website’s visual appeal and interactivity, it can also negatively impact web performance. Specifically, when JavaScript code is the render-blocking resource, it can significantly slow down page loading times and create significant processing demands for browsers.

To enhance your TTI, there are two key factors at play – optimizing JavaScript code and reducing server response time.

It can be overwhelming to battle those optimization challenges on your own, so don’t hesitate to check Onely’s JavaScript SEO services or learn more about web performce services provided by our experts.

You can help your WordPress site achieve a better TTI score by usingplugins. Start by trying tools from the following list:

TTI stands for Time To Interactive. It’s a website performance metric that measures the time it takes for a website to become fully interactive for users.

As a web page loads, the browser executes scripts and sends resource requests to the server. The “quiet window” occurs when the browser can take a break for at least five seconds without executing any long tasks or having more than two resource requests open. To identify TTI, you need to focus on the time between FCP and the start of the quiet window and observe when the browser finishes the last long task before the quiet window.

Google’s Lighthouse 10 tool removed TTI and focused on CLS (Cumulative Layout Shift) instead, but measuring and optimizing your TTI can still improve user experience.

To improve TTI, optimizing JavaScript code and reducing server response time are key. Your goal should be achieving a TTI score under 5 seconds.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
