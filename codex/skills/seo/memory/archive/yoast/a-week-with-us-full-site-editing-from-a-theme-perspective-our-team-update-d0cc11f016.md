---
source: https://yoast.com/full-site-editing-from-a-theme-perspective/
title: A week with us: Full Site Editing from a theme perspective & our team update
scraped: 2026-03-23
published_on: 2021-04-01
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

# A week with us: Full Site Editing from a theme perspective & our team update

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/full-site-editing-from-a-theme-perspective/
Published: 2021-04-01
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
In this week's blog, Ari discusses Full Site Editing in WordPress from a theme perspective. And, we share our weekly team update.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

An essential item in WordPress’s roadmap for 2021 is to bring Full Site Editing (FSE) into WordPress Core. This is a rather big project, one that has been ongoing for more than twelve months. After all this time, we’re finally getting close to including it in WordPress Core.

At the heart of FSE is a new paradigm of WordPress themes. One that will allow a lot more freedom and versatility without requiring expert coding skills. Using FSE, site owners will be able to freely edit their layouts and templates using nothing but the block editor. What’s more, theme authors will be able to design their theme directly in the editor, then export the templates with the push of a button. There’s no need to write complicated PHP for templates, so theme authors can focus on what makes themes great: their styling.

If it sounds like a big change, that’s because it is . But it’s also a non-breaking change: nothing will change for existing themes. Nothing will break when WordPress gets updated. Using an FSE-enabled theme is a choice, and if you don’t use a theme built around FSE, then chances are you won’t even know it exists.

The goal in WordPress 5.8 is to include a Minimum Viable Product (MVP) of FSE. But what does that MVP look like? Josepha Haden Chomposy, the executive director of the WordPress project, answers that question in a recent podcast in WPTavern (quote on the FSE MVP is about 26 minutes in):

“ Could I, using the blocks available, pull together the major functional parts of a campaign landing page? “

At this stage, that is our goal: to allow users to create simple websites using nothing but the editor. All the ingredients are there. All the options and components are there. What we need to do is make the experience more intuitive and streamlined.

Existing themes don’t need to change. New themes can be built either as FSE themes or as “classic” themes, using the same techniques and structure we’ve all been using for more than a decade. But right now, that is a binary choice: it’s either one or the other. There is no middle ground. And that is where “hybrid” themes come in.

Hybrid themes are a way to allow a gradual transition from classic, PHP-based themes to block-based (FSE) themes. They are part PHP-based and part block-based. Support for hybrid themes is still under active development and not a prerequisite for the FSE MVP. Still, we think they are essential to FSE’s future as they will ease its adoption by pre-existing themes.

We took the first step towards allowing hybrid themes by merging a pull-request to allow a mixture of PHP and block template files . The next step is to allow PHP-based themes to use block-based template-parts for their header and footer .

These pull-requests tackle the basic mechanics of how things will work. However, they don’t address some bigger-picture questions like how the user will edit these parts or interact with the FSE interface. Still, they are essential to theme authors. They will enable authors to start migrating parts of their theme without being forced to convert everything all at once. They will also allow block-based themes to work out of the box with plugins that load their own PHP templates (a popular example of such a plugin is WooCommerce).

FSE is vital to the future of WordPress, and we could use your help. One of the most important things moving forward is testing. Everything needs to be thoroughly tested so we can pinpoint issues and fix them. To that end, there is a Full Site Editing Outreach Program where you can test specific scenarios, following detailed instructions.

If you have experience in design, UX, or writing code, you can check out issues tagged with the Full Site Editing feature or help review one of the already submitted pull requests .

Last week, my main focus was to continue reviewing bug fixes and enhancements for WordPress 5.8, the next major release, as part of my duties as a Core Committer. I made nine commits to WordPress Core, led a meeting for new Core contributors, and triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

Just like the past few weeks, I have mostly been testing and reviewing pull requests regarding full site editing on the Gutenberg GitHub repo. I am still learning how to contribute better to the Gutenberg plugin, and I try to create small pull requests for small bugs, like this bug where the new post excerpt block could not be selected, deleted, or moved if it was not placed in a post or an archive. The post excerpt block is one of the new blocks that can only be used with full site editing. With this block, you can add and customize a post excerpt or set the length of an automated excerpt. It also has an optional read more text. There is ongoing work to update the CSS that the editors use to make sure that what we see in the editor matches the front of the website. Not a day too late, and I think most theme authors would agree because themes have had to add their own CSS to solve this. Another thing that may interest theme authors is that the default margins between blocks in the editor may be removed or may be moved to a separate file; different solutions are being discussed in the pull request.

The design team is making nice progress on refreshing some of our Handbook content. Many articles are written for people who are familiar with how the team works, so it already helps a lot to start by thinking: “Would a newcomer understand what this is for?” And then writing a new first paragraph addressing that. Other than that, I’m also trying to help out reviewing FSE issues, but wow, lots going on over there! It’s going to take some time to really get up to speed with everything.

We have completed Q1 and are now entering Q2 of 2021. This week I am focusing on refining my goals for this quarter. Among other things, it will be working on testing in WordPress, especially End-to-End (E2E) testing. Also, I have Google Season of Docs on my plate, and as always: documentation.

This week, we’re working on reviving the WordPress Test Team with Tonya Mork from Automattic. This will include announcements on the team blog , planning team meetings, and reaching out to people who are or might be interested in contributing to testing in WordPress.

This week, I focused on experimenting with hybrid themes and finding ways to move this important aspect of theming forward. One of the primary goals is to allow FSE themes to work with WooCommerce, as that would be a clear signal that most aspects of a hybrid implementation will work both for plugins and themes.

Among other things, I submitted a new pull request for skip-links in FSE themes , an important component of making the frontend of an FSE-enabled website more accessible.

Next week, my focus will remain the same; improving the hybrid-themes implementation and the accessibility for end users/visitors. I will continue dedicating a significant portion of my time doing code reviews and helping other authors get their ideas and code included in Gutenberg and WordPress.

Ari is a member of the WordPress core team where he gets to work full time on the open-source project with some of the brightest minds in the industry. He is an accomplished contributor with a focus on sustainability & accessibility.

We care about the protection of your data. Read our privacy policy.
