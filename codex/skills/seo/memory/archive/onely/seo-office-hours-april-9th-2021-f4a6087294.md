---
source: https://www.onely.com/blog/seo-office-hours-april-9th-2021/
title: SEO Office Hours - April 9th, 2021
scraped: 2026-03-23
published_on: 2021-04-12
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

# SEO Office Hours - April 9th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-april-9th-2021/
Published: 2021-04-12
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 9, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 9, 2021.

00:45 – This Page Experience algorithm coming in May, will it be a real-time algorithm, or should we expect it to be updated from time to time?

“There is a general lag for the data anyway, so we kind of have to wait that period of time until we have collected enough data. I suspect it’s not something that will be optimized for speedy updates but more kind of to have a clear understanding of the overall picture. My guess is it’ll be more something of a slow thing rather than a real-time change.”

01:51 – “We recently updated our site, and now we’re getting a 100 score in Lighthouse, but after deploying the changes, the number of poor URLs has increased dramatically in GSC(…)Our good URLs have actually gone down. I understand the difference between lab and field data, but it seems a bit weird that we’re now getting a much better score in Lighthouse, but our real field data seems to be getting worse.”

John reiterated that with regards to Chrome User Experience Report data, you have to take the delay into account. It’s about a 28-day period during which data is collected.

If that is not the issue, then John recommended trying to figure out which part of the Core Web Vitals is affected by the change.

“One of the things that generally happens with the lab vs. field data is that with the lab data, it’s basically an assumption, an approximation of what our systems think might happen in the field because they’re just so many unknowns.”

It all depends on your users, where they’re coming from, what kind of devices they are using. Lab data can help you improve incrementally, but there isn’t necessarily a clear connection between lab and field results.

05:03 – Is there any consideration with regards to different internet speeds in different countries when it comes to Core Web Vitals?

John said “We have country information in the Chrome User Experience Report data so […] we’d be able to figure out where users are primarily coming from.

But the general idea is still kind of that users should be able to have a good experience […] if the bulk of your users sees a slow experience regardless of why then essentially that’s what will apply.”

The bottom line is, unfortunately, that if most of your users are coming from places with poor speeds then they will have a poor User Experience on your site. This will be taken into account when it comes to Core Web Vitals.

AMP makes it easier to make really fast pages, but yes, it’s harder, but it is still possible to have a poorly performing AMP page.

If you’re having issues with your Core Web Vitals data, take a look at our Core Web Vitals services. We can help diagnose and solve the issue.

08:29 – How to outrank huge competitors in a particular niche? Their on-page SEO is going to be brilliant, they are going to have a lot of products on the first page, their page speed is usually brilliant. Is there a way to bypass that?

There’s obviously no simple solution to that. “The good thing is, we occasionally hear from large sites as well that come to us and complain and say, This small site is ranking for our terms now! Shouldn’t we be ranking first because we’re like the most well-known? ”

John said it’s not impossible to rank well when there is a lot of competition, but it will be a lot harder.

12:05 – The article in the Search Central book talks about providing better information for shoppers. Does this apply to customer reviews?

John said, “From my understanding, the changes that we made there are really specific to […] where you’re actively reviewing one product or multiple products on a separate page, not where the primary purpose is a product page.”

16:25 – Can I use user-generated content below health articles, or will this affect the article’s authority?

You can use user-generated content anywhere. Google looks at the overall quality, not whether some content is user-generated. So use your judgment to determine whether that content is making the page better or worse.

17:33 – With regard to the mobile-first index rolling out, if a website is already being predominantly crawled with the mobile crawler, should you expect any changes?

18:08 – Our site is global, we do break it down by country, but it’s all English. Is it still helpful for the crawl to have a country-level XML sitemap, or does it not matter until you get to thousands of URLs?

Not necessarily. It makes sense to have a country-specific or localized sitemap file if you use hreflang. Otherwise, Google doesn’t differentiate between the source of the hreflang annotations.

“So, essentially, the hreflang side is the part which is relevant for us, and how you split things up into sitemaps is totally up to you.”

John added that “the one reason why you might split things up into separate sitemap files is so you can track it separately in Search Console.”

Find out how to implement hreflang properly with our hreflang international SEO guide.

23:52 – If a website is still on the desktop crawler, does that mean Google is detecting issues?

John suggested double-checking what the mobile version looks like. If you are sure it’s all good to go, then it’s probably the algorithms picking up something incorrectly. It’s not something you should worry about if there are no issues with your mobile version.

On the other hand, if there are issues to do with internal linking, structured data, or image embedding, then focus on fixing those issues.

The algorithm tries to pick up on the differences between the versions. If you’re happy with those discrepancies, then that’s, as John said, “essentially fine.”

“The reason for the delay has nothing to do with the fact that some sites haven’t fixed whatever differences there are.”

28:09 – If there are sites there are businesses that still have the majority of traffic coming from desktop users, will they still be moved over to mobile indexing? And in that case, will they see much of a difference?

John said, “As long as the mobile website is not like “ this page is not available for mobile users” then that should be fine.”

31:22 “We’re moving our site from a separate m-dot domain to one responsive URL in batches, and we’re starting with the home page. From the responsive home page, is it okay to link to the www URLs that will have alternate tags pointing to identical pages on the m-dot domain, and those pages will have canonical back to URLs for the desktop version?

“From our point of view, what happens there is we essentially change the canonicals from the m-dot versions to the www version so it’s kind of like a site migration and […] it’s something you can do incrementally if you wanted to.”

If you do want to do it that way, John recommends watching out for internal linking and redirects. Make sure they are updated as you move things over, so if you move the home page, then make sure internal links point to the new home page. The same goes for structured data. Make sure it applies to the new home page URL.

If you have things like hreflang annotations or rel canonicals, or any other URL-based metadata on those pages, make sure they apply to the new URL.

Nonetheless, this kind of setup may be tricky to track in Search Console.

Struggling to structure your domain migration? Take advantage of our website migration services .

36:01 If a website covers both YMYL topics as well as non-YMYL, non-sensitive topics, and the website has a hard time establishing E-A-T, does the rank of all articles on the website get hit?

“I think if you have a website that covers very sensitive topics as well as very trivial topics, then it’s always going to be challenging for Google’s algorithms to figure out how to deal with that website, regardless of anything around YMYL or EAT.”

The one place where the separation is easier is websites that have both adult and non-adult content. If there is a clear separation based on the URL structure, or if there is a subdomain, then it’s possible Google can learn which part of the website should be treated differently when it comes to, let’s say, SafeSearch. Nonetheless, this is not guaranteed.

The bottom line is that if you want Google to treat these as separate websites… make them separate websites. Otherwise, you have to take into account that Google will go one way at some point and another later on.

Contact us for our E-A-T SEO services to fully demonstrate your expertise to Google.

39:35 “On the subject of the new product review update, will that increase the chances of reviews showing up for brand searches, and does this only affect third-party review sites or all sites including reviews? I’m thinking of an eCommerce store including review content on its blog.”

John said that this algorithm is for things exactly like reviewing blog posts.

“It’s less a matter of is this hosted on an e-commerce site or is it hosted on a random blog. It’s rather this piece of content is a review”.
