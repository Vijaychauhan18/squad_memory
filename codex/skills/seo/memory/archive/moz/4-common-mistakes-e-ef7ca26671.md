---
source: https://moz.com/blog/common-ecommerce-javascript-mistakes
title: 4 Common Mistakes E
scraped: 2026-03-23
published_on: 2022-11-28
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# 4 Common Mistakes E

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/common-ecommerce-javascript-mistakes
Published: 2022-11-28
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
By leaving JavaScript unoptimized, you risk your content not getting crawled and indexed by Google. And in the e-commerce industry, that translates to losing significant revenue, because products are impossible to find via search engines. In this article, Justyna demonstrates how to avoid some of…

## Extracted Body
Despite the resources they can invest in web development, large e-commerce websites still struggle with SEO-friendly ways of using JavaScript.

And, even when 98% of all websites use JavaScript , it’s still common that Google has problems indexing pages using JavaScript. While it's okay to use it on your website in general, remember that JavaScript requires extra computing resources to be processed into HTML code understandable by bots.

At the same time, new JavaScript frameworks and technologies are constantly arising. To give your JavaScript pages the best chance of indexing, you'll need to learn how to optimize it for the sake of your website's visibility in the SERPs.

By leaving JavaScript unoptimized, you risk your content not getting crawled and indexed by Google. And in the e-commerce industry, that translates to losing significant revenue, because products are impossible to find via search engines.

It’s likely that your e-commerce website uses dynamic elements that are pleasant for users, such as product carousels or tabbed product descriptions. This JavaScript-generated content very often is not accessible to bots. Googlebot cannot click or scroll, so it may not access all those dynamic elements.

Consider how many of your e-commerce website users visit the site via mobile devices. JavaScript is slower to load so, the longer it takes to load, the worse your website’s performance and user experience becomes. If Google realizes that it takes too long to load JavaScript resources, it may skip them when rendering your website in the future.

Now, let’s look at some top mistakes when using JavaScript for e-commerce, and examples of websites that avoid them.

Crawlers don’t act the same way users do on a website ‒ they can’t scroll or click to see your products. Bots must follow links throughout your website structure to understand and access all your important pages fully. Otherwise, using only JavaScript-based navigation may make bots see products just on the first page of pagination.

Nike.com uses infinite scrolling to load more products on its category pages. And because of that, Nike risks its loaded content not getting indexed.

For the sake of testing, I entered one of their category pages and scrolled down to choose a product triggered by scrolling. Then, I used the “site:” command to check if the URL is indexed in Google. And as you can see on a screenshot below, this URL is impossible to find on Google:

Of course, Google can still reach your products through sitemaps. However, finding your content in any other way than through links makes it harder for Googlebot to understand your site structure and dependencies between the pages.

To make it even more apparent to you, think about all the products that are visible only when you scroll for them on Nike.com. If there’s no link for bots to follow, they will see only 24 products on a given category page. Of course, for the sake of users, Nike can’t serve all of its products on one viewport. But still, there are better ways of optimizing infinite scrolling to be both comfortable for users and accessible for bots.

Unlike Nike, Douglas.de uses a more SEO-friendly way of serving its content on category pages.

They provide bots with page navigation based on <a href> links to enable crawling and indexing of the next paginated pages. As you can see in the source code below, there’s a link to the second page of pagination included:

Moreover, the paginated navigation may be even more user-friendly than infinite scrolling. The numbered list of category pages may be easier to follow and navigate, especially on large e-commerce websites. Just think how long the viewport would be on Douglas.de if they used infinite scrolling on the page below:

Product carousels with related items are one of the essential e-commerce website features, and they are equally important from both the user and business perspectives. Using them can help businesses increase their revenue as they serve related products that users may be potentially interested in. But if those sections over-rely on JavaScript, they may lead to crawling and indexing issues.

I analyzed one of Otto.de’s product pages to identify if it includes JavaScript-generated elements. I used the What Would JavaScript Do (WWJD) tool that shows screenshots of what a page looks like with JavaScript enabled and disabled.

Test results clearly show that Otto.de relies on JavaScript to serve related and recommended product carousels on its website. And from the screenshot below, it’s clear that those sections are invisible with JavaScript disabled:

How may it affect the website’s indexing? When Googlebot lacks resources to render JavaScript-injected links, the product carousels can’t be found and then indexed.

Let’s check if that’s the case here. Again, I used the “site:” command and typed the title of one of Otto.de’s product carousels:

As you can see, Google couldn’t find that product carousel in its index. And the fact that Google can’t see that element means that accessing additional products will be more complex. Also, if you prevent crawlers from reaching your product carousels, you’ll make it more difficult for them to understand the relationship between your pages .

In the case of Target.com’s product page , I used the Quick JavaScript Switcher extension to disable all JavaScript-generated elements. I paid particular attention to the “More to consider” and “Similar items” carousels and how they look with JavaScript enabled and disabled.

As shown below, disabling JavaScript changed the way the product carousels look for users. But has anything changed from the bots' perspective?

To find out, check what the HTML version of the page looks like for bots by analyzing the cache version.

To check the cache version of Target.com’s page above, I typed “cache: https://www.target.com/p/9-39-... ”, which is the URL address of the analyzed page. Also, I took a look at the text-only version of the page.

When scrolling, you’ll see that the links to related products can also be found in its cache. If you see them here, it means bots don’t struggle to find them, either.

However, keep in mind that the links to the exact products you can see in the cache may differ from the ones on the live version of the page. It’s normal for the products in the carousels to rotate, so you don’t need to worry about discrepancies in specific links.

But what exactly does Target.com do differently? They take advantage of dynamic rendering. They serve the initial HTML, and the links to products in the carousels as the static HTML bots can process.

However, you must remember that dynamic rendering adds an extra layer of complexity that may quickly get out of hand with a large website. I recently wrote an article about dynamic rendering that’s a must-read if you are considering this solution.

Also, the fact that crawlers can access the product carousels doesn’t guarantee these products will get indexed. However, it will significantly help them flow through the site structure and understand the dependencies between your pages.

Blocking JavaScript for crawlers in robots.txt by mistake may lead to severe indexing issues. I f Google can’t access and process your important resources, how is it supposed to index your content?

It’s impossible to fully evaluate a website without a proper site crawl. But looking at its robots.txt file can already allow you to identify any critical content that’s blocked.

This is the case with the robots.txt file of Jdl-brakes.com . As you can see below, they block the /js/ path with the Disallow directive. It makes all internally hosted JavaScript files (or at least the important ones) invisible to all search engine bots.

This disallow directive misuse may result in rendering problems on your entire website.

To check if it applies in this case, I used Google’s Mobile-Friendly Test . This tool can help you navigate rendering issues by giving you insight into the rendered source code and the screenshot of a rendered page on mobile.

I headed to the “More info” section to check if any page resources couldn’t be loaded. Using the example of one of the product pages on Jdl-brakes.com , you may see it needs a specific JavaScript file to get fully rendered. Unfortunately, it can’t happen because the whole /js/ folder is blocked in its robots.txt.

But let’s find out if those rendering problems affected the website’s indexing. I used the “site:” command to check if the main content (product description) of the analyzed page is indexed on Google. As you can see, no results were found :

This is an interesting case where Google could reach the website's main content but didn’t index it. Why? Because Jdl-brakes.com blocks its JavaScript, Google can’t properly see the layout of the page. And even though crawlers can access the main content, it’s impossible for them to understand where that content belongs in the page’s layout.

Let’s take a look at the Screenshot tab in the Mobile-Friendly Test . This is how crawlers see the page’s layout when Jdl-brakes.com blocks their access to CSS and JavaScript resources. It looks pretty different from what you can see in your browser, right?

The layout is essential for Google to understand the context of your page. If you’d like to know more about this crossroads of web technology and layout, I highly recommend looking into a new field of technical SEO called rendering SEO .

Lidl.de proves that a well-organized robots.txt file can help you control your website’s crawling. The crucial thing is to use the disallow directive consciously.

Although Lidl.de blocks a single JavaScript file with the Disallow directive /cc.js*, it seems it doesn’t affect the website’s rendering process. The important thing to note here is that they block only a single JavaScript file that doesn’t influence other URL paths on a website. As a result, all other JavaScript and CSS resources they use should remain accessible to crawlers.

Having a large e-commerce website, you may easily lose track of all the added directives. Always include as many path fragments of a URL you want to block from crawling as possible. It will help you avoid blocking some crucial pages by mistake.

If you use unoptimized JavaScript to serve the main content on your website, such as product descriptions, you block crawlers from seeing the most important information on your pages. As a result, your potential customers looking for specific details about your products may not find such content on Google.

Using the Quick JavaScript Switcher extension, you can easily disable all JavaScript-generated elements on a page. That’s what I did in the case of one of Walmart.com’s product pages :

As you can see above, the product description section disappeared with JavaScript disabled. I decided to use the “site:” command to check if Google could index this content. I copied the fragment of the product description I saw on the page with JavaScript enabled. However, Google didn’t show the exact product page I was looking for.

Will users get obsessed with finding that particular product via Walmart.com? They may, but they can also head to any other store selling this item instead.

The example of Walmart.com proves that main content depending on JavaScript to load makes it more difficult for crawlers to find and display your valuable information. However, it doesn’t necessarily mean they should eliminate all JavaScript-generated elements on their website.
