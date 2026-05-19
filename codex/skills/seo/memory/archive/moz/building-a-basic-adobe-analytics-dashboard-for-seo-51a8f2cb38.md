---
source: https://moz.com/blog/basic-adobe-analytics-seo-dashboard
title: Building a Basic Adobe Analytics Dashboard for SEO
scraped: 2026-03-23
published_on: 2021-08-26
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

# Building a Basic Adobe Analytics Dashboard for SEO

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/basic-adobe-analytics-seo-dashboard
Published: 2021-08-26
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Caitlin and Kristi cover the basics of Adobe Analytics for SEO, and guide you through creating a simple dashboard. To learn more, check out the full guide on Moz’s SEO Learning Center!

## Extracted Body
The largest players in website analytics are Adobe Analytics and Google Analytics (GA), and for many SEOs, GA is typically their first foray into the world of analytics.

While there are plenty of guides to self-learn GA, there is noticeably less documentation for Adobe Analytics. In this new guide, we’ll cover the basics of Adobe Analytics for SEO, guide you through creating a simple dashboard, and help you ensure your Adobe Analytics implementation is set up correctly for your business needs. Then, we’ll show you how to add a few new and exciting elements to your SEO dashboard.

On a basic level, Adobe Analytics functions just like Google Analytics. They both allow you to monitor website traffic across channels, track conversions, and understand customer behavior.

However, Adobe Analytics has many advanced features that allow you to get down and dirty with the data. As for SEO, with even a basic setup, it can provide you with a wealth of information about your website and its visitors.

For an excerpt, read on for a brief how-to on building a basic SEO dashboard.

In this section, we guide you through creating your first SEO dashboard. By the end, you’ll have built a dashboard that includes all the SEO basics in one place.

Now, open up a blank Adobe Analytics Workspace and let's get started!

The first panel we’ll be creating is an Organic Traffic Overview. This panel is simple and meant to give a quick gauge of SEO performance. Here are the steps to recreate this panel:

1. First things first, create a new workspace panel and add a Natural Search segment. To do so, within the components panel, search for Marketing Channel . Once found, click the small > to refine the dimension. Find Natural Search and drag and drop into the top of the panel.

2. To create the field that summarizes the total Organic Visits, within the visualization panel, select Summary Number, and drag and drop into the panel. Two things will pop up: Summary Number and Summary Number Data. In the Summary Number Data chart, drag and drop Visits into the Drop a Metric Here (or any other component) placeholder. If you only want to report on December, for example, within the component panel search, search for Last Month or any time frame you desire. Drag and drop this into the chart too. It should look like this:

Your summary number should now be showing. To hide the chart and only show the line graph, click the colored dot next to the title of your Summary Number. Then toggle off Show Data Source . Lastly, rename and resize the summary number as you see fit.

3. To create the month-over-month (MoM) change visualization, within the visualization panel, select Summary Change , and drag and drop into the panel. Two things will pop up: Summary Change and Summary Change Data. In the Summary Change Data chart, drag and drop Visits into the Drop a Metric Here (or any other component) placeholder. Then filter visits with the time periods you want to compare. For example, add a filter for Last Month vs. 2 Months Ago for a MoM comparison. Then, drag and drop All Visits into the chart as well. It will look like this:

Now, your summary change should be showing. To hide the chart and only show the line graph, click the colored dot next to the title of your Summary Number. Then toggle off Show Data Source . Lastly, rename and resize the summary change to your liking.

4. Finally, to create the line graph, first update the time panel to Last Year (or whatever time period you plan to report on). Then, from the visualization panel, select Line and drag and drop into the panel. Two things will pop up: Line and Line Data. In the Line Data chart, drag and drop Visits into the Drop a Metric Here (or any other component) placeholder. Your line graph should now populate. To hide the chart and only show the line graph, click the colored dot next to the title of your line graph. Then toggle off Show Data Source . Lastly, rename and resize the line graph as you see fit.

The second panel we’ll be creating is a Top Entry Pages Report. This panel is also relatively simple and is meant to quickly show which website’s pages are performing best in the SERPs. Here are the steps to recreate this panel:

1. First, add a new panel to your dashboard and add a Natural Search segment. To do so, within the components panel search Marketing Channel . Once found, click the small > to refine the dimension. Find Natural Search and drag and drop into the panel.

2. To create the table, within the visualization panel, select Freeform Table, and drag and drop into the panel. An empty table will show up. In the Freeform Table , drag and drop Entry Page into the body of the table. In the Drop a Metric Here (or any other component) placeholder, drag and drop Visits , Bounce Rate , and Average Time on Site side-by-side. Lastly, rename and resize the table as you see fit.

The third panel we’ll be creating is a Marketing Channels Report. This panel will break down your website’s marketing channels with two different visualizations: a donut chart and a freeform table.

1. To begin, add a new panel to your dashboard. No segment is needed for this report.

2. To create the table, within the visualization panel, select Freeform Table, and drag and drop into the panel. An empty table will show up. In the Freeform Table , drag and drop Marketing Channel into the body of the table. In the Drop a Metric Here (or any other component) placeholder, drag and drop Visits. Lastly, rename and resize the table as you see fit.

3. To create the donut chart, within the Freeform Table you just created, highlight the Marketing Channels like so:

Then, right click, go to Visualize , and select Donut . A Donut Chart should appear and be populated with your information. Lastly, rename and resize the donut chart as you wish.

The fourth panel we will be creating is a Referral Report. This panel is meant to provide a glimpse into what external websites are driving traffic to your website. Here are the steps to recreate this panel:

1. To start, add a new panel to your dashboard. No segment is needed for this report.

2. To create the table, within the visualization panel, select Freeform Table, and drag and drop into the panel. An empty table will show up. In the Freeform Table , drag and drop Referring Domain into the body of the table. In the Drop a Metric Here (or any other component) placeholder, drag and drop Visits and Unique Visitors . Lastly, rename and resize the table as you see fit.

In this final panel, we’ll be creating a Conversion Report to highlight the top conversions for the website. In this example, we will simply be using Summary Numbers. However, feel free to include a line graph, bar graph, or any other visualization that fits your needs. If you’ve been following along so far, you’ve got all the skills you need to create these visualizations, too.

1. To start, add a new panel to your dashboard and add a Natural Search segment. To do so, within the components panel search Marketing Channel . Once found, click the small > to refine the dimension. Find Natural Search and drag and drop into the panel.

2. To create the various Summary Number visualizations, in the visualization panel, select Summary Number, and drag and drop into the panel. Two things will pop up: Summary Number and Summary Number Data. In the Summary Number Data chart, drag and drop your Goal Metric into the Drop a Metric Here (or any other component) placeholder. Your summary number should now be showing. At this time, don’t forget to update the time period range to fit your needs. To hide the chart and only show the summary number, click the colored dot next to the title of your Summary Number. Then toggle off Show Data Source . Lastly, rename and resize the summary number as you see fit.

3. Repeat step two for all the conversions you want to display, renaming and resizing each Summary Name to your liking.

That’s that! You have created a simple SEO dashboard in Adobe Analytics, and are hopefully feeling more confident about the basics.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

Caitlin Boroden is the Sr. Director of Digital Strategy at Adept, an award-winning marketing agency headquartered in Columbus, Ohio. For almost a decade, she's helped small businesses and Fortune 100 brands track, analyze, and activate data to improve performance. Her other interests include photography and puppies, and she has a slight addiction to Reddit.

Overwhelmed by AI tools for automation? Discover 13 powerful tools to streamline workflows, boost productivity, and automate repetitive tasks effortlessly.

Description: Still using traffic and clicks to prove content success? Learn how to measure content ROI in revenue terms and make data-backed decisions that impress stakeholders.

Want to go beyond pageviews in GA4? Learn how to use custom event tracking to understand user journeys in SaaS and turn insights into growth.
