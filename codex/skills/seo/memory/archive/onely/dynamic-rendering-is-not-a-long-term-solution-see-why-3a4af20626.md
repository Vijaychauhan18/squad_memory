---
source: https://www.onely.com/blog/why-dynamic-rendering-is-not-a-long-term-solution/
title: Dynamic Rendering Is Not a Long-Term Solution - See Why
scraped: 2026-03-23
published_on: 2022-08-29
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

# Dynamic Rendering Is Not a Long-Term Solution - See Why

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/why-dynamic-rendering-is-not-a-long-term-solution/
Published: 2022-08-29
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Why long-term relying on dynamic rendering is actually hurting your site and SEO? See 4 main reasons and recommendations prepared by specialists at Onely!

## Extracted Body
Although the official Google documentation sheds light on how we should treat dynamic rendering now, the question that bothers many remains: why exactly should we consider dynamic rendering a temporary solution?

If this question triggers you to look for the answer like me, let’s dig in!

To understand why we consider this update vital, let’s travel back to see how Google previously treated (dynamic) rendering.

It all started in 2009 when Google realized that almost 70% of all the websites Google knew about already used JavaScript. But the problem was that at that time, they weren’t able to render JavaScript at all.

To ensure crawling and indexing JavaScript, Google suggested serving a static HTML version of a website to bots when serving a fully-featured JavaScript-based website to users. It was the very beginning of today’s dynamic rendering as a workaround in cases when Google couldn’t deal with a client-side rendered website.

In 2014, Google officially admitted that they started rendering JavaScript-based websites , to update in 2015 that they are generally able to render JavaScript . However, many websites still struggled with correctly rendering and indexing their JavaScript content.

That’s why Bartosz Góralewicz, CEO of Onely, started researching the topic and experimenting to find out if Google can properly crawl and index JavaScript frameworks . It was also the beginning of Onely providing JavaScript SEO services to its clients.

Whereas, from Google’s side, more precise information on dynamic rendering showed up in 2018. During the Google I/O conference , Googlers admitted that they use two waves of indexing. It outlined that, in general, the rendering of JavaScript-based websites is deferred as long as Google doesn’t have the resources to process that content. Also, shortly after the conference, Google published its official documentation (now updated), recommending dynamic rendering to get your JavaScipt content indexed faster.

Then, in 2019, Bartosz Goralewicz elaborated on dynamic rendering during his presentation at SMX WEST . He aimed to explain why this solution isn’t a silver bullet to all rendering issues.

And although we, at Onely, already knew by then that dynamic rendering isn’t the best solution, Google still recommended it as a workaround to processing JavaScript by crawlers so that webmasters kept using it. But unfortunately, they often didn’t realize how expensive it is to host.

Dynamic rendering (also known as prerendering) consists of serving a fully-featured JavaScript version of your website to users and a static HTML version to crawlers to present your JavaScript content. It works by detecting and distinguishing different user agents and serving suitable website versions to users and bots.

However, it doesn’t necessarily mean users have to be served entirely client-side rendered content; they just aren’t served the same static files as bots. In general terms, the whole JavaScript experience is served to users and the HTML files ‒ to robots.

We call it dynamic because your site dynamically detects whether or not the request there is a search engine crawler, like Googlebot, and only then sends the server-side rendered content directly to the client. You can include other web services here, as well, that can’t deal with rendering. For example, maybe social media services, chat services, anything that tries to extract structured information from your pages. And for all other requesters, so your normal users, you would serve your normal hybrid or client-side rendered code. source: John Muller

As the rendering stage, in general, is expensive to be processed by crawlers, dynamic rendering serves Googlebot an easily understandable, lightweight, static HTML version to make your content ready for possible indexing faster.

That’s why Google suggests dynamic rendering can be a trade-off mainly for websites:

Rendering is a crucial step of the indexing pipeline ‒ how your website gets rendered affects how search engines see your content. And to address the needs of both bots and users, you need to learn about two different approaches: server-side and client-side rendering.

Understanding them is crucial as those concepts also recur in different ways of serving JavaScript that you may choose, such as dynamic rendering.

Client-side rendering is based on processing content directly in the browser using JavaScript. At first, browsers and crawlers get initial HTML (which usually represents blank pages with little or no content). Then, JavaScript is asynchronously downloaded and run from the server displaying your dynamic content to users.

However, taking this approach, you risk your content not getting rendered by Google as it may struggle to process the JavaScript-based version of a website independently due to its limited resources. Keep in mind that client-side rendering on its own is not a problem and Google can deal with it, but unless it’s well optimized, it’s very expensive for Google to crawl, render, and index.

With server-side rendering, bots and users receive your website’s HTML version fully rendered on the server immediately, at the request time. The fact that rendering HTML is handled on the server makes the whole process faster for browsers and generally easier for search engines to pick up the content.

Also, although server-side rendering is a recommended solution, Google underlines that choosing it doesn’t influence your rankings ‒ it only differs from dynamic rendering in terms of setup and maintenance:

There are no SEO ranking bonuses for implementing it one way or another – they’re just different ways of making the content indexable (as is client-side rendering). The differences between dynamic rendering and server-side rendering from my POV are more in terms of practical infrastructure setup & maintenance (it can also affect speed, depending on how you have things set up). source: John Muller

Also, take a look at our ultimate guide to JavaScript SEO to learn more about the different solutions for serving JavaScript on your website.

Dynamic rendering may use an external renderer to facilitate changing initial HTML and JavaScript into the static HTML that crawlers can process.

Having configured any of the recommended solutions, remember to:

Regarding implementing dynamic rendering, Google provides its official documentation on implementing and verifying dynamic rendering configuration.

Google can’t fully index a JavaScript-based website until it gets fully rendered. So if dynamic rendering fails, your content won’t be included in SERPs.

And just take popular US-based eCommerce websites as an example: 80% use JavaScript to generate main content and links to similar products . It poses a severe threat to the indexability of the critical parts of those domains. Now, think about how it translates to their revenue going down.

That’s why the crucial step of implementing dynamic rendering is to navigate and verify the potential problems.

The tool allows you to ensure your website’s mobile friendliness and to see the rendered source code of the tested website, along with a screenshot of how Googlebot renders your page on mobile devices.

You may observe some parts of your content missing in the source code ‒ that’s a signal for you that Googlebot wasn’t able to render those resources, and this may be the result of improperly implemented dynamic rendering.

Within the tool, you can dive into the Details section to learn when and by what crawler the page was crawled or even check the HTTP response. If you’re checking your domain, the Mobile-Friendly Test can transfer you into further analysis in Google Search Console.

If you happen to find any issues using the Mobile-Friendly Test, read the article on our blog to learn how to optimize your website for mobile devices.

One of the reports you need to check to make sure you properly implemented dynamic rendering is the Index Coverage (Page indexing) report. It helps you navigate your indexing issues and informs you about which of your pages aren’t indexed and why.

An example of a status that can suggest rendering issues on your website is the “Page indexed without content” status ‒ Googlebot couldn’t see the content because it couldn’t render the page.

Another helpful feature within Google Search Console is the URL Inspection tool . Similar to the Mobile-Friendly Test, the URL Inspection tool allows you to check the status of a tested page and see its rendered version.

As indexing issues may stem from rendering problems, it’s worth analyzing how your website is indexed. You should look at both the number of indexed pages and whether specific sections of those pages get indexed.

To check if a particular fragment of your page is indexed, you can use the site: command together with a text fragment in quotes. But when you have a large website with millions of URLs to analyze, you won’t be able to check them all manually.

ZipTie.dev analyzes indexing together with other data points like word count, titles, headers, meta descriptions, and more. This will help you identify the potential causes of your indexing (and so rendering) problems.

If you use structured data on your website and care about your rich results, use the Rich Results test to check if the markup is correctly implemented.

The test also shows you the rendered version of your website and outlines how Googlebot understands your markup specifying any errors, their types, and where they appear in the code.

However, just checking off the boxes on the list “How to troubleshoot the dynamic rendering issues” may usually not be enough. The larger and more complex the website, the more difficult it may be to specify what exactly went wrong at first glance.

For example, the error results from the Mobile-Friendly Test may suggest that you have some rendering issues. But, at the same time, the server may have just experienced a temporary glitch and didn’t effectively respond with other resources, such as CSS files. As a result, it influences how the website is displayed, but it may only be a one-time situation.

Troubleshooting (dynamic) rendering will always require general technical SEO auditing and thorough analysis.

Dynamic rendering may significantly slow down your server. A large amount of prerendering requests can make the renderer fail, so as a result, Googlebot will:

Therefore, before you decide on dynamic rendering, it is essential to make a deliberate decision if your website needs it.

Implementation and maintenance of dynamic rendering can use a significant amount of server resources. And if you see Googlebot is able to index your pages properly, then if you’re not making critical, high-frequency changes to your site, maybe you don’t need to actually implement anything special. […] source: John Muller

Using dynamic rendering, you maintain two versions of your website. It means you need to verify separately that your website is well-optimized for users and for bots.
