---
source: https://www.oncrawl.com/technical-seo/how-does-a-browser-create-a-web-page/
title: How does a browser create a web page? - Oncrawl
scraped: 2026-03-23
published_on: 2020-03-17
tags: live_feed, phase1_ingest, oncrawl, publication, technical-seo, ai-visibility, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Oncrawl
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How does a browser create a web page? - Oncrawl

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/how-does-a-browser-create-a-web-page/
Published: 2020-03-17
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
As a technical SEO, it is important to understand how a browser creates a web page. This can help, later, to understand the difference between human and search-engine bot interpretations of a page, or to diagnose page speed issues, among other things. I'll be looking at it with an eye to improving page speed.

## Extracted Body
As a technical SEO, it is important to understand how a browser creates a web page. This can help, later, to understand the difference between human and search-engine bot interpretations of a page, or to diagnose page speed issues, among other things. I’ll be looking at it with an eye to improving page speed.

This is the first of this series of 4 articles about the browsers’ phases of creating a page and its reflection on Pagespeed.

In order to display content, each browser must complete the DOM and CSSOM processes before creating the rendering-tree to create a web page.

DOM or Document Object Model is constructed from HTML markup. The DOM is a data representation of the elements that make up the structure and content of the web page. This representation is used by different programs, like JavaScript scripts, that might modify either the structure, the content, or both.

CSSOM is created by CSS MarkUp such as animation, keyframe, media queries along with selectors, properties and values semantically parallel to the DOM.

This is a screenshot from the first web browser of history. It can’t render Javascript and doesn’t have lots of CSS Properties. It can’t use modern HTML Rules also. Experiencing these kinds of primitive web browsers (such as Lynx) can help you to understand browser engines and their natures in terms of web performance. You may visit this page!

No browser sees content or source code on a page as people do. First of all, it will see everything on the preDOM in bytes. It will then convert the bytes to specific characters and solve what they mean to form the page structure as a hierarchy.

Note: preDOM is the version of the DOM that appears in source code and has not yet been read and processed by the browser. The preDOM is then read and interpreted by the browser:

Before I give you a few tips, you’ll need to understand the DOM Load Event types and their meaning.

If you want to only calculate DOM Process Time, you should focus on the domInteractive event. However, this event is not shown in Chrome’s devTools. You may use or consult your IT team for PerformanceNavigationTiming API which can calculate all of these events, as well as additional subEvents such as domContentLoadedEventStart.

You can also look at domInteractive preferences in Google Analytics > Behaviour > Site Speed > Page Timings > DOM. However, the information here is not particularly stable and reliable. Still, it may give you a place to start.

You may also calculate DOM Interactive Timing with DevTools but only with console codes. It is a little bit of a slow method but you may try “performance.timing” code library. Above, you will see at the left side, performance.timing which shows most of the performance metrics. Only the last three or four digits are important here. If you want to see a custom metric, for example DOMInteractive, you can write performance.timing.domInteractive – performance.timing.responseStart. On the right, DOMInteractive, DOMComplete, Total Page Load Time are given respectively. Example is from the same news site.

In this article, the domContentLoaded event and DevTools will be enough for our purposes.

Note that when resources are correctly organized and loaded, domInteractive and domContentLoaded times are not so different from each other. Because the real challenge is separating JS files and CSS files from one another without interrupting HTML parsing or creating a bottleneck in the main thread. If you can do this successfully, it is likely that both the DOM and the CSSOM (domContentLoaded Event) are fired in the fastest way.

If we were in 2019 and before, I might say that as a Technical SEO Expert, you don’t have to know how to code.

But in 2020 and beyond, you actually have to know some beginner level coding. To understand how to optimize a Document Object Model or an HTML Node structure, you need to examine it with enough experience to create a new code structure.

You can use different DOM types for better page speed, UX and crawl budget. One example is Virtual DOM.

Virtual DOM loads only the parts of the DOM that change when a new page is opened, instead of reloading all of the DOM elements. This creates a faster and lighter page presentation for the user or search engine bot.

Virtual DOM works well with the JavaScript libraries Vue or React.

DOM size is directly related to page speed and to the initial contact with the user.

If you have a big DOM size and don’t use Shadow DOM or similar preventive methods to avoid loading and styling all of the HTML nodes that are not visible during the initial page load, you will probably delay your speed index and initial contact speed for user.

If your DOM size is large, you will probably suffer from browser reflow .

Reflow refers to resizing, styling or painting and positioning an HTML Element in the re-rendering process. If an HTML parent element changes, the child elements are also affected. The length and count of this sort of HTML element chains can harm your page speed.

Reflow loops can harm your crawl budget, increase the load on the server and the network. It can consequently affect conversion rate and even rankings.

Google has actually published a nice and brief presentation video on this topic:

Browsers tend to start the CSSOM process after completing the DOM process.

Since modern browsers are aware that the DOM will not make any sense until CSSOM is completed, some HTML elements are not displayed by the browser until it has read the style codes. A good example of this would be the CSS background-image.

Above is an example of a CSS code snippet which needs to be refactored. ‘Zoom’ property is used more than 19 times for different selectors. They can be unified.

You can check CSS properties and their costs to the browser engine via CSS Triggers in terms of different browser engines.

Remember, the CSSOM has a hierarchical tree just like the DOM. It applies the current rules to the largest element first, and the child elements remain affected until the browser reads the code written specifically for them.

In CSSOM, all CSS ID, Class and Properties and Value elements are listed according to the semantic structure of the HTML DOM elements. CSSOM is taken from the same HTML document as the DOM. The main reason I have not indicated HTML nodes in CSSOM is to draw attention to the hierarchical structure of CSS Codes.

Executing the CSSOM is not the same thing as rendering. When the DOM and the CSSOM are read in the same hierarchy, rendering is the process of joining these two code-trees from the top down in the viewport.

During rendering, some code snippets that exist during DOM and CSSOM processing may be disabled. The main reason for this is that they are not visible or are disabled by a different code. Therefore, optimization of code that is not included in the rendering tree but that appears in the DOM and the CSSOM is useful for page speed.

Above, the DOMContentLoaded data in Chrome’s DevTools shows the time it takes to load and parse the HTML and CSS documents.

Therefore, consistency between the performance main thread and call tree sections yield close results. All examples are from the same site.

If you want to calculate only DOM, you need to check domInteractive time, which is not shown by DevTools but can be measured with the Navigation Timing API.

After the DomContentLoaded event, your browser will start the rendering tree and you will see that pixels of your screens are colored with meaningful information and design. During this time, Javascript rendering will also come into play and will instantly split, change, and repaint the rendering tree.

A properly structured resource order, resource request count, and rendering-tree and Javascript rendering relationship reduce cost in terms of page speed.

The next article in this series will look at how this relates to advanced page speed metrics and how Google perceives page speed.
