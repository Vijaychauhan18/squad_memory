---
source: https://www.onely.com/blog/seo-office-hours-march-4th-2022/
title: SEO Office Hours, March 4th, 2022
scraped: 2026-03-23
published_on: 2022-03-22
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

# SEO Office Hours, March 4th, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-march-4th-2022/
Published: 2022-03-22
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on March 4th, 2022.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on March 4th, 2022.

7:41 “John, so my first question is, Google Search Console is throwing an error […] in required structured data element. But when I check the same on validator.schema.org, it does not show any warnings or any errors. So the first question is, is it the right site to check the AMP implementation of a web page? […]“

John replied, “ Yeah, so these testing tools are for slightly different purposes. That’s probably why you’re seeing that difference. The testing tool in schema.org is more about understanding schema.org markup in general, like overall, based on the requirements that schema.org has. And the testing tool in Search Console is focused purely on what we can pull out of the structured data and use to show in the Search feature. So it’s really focused on the Search part of that story. And within Search, we only use a small part of the schema.org markup. And sometimes, we have slightly different requirements that maybe we require a specific element more than the base schema.org markup would require. And that’s often why you see that difference. And the schema.org validator is for the theoretical markup, and the Google validator is really for the practical Google Search side of things. “

9:20 “[…] Basically, it’s not an error. It’s a warning in Search Console. And when I check the details in Search Console, it just says that you’re not doing it right. So will there be a possible way [to fix the issue], or should my dev team figure it out?

John explained, “Yeah, if it’s a warning, then I wouldn’t worry about it. It’s basically just saying you could have done something differently. […]. What I would do if you want to find out what exactly the difference is, is double-check the documentation on developers.google.com for Search, where we have all of the structured data documented and all of the required and recommended fields. And probably one of the recommended or optional fields is what is triggering this warning.”

14:11 “ What’s the possible reason that […] certain pages didn’t get indexed, even though they were crawled multiple times? ”

John replied, “ It can happen. I would assume it’s not that frequently because, usually, when we decide to crawl something, we’re also pretty happy to go off and index it. But it can happen that we crawl a page and then, in the end, decide, actually, we don’t need to index it.

[…] some common situations where that can happen, which perhaps don’t apply in your case, is if there is an error code on the page. We have to crawl it first, and then we see the error code. If there’s a noindex on the page, we also have to crawl it first, and then we see the noindex. If the page is a complete duplicate of something else that we’ve already seen, then we crawl it, we see it’s a duplicate, but we focus on the primary page again. So those are kind of the normal situations where we would crawl something and not index it. But it can also happen that we crawl something and then, by the time we get to indexing, we decide, oh, well actually, we want to get something else from the website instead. ”

Google Search Console notified you about indexing problems due to duplicate content? Read our guides and fix:

15:41 “[…] what other factors [besides the ones already mentioned] may cause Googlebot to decide, oh, we don’t want to index it at the end?”

John said, “I don’t know offhand. I think the overall website quality definitely plays a role there, but usually, if we’re not convinced about the website quality, then we would probably not crawl the page in the first place. So that’s, I think, kind of a tricky situation. And if you look in Search Console, I think, pretty much for every site, you will have the grouping of discovered but not indexed and also crawled and not indexed. That’s, I think, just pretty common across sites.”

The person asking the question wanted to know if there’s something else they should look into except page quality and technical issues. John recommended they shouldn’t focus too much on one page, “ I also think it’s important to not overfocus on that specific page. So if you’re sure that, from a technical point of view, everything is OK, I wouldn’t assume that the quality of that specific page is a problem, but rather kind of the perceived quality of that part of the website or the whole website itself. That’s kind of the place where I would try to see what you can do to improve things, not just that individual page tha t didn’t get indexed, but kind of what is the bigger picture around that page. ”

21:48 “ So we run an eCommerce website, and we are now in a stage where we want to make major updates to our category pages. […] in one draft, we want to get rid of the product listings. So you have the product listings with the faceted search, where you can filter for the products you are looking for. […] when we remove the whole product listing of category pages, would we have a disadvantage in the rankings because, first, all the other competitors have these kinds of product listings? And second, my guess is this is such an established element for eCommerce pages that the users expect […] to have some kind of overview of all the products and the filters let them search for the products they want. ”

John replied, “ I wouldn’t see any problems there from an SEO point of view. I think there are different things you would want to watch out for, […] so that we can still find all of the individual products that we have clean links there. But if you’re just kind of redesigning this category page and making it look more like an informational page, I wouldn’t expect any problems with that. I also don’t think we do anything special with those kinds of category pages in Search anyway, so from that point of view, you’re just changing the design, essentially.

I think it would be different if it was a product page, and you were to change it completely because we do try to recognize product pages and figure out where’s the price, where’s the availability , those kinds of things. And if you made it look completely different […], then I could imagine that affects how we pick up the product pages and if we can show it in Product Search results or not. But the category pages, as far as I know, we don’t do anything special with them. So if you hide them, essentially, and make sure that we can still find the links to the products […] you could do that. But if you want to make them more useful by providing more information on them, I think that’s a good idea.”

At the end of the question, John added that it’s important to check the changes from the user’s perspective : “[…] you mentioned ‘would users be confused’. I would double-check that. So from the SEO side of things, I think that’s perfectly fine, but from the user side of things, it’s probably something you’d want to test first.”

25:18 “ If you have structured data for breadcrumbs setup, is internal linking still important for SEO?”

John replied, “Yes, absolutely. It’s something where internal linking is supercritical for SEO. I think it’s one of the biggest things you can do on a website to guide Google and guide visitors to the pages you think are important. And what you think is important is totally up to you. You can decide to make things important where you earn the most money, or you can make things important where you’re the strongest competitor, or maybe you’re the weakest competitor. With internal linking, you can really kind of focus things on those directions and those parts of your site. And that’s not something that you can just replace with structured data.

So, just because there is structured data on a page somewhere, I wouldn’t see that as a replacement for normal internal linking. Even if in the structured data, you also provide URLs, we don’t use those URLs in the same way as we would use normal internal links on a page. So it’s definitely not the case that hreflang annotations replace links between country versions, or breadcrumb annotations replace links between different levels of a website. You should really have normal HTML links between the different parts of your website. And, ideally, you should not just have a basic set of links, but, rather, you should look at it in a strategic way and think about what do you care about the most, and how can you highlight that with your internal linking? ”

Let us help you with optimizing internal links! Resolve your doubts and contact Onely for thorough internal linking optimization.

29:50 “ For a product listing page, can we implement multiple product schemas on the product listing page? ”

John said, “ From our policy point of view, I don’t think you should be doing that, at least the last time I checked the policies around structured data, because for product structured data, we really want that to apply to the primary element of the page. And if you have multiple products on a page, it’s not that one of them is the primary element of the page. So from that point of view, you should not use multiple products structured data elements on a category page […]. ”

30:30 “ Is there a best practice for pages with mixed language used? For example, our international school in Japan caters to Japanese and non-Japanese families, but we keep most of the information on our home page in English. We add support on the page in Japanese as well. […] Since our communication in real life is mixed language, having the home page reflect that felt more natural. Are we punished in search if a page is an intentionally mixed language?”

John replied, “I wouldn’t necessarily say that a page is punished in a case like that. But we do try to understand what the primary language is of a page, and that helps us to understand for which kind of queries we would be able to show this page. So that, I think, is kind of tricky in a case like this.

We can understand when there are multiple languages on a page too. It just makes it a lot easier for us to really be clear that, if someone is searching in English, this is the right page to show to them. So I could imagine for something like a home page, maybe it makes sense to have that mix or a slight mix. If you have one home page as primary English, then maybe include some elements in Japanese. If you have another version that’s primarily Japanese, with some elements in English, it’s fine. But it helps us to really understand that, for the most part, this is an English page. And if someone is searching in English for a specific kind of international school in Japan, then it makes sense for us to say, well, here’s an English piece of content that we know fits your needs and that matches the queries that you gave us. So from that point of view, I wouldn’t necessarily say that the page is punished, but it makes it a lot harder for our systems to figure out how to rank that page properly.

One of the things you can think about here is to look in Search Console at what queries are going to your website or for your home page. And think about which of these queries might be affected if Google didn’t understand the language properly. And it could well be that if most people are searching for your name or the brand of your school, essentially, then probably that would not be affected at all. On the other hand, if most people are searching for broader queries, more generic queries, almost like a sentence that would match something on your home page, then I could imagine that would be a little bit harder for you to appear in search results for, just because we’re not sure if your home page is actually in that language of that query […].

One thing you could also do, […] is to make your home page kind of this bilingual version […] but to create separate pages additionally for the individual language so that if someone is looking for long-form information about an international school like this, they can still find those pure English or mostly English pages and then, from there, transition to the rest of your website […].

Find out how to create separate pages for individual languages in our article on International SEO.

34:20 “ If there’s a difference between content in the mobile and desktop version, does it mean that Google will punish the website and affect the website’s ranking, or does it simply mean that Googlebot can find it in the mobile version, but it won’t be able to rank? ”

John said, “ So, for the most part, we shifted most of our indexing to mobile-first indexing, which means we would only look at the mobile version of a website in a case like that. So, essentially, if there is something that is slightly different on the desktop version of a website, we would, for the most part, not even use that for Search. So it’s not that we would punish a website because of a difference, but, rather, it’s like, we just look at one version of the website, and we don’t even know what is on the other version to kind of treat it differently.

And for the handful of sites that are still in desktop indexing, that applies the other way around. Of course, if there’s […] something on the mobile version that’s not on the desktop version, and you’re being indexed by the desktop crawler, then we wouldn’t really see that. We do crawl the alternate version from time to time, but we don’t crawl it to pick up more information, but, rather, just to confirm that there is this connection between the desktop URL and the mobile URL. ”

46:20 “ We have a really huge page with millions of URLs, and […] the sitemaps are being currently renovated. And our IT team is considering storing […] the new sitemap files in our cloud service. That means from example.com/sitemaps to cloud.com/sitemaps. And we are wondering, is that a problem if we store the sitemaps in the cloud? And if that’s not a problem, shall we also create a permanent redirect for the old URL for this example.com/sitemap, or how should we plan the move? ”

John said, “ It’s definitely possible to host the sitemap file somewhere else. There are two ways that you can do that. One is if you have both of those domains verified in Search Console, then that works. The other way is if you submit it with the robots.txt file, where you specify ‘sitemap:’ and then the URL of the sitemap. That can also go to a different domain. […] I would also redirect the old sitemap file to the new location just to be clean, but probably even if you just delete the old sitemap URL and make sure to submit the new one properly, then that should just work.

What might be a little bit tricky is I don’t know how Search Console would show that directly in the UI, in particular, if the sitemap file is in a different location, if Search Console would show the sitemap information in the indexing report, for example. But that’s a reporting problem. That’s not something that relies on the functionality of the sitemap file. It’s really just Search Console doesn’t show it properly. And, again, maybe it does. I’m just not 100% sure. ”

49:40 “[…] So [during the previous SEO Office Hours ] we posed that question about domain with a history as an escort service provider. […] the domain has a long history because the first snapshot of that website is from 1997. […] we relaunched our website in June last year […]. And the main issue that we are having is […] that we still are getting flagged [as adult content]. And additionally, we have this issue […] – crawled, currently not indexed. And we are trying to understand if the history of the domain can actually affect that we are having issues with indexing. […] we do believe that the content we are publishing is of good quality. It’s internally linked, and we try to build a quality site. Where we struggle at the moment is page performance, so it’s kind of in progress at the moment to optimize for that. But we use prerender.io so what we show for Google is already prerendered version. So when it comes to our Lighthouse score, it’s all good. […] What can we improve or look for to understand why we are not getting indexed? I’m happy to share the URL as well. “

John offered that he could take a look at the URL later, and then he answered, “ Usually, the indexing side of things would not be related to if there was adult content on the website before.

The indexing side might be affected if the content that was on there before was very spammy. So that might be something where, from an indexing point of view, it just takes a while to figure out, oh, this new website is actually not spammy at all.

But if it was just purely that there was adult content there before, then I could imagine that maybe our SafeSearch filters are a little bit slow in recognizing that. I do know we’ve taken some steps to make that faster […], or maybe there is something else on the SafeSearch that is kind of sticking.

The SafeSearch side is something that you can check if you do a site query and then turn SafeSearch on and off. You should be able to see is there something from SafeSearch happening or not. You don’t see that with regards to indexing, though. But I can take a look at this afterward, and we can see if there’s something super obvious that I can let you know about. ”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
