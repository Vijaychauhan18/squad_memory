---
source: https://builtvisible.com/recovering-your-organic-performance-after-a-site-migration/
title: Recovering your organic performance after a site migration
scraped: 2026-03-25
published_on: 2023-05-17
tags: live_feed, phase1_ingest, builtvisible, publication, seo-strategy, content, archive_backfill, historical_source
topic: seo_strategy
intent: research, monitoring, source_selection, strategy
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Builtvisible
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Recovering your organic performance after a site migration

Source: Builtvisible
Homepage: https://builtvisible.com/blog/
Original URL: https://builtvisible.com/recovering-your-organic-performance-after-a-site-migration/
Published: 2023-05-17
Strength: search strategy, content, technical SEO, digital PR, and modern search operations

## Summary
Experiencing a decline in organic performance after migrating your website? This post provides proven strategies to revive organic rankings.

## Extracted Body
Data tracking is a key element in migrations which too often goes missed. Outages in data tracking can happen at the best of times; therefore, the chances of this going wrong during a migration are even higher.

Furthermore, even with badly executed migrations, it’s very rare that all forms of traffic disappear completely so if you are seeing any of your key metrics dropping off completely around your migration time, chances are that this isn’t a real performance drop but a tracking issue .

One of the first things you should check is whether there are issues preventing your content from being crawled and indexed by search engines. There are a few things you should look into:

Preventing staging sites from being indexed as part of the migration process too often results on noindex tags being deployed to the production environment or robots.txt blocking rules not being removed when the migration is launched. For these reasons, a page’s ability to be indexed should be the first port of call when investigating drops in performance. This includes checking robots’ meta tags to ensure there isn’t a noindex tag on the page’s header and checking the robots.txt file to ensure there aren’t any unnecessary blockings in place.

Furthermore, log into GSC and navigate to Index > Coverage to find any potential errors and test the URLs that dropped using the ‘URL inspection tool’ to identify any issues that Google might be encountering when trying to access your pages.

Self-referencing canonicals are a strong indexing signal to Google that a URL is the original version of itself and deserves to be indexed (provided there is no countersignal). There are a few common errors during migrations when it comes to canonicalisation. Examples include:

Javascript is also an increasing pain point as more websites migrate to JS frameworks without properly factoring in the SEO consequences. Whilst Google can render JS content in most cases, there are some limitations to this. As such, tools like Google Search Console’s fetch and render should be used to ensure that on-page content is crawlable.

Some issues include internal links not using the “<a href>” attribute, which can severely detriment the crawlability of a website, or desktop content not present on mobile.

We’ve covered this topic in great detail on our CMS migration guide , so have a look if you feel your drop in performance could be related to JavaScript content accessibility.

Depending on the type of migration, there can be cases where the internal linking structure changes as part of this process. This can be an issue if a key page is not being linked to as much as part of a new structure as its older version was, which can severely dampen the PageRank flow and affect organic performance. Changes on the main navigation or footer, for example, are common causes behind this type of issue.

Furthermore, when URLs change as part of a migration, failing to update internal linking (so that links point to the new versions of the URLs instead of the old ones) is a common mistake. Often this takes lower priority and links are updated time after the migration has launched. This is a problem because a percentage of the internal link equity is being lost during the redirects, which can contribute to lower performance.

For this reason, whilst a redirect may be in place; it should not be relied upon as a substitute; instead of link realignment so it’s important.

Open you pre-migration and post-migration crawls and compare the number of links pointing to your old and new URLs and investigate any potential differences when it comes to number of links or click-depth.

A successfully implemented redirect mapping is an integral part of any website migration which will help you avoid lots of issues post-migration. Therefore, checking that your redirect mapping plan has been executed as intended is one of the key checks you’ll need to perform if you are experiencing drops in traffic after launching a migration.

Whilst link realignment can be laborious, links (both external and internal) are a heavy contributor to on-page authority due to the flow of link equity. Ensuring an efficient path for the flow link equity is crucial to organic performance so you should make sure you invest the time needed to realign both internal and external links .

A drop in visibility could also be down to the new site’s pages and content structures being less cohesive and detailed, or not building as much relevance and delivering the same great experience as older pages.

On-page content missing or changing at the back of the migration is the most common issue, especially when this happens across key pages. Stripping content can lead to fewer keywords being effectively targeted and changing key elements of the page’s content, such as headings or meta titles, can lead to different keywords being targeted, leading to ranking loses.

Content changes can still be required – or even beneficial – during a migration. However, it’s important that these are part of the a new keyword targeting strategy carefully planned.

The importance of internal links has already been covered previously, however, when it comes to links, is also important to consider what anchor text is used, as this plays a strong relevancy signal in telling Google what a page is about and the keywords it’s trying to target. Consequently, maintaining the same anchor text in links, where possible, will negate possible keyword fluctuations. This includes links within pages’ copy but also in the main navigation.

Sometimes, the migration might not be the culprit of a drop in performance. External factors which are out of your control – such as Google algorithm updates causing volatility in SERPs – might be at play too.

Check tools like SEMRush’ Sensor to see if any fluctuations have been recorded around the time of your migration. If so, give the SERPs enough time to settle and keep a close eye until your rankings recover:

Changes in search demand and seasonal dips could also lead to a perceived decline if coinciding with a migration. Identify the pages and keywords that saw a decline in rankings and investigate whether there has been a change in demand using tools like Google Trends or Mangools.

If none of the above reasons explain the performance issues your site is experiencing since the migration, you might want to reaudit your site again using the SEO migration checklist you used during the migration process, to ensure you haven’t missed anything when checking implementations before launch in staging and immediately after launch in production.

Don’t give anything for granted and conduct all the checks you would execute on a launch day to find where the problem might be coming from and how to solve it. Our migration guide mentioned above contains all the steps you’d want to follow to ensure your migration is successful or, if you are still struggling with website performance you can also get in touch with our site migration experts , who will be able to help you.
