---
source: https://moz.com/blog/helpful-content-update-not-what-you-think
title: The Helpful Content Update Was Not What You Think
scraped: 2026-03-23
published_on: 2024-09-05
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

# The Helpful Content Update Was Not What You Think

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/helpful-content-update-not-what-you-think
Published: 2024-09-05
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Raise your local SEO visibility with complete local SEO management.

## Extracted Body
Inspired by the Google leaks earlier this year, I’ve had a hypothesis that the HCUs (Helpful Content Updates) — part of Google’s core ranking system since March 2024 — are about something almost completely separate from Google’s messaging, and most SEOs’ tactical understanding.

In their original announcement in August 2022, Google wrote that this was a sitewide signal, but mainly affected by document-level factors intended to judge the helpfulness of content. Many SEOs, including myself, speculated that this might be a highly prescient first move against a new wave of LLM-generated spam. Google, through some complex machine learning methodology, was judging the subjective quality of content, or so we were to believe.

Googlers often hint that their search engine is simpler than we think, and my data backs this up. The HCU appears to be based, at least in part, on an older and simpler system. After studying the last three HCUs & post-HCU-merged Core updates from September 2023, March 2024, and August 2024, there’s something that demoted sites overwhelmingly have in common. Before we get there, though, a bit of scene setting.

Google has long been a little bit cryptic about major algorithm updates. Way back in 2011, with the launch of the first Panda update, Google said:

“This update is designed to reduce rankings for low-quality sites – sites which are low-value add for users, copy content from other websites or sites that are just not very useful.” - source

That could just about have been written to accompany a Core update in 2024. The impression in the industry is that over time, though, the reference to specific tactical information has gotten thinner and thinner, and we have heard more and more vagaries, or reference to things which many SEOs suspect have no direct ranking impact.

I have written in the past on this blog about how Core updates have become a bit of a Rorschach test. Hugely authoritative, high-quality sites go down as well as up, and basically no websites are consistently punished or consistently rewarded. Core updates behave more like a refresh — perhaps of short-term user signals or some other temporary data. They very likely have more to do with Google fiddling with the dials on their system than the changes panicked SEOs are making between updates.

So what, then, might the Helpful Content Updates be? They arrived with pretty similar vagaries to Core updates. Many high profile “losers”, though, seemed to match exactly what Google were saying they were hoping to reward . Then, in May this year, we had the leaks. Mike King, in his initial unpacking, speculated that something referred to as “babyPandaDemotion” might be the Helpful Content Update(s). He also linked this to a much earlier patent relating to branded or navigational search, which had been linked to the original Panda updates over a decade ago. This took me down a bit of a rabbit hole , as the concept of a navigational or branded query is central to Moz’s Brand Authority metric, which myself, Dr Pete, and others had been working towards for some years.

The hypothesis, then, is that the helpful content system has something to do with a suspect ratio of search volume for a site’s navigational terms, to its link signals. If you have lots of links (over-SEOd?), and not much navigational interest in your site, you probably don’t deserve to rank as well as it might look like you do. Happily, we’re in a pretty good place to assess that theory with data.

It’s become extremely difficult to do anything resembling a good winner/loser analysis on Google updates in all the above context. Not only are Google going back and forth on the same sites from one update to the next (making the definition of a “winner” a bit dubious,) but also updates usually arrive two at a time — HCU+Core, Core+Product Review, Core+bug, even not counting that Core itself contains multiple systems. Then there’s the generally high background fluctuation — whether it be Google updating their systems half a dozen times a day or more, or just your competitors launching campaigns that take away your traffic .

To mitigate this, I wanted to look at sites that had lost out, or won out, in successive Helpful Content Updates. Specifically, I defined losers as sites that met all of these conditions:

Reduction in top 10 ranking keywords between September 14th and September 28th 2023 (3rd HCU)

Reduction in top 10 ranking keywords between March 5th and April 20th 2024 (first merged Core+HCU)

These two reductions multiply to represent a drop in top 10 ranking keywords of at least 50%.

Increase in top 10 ranking keywords between September 14th and September 28th 2023 (3rd HCU)

Increase in top 10 ranking keywords between March 5th and April 20th 2024 (first merged Core+HCU)

These two increases multiply to represent a rise in top 10 ranking keywords of at least 50%.

To avoid too much pollution in the data, I also excluded all of the following:

Sites with <50 top 10 ranking positions at the start of any core update

54,537,783 top 10 ranking positions across four dates for said subdomains

August 30th - September 13th, 2023 (same duration as and immediately before 3rd HCU)

January 18th - March 4th, 2024 (same duration as and immediately before first merged Core+HCU)

Losers typically had a very different profile of BA, and BA:DA ratio, compared to winners.

HCU winners have a pretty similar profile of DA ( Domain Authority ) and BA ( Brand Authority ) to sites that saw no impact. This could mean that they were rewarded for something that isn’t captured by these metrics, or it could mean that search is a zero-sum game, and if someone goes down, someone must come up to take their place.

HCU losers, however, had markedly lower BA (37 vs. 50-52) and higher DA:BA ratios (2:1 vs. 1.4:1) than the sites that won or saw inconclusive movement.

To put this another way, for any given DA, we expect an HCU loser to have a lower BA than either other group. Or equivalently, a higher DA for any given BA.

That picture of similarity between the profile of neutral and winning sites also makes me think the HCU was likely a demotion or algorithmic penalty rather than a potentially positive factor.

This result stands up similarly with a variety of methodology changes. For example, if we restrict our analysis to the top 3 ranks gained/lost, rather than the top 10 ranks:

I also tested playing around with other definitions of winners or losers, or leaving in some of those very small/new sites I’d excluded — with similar results.

By contrast, if we look at sites that gained or lost during similar periods when there was no HCU rolling out, we do not see an equivalent effect:

Is Brand Authority a ranking factor ? No, of course not. It is a Moz metric. Google is not currently paying Moz for search data. We’re looking here at things which are correlated with what Google is doing.

Could it be that BA is correlated with the helpfulness of content? Yes, that’s quite likely. People do search out brands that they know have helpful websites. But I don’t think that explains the picture above — it would be quite an indirect causal link, and I wouldn’t expect it to be so clear-cut as what we can see here. Especially given the existence of a patent showing something very similar to a DA:BA ratio.

So, this is not conclusive. But to my mind it is pretty compelling — HCU was about the demand for your brand . That makes sense, given what Google is trying to do — what they have always been trying to do — in avoiding embarrassing search results, and showing people what they expect to see. It also aligns, potentially, with some other studies of “over-SEO-d” websites being hurt by these updates.

The current update completed on September 3rd, 2024. The data shared below is from that date - and I think captures all the movement of the update. If anything happens in the next few days that changes my view of that, I’ll post an update in this section.

That said, so far this update appears to be a partial reversal.

As with many core updates, this may leave affected site owners wondering why Google saw fit to crush their business for several months then essentially admit it was wrong. Perhaps even moreso, in this case, given how extreme some of the demotions were.

It’s only partial relief, too — if we compare the state of these sites now to how they were before the September 2023 Helpful Content update, generally speaking, it’s a very partial recovery indeed.

There are a few ways one could dangerously misinterpret my conclusions here.

Even if HCU is mainly a brand/demand signal, that doesn’t mean that you can ignore your content. There are plenty of other ways that Google rewards content that generates long clicks and satisfied users. Indeed, over time, this will be good for your brand, too.

Yes, I’m saying some of that remedial work that you’re doing between Google updates is not responsible for the recovery. That doesn’t mean it’s useless. It’s hard to predict when you will be rewarded for your efforts, but I am not negating the existence of SEO here.

Links are not negative, or worthless, to your SEO efforts. I’m saying that if you have a lot of DA, and no BA, you won’t benefit fully from the DA. The answer to this situation is to build your brand. It’s about balance.

Rather than negating any SEO practice, I want to add something that you might not consider part of SEO. Is it your job to build demand for your brand? Well, in part, yes - everyone in a business is working towards that in some way. Is it mainly your job? Perhaps not, but you should be encouraging your bosses and clients to invest in this area as a prerequisite for organic success.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

As keyword targeting continues to evolve, you may be wondering if exact-match keywords still matter. Learn how machine learning and NLP have shifted SEO from simple synonyms to complex semantic clusters. See the data behind how Google and Gemini interpret the meaning of your content.

Analyze early data from Google’s AI Mode in STAT. This study of 40,000 keywords reveals a mere 12% overlap with traditional organic rankings and explores how the verbose, text-heavy nature of AI Mode is shifting the search landscape.

What is ChatGPT's Atlas? Charlie Marchant explains OpenAI's new AI-powered browser, its "Agent Mode" capabilities, and the pros and cons of using it.
