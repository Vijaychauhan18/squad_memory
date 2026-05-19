---
source: https://www.onely.com/blog/top-insights-from-chrome-dev-summit-2021/
title: Top Insights from Chrome Dev Summit 2021
scraped: 2026-03-23
published_on: 2021-11-04
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

# Top Insights from Chrome Dev Summit 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/top-insights-from-chrome-dev-summit-2021/
Published: 2021-11-04
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Chrome Dev Summit's 2021 Keynote came with many exciting announcement for anyone involved with web development and SEO, including new performance metrics!

## Extracted Body
Chrome Dev Summit is an annual event where experts from Chrome share the highlights about their latest products and their vision for the future of Chrome and the web.

This article contains the top insights from the Chrome Dev Summit 2021.

The most interesting changes announced by the Chrome team include:

Privacy Sandbox continues to be one of the key elements of Google’s growing effort to create a more privacy-focused web.

The browser has no way to tell whether you’re using third-party cookies for something helpful like providing a customized experience or keeping a user logged in, or for cross-site tracking. source: Barb Smith

That’s why Chrome aims to create purpose-built APIs that allow you to preserve functionalities (like advertising, fraud detection, or delivering customized content) without the need for third-party cookies.

After ensuring developers have time to adopt the APIs, Chrome will safely phase out support for third-party cookies.

The new technologies and their stages of development can be seen on Privacy Sandbox Timeline.

One of the new solutions launched this year is User-Agent Client Hints (UA-CH).

The User-Agent string contains a lot of information about the user’s device and browser, which can be used for browser fingerprinting.

Chrome aims to fight browser fingerprinting by reducing the default amount of information in the User-Agent string and making it harder to identify the individual users. The information in the string will only contain:

The User-Agent string will give you some information by default, which may cover most of your use cases, but more detailed information is available only on request in a straightforward format. source: Chrome Developers

Starting April 2022, Chrome will gradually reduce the User-Agent strings.

You’ll still be able to get additional data about your users using the User-Agent Client Hints API, but users will be able to decide how much information they are willing to share.

Chrome announced some exciting changes and new features to measure and analyze web performance. It includes:

There’s been an update in the PageSpeed Insights UI making it more intuitive and improving the presentation of data.

The new interface includes a clear distinction between “Lab Data” based on the Lighthouse report and “Field Data” based on real user experiences.

Additionally, a new feature called “Expand View” adds a function to the Field Data section. You can use it to see granular details for Core Web Vitals.

Google also moved the Origin Summary below Field Data. After clicking on it, you can see the aggregated score of all pages from the same origin.

Below the field and lab data sections, you can find additional, helpful information, including:

The changes are also coming to the Core Web Vitals assessment. Instead of a single “passed” or “failed” word, it will be available in a separate subsection.

Lastly, the image of the loading page will be removed from the field section. You will find the image and thumbnails displaying the loading sequence in the lab data section.

The new Lighthouse API allows you to analyze the user flow by simulating link clicks, scrolling, and loading additional pages instead of analyzing the performance of each page separately.

Lighthouse will be able to distinguish and provide separate reports for page navigation, any user interactions that occurred during a given time span, and snapshots to represent a captured state of a page. source: Houssein Djirdeh

With the new feature, you can better understand the user experience and spot the performance issues throughout the user’s journey on your website.

The support for analyzing the user flows has also been added directly in the DevTools.

With a newly launched Record Panel in the DevTools , you can now analyze, record, and export the entire user journey on your website.

The new tool lets you view all of the actions users perform on your website, like key presses or link clicks, directly in the Performance panel. This feature aims to help you understand and debug complex interactions easily.

Chrome announced two new performance metrics as potential candidates for Core Web Vitals.

Responsiveness is meant to capture the overall responsiveness of a page.

We currently use First Input Delay to measure how responsive a page is during loading. FID is a useful metric because responsiveness is particularly volatile when the browser needs to load many resources and the main thread time is in great demand.

But all FID measures is how soon the browser is ready to process a user request. It doesn’t allow you to measure input latency throughout the lifecycle of a given page.

The Chrome team is still conceptualizing the new Responsiveness metric. You can find out more about the challenges of measuring input latency throughout the page lifecycle here.

Smoothness aims to address measuring “stutters” or “freezes” during animation or scrolling. This new metric aims to better understand how often animation frames are dropped and how much it affects the user.

The proposed Percent Dropped Frames metric would calculate the number of dropped frames and present an average score which is supposed to reflect how smooth the animation is from the user’s perspective.

What matters is: the proportion of time waiting for important updates. We think this matches the natural way users experience the smoothness of web content in practice. So far, we have been using the following as an initial set of metrics :

Responsive Design is no longer only about adjusting your website to work well on mobile phones and desktops. It’s much more, and developers need to provide a customized experience for everyone and include user preferences like dark mode or foldable devices.

The changes to the Responsive Design concern CSS features. Some of the new features include new container queries spec, Scroll Timeline, and Accent Color properties.

One particularly exciting feature is the size-adjust property for typography. You can use size-adjust to adjust the default font to match the web font that’s about to load.

It’s especially important because it can help you prevent Cumulative Layout Shift by reducing the shift caused by your web font loading.

Additionally, Chrome is working on a machine-learning-aided auto-dark algorithm feature. It means that the browser can automatically generate a dark theme, with the possibility to opt out of this functionality.

Visit the Chrome Developers page to learn more about Chrome’s new auto-dark feature and test it out on your device.

Not sure how to interpret the new Core Web Vitals metrics? Access our Web Performance services . We can help you.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
