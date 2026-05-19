---
source: https://www.searchpilot.com/resources/blog/how-we-did-an-emergency-https-migration-using-searchpilot-to-avoid-chrome-security-warnings-case-study
title: How we did an emergency HTTPS migration using SearchPilot to avoid Chrome security warnings [case study]
scraped: 2026-03-22
published_on: 2024-06-22T17:01:40+01
tags: live_feed, phase1_ingest, searchpilot, publication, testing, geo, archive_backfill, historical_source
topic: testing_and_experimentation
intent: research, monitoring, source_selection, testing
role: researcher, seo, pinchy, developer
confidence: medium
canonical: false
canonical_group: Archive backfill - SearchPilot Resources
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How we did an emergency HTTPS migration using SearchPilot to avoid Chrome security warnings [case study]

Source: SearchPilot Resources
Homepage: https://www.searchpilot.com/resources
Original URL: https://www.searchpilot.com/resources/blog/how-we-did-an-emergency-https-migration-using-searchpilot-to-avoid-chrome-security-warnings-case-study
Published: 2024-06-22T17:01:40+01
Strength: SEO testing, GEO experimentation, enterprise SEO workflows

## Summary
When Chrome 68 rolled out and highlighted any site not yet on HTTPS as insecure, it made it incredibly urgent for sites that had been putting off their migrations to get them done. One of our customers needed help to achieve this, and we used SearchPilot to remove the final blockers preventing their team getting this critical change live.

## Extracted Body
Getting changes made in enterprise environments is hard , even when there are clear financial impacts of not making the changes. Anyone who hasn’t migrated to HTTPS by this point, is aware of the need; it hasn’t happened yet because of insurmountable blockers like mixed-content warnings in hard-to-update back-end systems.

If this sounds like you, read on because the architecture of SearchPilot, deploying as a CDN, or between your CDN and origin, means that it’s agnostic to whatever server-side technologies you are using, and whatever CMS you have in place, so no matter what limitations your tech stack is imposing, SearchPilot can help get past these kinds of blockers and allow you to migrate quickly to HTTPS if you haven’t already done so. Get in touch if you want to learn more or see a demo of SearchPilot.

With the rollout of Chrome 68 highlighting all HTTP sites as not secure , there has been widespread press about some sites getting “flagged” (here is the BBC highlighting the Daily Mail in their headline and calling out half a dozen retailers by name ).

Sometimes companies behave just like the people that make them up. Most of us can remember a time when we’ve left that big piece of work until really close to the deadline, or even ended up starting work once it’s arguably a tiny bit too late. And businesses do the same - whether it’s shipping the GDPR-related privacy policy update on May 24th (yeah, ok, we did that), or fixing mobile-friendliness issues in a frantic mobilegeddon-related rush , what’s important is too often left until it becomes urgent.

In the case of HTTPS migrations, though, there are a range of reasons why it can actually be really hard to get them done in an enterprise environment. It’s common to have an organisational desire to get this done, but to have specific technical blockers. So, with the growing urgency coming from the external changes, we’ve been looking for ways to live up to our core values and effect change and get things done. In alignment with this, we recently got an urgent HTTPS migration done for a major retailer by using SearchPilot platform to mitigate a range of technical and on-page blockers. Here’s how:

One of the most common blockers to an HTTPS migration in enterprise environments is fixing mixed-content warnings where your newly-HTTPS pages rely on assets or scripts that are still loaded over HTTP. Even once you have your images (for example) also moved over to a secure hosting environment, you still need to update all the references to those images to use their HTTPS URLs.

By being able to do this site-wide, across all pages sharing a particular template, or on specific pages, we get the right blend of power and efficiency that enables a large volume of mixed-content warnings to be resolved in a short period of time.

There’s a variety of meta information that might need to be updated during the migration to HTTPS, but probably the most important is the canonical and hreflang information. SearchPilot can inject this information into pages where it’s missing (including into the headers for PDFs, for example), and update existing links to the new scheme.

Since canonical and hreflang links are poorly-handled by many CMSs, the power of being able to fix this “outside the system” is powerful and can be set up as a final check to ensure correct canonical links.

A critical part of the deployment of a migration to HTTPS is the 1-1 page-level redirects from HTTP pages to HTTPS pages. It’s common for this to be hard to manage, because you may well want to prevent your origin server from even responding to port 80 (HTTP) requests in the new secure world, which means your server can’t handle the redirects needed. We can serve them for you, and make sure that every request hitting your origin is port 443 (HTTPS).

It’s possible to set up redirect rules at the edge with a CDN, but our platform brings two main benefits over that approach (read more about edge SEO here):

Content Security Policy (CSP) headers are an important part of many HTTPS setups, and in particular, in risk-averse environments, you may well want to use a changing set of CSP headers to roll out HTTPS cautiously:

It can be difficult in many hosting environments to achieve this level of granularity, control, and agility with changes to headers, and SearchPilot can help with controlling them at the page, template, or domain level.

The architecture of SearchPilot, deploying as a CDN, or between your CDN and origin, means that it’s agnostic to whatever server-side technologies you are using, and whatever CMS you have in place, so no matter what limitations your tech stack is imposing, SearchPilot can help fix up these kinds of blockers.

If you are in an environment where you are blocked from getting important things done by a lack of agility for on-page and server configuration changes, we might be able to help. Drop us a line if you would like to see SearchPilot in action.
