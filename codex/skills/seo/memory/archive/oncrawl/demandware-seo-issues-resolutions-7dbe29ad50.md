---
source: https://www.oncrawl.com/technical-seo/demandware-seo-issues-resolutions/
title: Demandware SEO Issues & Resolutions
scraped: 2026-03-25
published_on: 2016-12-07
tags: live_feed, phase1_ingest, oncrawl, publication, technical-seo, ai-visibility, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Oncrawl
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Demandware SEO Issues & Resolutions

Source: Oncrawl
Homepage: https://www.oncrawl.com/
Original URL: https://www.oncrawl.com/technical-seo/demandware-seo-issues-resolutions/
Published: 2016-12-07
Strength: technical SEO, data-driven SEO, AI search visibility, internal linking and crawl analysis

## Summary
Demandware is a leading e-commerce platform for retailers. The platform however is not without its own SEO challenges. How to deal with them?

## Extracted Body
Demandware (now known as Salesforce Commerce Cloud ) is a leading e-commerce platform for retailers , allowing them to grow and manage tailored desktop and mobile commerce sites and is especially well suited to large brands with international audiences.

Today Demandware is used by global brands such as Adidas, Lacoste and Puma and it is estimated that 21% of the top 10,000 sites using Enterprise technologies are using Demandware . The platform however is not without its own SEO challenges, which overcome can improve site performance in organic search.

However the principles of good SEO remain the same, regardless of the type of site and project. Having had experience of working with clients using Demandware previously, we’re aware of what issues to look out for before we begin any analysis.

Demandware relies on customised development, as do many platforms, and this can often lead to oversights and mistakes. This is because (unfortunately) a developer’s priority list isn’t always in line with an SEOs (or SEO best practice).

This means that without undertaking a technical SEO campaign, opportunities may have been missed through technical mistakes onsite, creating a glass ceiling and limiting performance within organic search. Below are some of the common Demandware issues and how to resolve them .

Faceted navigations can cause issues on a number of issues on e-commerce websites, and this is no different with Demandware.

With Demandware, each search filter adds a parameter to the URL, creating a duplicate page. If these URLs are then being indexed this can cause index bloat issues, issues with your crawl budget and duplication issues.

For instance, in your faceted navigation you might be able to filter products by brand, so your URL could look like:

The Adidas content is accessible without the parameters, so to fix this issue you would:

It’s common for Demandware to put a parameter on the end of a product URL, which changes depending on how you access it. On some product grid systems, the appended parameter reflects the position in the grid (so the first product becomes ?start=1, second becomes ?start=2 and so on).

As products move in the grid layouts, multiple URLs will be generated with a new parameter each time – because of this, simply blocking *?start* in the robots.txt won’t solve the problem.

The long term fix for this would be to make it so the product pages don’t require parameters, but in the short term adding a self referencing canonical to the product page, minus the parameter should mitigate the issue:

So https://onlinestore.com/sneakers/adidas-neo?start =1 would have a canonical pointing too https://onlinestore.com/sneakers/adidas-neo .

Demandware has the ability to generate some really long, horrific homepage URLs, for example:

http://www.columbiasportswear.co.uk/on/demandware.store/Sites-Columbia_EU-Site/default/Home-Show

http://www.geox.com/on/demandware.store/Sites-geox-Site/fr/Home-Show

Both of these have been ‘fixed’ with 301s pointing back to the root domain. It’s important that these are dealt with, with self-referencing canonicals put in place, otherwise you could end up with duplicate homepages.
