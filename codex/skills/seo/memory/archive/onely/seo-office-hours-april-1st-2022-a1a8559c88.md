---
source: https://www.onely.com/blog/seo-office-hours-april-1st-2022/
title: SEO Office Hours, April 1st, 2022
scraped: 2026-03-23
published_on: 2022-04-08
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

# SEO Office Hours, April 1st, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-april-1st-2022/
Published: 2022-04-08
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Find out about the most interesting questions and answers from Google's SEO Office Hours with John Mueller on April 1st, 2022!

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on April 1st, 2022.

14:53 “We have [had] a content publishing website since 2009 and we experienced a bad migration in 2020 where we encountered a huge drop in organic traffic. […] We had a lot of broken links so we used the 301 redirect to redirect these broken links to the original articles but […] in the robots.txt we disallowed these links so that the crawling budget won’t be […] [used] on crawling these 404 pages. […] If we fixed all these redirects […] [so they redirect] to the same article with the proper name, […] can we remove these links from the robots.txt and how much time does it take to actually be considered by Google?”

John said: “[…] If the page is blocked in the robots.txt , we wouldn’t be able to see the redirect. So if you set up a redirect you would need to remove that block in the robots.txt. […] There is no specific time because we don’t crawl all pages [at] the same speed. Some pages we may pick up within a few hours and other pages might take several months to be recrawled.

[…] If this is from a migration that is two years back now then […] I don’t think you would get much value out of just making those 404 links […] show content. […] I can’t imagine that that would be the reason why a website would be getting significantly less traffic , […] unless these pages are the most important pages of your website but then you would have noticed that. But if these are just generic pages on a bigger website then I can’t imagine that the overall traffic to a website would drop because they were no longer available.”

Read our guide on how to fix “Not found (404)” in Google Search Console.

17:27 “[…] Question about the optimal content length on the page – […] we have encountered many blog posts […] [saying] we need to have around 100 or 1000 words per page, so what’s the optimal content length?”

As John said, “I don’t think there is one – […] some pages are very short, some pages are very long. […] It […] depends on the amount of information that you want to give users.”

The person then continued asking about content, specifically that “There is this term propagating now: […] thin content. Is it […] [used] by Google […]?”

John clarified: “[…] Usually, that applies more to the overall website. So it’s not so much that one page doesn’t have enough content, it’s more that the website overall is very light on actual information. […] I wouldn’t use the word count as a way to recognize that. I think sometimes the word count is useful for you to look at a larger website overall and to try to find areas where maybe you could be doing better. But I wouldn’t use it as a metric to guide […] the specific things that you do on the website.”

19:00 “[…] We run a two-sided marketplace since 2013 that’s fairly well-established. We have about 70 000 pages and about 70% of those are generally in the index. And then there’s kind of this budget that crawls the new pages that get created and those we see movement on that so that old pages go out, new pages come on. At the same time, we’re also writing blog entries […], and to […] get those to the top of the queue, we always use […] Request indexing on those. So they’ll go quicker. We add them to the sitemap, as well, but we find that we write them and then we want them to get on […] Google as [quickly] as possible […]. As we’ve kind of been growing over the last year, and we have more content on our site, we’ve seen that that sometimes doesn’t work as well for the new blog entries. And they also sit in this [ Discovered – currently not indexed ] queue for a longer time. Is there anything we can do […] – like internal links – or […] is it content-based or do we just have to live with the fact that some of our blogs might not make it into the index?”

John explained that it’s not unusual to have unindexed content: “[…] I think overall it’s kind of normal that we don’t index everything on a website. […] It’s not tied to a specific kind of content. […] Using the [URL Inspection tool] to submit them to indexing is fine. It definitely doesn’t cause any problems. But I would also try to find ways to make [it] […] as clear as possible that you care about [those pages] so […] internal linking is a good way to do that. […] Make sure that from your home page you’re saying here are the five new blog posts and you link to them directly so that it’s easy for […] Googlebot when we crawl and index your home page to see there’s something new and it’s linked from the home page. So maybe it’s important […].”

John also provided another suggestion: “If you have a blog section on your site, you also have RSS feeds […]. I would also submit those to Google in Search Console. Just because RSS feeds tend to focus more on the newer content, and that kind of helps us to pick those up a little bit faster. We use them similar to sitemap files but sometimes RSS feeds are a bit easier for us to pick up.”

22:19 “[…] Ever since GPT-3 based AI writing tools started to get advertised, our community [on Reddit] is having a debate over whether or not to use them. […] Our stance is mostly against it but […] we are struggling to see what is Google’s official position. […] How does Google react to websites hosting AI written content […]?”

John replied: “[…] For us, these would essentially still fall into the category of automatically generated content. Which is something that we’ve had in the Webmaster Guidelines since almost the beginning, I think. And people have been automatically generating content in lots of different ways. And […], if you’re using machine learning tools to generate your content, it’s essentially the same as if you’re just […], shuffling words around, or looking up synonyms, or doing the translation tricks that people used to do. […] My suspicion is that maybe the quality of content is a little bit better than […] the really old school tools but […] we would consider that to be spam.”

As a follow-up, John was asked: “Are you saying that Google is able to understand the difference between human and AI content?”

In response, John said: “I can’t claim that. But […] if we see that something is automatically generated, then the web spam team can definitely take action on that. […] I don’t know how the future will evolve there but I imagine, like with any of these other technologies, there will be a little bit of a cat and mouse game, where sometimes people will do something and they get away with it. And then the web spam team catches up, and solves that issue on a broader scale.

But from our recommendation, we still see it as automatically generated content […]. Maybe this is something that will evolve. In that it will become more of a tool for people. […] Like you would use machine translation as a basis for creating a translated version of a website, but you still, essentially work through it manually. And maybe over time, these AI tools will evolve in that direction that you use them to be more efficient in your writing, or to make sure that you’re writing in a proper way, like the spelling and the grammar checking tools […].”

Thinking about using machine translation for your website? Find out the best way to get a translated version of your website in our International SEO guide.

39:50 “[…] I recently redesigned my website and changed the way I list my blog posts and other pages from pages one, two, three, four to a View more button. Can Google still crawl the ones that are not shown on the main blog page? What is the best practice? If not, let’s say those pages are not important when it comes to search and traffic, would the whole site […] be affected when it comes to how relevant it is for the topic for Google?”

John’s response was: “[…] It depends a bit on how you have that implemented. A View more button could be implemented as a button that does something with JavaScript, and those kind of buttons, we would not be able to crawl through and actually see more content there. On the other hand, you could also implement a View more button, essentially as a link to page two of those results, or from page two to page three. And if it’s implemented as a link, we would follow it as a link, even if it doesn’t have a label that says page two on it.

[…] The first thing to double-check – is it actually something that can be crawled or not? And […] if it can’t be crawled, then usually, what would happen here is, we would focus primarily on the blog post that would be linked directly from those pages.

[…] We probably would keep the old blog posts in our index because we’ve seen them and indexed them at some point. But we will probably focus on the ones that are currently there. One way you can help to mitigate this is if you cross-link your blog posts as well. Sometimes that is done with category pages or […] tag pages that people add. Sometimes blogs have a mechanism for linking to related blog posts […]. Even if we initially just see the first page of the results from your blog, we would still be able to crawl to the rest of your website.

[…] One way you can double-check this is to use a local crawler. There are various third-party crawling tools available. And if you crawl your website, and you see that it only picks up five blog posts, then probably, those are the five blog posts that are findable. On the other hand, if it goes through those five blog posts. And then finds a bunch more […] then you can be pretty sure that Googlebot will be able to crawl the rest of the site as well.”

46:51 “[…] Google said that there’s a maximum of 16 words that you can use in your alt text. […] Does Google read the rest of my alt text and […] what does this mean for usability?”

As John responded: “[…] We don’t have any guidelines with regards to how long your alt text can be. […] From a Google Search point of view, you can put a lot of things in the alt text for an image if that’s relevant for that particular image. When it comes to the alt text, we primarily use that to better understand the image. So if someone is searching […] in Google Images for something that matches the alt text, then we can use that to understand that your image is relevant for that alt text on that specific page […].

We do also use the alt text as a part of the page. But to me, that’s usually something that is already visible on the page, anyway. So it’s less something that is critical to the page itself. I would really use it as something that applies to the image, and […] for usability reasons and for Google Images to better understand that specific image.

[…] What might also be worth mentioning is, when it comes to Google Images, you don’t necessarily need to describe exactly what is in the image. But rather […] what this image means for your particular page. So if you have a picture of a beach, you could use an alt text and say, oh, this is a beach. But you could also say, this is the beach in front of our hotel, or this is the beach that we took a photo of when we were doing a chemical cleanup. […] Those intents are very different, and people would be searching in different ways in Google Images to find more information there, and giving that extra […] context also always makes sense in my opinion.”

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
