---
source: https://yoast.com/wordpress-5-8-and-beyond/
title: A week with us: WordPress 5.8 and beyond
scraped: 2026-03-23
published_on: 2021-07-22
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

# A week with us: WordPress 5.8 and beyond

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-5-8-and-beyond/
Published: 2021-07-22
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
This week, WordPress 5.8 was released! This also means that our WordPress core team was already working on WordPress 5.9. Read all about it!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

This week WordPress 5.8 was released, and it included many new features. It was a huge release and you can read more about it in a separate, dedicated post on the WordPress 5.8 release . However, when it comes to WordPress our team never stops work and we’re already thinking of and working on the next release: WordPress 5.9. Continue reading to find out what exactly our team has been working on!

As always when there is a WordPress release, we are all working to push it through over the finish line. That means that any and all communication happens at a frantic pace. The whole team is in a heightened-alert state for days, sometimes even weeks. This week was no different, so we did our best to push forward and help in any way we could.

This week Sergey and I continued working on the updater project. We made a few improvements to the implementation, and Francesca created a request-for-feedback post . Hopefully, we can use the feedback provided there to further improve the implementation and improve the updater for all WordPress sites.

With WordPress 5.8 released we could now get back to working on issues that were left behind due to the release process. This week I worked on improving the implementation to allow loading multiple stylesheets per block ( #32510 ). This tweak will allow plugin and theme developers to more efficiently style blocks in the future and is part of a greater effort to improve the way we load styles and scripts in WordPress.

I also refactored the implementation for auto-generating headings anchors in the editor ( #30825 ). The new implementation is lighter, more efficient, and addresses most of the concerns that developers raised regarding block-parsing. Hopefully, we’ll see this feature merged in a future release of Gutenberg, and once that happens, we’ll be one step closer to a table of contents block.

As always, I dedicated part of my time reviewing pull requests and helping others get their ideas ready for merging.

I am glad that 5.8 is finally released. I was surprised to be listed as a noteworthy contributor because I was not involved in 5.8 in the last couple of months. At the same time, I am happy with my contributions and everything I learned.

Besides 5.8, I am excited about the pattern directory going live. You can read the announcement here . In the pattern directory, you can search for and copy block patterns to paste into your content. There is so much potential in users being able to choose from so many designs.

On behalf of the WordPress.org themes team, I published a request for feedback about changes to the theme directory requirements. We need help improving, reducing, and clarifying the requirements to make it easier to share free themes. If you have any feedback, please share it as a comment on the blog post. Sandilya Kafle (team representative for the themes team) and I are planning to interview theme authors about the requirements on Wednesday, the 28th of July.

The theme developer handbook needs to be updated with information about changes in WordPress 5.8. The themes team decided to only make two additions for now instead of restructuring the entire handbook. I will be adding information about the new theme.json configuration file and template editing.

Last week, I didn’t work five days because the COVID vaccine side effects I experienced lingered a bit longer than expected. The majority of my tasks were actually related to the work I am doing with the Yoast commerce team.

On Monday, I recorded the WordFest panel , hosted by me with some amazing guests. I had the honor of hosting our COO and board member, Chaya Oosterbroek , on her first public WordPress appearance. It will stream on Friday, July 23rd at 12:00 PM UTC. I suggest you tune in!

Just like the week before, I continued working on automated testing for an internal Yoast project. Among other things, I have implemented an integration and e2e test suite. It was a great opportunity to learn more about automated tests and to discover new technologies.

Last week I continued looking into some early tickets for WordPress 5.9, as part of my duties as a Core Committer. I made fifteen commits to WordPress core, mostly some cleanup for unit tests and documentation. I also triaged new tickets incoming into Trac (the bug tracking system that WordPress uses).

As Ari also mentioned, we continued our work on the Updater project to make updating plugins and themes more reliable. We have published a request for feedback on the proof of concept for plugin and theme rollbacks.

I also worked on modernizing the WordPress unit test suite by using more appropriate assertions and native PHPUnit functionality where possible. See ticket #53363 for more details.

Ari is a member of the WordPress core team where he gets to work full time on the open-source project with some of the brightest minds in the industry. He is an accomplished contributor with a focus on sustainability & accessibility.

We care about the protection of your data. Read our privacy policy.
