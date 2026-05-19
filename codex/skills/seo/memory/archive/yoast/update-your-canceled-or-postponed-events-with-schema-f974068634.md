---
source: https://yoast.com/update-your-events-with-schema/
title: Update your canceled or postponed events with Schema
scraped: 2026-03-23
published_on: 2020-03-27
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

# Update your canceled or postponed events with Schema

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/update-your-events-with-schema/
Published: 2020-03-27
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Have an event that got cancelled or postponed? Moved it online? You can now let searchers and search engines know by using structured data.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

The outbreak of COVID-19 led to a wave of canceled or postponed events. Some events made the switch from an offline event to an online one. As everyone is scrambling to look up the latest information on events online, it is important to have all the latest details on your website. Search engines can pick up these details and post the correct information in the search results. New Event Schema helps speed up this process. Let’s find out how to update your canceled events with Schema.org structured data data.

In last week’s release of Schema.org 7.0 , you can find several updates to the Events structured data. You can give your event an eventStatus of EventCancelled when it’s cancelled or an EventPostponed when it’s been postponed. In addition, you can also set a rescheduled event as EventRescheduled .

A new option is available for events that moved online: you can now update the eventStatus to EventMovedOnline . Here, you can also mark events as online-only by setting the location to VirtualLocation and set the eventAttendenceMode to OnlineEventAttendanceMode .

We had a new edition of YoastCon planned for April, 2020. As everything else, we rescheduled that to a date later in the year. I thought I’d let you see how one of these additions could look in code.

Below, you can find a part of the Schema code found on the YoastCon page. I’ve added the eventStatus , plus the corresponding EventRescheduled property. Also, I’ve added the old, plus the new date. Now, search engines know this event was rescheduled to a new date and can update the listing accordingly.

Many canceled events are now being rescheduled as online-only, for the time being or completely. You can now let search engines know that the event has turned into an online event — or a mixed event with both an offline and an online component.

In the YoastCon example, I could move the event by adding an EventMovedOnline property, combined with a new VirtualLocation property with a link to the page where the event is happening online. Code is truncated.

Of course, you can combine both online and offline locations of the event. Simply add the MixedEventAttendanceMode to the eventAttendanceMode and set both a virtual as well as a real location for the event. In your JSON-LD structured data, might look something like this:

Google has a special page in on its developer website describing how to get your event in the search results correctly.

The new SpecialAnnouncement type lets governments announce important happenings, like the closing of businesses and public recreation areas. While the initial offering is focused entirely on the spread special announcements during the Coronavirus pandemic, this will be extended at a further date. Both Bing and Google accept SpecialAnnouncement and will highlight these pages in the results how they see fit. You can find more information on SpecialAnnouncement on Schema.org/SpecialAnnouncement .

As you see, it makes a lot of sense to add this to your event pages. Unfortunately, at the moment Yoast SEO doesn’t have to option to add code for canceled or rescheduled events automatically. We’re working on that, though! Our structured data content blocks already let you build great FAQ pages and how-to articles , but we’re also working on blocks for events and recipes, among other things. In a while, you can add events and mark these as online, offline or mixed, while the correct structured data will be applied automatically.

In the current COVID-19/Coronavirus pandemic, it is crucial to give people accurate information about your event or business. A lot things have changed, many people sit indoor and have to go online to find out which businesses they can still visit or which events take place when. So, please take a moment to bring all your listings up-to-date.

Please check your listings on Google My Business, Bing Places, Yelp, TripAdvisor et cetera. Also update your social media channels like Facebook and Twitter. In addition, it might be a good idea to put a COVID-19 related FAQ page on your website answering the most pressing questions on how your business or event is handling this crisis. The Yoast SEO FAQ content block helps you make such a page in an instant. It also automatically adds valid structured data that makes sure the FAQ shows up in Google. Use it to your advantage.

Also, make sure to read Google’s documentation on how to pause your business online in search during this crisis.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

Thanks for the article! I try it on my personal website. Unfortunately i must cancel an event in case of covid-19.

Hi. We’re sorry to hear that. Hopefully, everything will be back to normal as soon as possible.

We care about the protection of your data. Read our privacy policy.
