---
source: https://searchengineland.com/openofficeorg-mia-in-bing-but-not-censorship-39004
title: OpenOffice.org Is MIA In Bing, But It's Not Censorship
scraped: 2026-03-23
published_on: 2010-03-29
tags: live_feed, phase1_ingest, search-engine-land, searchengineland, publication, industry-news, archive_backfill, historical_source
topic: industry_news
intent: monitoring, news, source_selection
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Search Engine Land
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# OpenOffice.org Is MIA In Bing, But It's Not Censorship

Source: Search Engine Land
Homepage: https://searchengineland.com/
Original URL: https://searchengineland.com/openofficeorg-mia-in-bing-but-not-censorship-39004
Published: 2010-03-29
Strength: industry coverage, rollout monitoring, search product and platform changes

## Summary
The home page of OpenOffice.org, the well-known Microsoft Office competitor, is missing from Microsoft’s Bing search engine. While it sounds suspicious, the problem has nothing to do with Bing itself — it’s a technical problem on OpenOffice.org’s end. Ian McAnerin noticed earlier today that OpenOffice.org doesn’t show up in Bing on searches for [open office] […]

## Extracted Body
The home page of OpenOffice.org , the well-known Microsoft Office competitor, is missing from Microsoft’s Bing search engine. While it sounds suspicious, the problem has nothing to do with Bing itself — it’s a technical problem on OpenOffice.org’s end.

Ian McAnerin noticed earlier today that OpenOffice.org doesn’t show up in Bing on searches for [ open office ] and [ openoffice.org ]. He wonders if Bing is “allowing its results to be unduly influenced by either money or corporate policy.” But, upon further digging with some help from SEL’s Vanessa Fox, that’s not the case.

To be clear: Pages from the openoffice.org domain do show up in Bing — a [ site:openoffice.org ] search proves that. But the home page itself is nowhere to be found.

It seems as though the problem is simply due to a technical misconfiguration on the openoffice.org servers. This issue is impacting Yahoo’s index as well as Bing’s. When you navigate to openoffice.org as a user, you see the home page as you should. If you change the user agent to Googlebot (Vanessa used the User Agent Switcher Firefox plugin ), you see the same nicely rendered home page.

However, if you change the user agent to either MSNbot or Yahoo Slurp, you see a 403 access denied error.

You can see this more clearly in the HTTP response from the server (using a tool such as the Live HTTP Headers Firefox plugin ). Accessing the page as Googlebot returns the following (shortened for space; note the 304 rather than 200 response simply because Vanessa had visited the page before as Googlebot):

How did the server get set up this way? Any number of explanations are possible. Sometimes this happens when the host notices overactive crawling from particular bots and blocks them. This is always something that a site owner who uses shared hosting should watch out for (as the result is that your site gets dropped from that search engine’s index). In this case, Open Office likely manages their own servers, but they may not be blocking Microsoft and Yahoo purposely. A piece of server software could have easily been misconfigured accidentally.

A Microsoft spokesperson tells us: “We’re reaching out to them now to try and resolve the issue.”

Contributing authors are invited to create content for Search Engine Land and are chosen for their expertise and contribution to the search community. Our contributors work under the oversight of the editorial staff and contributions are checked for quality and relevance to our readers. Search Engine Land is owned by Semrush . Contributor was not asked to make any direct or indirect mentions of Semrush . The opinions they express are their own.

Matt McGee joined Third Door Media as a writer/reporter/editor in September 2008. He served as Editor-In-Chief from January 2013 until his departure in July 2017. He can be found on Twitter at @MattMcGee .

Free technical audit shows what's blocking your search visibility.

1 Year → 1,000 Links: How Digital PR Builds Authority for SEO and AI Search

Blueprint for excellence: How leading agencies drive growth, prove value, and scale smarter

Third Door Media operates business-to-business media properties and produces events, including SMX. It is the publisher of Search Engine Land, the leading digital publication covering the latest search engine optimization (SEO) and pay-per-click (PPC) marketing news, trends and advice. The company headquarters is 800 Boylston Street, Suite 2475, Boston, MA USA 02199.
