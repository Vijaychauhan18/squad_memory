---
source: https://yoast.com/setting-google-analytics-goals/
title: Perfecting your goals in Google Analytics
scraped: 2026-03-23
published_on: 2017-05-04
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

# Perfecting your goals in Google Analytics

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/setting-google-analytics-goals/
Published: 2017-05-04
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
How do you set up goals in Google Analytics? And what Google Analytics goals make most sense for your site? Read all about it!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

There are quite a few tracking features in Google Analytics for which you have to do a bit more than just implement the UA-code on your pages. One of those features is the ‘goal’. The goal is a feature in which you can track one of the following things:

We’ve noticed that people are often having trouble setting up these goals in Google Analytics. Not only are they stuck on how to set them up, but also on which goals to set up. Especially the latter really requires some thought. I’ll try and take you through that thought process in this post.

Goals give you an enormous amount of extra and valuable information. With goals you can track if people are doing on your website what you want or expect them to do. There are always multiple things that people could do that would benefit you, so tracking how many people are doing that is invaluable.

That’s not all though. When you set up goals, you have the option to set up multiple steps, if you turn the option ‘Funnel’ on:

A funnel is basically the process people go through to buy one of your products, or to sign up for your newsletter. You can set up as many steps as you want, but I think the only reason to add a step is when it’s required. If a step is not required, it’s not part of your funnel, because people can also come from other pages. For instance, people will need to have viewed your page on a specific product, before they can actually add it to the cart and buy it.

But the best thing is yet to come! When you’ve set up a goal with a funnel, you can actually see how that goal is doing in the ‘Funnel Visualization’. This is a very visual and easy to understand representation of what’s happening with your goal.

It shows how many people entered every step, how many people went through to the next step, and how many people dropped off on each step. This makes it very clear where in your funnel you can improve things. And it shows you the percentages and the overall funnel conversion rate. How’s that for useful?

If you have an online shop, you might have a lot of products. When this number keeps growing, it’ll be hard to keep track of the sales of each product. Setting up your goals with funnels as I’ve shown above, will give you insights into how your products are doing, as well as showing you how the related pages are doing.

You’ll be able to see if your product page is actually getting people to add that product to their cart. And when people have added the product to their cart, you’ll be able to see how many of them actually bought the product in the end. You can see all that in the Funnel Visualization.

You can create goals in the ‘Admin’ section of Google Analytics. The Admin tab is found at the bottom of your left sidebar when you’re logged in to Google Analytics. Make sure you have the right account and view selected. When you click admin, there will be three “columns”, of which the most right will look like this, this column is called ‘view’. Here you can click on that red call-to-action button that says ‘+NEW GOAL’ :

You have a default of 20 goals. To get more, you need to pay, unfortunately. Clicking +NEW GOAL will give you this screen:

The options you can choose from speak for themselves as they come with examples of the sort of goals. You can also set up a custom goal, which sounds scarier than it actually is. Just try it ;-)

Once you’ve chosen one of the options above, the second step awaits. And that second step looks like this:

Making a goal using ‘Destination’ allows you to make a goal for people ending up on a certain page. For instance, if you have a contact form, and your contact form has a confirmation page, you can track everyone who has been on your confirmation page.

‘Duration’ allows you to track everyone who’s spent more than the minimum amount of time you set on your website.

‘Pages/Screens per visit’ does the same thing as ‘Duration’, just with pageviews. When people hit a threshold of a minimum amount of pageviews you’ve set, that ‘ll count as a goal completion.

The ‘Event’ goal is the hardest. This requires actual coding, as events need to have been set up first. Luckily, there’s this awesome tool called Google Tag Manager that allows you to easily create events. No developer needed! Events are pretty powerful: you can track how many times a video on your website was played, for instance.

When you’re creating ‘Destination’ goals, you’ll have these options:

The ‘Equals to’ is simply that. The URL people visit has to exactly match the URL you put in there. So if you have any campaign variables, or a subpage, it won’t be counted towards the goal.

The ‘Begins with’ is exactly the opposite: everything beginning with the URL you fill out will be counted toward your created goal.

The hardest is the ‘Regular expression’ goal. At the same time, this is the most powerful and precise option of the three. Regular expression, or regex, is a sequence of patterns that, if you know how to use them, can be very specific in its targeting.

Let’s say you have an online store with over 20 products, so you can’t fit them all in your free Google Analytics account. What you could do is create a goal for every brand you’re selling, using regex goals. Your destination goal will simply be the confirmation page after your checkout. And, if the brand you were wanting to track was Yoast, you could add a regex line like this:

This expression will simply track everything with /yoast/ in the URL. You have to be aware that every step in a regular expression goal and funnel should be written in regex. Also, be sure that your regex doesn’t match any other goals, or it will simply be counted twice.

“I have too much data!”, said no one, ever. Of course, people will be saying it from time to time, but you get my point. If not, here it is: try to make as many useful goals as you can think of. And there’s one very important word in that sentence: useful. There are literally millions of goals you could think of, but most of them will probably be completely useless for your website and/or business.

And that’s where the actual thinking comes in. You have to think about what you want your visitors to do on your website. Let me give you an example of what would be good goals for an online shop, in general:

Of course, you can be far more specific by tracking, for instance, how many people have viewed your product video, or how many people left a review of your product. It all comes down to thinking about what your website is for, and what you want people to do on it.

Assigning a value to your goals is important to be able to distinguish between your goals. If you don’t assign a value to your goals, you simply can’t see which of the goals is your most profitable goal. There are three ways in which you can assign values for your goals: actual values, average values or relative values.

Let’s say you offer a few services, all of which have one fixed price. People can hire you for these services, and they have to pay up front . In this case you should simply assign that price as the value of each goal representing a service. That way, you can simply see how many times a goal was completed and therefore one of your services was successfully requested.

In this case, it’s important that people actually have to pay up front because otherwise you’ll run into some trouble. Because even though the prices of your services are always the same, if people don’t have to pay immediately to finish the goal (order a service), there’s always the possibility they just won’t pay.

When people don’t have to pay up front, or you offer services or products that can have different prices (such as our plugins), or the specific goal generates leads, you need to assign average values. You can calculate average values in three different ways.

If you’re making goals for things that don’t actually earn you money, you can assign relative values. Relative values are simply values that show which of the goals are worth more to you. So, if you prefer people signing up for your newsletter over liking your Facebook page, you could assign the newsletter signup goal a value of 2, and your Facebook like goal a value of 1. Or, if you think twice as much is too much, you can assign them values of 3 and 2 respectively.

Obviously, we’ve made up these numbers, but it still helps you differentiating between each goal.

This all depends on how big your website is, of course. However, if you own an online shop with a lot of products, the answer is simple: yes. Although it can be hard to find the time to set this all up decently and correctly, in the end it will be worth it!

So there’s really no excuse anymore to not set up your goals! In the end, you’ll be amazed you ever did without. And although you can make the ‘wrong’ goals, you won’t jeopardize your original data. It will only influence the data of your goals. Feel confident enough to try goals out!

Which cool goals did you set up? Let me know in the comments!

Annelieke is a former employee of Yoast and used to lead the research team at Yoast. She has her Master's degree in Sociology and focuses on all things related to data.

ok but 1 question – I cant seem to segment my data buy just a few goals – its either ALL my goals or just 1 of my goals. Any way round this? Otherwise my Macro goals get all muddled up with my micro goals. thoughts?

I already have checked that feature in Analytics but i haven’t it that useful, Isn’t that?

We care about the protection of your data. Read our privacy policy.
