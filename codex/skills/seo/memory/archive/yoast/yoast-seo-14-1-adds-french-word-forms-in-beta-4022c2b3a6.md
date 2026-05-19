---
source: https://yoast.com/yoast-seo-14-1/
title: Yoast SEO 14.1 adds French word forms in beta
scraped: 2026-03-23
published_on: 2020-05-13
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

# Yoast SEO 14.1 adds French word forms in beta

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/yoast-seo-14-1/
Published: 2020-05-13
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Yoast SEO 14.1 is out today! This release comes with another language addition for our Premium analysis: French. Also, fixes and enhancements.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Yoast SEO uses sophisticated language analysis tools to help you optimize your texts. Most checks work for any language, but our Premium analysis relies on word recognition functionality, which we develop custom for every language. It takes a lot of time to get this perfect for every language out there. Starting with French in Yoast SEO 14.1, we decided to try something new and just ship what we have. This way you can already benefit from better keyphrase recognition, and we’ll allow you to give us feedback to help improve support for your language faster!

Over the last couple of releases, we’ve talked a lot about word form support for different languages. Thanks to the Premium SEO Analysis , the plugin recognizes your focus keyphrase in a text, even if that word is in a different form. In French, that means we will be able to detect all these word forms, which helps you quickly improve your content. Today, we’re launching a beta version of the word form feature in French. We’ll allow users to help us improve it, more on that below.

The Yoast SEO Premium analysis makes it easier to improve your text. It helps you write a perfect blog post, and it does so in a much more transparent way. Combine this with the synonyms and related keyphrases feature, and you have an excellent tool that is intensely satisfying to work with!

Check out the video, featuring our good friend and renowned SEO expert Jason Barnard!

Of course, we have more language on the way. We collected all the supported languages in our SEO analysis on our features per language page .

The launch of French word forms consists of a beta version that we’re improving and expanding as we go. We use this first release to get French up and running. Now, we can find and recognize word forms in French much better than before, but not as good as the other languages we’ve implemented. That might mean that we don’t recognize every word correctly or that you’re noticing false-positives. If you find things like this, we’d like to know!

To help us collect your insights and experiences, we’re working on a special language feedback system inside the plugin. That’s not done yet, so until then you can send us your improvements via email .

While sending us your feedback, please include the following:

In Yoast SEO 14.1, we’ve not only added a new language to our word forms roster but also improved the Dutch language version. Another language-based improvement is an updated list of Hungarian transition words.

Curious about what happened with Yoast SEO 14.0? Read Joost’s post Yoast SEO 14.0.x; or “Why you should never bypass wpdb” .

Despite weeks and weeks of testing Yoast SEO 14.0 , there were still some people running into issues. In Yoast SEO 14.1, out today, we’re improving things to help stabilize the plugin.

Among other things, we’re making several changes regarding the indexables. In the backend, we’re making it clearer what the process actually does and what you as a user can expect. We’ve also made it possible to show debug information that gives an idea of what went wrong in the indexing process in case you run into issues.

We’ve made several improvements to the indexing process itself. For instance, we’re preventing duplicate indexables to enter the database table. Plus, we’re no longer building indexables from taxonomies that aren’t public. We’ve also added the option te reindex a site’s content from the CLI.

In addition, we fixed several bugs regarding the publication and presentation of breadcrumbs, in Schema and elsewhere. In the changelog for Yoast SEO 14.1 , you’ll find a list of all the fixes and enhancements.

That’s Yoast SEO 14.1 for you! In this release, we’ve fixed a number of bugs and made several improvements concerning the indexable release. In addition, we made several enhancements that’ll make the current version of Yoast SEO more stable and easier to use.

That’s not all, because we’ve also added another language to our ever-expanding list: French! Premium users who write in the French language can now enjoy a more flexible and natural writing and optimizing environment thanks to word form support. More languages on the way, so stay tuned. And don’t forget you can help add or improve your language!

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

I am using Rank Math due to my friend suggest but could not get any good result from Rank Math now I want use Yoast but how can it replace by Rank Math tools??

Hi Omprakash, if you’re thinking about switching to Yoast this article can help you with the import from other SEO plugins: https://yoast.com/help/import-options-in-yoast-seo/

How do I block individual pages from Google now in version 14.1?

Hi Eric, if the advanced section of the meta box disappeared you can use a temporary workaround: In your left-hand menu, go to SEO –> General –> Features tab. There you see “Security: no advanced settings for authors”. If you turn that on, you should get the advanced section back on individual pages. It’s a known issue and we’re working on a fix https://github.com/Yoast/bugreports/issues/1021 . Hope this helps and sorry for the inconvenience!

Hi Anand. I’m sorry you are running into problems. It might be a good idea to reset the Yoast database tables and re-install Yoast SEO 14.1. To reset the tables, install the Yoast Test Helper , then go to SEO>Tools>Yoast Test. Click “Reset indexables & migrations” to delete the tables. After that, re-install Yoast SEO 14.1, press the indexing button, and see if that helps. If you have a large site or prefer to do this from the command line, you can run the Yoast SEO WP CLI command here: https://developer.yoast.com/customization/yoast-seo/indexables-cli/ Good luck!

You wrote to me: We wanted to follow-up and let you know there is a Breadcrumb bug in the Yoast plugin that is causing breadcrumb items to get out of order.

I confirm that it goes like Home > child>parent> page … It’s really annoying. Hope next update will fix that

Hi. The breadcrumb order bug will be solved in Yoast SEO 14.2, which is due next Tuesday. Sorry for the inconvenience!

Hi Aleksey. We have a fix planned for 14.2, which is due May 26.

I installed v14.1. But when I pressed the button to build your SEO index, i still receive the error – ‘Something went wrong while optimizing the SEO data of your site. Please try again later.’

Hi Anand, we’re so sorry, something when wrong with the comment reply. You can see Edwin’s reply to your comment above, for some reason it wasn’t placed as a reply to your comment, but as a new one. I’ll paste it here too, just to be sure. Hope this helps:

Hi Anand. I’m sorry you are running into problems. It might be a good idea to reset the Yoast database tables and re-install Yoast SEO 14.1. To reset the tables, install the Yoast Test Helper, then go to SEO>Tools>Yoast Test. Click “Reset indexables & migrations” to delete the tables. After that, re-install Yoast SEO 14.1, press the indexing button, and see if that helps. If you have a large site or prefer to do this from the command line, you can run the Yoast SEO WP CLI command here: https://developer.yoast.com/customization/yoast-seo/indexables-cli/ Good luck!

Is this compatible with WPML now? 14.0.4 didn’t worked before.

Hi Flavius, it should work now! If you, unexpectedly, encounter any issues please let us know. Good luck!

I am a user of Yoast plugin I can’t see the “Advanced tab” again. I want to add no-follow alt to all links on a particular page. Please help

Hi Nirmal, Sorry for the inconvenience, that’s a known bug and we’re working on a fix! For the time being, you could use this workaround: In your left-hand menu, go to SEO –> General –> Features tab. There you see “Security: no advanced settings for authors”. If you turn that on, you should get the advanced section back. Hope this helps!

This is great news, and thank you for all the hard work! I was wondering, though: does this mean the Yoast plugin gets larger and larger in size? Will adding more and more languages slow everything down. I just remember a former plugin I used to use which kept adding new features, but at the sacrifice of performance, so I was wondering how the same might affect Yoast?

Good question, John! None of this is ever loaded on the Frontend. As for the admin: some of these files are only loaded as needed from MyYoast already, so we don’t have to load all the data for every language for everyone. We’re constantly working on improving that, as you can imagine this is new grounds as nobody in the WordPress world does something similar. Good luck with your site!

After updating my Yoast plugin, I can’t see the “Advanced tab” again. I want to add no-follow alt to all links on a particular page. Please help

Hi there, sorry for this bug and thank you for letting us know! It’s a known issue and we’re working on a fix https://github.com/Yoast/bugreports/issues/1021 . There is a temporary workaround: In your left-hand menu, go to SEO –> General –> Features tab. There you see “Security: no advanced settings for authors”. If you turn that on, you should get the advanced section back.

Best blog to learn about yoast seo plugin how you can use the plugin to make your website seo friendly.

So when would you finally reduce the price of premium yoest to we the young once

Hi Richard, sorry we don’t have plans to reduce the price. It might be wise to subscribe to our newsletter though, so you don’t miss any of our temporary discounts!

Good to have this new tool. We work with a website in French and this will certainly be one more tool to improve our presence on Google and other search engines.

We care about the protection of your data. Read our privacy policy.
