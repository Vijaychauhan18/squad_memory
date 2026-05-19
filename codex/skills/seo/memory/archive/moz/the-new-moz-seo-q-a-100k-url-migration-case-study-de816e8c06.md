---
source: https://moz.com/blog/moz-qa-migration-case-study
title: The New Moz SEO Q&A: 100K URL Migration Case Study
scraped: 2026-03-23
published_on: 2021-08-16
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

# The New Moz SEO Q&A: 100K URL Migration Case Study

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/moz-qa-migration-case-study
Published: 2021-08-16
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Over time, the Moz Q&A saw serious neglect, resulting in loss of user satisfaction and traffic. So Moz had a choice: improve the Q&A immediately, or kill it. Thankfully, we chose to improve it. Here’s how we did it.

## Extracted Body
Should you always expect a traffic drop during a site/URL migration, even a temporary one?

In case you didn't notice, Moz recently launched a shiny new SEO Q&A platform for all the world to see, explore, and use to learn about SEO.

Originally launched as a private feature for Pro members many years ago, the Q&A was opened for public — and search engine — viewing back in 2011.

In the years since, it grew to over 60,000 posts covering every SEO topic imaginable, and tens of millions of page views. For a long time, a significant portion of Moz's organic traffic came from the Q&A.

Sadly, though, as often happens, over time the Q&A saw serious neglect. As a result:

The platform accumulated a ton of technical debt , making it nearly impossible to update

So Moz had a choice: improve the Q&A immediately, or kill it.

Working with the fantastic team at NodeBB (highly recommended, by the way), we quickly spun up a new Q&A using our existing database, but with entirely modern technology on the front and backend.

We were under intense time constraints . What might normally take months, we needed to accomplish in a couple of weeks. This presented unique challenges from an SEO perspective.

The biggest challenge? Our entire URL structure needed to change. (If we had more time, we could have avoided this, but it was a luxury we didn't have.) That meant we needed to migrate thousands of URLs that looked like this:

Old : moz.com/community/q/how-long-will-it-take-to-reach-da-2

New : moz.com/community/q/topic/69872/how-long-will-it-take-to-reach-da-2

The migration also included all of Moz's user profiles, which number in the hundreds of thousands . To be fair, most of the user profiles aren't actually indexed.

The other potential red flag was that most of the Q&A would use client-side rendering — not considered a best SEO practice! We could've implemented a solution for server-side rendering, but again, we simply didn't have time. We were concerned Google would have trouble rendering the content, and this might tank our rankings (more on this later.)

To pull off this huge migration while minimizing the risk of traffic loss, we followed basic SEO site migration best practices , along with a few "special" extras for an added boost.

To put it simply, how you implement your 301 redirects is either going to make or break your migration implementation.

For us, this was actually the easiest, most straightforward part of the job, as we have a lot of experience with site migrations ! (Does anyone remember seomoz.org?)

We made a list of every possible URL and URL path. It's amazing how many URLs and patterns you might miss. A good crawler is essential to help with this to make sure you don't forget anything. For Moz, we were able to accomplish this with data from Google Analytics, Search Console, and our own Moz Pro site crawl.

We mapped every URL to its corresponding URL on the new NodeBB platform. While we found many edge cases, this was relatively straightforward.

We made sure to redirect everything via 301. This is important because many platforms and developers may use 302s by default. While Google has told us that they pass PageRank equally through 302s and 301s , Google has also indicated that 301s are a stronger canonicalization signal .

Speaking of canonicalization, we also ran crawls of the new URL structures using the NodeBB platform. In instances where we found URL paths that didn't match our old patterns or we thought were extraneous, the NodeBB team was able to easily set up canonicalization patterns to avoid Google over-indexing our URLs.

A key part of our migration strategy was sitemap management. This involved two steps:

1. Old URLs: We already had sitemaps of all the old URLs in place. Importantly, we kept these sitemaps live and registered in Search Console. This way, Google would continue to crawl the old URLs and "see" the redirects.

Often, webmasters make the mistake of removing sitemaps too early, which may cause a decrease in crawl rate by Google. This means it could potentially take longer for Google to process the redirects.

Sitemaps aren't a perfect guarantee that Google will visit all your old URLs, but they do provide a hint. In fact, we still had several thousand URLs after several months that Google still hadn't visited, even with the sitemaps in place. Regardless, without the sitemaps of the old URLs, the issue could have taken much longer.

2. New URLs: Our old sitemaps were grouped into lists of 50,000 each — the maximum allowed by Google. There's some suggestion in the SEO community that grouping URLs into smaller sitemaps can actually improve crawling efficiency.

Fortunately, NodeBB allowed us to build smaller sitemaps by default, so that's exactly what we did. Instead of 2-3 sitemaps with tens of thousands of URLs, we now had 130 individual XML sitemaps , typically with no more than 500 URLs each.

As I mentioned earlier, the old Q&A had over 60,000 individual posts built up over 10 years.

Inevitably, a number of these posts were very low quality. We suspected both the low quality of the posts, along with poor user experience, could be causing Google to rank us lower.

Again, time constraints meant we couldn't do a full content pruning audit . Fortunately, NodeBB came to the rescue again (this is starting to sound like an advertorial — I swear it's not!) and ran all 60,000 posts through their spam plugin to remove the most obvious, low-quality offenders.

We did not redirect these URLs, and simply let them 404 after the migration. No one seemed to miss them.

FYI: another excellent resource on content pruning is this excellent webinar with Bernard Huang, Suganthan Mohanadasan, and Andy Chadwick.

Even though we were porting over the same content and basic design, the migration presented a terrific opportunity to improve user experience. To accomplish this, we made two tiny tweaks to the overall UX:

The old Q&A had neither of these features. Users who landed on a question had no options to explore other questions. As a result, we suffered for years with a frustratingly high bounce rate and poor site engagement metrics.

To be honest, I've never seen a migration quite like this. Having performed many migrations, I did my best to prepare everyone for the most likely scenario: be prepared for a 15-30% dip in traffic for 1-3 months while Google processes all the URLs.

As you can see in the chart below, we actually saw an increase in traffic, nearly starting at day one.

In fact, in the two months after the migration, organic Google traffic to Q&A pages was up nearly 19% compared with traffic to all other pages.

What caused this immediate lift in traffic? Was it the improved sitemap coverage, the better internal linking, or something else?

As soon as we launched the new Q&A, engagement numbers shot through the roof:

In short, users seemed to be much happier and more engaged with the new experience.

Again, we don't know. Google is rather tight-lipped about how it may or may not use user click signals for ranking purposes, but we do have our suspicions .

We're still continuing to improve the Q&A experience. Most notably, we're working to prioritize speed improvements, especially in light of Google's work around Core Web Vitals .

Regardless, this was definitely a delightful migration where we didn't experience a traffic drop — not even for a single day!

Perhaps if you vastly improve your user experience, site architecture, and SEO best practices, migrations might actually lead to a quick net win.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

Cyrus Shepard is the founder of Zyppy SEO , an SEO consulting and software company. He writes/tweets about Google ranking signals, SEO best practices, experiments, tactics, and industry updates.

For the latest, follow Cyrus on Twitter , or check out more of his posts on Moz .

Turn any keyword into a winning content plan in seconds. Try Moz’s new AI Content Brief, where real SEO data meets creative inspiration.
