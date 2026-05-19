---
source: https://www.onely.com/blog/seo-office-hours-october-29th-2021/
title: SEO Office Hours – October 29th, 2021
scraped: 2026-03-23
published_on: 2021-11-04
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

# SEO Office Hours – October 29th, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-october-29th-2021/
Published: 2021-11-04
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on October 29th, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on October 29th, 2021.

4:39 “Can noindex pages affect Google’s evaluation of “website quality” at the site level that is used in Core Updates?

John said, “[…] First of all, the amount of low-quality pages that you’re saying yourself are low-quality pages – it feels tricky and problematic to me. Just independently of anything with regards to Google Core Updates, if you find that you have so many pages on your website that are really low-quality in the sense that they are not good pages, they don’t have any useful content on them, then it feels like an opportunity for something to clean up there.

Because even if we don’t index those pages, users might go to those pages, and if that’s what they build the perception of your site on, and you know these are bad pages, that feels like a recipe for people just not coming back—kind of outside of anything specific to SEO that feels like something that would be worth cleaning up.

Sometimes people see things as being lower quality just because of technical reasons. For example, if you have category pages and you can filter them and sort them in different ways, you might say, well, this is lower quality because it’s not actual content from my point of view. That’s more technically not interesting content. It doesn’t mean that it’s actually a bad page.

[…] With regards to the core updates and Google’s understanding of the quality of a website overall: we don’t take these pages into account , so we really focus on the content that we have indexed for a website. That’s the basis that we have with regards to all our quality algorithms and understanding of the website itself. On the one hand, because that’s what we’re showing in search. So, if there’s something on your website that we’re not showing in search and we’re not using it to promise anything to users who are searching, then from our point of view, that’s up to you what you do with that.

The other point I think is a little bit more practical in the sense that if we don’t have these pages indexed and we don’t have any data for these pages, then we can’t aggregate any of that data for our systems across your website.”

7:43 “On our About us page, we have different paragraphs for every author. Would it be okay to make anchor links for each author on this page (e.g., domain.com/our-news-team/#author-1 and domain.com/our-news-team/#author-2) and use these anchor links for the author.url property, or does it have to be a dedicated page for every author?”

“I don’t think we have any guidelines specifically around that. This is something where it’s less a matter of their technical requirements for how you link your authors, and more a matter of it has to work well for users. […] If this is a page that works well, where it makes sense that authors can, or people can find information about the authors on your website, then that seems fine.

The one thing I might caution here a little bit is that sometimes for individual authors, it makes sense for us to understand a little bit better how that author fits in overall. For that often, these authors link their different profiles together, or they pick one author profile that they use across the whole web. For that scenario, I think it does make sense to have individual URLs for each other.

But if this is purely within your website and purely for informational reasons for users, then probably that would be perfectly fine like that.”

9:18 “Is the country code top domain a ranking factor especially for the local business?”

“On a very rough basis, I would say yes. We do use the country code top-level domain as a factor in geotargeting. In particular, if someone is looking for something local, and we know that the website is focused on that local market, then we will try to promote that website in the search results.

We use the top-level domain if it’s a country top-level domain. If it’s not a country top-level domain, then we’ll check the Search Console settings to see if there are any countries specified for international targeting.

If you have a generic top-level domain, then setting that in the Search Console if you want to focus on a specific country definitely makes sense.”

If you’re having issues with country codes, check out our article on International SEO , which covers country code mistakes.

15:37 “How does it affect the SERP rankings when page and SERP titles do not match? Often we experience that the page title has been shortened and our company name added at the end in the SERP title. We do add our company name at the end sometimes, but the concern is that this to all our page titles will limit how much we can write in the title. Is it better to have shorter page titles that will be displayed in the SERP, or is it better to keep the page titles we already have and then let Google choose a different SERP title?”

“I don’t think there is anything explicit about what is better from our side. One of the things I think is worthwhile to keep in mind is we do use titles as a tiny factor in our rankings as well. So it’s something where I wouldn’t necessarily make titles on your pages that are totally irrelevant, but you can try different things out. […] It’s not a critical issue if the title that we show in the search results […] doesn’t match what is on your page. From our point of view, that’s perfectly fine, and we use what you have on your page when it comes to search. […]

With regards to the company name, […] we do see that users like to have an understanding of the bigger picture of where does this page fit and sometimes the company name or a brand name for the website makes sense to show there. Some people choose to put it in the beginning or in the end. […] From my point of view, that’s more a matter of personal taste and decoration rather than anything related to how ranking would work.”

18:01 “Does using the Disavow tool raise a flag in the algorithm and trigger a soft penalty on the website for possibly engaging in link building in the past? We used this tool to remove hundreds of spammy links, and our site traffic collapsed a few days later. Should we remove the Disavow file, and how long will it take for our site to return to normal traffic and ranking? Or is there a permanent “black mark” against this website for using the Disavow tool?”

“There is not any kind of penalty […] associated with using the Disavow tool. From our point of view, this is purely a technical tool that you can use if you have any links that are pointing at your website that you don’t want to be taken into account by Google’s systems. It doesn’t mean that you created those links. It can be something that you found where you’re really worried that Google might get the wrong picture for your website. It’s essentially up to you. […] In most cases, if you’re just seeing random links coming to your website, you don’t need to use a Disavow tool. But if you see something where you’re saying, wow, I definitely didn’t do this. And if someone from Google manually were to look at my website, they might assume that I did this, then it might make sense to use the Disavow tool.

Don’t let a Google penalty ruin your online presence. Take advantage of our Google penalty recovery services to get your website back on track and regain your rankings.

From that point of view, it doesn’t mean that you did it. It’s not a kind of a sign that you’re admitting that you were doing link games in the past. […] If the manual action is resolved and if the issue is cleaned up, then we’re treating your site as we would treat any other website. It’s not that we have a memory in our systems that would say, well, this website had a manual action in the past therefore, it might be shady in the future as well. If you’ve cleaned up an issue, then you’ve cleaned up that issue. […]

With regards to this particular case where you’re saying you submitted a Disavow file and then the ranking dropped or the visibility dropped, especially a few days later – I would assume that that is not related.”

Need help with disavowing some unwanted backlinks? Take advantage of link risk management to reevaluate your backlink strategy.

26:18 “Does writing comprehensive articles covering a specific subject build trust with Google?”

“I don’t think we have any measure or metric […] where we’d say you have built trust with Google, and you’ve built that based on writing comprehensive articles. I would see this kind of work as being focused a little bit more on the user side. Does this build trust with your users? Do users appreciate this kind of content? […] The important part here is really to figure out which users you want to target and to make sure that your content actually speaks in their language.

For example, if you have technical content and you write a really detailed technical article about that, if your users are looking for something that is more general or more simplified that explains the basic topics a little bit better, then maybe that highly specialized technical article is not the best thing for them. […] So that’s something where you almost need to think about which users do I want to target. What kind of content are they looking for? How can I write it in a way that matches what they search for? And what would they like to find? Then based on that, you can build out your website.”

28:35 “We keep coming across sites that scrape our content and republish it on their websites, sometimes including a link to the original article, and sometimes not. My question is:

John said, “Some sites don’t care about things like copyright, and they just take content from other people and republish that. So the way we handle it is kind of nuanced and includes lots of different things. The first thing I would consider as a site owner if you’re seeing this with your content is to think about whether or not this is a critical issue for your website at the moment. […] If there is a critical issue, then I would recommend trying to see if there are legal things that you can do to kind of help resolve this even outside of anything SEO-related. […] I can’t give you advice on legal topics […], but in many cases, the DMCA process would be appropriate here. […] So I would, on the one hand, read up on that process. On the other hand, get local legal advice as well. […]

On Google’s side […], sometimes copies are also relevant […] especially when it’s not a pure one-to-one copy of something, but rather you’re taking in a section of a page and writing about this content. We see that sometimes, for example, when we publish blog posts that other sites will take our blog posts and include either the whole blog post or large sections of it, but they’ll also add lots of commentary […]. On the one hand, they’re taking our content and copying it. But on the other hand, they’re creating something newer and bigger based on that content. So in the search results, if someone were to search for that content, I would expect to see these kinds of other pages ranking as well because they’re providing a slightly different value than just what our pages are providing. […] Sometimes, these pages rank above ours, and that’s all fine.

With regards to indexing the scraped content first or not […], what I’ve seen in our systems over the years is that we tend to look at the bigger picture for a lot of things when it comes to websites. If we see that a website is regularly copying content from other sources, then it’s a lot easier for us to say, well, this website isn’t providing a lot of unique value on its own, and we can treat it appropriately based on that. That’s something where usually the ranking side settles down there a little bit.”

John added, “[…] sometimes it’s okay for copies to also appear in the search results, but essentially it depends on quite a bit the individual use cases there. […] If you’re seeing that this is really causing problems, then submitting spam reports to us is also a good way to let us know about these kinds of issues.”

34:55 “ Does a business presence in social media channels influence SEO? For example, more followers, likes, shares, social media links = better PageRank?”

“No. For the most part, we don’t take into account social media activity when it comes to rankings. The one exception I think that could kind of play a role here is that we don’t special-case social media sites, but we do sometimes see them as normal web pages. […] For example, if you have a social media profile somewhere and it links to individual pages from your website, then we can see that profile as a normal web page. And if those links are normal HTML links that we can follow […], we can process those HTML pages just like any other HTML page. But we wouldn’t go in there and say this profile has so many likes therefore, we will rank the pages that are associated with this profile higher. […] We can rank those pages individually, but it’s not based on the social media metrics.”

37:07 “ Is the Penguin penalty still relevant at all or are less relevant/spammy/toxic backlinks more or less ignored by the ranking algorithm these days?”

“I’d say it’s a mix of both. For the most part, when we can recognize that something is problematic and any spammy link – we will try to ignore it. If our systems recognize that they can’t isolate and ignore these links across a website, or if we see a very strong pattern there, then it can happen that our algorithms say, well, we really have kind of lost trust with this website. And at the moment, based on the bigger picture on the web, we need to be more on a conservative side when it comes to understanding this website’s content and ranking it in the search results. Then you can see a drop in the visibility there. But for the most part, the web is pretty messy, and we recognize that we have to ignore a lot of the links out there. So for the most part, […] you would only see this kind of a drop if it’s really a strong and clear pattern that’s associated with the website.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
