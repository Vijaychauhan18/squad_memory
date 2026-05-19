---
source: https://yoast.com/google-doesnt-use-rel-prev-next-for-pagination/
title: Google says it doesn't use rel=prev/next for pagination
scraped: 2026-03-23
published_on: 2019-03-22
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

# Google says it doesn't use rel=prev/next for pagination

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/google-doesnt-use-rel-prev-next-for-pagination/
Published: 2019-03-22
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Google announced that it doesn't use rel=prev/next links and hasn't for years. This post describes what this means and what you should do.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Sometimes you wonder if Google even knows how Google works. Search is getting more complex by the day and there comes a point where it’s anybody’s guess. Yesterday, Google ‘announced’ that its search engine doesn’t use the pagination markup rel=prev/next at all and hasn’t for years. That’s curious because they have been advocating using it until very recently.

The web standard rel=prev/next was introduced many, many years ago to help determine relations between part of URLs or different pages. In 2011, Google started using those links as a strong hint to discover pages that were related. Almost every site now uses these links to provide these hints. Yoast SEO automatically adds these links for our users. Now, it turns out Googlebot is deemed so ‘smart’ by Google that it doesn’t need help anymore.

Some smart SEOs found the official help docs for how to use this for pagination gone. Yesterday, Google was pressured into giving an official announcement on this. Here’s that announcement:

Nice and easy, right? Although it is unclear what the pagination changes mean for huge e-commerce sites, for instance: good luck trying to cram 10.000 products on a single view-all page.

Google’s advice on its now deleted Webmasters Help page gave the following three options to handle paginated content:

That page was available up until early this week and it’s not a good practice to simply delete such a page. It would have made much more sense to update the article or show a notice that something changed. Just deleting it without even redirecting it to something else useful feels off. For now, the original blog post announcing the use of rel=prev/next by Google is still available — with a new notice at the top.

Google’s current stance is that Googlebot is smart enough to discover the next page by analyzing the links on a page and, therefore, a strong signal like rel=prev/next isn’t necessary anymore.

That, however, doesn’t mean you should go and delete all those rel=prev/next links you’ve worked so hard to implement.

It’s important to remember that this is a web standard and that there are other search engines besides Google. Bing’s Frédéric Dubut already said they’re using rel=prev/next as hints for discovering pages and understanding site structure, but not to group pages or rank them.

While we wait for the dust to settle and maybe see if Google details a new way of handling pagination, here are a couple of things you should keep in mind:

So, for the moment keeping everything as it seems like the most sensible option. As this is a W3C standard and not just something Google dreamed up, it’s best to stick to it. It is a good time to take a long hard look at your site structure though!

Yoast SEO has handled pagination for WordPress sites for ages. As I said, we automatically add everything search engines need to understand how things fit together, like rel=prev/next and a self-referencing canonical.

Not too long ago, we changed the way we handled indexing of paginated content . Initially, we offered the option of noindexing archive pages, but as Google mentioned several times that long-term noindexing eventually leads to them not following those links after some time. This makes adding noindex to page 2 and further of paginated archives a bad idea, as it might lead to your articles no longer getting the internal links they need.

As it stands now, we are talking about how to best go about handling pagination. The need for proper pagination is still there, but it might just turn out that Google has indeed become much smarter at figuring out how everything fits together — and what to show in search or not.

For now, we think that it makes sense to keep everything working the way it does at the moment. Pagination tags can still be useful to other systems — and, if paginated pages are just ‘normal pages’ now, then it makes it even more important not to noindex them.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

Thank you for sharing such helpful information with us. We was not aware about this. Keep up the good work!

Hey @Edwin Toonen, thanks for aware about don’t use “rel=prev/next” for pagination also we will immediately applied on our websites as well as. we will waiting for your upcoming post about Google latest updates.

But how to remove this rel=prev/next on site any idea please

Thanks Yoast team for sharing this powerful and helpful article with us.

Thanks yoast . your team is powerfull in worldwide and i learn everything from your blog and used your best plugin thanks you

Does eliminating the rel=prev/next mean that Google will be doing the choosing for what our readers view next? I’m subbing the free SEO tips to learn more, but I don’t wish to spend a lot of money if I don’t have time to look at all the training tools. One bite at a time! ;-) I do love how my site is working so far! ^__^

“Not too long ago, we changed the way we handled indexing of paginated content. Initially, we offered the option of noindexing archive pages, but as Google mentioned several times that long-term noindexing eventually leads to them not following those links after some time. This makes adding noindex to page 2 and further of paginated archives a bad idea, as it might lead to your articles no longer getting the internal links they need.”

In the above are you saying not including category/tag archive pages in the sitemap or getting them index is a bad idea?

Its also better to use number pagination for great user experience

We care about the protection of your data. Read our privacy policy.
