---
source: https://moz.com/blog/google-business-profile-ranking-drop-diagnosis-fix
title: How to Diagnose and Fix Google Maps Ranking Drops
scraped: 2026-03-22
published_on: 2025-12-18
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

# How to Diagnose and Fix Google Maps Ranking Drops

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/google-business-profile-ranking-drop-diagnosis-fix
Published: 2025-12-18
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Lost rankings or calls from your Google Business Profile? Learn a step-by-step process to confirm a drop, find the real cause, and recover your local rankings fast.

## Extracted Body
Managing a Google Business Profile (GBP) that is suddenly not driving the leads or traffic it once did can be stressful. A loss of ranking in Google Maps can feel mysterious, but visibility drops usually have identifiable triggers. With the right sequence of analysis and fixes, you can recover.

This guide will walk you through a systematic diagnostic framework that you can use to confirm if it’s a real ranking drop versus normal fluctuation. If it’s a real ranking drop that needs to be corrected, this guide will help you:

You can obviously identify a ranking drop by comparing ranking grids over time, but the first true sign of a ranking drop that’s causing a real-world issue is a decrease in calls coming from the business profile. You’ll need to review your call data to see if calls coming from the business profile are down month-over-month AND year-over-year (important for seasonality). If you do not have dedicated call tracking for your business listing (which you ABSOLUTELY should), you can use the call data in the Google Business Profile Insights tab as a directional dataset. Insights only show calls made from mobile devices and are based on just tapping on the button, versus a placed call, so you are not seeing “true” call data if you rely on Insights only.

However, if you must rely on Insights, also check if search impressions and clicks are down, and direction requests (if those matter to your business). To see year-over-year data, you need to exclude the current month from the date range.

Keep an eye on your GBP metrics in the same platform you use for location data & review management.

Google Analytics will have better click data than GBP insights, so make sure to review your GA4 data. However, to segment only GBP traffic out in GA4, you’ll need to already be using UTM codes on your GBP links. If you notice clicks to the website are down from GBP, this is another sign that rankings may have dropped.

Pro tip: Filter for GBP users only with a filter that contains your specific UTMs (for example: “first user campaign” contains “gbpwebsite”, or however you have the UTM parameter for campaign set up).

Then, using Google Search Console , identify what specific keywords show the biggest drop in clicks from your GBP URL. Ignore impressions because these are heavily skewed by rank trackers . You’ll want to do so by navigating over to the “Search results report, under the Performance Section. Next, add a ‘page’ filter, where the logic is ‘URLs containing’ = ‘utm’.

Jot down or export the keywords you have seen the biggest drop in clicks for, specific to the GBP.

Use a geo grid rank tracking tool, such as GeoRank in Moz Local , to check your map pack visibility and shifts to your key revenue-driving keywords. This is where ongoing local rank tracking becomes super important!

Pro tip: Set up your local rank tracking reports to scan regularly. This can be either monthly or weekly, depending on the need. Ensure the reports are set to run on the same days, and at the same time of day. (eg, weekly, on Tuesdays, at noon).

Check which keywords have lost visibility, and whether the loss affects all keywords or only some. For example, let’s say you are an HVAC company in Tampa, that provides multiple services. You should check to see if:

Take note of the timing of the drop. Was it sudden? Were you ranking last week, but not this week? Or was it a gradual decline over months?

Mark the date the drop was first started. Overlay internal changes, such as listing edits or website updates, and external events, such as algorithm updates or changes to the Google results layout. This will help isolate the cause later. You can add annotations to Google Search Console or GA4.

You are still visible in Google Maps, but just in noticeably lower ranking positions. You may have dropped out of the top three map pack, which can account for serious traffic loss. Dropping out of the map pack can indicate a number of causes, such as competitor shifts, category problems, or weakened ranking signals , such as fewer reviews.

Check if competitors have also lost rankings or if the issue is isolated to your profile. If several businesses drop at the same time, it may be a local algorithm update. If only your listing is affected, then it points to a problem specific to your own profile.

For example, the first ranking grid here shows a Moz Local GeoRank by Competitor report, where a business and two other listings are competing for the top three spots. Fast-forward a month, and the second ranking grid shows the business has dropped from position 3 to 9, while the other 2 listings stayed in the map pack (top 3). So the business we are tracking lost rankings, while all the competitors stayed more or less the same. This indicates a likely isolated ranking signal issue on the listing that saw the decline, rather than an algo update.

Your listing disappears entirely from Maps for your top keywords, or appears only some of the time, creating a pattern of inconsistent visibility. This often indicates that Google’s local filter is impacting your listing, possibly due to duplicate listings or a competitor that is too close to your listing.

Check for conflicting listings at the same or a nearby address, within 200 ft of your business listing pin. If you see a “Swiss cheese” pattern on a ranking report, where you are ranking for some pins but completely missing from the rankings for other pins, check whether a nearby competitor has the opposite pattern on their report (i.e. they are ranking for the pins you are not).

If your profile shows it’s suspended, not visible to the public, or changes cannot be published, you may experience ranking drops.

If your profile is suspended, it falls into one of two categories:

Both types of suspensions require a reinstatement process, which is most likely video re-verification. Only a hard suspension would cause your rankings to drop, as with soft suspension, your profile is still on maps and should not lose any rankings.

If your ranking position has not changed, but calls, clicks, and direction requests have dropped, the cause may be tracking issues, website problems, changes in the Google results layout, or changes in user intent. First, investigate your measurement setup to make sure it’s not a simple tracking issue.

Then, compare before-and-after screenshots of the search results for your top keywords. Recently, in mobile search results, I’ve seen a trend where the local pack is being replaced by an AI Overview , and that AI Overview is showing local businesses. Seer Interactive did a study that shows the presence of an AIO in the search result significantly reduces CTR for everything showing in the SERP (including Ads!).

Oddly enough, sometimes Google can change its definition of a city’s boundaries on Google Maps. So, if your map pin now suddenly falls outside the city you aim to rank in, your rankings for location-specific keywords won't be as strong as businesses that are still “inside” the city borders (e.g. “Albany pest control”).

Compare the city Google assigns in the knowledge panel with the one you expect your business to be in. In the example below, the business has an address “in” Albany, but according to the borders set on Google Maps, it falls outside Albany, and Google notes it as being in Albany County. This will directly impact its ability to rank for searches that contain “Albany”.

Pro tip: To fix this, see whether you are able to move the map pin inside the borders, although this is not always possible because it can affect driving directions to your business.

If you see that your competitor rankings are down alongside your own, and that your ranking decline is not isolated to your specific profile, then it’s a good idea to check for recent local ranking volatility and a possible Google algorithm update.

First, review Google’s Search Status Dashboard and see if there is a confirmed core algorithm update. These core updates don’t always impact local (Maps) significantly, but sometimes they do.

You can also check a Local Rank Fluctuation report, like this one from BrightLocal .

I also use tools like GSC Guardian , which overlays Google’s changes directly onto the data graphs. This can be extremely helpful when spotting instances where an algorithm shift could have impacted rankings and thus traffic from local.

Pro tip: Filter for Google Maps traffic only with UTM parameters on all GBP links. Also, filter out branded searches.

Review before-and-after screenshots of the search results. This is such an underrated data layer you should be tracking for your business, just like rankings. At our agency, we take SERP screenshots every time we pull a ranking report, which makes seeing SERP layout changes so much easier.

Pro tip: Track rankings and take a screenshot of mobile search results — because Google often tests new features on mobile first.

What should you look for when comparing before and after SERP screenshots? Check whether the local pack has disappeared, shrunk, or been pushed below even more Ads, like traditional Google Ads and/or Local Service Ads (LSA).

Check whether AI Overviews are showing local businesses instead of a traditional local pack. I have seen this recently for a client where it looked like they dropped right out of the map pack for their top keywords. Turns out, there is an AIO with local businesses that replaced the local pack across their entire city, and my rank tracking tool was only looking for local packs. So in reality, they were in the AIO, and thus visible on the SERP, but not the same as they once were.

Also, this was ONLY showing on mobile, so if we were just looking at desktop results, we wouldn’t have seen the AIO.

Identify if new competitors, either legit or spam, are now ranking above your business. Check to see if they have stronger signals, such as reviews, categories, website relevance, or better location proximity.

Check whether your categories, business name, or URL has changed. Review whether your website landing page has changed or lost relevance.

Pro tip: Moz Local’s Listings AI feature makes suggestions for profile updates based on competitor changes, engagements, rankings, and more.

If you are hit during a Google core algorithm update, time and patience are the only real answers. Like with the March 2024 update ( Helpful Content Update ), the “fix” usually won’t come until the next core update, according to Google themselves.

If your site is affected during a spam update, which is an algorithm update that aims to demote content/websites that violate Google’s spam policies, then again, the only fix is time and to stop building links or engaging in spam activity that Google deems unacceptable.

A drop in calls or website clicks may be caused by broken tracking. This can happen if UTM parameters or call tracking were changed. Confirm that all tools are still capturing the correct data.

There are tons of ways you can optimize your Google listing if you find that rankings have slipped due to under-optimizations compared to the competition.

Depending on what is causing the listing to be suppressed or filtered, you have some options. Luckily, this is one of the easier issues to fix!

Duplicate listings: Make a map edit or contact Google Support to remove any duplicate listings for your business found at this address.

Local filter: Identify any competitor listing that is too close to your pin and see if you can move your pin far enough away (over 200ft) from your business found at this address, but still be at the same “location”.

Suspended listing: Appeal your suspension using Google’s appeal management tool .
