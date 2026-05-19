---
source: https://yoast.com/wordpress-5-8-beta-1-and-more/
title: A week with us: WordPress 5.8 Beta 1 is here and more
scraped: 2026-03-23
published_on: 2021-06-10
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

# A week with us: WordPress 5.8 Beta 1 is here and more

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-5-8-beta-1-and-more/
Published: 2021-06-10
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Find out what our WordPress core developer team has been up to this week, including WordPress 5.8 Beta 1 and WordCamp Europe!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

On Tuesday, June 9th (or Wednesday June 10th, depending where you are in the world) WordPress 5.8 Beta 1 was released . Many members of the team contributed to take this version of WordPress past this first milestone. After getting a small break thanks to WordCamp Europe, we are now switching our focus to finding bugs, squashing them and preparing for Beta 2. And of course we did some other stuff along the way.

This week I continued working on items related to WordPress 5.8 and the Gutenberg editor. I focused on backporting fixes intended for the next WordPress release.

The site-logo block was finally merged in WordPress Core and will be included in version 5.8, so this brings us one step closer to template-editing in core. This required backporting changes from core to Gutenberg and vice-versa so the task took a few days to complete.

In an effort to improve the way developers can use CSS units in blocks, I submitted an additional pull request, refactoring the way CSS Units are defined in editor controls ( #32482 ).

I finished working on a pull request which will allow theme-authors to style blocks more efficiently ( #32275 ). This is part of a continued process to improve the sustainability of WordPress sites, and will allow themers to take advantage of some recent improvements on that front. On the topic of sustainability, I also continued working on a pull-request to split theme.css files in blocks, and load them conditionally when the block gets rendered.

I submitted a proposal/pull-request to allow enqueuing multiple stylesheets per-block ( #32510 ). This will allow blocks to have stylesheet dependencies, and also allow plugin and theme authors to properly enqueue styles for their blocks. Combined with the pull-requests mentioned above aiming to improve sustainability, this can be a powerful tool for WordPress.

WordCamp Europe (WCEU) was an online event held this week, and I spent a lot of time in the Yoast booth, meeting new people and talking to members of the community. It was an awesome event, but hopefully it will be the last of its kind, and next year we’ll be able to attend a physical event instead of an online one due to the Covid restrictions.

This week I received an introduction to acceptance testing and the different testing procedures at Yoast. I have continued working on the Theme Check plugin and learning about the Theme Review Action tool. On this topic, I have participated in a cross-team meeting about theme directory requirements and testing tools.

In the afternoons, I have enjoyed WordCamp Europe Online, both the theme-related talks and workshops and chatting with new and old WordPress friends.

This past week was about prepping! Lots of things cooking in WordPress and at Yoast, so I did feel more than ever the cognitive load of infamous context switching. The cognitive load gets counterbalanced by love: for my job, my team, my company and knowing that what we do can have a big impact on lots of people. So with this in mind, here are my main topics for the week.

I am not actively involved in this release. However, as I mentioned last week , I started contributing to the Upgrade/Install component. The first goal contributors are tackling, besides the day-to-day operations of addressing issues in that component, is to make the process of updating seamless, painless, and safe. Not many people show up for the meetings, but they are useful nevertheless and consistency is key for open source projects. This is one of the ways you can gain traction and keep it on issues that are dear to you.

Now that WordPress 5.8 is in Beta 1, I plan to review the existing documentation, so the next release squad will find an updated handbook. I will start with the release section, which needs some sprucing up.

I am also interested in the progress of the theme review process, based on the desired outcomes expressed by Josepha and Matt after their meeting with the Themes Team .

The WordPress Core team hosted two Q&A’s inside the Yoast booth at WordCamp Europe 2021. I have mixed feelings about online events. I see why we need them to keep the community spirit going, but as someone who spends most of her time on video calls, consuming content in video form, having professional events on video too is difficult.

Overall I am happy that familiar and new faces came to visit. But yeah, I am ready to meet everyone in person and hug.

We have already hosted a number of contributor days online for Yoasters. You can read about two on this blog: February and April .

This time we are inviting other contributors to lead the teams that will be working on WordPress.org. It is another step we are taking to refine the contributor day experience. After we review the upcoming one, I expect us to be ready to host contributors from outside of Yoast to join us for the day.

I am a community manager at heart. And I am also a decent business person. So I am putting the two together to work with team Commerce. Right now this means reaching out to companies in the WordPress ecosystem to do some user/business interviews. I started by pinging friends and contacts in the community. It’s also a good excuse to catch up with people and celebrate the fact that, despite a pandemic, we are still here :)

This week, I’m working on some projects for the WordPress Core test team. Mainly publishing posts on the Make/Test blog to inform contributors about the current status of e2e testing in WordPress Core.

I also continued to triage tickets in the 5.8 milestone, but also tickets marked as needing testing on Trac.

I’ve made some notable progress lately on our e2e testing package at Yoast. I’ve implemented new tests, extended the coverage of existing tests, and also made improvements to the documentation.

For the last week, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8 , the next major release, as part of my duties as a Core Committer.

I made thirteen commits to WordPress core and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

WordPress Core Committer and plugin author, also working on Polyglots, Support, and Meta teams. Co-founder of Russian WP community.

We care about the protection of your data. Read our privacy policy.
