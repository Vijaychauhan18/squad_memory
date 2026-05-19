---
source: https://www.searchenginejournal.com/google-is-testing-new-bot-authorization-standard/573957/
title: Google Is Testing New Bot Authorization Standard
scraped: 2026-05-06
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

# Google Is Testing New Bot Authorization Standard

Source expert/publication: search-engine-journal
Source homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/google-is-testing-new-bot-authorization-standard/573957/
Published: 2026-05-05

## Why This Matters
Google is testing a cryptographic protocol for verifying bot traffic that could make unwanted crawlers easier to identify. The post Google Is Testing New Bot Authorization Standard appeared first on Search Engine Journal .

## Extracted Article Passages
- Google is testing an advanced cryptographic protocol for verifying bot traffic that may make it easier to isolate unwanted crawlers.
- Google is testing Web Bot Auth, an experimental protocol designed to help websites verify that automated traffic is really coming from the bot or service it claims to represent. The new protocol could give site owners a dependable way to separate legitimate automated traffic from bots that hide or misrepresent who they are.
- A new developer support page was published provide information on how to verify requests with the Web Bot Auth protocol, which is currently in an experimental phase.
- The new protocol is technically called the HTTP Message Signatures Directory. It’s a proposed technical standard designed to automate trust between web services. It helps websites recognize verified automated services without requiring each side to manually exchange security keys beforehand.
- The basic idea is similar to giving verified automated services a standardized way to present credentials. Instead of relying only on names, user-agent strings, or private setup between companies, the protocol gives websites a repeatable way to check whether an automated request can be verified. That matters because many bots can claim to be something they are not. Web Bot Auth does not decide whether a bot is good or bad, but it can give site owners a stronger signal about whether the bot is really the service it claims to be.
- The cryptographic part is important because it makes identity harder to fake. Today, a rogue bot can claim to be a legitimate crawler by copying a name or user-agent string. Web Bot Auth is designed to move beyond that kind of self-identification by giving websites a way to check whether an automated request matches the service’s cryptographic credentials.
- Under this protocol, a bot would need more than a label saying who it is. It would need to prove that identity in a way that a website can validate. That could give site owners a secure basis for allowing verified automated services while blocking bots that cannot prove who they are. The protocol does not automatically decide which bots should be allowed or blocked, but it could give websites a more dependable signal for making that decision.
- Cryptographic verification is what makes Web Bot Auth better than current bot identification methods. Instead of relying on signals that can be misrepresented, it gives websites a way to verify automated requests. That means recognition is based less on what a bot says about itself and more on whether its identity can be confirmed by cryptographic credentials.
- The proposed protocol will make it possible to distinguish between rogue bots that are impersonating trusted crawlers from the genuine bots from trusted services. This protocol is like a whitelist of what’s allowed which may make it easier to isolate untrusted crawlers.
- However, because this is an experimental phase, the “whitelist” currently only applies to a subset of traffic, such as the Google-Agent . Google is “not yet signing every request,” so a missing signature does not automatically mean a bot is rogue. Site owners are advised to continue using IP addresses and reverse DNS alongside the protocol to avoid accidentally blocking legitimate traffic that hasn’t migrated yet.
- The new standard replaces manual setup between websites and bots, crawlers, and other automated services with a three-step discovery process:
- Web Bot Auth could make bot verification easier to scale by reducing the need for manual setup between each website and automated service. It also gives automated services a more consistent way to stay recognizable when their security details change, which can help avoid broken verification over time.
- Google stresses that users should continue using existing standards such as user-agent IP-based bot verification, stressing that the standard itself is a proposal that is subject to change.
- We recommend that in addition to Web Bot Auth you continue relying on IP addresses, reverse DNS, and user-agent strings as we gradually roll out signed traffic.
- If you’re a developer or system administrator looking to allowlist our experimental AI agents, you can implement verification through the Web Bot Auth protocol:
- Nevertheless, the standard does aim to simplify bot identification and controlling bot traffic by using a cryptographic protocol that a rogue agent can’t spoof, provide insights into how bots are interacting with your traffic, and to build a better way to control the currently out of control situation with bot crawling.

## Retrieval Use
- Use when the task maps to `search-engine-journal` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

