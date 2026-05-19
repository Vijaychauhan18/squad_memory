---
source: https://yoast.com/meeting-theme-developers-block-editor-improvements/
title: A week with us: Meeting with theme developers and improvements on the block editor
scraped: 2026-03-23
published_on: 2021-07-29
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

# A week with us: Meeting with theme developers and improvements on the block editor

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/meeting-theme-developers-block-editor-improvements/
Published: 2021-07-29
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week were were, once again, busy with making improvements to WordPress. And, some of us were learning a lot about SEO!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

In our weekly blog, you can read about why Ari is working on improving the block editor user preferences. Carolina has had a zoom meeting with theme developers, and Sergey is triaging tickets for WordPress 5.9. Justin has been working on other internal projects within Yoast, and Francesca is on vacation this week.

Last week I continued looking into some early tickets for WordPress 5.9 as part of my duties as a Core Committer. I made twenty nine commits to WordPress core. They were mostly some cleanup for unit tests and documentation and some bug fixes for block patterns in bundled themes. I also triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

I also worked on modernizing the WordPress unit test suite by fixing bugs in some tests and using better naming to follow the established conventions. See ticket #53363 for more details.

This week I focused on some higher-level items and concepts. During the development of Gutenberg, the team made choices. In hindsight, not all of them were optimal.

One of these choices was the way we store user preferences. Currently, these get saved using the localStorage API in the browser itself. That poses some interesting challenges, the most important being the lack of persistence. This becomes evident in things like the editor’s Welcome guide. That guide can show up again and again for the same user.

In order to fix this issue which impacts all user settings in the editor, we need to refactor some things in Gutenberg. We need to implement a method to store settings as user-meta in the database. It’s a process that will require multiple changes in the way the editor stores data. As a result, it will take a while to properly fix while accounting for backwards compatibility to make sure existing preferences are maintained and synchronized.

Since I shifted my attention back to Gutenberg after the WP5.8 release, this week on WordPress core, I assisted my colleagues in resolving issues and was part of a PHPUnit fix that was merged in WordPress Core ( #53363 ).

This week I continued with my React lessons and started taking some lessons on the Yoast Academy . Working in an SEO company, we need to stay on top of our field at all times, so it’s important to educate ourselves.

On Wednesday, I participated in a zoom call with eight theme developers from different companies. We discussed changes to the theme directory requirements . We extended the call to an hour and a half, and I think the big win was that the participants had a chance to ask questions about the requirements and the theme review process. They shared important feedback that will help us explain some of the requirements better. We will soon publish a recap on the themes team’s blog on WordPress.org. We also discussed the need for scheduling regular calls. For our next call, we are looking at dates for a zoom meeting focused on block themes.

Because I did not work an entire week, I am behind in completing my pull requests for the automated code review tools, and I will continue with them next week. The updates I made to the theme developer handbook last week have not been reviewed or published yet.

I have completed the Yoast Academy course on Site Structure and Yoast SEO and started on the copywriting course. When I finish a lesson, I always feel that I need to go and make improvements to my own website, and I think that is a good review of the courses! If you have the chance, I recommend the workshops in the Yoast Summer School . Maybe I will see you there?

Carolina is a member of the WordPress core team. Her focuses are accessibility and themes, and she enjoys every aspect of theme development.

We care about the protection of your data. Read our privacy policy.
