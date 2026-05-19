---
source: https://www.onely.com/blog/seo-office-hours-february-12th-2021/
title: SEO Office Hours - February 12th, 2021
scraped: 2026-03-23
published_on: 2021-02-15
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

# SEO Office Hours - February 12th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-february-12th-2021/
Published: 2021-02-15
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
A summary of Google's SEO Office Hours from February 12th, 2021. Read the most interesting questions and John Mueller's answers!

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on February 12th, 2021.

3:05 – On a classifieds site, users may want to refresh their ads after they have expired. At the same time, the website might want to use the unavailable_after meta tag to inform Google when the page is about to expire and become a 404 or a noindex page in order to optimize its crawl budget. If the user refreshes the page after it’s been declared as unavailable , will Google still recrawl it and index it again? Can you redeclare the unavailable_after tag? And will using the lastmod tag in your sitemap help let Google know that the page has been refreshed?

John said: “If we refresh that page for crawling and indexing, then we would see the updated unavailable_after meta tag, so that would work. (…) If we recrawl that page and see the new tag, we’ll take that into account.”

He said that using the lastmod tag in your sitemap would help – it’s not guaranteed that the page gets recrawled right away, but eventually, Google should recrawl and index again.

Finally, John said that using the unavailable_after tag doesn’t mean that Google will stop recrawling the site altogether. It only means that the page is about to become a “Not found (404)” or a noindex. He said: “Our systems are essentially going to treat it as if there’s a noindex on there after that date, even if we don’t recrawl it.”

9:43 – “A large site has legacy code that generates parameters on internal links, which are unique for each session. Googlebot is served these links with parameters stripped. Is this considered cloaking?”

From a technical standpoint, this would in fact be considered cloaking and would be discouraged by anyone on Google’s webspam team. But from a practical point of view, it wouldn’t be a problem – your site will not be penalized for this.

However, you need to remember that this issue makes it hard for you to control what your users and Googlebot are seeing on your website. John said: “It’s very easy to run into a situation where suddenly Googlebot gets error pages, or Googlebot gets bad links, and every time you check that with maybe a local crawler, you don’t see those broken links.”

10:54 – “If a niche news portal is moved to a subdomain of a larger general news portal, can its visibility be affected by the main domain?”

John said that any time you’re splitting a site or combining many sites into one, you should expect ranking fluctuations , both short and long-term. Moreover, you may see the results being different than what you expected, particularly in the short term. When you merge or split websites, Google has to reprocess everything and “come up with a bigger new picture.”

20:43 – “A website uses JavaScript to change the URL with the History API. For instance, the server responds with /page, while the users see /page-updated. The latter can’t be found anywhere in the website’s resources. Would Google see the updated URL and index it?”

John said that Google would treat this change of URL as a redirect. Google would try to use the updated URL and index it. The next time Google would try to crawl the /page-updated URL and not the original one.

“The important part here is that /page-updated is actually a page that we can crawl. It shouldn’t be the case that you swap out the URL for something that is non-existent if you go there directly.”

Not sure where to get started with JavaScript SEO ? Book a discovery call with Onely’s experts today!

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
