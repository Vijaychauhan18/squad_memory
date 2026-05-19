---
source: https://moz.com/blog/what-is-index-bloat-whiteboard-friday
title: What is Index Bloat? — Whiteboard Friday
scraped: 2026-03-22
published_on: 2025-10-17
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

# What is Index Bloat? — Whiteboard Friday

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/what-is-index-bloat-whiteboard-friday
Published: 2025-10-17
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Deep dive into index bloat - a critical SEO challenge affecting medium to large websites. Learn how to identify URLs consuming your index quota without delivering traffic, understand the difference between crawl budget and index bloat, and discover practical solutions for cleanup.

## Extracted Body
Deep dive into index bloat - a critical SEO challenge affecting medium to large websites. Learn how to identify URLs consuming your index quota without delivering traffic, understand the difference between crawl budget and index bloat, and discover practical solutions for cleanup. This Whiteboard Friday video helps you assess your site's index health and implement effective remediation steps, from content consolidation to proper URL handling.

Click on the whiteboard image above to open a high-resolution version!

Happy Friday, Moz fans. Today I want to talk about index bloat.

So this is a pretty common problem affecting especially large, but also sometimes medium-sized sites. And I'd say this is definitely something that you should have looked into if you work for a medium or a larger site. It's definitely something you should have looked into at least once. It does affect a lot of sites. It's worth checking whether this might affect you. This is something that I and a lot of other SEOs have seen very good results with both for a long time and very recently. And despite that, it's something that I think is relatively poorly codified and talked about in the industry, there are some reasons for that which I'll come on to in a moment.

But before we get into all of that, I just want to explain this. So I put this diagram in just to give a bit of context, so that what I say next makes sense. So this outer box, this diagram as a whole is all of the URLs on your site, all of the URLs that might exist, that could exist, including parameters that no one has tried before, this kind of thing, the maximum possible set of URLs that would return a 200 response code and a valid page.

And then I've got smaller sets within that, sort of subsets of URLs. So the next one down is Google discovered URLs. So if Google has seen the URL – they might have not crawled it, they might have not indexed it, but they've seen the URL, they know it exists. That's sort of your next step down. And if you've got a big difference between the red box and the blue box, that probably indicates some kind of crawl budget problem. But that's not what we're talking about today.

If you've got a URL that's discovered, it might not necessarily be indexed. So indexed URLs is another smaller set. If you've got a URL that's discovered but not indexed, again there might be some reasons for that. Google might suspect that the page is unimportant based on other signals. You might have said not to index it. You might have shown them a noindex tag or something like this. So that, again, is a smaller set. Again, we're not necessarily speaking about that gap today.

And then you've got indexed versus pages with non-trivial traffic. Now what counts as non-trivial traffic to a page might vary from site to site. You might have your own idea of this. But a big gap between the number of URLs that are indexed and the number of URLs that are getting any kind of meaningful non-zero traffic, if that's a big gap, that would suggest an index bloat problem, and that's what I want to talk about today.

So before I get into that, just to make it totally clear, I want to quickly disambiguate a couple of things I mentioned there. So I'm not talking about crawl budget . As I mentioned before, that's when you've got a lot of URLs that Google just isn't going to crawl at all. Perhaps you're producing them too quickly. You've got a very large number, a huge number of URLs on your site. This might affect news websites, for example, sometimes large forums.

I'm also not talking about cannibalization . Now that is a related concept. Often when you've got a huge number of indexed pages that aren't getting traffic, it's because their topics are too similar. But you could theoretically have a cannibalization problem on a site with three pages, if they're all about roughly the same thing. That's not really what I'm talking about today. I'm talking about a larger-scale problem.

So we're specifically talking about the difference between the yellow and green boxes I talked about earlier. So how many of all the URLs that are indexed, are there a large number that Google is not really bothering to send any meaningful traffic to or show up in search results?

Why do we care? Why is that a problem? So what? I've got lots of indexed pages that don't get any traffic. What's the big issue?

Well, the first thing is that we have to theorize about how Google sort of treats these and why it behaves the way it does, and why we see the results we do. This is mostly based on experience within the industry. It's not something that Google has ever sort of codified for us. But we suspect that if you have a lot of pages that are receiving no traffic, that sends a quality signal , which might reflect on your site or certainly parts of your site as a whole. So if you have a huge number of pages that either are very thin, they've got nothing on them, or when you click through to them, they don't answer the question, they're a bit pointless, and you go back to search results, that could reflect on your entire site. So that could be part of the reason we care here.

The other is that, as I just mentioned, cannibalization, but also some other technical SEO problems. This can be symptomatic of other issues. If you're generating these large numbers of URLs on your site that are getting indexed, if we think about sort of Page Rank in a very old-fashioned SEO way, that's creating a lot of loss as Google sort of dilutes Page Rank across all of these pages on your site that could be consolidated into the pages that actually have potential to deliver traffic.

Some common causes we might have. So if we've got all of these URLs that are indexed and not receiving traffic, in a lot of sites that couldn't happen, right? If you have an editorial policy where you're constantly reviewing and creating pages based on demand, you would hope that this just wouldn't happen.

But on a lot of sites, it does happen, and there are two sort of groups of common reasons for that. This is just based on things that I've seen as a consultant in the past. One is if you have blogs or user-generated content, often you will end up generating a lot of thin pages on similar topics.

So I've worked on sites in the past where they'll have a blog where they post any kind of business announcements. They've hired a new member of staff. They've opened a new branch. They've won some kind of award. They had a Christmas party. Or any press release, anything like that goes on the blog, and you end up with this huge number of indexed pages, none of which were ever really designed to get search traffic in the first place.

And similarly, if you've got a forum section or something like this, users are going to do the same. They're going to generate threads about whatever they happen to be thinking about. Those will all get indexed. That can be a source of traffic, but it can also be a source of a lot of thin URLs on very similar topics.

The second sort of group to my mind is listings or products. So if you imagine a real estate website or a used car website or a job listings board, anything like this, a marketplace, you're going to get a lot of these pages that just come and go. A page is going to be created for a job listing. A couple of months later, it will be taken down. This is happening all the time. They're all pretty low value, very specific pages. Most of them will never get any traffic.

And similarly on an e-commerce site, on a big e-commerce site, you've got lots of individual products. Some of them are going to be extraordinarily long tail and realistically never get any traffic because they're too similar to some other page.

So in both of these cases, you can generate this very large number of URLs that are getting basically no traffic. So what might we actually do about this or decide whether we want to do something about this?

So the first step I would take is identify URLs which have near as dammit no traffic. And a rule of thumb I've often used in the past is are they getting on average less than one click a month or something like this? You can draw a very low bar. And on sites that are affected by this in a big way, you're still going to pick up a lot of pages that are getting literally zero traffic in most cases.

Remember, by the way, if you're looking at this from an organic lens, do check other channels as well. You don't want to accidentally remove something that it actually isn't really important to the social or email team or something like this.

Next up, improve any that are opportunities. So that's kind of a big catchall statement. But if some of these pages, that you identify, perhaps you used to get a lot of traffic but have become out of date or something like that, or you think they do actually have quality content on them, maybe there's a technical SEO issue that's holding them back, find any that are actually worth doing something with. Perhaps they might have a lot of links, for example. You don't want to just blanket wipe out this sort of latent value that you have. Do something with it if you can.

And then what's left, you've got this big bunch of pages that get zero traffic that you don't think are any kind of opportunity. So there's a few different ways you can go, and you're probably going to want to go and mix.

So anywhere you have either existing or potential pages that match the intent or are very similar, you're basically doing the same thing. So for example, if you've got one of these very specific product pages, but you've got a category page that's about basically the same thing, and the product is no longer in stock, then you could consider a canonical or a 301 . Obviously, a canonical if you still want that URL to be accessible, or a 301 if actually the page is totally redundant and you don't need anyone to see that anymore.

Again, this is if the intent and purpose and content of the page is going to be very similar. You could even if you think some of the content is worth consolidating, you could have that one page that you're consolidating to have the best of the content from all of the sort of component pages. And you could choose this to be a new or existing URL. You don't have to already have a good page. You could choose to make a new page that is really going to do well for this topic, rather than having all of these old pages, none of which were particularly worthwhile.

For anything where you really just don't serve this intent, it's redundant, it never had any value anyway, you can just 404 or noindex . Again, 404 if you don't need it to be accessible anymore. Noindex if you do, for example, it's used by another channel or something like this. This is quite an extreme step. I would try to avoid this if you can. Google isn't necessarily going to pass the full equity through a redirect or a canonical if the pages aren't a good match, but with a 404, they're definitely not. And with a noindex, eventually they're not as well. Google eventually stops crawling noindexes. So yeah, this is something you want to avoid. But realistically, there probably will be some pages that fall into this bucket.

So yeah, this is the sort of process I've followed myself in the past. It's something I've seen good results with. I've seen a lot of other SEOs speaking about this, especially in the wake of the helpful content update and in the past around Panda , which I think probably worked quite similarly.

So, yeah, let me know how you get on. And thank you very much.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

How does Google's AI Overview expand user queries? Tom Capper reveals 10 fan-out categories you can use to improve your prompt tracking and keyword research.

In this episode of Whiteboard Friday, Chloe Osunsami provides 3 simple steps for crafting a successful digital PR strategy in 2026. Join her to discover how to analyze competitors, find AI visibility gaps, and secure authoritative brand mentions.

Is your SEO strategy ready for LLM grounding? Explore the distinction between training data and live web retrieval, and discover how to optimize your brand's visibility in AI search results.
