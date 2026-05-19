---
source: https://www.searchenginejournal.com/yahoo-mail-fixes-security-flaw-was-open-to-account-hijacking/476/
title: Yahoo Mail Fixes Security Flaw, Was Open to Account HiJacking
scraped: 2026-03-23
published_on: -0001-11-30T00:00:00+00:00
tags: live_feed, phase1_ingest, search-engine-journal, searchenginejournal, publication, industry-news, archive_backfill, historical_source
topic: industry_news
intent: monitoring, research, source_selection
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Search Engine Journal
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Yahoo Mail Fixes Security Flaw, Was Open to Account HiJacking

Source: Search Engine Journal
Homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/yahoo-mail-fixes-security-flaw-was-open-to-account-hijacking/476/
Published: -0001-11-30T00:00:00+00:00
Strength: broad SEO coverage, platform updates, practitioner commentary

## Summary
Yahoo Mail was open to hacker attacks due to a file size bug. ZDNet reports that a flaw in the Yahoo Mail system could have let attackers control victims'

## Extracted Body
Yahoo Mail was open to hacker attacks due to a file size bug. ZDNet reports that a flaw in the Yahoo Mail system could have let attackers control victims’ Yahoo accounts

Yahoo has fixed a bug in its Yahoo Mail email system that would have allowed attackers to seize control of users’ email accounts. This bug enabled attackers to take control of a user’s account by simply sending them a specially crafted email.

The security flaw, according to eEye Digital Security’s Drew Copley:

Allowed attackers to by-pass the Web-mail system’s Javascript filters. Any message exceeding approximately 100kb in length would not be analysed by the filter, which is meant to strip messages of any potentially malicious Javascript.

“A remarkable note about this bug is that no one seems to have found it before,” Copley’s advisory reads. “As far as anyone knows.”

SCRIPT [->a bunch of chars here [spaces are most stealth], the whole file size will be just about 100KB] [this causes the filter to not work… the code is then run automatically]

The pseudo-diagram above explains the scenario rather well. For whatever reason, Yahoo’s email filter simply does not work on files which exceed a certain range. This kind of software issue is relatively common. A remarkable note about this bug is that no one seems to have found it before.
