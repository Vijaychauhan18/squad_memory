---
source: https://www.onely.com/blog/googles-two-waves-of-indexing/
title: Is Google's Two Waves of Indexing Over?
scraped: 2026-03-23
published_on: 2019-08-28
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Is Google's Two Waves of Indexing Over?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/googles-two-waves-of-indexing/
Published: 2019-08-28
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Last week Bartosz Goralewicz was invited to Google Zürich to meet with Googlers John Mueller and Martin Splitt and discuss JavaScript SEO, and he walked away with a whole new understanding of how Google renders and indexes websites.

## Extracted Body
Last week I was invited to Google Zürich to meet with Googlers John Mueller and Martin Splitt and discuss JavaScript SEO . Not only was it a fantastic experience, I walked away with a whole new understanding of how Google renders and indexes websites. Here are my three main takeaways from the discussion:

Want to know more about what Bartosz learned in his conversation with J ohn Mueller and Martin Splitt? Then check out “ JavaScript SEO is Dead, Long Live JavaScript SEO! “

This is the relevant transcript from the Google Webmaster Central Office-hours Hangout , as recorded on August 23, 2019. This hangout was hosted by Googlers John Mueller and Martin Splitt from Google Zürich. Onely’s CEO Bartosz Goralewicz was the invited guest.

Bartosz Goralewicz : What’s the factor, what’s the metric that [decides], “OK, this website goes into two waves, and this one isn’t”? So we see that quite a lot where JavaScript websites are not [indexed] within two waves. Maybe there’s not enough JavaScript or whatever. Actually, we have quite a lot of bots recently to play with that because we’re investigating that.

Martin Splitt: Do you want to answer that? Or should I answer that?

MS : These days two-wave indexing – or the two waves of indexing – play less and less of a role . So, basically, generally speaking, you may see a lot of websites that are not using JavaScript that are still going through basically two waves . And you might see some, you might see –

MS: No, so here’s the thing. Pretty much every website, when we see them for the first time, goes to rendering. So there’s no indexing before it hasn’t been rendered. And, there are certain heuristics, that, if we see after a while, like, oh, this page, actually, the renderer does not diff as much or doesn’t diff, it looks the way before, like, we get – so what happens –

MS: Right, we do a crawl, right, which means, yeah, let’s say you get a new domain –

MS: No, that’s not what we do. What we do is we do an HTTP request, and we get something back, right – some HTML, maybe it’s a barebone HTML and all it does is load the JavaScript and run the JavaScript. Then, this HTML that we got from the original HTTP GET request from the crawl, goes into rendering. Rendering runs JavaScript – boom! – a lot of content happens that wasn’t there before – so we’re like, aha! OK, so this needs to be rendered. BUT there is a heuristics that is very, very –

BG : So, you look at the difference between the initial HTML, and, then, if after rendering you see extra content?

MS: Yeah. And the interesting thing is that, so, what I want to make very, very clear because I talked to the team and I was surprised about this. I thought this was a lot more, this is still a lot, like, more frequently happening that we are going like: ”Oh, all right, we are gonna skip rendering.” It is not as frequently happening anymore. So, like, for many, many websites even if they do not run JavaScript, they might still go through the render phase , because it doesn’t make a difference as much.

MS : It’s cheap. It’s cheaper than the complexity that we infer, so, like, there’s very, very few cases, and the internals of that are very complicated, and I still haven’t fully, like, grasped what exactly triggers the heuristics –

BG : Because what we see is that there is quite a lot of JavaScript websites that never go through, like, two waves. And, there are some websites that go through two waves, like we, again, we don’t see really the difference. So one of the factors for you is, like, the difference between the –

MS : And I wouldn’t say that two waves of indexing are dead, but it’s definitely something that –

MS : They’re absolutely not, but it’s definitely – I expect, eventually rendering, crawling and indexing will come closer together . We’re not there yet, but I know the teams are looking into it.

MS : No plans, no deadlines, no road maps to be announced yet. But –

Not sure on how to troubleshoot JavaScript SEO issues? Book a discovery call with Onely’s experts today!
