---
source: https://searchengineland.com/google-features-volkswagen-which-happens-to-be-search-spamming-11132
title: Google Features Volkswagen, Which Happens To Be Search Spamming
scraped: 2026-03-23
published_on: 2007-05-03
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

# Google Features Volkswagen, Which Happens To Be Search Spamming

Source: Search Engine Land
Homepage: https://searchengineland.com/
Original URL: https://searchengineland.com/google-features-volkswagen-which-happens-to-be-search-spamming-11132
Published: 2007-05-03
Strength: industry coverage, rollout monitoring, search product and platform changes

## Summary
The Google Enterprise Blog recently featured the Volkswagen web site for using Google Enterprise search to power a new feature on the VW web site. As you can see, the Volkswagen home page has a huge search box in the middle of the page. Cool, right? Danny and I think so. As Danny was explaining […]

## Extracted Body
The Google Enterprise Blog recently featured the Volkswagen web site for using Google Enterprise search to power a new feature on the VW web site. As you can see, the Volkswagen home page has a huge search box in the middle of the page. Cool, right?

Danny and I think so. As Danny was explaining the news on the Daily Search Cast today, he noticed that the site loads the box up in Flash. Looking at the source code, he discovered hidden text! Yes, hidden text on a page that was featured by an official Google blog.

Here is the text that is clearly not visible on the page. It’s kept invisible using a special style called “invisibleContent:”

<div class=”invisibleContent”>Volkswagen of America presents U.S. vehicle information, pricing, incentives, deals, comparisons on Eos, GTI, Jetta, New Beetle, New Beetle Convertible, Passat, Passat Wagon, Touareg, Rabbit, R32 and the GLI with links to VW dealers, owner information, Volkswagen merchandise, and VW accessories. homepage, volkswagen, volkswagon, vw.com, home, landing, top, volkswagen.com, home page, home, top, back, VWofAmerica, Volkswagen of America, Volkswagon of America, VWoA, VWofA, volkswagon.com</div>

Google has guidelines against using hidden text. In fact, such use got a different car maker, BMW, banned briefly from Google last year. YADAC: Yet Another Debate About Cloaking Happens Again covers both of these points.

Even Google has violated its own rules. Back in 2005, text meant for internal indexing was showing up on public pages, causing one part of Google to file for a reinclusion request with another part of Google. From what Google said at the time in a WebmasterWorld discussion :

Those pages were primarily intended for the Google Search Appliances that do site search on individual help center pages. For example, https://adwords.google.com/support has a search box, and that search is powered by a Google Search Appliance. In order to help the Google Search Appliance find answers to questions, the user support system checked for the user agent of “Googlebot” (the Google Search Appliance uses “Googlebot” as a user agent), and if it found it, it added additional information from the user support database into the title.

The issue is that in addition to being accessed via the internal site-search at each help center, these pages can be accessed by static links via the web. When the web-crawl Googlebot visits, the user support system thinks that it’s the Google Search Appliance (the code only checks for “Googlebot”) and adds these additional keywords.

That’s the background, so let me talk about what we’re doing. To be consistent with our guidelines, we’re removing these pages from our index. I think the pages are already gone from most of our data centers–a search like [site:google.com/support] didn’t return any of these pages when I checked. Once the pages are fully changed, people will have to follow the same procedure that anyone else would (email webmaster at google.com with the subject “Reinclusion request” to explain the situation).

Postscript: The Google Enterprise blog updated us with a post telling us that they contacted the Volkswagen team and Volkswagen removed the hidden text from the page and placed them in the meta description of the code.

Search Engine Land is owned by Semrush . We remain committed to providing high-quality coverage of marketing topics. Unless otherwise noted, this page’s content was written by either an employee or a paid contractor of Semrush Inc.

Barry Schwartz is a technologist and a Contributing Editor to Search Engine Land and a member of the programming team for SMX events. He owns RustyBrick , a NY based web consulting firm. He also runs Search Engine Roundtable , a popular search blog on very advanced SEM topics.

In 2019, Barry was awarded the Outstanding Community Services Award from Search Engine Land, in 2018 he was awarded the US Search Awards the "US Search Personality Of The Year," you can learn more over here and in 2023 he was listed as a top 50 most influential PPCer by Marketing O'Clock.

Barry can be followed on X here and you can learn more about Barry Schwartz over here or on his personal site .

Free technical audit shows what's blocking your search visibility.

1 Year → 1,000 Links: How Digital PR Builds Authority for SEO and AI Search

Blueprint for excellence: How leading agencies drive growth, prove value, and scale smarter

Third Door Media operates business-to-business media properties and produces events, including SMX. It is the publisher of Search Engine Land, the leading digital publication covering the latest search engine optimization (SEO) and pay-per-click (PPC) marketing news, trends and advice. The company headquarters is 800 Boylston Street, Suite 2475, Boston, MA USA 02199.
