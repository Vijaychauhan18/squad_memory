---
source: https://moz.com/blog/measure-content-impact-with-intent
title: How to Measure the Impact of Content Based on Intent
scraped: 2026-03-23
published_on: 2022-03-02
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

# How to Measure the Impact of Content Based on Intent

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/measure-content-impact-with-intent
Published: 2022-03-02
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
When it comes to measuring the impact of content, you might think of KPIs like “sitewide conversion rate”, or picture an upward graph that shows an increase in traffic. But are those metrics really meaningful? In this piece, Kelly argues that, no, they’re not. Instead, focus on getting actionable…

## Extracted Body
When it comes to measuring the impact of content, you might think of KPIs like “sitewide conversion rate”, or picture an upward graph that shows an increase in traffic.

But are those metrics really meaningful? In this piece, I’ll argue that, no, they’re not. Instead, let’s focus on getting you actionable insights that can help your content flourish, by measuring its impact in a meaningful way.

Unless your website is a one-pager, the likelihood is that not all of your pages have the same intent. So why do we still measure conversion rates across an entire site?

The quick and honest answer here is that we do this because it’s easy and because that’s the way it’s always been done. But in reality, measuring your conversion rate across an entire site doesn’t give you any actionable insight - even when used in conjunction with volume of traffic.

Using a sitewide conversion rate neglects to consider pages where the intent isn’t to buy something. Think about your blog pages, customer services or FAQ pages. A growth in traffic to these sections won’t directly lead to an increase in sales. But what it will do is drop your sitewide conversion rate. That’s not a bad thing, it just means that using sitewide conversion rates on their own isn’t the best way of measuring performance here.

The answer instead, is to make sure you can report on the intent of your pages to be able to understand what’s performing well and what’s not in their own right.

How can you do this? Well… we separate the pages in our reports based on their intent.

Separating out pages based on their intent for reporting might sound like a pain, but there are ways you can automate this.

The biggest trick you can use is the URL structure. If you have a neat hierarchy, then this can work wonders to help you to group your pages in a way that makes sense to you.

Once they’re set up, you’ll be ready to report on your performance in a flash next time!

Here’s how you can do this in Google Analytics, Data Studio and in Excel/Google Sheets.

Creating custom segments in Universal Google Analytics allows you to pull out your data in a way that makes sense to you. It also allows you to quickly pull these segments into other reports, saving you countless hours.

What about GA4? “Segments” aren’t available in standard reports in GA4. An alternative called “Comparisons” are, but they can’t be saved once you exit the report. The key mechanics of how Comparisons work is similar to Segments, but can only be used as a quick review rather than an in-depth report. For in-depth reports that use Segments in GA4, you’ll need to visit “Explore” from the left hand tab and set up a new report.

If you haven’t used segments yet in Universal Analytics, you’ll find these by clicking on the blue circle of “All Users”. You’ll also see a button for “Choose segment from list” when looking at virtually any report in Google Analytics.

In Universal Analytics, you’ll see a list of segments that have already been created for you. But for now, these aren’t the ones we want to use. We want to create our own almighty segments.

So go ahead and click the big red button of “+ New Segment”.

Now you’ll need to give your segment a name that will help you find it again later.

Here you can segment your data in pretty much any way you can think of. But for the purposes of today, we’re looking to create a segment to work out your conversion rate based on the intent of the page they landed on. For that, we need to head over to the “Advanced” section under “Conditions”.

You can first choose whether you want to filter based on sessions or users. As we want to find sessions that started on a particular section of your site, you’ll want to keep this filter to “Sessions” and “Include”.

Next, you need to think about what section of the site you want to look at. One of the easiest ones you can start with is blog traffic, especially if you have /blog/, /news/ or similar as the defining hierarchy in your URLs.

If you have both sections, then you can lump these together by using the “OR” function of the filter. This will then show you all of the data based on landing pages that contained either the /blog/ or /news/ in the hierarchy.

One tip: be careful which match condition you use. If you choose “exact match”, then this data might not include ALL of your data, as it won’t include any page landings where parameters were appended. Equally, if you have a hierarchy where the URL you’re looking to match is also used in other pages, then you might have to add exclusions to your filter.

When setting up your segment, always double check your data against your expected raw data in Google Analytics to check for accuracy. Small differences in the way you’ve set up your segments can impact the reliability of your data as you could either under- or over-estimate the volume of traffic, conversions or goals by assuming that your segment is giving you an accurate view. So, manually checking the raw data output against your logic can help to find any holes (or you could even create counter-segments using the reverse logic to check that you’ve covered 100% of your raw data).

When you save your segment, you’ll be able to review your subset of data in seconds, and pull them into other external reports.

Here’s an example of what you’ll typically find when you’re looking at a conversion rate for all users, alongside your segments for commercial pages and blog pages.Your ‘true’ conversion rate for the pages that are designed to convert is much higher than your sitewide conversion rate. You’ll also see that your blog traffic (that might not be designed to convert) has a lower conversion rate - which has impacted your sitewide conversion rate, skewing your outlook on how they’re actually performing.

To use segments in GA4, you’ll need to visit the “Explore” section. Here, you’ll be able to create your own custom reports and delve deeper into your segmented data. If you’re new to GA4, it’s worth reading Google’s guide to Explorations .

In Explore, segments can be found when setting up your report — you can even add a separate comparative segment to benchmark your data against.

To add a new segment, click on the “Segments” section shown below on the left.

You’ll then be given options to “Include” and “Exclude” your dimensions based on metric values.

As the naming conventions of dimensions in GA4 are different to Universal, you’ll need to include sessions where the “Page location” (URL to me and you) contains “/blog/”. You can add “Or” statements here too if needed.

Once you’ve set up your report, with Explore, you can customize the metrics to view in your reports and choose how to visualize it, unlike Universal Analytics. The world is your oyster to create custom content-based reports here!

I love using Google Data Studio. I think it’s an underused tool for content management. Sure, it’s used a lot for top-level reporting, but I’m talking about the real juicy, actionable reports.

When it comes to making deep-diving reports, using Data Studio saves time and allows you to bring together data from different sources like Google Sheets, Search Console, and Google Analytics.

When setting up your data sources from Google Analytics, you’ll be given the option of adding a Google Analytics segment (you’ll have to scroll down to the bottom of your data tab). Here you can import any segment you’ve already made. I’ve imported one of my brand’s Google Analytics segments:Staysure blog.

As well as being able to import segments, you can also create your own filters when you click on “Add a filter”. Doing this prompts this box:

Here you can give your filter a name. This isn’t saved back to Google Analytics, and will only ever be found in the Google Data Studio report that you’re working on, so if you want to work on something particularly complex that you want to reuse, it’s worth adding your conditions as a segment in GA.

Above, I’ve replicated the segment in GA to show you what it would look like if I only wanted to create that filter in Data Studio.

Another benefit of using Data Studio for reporting rather than Google Analytics is that you can layer your filters and blend data together to build in-depth reports that you can jump into without having to dig through data time and time again.

So, if I wanted to find out what percentage of organic landings my page contributed to, that answer’s pretty hard to find in GA without writing down numbers somewhere else, or scrolling through a full dataset.

Instead, in Data Studio, you can use the organic segment from GA and add on a custom filter to look at just the page you want to review. To get your magic number, blend the data to pull through:

Left hand side: All organic traffic: Dimension: Page, Metric: entrances (+ add a filter for organic)

Right hand side: Your new ‘page only’ segment: Dimension: Landing page (to act as the key match), Metric: entrances .

To make life easier, rename the fields by clicking on the “ABC” or “AUT” box next to the field name so that it’s something different…

Once you’ve blended your data, you’ll need to create a new field. To do this, click on the Metric title that’s used for your new blended data chart - this then expands to show you data from table 1, table 2 and a new option at the bottom with a plus mark and “Create Field”. Click this to see this pop up:

Here you can create your own formulas based off of your datasets. So this is where we do SUM(my chosen page entrances)/ SUM(all organic landings). It’s important to add the “SUM” when adding calculations to blended datasets to amalgamate the data.

Finish by naming your field and boom. You now know - for any date range you’ve chosen, what proportion of organic traffic that page accounts for.

If you want to get really fancy, you can even add a comparison date range to see how this percentage changes over time.

If you want to go old-school, you can even filter pages in Google Sheets, or Excel.
