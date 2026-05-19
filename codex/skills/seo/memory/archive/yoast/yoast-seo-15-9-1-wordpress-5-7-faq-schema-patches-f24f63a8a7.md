---
source: https://yoast.com/wordpress-5-7-yoast-seo-15-9-1/
title: Yoast SEO 15.9.1: WordPress 5.7 & FAQ schema patches
scraped: 2026-03-23
published_on: 2021-03-04
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

# Yoast SEO 15.9.1: WordPress 5.7 & FAQ schema patches

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-5-7-yoast-seo-15-9-1/
Published: 2021-03-04
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Today we released a patch release of Yoast SEO, 15.9.1, to prepare for some of the changes in WordPress core and FAQ schema. Read more!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Today we released a patch release of Yoast SEO, 15.9.1, to prepare for some of the changes in WordPress core. There were two changes in WordPress itself that we needed to account for, one to do with updates and one to do with meta robots output. We also had to fix an issue with how Google parses FAQ schema. Let me explain all three issues:

If you don’t want a page to be in the index of search engines, there is a standard called meta robots that allows you to exclude pages by setting them to noindex (if you don’t know what this is but want to learn, read our ultimate guide to meta robots ). WordPress 5.7 introduces a new API to output these meta robots tags. WordPress has always output some robots tags, but in 5.7, Google’s WordPress team want to add a default: they wanted to allow WordPress users to opt into seeing large image previews in, for instance, Google Discover .

This feature, introduced by Google in 2019 , has been in Yoast SEO for quite a while already as we introduced our changes two days after Google announced theirs. The changes to how WordPress outputs robots tags forced us to make some changes on our end. Note that we do not consider this a bad thing at all; we were an active part of this feature’s discussion. We settled on opting users in by default but introducing very clear messaging that shows what’s happening. For more details, see the Trac ticket .

So, if you’re updating to WordPress 5.7, please make sure you’ve updated to Yoast SEO 15.9.1 as well.

We’re slowly changing how Yoast SEO Premium works, moving it from being a replacement for Yoast SEO to being an add-on to Yoast SEO. This allows for more robust updating and much easier development. We’re making this change slowly so we can prevent updates from going wrong.

As a result of this, we’re slowly getting more and more sites running Yoast SEO and Yoast SEO Premium next to each other. What we’re now opting to do is that when you enable auto-updates for Yoast SEO, we’re also enabling them for Yoast SEO Premium and other add-ons. The reason is that if one updates and the other doesn’t, we might end up in a situation where stuff breaks. You can, of course, disable our auto-update if you’re not happy with this, and we’ll notify you in the plugin screen as well that we have just enabled auto-updates for Yoast SEO Premium or another add-on when you enable them for Yoast SEO.

Google started emailing users of our FAQ blocks about an error in the Schema output on pages containing FAQ blocks. The Schema on those pages is still valid, but Google wants to see different Schema for an FAQ than what we’re currently outputting, so we’ve changed it. For those technically inclined: instead of a Schema ItemList that we were referencing as the MainEntityOfPage , we now output a list of ID’s for the questions on the page within the MainEntity attribute of the WebPage piece.

Please update to Yoast SEO 15.9.1 if you are using our FAQ blocks.

Be sure to update to 15.9.1 if you’re planning to update your WordPress to 5.7 immediately. Of course, if you’re not ready to update WordPress itself yet, you can also safely update to 15.9.1! Also, if you use the Yoast SEO FAQ structured data block in your content you should upgrade too.

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

Hi, When I am using FAQ schema block, I can add question and answer, but can’t find “add image” option. How to solve this issue?

Hi William. That’s curious! The button should be right next to the trashcan button on the right-hand side of the block. Have you updated to the latest version? Are you running a page builder by any chance?

We care about the protection of your data. Read our privacy policy.
