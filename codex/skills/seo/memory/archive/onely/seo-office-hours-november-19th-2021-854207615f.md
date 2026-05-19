---
source: https://www.onely.com/blog/seo-office-hours-november-19th-2021/
title: SEO Office Hours, November 19th, 2021
scraped: 2026-03-23
published_on: 2021-11-25
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

# SEO Office Hours, November 19th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-november-19th-2021/
Published: 2021-11-25
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 19th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 19th, 2021.

02:58 “I work in the news industry. […] When I was optimizing the SEO, I told [my colleagues] we need to fix the title to 65 letters only. […] I searched the web, and I didn’t get the right answer. Is that a ranking factor that the title should be that long?”

John said, “No, we don’t have any recommendation for the length of a title. I think picking a number from your side and saying: on mobile, this much room is available, so as an editorial guideline, we’ll say 65, or whatever you want to choose, that’s perfectly fine. But from Google, the search quality [and] ranking side, we don’t have any guideline that says: it should be this long or not.

[…] The length doesn’t matter. If we show something shorter, or if we show something slightly different, that’s just kind of how we display it in the search results. It doesn’t mean the ranking changes.”

When it comes to the length of the URL, John said it doesn’t matter too. “I think it’s good practice to have some of the words in the URL, so it’s more a readable URL, but it’s not a requirement from an SEO point of view.”

John also added that having only the ID in the URL is okay from Google’s perspective. “It’s better to have some words in there, but it’s essentially fine. For the most part, that’s something that just users see, and when they copy and paste the URL, they might see, oh, I know what this article is about based on what I see here. Whereas, if they just see the number, then they might pick the wrong one or might not be sure about that. But that’s a user question almost, not an SEO question.”

25:30 “ We notice that when our crawl request from Google decreases, our crawl request from Bing increases. Are these two related?”

John replied, “I think that would be a really weird coincidence, but I’m not aware of any collaboration with Bing that we swap out the crawl requests, so I don’t see that being related.

What might happen sometimes is, on the Google side, when we recognize that a server is overloaded, slow, and showing server errors, then we’ll tend to crawl less. And it could be the case that when Bing crawls a lot, we see the server is generally slower, so we’ll crawl a little bit less. And when we see that the server has more capacity, is a little bit faster, then we’ll crawl more which might be related to when Bing happens to crawl less. Theoretically, that’s possible. From a practical point of view, I doubt that would be happening just because, usually, websites have so much capacity for users to come that some crawling from Bing and some crawling from Google is not going to slow down the whole website.”

32:27 “ Indexing seems to have changed a lot for me over the past year or two (happens on all my web properties). Whereas things were quickly indexed before when submitting them in GSC, nowadays, GSC submissions seem to have no effect. Rather it appears on its own in the index after days or even weeks (sometimes bouncing in and out of the index). This happens on well-established sites with 50,000+ organic monthly visitors. Why is this?”

John said, “I don’t know. It’s hard to say in a broad way: this is why things are not being indexed so quickly on your website. In general, the request indexing tool in Search Console is something that passes it on to the right systems, but it doesn’t guarantee that things will automatically be indexed.

I think in the early days, it was something that was a lot of a stronger signal for the indexing system to actually go off and index that. But one of the problems that happens with these things is, of course, people take advantage of that and use that tool to submit all kinds of random stuff as well. So over time, our systems have grown a little bit safer, almost in that they’re trying to handle the abuse that they get, and that does lead to things sometimes being a bit slower. Where it’s not so much that it’s slower because it’s doing more, but it’s slower because we’re trying to be on the cautious side here. That can mean that things like Search Console submissions take a little bit longer to be processed. It can mean we sometimes need to have a confirmation from crawling and a natural understanding of a website before we start indexing things there. From our point of view, that’s expected.

One of the things that I think has also changed quite a bit across the web over the last couple of years, probably longer, is that more and more websites tend to be technically okay in the sense that we can easily crawl them. […] So we can, on the one hand, shift to more natural crawling. On the other hand, that means a lot of stuff that we get ‒ we can crawl. Whereas in the past, when something would not get indexed, you might say, well, maybe there’s something set up incorrectly on the website, and you try to find that problem from a technical point of view. Nowadays, most submissions that we get are technically okay, so we can go off and index them, which means because there’s still a limited capacity for crawling and also for indexing, we need to be a little bit more selective there. I imagine, overall, that’s what you’d be seeing there if we’re not picking things up as quickly as we might have in the past.”

35:33 “ I have a domain that hasn’t been used for four years. The blog I had was doing great in SERP for its niche, but because I didn’t want to sell it, I deleted all the content and let the domain “parked.” I want to revive the content on it, but I want to take a slightly different approach. My question is, does Google needs to learn about my blog again as if it was new? Or do I have a better chance to be an authority on my niche faster than usual because of this old domain?”

According to John, “If the content was gone for a couple of years, probably we need to figure out what this site is, essentially starting over fresh. So from that point of view, I wouldn’t expect much in terms of bonus because you had content there in the past. I would assume you’re going to have to build that up again like any other site. If you have a business and you close down for four years, and you open up again, then it’s going to be rare that customers will remember you and say, oh, I will go to this business. It looks completely different, they offer different things, but it used to exist. I think that situation is going to be rare in real life […] as well. So I would assume that you’re essentially starting over here.

This is also one of the reasons why it usually doesn’t make sense to go off and buy expired domains in the hope that you’ll get some bonus out of using those expired domains.”

37:03 “I’m managing a website with over 5,000 URLs. We do our best to comply to search ranking/SEO factors, but we find that on average, we get around 100 URLs per month that get deindexed. What can we apply to our pages to prevent this from happening?”

John: “It’s hard to say with just that information because for the most part, we don’t just remove things from our index, we pick up new things as well. So if you’re adding new content at the same time and some things get dropped on along the way from our index, usually that’s normal and expected because, essentially, for pretty much no website we index everything on the website. It’s something, where on average, […] between 30 and maybe 60 percent of a website tends to get indexed. So if you’re adding hundreds of pages a month and some of those pages get dropped, or some of the older pages or less relevant pages get dropped over time, that seems expected.

To minimize that, I think it’s something where essentially you need to show to Google, or to your users, I guess, what the value of your website is overall so that Google says, well I need to make sure I keep as much as possible from this website in my index. That’s usually less of a technical thing and more of something where the value that you provide is critical for Google to keep this in our index. Even in cases when we think a website is fantastic, we still won’t index everything. From a technical point of view, it’s almost impossible, partially because a website tends to have a lot of, I call it, technically duplicated content where you have things like tracking parameters, or pagination that goes into infinite spaces, or filtering parameters, or search forms […] where, theoretically, we can find an infinite number of URLs on the website. And if it’s possible to find an infinite [number] of URLs and we can only index a finite number, then we’ll never be able to get everything indexed.”

41:58 “ We migrated our site about seven months ago to a new domain. Should I remove the old sitemap from the old site?”

John said, “ Probably yes. Usually, when you migrate a website, you end up redirecting everything to the new website, and sometimes you keep a sitemap file of the old URLs in Search Console with the goal that Google goes off and crawls those old URLs a little bit faster and finds the redirect. That’s perfectly fine to do in a temporary way. But I think, after a month or two, it’s probably worthwhile to take that sitemap out because what also happens with the sitemap file is you’re telling us which URLs you care about. And if you’re pointing at the old URLs, then you’re almost saying, well, I want my old URLs findable in search. That can lead to a little bit of a conflict in our systems that we say, well, you’re pointing at the old URLs, but at the same time, you’re redirecting to the new ones; which one do you want to have indexed? At that point, you essentially want to remove that conflict as much as possible. And you can do that by just dropping that sitemap file and giving us all the signals, that you can, that point at your new pages. Once we’ve seen that redirect, we can just focus purely on the new pages that you have on your website or the new domain, or whatever move that you’ve made.”

Experiencing issues with your site migration? Access our website migration services for an audit.

43:30 “ Google snippets and the Knowledge Graph seem to be getting better all the time, and often users don’t have to visit a website to get the answers they need. So what does the future hold for web publishers, big and small, in terms of getting SEO traffic?”

John said, “ I don’t see the need for websites ever going away because that information is really in detail on your website. Sometimes people just want something really quick, maybe they want the phone number or the address of your business, and then they go off and visit that business directly. But essentially, for anything more than just a snippet of information, you want to find out the full context and get some more information there, so I don’t see that going away.

It’s also definitely not our goal to be that one place where everyone goes and just gets the answers directly because we know we have to work together with the ecosystem, together with anyone who’s making websites to make sure that the things we’re providing in search, provide value for website owners as well. Because it’s easy for website owners to say, well, I don’t want to take part of this search, I’d rather just be findable on Facebook, or in social media, or somewhere else. We want to make sure that there’s an equal deal in that we can show your content, we can send users your way, but you also get something out of that in the sense that you’re getting all of this traffic as well. That is something that all of the teams at Google, that work on the search, care deeply about, so it’s certainly not the case that we’re trying to figure everything out and then just only show them on our side. But I understand this is something that folks also worry about because they see these fancy features in search, and it’s hard sometimes to understand what the bigger picture there is or what the net effect is across websites.

I think also if you run across situations where you’re like, well, I don’t like the way that Google is showing this because it’s something that I’d prefer people to look at on my website, then give us that kind of information. Contact me on Twitter, send me some screenshots of things where you’re saying, well, this is not the way that I want to have my content shown. And I’m happy to take that to the product teams, and we can figure out ways to improve that.”

53:13 “We want to create the same article in different languages. […] Should I define a canonical and alternate version there?”

John: “I think, in general, if you have multilingual content, then using something like the hreflang annotation is useful because it helps us to figure out which version of your content should be shown to which user. So that’s usually the approach to take.

With regards to the canonical, you tell us which URL to focus on, so the canonicals should be the individual language versions . It shouldn’t be one language, as a canonical for all languages, but rather each language has its own canonical version like this is the French version and the French canonical, this is the Hindi version and the Hindi canonical. So it shouldn’t be linking across the languages.”

54:43 “My site is on Google News ranking. I have AMP pages crawled there. Should I use their alternate versions, like we have an alternate version in the Hindi language or the Russian language? What do you recall on this?”

John replied, “With AMP pages, normal web pages, and different language versions, it gets very complicated. In the AMP documentation, they have a page on […] multilingual content that has a diagram with regards to the hreflang annotations that you should have there , I would check that out. With regards to the Google News side of that, I don’t know how [Google] News would handle that specifically. I don’t know, for example, if they would require separating that out into a subdomain, so it’s clearly a separate news site, or what their recommendations are there. But for AMP, I would check out that graphic in the documentation.

I think it’s complicated with AMP pages, and normal pages, and internationalization. When you look at the graph, you will probably say, oh, this makes a lot of sense, but if you have a lot of different pages and a lot of different language versions, it’s a lot of work to get all of those details right.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
