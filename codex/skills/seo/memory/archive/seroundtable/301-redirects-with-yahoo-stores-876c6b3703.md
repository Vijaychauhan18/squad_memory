---
source: https://www.seroundtable.com/archives/001147.html
title: 301 Redirects with Yahoo! Stores
scraped: 2026-03-23
published_on: 2004-11-16
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

# 301 Redirects with Yahoo! Stores

Source: Search Engine Roundtable
Homepage: https://www.seroundtable.com/
Original URL: https://www.seroundtable.com/archives/001147.html
Published: 2004-11-16
Strength: fast rollout monitoring, confirmation of changes, daily search news

## Summary
Yahoo! Shopping offers one of the easiest and quickest routes to setting up an online e-commerce store front. There must be thousands of Yahoo! Shops within the Yahoo network and then additional stores that tap into the network through...

## Extracted Body
Yahoo! Shopping offers one of the easiest and quickest routes to setting up an online e-commerce store front. There must be thousands of Yahoo! Shops within the Yahoo network and then additional stores that tap into the network through various feeds.

One of the major issues with a Yahoo! Store is the lack of flexibility when it came to configuring the server to handle certain requests. Nacho, a moderator over at SEW and the owner of MexGrocer.com , knows a thing or two about Yahoo! Stores. He posted a thread today named Yahoo! Stores finally offer 301 redirect , where he discusses how Yahoo! allows some additional flexibility in setting up 301 redirects.

However, if the solution Yahoo! provides does not meet your needs, then Nacho listed an addition work around. We set up a dedicated hosting account outside of Yahoo! because Yahoo! Webhosting would only allow one domain per account. We set up the server assigining an individual zone record for each domain as if it was their own site, here is an example:

zone "domain.com" { type master; file "/etc/namedb/primary/domain.com.db"; allow-transfer {imatest;}; notify yes; };

Then uploaded the .htaccess file to the root directory of each domain via FTP with the 301 redirects like so:

Then our robots.txt file so that the spiders send read to not index/follow 301, here is how:

User-agent: * Disallow: / Then you go to your registrar and change DNS primary and secondary to your new server. This usually looks something like this:

NS1.hositngcompany.COM NS2.hositngcompany.COM Then you wait for DNS to roll over and verify that spiders have done their work. If they haven't check for errors. For example, go type in one of your domains in the search box additional to the page title, spot the link and click on it. It should follow to the right location of the new domain. If it isn't go back and check everything one more time.

Finally, go back to the Store Manager and under Site Settings (all the way to the right), look for "Domain Names" and start deleting every additional domain you did a 301 redirect for. MAKE SURE YOU DON'T DELETE YOUR MAIN DOMAIN NAME (the one you did not do a 301 for).

The content at the Search Engine Roundtable are the sole opinion of the authors and in no way reflect views of RustyBrick ®, Inc Copyright © 1994-2026 RustyBrick ® , Inc. Web Development All Rights Reserved. This work by Search Engine Roundtable is licensed under a Creative Commons Attribution 3.0 United States License. Creative Commons License and YouTube videos under YouTube's ToS .
