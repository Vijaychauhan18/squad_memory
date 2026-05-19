---
source: https://www.screamingfrog.co.uk/blog/flying-blind-measuring-without-first-party-tools/
title: Flying Blind: Measuring Keyword Coverage on a Cluster Without First-Party Tools
scraped: 2026-03-25
published_on: 2025-10-06
tags: live_feed, phase1_ingest, screamingfrog, screaming-frog, publication, technical-seo, crawling, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Screaming Frog Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Flying Blind: Measuring Keyword Coverage on a Cluster Without First-Party Tools

Source: Screaming Frog Blog
Homepage: https://www.screamingfrog.co.uk/blog/
Original URL: https://www.screamingfrog.co.uk/blog/flying-blind-measuring-without-first-party-tools/
Published: 2025-10-06
Strength: technical SEO, crawling, site architecture, large-site workflows

## Summary
Most SEO audits today lean heavily on data from Google Search Console (or BigQuery), performance dashboards, or SEO suites. But what if you’re flying blind? This happens more often than you’d think: You’re onboarding a new prospect and they haven’t granted access yet. You’re reviewing a competitor site or a...

## Extracted Body
Posted 6 October, 2025 by Adriano Maggi in Screaming Frog SEO Spider

Most SEO audits today lean heavily on data from Google Search Console (or BigQuery), performance dashboards, or SEO suites. But what if you’re flying blind?

In these cases, we need to simulate a keyword coverage audit using only public tools and crawling software.

This is exactly what this workflow enables: a top-down clustering process based on Google Keyword Planner data, Screaming Frog SEO Spider crawls, and a bit of custom JavaScript.

No verified data? No problem, you can still make informed decisions.

This article is a guest contribution from Adriano Maggi , SEO Team Leader at WMR Group .

Before writing a single line of code or launching your crawl, take a step back. Ask yourself:

Start with Google Keyword Planner (or any keyword tool that gives you monthly search volume and query ideas). Build semantic clusters by grouping together keywords that belong to the same intent or subtopic. Try to avoid mixing too many intent types and keep the clusters tight and focused.

For this task, leveraging AI can do the heavy lifting. While AI tools aren’t perfect at fully automating clustering, if you perform a quick keyword research and clearly define search intents, you can quickly associate keywords to clusters using a well-crafted prompt or a easy/medium Python script. But hey, that’s a post for another day!

Finally, associate each cluster to a single canonical URL. This will be your target page, or in other words, the one that should comprehensively cover the cluster’s topics.

/farmaci.html → ["over the counter drugs", "otc medicine", "non-prescription drugs", etc.]

This mapping becomes your reference matrix: it tells the Screaming Frog SEO Spider what to look for and helps you calculate coverage later.

Once your keyword clusters are mapped to URLs, it’s time to test how well each page actually reflects its target queries.

The Screaming Frog SEO Spider allows you to run custom JavaScript extractors, a powerful but often overlooked feature. Instead of extracting static data (like meta descriptions or canonical tags), you can write a script in which you insert your defined keyword list and check whether those terms are present in the title, H1, meta description, and body content of the target URL.

This essentially turns the SEO Spider into a basic content audit engine, one that compares intent (your cluster) with reality (the actual on-page elements).

In your Screaming Frog export, you’ll end up with two useful columns: Keyword Coverage % and Missing Keywords .

These fields give you a quantifiable, actionable view of how aligned your content is with the topic it’s supposed to rank for, even without looking at traffic or performance data.

The beauty of this easy and basic method is that it scales easily with as many keywords as you want. And that’s crucial, because modern SEO is less about single-keyword targeting and more about ensuring full coverage across entire semantic clusters.

A query coverage check tries to reflect this shift. It moves us beyond the idea of optimising for individual queries and toward evaluating how well a page covers a broader search entity — a thematic topic that may span multiple SERPs and intents.

This approach gives you a fast, structured way to assess the on-page optimisation quality of the key pages in any domain. It is especially useful when you’re seeing a site for the first time during an audit or consulting project. By defining the keyword cluster yourself, you also control what kind of intent you’re analysing. You may focus on high-converting transactional terms, long-tail informational ones, or a mix – depending on your goals.

Ultimately, you decide whether to stick to exact-match phrasing or to simulate a broader query fan-out – something that Screaming Frog can support as well.

Below is the anonymised version of the custom JavaScript snippet used in this specific workflow example.

Once you’ve assessed keyword coverage on-page, the next logical step is to measure the potential impact of what’s missing.

Coverage alone tells you what is present or absent, but not how much it matters. Without traffic or performance data from Search Console, the most practical proxy for business opportunity is search volume. That’s where Google Keyword Planner comes into play: it provides the quantitative layer needed to prioritise gaps.

By enriching your dataset with monthly search volumes, you can begin to frame missing keywords not just as oversights, but as lost potential. This step brings you closer to understanding the real cost of poor alignment, helping you make smarter decisions when optimising or rewriting content.

At this stage, you’ve combined an initial qualitative check (keyword presence on-page) with quantitative data (search volume). Even without access to Search Console or Analytics, this allows you to derive meaningful SEO KPIs that can guide prioritisation and strategic decisions.

This stage turns a basic coverage audit into a business-relevant insight layer. It allows SEOs, strategists, or consultants to back up content decisions with clear, defensible data – especially useful during audits, pitches, or early-stage planning.

Understanding when your audience is searching is just as important as what they’re searching for. While many SEO workflows stop at average monthly volume, Google Keyword Planner goes one step further, offering granular monthly trend data that reveals real-world seasonality across your keyword clusters.

This layer of insight is especially valuable when you’re planning content updates, launches, or campaigns without access to performance data. Seasonality helps you prioritise not just what to fix, but when to act.

Bonus tip: you can automate this part in Google Sheets by calculating the peak month per row and surfacing it as a label (e.g. “Peak: November”), giving a quick filtering option for prioritisation.

Let’s say you discover that many of the missing keywords for your /farmaci.html page, such as “over the counter cold medicine” or “flu remedies without prescription” experience a significant spike in December. This seasonal increase likely correlates with winter-related health issues like colds, flu, and respiratory infections, which drive a surge in demand for non-prescription medication.

That insight alone already changes how you prioritise your SEO roadmap. Instead of treating this cluster as evergreen content, you now know it has a critical seasonal window . Now imagine this method applied to a blog section. By identifying a particular month is the peak of search volume, you can reverse-engineer your timeline. For this page, the month could be December, so:

This kind of data-driven seasonality insight moves you from reactive SEO to proactive planning . You’re not just fixing issues, you’re anticipating when the market is most ready to engage, and ensuring your pages are in peak condition right when it matters most.

Once you’ve mapped out the keywords your pages are not targeting – and tied those gaps to concrete search volumes – you can start putting numbers to your missed opportunities.

It’s no longer just a question of “are we optimised?” but rather:

It allows you to move away from vague SEO recommendations and toward quantified impact: ideal for stakeholder meetings, budgeting discussions, or consulting pitches.

In contexts where first-party data isn’t available (yet), it provides a compelling way to demonstrate early value and strategic direction, especially when trying to earn trust or unlock investment in SEO efforts.

This approach isn’t meant to replace the precision of Google Search Console, nor the depth of analytics tools and it doesn’t have to.

Instead, it fills a critical gap: for small websites, early-stage SEO projects, or audits where data access is limited, this method offers a practical, scalable way to evaluate keyword alignment at the page level.

By combining Screaming Frog’s Custom JS capabilities, Google Keyword Planner’s volume and trend data, and the flexibility of Google Sheets, you unlock a lean but powerful workflow.

It’s lightweight, modular, and scalable — perfect for quickly surfacing opportunities and building momentum in the early phases of an SEO engagement.

And hey, just imagine the value of this analysis once you’re able to merge your keyword cluster insights with real SEO performance data from Google Search Console, or even BI-level transactional data.

It opens the door to far more advanced use cases: predictive models, forecasting, and new ways to define SEO presence in this next era of search — one shaped by AI-powered results, AI Overviews, and soon, even AI Mode.

SEO Specialist with a strong interest in web development, Adriano designs strategies to make SEO the main driver of sustainable online business growth. He provides companies with advanced analysis by leveraging tools such as Python. At WMR Group, he contributes to the growth of digital projects for both startups and leading international companies across Italy and abroad.

For an in-depth proposal on our services, complete our contact form to request a proposal.

Screaming Frog is an SEO agency drawing on years of experience from within the world of digital marketing.
