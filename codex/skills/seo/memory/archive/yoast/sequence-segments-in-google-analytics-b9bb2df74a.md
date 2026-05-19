---
source: https://yoast.com/sequence-segments-google-analytics/
title: Sequence segments in Google Analytics
scraped: 2026-03-23
published_on: 2018-10-08
tags: live_feed, phase1_ingest, yoast, publication, seo-education, wordpress-seo, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Yoast SEO Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Sequence segments in Google Analytics

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/sequence-segments-google-analytics/
Published: 2018-10-08
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Segments in Google Analytics can give you more insight into the behavior of your audience. But what can you do with sequence segments? Annelieke explains!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

I love segments! And for those of you wondering why I love them, or for those of you wondering what the heck segments are: I’ve written a post about segments in Google Analytics , that I invite you to read. In short: using segments makes your Google Analytics life a whole lot more interesting because it specifies your data, which allows you to get more insight into the behavior of your audience. And that’s what you want, an insight that you can turn into action.

A sequenced segment is somewhat more advanced than just a regular segment because you can add steps to this segment. Using sequences in segments adds a lot of opportunities especially for those of you who run an online shop and/or have implemented goals and events in Google Analytics. If you have a certain funnel in mind, then you can test this funnel through a segment that’s sequenced-based. Let’s say you have a contact form on your website, you suspect people entering your website through page X which is step 1. You suspect that after reading this page, they want to contact you so they visit the contact page, that’s step 2. Then you’ve implemented an event in Google Analytics that measure the form completion, that’s step 3. These 3 steps can be added in a segment. And when you compare that segment with the same segment but then with people that didn’t complete a form, you can check where the differences are and how you can optimize so that more people complete a form.

To create a cool sequenced segment, you need to go to the segment area in Google Analytics. You can find it almost always at the top of a report:

Click on ‘Add Segment’ and that will take you to the following screen: Clicking on the red button will take you to the place where you can create the actual segment: In the left sidebar you can see an item called ‘Sequences’ this is the place to go. If you click on that, you see where you can add steps. And you can choose if you want to include or exclude the sessions/users. If you don’t want to create a session based segment, you can also choose a user based segment. And you can choose how you want your segment to start. Do you want it to start with ‘any user interaction’ or ‘first user interaction’?

To fully understand how this works you need to understand a bit more about users and sessions . A user can have more sessions. And sessions can consist of more pages. If you choose first user interaction, then the first step of the segment you’re building has to start with that step, so it’s the first step of the session. If you choose any user interaction, then this means that the step can also be in the middle of a session.

Now you’re probably wondering, what can I do with this? And the answer is: a lot! For example, if you’re running a campaign because you’ve launched a new product, a keyword research training for instance. You can create a segment saying: The first interaction must be through this campaign, so the session starts with someone coming from this campaign, and buying more than 1 product (transactions > 0). If you create the same segment but then without sessions containing a transaction, you can compare sessions that converted with sessions that didn’t convert. Then you can try to find out what a successful user flow looks like and what an unsuccessful flow looks like. Especially for conversion questions, sequence segments are very useful. You can also add all the steps of your checkout process for instance in a segment. You can even create a segment that shows you insight about shopping cart abandonment . And what to think about what comes before the cart. What’s a more successful flow? People adding a product to the cart from the overview page or from the specific product page?

Another example: let’s say you offer a free ebook on your site. You’re probably hoping that this ebook will lead to sales or people hiring you for your expertise. But how do these people behave on your site after they received that ebook? Do the calls-to-action in your ebook work? You can create a user-based sequence segment where step 1 is the form completion and step 2 is a page where people land on after clicking on a call-to-action.

With a sequence segment, you can also discover what the conversion rate is of people who add a product to the cart (step 3) by clicking on the product page (step 2) from a banner on the homepage (step 1). And compare that conversion rate with people whose first step was the product page. And how about people coming from social media (step 1), do they return via a Google search (step 2)? These are just a couple of examples of how you can use sequence segments, but the possibilities are endless.

Adding steps in segments is an awesome feature in Google Analytics. It can bring you more insight about users or sessions that convert or don’t convert. It can specify data, for instance how many users come from mobile and then return from a desktop. That’s information you can’t get from the aggregated data you’re seeing in standard Google Analytics reports. You can go all out with segments, use your creativity when building segments. There’s a lot you can do! And as always, think about the question you want answered and base your segment on the question you have.

Annelieke is a former employee of Yoast and used to lead the research team at Yoast. She has her Master's degree in Sociology and focuses on all things related to data.

You explanations of this stuff are the best on the web. Simple, clear, tested by a real person! Thanks so much

We care about the protection of your data. Read our privacy policy.
