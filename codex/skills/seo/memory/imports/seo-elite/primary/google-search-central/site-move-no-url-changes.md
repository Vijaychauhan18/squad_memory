---
source: https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes
title: Changing your hosting
scraped: 2026-05-18
tags: google, official, hosting_migrations, dns, crawl_rate
topic: hosting_migrations
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: hosting moves, DNS changes, crawl-rate expectations, and migration risk reduction
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Changing your hosting

Source type: official_doc
Original URL: https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes
Page updated label: 2025-12-10 UTC

## Why This Matters
hosting moves, DNS changes, crawl-rate expectations, and migration risk reduction

## Extracted Passages
- Follow this guide to minimize the impact of changing your site's hosting infrastructure on the site's performance in Google Search. A change in hosting infrastructure means switching hosting providers or moving to a content distribution network (CDN). This guide is only for migrations that don't affect the user-visible URL.
- First, upload a copy of your site to your new hosting provider. What a "copy of your website" means depends entirely on your old content management platform; it may be actual HTML files that you replicate on your new hosting platform, or a database export that you have to import in the new location. Once you do that, verify that it works as expected by thoroughly testing all aspects of how your users interact with your site. Here are a few suggestions:
- If you don't already have a Search Console account, create a new account for your site to help you monitor Google access and traffic. If you created a temporary hostname for your new site, verify that property as well. Check that Googlebot can access your new infrastructure using the URL Inspection Tool in Search Console.
- You can help make your site move go faster if you lower your site DNS records' TTL value, which will allow the new settings to propagate to ISPs faster. DNS settings are usually cached by ISPs based on the specified Time to Live (TTL) setting . Consider lowering the TTL to a conservative low value (for example, a few hours) at least a week in advance of the move to refresh DNS caches faster.
- If you're using the HTML file method to verify ownership of your site in Search Console, make sure you don't forget to include your current verification file in your new copy of the site.
- Likewise, if you include in your content management system's (CMS) templates a meta tag or Google Analytics to verify ownership, ensure the new CMS copy includes these as well.
- When you change hosting infrastructure, it's normal to see a temporary drop in Googlebot's crawl rate immediately after the launch, followed by a steady increase over the next few days, potentially to rates that may be higher than before the move.
- This fluctuation occurs because we determine crawl rate for a site based on many signals, and these signals change when your hosting changes. As long as Googlebot doesn't encounter any serious problems or slowdowns when accessing your new serving infrastructure, it will try to crawl your site as fast as necessary and possible.
- Check the server logs on the old provider and, once the traffic to the old provider reaches zero, you can shut down your old hosting infrastructure. This completes the hosting change.
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

