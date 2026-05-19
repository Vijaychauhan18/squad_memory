---
source: https://www.onely.com/blog/seo-office-hours-november-5th-2021/
title: SEO Office Hours, November 5th, 2021
scraped: 2026-03-23
published_on: 2021-11-10
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

# SEO Office Hours, November 5th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-november-5th-2021/
Published: 2021-11-10
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 5th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 5th, 2021.

00:47 “We have three online pharmacies in Switzerland. […] For [one of them], we got a lot of spammy backlinks. […] From what I’ve known already, usually Google can manage those types of backlinks, but after Google core updates in July, we got really hurt in our visibility, specifically for that [one] shop that we got spammy backlinks. […] I would like to get your recommendation on that – what can we do to solve the technical problems that we have. So far, I still believe that happened because of spammy backlinks but [I’m] not sure.”

John said, “In general with the core updates, if you’re seeing changes there, usually, that’s more related to trying to figure out what the relevance of a site is overall and less related to things like spammy links. That’s something where I wouldn’t expect any reaction in a core update based on random spammy links that go to your website.

Also, with core updates, you can make incremental changes to improve your site over time with regards to the overall quality, and that will incrementally help there, but if it was a really strong adjustment with a core update, then you probably need to wait until the next core update to see those changes. […] It’s a matter of us trying to figure out what the relevance of the site is overall, and that’s something that almost relies on the overall site’s quality.

I imagine it’s tricky if you have multiple shops that are fairly similar. […] It’s probably not the case that one of them is bad – the other ones are really good. But it might still be something where you can use user studies to figure out what […] you could do to make it clear that this site is particularly relevant. I think, especially with regards to websites like pharmacies, it is something where our algorithms probably try to be a little bit more critical. […] It’s not a random website that has a story and a funny picture, it’s like people’s health that’s involved. “

John added, “Especially with regards to things like 404 pages and technical issues that would not be related to core updates. Core updates are more about understanding your site’s overall quality and its relevance and less about technical issues and less about spam.”

05:11 “I work on a website […] for Core Web Vitals . We have a feature where we put a Youtube video at the top, so that became the LCP element. It was heavier than what we just had, like a regular image. So we’re trying a method where we’re dynamically injecting it. […] Since it’s not below the fold content, we don’t lazy load it, but we’re using a facade, and then the <iframe> is dynamically injected when the user clicks the play button. I’m realizing now that the articles are not being indexed with the video content on the page essentially, so if I search for the page and I go to video search, it doesn’t appear there. So I’m wondering what the best way to get that content indexed with the page is. […] Is something like <noscript> or structured data the way to go? Is there any best practice for this?”

John: “Depending on the way that you set up the facade that you mentioned there, where you click on an image essentially or a <div>, and then it loads the video in the background, it can be the case that we don’t automatically pick it up as a video when we view the page. I have had feedback from the video search team telling us we shouldn’t tell people to do this because it causes problems like that. Essentially the best approaches are to make sure that with structured data, we can tell that there’s still a video there. I believe there’s a kind of structured data specifically for videos that you can add. Video sitemap is essentially very similar in that regard in that you’re telling us on this page there’s a video that is relevant. So those are the two approaches there.

I suspect over time, the Youtube embed will get better and faster, and it’ll be less of an issue where you have to do these tricks. But I think for the moment, it can still make sense, and it can still have a big effect on the Core Web Vitals of a page. So from that point of view, I’m torn. If the video team tells me like you should put it directly, and the other team says you should make things fast, then it’s hard to find the middle ground. But I think at least making sure that we can recognize the video is there, that’s really important.”

13:35 “We’re selling […] metal profiles, and we have many different types of those profiles. We have a lot of thin content because we have the same variations. […] We have within these URLs thousands of variations […], and I don’t know how to handle this. Should I canonicalize those? But then again, we’re linking to them [these URLs], so I don’t want to create bad in-links or bad quality links inside my page. Should I noindex [these URLs] or block [them] from robots? […] We don’t need people to come to those variation pages. We just want to create good quality on the category pages.”

John replied, “Usually what we recommend is if you have unique items that you want to have findable in a unique way, then you make sure that you have unique URLs for them and you make sure that they’re canonical [and] they’re not blocked by noindex. But if you don’t care about those individual URLs, if you care more about the higher-level categories, or if you have something like a broader product or category that essentially is the most important way of finding the content, then you can canonical to that page, you can noindex the other versions if you want. So you can essentially do whatever you want there to make it so that we focus all of our signals on that main page that you do care about.

[…] I imagine with industrial products like you mentioned, where you have so many different dimensions and variations, it probably makes sense to focus on the general layout and say all of these different options are essentially an attribute of the main product, and we should just focus on the main product.”

John added, “The thing to keep in mind with setting a canonical is that we will try to index the canonical page that you mentioned. So if there’s anything unique on the non-canonical pages, then we wouldn’t be able to find that , so essentially anything critical ‒ make sure it’s also mentioned on the canonical page.”

18:31 “In Discover, we have more or less two different search result pages. We have the first page, and then you can click on more results, and then you have the second page. Is there any ranking involved in this so that some article is on the second page, or is it more a matter of time when it is updated?”

John said the following: “ There is probably a sense of ranking, but I don’t think it’s the same as traditional web ranking. Discover is just so personalized, so it’s not something where I think it would make sense to have the traditional notion of, oh, you opened a Discover page, and you’re number five, and maybe next time you’re number four or something like that. […]

There are lots of things that go into even the personalized ranking side. I imagine there are also different aspects of maybe geotargeting and different formats of web pages, more video or less video, more images ‒ fewer images. But I honestly don’t know what [this is] specifically.”

John also advised to follow Google’s recommendations and added, “In particular watch out for the aspects where we say don’t do this or those kinds of things. I would also look around externally on Twitter – there are a handful of people who are almost specialized on Discover. […] I would check those things out, but because it’s such a personalized feed from our point of view, it’s not that you can work to improve your ranking in there. It’s not a keyword that people are searching for. So it’s kind of well, here’s some stuff for you that we think might be interesting.”

22:23 “I know you should use 301 for permanent redirects to pass PageRank the best and fastest way possible. However, our dev team doesn’t like to implement 301s because they’re stored in browsers, possibly forever. They say, in case of a misconfigured redirect, people might not ever be able to lose the incorrect 301 redirects. Does Google store 301 redirects just as some browsers seem to do?”

According to John, “The whole crawling and indexing system is essentially different from browsers in the sense that all of the network side of things they’re optimized for different things. In a browser, it makes a lot more sense to cache things, to cache things longer. But essentially, from our point of view, on the crawling and indexing side […], we don’t treat crawling and indexing the same as a browser. It’s a bit weird in the sense that we render pages like a browser, but the whole process of getting the content into our systems is very different. You see this sometimes when you render a page or when you see a page getting rendered, and it uses really old JavaScript files just because we’ve been able to cache them for a while, which may be on a browser wouldn’t happen, but essentially it’s different.”

23:59 “ Will Google accept 301 redirects with “Cache-Control: no-cache”, “Cache-Control: max-age=[time],” or “Expires: [date]” headers in order for us to get the best of both worlds?”

John said, “Yes, that’s perfectly fine. If it’s a 301 redirect, we treat it as a 301 redirect. It doesn’t matter what kind of cache headers you also add on top of that. So from that point of view, if this is a solution that works well for your dev team and for yourself, why not. […] The other thing is 302 redirects might also be an option if that works better for your dev team. 302 redirects have a bad reputation among SEOs which I think is incorrect because they work the same as normal redirects as well. It’s not that they don’t pass any PageRank anything like that, and if you have 302 redirects for the long run, we treat them the same as 301 redirects anyway. So if you can’t work out how it works with 301 redirects, maybe 302 redirects would be an option too.”

31:25 “If improving the quality of pages is important for Google with the Page Experience update , why does it take so long for Google to recognize these improvements? It seems counter-intuitive for SEOs to commit to making a real difference to improve the Web Experience if they have to sacrifice losing search position and traffic for several months.”

According to John, “[…] If you make a bigger change on your website, then sometimes you do see fluctuations, but that’s not something where we would say like those fluctuations are there because you improved your website. It’s just we have to re-understand a website when you make really big changes across a website. But from my point of view, a lot of the restructurings that you can do across a website depending on how you set them up […] – you can do that in a way that essentially has a very smooth transition when it comes to search and so that it doesn’t cause your whole website to disappear.”

32:48 “Does having multiple pages not being indexed due to quality affect the overall site crawlability?”

John: “No. If you choose to noindex pages, that does not affect how we crawl the rest of your website. The one exception here, of course, is for us to see in noindex we have to crawl that page first. So if there’s something where you’re creating, let’s say, millions of pages, and there 90 percent of them are noindex, and you have a hundred pages that are indexable. We have to crawl the whole website to discover those 100 pages, and obviously, we’ll get bogged down with crawling millions of pages. But if you have a normal ratio of indexable to non-indexable pages, […] ‒ I don’t see that causing any issue at all with regards to crawlability. And this is not […] due to the quality reasons that Google says, oh no, index pages are bad. It’s purely a technical thing. If we have to crawl a million URLs, we have to crawl a million URLs to see what is there. It’s not something where we can say, well, we’ll crawl only 50 000 because there are some noindex pages. Essentially it’s just a numbers issue.”

34:22 “We’ve heard that temporary (302) redirects do not pass link equity. Is our understanding of that accurate? More in general, we’ve heard that using 302s causes significant SEO issues, which has caused us to wonder if we should avoid these at all costs or if there are specific circumstances we should use them in.”

John said, “The answer is a clear no. There is no negative SEO effect from 302 redirects. I think the whole feeling of you losing PageRank when you do 302 redirects is false. It comes up now and then. I think the main reason why this comes up is because 302 redirects are, by definition, different. […] With a 301 redirect, you’re changing the address, and you want Google systems to pick up the destination page. With a 302 redirect, you’re saying, well, this is temporarily somewhere else, but you want Google systems to keep the original URL. So if you’re purely tracking the ranking of individual URLs, then, of course, a 301 will cause the destination page to be indexed, and ranking and a 302 redirect will keep the original page index and ranking. But there’s no loss of PageRank or any signals assigned there. […] Sometimes 302 redirects are the right thing to do – sometimes 301 redirects are the right thing to do. If we spot 302 redirects for a longer period of time where we think, well, maybe this isn’t a temporary move, then we’ll treat them as 301 redirects as well. But there’s no kind of hidden SEO benefit of using 301 redirects versus 302 redirects. They’re just different things.”

46:54 “[There is] one problem I have with a client. […] Many URLs blocked by robots.txt also have an HTTP header that is set on noindex. So I set open the robots.txt so the URLs can be de-indexed. But the client is afraid that the server won’t precede all the requests and will fail. So I said, well, if you see the user-agent as a bot, you can just give out a blank HTML body or maybe another page. Is there any risk of getting penalized because of cloaking if the HTTP header is set to noindex?”

John answered: “No, I don’t see any problem with that. In particular, if you’re showing search engines less than you would show users, that’s less of an issue with regards to cloaking. The part of cloaking that is more problematic for us is if you show us a really big and interesting page, and when users get there, they see something really tiny or slightly different. But if you’re showing us essentially an empty page and saying, oh, there’s nothing here you shouldn’t index this page, and we drop it out of the index, then we don’t care if users see something else. So from our point of view, what we want to avoid is that we promise users something that they can’t find. So if we drop a page from our index, we can’t recommend that page because we don’t have it anymore. […] If we recommend a page to people for a specific query and they go there, and they can’t find that content, then they’re frustrated, and they think we did a bad job, and that’s something where our cloaking problem comes from. But showing less is perfectly fine.”

Cloaking is one of the causes why some of your pages may respond with the “Page indexed without content” status in Google Search Console. Read my article to learn how to approach this issue.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
