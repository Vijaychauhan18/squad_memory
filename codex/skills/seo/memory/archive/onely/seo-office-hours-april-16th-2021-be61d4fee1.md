---
source: https://www.onely.com/blog/seo-office-hours-april-16-2021/
title: SEO Office Hours - April 16th, 2021
scraped: 2026-03-23
published_on: 2021-04-19
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

# SEO Office Hours - April 16th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-april-16-2021/
Published: 2021-04-19
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 16, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 16, 2021.

02:19 – Why doesn’t Google recommend using the noindex tag when Google is picking up the wrong canonical tag or ignoring the canonical tag?

”If you’re saying that something is a canonical of a different page then you’re saying that [these pages] are equivalent . And if you’re saying one of them should not be indexed and the other one should be indexed then you’re saying well, they’re not really equivalent because you want them treated in very different ways.

From a practical point of view, I don’t see this causing any problems. Suppose you’re in a situation where you really strongly want to have one page to be canonical, and you’ve done everything else that you need to do to make sure that the internal linkings are in the right place. In that case, the sitemap file has the right URLs all of that, then using noindex like that is something that is not going to cause any problems.”

So while using the noindex tag on some of your canonicalized pages sends a mixed signal to Google, it shouldn’t be a problem if everything else on your website works fine.

Is your page “ Excluded by noindex tag ” in Google Search Console?

Read our article to make sure that you used the noindex tag on purpose.

11:53 – Should you add noindex tags to pagination pages? It seems like users don’t need to see duplicate content in search. How does Google treat this issue?

First of all, think about why you are using pagination. Is it to split up a long article with different content on each page? Or are you an eCommerce store that divides product listings across several pages?

With regards to the second case, John said “It’s not so much that there’s any content that is unique on page two or page three, but there are links to other products.”

When it comes to content – if you’re splitting the content up across multiple pages, then, of course, you want to make sure that that is indexable. So, do whatever you need to do to make sure that those pages are findable, that you have links to part two, part three, part four within your website, that those pages are also indexable, that they don’t have a canonical pointing to another page for example (…) so i f it comes to content that is split up, make sure it’s absolutely indexable.”

16:15 – “We have a huge global website where we have to set up hreflang in a sitemap because HTML is just not feasible and I found best practices where you have hreflang in the HTML, where you have separate mobile and desktop pages. So, the mobile pages point to mobile pages, desktop pages point to desktop pages. How do we do this when we’re setting up hreflang in a sitemap?”

John said: “(…) Map out the whole site and get all of the URLs and figure out how they’re connected. Essentially, our guidelines with regards to sitemaps for m-dot pages are such that you don’t need to list them in a sitemap file, but I think in your case where you have hreflang annotations that you want to apply to the m-dot pages then I would absolutely list them.”

19:44 – A website is considering detecting AdBlock and preventing users who are using it from accessing the site. The website also has a paywall that’s properly marked up with schema. If they decide to exclude Googlebot from seeing the AdBlock detection, would that be cloaking?

John said that this shouldn’t be perceived as cloaking by Google. He said, “The cloaking team mostly tries to watch out for situations where you’re really showing something different to users as to Googlebot.”

With AdBlocking, that wouldn’t fall under this category, so it wouldn’t be cloaking, even though John clarified that he’s not a fan of such solutions.

21:27 – And what if they decide to serve Googlebot the AdBlock detection and it’s an overlay? Do you anticipate any problems with Google understanding the content there?

John said, “If it’s an HTML overlay on top of the existing page then, I don’t see that as being problematic because we would still see the actual content in the HTML. […] From our point of view, if we can still index the actual content from the page, then that’s fine.”

23:11 – Is it necessary to optimize the whole website if you want to rank a particular page or the URL, or is it okay if you don’t optimize the whole website?

John said that while Google always primarily looks at the specific page in order to rank it, every page is “embedded” within the broader context of the whole website. So John recommended improving the website overall. That helps Google understand what the value of the page is and how it is important.

34:13 Will switching from Squarespace to WordPress affect my Google search rankings?

“Yes, most likely it will.” A CMS change involves making other big changes to your website. If these changes are made with SEO in mind, the effect should be positive.

While it may seem the content is the same if you just copy and paste the content to the new version, Google is looking at the bigger picture, so you should have a checklist of things to work on. These things might include:

John added that “The tricky part is, by the time that you notice that something has gone wrong with a site migration, it’s often like a month or two later.”

Is something going wrong with your site migration? Check out our website migration services . We can help you.

38:09 – As user experience is one of the determining ranking factors, could you give us a quick insight into how user experience is measured by Google?

John said that Google doesn’t have a “pure” user experience ranking factor, but there are many individual things that “kind of map into UX.”

If you’re struggling to optimize your speed, stability, and responsiveness, contact us for a Core Web Vitals audit.

41:42 – What is the treatment that Google gives to a public URL for a whole website used for test purposes only?

Google doesn’t really have any specific treatment practices for testing websites. They can still show up in search. If you don’t want Google to crawl a staging website, the best way is to block it with a login screen.

“The advantage of using authentication versus things like robots.txt or noindex on pages is that with authentication, you recognize right away if you accidentally include that on your primary website.

So if you push that staging website live and you leave authentication in place, then that’s pretty obvious, whereas if you push your staging website live and you leave the robots.txt block or use the noindex, then you really have to watch out.”

Are your pages “ Blocked by robots.txt ” in Google Search Console?

Read our article to ensure you blocked the crawling of your pages on purpose.

43:48 – “We’re using an approved third party to collect our service and product reviews, and these are displayed on our website using a widget, but the data is actually held against our listing on the review site itself. How would Google feel if we copied these reviews and displayed them on our web pages as opposed to just using the widget to display them?”

First of all, you have to make sure you are allowed to do this with your service provider.

From Google’s point of view, you can include these reviews on your page if you treat them more like testimonials. John adds, “With regards to structured data on the pages, you can only use the review structured data on your site in a case like this if you’re collecting the reviews yourself .”

45:16 – Is user experience for both desktop and mobile taken into account when it comes to Core Web Vitals as a ranking factor, or is it only the mobile experience for the user that counts?

John said, “At the moment, the plan is only to use the mobile user experience.”

50:40 – How can you optimize your site to have sitelinks displayed in the search results?

John said the following: “Site links are something that happens algorithmically. It’s not based on any particular markup on a web page. For the most part, it’s not something that you can explicitly target to try to make it appear.”

If Google recognizes that there is a need for searches to show more results from a particular site, then it will show these links, but it’s not something you can force .
