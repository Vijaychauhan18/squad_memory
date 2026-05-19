---
source: https://portent.com/blog/seo/developers-seo-guide.htm
title: A Developer’s Guide To SEO
scraped: 2026-04-20
tags: elite_article, seo, portent, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# A Developer’s Guide To SEO

Source expert/publication: portent
Source homepage: https://www.portent.com/blog/seo
Original URL: https://portent.com/blog/seo/developers-seo-guide.htm
Published: unknown

## Why This Matters
Discovered via XML sitemap during elite bulk backfill.

## Extracted Article Passages
- That means developers hold the key to SEO. It’s true. If you’re a developer and you’re reading this, laugh maniacally. You’re in control.
- For this article’s purposes, a developer connects site to database (or whatever passes for a database, don’t get all anal-retentive on me), builds pages using the design provided, and does all the work those two jobs require.
- A developer does not design. They do not write content. If you do all three jobs, tell the designer/content parts of your brain to take a break. This post isn’t for them.
- Viability: Stuff you do on the server and in early software configuration that readies a site for ongoing SEO.
- Mostly I chose this word because the other two ended with “ility,” and it just works.
- Server logs are an SEO source of truth. Log file analysis can reveal all manner crawler hijinx.
- And now someone’s going to tweet me their platform that, in defiance of all logic, doesn’t generate log files. OK, fine.
- Most servers are set up correctly out of the box, but just in case, make sure log files include:
- Why does everyone treat analytics like a light switch? Paste the script, walk away, boom, you’ve got data.
- Before you add that JavaScript, make sure your analytics toolset—Google, Adobe, whatever—can:
- Is this all SEO stuff? Not exactly. But it all helps the SEO team. Is this your job? Maybe not. But you’re on the Dev team. You know you’re the top of the escalation tree for everything from analytics data to printer malfunctions. When they can’t find the data they need, the SEO team will end up at your door.
- 301 : The resource you requested is gone forever. Poof. Look at this other one instead
- 302 : The resource you requested is gone, but it might be back. Look at this other one for now
- 50x : Gaaaahhhhh help gremlins are tearing my insides out in a very not-cute way. Nothing’s working. Everything’s hosed. We’re doomed. Check back later just in case
- Some servers use 200 or 30x responses for missing resources. This makes Sir Tim Berners-Lee cry. It also makes me cry, but I don’t matter. Change it.
- Even worse, some CMSes and carts come configured to deliver a 200 response for broken links and missing resources. The visiting web browser tries to load a missing page. Instead of a 404 response, the server delivers a 200 ‘OK’ response and keeps you on that page.

## Retrieval Use
- Use when the task maps to `portent` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

