---
source: https://yoast.com/yoast-seo-14-5/
title: Yoast SEO 14.5: New internal linking blocks for Premium
scraped: 2026-03-23
published_on: 2020-07-08
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

# Yoast SEO 14.5: New internal linking blocks for Premium

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/yoast-seo-14-5/
Published: 2020-07-08
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Yoast SEO 14.5 is out! In this release, you'll bug fixes and enhancements. Plus, Yoast SEO Premium gets two new internal linking blocks.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Yoast SEO 14.5 is out today! In this release, we fixed a number of bugs, disabled the XML sitemaps that will arrive in WordPress 5.5 and added two new block editor blocks for our Premium users. These blocks help you with internal linking for hierarchical pages. Let’s find out more!

We all know internal linking is very important as it is helps you build your site structure, making your site easier to digest for both humans as well as machines. We have several tools that help you improve your internal linking and today, we’re adding two internal linking blocks for the block editor that can help you improve it even further. Meet the Subpages block and the Siblings block!

If you work with a lot of hierarchical post types, you’re often linking to underlying pages or to sibling pages. We thought of a way to make that process easier to do and we came up with two different — but related — blocks for working with subpages and sibling pages .

The new blocks in Yoast SEO 14.5 are very easy to use and basically do what they say on the tin. The Subpages block lists all the subpages that have that particular page as a parent. So, if I have a page about Italian food, I might have subpages like this:

Adding the Subpages block to the page, automatically presents all these subpages in a neat list.

You can add the Siblings block to any of the subpages to list the siblings of the page you’ve added it to. So, if you add it to the pasta page, it’ll automatically list the related pages, in this case pizza and soup.

Now, you can link all hierarchically related content by simply adding a block! The blocks only work on hierarchical pages, not on blog posts.

Want to read more about working with hierarchical pages? Read Willemien’s post on parent and child pages: Linking hierarchical post types for SEO .

While the blocks in their naked form might seem a bit awkward for some purposes, you can style them with CSS to your hearts content. For instance, by using a bit of additional CSS you can turn them into something like this:

You don’t need much to come to the above result. For reference, find the CSS below. Remember, you can easily add custom CSS via the theme customizer in WordPress.

With WordPress 5.5, XML sitemaps make their way into WordPress core. Of course, that’s good news for the web. Together with Google, we spearheaded the project of bringing XML sitemaps to core and we’re proud that the moment has come that every WordPress site will get an XML sitemap. Now, a large part of the web will be a much friendlier place for crawlers!

As awesome as the core XML sitemaps may be, we’ve decided to disable these for Yoast SEO users and we’re continuing to use our own XML sitemaps. Our XML sitemaps are more sophisticated, integrated, and automated, that’s why we decided to disable the core WordPress XML sitemap for our users.

You can read more about this decision in our FAQ on XML sitemaps in WordPress 5.5 and Yoast SEO .

In Yoast SEO 14.5, Premium users can enjoy two new blocks for the block editor: the Subpages and Siblings blocks. These can help improve internal linking for hierarchical pages. They are extremely easy to use, but powerful!

We’ve also chosen to continue to use our own XML sitemaps over those in WordPress 5.5 as ours are fully developed, fast and flexible. We think these’ll serve your site best.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

Will the content automatically update if sub/sibling pages are renamed, added, or removed?

Hi there Andrew, good question! The answer is yes, they will be automatically updated when you rename, remove, or add pages :)

My Yoast is showing as 14.5 but the new blocks are not showing in the block editor?? I’m a premium member

Hi Olivia. Have you added them to pages with subpages attached to them? They only work on hierarchical pages, so not on blog posts. If you still can’t see them, please contact our support team.

New internal linking system is sounds something new to me. great post Thanks.

It is generating empty lines and duplicate lines for me. I think the duplicate lines come from renamed or redirected pages.

Hi Jochen, that’s strange behaviour. Sorry for the inconvenience and thanks for letting us know! Could you please send an email to our Support engineers (support@yoast.com)? They’ll be glad to help!

Hello. ” aria label ‘undefined’ ” was added when I used your nofollow feature to external links. I guess WP has removed the use of the aria label. Because it doesn’t add aria label to my external links for a long time. So “undefined” is being added with your nofollow feature. Has this problem been resolved with this release?

Hi Mehmet, thanks for letting us know! We’re looking into it at the moment. We will let you know the outcome.

The new blocks are not showing on my end. I have premium and its updated.

Hi! Hmm, strange. Are you trying to add the blocks to blog posts maybe? These only work on pages with subpages attached to them.

Is their a timeframe for when the sitemap functionality is going to work with the new indexables capability of Yoast? My experience is that sitemaps take a (relatively) long time to generate, especially on image heavy sites.

Good to hear that you disabled the core XML sitemaps. Maybe later there can be an option to let us choose which of the two we want to use.

Hi Okoth. For the time being, we’re going to use our own. We’re actively working on making them even better.

does this sibling only work on pages? or posts as well? the other thing is, i seem to recall google hitting a provider that used to use this type of linking previously (sitesell package- think they now also do wordpress setup). But for the life of me i cannot remember exactly why. I would assume that you would also want to link upwards on the subpage, back to the “index” page.

Hi Kenny. The blocks only work on hierarchical pages, so not on blog posts. I’m not sure what you’re hinting at with the Google penalty. Would be interesting to know more if you can find it.

We care about the protection of your data. Read our privacy policy.
