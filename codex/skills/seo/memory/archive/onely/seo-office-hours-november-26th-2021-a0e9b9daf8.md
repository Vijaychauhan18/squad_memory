---
source: https://www.onely.com/blog/seo-office-hours-november-26th-2021/
title: SEO Office Hours, November 26th, 2021
scraped: 2026-03-23
published_on: 2021-12-01
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

# SEO Office Hours, November 26th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-november-26th-2021/
Published: 2021-12-01
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 26th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 26th, 2021.

06:44 “I have a website which […] is pretty bloated, and it’s been hit hard with the changes from the summer and onwards on the Core Web Vitals . So I’m now redesigning that website in AMP pages , and I’m converting all my images to WebP format. […] I’m trying to use the same URLs. The images currently rank but if I convert from JPEG to WebP, is that going to impact those rankings?”

John said, “ Potentially. What I’ve seen is some people use the same image extensions and make them WebP files, and if that works, then that would essentially save you the trouble because then you swap out the content but keep the same URLs, and all of that will continue to work. Whereas, if you change the image URLs, or if you change the URLs of the landing pages for the images, then obviously, for image search, that takes a little bit longer to pick up. But the thing to also keep in mind is that not all sites get significant traffic from the image search. So sometimes it’s something where theoretically it’s a problem if you make these changes and it takes time. But if, from a practical point of view, you get maybe five percent of your traffic from image search, then maybe that’s not your highest priority. “

11:27 “If we delete all JavaScript on a page for Googlebot, not for users, will there be any crawling or authority issues of our site? We fear that maybe Googlebot can crawl our page [and] simulate the user end, and so it will notice there may be no interactive functions. Will this be an issue?”

John replied, “ Probably not . If JavaScript is not required for your pages, the content, and the internal linking, then probably that doesn’t change anything. I don’t think it would significantly improve things from your side, so I would be cautious about just making that change.

It’s also tricky because once you go down this route of making more simplified pages for Googlebot, it’s very easy to fall into a situation where Googlebot sees something very different than what your users usually see, and that can make it very hard to diagnose issues. So if there’s like some bug that’s only affecting the Googlebot version of the site, you wouldn’t see it if users always see a working website.”

13:03 “Right now, there are many functions like Add to Cart or Buy Now and also localization functions like Select Language and Select Currency. These are all achieved by JavaScript. In regards to response time, we also want to reduce some loading time. So we want to know if we can disable this JavaScript on the page?”

John: “Probably you can. I don’t know the details of your site, how it actually uses JavaScript, but you can disable JavaScript in your browser and try the website out, and then you see what Googlebot would see there. The one thing you mentioned that I would watch out for is, I think, in product search. We sometimes check to see what happens when you add something to your cart to double-check that the pricing and things like that are the same. If you remove the Add to Cart functionality completely for crawlers, then maybe that affects those checks that product search does. But I don’t know the details of what exactly product search is looking for.

[…] We try to render the page to see if there’s something that we’re missing. But we don’t interact with the page because I think that would take too much time to crawl the web if we had to click everywhere to see what actually happened.”

16:44 “On our platform, we have B2B pricing benchmarks for various products and services that show pricing, especially for Switzerland. What we found now is if the user is searching for, e.g., “What is the cost of cashier system in Switzerland?”, we have no problem to appear in the featured snippets. But if the user in Switzerland is searching for [this query], then we found that the featured snippets are always in Euro and come from platforms in Germany that target the German market, not the Swiss market. Is there something we can do from our side […] to be shown in this context of Switzerland, even that [users] do not type “in Switzerland” but they are coming from Switzerland? […]”

According to John, “In general, the featured snippet is, from our point of view, a normal search result, so I wouldn’t focus too much on whether it’s shown in the featured snippet or not. […] It has a little bit of a bigger snippet, a little bit more information there, but otherwise, it’s a normal search result.

From our point of view, we try to do two things when it comes to searches. On the one hand, we try to recognize when a user wants to find something local and when we recognize that the user wants to find something local, we’ll use the geo-targeting information that we have from the websites to figure out which are likely the more local results that would be relevant for the user. […]

I think that the local aspect is something that helps to promote local websites, but it doesn’t mean that they will always replace anything that is global. So probably what we’re seeing are these bigger websites from Germany. […] And, on the other hand, we have the local results from the same country. And depending on how we understand the query, then we might show more local results, we might show fewer local results. I mean not fewer but more global search results. And probably what is happening when someone is searching for “in Switzerland” then, of course, we recognize, oh, they want something from Switzerland, and then we can strongly promote the local results from Switzerland. But without that addition, sometimes it’s hard for us to determine if the local context is critical here or not. And sometimes, we’ll take global results in a case like that. That’s not something that you, as a site owner, can influence. This is what we’ve learned from users over billions of searches that they’ve done. And it can change over time too, w here if we recognize that users in Switzerland tend to go more to Swiss websites for this kind of query, then maybe we should adjust our systems to learn that as well. But it’s not something that you can force.

The only thing you could do there is [to] use the feedback link on the bottom of the search results and say, oh, I was looking for something in Switzerland, and you showed me German stuff.”

22:37 “ Are there any situations where Google negates a site’s authority that can’t be recovered again even if the cause has been rectified? Assuming the cause was short-term turbulence with technical issues or content changes, how long for Google to reassess the website and restore full authority, search position, and traffic? Does Google have a memory as such?”

John said, “ For technical things, I would say we pretty much have no memory, in the sense that if we can’t crawl a website for a while, or if something goes missing […] and it comes back, then we have that content again. […] That’s something that picks up instantly again. This is something that I think we have to have because the internet is sometimes very flaky, and sometimes sites go offline for a week or even longer, and they come back, and nothing has changed, but they fixed the servers. We have to deal with that, and users are still looking for those websites.

I think it’s a lot trickier when it comes to things around quality in general, where assessing the overall quality and relevance of a website is not very easy. It takes a lot of time for us to understand how a website fits in with regard to the rest of the internet. That means, on the one hand, it takes a lot of time for us to recognize that maybe something is not as good as we thought it was. Similarly, it takes a lot of time for us to learn the opposite again. That’s something that can easily take a couple of months, […] sometimes even longer than a half a year, for us to recognize significant changes in the site’s overall quality because we essentially watch out for how does this website fit in with the context of the overall web. And that takes a lot of time. So that’s something where I would say, compared to technical issues, it takes a lot longer for things to be refreshed in that regard.

The other thing that I’ve very rarely seen is that a site gets stuck in some weird in-between stage in our systems. At some point, our algorithms reviewed the website and found it to be absolutely terrible, and for whatever reason, those parts of the algorithms just took a very long time to be updated again. Sometimes that can be several years. These are things that I’ve seen every now and then, but they’re extremely rare. So the chance of any random website falling into is fairly low. But it is something where if you struggle, and you see that you’re doing a lot of things right and nothing seems to be working, then do reach out to us and see if there’s something on our side that might be stuck. But I would say, at least technical things, they resolve very quickly. […] But especially if something happened five-ten years ago, and your site is stuck in a weird limbo state, then that’s something where reaching out and seeing if there’s something weird is always worthwhile.”

30:21 “ Google updates more than ten times a day. During the core update period, do you carry out the same updates as on regular days? If the changes in the core update are subtle, it’s indistinguishable from a regular update.”

John answered, “I don’t think we hold back on normal updates during this core update time, or when we roll it out. The core updates usually take a week or so to be rolled out, so I imagine the roll-out now will probably be complete soon. We tend not to hold [the normal updates] back during that time because we make lots of updates over the course of time.

The things we would hold back a little bit are maybe other bigger updates that we want to let people know about. So essentially, if we have some bigger update involving structured data that we want to talk about, then probably we’ll try to hold that back a little bit so that it’s not one update after another, but more like we can talk about the update a little bit clearer, and make it a little bit easier for people to understand what exactly is changing. But the normal updates that we do all the time like shifting the UI slightly by a couple of pixels, changing colors or, things like that, those are all updates that we can do independently.”

33:10 “ There is a blog on an eCommerce website of our clients, and for some reason, one particular article just won’t get indexed for three months now. […] Any ideas of what might be happening and what we can do?”

John: “In general, we don’t index everything on the web , so that’s the standard situation there. It’s something where we’re just not indexing this. If it’s something where you see that everything else tends to get indexed from that part of the website, for example, if you have ten blog posts and just one of them in between just randomly doesn’t get indexed, I would suspect that maybe there was some technical issue at some point. That takes a bit of time to be resolved, but it’s also just very hard to tell. In general, we don’t guarantee indexing, and even for a smaller website or as a section of a larger website, it can happen that we own the index everything.”

44:28 “ How does Google determine an out-of-stock [product] page? Will Google take actions on the out-of-stock page, for example, crawl less and lower the rankings? Structured data has been deleted, so it won’t be displayed out-of-stock in the search results.”

John said, “We do try to understand when a page is no longer relevant based on the content of the page. So, in particular, a common example is a soft 404 page, where you serve us a page that looks like it could be a normal page, but it’s essentially an error page that says: this page no longer exists. We do try to pick up things like that for eCommerce as well. So that’s something where you might see that out-of-stock products are seen as soft 404 pages. When they’re seen as soft 404 pages, we drop them completely from the search. If we keep the page indexed, despite being out-of-stock, we will not change the ranking. It’ll be ranked normally. It’s also still ranked normally if you change the structured data and say that something is out-of-stock. From that point of view, it’s not that the page would drop in ranking. It’s more that either it’s seen as software or 404 page, or it’s not. If it’s seen as software or 404 page, it’s still a normal page.”

Read Ania Siano’s article to learn when you need to address “Not found (404)” in Google Search Console.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
