---
source: https://www.onely.com/blog/seo-office-hours-november-12th-2021/
title: SEO Office Hours, November 12th, 2021
scraped: 2026-03-23
published_on: 2021-11-16
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

# SEO Office Hours, November 12th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-november-12th-2021/
Published: 2021-11-16
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 12th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on November 12th, 2021.

8:16 “ [Some pages] were wrongly set to noindex. This was fixed a couple of months ago. […] We tried to request the indexing via Search Console [and] resubmitting sitemaps but still, we don’t get these pages indexed. Do you have any ideas as to what might cause Googlebot not to listen to the indexing requests or if there are any known issues in Search Console with indexing?”

John: “I don’t think there are any known issues in that regard, but sometimes we’re a little bit conservative with regards to submitting to indexing requests, which is probably partially what you’re seeing there. […] On the one hand, if we see that a page is noindex for a longer period of time, then we usually slow down with crawling of that. […] It also means that when the page becomes indexable, we’ll pick up crawling again, so it’s essentially that one kind of push that you need to do.

Is your page “ Excluded by noindex tag ” in Google Search Console?

Read my article to make sure that you added the noindex tag on purpose.

Another thing is that since Search Console reports on essentially the URLs that we know for the website, it might be that the picture looks worse than it actually is. That might be something that you could look at by, for example, looking in the Performance Report and filtering for that section of the website, or those URL patterns, to see if that number of high noindex pages in Search Console is reporting on pages that weren’t really important and the important pages from those sections are actually indexed.”

John also stated that “[…] a sitemap is essentially a good start, but another thing that you could do is make it clear with internal linking that these pages are very important for the website so that we crawl them a little bit faster. That can be a temporary internal linking where you say: for a couple of weeks, we link to individual products from our home page. […] Essentially, when we find that the internal linking has significantly changed, then usually we go off and double-check those pages too. So that could be a temporary approach to pushing things into the index again. With internal linking, it’s not that you’re saying these are important pages across the web but rather important pages relative to your website. So if you significantly change the internal linking, it can happen that other parts of the website, that were maybe just barely indexed, drop out at some point. So that’s why I would do that on a temporary level and say, I want to push these back into the system so that they get recrawled at the regular rate, and then I’ll change the internal linking back so that everything is more normal again.”

Let us help you with optimizing internal links! Resolve your doubts and contact Onely for thorough internal linking optimization.

With regard to adding links to the footer, John added:” I think that would work too. It’s usually better if we can find it on really important pages on the website, usually like on your home page, […] where you’re saying that this is important for you, therefore, we’ll go double-check that page.”

14:25 “I’m using a WordPress website, and I’m using two plugins. One [of them] automatically adds a rel=” canonical” link to every page. […] [The other one is a translator plugin] that adds [to] every page a rel=” alternate” link. Does it make it logical that it says: for that URL, it’s canonical, but it’s also an alternate? Does it conflict somewhere in the crawler?”

John stated, “No. I mean I don’t know exactly what these two plugins do. From an overall point of view, if you have a page that has a rel=canonical on it, you’re essentially with a canonical saying: the link that is mentioned there is the preferred URL that I want. If it’s the same page, then that’s perfect because then it gives us confirmation that this page is the one that you want to have indexed.

The rel=” alternate” basically means there are alternate versions of this page as well. So with different languages, for example, if you have one page in English, one page in French, you would have the rel=” alternate” link between those two language versions. And it’s not saying that the page where that link is on is the alternate, but rather it’s like these are two different versions, one of them is in English, one of them is in French. They can both be canonical so having that combination is usually fine.

The one place to watch out a little bit is that the canonical should not be across languages. So it shouldn’t be that on your French page, you have a canonical set to the English version because they’re different pages essentially. But the French page can be canonical, and the English page can be canonical, and you have the alternate link between the two, and that’s essentially a good set.”

Do you struggle with optimizing duplicate content and your canonical signals get ignored by Google? Read our article on how to fix “Duplicate, Google chose different canonical than user.”

16:49 “We have a website with an e-commerce store with a lot of product variations that have thin or duplicate content . I made a list of all the URLs we want to have indexed […], and we don’t want to have indexed. […] I’m not sure what would be better: canonicalization or noindex?”

John said, “I think the general question of should I use noindex or rel=” canonical” for another page is something where there probably isn’t an absolute answer. […] If you’re struggling with that, you’re not the only person who’s like, oh which one should I use? That also usually means that both of these options can be okay. So usually, what I would look at there is what your really strong preference is. If the strong preference is you really don’t want this content to be shown at all in search, then I would use noindex. If your preference is more, I really want everything combined in one page […], then I would use a rel=” canonical”. Ultimately the effect is similar in that it’s likely the page that you’re looking at won’t be shown in search, but with a noindex – it’s definitely not shown, and with a rel=” canonical” – it’s more likely not shown.”

John summarized, “ You can also do both of them. If external links, for example, are pointing at this page, then having both of them there helps us to figure out well, you don’t want this page indexed, but you also specified another one, so maybe some of the signals we can just forward along.”

28:26 “[…] We optimize our site accordingly [for mobile-first indexing]. As for the configuration, Google recommends two ways of doing it. The first is a responsive web design and the second is a dynamic serving. Because the first way is a little difficult for us to achieve through our tech environment, we use the second way. But we still see that nowadays, there are over two hundred thousand daily crawls towards our mobile domain. Is this a normal thing to see? […] We had the m-dot domain, then we redirected it to the main domain.”

John answered, “Some amount of crawling like that is normal. It takes a very long time for our systems to completely stop crawling a domain even after it’s redirected, so I wouldn’t see that as an issue. Our systems have a very long memory for things like this sometimes, and if you move a site from one domain to another, or if you make this mobile change with a subdomain, sometimes that takes years for the crawling to stop completely.”

36:00 “ Is there any relation or impact upon the rankings for the websites which are made with normal HTML, CSS, JS, and another one – PWA? […] One of our main competitors has recently adopted it, and we noticed a huge jump into their SERP rankings.”

John said, “These are essentially different ways of making a website, and you can make a website with lots of different frameworks and formats. For the most part, we see these as normal HTML pages. So if it’s a JavaScript-based website, we will render it and then process it like a normal HTML page. If it’s HTML already in the beginning, we can do that. [There are] different frameworks and CMSs behind it. Usually, we basically ignore that and just say, well, here’s an HTML page, and we can process it.

So just the fact that one of your competitors has moved from one framework to another and has seen an improvement in search, that framework change, from my point of view, wouldn’t be kind of responsible for that. But rather, maybe they have a newer website now, together with that framework change. Maybe the newer website has different internal linking, different content internally, [it] is significantly faster or significantly slower, users really like it, or they did a marketing campaign together with the website launch. All of these things play in there, and these are all things that are not limited to the framework that you’re using.”

37:39 “Are the results in the lab data in Google PageSpeed Insights the same as Lighthouse results in my Chrome browser? Do they use the same formula?”

John said, “I don’t know one hundred percent, but they are done completely differently. […] If you use PageSpeed Insights that is run on a data center somewhere with essentially emulated devices where we try to act like a normal computer, and we have restrictions in place that make it a little bit slower. […] In Lighthouse, it basically runs on your computer with your internet connection. I think Lighthouse within Chrome also has some restrictions that it applies to make it look maybe a little bit slower than that your computer might be able to do just to make sure that it’s comparable.

But essentially, these run in completely different environments, and that’s why you would often see different numbers there. […] If you test with other speed tools that run online, you might [also] see different numbers. Also, the field data, the data that we use for search ranking that you see in Search Console, can be also completely different numbers just because your users might have, on average, a different kind of device or different kind of internet connection. So even if the formulas are the same, the whole environment around these systems is very different.”

Want to learn the difference between field data and lab data ?

Read the article on our blog to learn about these two ways of measuring web performance .

47:09 “We have noticed a big problem with Google Discover on our website. In two days, the traffic dropped by seventy percent. […] So we’re wondering if we did something wrong? […] Can you clarify as to what exactly happened since it’s such a drastic draw? […] Could it be a technical error?”

John said, “I don’t know specifically with regards to your website, but I get reports from a lot of people that Discover traffic is either on or off in the sense that there’s very little room in between in that if our algorithms determine we’re not going to show much content from this website in Discover at the moment then basically all of that traffic disappears. In the other way, it’s the same thing where if we do show something from your website in Discover, then suddenly you have that big rush of traffic again.

If it’s a technical issue, then you would see that in web search as well, and you would see crawl issues showing up. I don’t have full insight into what exactly happens in Discover, but usually, the issues that I see people talking about are, on the one hand, quality issues where maybe the quality of the website is not so good and with regards to the individual policies that we have for Discover. In particular, for Discover, we have some policies that are different from web search and recommendations that are a bit different with regards to, I think, adult content, clickbaity content. […] That’s all mentioned on the Help Center page that we have for Discover. I imagine a lot of websites have a little bit of a mix of all of these things, and I sometimes suspect our algorithms just find a little bit too much, and then they say, oh, we have to be careful now with this website. So without knowing your website and without knowing the details of what exactly Discover is picking up there, that’s the direction I would head there. […]

From our point of view, Discover is where we try to show a stream of information to people, and because of that, we tend not to have a lot of detailed information on what exactly you need to provide there to perform really well. So sometimes it makes sense to look at what other people have figured out.”

50:41 “What would be a good response time for a new news media site?”

According to John, “ The response time is something that plays into our ability to figure out how much crawling a server can take. Usually, the response time, from a practical point of view, limits or plays into how many parallel connections would be required to crawl. So if we want to crawl one thousand URLs from a website, then the response time to spread that out over the course of a day can be pretty large. Whereas if we want to crawl a million URLs from a website and a high response time is there, then that means we end up with a lot of parallel connections to the server. I think we have some limits there with regards to we don’t want to cause issues on the server, so that’s why the response time is directly connected with the crawl rate.

For a news website, it’s not so much a matter of is it news or not, but rather the number of URLs that we need to crawl per day. So that’s the angle I would look at there. It can be that on a news website, we crawl ten thousand pages a day, and those are the important news articles that are all covered. It might be that we have to crawl millions of articles a day because we always have to refresh the archive […], then obviously the response time, the crawl rate, looks different.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
