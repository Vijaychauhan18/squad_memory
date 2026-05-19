---
source: https://www.onely.com/blog/seo-office-hours-october-8-2021/
title: SEO Office Hours - October 8, 2021
scraped: 2026-03-23
published_on: 2021-10-15
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

# SEO Office Hours - October 8, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-october-8-2021/
Published: 2021-10-15
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Read the newest posts on our blog to make sure you're not missing out on anything!

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on October 8, 2021.

03:52 “So you’ve recommended several times in the past that large sites […] focus on a smaller set of pages […]. The site I’m working on right now, we have […] like 1,000 pages that don’t get any traffic, that are old, so I’ve been recommending to remove those. But there’s a question that our dev team has that they were under the impression that the more pages that Google has indexed of your site, the higher authority it ascribes to the site, and are reticent to remove any pages. Could you shed some light on that?”

As John said, “It’s definitely not the case that if you have more pages indexed that we think your website is better. […] Sometimes, it makes sense to have a lot of pages indexed. Sometimes, they’re kind of useful pages to have indexed like that. But it’s not a sign of quality with regards to how many pages that are indexed. And especially if you’re talking about […] 1,000, 2,000, 5,000 pages, that’s a pretty low number for our systems in general. And it’s not that we would say 5,000 pages is better than 1,000 pages. For us, it’s all kind of like, well, it’s a small website, and we make do with what we can pull out there. And of course, small website is relative. It’s not like saying it’s an irrelevant website. It might be small, but it might still be very useful […]”.

10:03 “Last time we talked about some problems with the website […] – it’s an e-commerce website where we have informational stuff and transactional stuff. […] Your advice was to separate this content a little bit into transaction-oriented and information-oriented pages. So I have another question regarding this. If you have, let’s say, an e-commerce website, and you have a huge blog, or a magazine, or something like that where you have loads of informational stuff, but it’s an old section. And on the other hand, you have all these product pages, and categories, and so on. So would this huge block with pure informational stuff give the whole website kind of an informational touch or character so that Google says, oh, we are not sure if this is […] something where people can get information rather than buying stuff, or is this evaluation done on a per-page base?”

John said: “[…] My understanding is that this is more of a page-level thing. […] A lot of websites just have a mix of different kinds of content. And then you try to figure out which of these pages match the searcher’s intent and try to rank those appropriately. […]

I mean, you see that with news websites often. […] They have the recent events, but they also have sections for older events that took place, or […] for other big events, they kind of have an isolated archive section. And those are very different intents, if you want something really now that is happening or if you want some kind of informational research, evergreen-type content.

[…] We kind of have to look at it on a per-page basis , and not say, oh, this is a research website because there’s some research content here”.

13:21 “We are seeing that people are linking to […] our, let’s say, subcategory of pages. And the problem is that […] our content comes and goes, which means that sometimes, there is more content appearing in some categories. Sometimes, the content gets deleted. And so subcategories can be created and can disappear as well. And we are seeing a bunch of referrals from backlinks because they are linking to subcategories that no longer exist. My question here is: is it OK to redirect […] these links to the parent category. And if we do so, how do we do that – with 302, for example? Like a temporary redirect, because in the future, this subcategory might be populated with content again, […] it’s not a permanent redirect”.

John responded: “So if we see this happening at a larger scale that you redirect to the parent level, we would probably see that as a soft 404. […] And instead of a 404 code, you’re redirecting, and maybe that’s better for users, but we see it as a 404. […] If it makes sense from a user point of view to redirect, then I would just go for it.

[…] With regards to 301 or 302, I don’t think it matters there, because we would either see this as a soft 404, or we would see it as a canonicalization question. If it’s a soft 404, then the code doesn’t matter. If it’s a canonicalization question, then it comes down to which URL we show in the search results. And usually, the higher-level one will have stronger signals anyway, and we will focus on the higher-level one. So that doesn’t matter if that’s a 301 or a 302 in that case.

[…] If we see it as a soft 404, […] we would slow down crawling of that particular URL because there’s nothing here […]. If we see it as a redirect […], we don’t need to crawl this every day, because we focus on the primary URL. So I think in both of those cases, we would slow down crawling of that URL until we get new signals that tell us, actually, this is maybe something new again. […] That would be like internal linking, or sitemap file […]. And that would be the stronger sign for us to crawl again. But I think the slowing down of crawling would be similar in all of these cases.

[…] I think [updating] site maps alone is probably not enough. I would really make sure that the internal linking is also clear ”.

18:34 “So about a year ago, we saw some significant decrease in traffic. After the audit, […] all the signals pointed to the site having site quality issues. We were able to address those issues by February this year. And by June core update, we saw some increases. But it’s still not to the level where we used to be before the decrease about a year ago. So my question is the site quality issues, if that’s been the case, is this the recovery that we can expect, or can we expect more recovery if we think we’ve addressed all the issues identified […]?”

John said: “[…] It’s not so much that we would consider it as a situation where you have to fix something. But rather […] if you work on improving the relevance of your website, then […] you have a better website. So it’s not that […] we will change it back to the previous state. […] It’s not the same or comparable to before, so it would be kind of tricky to expect that it changes to the state it was before […].

[…] With the core updates, we don’t focus so much on just individual issues, but rather the relevance of the website overall . And that can include things like the usability, and the ads on a page, but it’s essentially the website overall. And usually, that also means the focus of the content, the way you’re presenting things, the way you’re making it clear to users what’s behind the content, like what the sources are […] . If you really want Google to see your website as something significantly better, you probably also need to work on the content side .

[…] Think about where might there be low-quality content, where might users be confused when they go to my website. And is that confusion something we can address with technical issues, with UX changes? Or do we actually have to change some of the content that we present?”

28:24 “[…] If [a website has] a guest post, and Google does not know whether it’s paid or not, how will Google then determine that [they should] take this link or burn this link? What is the answer so we are safe from all the angles?”

According to John, “[…] Our guidance for links and guest posts is that they should be no-follow . […] I would just really watch out to make sure that the links are no-follow so that you’re driving awareness, you’re talking about what you’re doing, you’re making it so that users can go to your page. But essentially, it’s an ad for your business. So from that point of view, I would just make them no-follow”.

32:25 “If there are two competing e-commerce sites that sell exactly the same product – one website offers the product at $500, the other at $100, all SEO signals are equal. Would the less expensive website have a better chance of ranking because there’s such a price difference for the exact same product?”.

John said: “So purely from a web search point of view, no. It’s not the case that we would try to recognize a price on a page and use that as a ranking factor. So it’s not the case that we would say we’ll take the cheaper one and rank that higher […].

However, a lot of these products also end up in kind of the product search results, which could be because you submit a feed, or it could be because we recognize the product information on these pages. And the product search results, I don’t know how they’re ordered. It might be that they take the price into account or things like availability […].

So from a web search point of view, we don’t take the price into account. From a product search point of view, it’s possible . And the tricky part, I think, as an SEO is these different aspects of search are often combined in one search results page, where you’ll see normal web results, and maybe you’ll see some product results on the side, or maybe you’ll see some mix of that […]”.

34:04 “If we have 200 sitemap files, and 20% to 30% of the URLs jump from one file to another every week, how bad can it be? Or should we strictly keep our URLs in the same file forever?”

“[…] Our recommendation is usually to keep the same URL in the same sitemap file . The main reason for that is we process sitemap files at different rates. So if you move one URL from one sitemap file to another, it might be that we have the same URL in our systems from multiple sitemap files. And if you have different information for this one URL – like different change dates, for example – then we would not know which attribute to actually use.

So from that point of view, if you have it always in the same sitemap file, then it’s a lot easier for us to say, oh, we have the information for this URL here, and we can trust that information because it’s only there. So that’s something where I try to avoid […] these URLs shuffling around randomly. But at the same time, it’s usually not going to break processing of your sitemap file. And it’s definitely not going to have a ranking effect on your website. So there’s nothing in our sitemap system that kind of maps to the quality of a website ”.

38:13 “I work in the news vertical. My team is looking to expand our international presence, and have done work to set up multi-regional subdirectories. For the most part, pages across the different multi-regional editions will look the same. Homepage and section pages like politics or lifestyle will have similar content minus a few pieces unique to the region.

The articles are tricky. There is not much we can differentiate across multi-regional subdirectories outside of modules with related links, which leaves us worried about duplicate content issues. How does Google handle duplicate content in the news space? […] The content stays the same, but elements of the template are different. Should there only be one canonical across all multi-regional websites?”

John’s response was: “[…] It sounds these are different regions within the same country, and it’s same language content. […] If these are different countries, then you have the aspect of geo-targeting, which plays a role if these are different languages. So if you’re working, say, in Europe, and you’re covering Germany, and France, and Italy, or something, then you have different languages as well.

[…] But if you’re talking about within the same country, same language content, then […] it’s a little bit easier because you don’t have to worry about all of these technical connections. But on the other hand, the duplicate content issues are a lot more visible. And when it comes to duplicate content, the tricky aspect on sites like these is that you essentially end up competing with yourself. And if you have one news article that you publish across […] five or six different regional websites, then all of these different regional websites try to rank for exactly the same article. And that could result in that article just not ranking as well as it otherwise could.

So because of that, I would recommend trying to find canonical URLs for these individual articles so that you can really say ‘well, I have this one article on my five regional websites, but this is my preferred version that I want to have seen in search’. And then we can concentrate all of our energy, all of our signals, on that one preferred version, and we can try to rank that one a little bit better. It doesn’t have to be the same version all the time. So it can definitely be the case that you have one news article that is within one region kind of be canonical, a different news article is more canonical for another region. How you pick which region you choose as canonical is totally up to you. […] Usually, you would try to figure out where is it the most relevant, and pick that one as the canonical version. So that’s for the individual articles themselves.

For the categories, and the sections, and the home pages, it seems like that would be something where the content is more unique, and more specific to the individual regions. And because of that, I would try to just keep those index-level separate. So if you have five different regional websites, their home page, their category sections, they would all be individually indexed. And the news articles themselves would be mapped to one of these different regions. So that’s kind of the approach that we recommend there […].

And this approach also […] works across different domain names. So if you have different domains for individual regions, but it’s all a part of the same news group, you can still do this canonical shifting across the different versions. If you’re doing it within the same domain with subdirectories, that’s fine too”.

If you want to add multi-regional editions to your website, take a look at our chapter on duplicate content in our International SEO guide.

44:34 “What is the best course of action to take when you have to 301 redirect all of the URLs to a new set of URLs? The number of pages will be over one million, and you want to minimize the sandbox effect? If there is a sandbox effect, how long could it be? Would we lose ranking that we might never recover? We plan on doing a one-to-one redirect, and had requested batch redirects, but that’s not a possibility, so pages, images, URLs, etc. would have to flip at the same time”.

As John said: “To me, this sounds like a traditional site move situation. You move from one domain to another, and you redirect all of the URLs from your old site to a new one, and we have to deal with that […]. There is definitely nothing defined as a sandbox effect on our side when it comes to site move . So if you have to do a site move, then do a site move, and redirect all of your pages. It’s often the easiest approach is just to redirect all pages at once. Our systems are also tuned to that a little bit to try to recognize that. So when we see that a website starts redirecting all pages to a different website, then we’ll try to reprocess that a little bit faster so that we can process that site move as quickly as possible. And it’s definitely not the case that we would say, oh, they’re doing a site move, therefore, we will slow things down […]”.

46:13 “I have a website that connects to APIs on the client-side to get data. Are those URLs being included in the crawling budget? If you disallow those URLs, […] would that create any issues?”

“[…] If these APIs are included when a page is rendered, then yes, they would be included in the crawling, and they would count towards your crawl budget essentially because we have to crawl those URLs to render the page. You can block them by robots.txt if you prefer that they’re not crawled or not used during rendering. Totally up to you if you prefer doing that. Especially if you have an API that is kind of costly to maintain or takes a lot of resources, then sometimes, that makes sense.

The tricky part, I guess, is if you disallow crawling of your API endpoint, we won’t be able to use any data about the API returns for indexing. So if your page’s content comes purely from the API, and you disallow crawling of the API, we won’t have that contact. […] If the API just does something supplementary to the page, like maybe draws a map or […] a graphic of a numeric table that you have on a page, […] then maybe it doesn’t matter if that content isn’t included in indexing. The other thing is that sometimes, it’s non-trivial how a page functions when the API is blocked. In particular, if you use JavaScript and the API calls are blocked because of robots.txt, then you have to handle that exception somehow. And depending on how you embed the JavaScript on the page, what you do with the API, you need to make sure that it still works. So if that API call doesn’t work, and then the rest of the page’s rendering breaks completely, then we can’t index much because there’s nothing left to render.

However, if the API call breaks, and we can still index the rest of your page, then that might be perfectly fine. […] I think it’s trickier if you run an API for other people, because if you disallow crawling then, you kind of have this second order effect that someone else’s website might be dependent on your API. And depending on what your API does, then suddenly, their website doesn’t have indexable content. And they might not even notice because they weren’t aware that suddenly, you added a disallow there. And that might cause kind of like indirect effects […]”.

49:36 “So there are two pages that originate from the same domain. The URL is a bit different, which is a part of the same directory structure. And […] they are generated by NextJS. So NextJS is a server-side rendered react framework. And they are being indexed, but I see one page in the Google cache, and the second page is not in the Google cache. And I see the same pattern regardless of how I generate the page […]. Most of my pages are in Google cache, but now I’m worried because I’m currently moving from my Java-based tech stack, which generates all these pages, to Google NextJS. […] When I was debugging, I found that this is also a problem with the older Java stack that we were using.

So the question is two parts. Basically, why this behavior? And second is, will this behavior impact my ranking? I see those pages appearing in search results which are not in Google cache”.

John answered: “[…] The cache pages are completely separated from what we index. So if there is a cache page or not, it doesn’t matter at all for ranking, it doesn’t matter at all for indexing . Sometimes, there are technical reasons why we don’t have a cache page. Sometimes, we just don’t have a cache page for individual URLs. The other thing is if the page is using a JavaScript framework, then whether or not that JavaScript runs on a cache page is sometimes tricky, because the cache page is hosted on a Google domain. Depending on what kind of JavaScript you have, where it pulls the JavaScript files in, sometimes, the JavaScript can’t run on the Google domain.

[…] The cache page is not the rendered page. It is essentially just the HTML file that we requested, and a copy of that. And if the HTML file shows something, that’s fine. If it uses JavaScript, and the JavaScript doesn’t run because it’s a cache page, that’s equally fine. You just don’t see it in the cache page. So if the cache page doesn’t show, I would not worry about that. That’s not a sign of any issue. And often, […] you can’t control if there’s a cache page or not. I would just ignore that”.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
