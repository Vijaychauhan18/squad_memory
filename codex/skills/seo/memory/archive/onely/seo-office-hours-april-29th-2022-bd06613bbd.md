---
source: https://www.onely.com/blog/seo-office-hours-april-29th-2022/
title: SEO Office Hours, April 29th, 2022
scraped: 2026-03-23
published_on: 2022-05-11
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

# SEO Office Hours, April 29th, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-april-29th-2022/
Published: 2022-05-11
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Read the newest posts on our blog to make sure you're not missing out on anything!

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 29th, 2022.

8:23 “If a website requires users to verify their age before showing any content by clicking a button to continue, is it possible that Google would have problems crawling the site? If so, are there any guidelines around how to best handle this?”

John said, “Depending on the way that you configure this, yes, it is possible that there might be issues around crawling the site.

In particular, Googlebot does not click any buttons on a page. So it’s not that Google would be able to navigate through an interstitial like that if you have something that is […] a legal interstitial. And especially if it’s something that requires verifying an age, then people have to enter something and then click Next . And Googlebot wouldn’t know what to do with those form fields. So that means, if this interstitial is blocking the loading of any other content, then probably that would block indexing and crawling as well. A really simple way to test if this is the case is to try to search for some of the content that’s behind that interstitial. If you can find that content on Google, then that probably means that we were able to find that content.

From a technical point of view, what you need to watch out for is that Google is able to load the normal content of the page. And, if you want to show an interstitial on top of that, using JavaScript or HTML, that’s perfectly fine. But we need to be able to load the rest of the page as well. So that’s the most important part there. And that also means that if you’re using some redirect to a temporary URL and then redirecting that to your page, that won’t work. But, if you’re using JavaScript/CSS to display an interstitial on top of your existing content that’s already loaded, then that would work for Google Search. And, from a policy point of view, that’s fine. That’s not something that we would consider to be cloaking because the content is still being loaded there. And especially if people can get to that content after navigating through that interstitial, that’s perfectly fine.”

Is your website using JavaScript? Read our ultimate guide to JavaScript SEO .

10:54 “Our website was ranking well before we performed a design overhaul. Our timing was terrible, as a core update was released just after the launch, which had some issues with internal links. We suspect Google reassessed the site quality at this time, but we could resolve the issues. Our ranking and traffic dropped a lot, and [we] lost all rich snippets in the process, and [it] is in limbo for the last five-six months. Do we wait for another core update for Google to assess our site quality again, or does this happen when the website is recalled? […]”

John replied, “I think there are a few things here that come together. But, first of all, I would recommend checking out our blog post that we did about core updates . […] It has a lot of information about core updates, especially about the issues that we look into there and how things are resolved over time. So that’s the first thing I would do in a case like this.

The information that we use for core updates to understand the site is […] collected more over the long term. It’s not something where, if, right when the core update launched, you had a technical issue, then suddenly your site would fall into this problem. […] So that means, if you are seeing any effects from a core update, that’s usually due to a longer period of time, where we’ve run into issues that we’re looking at with regards to the core updates.

Also, with regards to technical issues, usually, that’s not a trigger for core updates […] to not know what to do with the website because technical issues tend not to be the same as quality issues. Obviously, there can be some technical issues that, when a user looks at the website, make it impossible to use the website. But if it’s just something small, then that’s usually not a big issue. So, if you have things like 404s on a page or some broken links, that wouldn’t be a reason for our quality algorithms to jump in. But there are lots of other things that our quality algorithms do look for, and they’re all in the blog post. So I would recommend taking a look at that.

With regards to the resolution after improving your website, that’s also mentioned in the blog post. Some of these things will improve steadily over time as we reprocess your website. And some of them do require that our quality algorithms take another run through the site, and that might take a while for that to happen.”

14:04 “If I would translate a page from one language to another, would it be penalized?”

John answered, “ No. […]. Essentially, if you’re translating your content, you’re creating new content, and it’s new words, new sentences. […] And we would be able to crawl and index that normally, like any other separate piece of content. It’s not the case that we would penalize a website for having localized content.

The only time with regards to translations where our systems might be a little bit upset is if you’re using automatic translations and letting those automatic translations be indexed , and especially if those automatic translations are lower quality translations, where we might look at those pages and say, well, this is not a great page anymore. And that might be something where our algorithms would jump in and say, well, this is not a great page. We should not treat it like a great page. So that’s the primary thing there.”

15:35 “Is using the Indexing API good or bad for a normal website?”

John’s answer was: “The Indexing API is meant for very specific content, and using it for other content doesn’t make sense. That’s similar, I think, to using construction vehicles as photos on your website. Sure, you can put it on a medical website, but it doesn’t make sense. And, if you have a website about building houses, then, sure, put construction vehicles on your website. It’s not that it’s illegal or that it will cause problems if you put construction vehicles on your medical website, but it doesn’t make sense. It’s not something that fits there. And that’s similar to the Indexing API. It’s just for very specific use cases. And, for everything else, that’s not what it’s there for.”

19:06 “When does Core Web Vitals give steady and correct information? It keeps fluctuating without changing any data on the website.”

John: “I think this is probably a side effect of how the Core Web Vitals and the Page Experience update are processed. And that’s something where I would try to look up those details to understand a little bit more about how the field data, so the data that users see plays a role into this. And that is something where, if users from a wide variety of backgrounds and different locations and different device types access your pages, you will probably see some fluctuations over time there as well.”

Are you struggling with fluctuating Core Web Vitals data? Take advantage of our Core Web Vitals optimization services .

19:59 “I see a very dramatic increase in redirect errors of our site in the Search Console Coverage Report. All redirects look technically fine. There are 301s. Nearly all URLs listed in the report are for old products that now redirect to a more general all product page. Has Google started to treat that kind of redirect as redirect errors?”

John said, “It sounds like there’s a very specific situation on your website with regards to redirects and data that you’re seeing in Search Console. And this is something I would probably post in the Help forum . […]

One of the things I suspect might be happening there is that we picked up those URLs in your sitemap file, and you’re redirecting them now to something else, and then our systems are like, well, you mentioned them in the sitemap file. Why don’t they actually work? And maybe that’s just why they’re flagged.”

You can read more about redirects in our Ultimate Guide to Redirects in Technical SEO .

23:09 “Why would an English version of a website home page rank higher and then another language version of the home page in a country of that language?”

According to John, “It’s always hard to say why would it rank higher, but it definitely can. And, when it comes to different language versions, if you’re searching for a word or a term that is essentially ambiguous with regards to its language, then it can happen that we pick one language version or another language version, or different country versions. This is the same thing. And this is probably primarily true on home pages, when people are searching for your company name, it’s not necessarily clear that they mean the English language version or maybe a French-language version or a German-language version of your home page just from the query itself. So that’s something where sometimes we would show maybe whatever we think best matches that query, and that might not be the right language or country version.

[…] There are two things that you can do. On the one hand, with the hreflang annotations, you can tell us about the different language and country versions, and then it’s easier for us to swap those out. The other thing, especially for different country versions, which is usually where the home page problem comes into play, you can use a JavaScript interstitial or a banner on a page to guide people to the right version of the page. So, if you can recognize that the user is in a country where you have a specific country version, and they’re on a different country version, then using a JavaScript banner is a good way to let them know that ‒ it looks like you’re from this country, and we have a country version for you here. Maybe you would like to go there. The important part with this is that, by having a JavaScript banner, it tends not to get indexed. And, by having it as something that the user can click on, it doesn’t redirect the user there automatically, which means it’s easier for our systems to process and index these pages.”

If you want to know more about implementing hreflang annotations, check out our article on International SEO.

26:49 “Does adding the location name in the meta description matter to Google in terms of ranking if the content quality is maintained?”

John replied, “ The meta description is primarily used as a snippet in the Search results page, and that’s not something that we would use for ranking. But, obviously, having a good snippet on a Search results page can make it more interesting for people to visit your page when they see your page ranking in the Search results.”

27:20 “How does schema affect a medical niche’s website? What kind of structure data should be used there?”

John said, “When it comes to structured data, I would primarily focus on the things that we have documented in our developer documentation and the specific features that are tied to that. So, instead of saying, what structured data should I use for this type of website, I would kind of turn it around and say, what visible attributes do I want to have found in the Search results? And then, from there, look at what are the requirements for those visual attributes, and can I implement the appropriate structure data to fulfill those requirements? So that’s the direction I would head there.

John: “No, definitely not. Like I mentioned, use the guide of what visual elements do I want to have visible for my page, and then find the right structured data for that. It’s definitely not the case that you need to put structured data on every page.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
