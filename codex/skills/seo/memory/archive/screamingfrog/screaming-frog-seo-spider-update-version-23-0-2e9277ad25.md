---
source: https://www.screamingfrog.co.uk/blog/seo-spider-23/
title: Screaming Frog SEO Spider Update – Version 23.0
scraped: 2026-03-25
published_on: 2025-10-20
tags: live_feed, phase1_ingest, screamingfrog, screaming-frog, publication, technical-seo, crawling, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Screaming Frog Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Screaming Frog SEO Spider Update – Version 23.0

Source: Screaming Frog Blog
Homepage: https://www.screamingfrog.co.uk/blog/
Original URL: https://www.screamingfrog.co.uk/blog/seo-spider-23/
Published: 2025-10-20
Strength: technical SEO, crawling, site architecture, large-site workflows

## Summary
We’re quite pleased to announce Screaming Frog SEO Spider version 23.0, codenamed internally as ‘Rush Hour’. The SEO Spider has a number of integrations, and the core of this release is keeping these integrations updated for users to avoid breaking changes, as well as smaller feature updates. So, let’s take...

## Extracted Body
Posted 20 October, 2025 by Dan Sharp in Screaming Frog SEO Spider

We’re quite pleased to announce Screaming Frog SEO Spider version 23.0, codenamed internally as ‘Rush Hour’.

The SEO Spider has a number of integrations, and the core of this release is keeping these integrations updated for users to avoid breaking changes, as well as smaller feature updates.

Lighthouse and PSI are being updated with the latest improvements to PageSpeed advice, which has now been reflected in the SEO Spider.

This comes as part of the evolution of Lighthouse performance audits and DevTools performance panel insights into consolidated and consistent audits across tooling.

In Lighthouse 13 some audits have been retired, while others have been consolidated or renamed.

The updates are fairly large and include changes to audits and naming in Lighthouse that users have long been familiar with, including breaking changes to the API. For example, previously separate insights around images have been consolidated into a single ‘Improve Image Delivery’ audit.

There are pros and cons to these changes, but after the initial frustration with having to re-learn some processes, the changes do mostly make sense.

The groupings make providing some recommendations more efficient, and it’s still largely possible to get the granular detail required in bulk from consolidated audits.

To get ahead of the (breaking) changes, we have updated our PSI integration to match those across Lighthouse and PSI for consistency.

Older metrics, such as first meaningful paint, have also been removed.

If you’re running automated crawl reports in Looker Studio and have selected PageSpeed data, then you will find that some columns will not populate after updating.

The next time you ‘edit’ the scheduled crawl task, you will also be required to make some updates due to these breaking changes.

The SEO Spider provides an in-app warning, and advice in our Looker Studio Export Breaking Changes FAQ on how to solve it quickly.

The SEO Spider has been updated to integrate v3 of the Ahrefs API after they announced plans to retire v2 of the API and introduced Ahrefs Connect for apps.

This allows users on any paid plan (not just enterprise) to access data from their latest API via our integration. The format is similar to the previous integration; however, users will be required to re-authenticate using the new OAuth flow introduced by Ahrefs.

You’re able to pull metrics around backlinks, referring domains, URL rating, domain rating, organic traffic, keywords, cost and more.

Metrics have been added, removed and renamed where appropriate. Read more on the Ahrefs integration in our user guide.

Crawls are automatically saved and available to be opened or deleted via the ‘File > Crawls’ menu in default database storage mode. To date, the only way to delete database crawls was to delete them manually via this dialog.

However, users are now able to automate deleting crawls via new ‘ Crawl Retention ‘ settings available in ‘File > Settings > Crawl Retention’.

You do not need to worry about disappearing crawls, as by default the crawl retention settings are set to ‘Never’ automatically delete crawls.

The crawl retention functionality allows users to automatically delete crawls after a period of time, which can be useful for anyone who doesn’t want to keep crawls but does want to take advantage of the scale that database storage mode offers (over memory storage).

As part of this feature, we also introduced the ability to ‘Lock’ projects or specific crawls in the ‘File > Crawls’ menu from being deleted. If you wish to lock a single crawl or all crawls in a project, just right click and select ‘Lock’.

For project folders, this will lock all existing and future crawl files, including scheduled crawls, from being automatically deleted via the retention policy settings.

You can now set embedding rules via ‘Config > Content > Embeddings’, which allows you to define URL patterns for semantic similarity analysis .

This means if you’re using vector embeddings for redirect mapping , as an example, you can add a rule to only find semantic matches for the staging site on the live website (so pages from the staging website itself are not considered as well).

In the above, the closest semantically similar address can only be the staging site for the live site.

This can also be used in a variety of other ways, such as if you wanted to see the closest matches between two specific areas of a website, or between a page and multiple external pages.

It’s now possible to see all inlink and outlink relationships in our site visualisations .

You can right-click on a node and select to ‘Show Inlinks’, ‘Show Inlinks to Children’ of a node, or perform the same for ‘Outlinks’.

This will update the visualisation to show all incoming links, which can be useful when analysing internal linking to a page or a section of a website –

Linking nodes are highlighted in green, while other nodes are faded to grey.

This option is available across all force-directed diagrams, including the 3D visualisations.

Similar to site visualisations, you’re now also able to right-click and ‘Show Inlinks’ or outlinks within the semantic Content Cluster Diagram .

As well as viewing all internal links to a page, you can also select to ‘Show Inlinks Within Cluster’, to see if a page is benefiting from links from semantically similar pages.

This can be a useful way to visually identify internal link opportunities or gaps in internal linking based upon semantics.

Version 23.0 also includes a number of smaller updates and bug fixes.

Thanks to everyone for their continued support, feature requests and feedback. Please let us know if you experience any issues with this latest update via our support .

We have just released a small update to version 23.1 of the SEO Spider. This release is mainly bug fixes and small improvements –

We have just released a small update to version 23.2 of the SEO Spider. This release is mainly bug fixes and small improvements –

We have just released a small update to version 23.3 of the SEO Spider. This release is mainly bug fixes and small improvements –

Dan Sharp is founder & Director of Screaming Frog. He has developed search strategies for a variety of clients from international brands to small and medium-sized businesses and designed and managed the build of the innovative SEO Spider software.

For an in-depth proposal on our services, complete our contact form to request a proposal.

These are great additions, especially the visualization updates.

However, I’d really like to be able to apply custom filters in GA4 to view specific session sources. For example, I want to see sessions where the source contains a specific word (like Bing or ChatGPT) It would be great if you could add this functionality as well. Thanks!

Hot dang, the heading count is finally more than 2! I’m sure it’s been like that since I first started using the tool almost a decade ago. Everything else is great and all, but finally being able to see how many headings there are is really nice.

The crawl retention settings are exactly what I needed for quarterly site reviews—auto-delete old crawls.

#Irish Language Spelling & Grammar Support – Just for the craic!
