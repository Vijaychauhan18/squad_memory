---
source: https://moz.com/blog/ga4-things-you-dont-want-to-miss
title: Your GA4 Migration: 10 Things You DON’T Want to Miss
scraped: 2026-03-23
published_on: 2023-07-17
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

# Your GA4 Migration: 10 Things You DON’T Want to Miss

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/ga4-things-you-dont-want-to-miss
Published: 2023-07-17
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
GA4 may seem like a monster, but you’re here, so you’re already tackling it! In this article, let Brie take you through 10 things you don’t want to miss in your GA4 migration.

## Extracted Body
Universal Analytics is officially done collecting data. Cue one single tear running down every marketers’ cheek.

Now all of your site data will flow solely through Google Analytics 4.

Are you sure you’re ready for that? The only reason I ask is because, well, GA4 is a bit of a beast with tons of hidden settings that need to be addressed for optimal data collection.

In the admin section of GA4 you will see two columns: Account and Property. The Property column is where the majority of important setting options are hiding.

Your property timezone can be set under the Property Settings section of the Property column. (Yes, this is very meta.)

This one may seem like a no-brainer, but it’s an easy one to overlook.

When you created your GA4 property, you had the option to set your timezone. If you’re anything like me, you probably just hit the “next” button.

We already know that different platforms track differently so we aren’t tracking apples to oranges, but if we aren’t even using the same time zones for reporting, well we may as well be tracking apples to cucumbers.

The TL;DR: Using the same timezone everywhere allows you to compare data a bit more easily.

Turns out, there is more than one thing to touch in that Property Settings section in column two.

In the same place you set up your timezone, you have the option to change your currency.

By default Google sets the currency to USD for all reporting.

Note: If you’re doing business with multiple currencies, Google will do the conversions on the backend to continue to report in USD.

Enhanced measurement is perhaps one of the biggest changes with Google Analytics 4.

If you’re not sure what enhanced measurement is, it’s essentially pre-built event tracking. Which is actually great, except when it tracks things incorrectly.

You can view all of the automatically collected events in the Data Streams section once you click on your desired data stream.

Now don’t worry, most of these events and parameters will be tracked just fine, but there are a few instances that may require additional debugging.

This most pertinent issue for users revolves around form interactions, especially for those who have the Meta pixel on their site. False form interactions tend to be triggered by Facebook pixels because Facebook uses a “form submission” to pass data from your site to theirs.

I highly suggest using the GA4 debug tool or by looking at your real time analytics to double check that the “form_destination” is correct.

Another major pain point in enhanced measurement is that it relies on site searches passing one of the following parameters into the url: q, s, search, query, keyword. Should you use a different parameter, it can be defined in this enhanced measurement section by clicking the gear icon next to the events.

The Events section is a great place for a tracking gut check.

This is basically just a massive list of all of the events being tracked and how often they are being fired. If you don’t see your events here or the numbers seem low, you may need to go check your setup.

Also, new in GA4, you can create and modify your events directly in the platform.

If you were a destination goal type person in Universal Analytics, this is the section that allows you to create events based on page location.

Tons of other changes can be made using the modify event tool like reconciling event names, creating sub events from collected events, etc.

Much like the Events section, this Conversion section is the best place to do a quick gut check and make sure the most important things are being tracked on your site.

If you don’t see one of your conversions on this screen, you will need to head back to the Events sections and click the toggle to the right of the event name.

(Yeah, it really is that easy to create conversions in GA4. Thank goodness.)

If you do see your conversions, but the numbers look odd, you may want to click the three dots to the right of the conversion to see the counting method.

By default, Google counts conversions for each event completion. However, you may only want to count conversions once per session. If that is the case, click on those three dots and change the counting method to “Once per session.”

For all of my friends out there using different domains for their stores, their courses, their main site, and/or their blog - your time has come.

The good news is, cross-domain tracking in GA4 is much easier than it was in UA. The bad news is that this is only true if you know where to find the setup widget.

To define all of your domains, navigate to Data streams > select data stream > Configure tag settings > Configure your domains.

Taking this step is especially important in GA4 because outbound clicks are tracked using Enhanced Measurement. Thus, not defining all of your domains can lead to false “click” counts.

Ah, now this is a question I’ve been asked over a dozen times. Yes, you can filter out internal traffic.

To filter internal traffic by IP address, you will need to go to Data streams > select data stream > Configure tag settings > Show all > Define internal traffic.

Unfortunately, in the GA4 platform, this is currently the only way to define internal traffic.

If you’re using a third-party payment processor like Stripe or Paypal, this is a big one.

Unless you want all of your purchases to be attributed to your payment processors, you have to specify to Google that there are unwanted referrers.

If you’re not sure if you have sites you need to mark as unwanted referrals, check your Traffic Acquisition report and change the primary dimension to Session Source/Medium.

If you’re anything like me, and send 80% of your events using Google Tag Manager, you’re going to want to listen up!

Most of the time, people use GTM to send extra data with their events in the form of event or user parameters. GA4 does collect and process these parameters, but it DOES NOT retain this data unless you’ve defined the dimensions.

So if you want to be able to see your parameters, you need to create a custom dimension for each one. It’s pretty easy, you just name the dimension and select the coordinating parameter.

Lastly, and maybe most importantly, you are going to want to extend your data retention window.

This is perhaps one of the most important but most overlooked settings.

In the property column, you’ll navigate to Data settings > Data retention. Once you’re here you will find that by default GA4 properties are only set to retain event data for 2 months.

That’s just 60 days. That’s not even a whole season of Big Brother.

The good news is that you can change this from 2 months to 14 months with three clicks of a button.
