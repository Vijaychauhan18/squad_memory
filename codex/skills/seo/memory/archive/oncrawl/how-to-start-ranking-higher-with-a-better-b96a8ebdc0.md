---
source: https://www.oncrawl.com/technical-seo/start-ranking-higher-better-optimized-crawl-budget/
title: How to start ranking higher with a better
scraped: 2026-03-25
published_on: 2018-09-06
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

# How to start ranking higher with a better

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/start-ranking-higher-better-optimized-crawl-budget/
Published: 2018-09-06
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
The way your website is crawled is determined by your crawl budget — the number of times Googlebot visits your site during a certain period of time.

## Extracted Body
There are multiple factors that affect rankings — external links, keyword usage, site speed and many, many more. But when you start optimizing your site, what you need to remember is that for all of your optimization efforts to pay off your site needs to be crawled and indexed.

The way your website is crawled is determined by your crawl budget — the number of times Googlebot visits your site during a certain period of time. And your site’s visibility depends on how well the crawl budget is balanced.

So, to make sure that all the important pages are visited regularly, the crawl budget needs to be optimized. Here’s how you can do it.

To figure out whether your crawl budget needs optimizing, first check if you’re short on it at all. According to Google’s Gary Illyes , only big sites really need to prioritize what to crawl, especially the ones that auto-generate a lot of URLs based on parameters. If you think that your site requires additional crawl budget balancing, here’s how you start.

In Google Search Console, you can find your current site’s crawl statistics and find out the details of your crawl budget.

Avg.number of pages crawled per day x number of days in a month = Approximate crawl budget

For example, from a report below, you can see that on this website Google crawls 371 pages per day.

But to know exactly how often Google crawlers hit your website, you need to check the server logs. Google Search Console shows the aggregated crawl budget for 12 bots, and to see the exact crawl budget distribution you’ll need a log analyzing tool.

The ups and downs in the crawl graph can be a sign of an issue, but that’s not always the case. For example, a spike in the graph above represents a re-submitted sitemap, which is a trigger for a Googlebot to revisit the website.

To optimize your crawl budget, you need to stick to a simple rule:

Make sure that what needs to be crawled is crawled and what doesn’t need to be crawled is not crawled.

That means, that the important pages are getting enough attention and the ones that are not bringing your site any value are left out. Here are the exact steps that will take you there.

Surprisingly, it is very common when important pages have a disavow status in the robots.txt file. This way they are ignored by Googlebot and, thus, are hidden from indexation. Your task is to make sure that the pages you want to be crawled don’t have that status and are accessible to the crawlers.

You can find the robots.txt file in Google Search Console. To make sure that your important pages are not disavowed, just browse the file.

As Google itself says , the crawl rate limit is the maximum fetching rate for a given site. Simply put, it specifies how many parallel connections can a Googlebot create to crawl the site and how long should it wait between the fetches. When the site speed is high and, the limit goes up and Googlebot creates more simultaneous connections. When the site response rate is low or returns server errors, the limit goes down and Googlebot crawls less.

Thus, the way your site is crawled is also affected by the site’s health. This includes site speed, mobile friendliness, the amount of 404 errors, etc.

You can then monitor your crawl frequency using a log files analyzer like Oncrawl and see if the Googlebot has been hitting your pages more often.

These are the pages that have weak or no content, technical pages etc. Since they are indexed and have little impressions, they can be found in the Google Search Console. Another place to spot them is the Oncrawl’s SEO Impact report. For instance, it shows the impact of the word count on the crawl frequency.

For example, a common problem for large e-commerce websites is faceted navigation. Ryan Stewart talks about it in his video about crawl budget optimization (you can jump to 7:20 to check this out, but the whole video is extremely useful as well). When the user selects a category at a website, it’s parameter is added to the page URL. According to Googlebot, from that moment, it is a different URL and requires a separate visit. Since the number of possible category combinations is vast and can significantly overload the crawl budget, such pages need to be filtered out.

A similar issue occurs when a session identifier is placed inside the URLs. Such pages should be filtered out as well.

First of all, these are the pages that already have a lot of traffic; you can spot them in Google Analytics. Under Behavior report, go to Site Content → All Pages and sort the pages by the number of pageviews.

Second, it’s the pages whose positions are improving, which means they are growing in popularity. Such pages can be found in Google Search Console, but with its filtering options limited it might take a while before you spot them.

An alternative would be to use AccuRanker as it allows you to see what kind of pages have a growing visibility trend. To start using it, you can import the list of keywords from Google Search Console in one click and then spot what pages are the most promising ones.

Additionally, there’s a way to spot the pages that can have additional SEO traffic in the following weeks and months. It involves some playing with Google Search Console API and Google Data Studio, but the result is somewhat amazing. By using Landing Pages as dimension and Impression, URL Clicks and URL CTR as metrics you can find the pages that are growing in popularity faster than the others.

When you find out what pages require prioritization, here’s what you can do to make sure that they are crawled more often:

Internal links are crucial for crawling as the main pathway for Googlebot. Without an internal link on a page, it simply can not move forward. So, by adding links leading to a page you increase its chances of being indexed sooner.

For example, if you want an old page to be crawled more often, add a link leading to it, to your new pages. When the Googlebot visits the new page, it will as well re-index the old one.

By adding the page link to the website’s navigation menu you also make it easily accessible by users and by Googlebot. SEMrush uses this technique to speed up the crawling of its new blog posts. All the new articles appear in the Recent Posts section on their main page and, thus, get prioritized by the Googlebot.

This technique can also be used to speed up the indexation of the new product pages on the e-commerce websites.

As said above, crawl budget optimization is more important for bigger sites with a ramified structure such as e-commerce sites. But since proper page crawling is the foundation of SEO and directly affects SERP visibility, you may want to revise your crawl stats and balance the crawl budget to speed up the results of your SEO efforts.
