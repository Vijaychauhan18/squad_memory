---
source: https://moz.com/blog/100-website-migrations
title: What I Have Learned From Conducting Over 100 Website Migrations
scraped: 2026-03-23
published_on: 2024-01-11
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# What I Have Learned From Conducting Over 100 Website Migrations

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/100-website-migrations
Published: 2024-01-11
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Conducting your first migration or looking to improve your workflow? Learn how to prevent issues and ensure success during website migrations

## Extracted Body
Picture this nightmarish scenario. The design team has just built a new, shiny website that everyone is mighty proud of. However, you wake up one morning, and 50% of your website traffic has vanished into thin air.

That's when the reality hits you that a visually appealing website redesign or CMS change can come at the cost of hard-earned traffic. Unfortunately, this scenario is too common, especially if you prioritize aesthetics over web traffic.

Avoiding this scenario is crucial to a website migration's success. While there are numerous advantages to a strategic migration, preserving existing traffic must be the top priority.

Drawing on my extensive experience with over 100 website migrations, you’ll learn essential steps to ensure a seamless, SEO-friendly site migration.

URL mapping is assigning new destinations for each page that currently drives traffic. While seemingly straightforward, this task is often a stumbling block in many migrations. For instance, a page you thought was unnecessary might be attracting significant traffic.

Google's bots won't be able to locate your old pages without proper redirect mapping, leading to traffic loss. For example, a page about ‘glassware’ may now be under a 'glasses' subfolder. Such changes, though clear to humans, are not obvious to search engine bots, causing you to lose traffic.

This happened when a client hired my team late in the migration process. A recruitment business had individual pages for each job location. After changing to a dropdown format for locations — similar to selecting clothing sizes on an e-commerce site, localized searches vanished, causing significant traffic loss.

After tracing the root cause of lost traffic, we attempted to reinstate these pages but had to start from scratch as our intervention came too late.

This issue is typical for e-commerce sites and can occur with varying severity. For example, discontinuing products like an old iPhone model without redirecting can lead to lost traffic. Redirect to an alternative product page if the original product is unavailable.

I'd recommend domain consolidation for international sites if you have multiple locations or websites hosted on different top-level domains (TLDs). Domain consolidation involves moving pages from various TLDs to one main domain, usually a .com.

However, each country’s page should maintain its unique identity, offering relevant products and information.

Avoid launching a site on a Friday. Typically, businesses do not have their development or web teams available over the weekend. If insufficient testing occurs, you could have a malfunctioning site for three days, not just 12 hours.

In one case, an incorrect phone number led to a private residence in Yorkshire, England, receiving all company calls over a weekend. This resulted in a very annoyed individual and many frustrated customers.

Ensure all internal links are updated from the staging domain to the live domain to avoid directing traffic to an inaccessible site. During the testing phase (also known as staging site), sites often have links that use a domain such as ‘staging.yoursite.com.’

When you transition to the live site, update all internal links. If the links are hardcoded, you could end up with thousands of links all pointing to a domain used for testing, which ideally shouldn't be accessible.

Misuse of JavaScript can hinder search engine discovery of pages. While it’s important to identify this issue during testing, sometimes you can find site URLs through crawling, even though it’s not the root of the issue. Hence, I always recommend some manual testing as well. I encourage you to read Moz’s detailed explanation of JavaScript issues .

Comprehensive benchmarking is the first step in a client migration. Crawl the current site, integrating Google Search Console and Google Analytics APIs, and analyze it using tools like Moz Site Crawl.

You can see each page's sessions, user clicks, impressions, and other important metrics. Also, examine a page's rankings and backlinks and create a comprehensive table with this data for every page on the site.

Based on this analysis, you can advise which pages to keep and which are no longer needed. This document is essential, and you’ll reference it throughout the migration process. Timeliness in producing this document is key. While preparing it a year before the go-live date may be excessive due to changes in traffic and new page additions, having it ready a few months in advance is highly beneficial.

Once the new site structure is known, all the new URLs are provided, or the site is ready in a staging environment, we can create the redirect map.

This stage involves understanding which pages attract traffic and backlinks. Depending on the agreement with the client and whether you're on a long-term retainer or this is a new project, you might also explore potential featured snippets and conduct keyword research, especially if you anticipate significant content changes.

Here, you ensure the site adheres to SEO best practices, particularly vital during design changes or CMS updates. You’ll also review wireframe designs, suggesting optimizations, like adjusting large above-the-fold images to ensure visible headers. Redirect mapping may also start here, although sometimes you could wait until the staging phase.

With the site in a staging environment, you can begin comprehensive crawling. I’ll advise you to conduct an initial review when 60 — 70% of the content is up and the templates are ready. Common issues like missing canonical tags or incorrect H1 settings are identified and should be fixed as early as possible.

Report your analysis and send the findings to the client or development team for implementation. Then, recheck the site. This iterative process continues until launch, focusing on correcting critical errors while minor ones can be addressed post-live.

The launch should be scheduled for the morning, avoiding Fridays. You'll want to clear your schedule for the day to thoroughly test the site immediately.

Immediate testing of the live site is essential to catch any new issues. It's also crucial to crawl the original list of URLs from the research and benchmarking phase to ensure they redirect to the intended destinations. This is an important step where you might identify potential errors. Next, provide initial feedback to the client on launch day, focusing on major issues and redirect accuracy.

Post-launch, monitor website performance meticulously. However, a few things to note include:

Slight drop in traffic before it starts recovering. As long as the recovery is on the horizon, it's generally a positive sign.

Create a list of smaller pending issues that still need to be addressed. Then, create a graph tracking how traffic evolves and identify pages where traffic hasn't transitioned as expected. This could be due to the removal of certain content sections. The decision of whether to reintegrate this content depends on the brand and its goals. Additionally, it's beneficial to provide a summary document to encapsulate the entire migration process.

Here are some valuable tips and tricks to navigate the complexities of migration projects:

The size of the site doesn't necessarily correlate with the complexity of the migration. Sometimes, a large site can transition relatively straightforwardly without major URL or design changes.

While it's ideal to have a flawless technical SEO report, minor issues such as overly long titles or temporary 302 redirects shouldn't halt the entire migration process. These can be addressed post-migration as part of regular maintenance.

Use the design and build stage to enhance the website's SEO. Address site architecture issues, meta structures, schema, and content edits you haven’t implemented. These are more likely to be pushed through because they make more fundamental changes.

I've been doing these migrations for a long time, but only one month ago, I was in a situation with a client where the URL structure had to keep changing due to niche technical issues.

As a result, I had to recreate the redirect mapping 14 times. You don't want to call all those documents something like “redirect_mapping.xlsx” or “redirect_mapping_revised.xlsx.” Instead, make sure it's versioned and dated, along with the staging testing, because you might have to do that multiple times.

While it's useful to test site speed in the staging environment, some optimizations, like text compression, may not be fully implemented until the live environment. The same rules will not always apply to staging environments, as developers do not need to implement them. Hence, look for broader speed issues in staging and conduct speed testing post-launch.

As you start a migration project, help your clients understand the potential downsides and the necessary steps. Use a standard migration walkthrough to demonstrate what could go wrong, emphasizing the importance of thorough planning and risk mitigation.

Remember that from an SEO perspective, the primary goal is to retain traffic. While enhancing traffic and conversion rates is possible, focus on maintaining current traffic levels. A steady traffic flow post-migration signifies success.

A useful tactic in discussions with clients involves redirect mapping. When you list out URLs to keep and those to remove, consider presenting a bar graph showing the estimated traffic loss if you discard specific URLs. This visual representation can be impactful, helping clients reassess the necessity of removing specific pages.

When working with staging sites, two preferred methods are password-protecting URLs or using IP blockers to restrict access. Avoid blocking sites with robots.txt or using a noindex tag on every page, as these can introduce more issues.

To see those who got it wrong, go to https://www.google.com/search?q=site%3Astaging.*.com

To measure the transition of traffic, compare traffic growth between old and new URLs. Blend data sources on Looker Studio and use tools like Google Search Console to track changes in URL structures and monitor traffic trends over time.

Filter for old URLs: Implement a filter for URLs with the old structure, such as ‘/glassware/.’

Filter for new URLs: Set up a filter for the new URL structure, like ‘/glasses/.’

No filter for overall traffic: Have another data source without filters to observe the total site traffic.

The result should be three-line graphs. Ideally, the top line graph, representing all traffic, remains consistent, indicating stable site traffic. The other two graphs should show a crossover pattern: the old URLs gradually decrease in traffic, while the new URLs experience a corresponding increase. This transition typically takes around six weeks but can extend over several months.

Having navigated over 100 website migrations, one of the most important lessons I’ve learned is knowing which battles to pick and understanding what can realistically wait until after the site goes live.

Furthermore, my experience in seeing the long-term impacts of minor mistakes has bolstered my confidence in decision-making. It's taught me to offer a calmer perspective during a stressful process. Finally, it’s important to embrace the uniqueness of each migration and strive for positive outcomes.
