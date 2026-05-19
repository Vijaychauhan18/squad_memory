---
source: https://searchengineland.com/yahoo-provides-noydir-opt-out-of-yahoo-directory-titles-descriptions-10631
title: Yahoo Provides NOYDIR Opt
scraped: 2026-03-23
published_on: 2007-02-28
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

# Yahoo Provides NOYDIR Opt

Source: Search Engine Land
Homepage: https://searchengineland.com/
Original URL: https://searchengineland.com/yahoo-provides-noydir-opt-out-of-yahoo-directory-titles-descriptions-10631
Published: 2007-02-28
Strength: industry coverage, rollout monitoring, search product and platform changes

## Summary
Yahoo! Search Support for ‘NOYDIR’ Meta Tags and Weather Update from the Yahoo Search Blog covers how at long last, you can now tell Yahoo to not use Yahoo Directory information to make a title and/or description for your web page listings. It also cover how Yahoo’s currently doing a reindexing change that might impact […]

## Extracted Body
Yahoo! Search Support for ‘NOYDIR’ Meta Tags and Weather Update from the Yahoo Search Blog covers how at long last, you can now tell Yahoo to not use Yahoo Directory information to make a title and/or description for your web page listings. It also cover how Yahoo’s currently doing a reindexing change that might impact rankings. More on that below, plus tips about also blocking the Open Directory information from being used for your pages and some possible conflicts with multiple robots tags.

Sometimes pages are listed in both Yahoo’s crawler-based search results and within its human-compiled directory, the Yahoo Directory . In those cases, Yahoo usually replaces the title and description of a web page in the crawler-based results with the information from the Yahoo Directory. Yahoo has operated this way for as long as I can remember — that’s over a decade :)

Now this has changed. Sometimes a site owner might not want the Yahoo Directory description to be used for their page. A case in point is Tony Knowles. The Yahoo Directory lists him this way:

Knowles, Tony (D) Democratic candidate from Alaska for U.S. Senate, 2004. www.tonyknowles.com

So when you search for him in Yahoo web search service like this — tony knowles — his listing comes up as so:

Tony Knowles Democratic candidate from Alaska for U.S. Senate, 2004 Category: Alaska > 2004 U.S. Senate Election www. tonyknowles .com – 15k – Cached – More from this site

The problem is, Yahoo’s directory information outdated. Knowles did run for Senate in 2004, but then he ran for governor of Alaska in 2006 using the same web site. During his governor campaign, this caused Yahoo to list him as a senate candidate, as I covered last year.

Now there’s a solution. By inserting this meta tag on any page:

You can ensure that Yahoo will not use a directory description it might have for that page.

The first tag tells any spider that wants to recognize the tag not to use a Yahoo Directory title or description. Of course, no other spiders do that — but Yahoo’s just building in some protection should that come up in the future. The second tag specifically tells the Yahoo spider not to use the information.

A related tag is the NOODP meta tag. Similar to how Yahoo works, various search engines have looked at the Open Directory Project to get information to make titles and descriptions of pages they also crawl. Pressure started building back in 2005 that site owners should be able to prevent Open Directory information from being used on their pages in this way. Last year, we saw all the major search engines do it except Ask. Instructions and dates of implementation for each are below:

That solved the ODP issue, but pressure remained on Yahoo to provide a fix for its own directory. Now that’s happened.

Back to the ODP. The tags to use to block the ODP are similar. Here’s the one to use for all spiders:

And if you wanted to block both the Open Directory and Yahoo Directory titles being used, you’ll need to do both of there:

<META NAME="ROBOTS" CONTENT="NOYDIR"> <META NAME="ROBOTS" CONTENT="NOODP">

Maybe. Then again, having two meta robots tags possibly might make a search engine choose one or the other, not both. You could be safe by using a tag for each specific spider:

<META NAME="GOOGLEBOT" CONTENT="NOODP"> <META NAME="SLURP" CONTENT="NOODP"> <META NAME="MSNBOT" CONTENT="NOODP">

But that’s a lot of unnecessary work, likely. Instead, I suspect that you really need to do something like this:

That’s consistent with the long-standing standard for the meta robots tag in general, as covered here . And if you’re already using the meta robots tag for other things, such as to block archiving (here are instructions from Google), you probably have to do this:

By the way, upper or lower case — it doesn’t matter. I’m also fairly sure that putting spaces after the commas like below works:

I’ll do some pinging to get answers to some of the questions above. While it’s great everyone has rolled out support to extend the meta robots tag, they’ve unfortunately not come together to answer clearly some of the questions I’ve raised above.

Postscript: I’ve asked Google, Microsoft and Yahoo the same three questions:

Contributing authors are invited to create content for Search Engine Land and are chosen for their expertise and contribution to the search community. Our contributors work under the oversight of the editorial staff and contributions are checked for quality and relevance to our readers. Search Engine Land is owned by Semrush . Contributor was not asked to make any direct or indirect mentions of Semrush . The opinions they express are their own.

Danny Sullivan was a journalist and analyst who covered the digital and search marketing space from 1996 through 2017. He was also a cofounder of Third Door Media , which publishes Search Engine Land and MarTech , and produces the SMX: Search Marketing Expo and MarTech events. He retired from journalism and Third Door Media in June 2017. You can learn more about him on his personal site & blog He can also be found on Facebook and Twitter .

Free technical audit shows what's blocking your search visibility.

1 Year → 1,000 Links: How Digital PR Builds Authority for SEO and AI Search

Blueprint for excellence: How leading agencies drive growth, prove value, and scale smarter

Third Door Media operates business-to-business media properties and produces events, including SMX. It is the publisher of Search Engine Land, the leading digital publication covering the latest search engine optimization (SEO) and pay-per-click (PPC) marketing news, trends and advice. The company headquarters is 800 Boylston Street, Suite 2475, Boston, MA USA 02199.
