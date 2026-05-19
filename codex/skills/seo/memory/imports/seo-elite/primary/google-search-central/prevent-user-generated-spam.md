---
source: https://developers.google.com/search/docs/monitor-debug/prevent-abuse
title: Prevent user-generated spam on your site and platform
scraped: 2026-05-18
tags: google, official, spam_policies, ugc, site_quality
topic: ugc_spam
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: UGC spam prevention, abuse controls, and quality-system hardening
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Prevent user-generated spam on your site and platform

Source type: official_doc
Original URL: https://developers.google.com/search/docs/monitor-debug/prevent-abuse
Page updated label: 2025-12-10 UTC

## Why This Matters
UGC spam prevention, abuse controls, and quality-system hardening

## Extracted Passages
- Spammers often take advantage of open comment forms and other user generated content inputs and generate spammy content on an unsuspecting victim site. Hosting platforms may be similarly open to abuse; spammers may create a large number of sites that violate our spam policies and add little or no value to the web.
- Preventing abuse on your platform or site is usually not hard. Even simple deterrents such as an unusual challenge users have to complete before interacting with your property may discourage spammers.
- Publish a clear abuse policy and communicate it to your users, for example during the sign-up process. Furthermore, allow trusted users to report content on your property that they consider spammy.
- Keep a record of signups and other user interactions with your platform, and try to identify typical spam patterns, such as:
- These signals may help you create a user reputation system, which can not only help you engage users, but it can also help identify spammers. Since many comment spammers want their content in search engines, consider adding the noindex robots meta tag on posts that come from new users that don't have any reputation on your platform. Then, after some time, when the user gains reputation, you can allow their content to be indexed. This will greatly demotivate spammers from interacting with your platform.
- Since oftentimes spammers are motivated by leaving a link to their site, consider adding a nofollow or ugc rel attribute to all links in untrusted content.
- Manual approval (or moderation) for certain user interactions can decrease spam on your platform considerably by preventing spammers to instantly create content that may be spam. Moderation adds overhead to your daily workflows, however it's a very effective way of fighting spam. Its efficacy is why, for example, comment moderation is a built-in feature in most CMSes.
- Once you find a single spammy profile, make it simple to remove any others. For example, if you see several spammy profiles coming from the same IP address, you can add that IP address to a permanent ban list. For CMSes (for example, WordPress), there are plugins like Akismet that can help, but adding the IP address to your firewall's deny list can be very effective also.
- In your sign-up form, consider using reCAPTCHAs or similar verification tools to only allow human submissions and prevent automated scripts from generating a lot of sites on your hosting service.
- Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

