---
source: https://www.onely.com/blog/seo-office-hours-march-26th-2021/
title: SEO Office Hours - March 26th, 2021
scraped: 2026-03-23
published_on: 2021-03-30
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

# SEO Office Hours - March 26th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-march-26th-2021/
Published: 2021-03-30
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
A summary of Google's SEO Office Hours from January 29th, 2021. Read the most interesting questions and John Mueller's answers!

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on January 29th, 2021.

00:39 – “Is it a problem if the AMP version differs from the canonical HTML version in that there’s a small ad in the AMP version?”

The versions should be equivalent and have the same content, but things like monetization can always vary – one example is dynamic ads.

03:06 – “In Mobile-first Indexing, will Google use mobile content to rank pages on mobile devices only or in desktop search as well?”

John said, “We will index the content once with the mobile crawler, and we’ll use that version with all the signals that we have as a basis for both desktop and mobile rankings.”

When it comes to things like Core Web Vitals , different metrics will be used for different devices. But when it comes to content, Google will only use the mobile version.

04:29 – “What is the best practice when it comes to indexing products with attributes? Do you have to canonicalize one option?”

From the search side, you can choose whether you want to canonicalize them or not.

John: “Sometimes I think it makes sense to have one strong page with all of the variants there, and sometimes it makes sense to have multiple pages. […] If the two variants are significant enough and people do search for the variant, it’s better to index them separately”.

07:01 – “Google is showing third-party content from my page inside the result snippet. Is there a way to avoid this?”

There is no direct way to do that. You could use the data-nosnippet. This may be enough in some cases.

If there are licensing or legal reasons why some content should not be indexed, you can use Javascript to pull that content in and then robots.txt to block that file from being crawled. That way, Google won’t see that content when crawling the page.

That being said, having third-party content indexed is a common situation with product pages. It rarely hurts the site or page, so you don’t need to worry unless you have a good reason to use this method.

09:33 – “A domain migrated separately from old desktop to new desktop and from old m. to new m. Now, the site is going to move to a responsive version to remove the m-dot. This means another redirect. Can this hurt the domain’s rankings?”

John said: “I would set up the redirect from the m-dot version to the responsive version and make sure that the change of address that you have in Search Console goes to the final destination.”

So basically, have the old m-dot version go directly to the www. version to avoid multiple redirects. Other than that, watch out for internal linking, and everything should be fine.

Many site migrations are done without using the change of address tool, so just setting up redirects should be enough.

If you’re struggling to conduct a site migration, contact us. We can help you develop an SEO migration plan .

13:00 – “Owners of a ccTLD domain want to expand internationally and use a generic domain. Services differ a bit for each country. Hreflang tags can’t be used because there are different landing pages for different countries. How will Google treat it if subfolders are used as opposed to subdomains for specific countries? Do you just set up geotargeting in the Search Console, and that should be enough?”

John said that it mostly comes down to setting it up in Search Console. In terms of subdomain vs. subfolder, it’s really about what’s easier for you to maintain.

15:23 – “Let’s say the main site targets a specific country, and you have sub-domains that target other countries. How to prevent people from, for example, the UK, typing the main domain name (which is targeted to, let’s say, the US) and trying to purchase something there? Can you, for example, disable the cart based on the user’s IP?”

John said that disabling the cart would be a viable approach.

Set up IP redirects on the main page only. So the minute someone from the UK enters a US version, redirect them to the correct one. That way, individual country versions don’t have to redirect, and you won’t have trouble with indexing and ranking.

Find out more about International SEO, including hreflang tags and geotargeting, in our what is international SEO article.

19:32 – “What techniques are recommended for e-commerce websites to improve traffic and enhance visibility?”

John recommends following the best practices for making a high-quality website and making sure you get the word out.

Some niches, such as medical, will have higher restrictions, so familiarize yourself with E-A-T and YMYL guidelines.

There is no one simple magic trick that will boost your traffic or search visibility, unfortunately.

In other niches, e-commerce websites are treated by Google just like any other page. John recommends looking into everything around Google Shopping and taking advantage of the Merchant Center.

26:53 – “What do we need to consider to solve hreflang issues in GSC?”

John ”It depends on the type of issue that you see there […] The idea of hreflang annotations is that it connects the different language and country versions of your pages”.

In many cases, the content management system does that automatically. If you still see GSC issues despite never setting anything up, then contact whoever takes care of the CMS or plugins you are using.

Errors don’t necessarily mean that the website is less visible. If it has been there for a long time, the chances are that GSC is just letting you know Google doesn’t use that markup at the moment.

28:25 – “How big of an issue is it when you have medical content not written by doctors?”

John, once again, recommends looking at the Quality Rater Guidelines. Looking at your website objectively is hard, and the document may help you see it as if with somebody else’s eyes.

“I think it’s trickier because it’s not a pure yes or no kind of situation. You kind of have to look at your site and think about what variations might there be that you could do”. But sometimes, the changes are as simple as highlighting who creates content, who reviews it, who contributes.

Quality raters may not directly influence the algorithms, but they do give a lot of feedback and input that is then used for both core updates and smaller updates.

Contact us for our E-A-T SEO services to fully demonstrate your expertise to Google.

46:57 – “Hreflang is not needed for translated pages because they’re not duplicate. Would you still recommend using hreflang for translated pages for geotargeting?”

With hreflang, Google essentially doesn’t change anything with the rankings. They swap out the URLs. For geotargeting, Google does use the location as a ranking factor, especially when Google suspects the query is to do with something local.

“If you have content for multiple countries, then I would try to make sure that you can use geotargeting. If you just have content in different languages, then hreflang is obviously fine […] When you see that people are reaching the wrong language version of your pages, then to me, that’s a sign that hreflang would be useful”.

50:10 – “ Do you recommend a short URL structure without directory depth? Is it bad to show users where they are?”

“The URL structure that you have on your site is something that you can use however you want. Google does not count the number of slashes in your URLs. […] For the most part, we treat URLs as identifiers of content; we don’t try to understand the site structure based on the URL.”
