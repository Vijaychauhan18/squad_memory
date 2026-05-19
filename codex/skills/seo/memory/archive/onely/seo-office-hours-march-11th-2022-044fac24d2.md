---
source: https://www.onely.com/blog/seo-office-hours-march-11th-2022/
title: SEO Office Hours, March 11th, 2022
scraped: 2026-03-23
published_on: 2022-03-28
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

# SEO Office Hours, March 11th, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-march-11th-2022/
Published: 2022-03-28
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on March 11th, 2022.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on March 11th, 2022.

6:50 “ […] we recently added a page to our site that is consistently driving significant traffic and engagement […]. My question for you is, can a single page with extremely high engagement and traffic have an influence on the domain as a whole? […] ”

John replied, “ I don’t think we would use engagement as a factor. But it is the case that, usually, pages within a website are interlinked with the rest of the website. And through those internal links across the website, we do forward some of the signals. So if we see that a page is a really good page and we would like to show it in search a lot, maybe it also has various external links going there, then that gives us a lot of additional context about that page. And we can kind of forward some of that to the rest of the website. So usually, that’s a good thing.

The thing I might watch out for is if it drives engagement for the kind of things that you care about. That’s just something that I’ve sometimes seen, where a page might be very visible for certain queries, but when you look at the queries, you’re like, well, I don’t really want to rank for that. My topic is something else. So that might be something just to take a cautious look at the metrics.”

The person then asked if a poor Core Web Vitals score in one section of a page can affect the rest of the domain. If you’re not familiar with the metrics she mentioned: Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS), I recommend you read our guides on What Is Largest Contentful Paint and What Is Cumulative Layout Shift.

8:28 “[…] for Core Web Vitals, we prioritize our high-search pages for product improvements, […]. Can a subset of pages with poor LCP or CLS, say only the video page on the site that aren’t the main or secondary or even tertiary search-traffic-driving pages on the site, impact the rest of the site’s overall Core Web Vitals score? […] “

John replied, “ Usually, that wouldn’t be a problem. So I think there are two aspects there. On the one hand, for the Core Web Vitals, we look at a sample of the traffic to those pages, which is done through, I don’t know, the Chrome User Experience Report functionality. I believe that’s documented on the Chrome side somewhere. But it’s essentially a portion of the traffic to your website. So that means that, for the most part, the things that we will look at the most are really the pages that get the most visits. So if you have random pages on the side that nobody ever looks at, and they’re really slow, then those wouldn’t be dragging your site down . And the other way around as well – if those random pages were really fast, they wouldn’t be pulling your site up. Even if it’s a lot of random pages, if, overall, they just don’t get a lot of traffic, then we don’t really care about it. […] the things people see should have a good user experience. So if most people are seeing a certain portion of your site, then that’s the part that we want to focus on.

The other thing is, with the Page Experience update , depending on how much data we have for a website, we might split it up into different sections. And we try to do that by understanding which pages across a website are essentially similar. And that can be by type of template or something like that, which means, if we can see that, say, for an eCommerce site, all of the product pages are really fast, and maybe we have enough data to look at the product pages separately, then we can have that group of pages treat it on its own. And if there is a different kind of page across the site that has enough data that is kind of slow, then we’ll say, well, this kind of page is more slow. So that’s the second part there, in that, if you have a kind of page that is very slow and we have enough data for that kind of page to understand, well, this is just that part of the website, then just that part will be affected by the Core Web Vitals and the page experience update. ”

12:50 “ So in the previous Office Hours, you once said that using too many internal links on the same page can dilute their values, and maybe Google won’t be able to understand the site structure. So in your opinion, what’s the amount of ideal internal links per page for an eCommerce site, maybe with millions of pages? ”

John replied, “ I don’t think there is an optimal number. The part that I would kind of watch out for is that when you crawl the website that you can still recognize there’s a structure. So especially with an eCommerce site that you can still recognize: here’s the main home page, here is the top-level categories, second-level categories, you can kind of still recognize that structure so that it’s clear how the context is of individual pages. […] it’s harder to recognize the structure if every page is linked with every other page. And if you have millions of pages on your website, it’s not going to be the case that you have millions of links on every page. So from that point of view, I usually don’t see any issue with this with eCommerce sites, just because, I don’t know, the eCommerce CMS tend to be set up in that way anyway, that you have different levels of categories and then the individual product page at some point. “

25:47 “ We have looked at the Crawl Stats reports in Search Console and have been trying to identify if there might be some issue on the technical side with Google crawling our website. What are some of the signals or things to identify that will point us if Google is struggling to crawl something or if Googlebot is distracted by files that are irrelevant […]? ”

John ensured that the person asking the question is managing a relatively small website and then he replied, “ Ok, so my guess is the Crawl Stats report will not be useful for you in that case [for a small website] because, with the Crawl Stats report, you’re really looking at an aggregate view of the crawling of your website. And usually, that makes more sense if you have something like, I don’t know, a couple hundred thousand pages. Then you can look at that and say, oh, well, on average, the crawling is slow. Whereas if you have a website that has, I don’t know, maybe around 100 pages or so, then essentially, even if the crawling is really, really slow, then those 100 pages, we can still get that, like, once a day, worst case, maybe once a week. It’s not going to be a technical issue with regards to crawling.

It’s essentially more a matter of understanding that the website actually offers something unique and valuable that we need to have indexed. So less an issue about the crawling side and more about the indexing side. The exception here would be if there’s really a big technical issue with your website. But that’s something that you would see right away because you would probably check individual of these URLs and notice, oh, Google can’t crawl them at all. There’s an error that’s returned, or there’s a noindex [tag] that’s returned. And that would be very obvious. So my assumption there, especially for a smaller website, is that it’s really a matter of making sure that Google understands the value of the website and that it knows that it makes sense to index as much as possible. Because the crawling side is not going to be the limiting factor. It’s really more like, well, you have to convince Google first that actually it should try to crawl. ”

39:34 “Why might there be tiny differences in synonyms […] that make such a big difference in ranking position?”

The person presented the following examples of synonyms: “edit video” and “video editor.”

John replied, “So from our point of view, that can be completely normal, and that’s something where, on the one hand, we do try to understand things like synonyms in a query, but we also try to look at the full context of the query. And especially when it comes to synonyms, we might assume that something is mostly a synonym, but that doesn’t mean that it’s completely a synonym. And especially when you’re looking at something like “edit video” versus “video editor,” the expectations from the user side are a little bit different. On the one hand, you want to edit a video. On the other hand, you might want to download a video editor. And it seems very similar, but kind of the things that the users want there are slightly different. So from my point of view, that kind of makes sense that we would show different rankings there. And we have the same with slightly different spellings of words. Like if you have the British or the American version of an English word, if you have a word or letter with an accent and it doesn’t have an accent, we understand that these are mostly the same, but we also understand that they’re slightly different. And we try to show search results that kind of take that into account.”

42:06 “ We’ve seen that most recipe websites are not providing very useful information in my country, and we try to change that by providing more useful information and going to the point of adding FAQs to every recipe. What is the best way to add these FAQs? ”

John replied, “[…] from my point of view, it’s totally up to you. The one thing I would watch out for in cases like this, where you have multiple rich results types that are potentially relevant for your pages, is that some of these types, we can combine, and some of them we can’t really combine that well. I don’t know specifically when it comes to recipes, if we can combine them, or if we essentially have to choose one or the other. And if you notice that no other recipe website has the recipe rich snippet plus the FAQ section on the bottom, then probably we can’t combine those. And then it’s probably better for you to pick which type of rich result type you really want to have shown and to focus on purely that type. ”

43:43 “ Google explains, in its subscription and paywalled content guidelines, that a specific schema must be added to a page in order to share paywalled content into the index and not trigger a cloaking penalty. After implementing this, however, the Rich Results Test does not seem to identify this, and aren’t we inadvertently risking a cloaking penalty?”

John said, “So I assume the Rich Results Test will show this, but I haven’t actually checked it because the Rich Results Test, for the most part, focuses on what Google actually would show in the search results as a rich results type. And essentially, the paywall content is probably not one of the things that we would show as a specific rich result type. So it’s possible that we wouldn’t show that in that test. One simple way to do that is to make a very simple test page and just test that page individually. The other test that you can do to make sure that Google is actually seeing the full content with the markup is the normal URL Inspection test, where you can do a live sketch of the page and you can look at the HTML that is generated for that page. And you could copy that out into an editor and double-check to make sure that the structured data that you want to have visible there is actually shown there. So that’s kind of the direction I would head there.”

Don’t let a Google penalty ruin your online presence. Take advantage of our Google penalty recovery services to get your website back on track and regain your rankings.

45:11 “ […] are links within certain sections of a site looked at differently? For example, if a page is linked within a header or a footer and therefore included on every page of a site, does Google view those links differently than links within the body of the page? ”

John answered, “ We don’t really differentiate there. So if things [pages] are linked in your footer of the page, and they’re linked from across the whole website, then, from our point of view, you have those links from across your whole website. It’s not the case that we would say, oh, links in a footer have less weight or are not as useful, we will ignore them, or anything like that. So from that point of view, when it comes to links, we essentially just see them as links on a page.

It’s slightly different when it comes to text in there in that we try to understand what the primary content is of the page. And when it comes to ranking relative to the other content on your website, we’ll try to focus on the primary content section of the page. But links, from our point of view, just help us to better understand a site’s structure. And whether they’re in the header, or in the footer, or the sidebar, or the main content, that doesn’t really change anything for us. ”

46:33 “ Does mobile-first indexing help with search rankings? Our website is still being crawled by Googlebot desktop. And we can’t figure out why it isn’t switching to mobile-first. We’ve been through the Google documentation and troubleshooting, but nothing jumps out. Would moving across to a Progressive Web App and offline support help? ”

John replied, “ So first of all, mobile-first indexing does not change anything for ranking. So it’s not the case that you need to force any kind of a move to mobile-first indexing. It’s purely a matter of indexing and picking out the content that we would use on a website. So from that point of view, I would not worry about this. If your website works fine on mobile, then, at some point, it’ll be switched over. I believe there are still some sites that are left that we haven’t switched over yet. But for the most part, we’ve switched, I guess, most sites over. And those that are remaining, we continue to double-check them. When they’re ready and when we think they’re ready, we’ll just switch them over.

But it’s not the case that you would notice any ranking change there unless the mobile version is significantly different from the desktop version. And that would also be a reason for us not to switch over to mobile-first indexing. And if the mobile version is significantly different and we did use mobile-first indexing for your site, then we would essentially just index your content based on the mobile version. And if there’s more content on a desktop version, we would ignore that. So from that point of view, I wouldn’t try to force this. Moving to a Progressive Web App is something you can do, but I don’t think it would affect how mobile-first indexing looks at your website. And usually, when it comes to Progressive Web Apps, they’re JavaScript framework websites. And that brings a whole set of other challenges that come with that in that you need to make sure that Google can actually see your content because JavaScript is something that we can usually render and handle well, but it’s not always as easy as a pure static HTML page. ”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
