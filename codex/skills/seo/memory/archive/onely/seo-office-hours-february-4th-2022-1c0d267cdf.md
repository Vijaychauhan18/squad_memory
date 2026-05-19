---
source: https://www.onely.com/blog/seo-office-hours-february-4th-2022/
title: SEO Office Hours, February 4th, 2022
scraped: 2026-03-23
published_on: 2022-02-08
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

# SEO Office Hours, February 4th, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-february-4th-2022/
Published: 2022-02-08
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on February 4th, 2022.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on February 4th, 2022.

01:02 “ [I work] in the stock industry. […] The particular number [of the stock prices, mentioned in the page titles] keeps on changing every single day. […] Does it make sense to change titles frequently [regarding the number is changing daily]?”

John said, “I think that’s fine. It’s something where we wouldn’t give it any special weight if your title tag keeps changing, but if you want to update your titles regularly, that’s totally up to you.

The difficulty, I suspect, is more that if you change your titles on a daily basis, we might not recrawl that page on a daily basis. It might be that you change it every day, but in the search results, the title that we show is a few days old just because that’s the last version that we picked up from that page. That’s more of I’d say a practical effect rather than a strategic effect.”

03:17 “Does having a date function […] in the content, last modified date, on your particular page can help Google index that page much faster?”

John: “It helps us to recognize when something has changed, but it’s not necessarily going to happen that we’ll say, oh, we’ve seen this page changes every day therefore, we’ll recrawl it every day. It might be that we recrawl it every day, […] every week or every month, so it’s not that the changes that you make with the titles would affect how quickly we recrawl.”

16:47 “We have a comment section under the article, but it’s not showing in Google. […] Are there any good practices for the comment section [that] I should [follow] so Google can see more of our comments?”

According to John, “It’s up to you. You can decide if you want to have that shown or not. But it’s essentially a technical element on the page, so it’s not that there’s a setting in Search Console to turn it on or off. There are different ways of integrating comments on web pages, and some of those ways are blocked from indexing, and some of those ways are easy to index.

If you want to have your comments indexed, then make sure that you implement them in a way that is easy to index. The URL [Inspection] tool in Search Console will show you a little bit of what we find on the page so you can test to see [if] Google can index the comments. But it sounds like even when you search in Google directly, you already see that we can’t index them.”

18:11 “Should we add the dates [to] the titles? […] [In our titles, we mention] some currency prices.”

John answered, “I don’t think it changes anything. For news articles, I do think it makes sense to include the date in various places on the page, and that can include the title. Just because with news articles, we try to understand what the primary date is of the page, and we do that by looking at all of the mentions and things that you have on the page. If we can confirm that date with these mentions on the page, then it’s easier for us to pick that up. But I think for a page that is changing constantly like currency prices, […] I don’t think it’s critical to have the date in the title.

19:18 “[But] we are creating a new article every day with different dates. We’re not changing the main article.”

John added, “[…] From my point of view, those would be normal news articles, so if you want to include the date in places like that, I think that’s perfectly fine. I don’t think you would get any magical SEO bonus from adding the date, but it’s okay.”

21:06 “Recently, we are facing some issues with our client website. […] Last four months we were posting content on the website, but most of the content is not getting indexed by Google. When we [use] the URL Inspection [tool], we usually get two messages: the URL is Crawled – currently not indexed yet or URL is Discovered – currently not indexed . […] Does it mean Google thinks this content is not perfect for indexing?”

John replied, “I don’t think it means anything in particular. I think that’s always an easy, early assumption to say, oh, Google looked at it but decided not to index it. Most of the time, when we still crawl something, it doesn’t necessarily mean that we will automatically index it. So I would almost treat those two categories of not indexed as a similar thing. It’s tricky because we don’t index everything, so that can happen. […]”

22:53 “[These issues happen] not only for one client, [but] we are facing these for multiple clients. […] Is there any other way to make [indexing] faster, or are there any other things […] that will help [us] getting indexed?”

John said, “There are different things which perhaps you’re already doing. On the one hand, making sure that it’s easy for us to recognize the important content on a website is really good, which sometimes means making less and better content so having fewer pages that you want to have indexed. The other thing is internal linking [that] is very important for us to understand what you would consider to be important on a website. So things, for example, that are linked from the home page are usually a sign that you care about these pages, so maybe we should care about them more. Things with external links also go into that category of where we see other people think that these pages are important, then maybe we’ll see them as important too. And then sitemaps and RSS feeds, from a technical point of view, also help us a little bit better to understand these pages are new or they have changed recently, we should check them out again and see what is there. But all of these things come together, and it’s something where it’s rarely that there’s one trick that you’re missing to get these pages indexed.”

24:42 “When we saw that those articles are not getting indexed, we told our client to share [them] on their social media accounts […] and those actually help us to draw some links from the other website to those blog posts. Now, we are using these blog posts for interlinking as well to other pages. Will getting linked to those blog posts which are not indexed by Google have any impact on the website ranking?”

John’s response was, “If we find external links to those pages, then chances are we might crawl and index that page are a little bit higher. It depends a little bit on what external links there are. Links from social media directly usually have nofollow attached, so we don’t forward any signals there. And if […] we can recognize these are maybe problematic links or not that useful links, maybe we will ignore those too. But obviously, if we can tell that something is seen as being important, we’ll probably go off and crawl and index that page more likely.

What you generally won’t see is that we will forward value to the rest of the website if we don’t actually index that page. Because if we decide not to index a page, then it’s still that situation that we don’t have a destination for those links so we can’t do anything with those links for the rest of the website.”

40:32 “ If an href tag contains both text and an image, which one helps Google better understand what the linked page is about: the alt text of the image or the visible anchor text? Does the order in which they occur within the tag play a role?”

According to John, “With regards to an image itself, we would probably not find a lot of value in that as an anchor text. If you have an alt text associated with the image, then we would treat that the same as any anchor text that you have associated with the link directly. From our point of view, the alt text would be converted into text on the page and be treated in the same way. It’s not that one or the other would have more value or not. They’re essentially equivalent from our side. The order doesn’t matter as much. […]

However, one thing I would not do is […], if the visible text doesn’t matter as much or is the same as an alt text, […] [removing] the visible text because especially other search engines might not see it that way and it might also be for accessibility reasons that it makes sense to have a visible text as well. So I wouldn’t blindly remove it to a minimum but rather at least know that you’re not losing anything by having both of those there.”

42:04 “ We are relaunching a customer website and also moving it from domain A to domain B. We are configuring redirects from domain A to domain B. Will the page authority and page ranking be negatively affected if there are many backlinks to domain A (and also future backlinks will point to domain A)? Is the domain authority from the old domain automatically inherited by the new domain even if there are a lot of backlinks to the old domain?”

John said, “I think there are two aspects. On the one hand, if you’re moving from one website to another and you use the redirects to move things over, and you use the various tools that we have, like the Change of Address tool in Search Console, then that helps us to understand everything from the old domain should just be forwarded to the new one. So that’s a situation where, as much as possible, we’ll take everything from the old domain apply it to the new one.

The other aspect there is on a per-page basis, we also try to look at canonicalization. For canonicalization, we look at a number of different factors that come in. On the one hand, redirects play a role in things like internal linking […], the rel=”canonical” on the pages, but external links also play a role. So what could happen […] is that if we see a lot of external links going to the old URL and maybe even some internal links going to the old URL, we actually index the old URL instead of the new one, because, from our point of view, it starts to look like the old URL is the right one to show and the new one is maybe more of a temporary thing.

Because of this, what we recommend when you do a migration from one domain to another is not only [to] set up the redirect and not only use it the Change of Address tool but also go off and try to find the larger websites that were linking to your previous domain and see if they can update those links to your new domain making sure that everything that you do is aligned with making sure that we can focus on the new domain rather than the old.”

If you’re struggling to set up a domain migration, access our website migration SEO services.

44:24 “ We are having a problem with eCommerce facets, filters that are getting indexed even though they are blocked by robots.txt and have a canonical tag. Is there a point in adding the noindex tag too?”

John said, “Probably not. The short answer is if the URL is blocked by robots.txt, we don’t see any of those meta tags on the page. We don’t see the rel=”canonical” on the page because we don’t crawl that page at all. So if you want us to take into account the rel=”canonical” or a noindex that you put on a page, you need to make sure that we can crawl the actual page itself.

The other aspect here is that these pages may get indexed if they’re blocked by robots.txt, but they’re indexed without any of the content because we can’t crawl it. Usually, that means that these pages don’t show up in the search results anyway . If someone is searching for some products that you sell on your website, then we’re not going to dig and see if there’s also a page that is blocked by robots.txt, which would be relevant because we already have really good pages from your website that we can crawl and index normally and that we can show.

On the other hand, if you do a site: query for that specific URL, then maybe you’ll still see that URL in the search results without any content. So a lot of times, what I notice is that this is more of a theoretical problem than a practical problem. Theoretically, these URLs can get indexed without content. But in practice, they’re not going to cause any problems in search.

Struggling with the “Page indexed without content” status in Google Search Console?

If you do see them showing up for practical queries on your website, then most of the time that’s more a sign that the rest of your website is really hard to understand. So if someone searches for one of your product types and we show one of these roboted categories or facet pages, then, from my point of view, that would be a sign that the visible content on your website is not sufficient for us to understand that the normal pages that you could have indexed are relevant here. My first step there is to try to figure out do normal users see these pages when they search normally? And if they don’t see them, then that’s fine, you can ignore them. If they do see these pages when they search normally, then that’s a sign that maybe you should be focusing on other things on the rest of your website.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
