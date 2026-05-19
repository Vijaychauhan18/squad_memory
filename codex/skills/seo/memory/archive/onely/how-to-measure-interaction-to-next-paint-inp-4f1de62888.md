---
source: https://www.onely.com/blog/how-to-measure-inp/
title: How to Measure Interaction to Next Paint (INP)
scraped: 2026-03-23
published_on: 2024-04-16
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

# How to Measure Interaction to Next Paint (INP)

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/how-to-measure-inp/
Published: 2024-04-16
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Read the newest posts on our blog to make sure you're not missing out on anything!

## Extracted Body
For several years, INP was an experimental and later a pending metric.

Some found it familiar, others overlooked it, and a few actively addressed it in anticipation of changes in Core Web Vitals metrics.

Since March 12th, INP has become a stable Core Web Vital, which is now one of the ranking factors.

If you’re reading this article, you likely belong to one of the first two groups I mentioned earlier.

By the way, if you’re still unsure about what INP is and how it’s calculated, I recommend visiting our post that explains what Interaction to Next Paint is about.

Important to note: Data from the lab and field can be differentiated. That is because website visitors might use completely different internet connections or devices than you or your dev team.

Now, let’s move to the article’s core, and let me walk you through the tools and help you choose the best for you!

Measuring the speed of interaction, whether in the lab or the field, can be achieved through various methods. Some are easy to use and provide a general overview, while others demand technical knowledge that assists in identifying poor interactions.

Additionally, there are paid solutions that are straightforward to install and intuitive to use.

Below are tools for measuring INP in the lab and in the field. Please note that this is not an exhaustive list.

Chrome browser users can test or evaluate Interaction to Next Paint in a controlled environment using developer tools. By selecting ‘timespan’ and ‘performance’ in the Lighthouse tab, users can generate a report detailing the INP metrics.

The Web Vitals Chrome extension displays, among other things, the INP score after interacting with a page.

It’s important to note that this tool only records the interaction once. If you wish to measure a different one, you must reload the page, as I haven’t found a better workaround for this yet.

The widely-used Google Search Console (GSC), accessible to every website owner, can help identify if your website has slow interaction issues.

Simply go to the GSC dashboard , click on the Core Web Vitals tab, and select either the mobile or desktop panel, depending on what you want to check.

Note: Core Web Vitals metrics are calculated separately for different devices.

When you’re there, find and click on the row in the table where the INP score is labeled as ‘ needs improvement ‘ or ‘poor’ . This will show you which URLs are having issues with slow INP.

However, keep in mind GSC has its limitations. It doesn’t report all INP times for each URL in a group, nor does it specify which element caused the poor score. Despite this, it’s a useful starting point for identifying potential INP issues on your site.

Rick Viscomi released the CrUX Dashboard Launcher some time ago. This tool greatly simplifies the process of verifying CrUX.

You can create a dashboard in just one step, which includes Core Web Vitals and other metrics for a specific domain. Among these metrics, the report provides insights into the domain’s INP scores for different devices over a prior 10-month period.

Just use the link from the first paragraph , paste the domain into the box, and push enter.

This might be because the domain isn’t publicly discoverable, or it doesn’t attract enough visitors.

If your website is included in the dataset, you should see a dashboard similar to the one described below.

The CrUX dashboard is an excellent tool for sharing website performance scores with colleagues or clients and for comparing your domain against competitors. Much like the GSC, it offers a solid foundation for assessing whether a website needs improvements.

Googlers have released a JS library designed to collect data about the INP and send it to a Real User Monitoring (RUM) provider. I strongly suggest exploring it — you can do it right here .

You need to have coding skills or access to a developer who can assist in its implementation.

If you want to use GA4 for that, implement the code below on your website (source: web.dev) and find slow interactions in the field .

Implementing this code on the website will also require creating custom metrics in GA4 once the parameters are delivered to the property.

A few years ago, Simo Ahava created a guide and a template for GTM that collects CWV metrics from visitors’ experiences and sends them to Google Analytics. This is a great way to implement CWV measuring on your page without having developer knowledge.

There are plenty of paid tools that can measure the INP metric based on real user experience.

A complete list of RUM providers would be long, so just to give you an idea, here are a few examples of RUM providers that can measure INP:

However, there is one big disadvantage for some of you—these tools are not free. However, some tools let you test them out for free. For instance, Debugbear won’t ask for your credit card details just to try it out.

Curious about what you get with these paid services, I gave DebugBear a whirl on my site to see what setting it up and navigating the interface was like.

After starting a new project, I had to add a small bit of code to the website.

After I got that bit of code in place, I could check out the INP scores right from the INP tab with all the necessary details needed to find out which interactions are slow.

From my point of view, while having paid tools for measurement can be a nice bonus, it’s definitely not essential . Sticking with free options works pretty well too, since you’re essentially getting the same kind of data.

You might be wondering, “Which method should I use to measure the INP?”

Ideally, both methods should be used, but this might not always be possible. However, if you can measure the INP using both field and lab methods, that would be ideal!

First, field data lets you identify if and where your visitors are experiencing slow interactions. Second, lab data helps you measure whether your efforts to improve interaction are effective.

Below is a table outlining the key pros and cons of each method for gathering INP data.

Measurement of the INP metrics is not the easiest one. As FID before and now INP, interaction is required to capture the value. However, identifying slow interactions becomes much easier once you properly set up the measurement.

My suggestion is to implement one of the solutions I’ve described above right away. This could change even if your website isn’t currently facing issues with poor interactions. The worst-case scenario would be encountering this problem and being left without any data, leaving you to guess which interactions lower your website’s rating.

The sooner you start gathering data from visitors, the quicker you’ll be able to address and improve any poor interactions.

Don’t let INP hurdles hold back your website’s success. If you need help, partner with us for top-tier Technical SEO Services , overcome INP challenges and propel your site to new heights of performance.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
