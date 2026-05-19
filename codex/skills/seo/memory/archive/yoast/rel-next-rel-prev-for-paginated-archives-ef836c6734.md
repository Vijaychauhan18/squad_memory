---
source: https://yoast.com/rel-next-prev-paginated-archives/
title: rel="next" & rel="prev" for paginated archives
scraped: 2026-03-23
published_on: 2011-09-15
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

# rel="next" & rel="prev" for paginated archives

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/rel-next-prev-paginated-archives/
Published: 2011-09-15
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Google has started to use rel="next" and rel="prev" for handling paginated archives and posts, read how this affects you!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Google is once again showing why standards compliant building might be very beneficial for SEO. They have started to use rel="next" and rel="prev" , both part of HTML4 and HTML5 , to recognize archives and paged articles.

Google recently announced that it isn’t using rel=next/prev anymore . Our advice hasn’t changed, though. Yoast SEO will still take care of all pagination automatically as other search engines still use it to discover content.

A few years back, I was having a discussion with Nathan Rice, one of the developers of Genesis over how one should deal with paginated archives, eg. page 2 of my SEO category . In Genesis, there is the option to canonicalize the subpages back to the first page of an archive. I have said and will keep saying that I think that that’s the sole big SEO mistake in that theme.

Now, as it goes with these things, Google has just posted the solution . They’ve asked to add rel="next" and rel="prev" to paginated archives, so that they can distinguish them as a series and, quote:

Send users to the most relevant page/URL—typically the first page of the series.

Bingo! That’s what we want. The syntax is very simple. On https://yoast.com/cat/seo/page/2/ we should have a prev link pointing to the first page in the series and a next link pointing to the next page in the series, like so:

Now I think this should be added to WordPress core, but of course, it currently isn’t. We have some other related links in core right now, most of which are useless. In fact – with the exception of rel="prev" and rel="next" – they’ll be removed from core anyway . I’m working on a patch for that combined with the ticket to add this to core . I’ll probably need to combine that with the work Nathan and I were doing on canonical on another ticket .

For now though, I’ve added this functionality to my Yoast SEO WordPress plugin, so all you have to do is update to the latest version and you’ll be taken care of!

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

We care about the protection of your data. Read our privacy policy.
