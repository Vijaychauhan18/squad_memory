---
source: https://www.onely.com/blog/what-is-first-input-delay/
title: First Input Delay: A Complete Guide to Optimizing FID
scraped: 2026-03-23
published_on: 2022-09-03
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

# First Input Delay: A Complete Guide to Optimizing FID

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/what-is-first-input-delay/
Published: 2022-09-03
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Not satisfied with your FID score? See what's FID exactly is, what causes poor FID score and how to fix it for good!

## Extracted Body
First Input Delay (FID) , a Core Web Vital metric, measures the delay between the first user interaction with the page and the moment the browser can start processing that interaction. It’s a key indicator of loading speed, influencing Google’s ranking criteria. Starting in March 2024 , FID will transition to INP, a more comprehensive metric.

2. Break up long tasks into smaller asynchronous chunks under 50ms.

3. Implement code splitting to lazily load non-critical JavaScript on-demand

4. Use web workers to run JavaScript tasks on separate background threads

5. Optimize server response times for API calls and database queries

First Input Delay is a real-user web performance metric that tracks the time between the moment a user first interacts with a web page after entering it to when the browser can start processing that interaction (when the browser’s main thread is idle).

The time between these two events is called input delay (also known as input latency.)

In other words, FID reflects the latency between the user interaction (when you click or tap on something like a link or a button) and the time the browser responds to your action and starts processing it.

Imagine visiting an online store and expecting a given element to open on the spot. However, the hyperlink you clicked on might not respond immediately. Technically speaking, this is because the browser’s primary thread is processing a different request.

The events that count as user input measured by FID must be discrete (finite). Continuous types of user interaction, like zooming or scrolling the page, can’t be accurately measured using this metric. This is because they often don’t run on the browser’s main thread and have different constraints.

FID is about first impressions, making it a user experience metric. The first time a user interacts with your page is fundamental in their experience and perception of your web performance.

Furthermore, most of the blocking of the browser’s main thread occurs in the first moments of a web page’s life cycle – that’s when critical resources are loaded. FID is a metric that helps you address that and ensure that loading those critical resources doesn’t make your website feel clunky and irresponsive.

The actual processing or updating of the web page as a consequence of that interaction is not measured by FID. That’s because it would be easy for developers to game FID by separating the event handler from the task associated with the event.

Input delay occurs when page elements, like images or scripts, are loaded without a user request.

According to Google , one of the reasons behind long input delays is JavaScript execution. In particular, it applies to large JavaScript files the browser must execute before running any event listeners.

Why? Because the JavaScript code that is being loaded can change the subsequent actions of the browser.

It can make the website feel unresponsive as the browser waits to determine the next steps, contributing to the long input latency. It feels like the browser is stuck in a traffic jam that can be streamlined by minimizing JavaScript files. It can reduce the time it takes for the browser to register an event.

The First Input Delay score is unique for each visitor to your website. Some visitors may get distracted more easily and stop browsing your page until they can quickly interact with the content.

And while the score differs for an individual’s interaction with the site, also not all visitors’ actions are considered relevant to the score. That’s why Google understands it’s normal for not all visitors to interact with your site within a single visit.

Time to Interactive (TTI) measures the time it takes for a page to be fully interactive, while First Input Delay (FID) tracks user input before the page is fully interactive.

Time to Interactive is registered when there’s valuable content already rendered on the page (measured by First Contentful Paint ), event handlers are registered for most page elements, and user interaction is processed within 50ms.

Meanwhile, First Input Delay can track, for example, when a user clicks on a link that appears before event handlers are registered for most page elements. First Input Delay, unlike Time to Interactive, allows you to capture those early, critical interactions.

In other words, there are plenty of reasons to focus on First Input Delay optimization on your website.

Do you want a deeper understanding of FID, CLS, and LCP? Find out more about them in our ultimate guide to Core Web Vitals .

Studies show that a delay of 100ms is perceived as caused by an associated source. 0.1 seconds is about the limit for having the user feel that the system is reacting instantaneously.

For these reasons, it’s good to try and keep your FID under 100ms.

Here are the thresholds that Google set for FID in PageSpeed Insights:

Keep in mind that the browser still needs to run the task associated with the user input, which FID doesn’t measure. So in some cases, your FID might be under 100ms, but the page may still feel a little irresponsive.

If you’re unsatisfied with your FID score, it usually indicates that you need to improve your JavaScript or CSS usage.

Here’s how you can proceed with your First Input Delay optimization.

When it comes to CSS files, they need to be downloaded and parsed as soon as possible so that the browser can render the layout of the page. Because of that, your options for reducing the impact of CSS on your First Input Delay are limited . However, you can refer to the best practices , such as minifying and compressing your files or removing unused CSS code.

JavaScript tasks are usually the culprit when there’s a long input delay. Blocking the browser’s main thread for extended periods, they don’t let it process user input.

Here’s when you can take advantage of JavaScript SEO services .

Also, below are some strategies you can use to minimize the time the main thread is blocked by the JavaScript execution:

Long tasks block the main thread, not allowing it to process user input. If you break them up into smaller tasks, user input can be processed between them. Try to keep your tasks under 50ms to be safe.

Aim to minimize how much data needs to be post-processed on the client-side. That reduces the amount of work that has to be done by the browser to render a page.

Third-party code, such as tags or analytics, is often responsible for unnecessarily blocking the main thread. While sometimes analytics need to be loaded at the very start to ensure the whole visit is tracked correctly, you’ll likely find third-party code on your page that doesn’t need to be run immediately. Prioritize loading what you believe offers the greatest value to users first.

You can delegate some main thread work to web workers to reduce the workload on the main thread. Web workers allow you to delegate some of your JavaScript code to be run on the worker thread, which means less work for the main thread and less input delay.

Use async or defer so JavaScript is executed only when it’s needed. If you’re using modern JS, configure ES6 modules to load on demand.

Polyfills are needed when a user is using an older browser. Developers use them to build websites with modern JavaScript and still deliver all functionalities to browsers that don’t support some of the modern features.

Make sure that polyfills are not run if they are not needed. Deliver separate bundles using module/nomodule.

Do you want to know more about optimizing your JavaScript code? Start by reading about the foundations for successful JavaScript SEO .

Idle until urgent is a code evaluation strategy conceived by Philip Walton from Google.

This strategy takes elements from the two most popular approaches to code evaluation – eager evaluation and lazy evaluation .

Eager evaluation means all of your code is run right away. This approach results in a page that loads for a long time until it’s fully interactive but then runs smoothly without any hiccups.

Lazy evaluation is the opposite approach – your code is run only when it’s needed. While it has its benefits and might be useful for some websites, lazy evaluation means that you risk having input delay once the code needs to be run.

Idle until urgent takes the best aspects of both approaches to provide a clever way to evaluate your code, so input delay is minimal.

Idle until urgent lets you run your code during idle periods, using the main thread to the fullest extent possible. At the same time, it guarantees that urgently needed code is run immediately.
