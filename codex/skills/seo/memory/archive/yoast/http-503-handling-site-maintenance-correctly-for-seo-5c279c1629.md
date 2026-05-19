---
source: https://yoast.com/http-503-site-maintenance-seo/
title: HTTP 503: Handling site maintenance correctly for SEO
scraped: 2026-03-23
published_on: 2021-06-08
tags: live_feed, phase1_ingest, yoast, publication, seo-education, wordpress-seo, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Yoast SEO Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# HTTP 503: Handling site maintenance correctly for SEO

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/http-503-site-maintenance-seo/
Published: 2021-06-08
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
An HTTP 503 header is a very useful tool for site maintenance. This post explains why and gives some pro tips on how to use it!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Sometimes, your site will need some downtime, so you can fix things or update plugins. Most of the time, this tends to be a relatively short period in which Google will most likely not attempt to crawl your website. However, in the case that you need more time to get things fixed, chances are much higher that GoogleBot might come for a visit and be confronted with a website that’s down. So how do we prevent Google from deranking your website?

For those not familiar with HTTP status codes, here’s a brief summary of the ones that apply to you when dealing with site maintenance:

Please note that Google will consider pages returning the 200 HTTP status code, despite there being an error (or very little content) on the page, as a “ soft 404 ” in Google Search Console.

If Google runs into a 404 while crawling your site, it’ll usually toss out that page from the search results until it comes back the next time to verify the page is back. However, if Google repeatedly runs into a 404 on that specific page, it’ll eventually postpone re-crawling which means that more time will pass before the page returns in the search results.

To overcome this potential longer loss of rankings, you need to return a 503 status code whenever working on a particular page. The original definition of the 503 status code, according to this RFC , is:

The server is currently unable to handle the request due to a temporary overloading or maintenance of the server. The implication is that this is a temporary condition which will be alleviated after some delay. If known, the length of the delay MAY be indicated in a Retry-After header. If no Retry-After is given, the client SHOULD handle the response as it would for a 500 response.

What this means is that returning a 503 in combination with a Retry-After header, which will tell Google how many minutes to wait before coming back. This does not mean Google will crawl again in exactly X minutes, but it’ll ensure Google doesn’t come back around to take a look anytime before then.

If you want to implement the header, there are a few options you can choose from.

By default, WordPress already returns a 503 when updating plugins or WordPress core. WordPress allows you to override the default maintenance page by adding a maintenance.php to your wp-content/ directory. Please note that you’ll then be responsible for properly returning the 503 header. Plan on doing database maintenance? You’ll have to take care of that as well. Add a db-error.php file to your wp-content/ and make sure that you also properly return a 503 header here as well.

If you’re looking to add something fancier to your WordPress website, check out WP Maintenance Mode . This plugin also adds a lot of extra features, besides what we mentioned in the previous section.

If you’re just writing your own code and want a solution that’s easy to implement, you can add the following snippet to your codebase and call it in the code that determines if you’re in maintenance mode:

Note that the 3600 in the code snippet dictates the delay time in seconds. That means that the above sample will tell GoogleBot to return after an hour. It’s also possible to add a specific date and time in Retry-After , but you need to be careful with what you add here, as adding a faulty date might result in unexpected results.

There are a few things you need to take into consideration when working with maintenance pages and returning 503 status codes. If you actively use caching, you might run into a situation where the cache isn’t properly passing on the 503 status, so please make sure you test this properly, before actively using this on the live version of your website.

Did you know it’s also possible to return a 503 status code for your robots.txt? Google states in its robots.txt documentation that you can temporarily suspend crawling by throwing a 503 for your robots.xt file. The biggest advantage to this is less server load during maintenance periods.

As we have seen, you can avoid losing rankings by adding a 503 when you’re doing site maintenance, to let Google know it can come back to crawl your site later. There are several ways to do this. Pick what works best for you, and you’ll have a well-maintained site with no danger of losing rankings. Good luck!

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

Ranking of keywords have become a major issue nowadays even if the content is unique

Hi there! Ranking with your content, even if it’s unique, can prove to be difficult if other aspects of your site aren’t up to par. That’s why we suggest a holistic approach to SEO in which you work on improving every aspect of your website.

If we have cache plugin and Cloudflare cache active on website, will google consider not found status, when the host was down for maintenance?

That’s a great question! If you’re using Cloudflare’s “always available” feature (which shows a static copy of your site when it’s ‘down’), I *think* it still serves a 503 status. But, your users get a much better experience!

Hello, maybe you can make an article about a more detailed guide for this 503 redirect to a wordpress website, specifically so that someone who is just learning SEO for wordpress websites like me can understand more easily. thank you

Hi there, Rudhi. Thanks for your feedback! We aim to share content that’s understandable for everyone, so we’ll keep an eye on that :)

We care about the protection of your data. Read our privacy policy.
