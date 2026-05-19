---
source: https://www.seroundtable.com/archives/001059.html
title: Weighing the Time of a Link: Temporal Link Analysis
scraped: 2026-03-23
published_on: 2004-10-25
tags: live_feed, phase1_ingest, seroundtable, publication, daily-monitoring, archive_backfill, historical_source
topic: daily_monitoring
intent: monitoring, news, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Search Engine Roundtable
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Weighing the Time of a Link: Temporal Link Analysis

Source: Search Engine Roundtable
Homepage: https://www.seroundtable.com/
Original URL: https://www.seroundtable.com/archives/001059.html
Published: 2004-10-25
Strength: fast rollout monitoring, confirmation of changes, daily search news

## Summary
Dr. Garcia (aka Orion) over at Search Engine Watch forums created a thread named Temporal Link Analysis, which discusses a paper presented by IBM researcher Einat Amitay. This paper discusses the difference between how journal citation...

## Extracted Body
Dr. Garcia (aka Orion) over at Search Engine Watch forums created a thread named Temporal Link Analysis , which discusses a paper presented by IBM researcher Einat Amitay . This paper discusses the difference between how journal citation and Web IR citation. The basic premise is that the more often AND the more recent those citations are, the more important the journal is.

If we apply the concept of temporal link analysis to the much manipulated linkage structure of the current Web index, then we can possibly provide more relevant pages to the search user. To achieve this, the search engines would have to accurately capture time data in both the last update of the document as well as the last update of the link found within the document. Capturing this data is no easy task, nor is processing this information. But if it can be done, then the search engines can assign higher weights to more recent links as opposed to older links.

Why would you want newer links to be worth more? There are (generalizing here) two types of Web pages; (1) a page that is updated on a constant basis (be it daily, weekly, monthly) and (2) a page that is put up once and left there forever. Page number two, the one that is written once and left alone for ever, is by its very nature, outdated and irrelevant. The information, the links and the citations from this page launched in 1996 are most probably gone, misplaced or outdated. However if a page that was launched in 1996, but is updated on a monthly basis, contains links (i.e. citations), it can be assumed that this page is a "timely authority" and thus can be assigned a higher weight.

I was in the process of developing a small excel worksheet with the appropriate weights I feel should be associated with pages based on this paper, but I stopped. Instead let me just give you my thoughts in words, and you can argue. :) Pages that are old, but are not updated ever should be assigned a very low weight (possibly close to 0 weight). Pages that are new, and not updated (within a year or few months), should be given a higher weight then the old page that is not updated, however, this page is still not an authority, so it should be a relatively low weight (possibly close to .1). Now, pages that are new but updated often, relative to the data the page was first created (or found), should be given a higher weight then the above (possibly close to .2). And pages that are old and updated on a frequent basis relative to the date the page was first created, should be given the highest link weight (possibly close to .4).

Keep in mind, there are of course other factors. In the paper it discusses, DIPs (Dated Inline Profiles) where you associate a profile or community. You look at the dated inlink of a page, associated with a topic/concept/community to determine its value. Ok, I am stopping there. :)

The content at the Search Engine Roundtable are the sole opinion of the authors and in no way reflect views of RustyBrick ®, Inc Copyright © 1994-2026 RustyBrick ® , Inc. Web Development All Rights Reserved. This work by Search Engine Roundtable is licensed under a Creative Commons Attribution 3.0 United States License. Creative Commons License and YouTube videos under YouTube's ToS .
