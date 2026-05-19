---
source: https://moz.com/blog/helpful-content-update-lessons
title: The Biggest Lessons I Learned From the HCU So Far
scraped: 2026-03-22
published_on: 2025-07-16
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

# The Biggest Lessons I Learned From the HCU So Far

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/helpful-content-update-lessons
Published: 2025-07-16
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Struggling to recover from Google's HCU updates? Learn data-backed strategies to protect your site by understanding topical radius and helpful content signals.

## Extracted Body
Google’s Helpful Content Update (HCU) has dominated SEO and content strategy discussions since 2023. Yet despite the attention, both Google and industry experts offer advice that remains vague and difficult to translate into clear strategies that protect your site.

Google tells us to write “helpful content,” but never defines what that actually means.

In my work, researching site data, I have observed two behaviors. First, HC appears to measure "unhelpful" content on sites in multiple ways. Second, the data shows that content earns unhelpful tags based on how topically aligned it is with other pages across a site.

Content writers market their services to write within HC guidelines. But that’s not possible because writers focus on a single piece of content while HC evaluates every page as part of a larger topical group. Ultimately, you are the guardian of your domain, not the writer.

Since August 2021, I have been running daily indexation tests. I did not set out to study HC updates in 2021, but I found that something shifted sharply in December 2022: Google stopped indexing and serving content it previously would have indexed and served.

On December 5, 2022, a standalone HC update rolled out, and the Indexing API that controlled bot behavior altered its bot pattern. This coincided with a steep drop in content indexation rates.

So I began to test various factors. When I topically themed test site content, indexation rates dramatically increased from 63% to 94% for 1st pass and 68% to 88% for JavaScript. [ Source ]

Data strongly implies that HC isn't like other updates , which evaluate individual pages in isolation. While reminiscent of the 2011 Panda Update, due to its sitewide impact, the HC update goes far beyond targeting thin spammy content.

Evidence from my test results and observations indicate that Google now evaluates every page as part of a topical group within the domain.

This evaluation compares the topic of new content against all other pages on the site. When HC finds pages with topical distances that are too far or too close to other existing pages, it assigns an "unhelpful" tag that eventually suppresses the visibility of those pages.

Documentation supports this understanding of HC. The April 2024 API documentation leak revealed that Google refers to a "siteFocusScore," a "siteRadius," and "siteEmbeddings" pages: "In plain speech, Google creates a topical identity for your website, and measures every page against that identity." [ Source ]

Yes. News sites can be and are served. News sites have no singular topical focus, not even under a general news topic.

How could Google measure the topical radius of a domain composed of news articles covering innumerable world news topics?

Given the lack of evident HC impact on news sites, it appears that these sites contain more “helpful” content. But could it be that they are exempted from it?

I believe it did because during the summer of 2023, large enterprise news sites that syndicated their original content through self-canonicalized RSS feeds to other publishers began facing indexation issues. Published pages started disappearing from search results within hours of posting. [ Source ]

Shortly afterward, question boxes popped up in Search Console (SC). This led many to conclude that Google couldn’t categorize or identify news sites based solely on their website data.

Google has never explicitly stated that news sites are exempt from HC. Yet, other evidence, such as a manually enforced Site Reputation Abuse (SRA) penalty, suggests that this exception from the HC classification process is necessary.

Based on a topical radius measurement in the API documentation, HC doesn't assess a site solely on the representation of a single page but rather on the specific collection. Google explained, "The signal is also weighted; sites with lots of unhelpful content may notice a stronger effect." [ Source ]

With this information, I concluded that a site's structure and content determine whether the site will be affected. The following are features that can potentially impact topical radius measurements.

Domains are vulnerable when they cover multiple topics that humans can connect mentally, but lack a mathematical “topical bridge” in their content that Google can recognize algorithmically.

For example, our brains can easily connect dog beds with dog health insurance or, buying a home to live in, with purchasing a house to flip as an investment.

However, the HC system cannot make these connections without assistance. The topic boundaries it expects are determined mathematically by what already exists on our sites. To bridge these topics for HC, those connections must be present within the content.

“Old school” SEO methods that create multiple pages targeting an identical query have caused many sites to lose visibility since the September 2023 HCU.

Multiple pages on the same domain targeting the same query now lead to a decline in visibility, even if they aren’t exact duplicates.

In such consults, these pages were indexed in Search Console data, but only one page out of the group was served in search results for the query. It is not uncommon for multiple pages on the same "topical node" to disappear and no longer be findable by their keywords.

Even if one page continues to appear in results, having enough similar “unhelpful” content leads to site-wide suppression.

Duplicate content (i.e., multiple URLs leading to exact word-for-word content) has never been beneficial. In the age of HC, it is proving to be existential.

Repeatedly, in my private consultations, data for sites using Table of Content (TOC) anchor links in their articles demonstrate sharp drops in impressions, clicks, and rankings.

When I read public social media posts where site owners posted their domains using SEO tools with historical data, the sites that used TOC links saw drops in visibility. These drops were present across the board from large enterprise sites (like Hardbacon ) to affiliate bloggers.

All sites I've observed using TOC have a declared canonical meta tag . Those to which I had Search Console access revealed that anchor-text URLs suddenly gained impressions and positions, but not in overall clicks.

Just as suddenly, those jump-link URLs disappeared from the data while the site went on to flatline in visibility. Often, data demonstrated that anchor-text URLs outrank their canonical URL for multiple terms.

The only logical explanation is that HC scores every URL with a hashtag (#) as a separate page unrelated to the canonical. Thus, it creates a false and damning narrative of duplicate content on the domain.

When measuring topical radius, judging each # URL separately creates a double whammy of multiple pages answering the same query and replicating each other word for word.

At the latest Google Creator Summit in Washington, DC, Google addressed table of content. According to one participant, in a private setting (no cameras allowed), Google shared that "some Table of Content widgets can confuse their crawlers and even reduce clarity scores." [ Source ]

There is a reason why Google must enforce Site Reputation Abuse (SRA) as a manual penalty, and manual enforcement supports the contention that news sites are exempt from HC, since many news sites appear to have received penalties.

If HC were used algorithmically on news sites, due to the topical nature of HC's assessing a collection of pages on the domain, HC could single-handedly decimate the online news industry within 48 hours.

To rein in enterprise news sites, which may have surmised they were granted some form of algorithmic protection and began to move their full power and authority into affiliate offerings, Google was forced to manually enforce the spirit of HC.

By exempting a site type from HC constraints, Google created a situation they had to control, and yet not destroy enterprise news organizations to accomplish their goal.

At the May 2025 private Google Creator Summit, "Google admitted upfront that they know their system has favored larger sites. They didn't mean to, but that's how the algorithm evolved." [ Source ]

I believe this is exactly how it evolved: Google operates with two sets of rules, depending on whether they consider your site a news site or not.

What follows is an extreme example of a site repeatedly slammed with HC updates. This site was devastated by the September 2023 HC update and continues to be overwhelmed to this day.

The Search Console data below, gathered over the last 18 months, illustrates clicks, impressions, CTR, and average position. Every page contained TOC links; some had as many as 17 chapters.

For blogger and affiliate sites that are TOC-dependent on most of their pages, dramatic drops in visibility (impressions) appear to result from their anchor URLs being scored as separate pages, creating a false assessment of duplicate content. These sites may inadvertently cover more topical ground that would not have fared well with HC.

Aggregate views of Search Console data clearly reflect the damage of the helpful content system and, at the same time, also obscure the ability of SEOs to recognize its cause.

Below is an example of a single canonical URL compared to a single anchor-text URL of a TOC URL ranking for the same search phrase on the same day.

Given that both URLs ranked in the same position on the same day for the same search phrase, we can reasonably infer that the resulting ranking for an identical position for a similar keyword phrase indicates an exact score match by Google's ranking and scoring system.

These pages are identical; they are just different URLs with matching content. The following screenshot displays in numbers what duplicate content on the same domain looks like.

The same data reveals that, shortly after this date, impressions and the position of the anchor#1 URL are no longer reflected in the data. Once it disappeared, the canonical URL dropped in impressions and position.
