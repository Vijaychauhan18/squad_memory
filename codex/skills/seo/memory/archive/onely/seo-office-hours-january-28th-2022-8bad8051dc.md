---
source: https://www.onely.com/blog/seo-office-hours-january-28th-2022/
title: SEO Office Hours, January 28th, 2022
scraped: 2026-03-23
published_on: 2022-02-01
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

# SEO Office Hours, January 28th, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-january-28th-2022/
Published: 2022-02-01
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on January 28th, 2022.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on January 28th, 2022.

John answered, “Not necessarily. I think for internal links, on the one hand, we use it to understand the context better. […] But another really important part is being able to crawl your website. For that, it doesn’t matter where that link is on a page to crawl the rest of the website. Sometimes things are in the footer, headers, sometimes in a shared menu, sidebar, or within a body of content. All of those linked places are fine from our point of view.

Usually, what we differentiate more, with regards to location on a page, is the content itself to try to figure out what is relevant for this particular page. For that, it sometimes really makes sense to focus on the central part of the page, the primary piece of content that changes from page to page, and not so much the headers, sidebars, footers, or things like that. […] Those are a part of the website itself, but it’s not the primary reason for this page to exist and the primary reason for us to rank that page.

So that’s the difference that we take when it comes to different parts of the page. And for links, it’s usually more to understand the context of pages and to be able to crawl the website. And for that, we don’t need to differentiate between different parts of the page.”

24:11 “We have a website which had a malware attack last December. We have cleaned it up, and we made sure there’s no security issue in the Google Search Console. But the unwanted pages which were indexed [in] the result of malware are still being shown in the search results. […] What can we do?”

John said, “First of all, I would double-check that these pages are removed because some types of website hacks are done in a way that if you check manually, then it looks like the page is removed but actually for Google, it’s still there. So I would check with the [URL Inspection] tool some of those pages to double-check [if] it is completely cleaned up or is there something left over that is trying to hide. I think that’s the basis of everything else.

Then for the rest, there are two approaches that I recommend. On the one hand, the best approach is to make sure that the more visible pages are manually removed. That means searching for your company name, website name, […] primary products, those kinds of things, and seeing the pages that show up in the search results and making sure that anything that you don’t want to have shown is not shown. Usually, that results in maybe up to 100 URLs where you’re saying these are hacked, and I want them removed as quickly as possible. For those, use the Removals tool. That’s essentially the fastest way to clean things up. The Removals tool takes those URLs out within about a day, especially for things that would be visible to your users that take care of that.

The other part is, the URLs that are remaining will be recrawled over time. But […] when it comes to lots of URLs on a website, that’s something that takes a couple of months. So, on the one hand, you could leave those be and say, well, they’re not visible to people unless you explicitly search for the hacked content or do a site query of your website. They will drop out over time. Leave them be for half a year and then double-check afterward to see if they’re completely cleaned up.

If you want to try to resolve that as quickly as possible, you can also use the Removals tool with the prefix setting and essentially try to find common prefixes for these hacked pages, which might be a folder name, file name, or something that’s in the beginning and filter those out. The Removals tool doesn’t take them out of our index, so it doesn’t change anything for the ranking, but it doesn’t show them in the results anymore. That’s one way you could go past just the more visible pages to try to clean the rest up.

Personally, I don’t think you need to clean up all of those pages because if users don’t see them, then technically [these pages] exist in the search results, but if no one sees them, it doesn’t change anything for your website. So from that point of view, I would focus on the visible part. Clean that up, and when that’s done, just let the rest work itself out.”

Are your pages “Blocked by page removal tool” in Google Search Console? Read my article to learn how the URL removal tool works in the wild and how to fix this issue.

28:39 “We have a website with valid URLs with quality content. They’re following the guidelines mentioned in the Google Search Central. […] But sometimes it takes ages to index those URLs. […] I wish we have a tool that we can use to index them faster.”

John: “[…] I think, overall, there is the Submit to indexing tool or functionality in Search Console that’s what we recommend for these things. But at the same time, we don’t index everything. It can very well happen that you have something that is a valid page, but we don’t index it. I think one of the reasons that go in that direction is, nowadays, almost all pages are valid pages, and it’s really hard to set up a CMS where you produce pages that are invalid. If you use WordPress or any of the common systems, it just produces valid pages by default.

From a technical point of view, we can’t index everything on the web, so we have to draw the line somewhere. It’s completely normal for websites to have parts of their content indexed and parts of their content not indexed. Usually, over time, as we understand that this is a really good website and if it has a reasonable internal structure, then we can pick up more and more, but it’s not a guarantee that we’ll index everything on a website. So that’s something to keep in mind. Especially in Search Console, it’s easy to look at the reports and say, oh, these pages are not indexed, therefore I’m doing something wrong. But from our point of view, it’s normal that not everything is indexed. It’s just a lot more visible nowadays, I think.”

33:04 “ Can you give [any] recommendations for emojis used in title and meta description? Are they affecting SEO or not?”

According to John, “You can definitely use emojis in titles and descriptions on your pages. We don’t show all of these in the search results, especially if we think that it disrupts the search results in terms of it looks misleading, perhaps. […] But you can keep them there. It’s not that they cause any problems.

I don’t think you would have any significant advantage in putting those there. At most, what we try to figure out is what is the equivalent of that emoji. Maybe use that word as well associated with the page, but it’s not that you get an advantage for […] a colorful title. From that point of view, if you like to have these in your titles and descriptions, go for it. If you don’t want them there, then that’s fine too. I don’t think it hurts or harms SEO or helps SEO in any way.”

36:15 “W e have FAQ schema on quite a few articles that do not show any technical errors in GSC. Are there non-technical reasons why Google does not show our FAQs in the SERPs below the post? Could it be a trust issue with the content on our site?”

John’s response was, “ FAQ rich results are essentially similar to other types of rich results in that we have several levels that we take into account before we show them in the search results. On the one hand, they need to be technically correct. It sounds these are technically correct. On the other hand, they need to be compliant with our policies. I don’t think we have any significant policies around FAQ rich results other than that the content should be visible on the page. The third issue that sometimes comes into play here is we need to be able to understand that this website is trustworthy in that regard that we can trust this data to be correct. That is something where, from a quality point of view, we’re maybe not convinced about a website, and then we wouldn’t show it. But those are the three steps that I would look at. […] If that’s all correct, then I would think about what could I do to significantly improve the quality of my website overall.”

37:38 “ We would like to expand existing pages with more up-to-date content, e.g., on seasonal topics or events. What do we do with such pieces of content when the season or event (e.g., Black Friday) is over? Just leave these sections on the page permanently, or remove them after the event and add them again next year?”

John answered, “From our side, it’s totally up to you how you deal with this. Keeping the pages there is fine, removing them after a while is fine if they’re no longer relevant. Essentially, what you would probably see is that traffic to these pages will go down when it’s not seasonal. If people are not looking for Black Friday, then they’re not going to find your Black Friday pages. Then it doesn’t matter if you have that page or not because you’re not missing out on any impressions there. If you make this page noindex, or if you make it 404 for a while and then bring it back later, that’s essentially perfectly fine.

The one thing I would watch out for with seasonal pages is that you reuse the same URLs year after year. So instead of having a page that is called Black Friday 2021 and then Black Friday 2022, have a page called Black Friday. That way, if you reuse that page, all of the signals that you have associated with that page over the years will continue to work in your favor rather than you having to build up new signals for every year for a seasonal event like this. That’s the main recommendation I have there.

If you delete these pages when you don’t need them and recreate the same URL later, or if you keep those pages live for a longer period of time, I think both of those are essentially perfectly fine. Especially about competitive seasonal events like Black Friday or Christmas […], it is something where I tend to see sites create those pages a little bit ahead of time. Even if they don’t have a lot of content to share there yet, they can start building up some signals for those pages. That could be with regards to internal and external links, marketing efforts, or whatever. By having those pages a little bit ahead of time, even if you don’t have a lot of content on them, it’s a little bit easier to be there when it is suddenly seasoned.”

40:19 “ How big is the impact on Google ranking if I have a bad CLS score ? FCP , FID , and LCP have good scores, only CLS is not so good.”

John said, “We don’t have anything like a fixed number with regards to how strong these scores work for a website. It’s really hard to say how bad is it or how big is the impact.

From our point of view, we do take these metrics into account when it comes to the Core Web Vitals and the Page Experience ranking factor. We try to look at them overall. And we try to focus especially […] where you’re in that reasonable area with regards to these scores. […] As soon as you’re out of that bad section, then that’s something that we can say, well, this is reasonable, and we can take into account. We don’t have any fixed rankings or algorithmic function where we say, well, we take one half of FCP and one half of CLS, and we take one-third of this into account. It’s something where we need to look at the bigger picture, and it can happen that over time we change things around a little bit to make sure that we’re flagging or treating the Page Experience of pages appropriately.

Especially with regards to the Page Experience ranking factor that is something where from year to year we will make changes as well, so I would expect, whenever they review this, they’ll probably pre-announce some other changes or other factors that come into play here, similar to how we introduced the desktop aspect of that as well, which we talked about, I think, last year sometime and it’s coming into play later this year.”

42:33 “ Can poor Core Web Vitals scores be a site quality issue that limits crawling or limits how many pages on a site end up being indexed?”

John: “It’s really hard to look at this without looking at a specific website. But, essentially, the Core Web Vitals plays into the Page Experience ranking factor, and that’s more of a ranking factor, that’s not a quality factor. In particular, it doesn’t play in with how much we crawl and index from a website. In some cases, there is a little bit of a relationship between how fast the page is and how fast we can crawl it, but it doesn’t have to be that way. So that’s something where usually these sides are less connected and not completely tied together.

In particular, when it comes to Page Experience, the time it takes for a page to load depends on so many factors, more than just that one request to the server, it can be that maybe you have fonts on this page or maybe you have large images that are pulled in from other sites, all of these things are elements that play into how fast the page loads for a user, but don’t map to how fast we can crawl a page. Obviously, if your server is so slow that any request made to the server takes a couple of seconds, then that’s something where I’d say, well, your page will be slow, and Google’s crawling will be slow just because we can’t crawl as much as we would like.

But for the most part, if you’re talking about some pages are good and crawling is reasonably fast, then I wouldn’t expect to see a relationship between the Core Web Vitals scores and the crawling and indexing of a website.”

53:25 “I know Google generally recommends against geo redirects on websites for a whole bunch of reasons. The fact that Googlebot will be able to properly crawl and index all of the sites, for example. […] I’m wondering if the situation is different for news content or news websites? A number of major news providers […], all have had geo redirects in place for quite a few years, and none of them seem to be experiencing negative effects on the ability of their content to be indexed.”

According to John, “That applies to all kinds of websites. From our point of view, usually, the geo redirects are more a matter of making it technically hard for us to crawl this content. Especially if you’re redirecting users from the US to a different version of a website, then we will follow that redirect because Googlebot usually crawls from one location. Then it’s less a matter of quality signals. […] It’s more that if Google can’t see your web pages, then we can’t index them, and that’s essentially the primary reason why we don’t recommend doing these things.

I don’t know if some of these sites are doing something where some users are being redirected, and others are not being redirected. Maybe Googlebot is not being redirected. It’s possible. From our point of view, I don’t think that would do them any favors because it would usually end up in a situation where you have multiple URLs with the same content in the search results, and you’re competing with yourself. Then it’s less a matter of doing something sneaky and sneaking your way into the results, but more like you’re duplicating things on your site. We’re finding your content multiple locations, we don’t know which one to rank best, so we’ll have to make a guess at that.

From that point of view, my suspicion, without checking any of these sites offhand, is that we’re aware of these geo redirects. We’re seeing them take place and, from a technical point of view, [we’re] trying to crawl and index the right pages there, but not that there’s anything sneaky happening behind the scenes there.

It’s also not the case that we would see this as a kind of an attempt of cloaking or something that would be against the Webmaster guidelines. From a technical point of view, if you make it hard for us to find and index your content, it’s going to be hard for us to do what you want us to do. That’s why we have these recommendations.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
