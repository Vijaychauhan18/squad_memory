---
source: https://moz.com/blog/ways-google-rewrites-title-tags
title: 9.5 Ways Google Rewrites Your Title Tags
scraped: 2026-03-23
published_on: 2021-08-31
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

# 9.5 Ways Google Rewrites Your Title Tags

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/ways-google-rewrites-title-tags
Published: 2021-08-31
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
You may be feeling confused and more than a little frustrated after Google’s recent title rewrite update, but why is Google rewriting titles, and what can we learn from it? Dr. Pete explored over 50,000 tags to find out.

## Extracted Body
You’ve spent months crafting the “perfect” brand message, focus-grouping it to core demographics and psychographics, and lovingly/hatingly crafting hundreds of page titles. You wake up, grab your coffee, and fire up Google to admire your handiwork, only to see this:

You may be feeling confused and more than a little frustrated after Google’s recent title rewrite update, but why is Google rewriting title,s and what can we learn from it? I explored over 50,000 <title> tags to find out.

All of the data was collected from the MozCast 10,000-keyword tracking set on August 25, 2021, and compared to original title tags collected using Screaming Frog (we only attempted one collection, since these were third-party sites). Here’s a brief rundown:

You might be doing the math right now, realizing that 58% of the <title> tags we tracked were rewritten, and rushing to Twitter to express your outrage. Please don’t — at least not yet.

First, there are bound to be quirks, like cached <title> tags that don’t match the current site, sites that blocked or modified our requests, cloaking, etc. I suspect those cases are relatively rare, but we can’t discount them.

Second, “rewrite” is a tricky word, because it implies a meaningful difference between the original version and rewritten version. Of this data set, over 13,000 <title> tags were over 600 pixels wide, the physical limit of Google’s desktop display title. Over 7,000 showed simple (...) truncation. Google has been doing this for years. Here’s an example from October 2011 (via the Wayback Machine):

Are these really “rewrites” in any meaningful sense? To understand what Google’s doing, and how it differs from the past, we need to dig deep into the unique scenarios at play.

Google can only fit so much on one line. That limit has changed over the years, but the basic fact remains. In many cases, <title> tags are just too long, and that’s not always a bad thing or necessarily spammy. Here’s one example and its corresponding search result:

This is a wordy <title> tag and we could certainly argue the merits of academic vs. marketing copy, but there’s nothing inherently wrong with or spammy about it. It simply doesn’t fit the available space, and Google has to account for that.

Even prior to the recent update, we saw a less common variant of this scenario, where Google would truncate a title and then append the brand after the “...”:

In this example, Google truncated the tag with “...” but then re-inserted the brand. Note that the original pipe (|) was replaced with a hyphen (-).

More recently (and possibly beginning with the August 16th update), Google is truncating long titles without displaying ellipses (...) and, in some cases, taking the display title from other elements of the page. For example:

This text actually appears in the middle of the <title> tag, but it’s possible that it was extracted from somewhere else on the target page. I would argue that this is a pretty successful truncation that serves the search query (in this case, “Dodd Frank”).

This scenario tends to overlap with 1-3 — sometimes titles are too long and have clearly been stuffed with keywords. I can’t speak to anyone’s motivations, but here’s an example that seems pretty egregious:

Mistakes were made, etc. Interestingly, this rewrite seems to be pulled from an <H2> on the page, but an entire paragraph is wrapped in that <H2>.

This reminds me of that joke, “An SEO walks into a bar, grill, tavern, pub, public house…”. In this case, it appears that Google is taking the truncated title from the primary <H1> on the page. It’s hard to fault Google for rewriting either of these examples.

These extreme examples can be entertaining, but it appears Google has also made some significant changes around less-extreme situations where phrases are strung together with separators like pipes (|). Here’s one example:

While this <title> tag does appear over-optimized, it’s obviously a far less problematic example than the previous two. Google seems to be taking a dim view of pipes (|) in general with this new update. In our data set, over 10,000 titles with pipes were rewritten, and nearly 6,000 of those were below the pixel-width limit.

In some of these cases, the original <title> tags simply appear to be reflecting the site’s information architecture. Take this example from Zales:

While you could make an argument that echoing the site’s IA isn’t particularly helpful to searchers, there’s nothing spammy or misleading about this <title> tag. It appears Google may be getting too aggressive with rewriting delimited phrases.

For a while now, Google has been appending brand names to the end of display titles in some cases. Here’s one example:

We don’t know exactly what signals Google uses to make this call. It could be a function of brand authority or based on measuring some kind of SERP engagement signals. In the case of a high-authority brand like WebMD that’s only five letters long, this change may be beneficial.

What about long brand names, though? Consider the example below:

Here, Google has exchanged a naturally-sounding and relevant title for a combination of the <H1> content and the brand name. Unfortunately, the addition of the 27-character brand name severely limits the rest of the display title. Fortunately, across a few hundred brand name addition examples I reviewed, this appears to be a rare occurrence.

One surprisingly common occurrence since the August 16th update is when Google takes a <title> tag with the brand name at the end and moves it to the beginning. For example:

Here, Google has moved the brand name to the front, followed by a colon (:), and has also shortened “I.T.” to “IT”. This version (with “IT”) is nowhere to be found in the page source.

On occasion, Google seems to be doing the opposite, and moving a brand name at the beginning of the <title> tag to the end of the display title. Here’s one example:

Unlike the back-to-front move, I believe this example is actually a variant of scenario #3. Google appears to be truncating the <title> tag and appending the brand name to the end of it. The removal of the brand name from the front is probably an accident of truncation.

Channeling a bit of Goldilocks, sometimes your <title> tag is too long for Google and sometimes it’s too short. Here’s an example from a recipe result:

This one’s an odd duck (pun intended) — in addition to appending the brand name, Google has expanded the title, and that exact phrase appears nowhere in any major page elements.

Here’s an example where Google rewrote a brand-only <title> tag:

Again, this was pulled from an <H1> tag on the page. What’s unclear is whether Google is rewriting these titles because they’re too short or because they aren’t particularly relevant to the query space. This brings us to Scenario #8:

At this point we don’t really know the exact trigger for a rewrite, but it does seem like some titles are being rewritten because they aren’t a good fit to query intent. Sadly, dozens of pages in this data set still had some variant of “Home” as their <title> tag:

In the majority of these cases, Google is rewriting the display title as the brand name. Of course, “Home” is also potentially just too short. Here’s an example of a longer <title> tag where relevance might have come into play:

Putting aside the odd orphaned pipe (|) at the beginning, I’d argue that this <title> tag is generic marketing copy that doesn’t do much to inform searchers.

That last case led me down a bit of a rabbit hole, and I’m not sure if this is a sub-case of #8 or a separate phenomenon. There were about 700 cases in our data set where Google rewrote a <title> tag with the word “Best” in it to remove that word. Here’s another example:

Once again, Google pulled the <H1> from the target page, but the rewrite and the original <title> tag share very similar intent and format. It’s possible that Google is taking a dim view of superlatives like “Best,” but that’s only a theory at this point.

Note that there were over 3,000 <title> tags in our data set where “Best” did not get removed, but some of those were contextually important, like “Best Man Speech” or “Best Buy” (the electronics retailer).

I think we can probably all agree that “Must Do Super Fun Things to Do” is pushing the envelope. Again, we can’t really prove what specifically is triggering this rewrite, but the pattern here is interesting.

We saw some similar patterns around marketing terms like “cheap,” “official,” and “2021.” Here’s the kicker, though: in some cases, Google is taking <title> tags without superlatives and adding them back in. For example:

Here, Google took a perfectly nice <title> tag, and chose the <H1> that included both “Best” and “Bespoke” instead. This begs the question — are <title> tags with words like “Best” being rewritten because of specific content, or are they being rewritten because of other factors, like length or keyword-stuffing, that just happen to be correlated with that content?

We’ve long suspected that Google would rewrite some display titles in real-time based on their relevance (or irrelevance) to the search query. In Google’s explainer about the August 16th update, though, they stated the following:

Last week, we introduced a new system of generating titles for web pages. Before this, titles might change based on the query issued. This generally will no longer happen with our new system.

So, are we seeing any evidence of query-based rewrites after the August 16th update? One way to test this is to look for pages/URLs that rank for multiple keywords and show different display titles (even though, being one URL, they share a <title> tag). For example:

The first result appeared on a search for “department of corrections,” and the second result on a search for “prison inmate search.” While this seems interesting at first glance, these results were collected across two different locations (and probably two different data centers). When I attempted to reproduce this difference from a single location, I only got back a single (rewritten) display title.

In our data set, only 96 URLs showed multiple display titles and only one of those showed more than two variants. In every case I spot-checked from a single location, those variants disappeared. It appears that Google really has removed or dramatically reduced query-based rewriting.

There’s currently no way to tell Google not to rewrite your <title> tag (although this latest update has the industry buzzing for that ability), but we can use the scenarios above to develop a few guidelines.

Changing your <title> tags at scale is a time-consuming job and carries risk. Before you overreact, collect the data. Are your display titles even being affected? Are these changes impacting your click-thru rate or organic search traffic? Is that impact negative? Frankly, we also don’t know when and how Google might adjust this update. If you’re seeing serious negative consequences, then definitely take action, but don’t panic.
