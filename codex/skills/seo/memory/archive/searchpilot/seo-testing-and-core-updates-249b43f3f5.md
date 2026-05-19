---
source: https://www.searchpilot.com/resources/blog/seo-testing-and-core-updates
title: SEO testing and core updates
scraped: 2026-03-22
published_on: 2023-08-08T09:53:43+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# SEO testing and core updates

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/seo-testing-and-core-updates
Published: 2023-08-08T09:53:43+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
Broadly speaking, your organic traffic from Google can be affected by a few classes of thing: Something you do Something your competitors do A change in the market A change by Google

## Extracted Body
Broadly speaking, your organic traffic from Google can be affected by a few classes of thing:

That fourth point is one that practitioners in the SEO industry can obsess over, and it can itself be broken down in many different ways:

Updates to the SERP, or to rankings algorithms are generally fine with respect to SEO testing . The only real impacts are that you may want to re-run some tests in light of big changes. And sometimes you might want to deploy fixes in advance of the change even if you wouldn’t expect or they don’t show a positive result. But it’s point #4 above that I wanted to talk about with respect to testing.

Throughout this article, I’m going to be referring to a great piece of work by an ex-colleague of mine, Tom Capper, who wrote A Different Way of Thinking About Core Updates over on the Moz blog:

These days, Google algorithm updates seem to come in two main flavors. There’s very specific updates — like the Page Experience Update or Mobile-Friendly Update — which tend to be announced well in advance, provide very specific information on how the ranking factor will work, and finally arrive as a slight anti-climax. …

This post is not about those updates, though, it is about the other flavor. The other flavor of updates is the opposite: they are announced when they are already happening or have happened, they come with incredibly vague and repetitive guidance, and can often have cataclysmic impact for affected sites.

I have written my own thoughts on what differentiates core updates from other kinds of update within Google which I summarised as core updates are “retraining a massive deep learning model”

I've been thinking about Google Core Updates and why recovery from them can take until the next core update ( https://t.co/rWggDGhFJh ). Theory: core updates are retraining a massive deep learning model that is so hyper-fitted to the *current* shape of the web that... pic.twitter.com/Prq2dCVmoi

One implication if I’m right is that a given model may be so hyper-fitted to the current shape of the web that it may learn things like ‘site X is trustworthy’ so totally that even if site X changed its content entirely and started peddling nonsense, the (over?)fitted model would still deem it trustworthy. Until the next retraining (read: core update).

This matches experiences people have had in the other direction where improving a load of things that damaged a site’s performance in a core update don’t reverse the impact until the next core update.

It makes core updates weird for SEOs who are used to how things work today because batch updates are so at odds with the direction of travel of Google over the last decade which has almost uniformly been towards continuously integrating new signals. Those of us who have been around longer remember batch updates all the way back to the Google Dance, however, and many will remember the way that Panda and Penguin signals didn’t start out as real time elements of the algorithm.

3. Should you avoid testing because a core update might change the landscape? Not in my opinion - you might as well argue that you shouldn’t change anything or do any SEO because the world might change.

The challenge boils down to the way that a change made today might have no impact immediately but turn out to be beneficial (or the opposite!) at the next core update . In such a scenario, a controlled test might give an inconclusive result because the variant pages have not (yet) improved relative to the control pages, but the change was in fact a good idea and would, if deployed fully, result in a performance improvement at the next core update.

Luckily, we have a range of reasons to think that things are not this bad:

The first, and biggest, argument in favour of running SEO tests even though they may not catch all core-update-related effects is that many of the possible effects are not captured in the ranking algorithms only at core update time, and are detectable in the interim via SEO tests (as can be seen in our regular positive test results )

One of the distinguishing features of core updates compared to other, more opinionated updates, is that they are generally not changing the “kind” of thing Google is looking for in a high ranking web page. They are, in a sense “more of the same” or “more refined hunt for the same” and so our experience is that continual improvement informed by a stream of test results will move you in the right direction in between and among core updates even if they don’t always capture the effect of the core updates themselves.

In general, with core updates being “un-opinionated” (which explains why Google’s advice around core updates is so anodyne ), it’s natural for them to be aligned with other ranking factors. This means that the benefit of a winning test will tend, in the long run, to be greater than measured because there will eventually be the tailwind of core updates.

In Tom Capper’s article that I referenced above , he pointed out that of the sites that have seen a measurable impact from multiple core updates, the vast majority of them have seen a mixed set of impacts:

What this says to me is that the sequence of core updates is probably much more like Google “ tuning ” an algorithm than it is about directional changes. As such, I tend to agree with Tom (emphasis mine):

The biggest implication of thinking about Core Updates as refreshes is that you should, essentially, not care about immediate before/after analysis . There is a strong chance that you will revert to mean between updates. Indeed, many sites that lose in updates nonetheless grow overall.

The bold part is equivalent, in my mind, to saying that you should focus on the short-run impact of your changes (as long as they are aligned with users’ objectives - see point #4 below) and should not consider the impact of core updates too much in your thinking as you decide what you should or shouldn’t do to your website.

A couple of years ago, I published a version of an internal SearchPIlot memo that we call default to deploy which made the argument that:

When a test is based on a strong hypothesis , and yet our analysis is failing to reach statistical significance for our chosen level of confidence, we should make a consulting-style call on whether to recommend that the customer deploys the change to their whole site / section.

The existence of core updates (read as future events that will happen at unknown times but that will, in aggregate, over time, push Google’s algorithm closer to its stated objectives) suggests that in addition to positive tests that will stay positive and positive tests that will get more positive , there are probably some inconclusive tests that will eventually be a good idea after enough core updates have rolled out. Although SEO tests themselves can’t capture these, thinking this way is very aligned with our general approach of describing what we do as being “ business, not science ”. We want to take a pragmatic approach and consider the strength of our hypothesis and its alignment with Google’s objectives when considering what to do when we can’t immediately detect a beneficial result.

The fundamental risk here is mainly mitigated by aligning your ideation and hypotheses with what users want . As long as you do that, I’m inclined to expect progress that looks something like what Tom discovered for many sites that saw steady positive progress between core updates, took steps back at some core updates (the red bars) but won out overall (the blue line):

There are many things that could affect your performance negatively (or, more optimistically, positively) that are outside your control and more importantly outside your knowledge horizon as you are making decisions today. You just have to do the best with the information you have today. I would argue that running tests so that you have evidence that the things you are focusing on are positive in the short term is a very strong version of this and is the right way to make data-aware decisions in the context of a large site’s performance in search.

The short version is that in our experience, and based on the data we have seen, short term test results and the net impact of multiple core updates over time tend to be aligned. Theory suggests that positive tests will remain positive (and may even be more impactful than measured), and some inconclusive results will end up being a good idea which 100% aligns with our philosophy of “defaulting to deploy” when we are testing a hypothesis that is clearly aligned with users’ objectives but that comes up inconclusive.

We can mitigate the risks of being led astray by not using testing as a hunt for loopholes or a search for hypotheses that turn out to be positive in the short run despite being at odds with user experience and users’ objectives.

Beyond that, we ultimately have to accept an element of randomness in the impact of individual core updates as they come along and trust the process of aligning our ideation and hypothesis creation with our understanding of users, and making the best decisions we can. In my opinion, testing is the most powerful tool for doing just that and winning in the long run.
