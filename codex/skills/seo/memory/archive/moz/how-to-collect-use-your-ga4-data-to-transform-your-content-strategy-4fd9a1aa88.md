---
source: https://moz.com/blog/transform-your-content-strategy-with-ga4-data
title: How to Collect & Use Your GA4 Data to Transform Your Content Strategy
scraped: 2026-03-23
published_on: 2023-10-02
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How to Collect & Use Your GA4 Data to Transform Your Content Strategy

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/transform-your-content-strategy-with-ga4-data
Published: 2023-10-02
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Learn how to harness the power of GA4 data to elevate your content strategy. Discover actionable insights to enhance existing content, improve engagement, and uncover new content opportunities.

## Extracted Body
Content without data is like a property without a foundation — it lacks stability. Without data, you can’t truly understand the impact of your content and what to do next.

Victor Ijidola put it best in his recent article on informational content , “You want your content to persuade your readers to do something,” but if traffic is low or sales are slow, chances are your content isn’t working hard enough at generating interest.

In the last few years, content marketing has become more data-driven than ever before. Content marketers and SEOs have tools like Moz Pro and Google Analytics to thank for that. These tools can help you identify which articles are working, how many conversions your content is generating, where your content gaps are, and much more.

Google Analytics 4 (GA4) replaced Universal Analytics, Google’s long-standing analytics reporting tool, in July 2023. Hopefully, you’ve already migrated to GA4 and taken ownership of your GA4 property, had a good look around, begun unpacking all of your data, and made yourself familiar with the reporting platform’s layout. As you settle in, you can begin to learn just how much GA4 can help you renovate your content marketing strategy.

Whether you’re creating content for a SaaS knowledge hub, planning articles for a service-based company’s blog, or publishing product guides for an e-commerce platform, the tactics I am about to share will help you evaluate your content marketing efforts so far (or within the last two months or 14 months, depending on your data retention period ), figure out which pieces of existing content to improve, and identify gaps and opportunities in your content.

You have admin access to your website’s Google Tag Manager (GTM) container or have a developer who can help you with tags.

If you don’t have admin access to your GA4 property, get this set up first! If you’re unable to gain access, you can send some of these recommendations to those who do, so they can share the reports we create with you.

As a content marketer, there’s always a desire to create new content. After all, we’re often told that Google favors “fresh” content — wisdom that is widely debated . That’s why I recommend working on your content strategy by improving existing content first.

This doesn’t just draw new attention to older articles. Beginning by improving your existing content also makes it much easier to develop new content ideas.

The first step in improving your existing content is to figure out which articles you should work on and prioritize. Enter GA4.

I’ll explore each of the following metrics in more detail, including where to find them in GA4. But first, here’s a quick rundown of the most helpful metrics when it comes to understanding how well your content is performing and choosing which pages to focus on for optimization:

Let’s start with one of the most important and easy-to-find metrics — page/screen views. Views will provide a helpful indication of your content’s performance, i.e., how many times your article has been viewed in a specific period of time.

In GA4, you can find this by going to Reports > Engagements > Pages and screens. Once there, you’ll see a list of pages and the number of views they had during your selected time period. By default, this is set to the last 28 days, but you can update this to a duration that suits you.

Filter this data so you can concentrate on your blog or content hub only. In most cases, you can do this by:

Choosing to filter by the “Page path and screen class” dimension

Selecting “contains” as your Match Type, then enter the subfolder that contains your relevant content — usually “/blog/” or “/news/”

Order the results by views, and you’ll see which articles have had the most — and the least — views during your selected time period. You might want to focus on a selection of the least visited articles first as these could have the biggest potential, so add those pages to your list.

Simple enough — but things can get complicated when choosing which period of time you want to evaluate. Older pieces of content will typically benefit from having a higher number of views just because they’ve existed longer. That is why other metrics can be more helpful in understanding what’s working well and what isn’t.

However, if posts about similar topics feature prominently in your least viewed articles, you may want to remove this type of content from your blog or hub altogether. It’s OK to delete content that attracts little attention or combine some of these pieces into a longer guide that provides more value for your readers. Just remember to implement redirects from your old URLs to the new ones for your guide.

Google defines engagement rate as “the percentage of engaged sessions on your website or mobile app,” where an “engaged session” is a “session that lasts longer than 10 seconds, has a conversion event, or has at least 2 pageviews or screenviews.”

Put simply, engagement rate measures the percentage of visits that involve a significant interaction with your website.

The engagement rate isn’t included by default in GA4, so you’ll need to add this to your report. The pages and screens report we just used to see views is a good place to add this metric.

At the top right, just below the date range, click the pencil icon to customize your report view

Average engagement time should be added by default. This metric provides the average “amount of time someone spends with your webpage in focus or app screen in the foreground.”

Analyze engagement rate and average engagement time against your pages to identify those with lower-than-average results. In the Base Creative blog , our average engagement rate is 51%, so I’d pay close attention to articles that are much lower than that and those that have a short average engagement time (which should already be in your report).

The aim is to use this data to improve engagement. Some quick wins based on engagement metrics could include:

Increasing font size so it’s easier to consume content (particularly on smaller devices)

Breaking up longer paragraphs into smaller chunks to improve readability

Adding links to related content and/or downloads or (more) links to your calls to action

Incorporating a range of media formats, such as audio, video, images, or interactive assets like quizzes or infographics

You can go one step further and compare how your content performs against these metrics across different devices. Compare desktop and mobile performance against each other in GA4 by using the “Add comparison” feature on any report screen you’re looking at:

In Values, choose either Mobile or Desktop and click “Apply”

Click “Add comparison” again and add the other device, e.g. “Desktop” in Values

In Base Creative’s case, there isn’t a large difference between engagement rates across devices. Around 90% of visits to our blog take place on desktop, so I’d pay closer attention to these statistics when reviewing performance, but you might find some interesting results that could make you rethink the design and layout of your blogs if there are some drastic differences between devices.

An exit counts as a session that ends on a particular page or screen. It’s similar, but not the same as a bounce , which is a single-page session where no engagement occurred.

Both are useful metrics for identifying weaker pieces of content, but I find the exit rate more helpful when it comes to articles. A high number of exits suggests that your content isn’t encouraging any further action on your site. Ideally, we want our articles to lead our readers to visit another article or — even better — your money pages (usually a service, product, or contact page).

Currently, Google doesn’t offer an exit metric in the Reports section of GA4, so you’ll need to create an exploration in the Explore section. You can add the bounce rate here, too, to see how it compares. Here’s how:

Go to Explore and click on “Blank exploration” to create a new exploration

Click the “+” icon next to DIMENSION, choose “Page path and screen class” under “Page/screen”, click “Import,” then drag to ROWS

Click the “+” icon next to METRICS, choose “Exits” and “Views” under “Page/screen,” then “Bounce rate” under “Sessions”, click “Import,” then drag to VALUES

Filter to just show your articles by dragging “Page path and screen class” to FILTERS. Update Match Type to “contains,” then enter your blog’s subfolder (e.g.,/blog/) below and click “Apply”

Don’t forget to change your date range on the left to a helpful time period and reorder by the number of exits, which you can do by clicking on the “Exits” column.

If you see high exit pages here, for example, if your number of exits on an article equals at least 50% of its views — then these are your priority to review. The aim here is to keep visitors on your site for longer (by visiting another page) or to encourage them to take action, so take this opportunity to add helpful, relevant links to related content or other appropriate pages.

This is also a good place to add links to your least viewed articles (that we identified previously) if you believe they still provide valuable information for your visitors, as they may be difficult to find on their own.

If you’ve enabled enhanced measurement in your GA4 property (which you can do by going to Admin > Data Streams > Web stream details, then clicking the toggle on Enhanced Measurement), then you’ll begin recording a “scroll” event. This will count every time a visitor has scrolled through 90% of your page.

To see scrolls, go to Reports > Engagements > Pages and screens, then under “Event count,” you can choose to just see “scroll.” Compare this number against the number of views to get a sense of how many users are making it to the end of your article without any additional setup.

GA4’s offering provides a limited interpretation of scroll depth but combined with Google Tag Manager, you can learn more about your visitors’ scrolling behavior.

Remember how I mentioned that content and data work so well together? Well, the same applies to GA4 and Google Tag Manager (GTM) when it comes to reporting on the impact of that content.
