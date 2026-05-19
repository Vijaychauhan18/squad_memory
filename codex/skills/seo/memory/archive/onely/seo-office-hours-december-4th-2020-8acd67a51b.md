---
source: https://www.onely.com/blog/seo-office-hours-december-4th-2020/
title: SEO Office Hours – December 4th, 2020
scraped: 2026-03-23
published_on: 2020-12-04
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# SEO Office Hours – December 4th, 2020

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-december-4th-2020/
Published: 2020-12-04
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
A summary of Google's SEO Office Hours from December 4th, 2020. Read the most interesting questions and John Mueller's answers!

## Extracted Body
A summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on December 4th, 2020.

0:31 The first question of the hangout revolved around a bug where Google deindexed pages, claiming that the canonical tag pointed to a different page. In reality, both the SEO and the URL Inspection Tool could see that the page was self-referential.

John replied that this occasionally happens and that he had seen examples of this happen in the wild. He said it might be caused by something quirky in the setup, like anti-adblock scripts. He recommended looking at other URLs to see what the difference is and what might have caused a portion of pages to get deindexed.

5:43 Barry Schwartz asked about the rationale behind releasing a Core Update just before the holiday season, and whether this update means Passage Ranking is now released to production.

John said that from his perspective, the timing is fine, as it’s just after Thanksgiving/Black Friday, and before the holiday season. When it comes to Passage Ranking, John wasn’t sure, but he said normally the team doesn’t release these big algorithm changes together with a core update.

13:19 A question was asked about anchor text from external links pointing to a website and whether Google looks at it on a page-by-page basis, or if it also looks at it site-wide.

John said Google uses anchor text to get semantic information both about a specific page (which you can see when a page is blocked from indexing by robots.txt, but it’s still indexed – Google would display the anchor text as the page title in the SERP), and the site as a whole. This is done to get more information about the contents of the page, and the site in general.

20:07 “Does Google index websites with new top-level domains like .club or .tools differently from other TLDs?”

John said Google treats all TLDs equally. There is no additional bonus from having keywords, countries, or cities in the TLD.

22:12 The next question was about displaying external reviews on your website. Does showing good ratings from external review websites influence rankings on Google?

John said that from an SEO point of view, showing good external reviews isn’t beneficial, although it may encourage users to choose your business.

25:01 An interesting question was asked about Passage Ranking and how it might influence SEO strategy. With Passage Ranking, doesn’t it make sense to consolidate several pages into one, hoping that Google would still understand that it’s about several different topics? By doing that, you’d also consolidate ranking signals, such as link juice, making it easier for that one page to rank well.

John wasn’t sure if this would be the right approach, and he recommended testing both strategies. He said consolidating might be less beneficial as users might be disappointed if they land on a page where what they’re looking for is buried deep within the content.

John also made a point that the topics of the pages would have to be closely related for this to make sense and that it strongly depends on the type of the site.

37:47 Is there anything you can do to force Google to index pages that are marked as “Discovered – not indexed” in the Google Search Console? And can using client-side rendering be a factor that’s contributing to this problem?

John said that client-side rendering shouldn’t have an impact in this case because Google should technically still be able to render JavaScript on your pages. Usually, if you have many URLs marked as “Discovered – currently not indexed” , it’s because Google doesn’t think this content is good enough to be indexed, so John recommended focusing on the quality.

52:03 Dave Smart asked a question about Core Web Vitals counting for noindex pages and pages blocked by robots.txt . Since Core Web Vitals are about to become a ranking factor, some website owners might be worried that their noindex pages that may often include search pages or tools that load slower than other pages will influence their rankings.

John said that from the user’s perspective, every page is a part of your website, so it makes sense to judge the website’s performance as a whole. However, he also pointed out that if pages are clearly grouped together, like search pages all placed in a /search/ directory, it makes it easier for Google to understand that these pages belong together, and Google might treat those grouped pages differently when it comes to Core Web Vitals scores.

If you’re struggling with your Core Web Vitals scores, contact us for a Core Web Vitals audit.
