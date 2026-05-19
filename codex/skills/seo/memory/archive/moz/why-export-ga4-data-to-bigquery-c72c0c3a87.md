---
source: https://moz.com/blog/why-export-ga4-data-to-bigquery-whiteboard-friday
title: Why Export GA4 Data to BigQuery?
scraped: 2026-03-22
published_on: 2026-02-13
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Why Export GA4 Data to BigQuery?

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/why-export-ga4-data-to-bigquery-whiteboard-friday
Published: 2026-02-13
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Unlock the full potential of your analytics. Dave Westby explains 8 key reasons to export GA4 data to BigQuery, from overcoming retention limits to fixing data sampling.

## Extracted Body
Unlock the full potential of your analytics. Dave Westby explains 8 key reasons to export GA4 data to BigQuery, from overcoming retention limits to fixing data sampling.

Click on the whiteboard image above to open a high-resolution version!

Hello and welcome to this edition of Whiteboard Friday. I'm Dave Westby, and I'm an analytics consultant at Piped Out.

So today, I'm going to be speaking about why you should be exporting your GA4 data to BigQuery if you're not already doing so.

Now the first thing to note here is that your GA4 data in BigQuery does not backdate. So if you set up that link between your GA4 and BigQuery, you'll only start collecting that data in BigQuery from today moving forward.

So moving on to the first key advantage, it's actually free to set up this link between GA4 and BigQuery. The thing that you do need, though, is a Google Cloud account, and what you pay for is the storage of this data.

But luckily for you, it's super cheap. So, as an example, if you have a website with 30,000 sessions a month, for example, the storage for this would actually be free. So it doesn't cost you dear.

So, coming on to the second point, you don't need to work with the GA4 interface when you're working with the raw GA4 BigQuery data.

A lot of the limitations that you have with the interface are actually solved by the fact that you're working with the raw data. So that's a great perk.

So coming on to the next point, which is data retention. So this is one of the biggest advantages of having your raw data in BigQuery. So with the raw data, you have that data stored forever. So that's great.

You just have access to it forever. Whereas with the interface, when you access any of the standard reports, it will use all-time data, which is fine. But if you segment it or you use Explorations, your user and event level data will be limited to 14 months. So that is a limiting factor there.

Coming on to the next point, which is sampling. So if you've worked with the GA4 interface at all, you'll be used to seeing sample data. The same applies as well for the GA4 Looker Studio connector as well, and that can be a real bummer.

And this happens basically when there are more than 10 million events within a single request. That's when your data starts getting sampled. Whereas, obviously, if you're working with your raw data, then you're not going to be having that problem.

Now moving on to the next point, which is cardinality. So this is when things get lumped under “Other.” Boo, no one likes it. This happens on the GA4 interface when you basically hit row limits. It just starts lumping everything under “Other.”

But again, when you're working with the raw data, you don't have that problem at all. So you can get far more granular with your data.

Then moving on to the next point, so customization. So working with the raw GA4 BigQuery data, you can customize your data however you like.

And this comes in really handy, for example, if you've got spam traffic that you want to remove, you can easily exclude that. You can fix historical conversions that are broken, and you can make your own conversions as well. So it's very customizable.

Then coming on to the next point, which is you can create your own sessions and user properties. Now you can do this in the GA4 interface under Explorations. But there are two main limitations here.

The first one being that you have to use Explorations, and the second is that you can only create dimensions. And when you've created these as well, these only live in your Explorations. You can't have these in other places, if you want to view them in dashboards or whatever.

But obviously, with the raw GA4 BigQuery data, you can create these properties, and then you can use them wherever.

So when you're working with the raw data, you can build all the attribution metrics however you like. So you've got your first click, your last click , your last non-direct click, linear times, etc. You can create all of those metrics, and then you've got access to them as well.

Then the final point is that you can combine your GA4 data far more easily with other data sources as well. So you can join it with your Search Console, Google Ads, or your CRM data as well. This just means you can get so much more out of your data.

So, just to wrap it all up, if there are only two things you take away from today, the first thing is that the export to BigQuery is free, and all you're paying for is the storage, which is extremely cheap. So it's definitely worth doing.

The second thing is that the BigQuery data does not backfill. So if you set it up today, you'll only start collecting that data from today onwards. So do it.
