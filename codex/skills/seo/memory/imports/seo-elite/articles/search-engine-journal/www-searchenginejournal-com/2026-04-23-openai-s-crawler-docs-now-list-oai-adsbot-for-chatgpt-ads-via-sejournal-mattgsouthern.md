---
source: https://www.searchenginejournal.com/openais-crawler-docs-now-list-oai-adsbot-for-chatgpt-ads/572861/
title: OpenAI’s Crawler Docs Now List OAI-AdsBot For ChatGPT Ads
scraped: 2026-04-24
tags: elite_article, seo, search-engine-journal, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# OpenAI’s Crawler Docs Now List OAI-AdsBot For ChatGPT Ads

Source expert/publication: search-engine-journal
Source homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/openais-crawler-docs-now-list-oai-adsbot-for-chatgpt-ads/572861/
Published: 2026-04-23

## Why This Matters
OpenAI's public crawler docs now list OAI-AdsBot, a bot that may visit pages submitted as ChatGPT ads to check policy compliance and ad relevance. The post OpenAI’s Crawler Docs Now List OAI-AdsBot For ChatGPT Ads appeared first on Search Engine Journal .

## Extracted Article Passages
- OpenAI's public crawler docs now list OAI-AdsBot, a bot that may visit pages submitted as ChatGPT ads to check policy compliance and ad relevance.
- OpenAI’s public crawler documentation now lists OAI-AdsBot, a bot that may visit pages submitted as ChatGPT ads to check policy compliance and help determine ad relevance.
- The entry sits alongside OAI-SearchBot, GPTBot, and ChatGPT-User on OpenAI’s crawler docs page , bringing the documented bot count to four.
- OpenAI states that OAI-AdsBot only visits pages submitted as ads and that the data it collects isn’t used to train its generative AI foundation models.
- Per OpenAI’s docs , OAI-AdsBot may visit an ad’s landing page after the ad gets submitted. The bot checks whether the page complies with OpenAI’s ad policies. It may also use content from the landing page to help decide when to show the ad to ChatGPT users.
- The bot identifies itself with the user-agent string Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-AdsBot/1.0; +https://openai.com/adsbot .
- OAI-SearchBot and GPTBot are both at version 1.3, per OpenAI’s docs. The crawler only visits pages submitted as ad landing pages, not the wider web.
- Data collected by OAI-AdsBot isn’t used to train generative AI foundation models. That keeps OAI-AdsBot out of GPTBot’s territory, which handles training data collection.
- It also keeps OAI-AdsBot separate from OpenAI’s other bots. OAI-SearchBot surfaces content in ChatGPT search, while ChatGPT-User fetches pages during user-initiated browsing, and OAI-AdsBot is limited to ad validation.
- OAI-SearchBot and GPTBot can be controlled independently through robots.txt. ChatGPT-User is user-initiated, and the company notes that robots.txt rules may not apply to it. The OAI-AdsBot entry doesn’t say how the bot treats robots.txt.
- OpenAI publishes IP range files for its three earlier bots at openai.com/searchbot.json , openai.com/gptbot.json , and openai.com/chatgpt-user.json . At the time of publication, no equivalent openai.com/adsbot.json file appears in OpenAI’s docs.
- Without a published list, verifying a real OAI-AdsBot visit becomes harder. User-agent strings can be spoofed, and the IP lists give you a way to cross-check for the other three OpenAI bots. For OAI-AdsBot, that cross-check isn’t available.
- OAI-AdsBot has two audiences. Advertisers buying placements on ChatGPT need the bot to reach their landing pages; otherwise, the ad may not validate. Anyone tracking AI bot activity in server logs gets a new user-agent to watch, one tied to paid inventory rather than search or training.
- Aggressive bot protection through Cloudflare, Akamai, or similar tools may block OAI-AdsBot before it reaches the page. That could create validation friction for advertisers who use strict bot-mitigation tools.
- ChatGPT’s ad program has moved fast since OpenAI started testing ads on Feb. 9 . As access opens up to more advertisers, OAI-AdsBot traffic will start showing up in more server logs. Watch for an eventual IP range file at openai.com/adsbot.json if OpenAI chooses to publish one. For now, the user-agent string is what you have to work with.

## Retrieval Use
- Use when the task maps to `search-engine-journal` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

