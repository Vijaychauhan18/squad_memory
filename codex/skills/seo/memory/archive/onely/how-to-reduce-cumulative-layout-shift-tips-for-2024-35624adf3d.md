---
source: https://www.onely.com/blog/cumulative-layout-shift/
title: How To Reduce Cumulative Layout Shift? Tips For 2024
scraped: 2026-03-23
published_on: 2020-11-09
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

# How To Reduce Cumulative Layout Shift? Tips For 2024

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/cumulative-layout-shift/
Published: 2020-11-09
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Your CLS score may have an impact on the traffic you get from Google and other search engines. See our tips to improve your CLS and SEO!

## Extracted Body
High Cumulative Layout Shift scores can result in a frustrating user experience, as well as decreased visibility in search engine rankings.

To provide users with the best possible experience, Google’s ranking factors aren’t focused just on the content or authority of the site but also on its loading speed. Google’s ranking system now includes Core Web Vitals, with CLS as a crucial component, to favor performant pages.

You can lower your CLS by using a consistent layout and sizing for important elements, and ensuring that images and videos have proper aspect ratios.

Cumulative Layout Shift (CLS) is a web performance metric that calculates the visual stability of a given web page. It’s calculated by measuring all layout shift scores during the entire lifespan of a page and choosing the largest group of layout shifts within a single session window.

CLS became a ranking factor in June 2021 when Google’s Page Experience Update started rolling out. That means your CLS score (together with Largest Contentful Paint and First Input Delay metrics) now affects your SEO. While it’s likely to be a minor ranking factor, your CLS score (along with the other Core Web Vitals) may reflect on the traffic you get from Google and other search engines.

Moreover, CLS correlates with user behavior metrics. Bounce rate may not impact Google’s rankings, but controlling it is vital for keeping visitors on your site and preventing them from switching to competitors.

For your users, the negative effects of multiple layout shifts span from mild annoyance to even accidentally purchasing the wrong product. It can result in bad reviews for the company and discourage users from returning to the site, as well as repel new clients.

On the other hand, sites that pay attention to their CLS score can win more of Google’s trust. They are also remembered by users as more modern, elegant, and refraining from distracting customers with intrusive advertisements.

A well-optimized CLS provides users with a stable layout, and it’s easier to engage with a predictable environment. On a website without confusing shifts, the user finds the desired content faster, increasing the chance that they will order your product or service before they lose patience with the site.

CLS score is impacted by every content that lacks a designated space on your page, causing it to load unexpectedly and displace other content, leading to user confusion.

According to Google , the most common causes of high CLS are:

The lower your score, the more stable your layout is. Official CLS thresholds used by Google’s performance measuring tools are as follows:

To receive a “good” CLS threshold, Google recommends that you keep your CLS score under 0.1 for 75% of all page views.

CLS compares two rendered frames to calculate how much the elements of a page have moved and the fraction of the viewport that was affected by the layout shift.

There are two factors that go into CLS: impact fraction and distance fraction.

To calculate the impact fraction, you need to calculate the impact region first.

The impact region defines the area affected by the layout shift. Google compares the original frame with the frame after a layout shift and identifies all affected page elements, thus defining the impact region.

The impact region is usually a rectangle, but if you have multiple layout shifts – both horizontal and vertical – it can be a more complex shape.

To define the impact fraction, you divide the impact region by the area of the viewport (part of the page visible on the screen without scrolling down):

Move distance defines the distance between a given element’s position before and after the layout shift. It pretty much answers the question: how far did the element move?

Once you’ve calculated the move distance, you can calculate the distance fraction by dividing the max move distance by the viewport height:

The next step is to calculate the layout shift scores. Here you multiply the impact fraction by the distance fraction to get the layout shift score for a single animation frame:

impact fraction x distance fraction = layout shift score for a single animation frame

Google’s researchers decided to implement a mechanism for grouping layout shifts in session windows.

Session windows are essentially time frames within the lifecycle of your page, inside of which layout shifts are summarized.

When a layout shift happens on your page, a session window is opened. It can last for a maximum of 5 seconds but will close sooner if no consecutive layout shifts occur within 1 second from the initial shift.

Layout shifts are then summarized within session windows. Your final CLS score for a given page is the score of the session window with the greatest total score – other session windows don’t influence your CLS.

The two initial layout shifts occurred within the same session window, so we added the scores together.

The third layout shift occurred after 2 seconds, so it belongs in a separate session window. The previous session window closed one second after the second layout shift.

So in this scenario, your page’s final CLS score would be 0.1 + 0.2 = 0.3! The third layout shift doesn’t influence the final score.

Before we delve into measuring and enhancing CLS on your site, it’s crucial to have a comprehensive understanding of CLS. That involves understanding three more key points.

CLS ignores all layout shifts that appear within half a second from any user input. It’s called the input exclusion window. This means that CLS measurement stops for 500ms after every user interaction with the site. So, if the layout change is intentional and caused by the user, it won’t affect your CLS.

Usually, layout shifts happen while loading the page – but they can occur later as well and will contribute to your CLS score if they happen outside of the input exclusion window.

Since CLS can be measured both in a lab and during real-user interactions, you can and should look at both your CLS lab score and your CLS Real User Data.

Lab Data means using tools to simulate the user’s experience. It’s exactly like lab testing – almost real, but in a controlled environment, and the results only account for a small range of possible situations.

You can access your CLS lab data via the performance tools mentioned below.

Real User Data is data based on real user interactions. Gathered by Google and other third parties, it allows you to see the bigger picture. You can compare Real User Data with your lab results. For Google, the main source of Real User Data is Chrome User Experience Report, also known as CrUX.

An alternative source of CLS based on Real User Data is the JavaScript API – and if you have some coding experience, there are some fun things to do with it, e.g., measuring CLS by the minute.

Still unsure of dropping us a line? Read how Core Web Vitals services can help you improve your website.

You can identify page elements contributing to your higher CLS score by using the tools we’ve discussed above. The easiest way to do this is by opening the Core Web Vitals report in your Google Search Console.

Click the “Open Report” button to see the list of URLs harming your web performance. CLS is among the three potential issues in the report.

Now, you can investigate each of the revealed URLs running a Lighthouse audit. Chrome DevTools may help you see the shifting element highlighted on your page.

Let’s enhance your website’s user experience and search engine rankings by fixing CLS issues. We’ll cover methods such as optimizing image loading, reserving space, and reducing unexpected layout changes.

It’s more advantageous to take preventive measures than to treat the problem later. CLS issues can be remedied, but let’s first consider some simple techniques for avoiding them altogether.

With lazy loading, you can optimize the loading of your pages and reduce the burden at startup. Yet, the hero image may not be a good candidate for lazy loading, especially if it appears prominently above the fold, as this technique may not be the best solution for such elements.

Animations can cause layout shifts, but not all of them will count toward your CLS score. Google ignores CSS transform changes – so if your animation uses the CSS transform property, it won’t affect your CLS.

A content Delivery Network is a group of geographically dispersed servers that cash content and cooperate to reduce the time it takes to respond to a user request. Slow server response times can lead to layout shifts, so investing in CDN may help you prevent high CLS on your pages.

Hardcoding the header and menu elements can result in a more consistent and stable layout of your page since the position and appearance of the header and menu will always be the same.
