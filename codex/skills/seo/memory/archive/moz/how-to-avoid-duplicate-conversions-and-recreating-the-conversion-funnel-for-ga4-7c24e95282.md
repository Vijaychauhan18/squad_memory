---
source: https://moz.com/blog/avoid-duplicate-conversions-ga4
title: How to Avoid Duplicate Conversions and Recreating the Conversion Funnel for GA4
scraped: 2026-03-23
published_on: 2023-03-20
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

# How to Avoid Duplicate Conversions and Recreating the Conversion Funnel for GA4

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/avoid-duplicate-conversions-ga4
Published: 2023-03-20
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
In this post, Robin takes you through how to avoid double counting in GA4, how to automatically ignore suspicious conversions, and how to recreate (and improve) the kind of funnels used in Universal Analytics.

## Extracted Body
As you’re probably all too aware at this point, GA4 is coming. Old versions of Google Analytics will be switched off for pretty much everyone come June 2023.

While GA4 is improving all the time, there are quite a few things that people are used to seeing in old versions of Analytics which, at the very least, take a bit of creativity in the new world.

One example is how conversions are handled. In the old versions of Google Analytics, a conversion could only fire once per session. In GA4 conversions are just another kind of event, so it’s possible for a conversion to fire multiple times in one session.

Problem is, you might be very interested if someone signs up via your contact-us form once. But that person might reload the thank-you page, or sign up for something else via a different form on the site. That doesn’t mean you necessarily want to track two conversions.

Speaking of signing up via different forms, on some websites, users may wind up on the same thank-you page having taken very different routes to get there. If we don’t have that much control, and we’re having to rely on thank-you page views to track conversions, it can be hard for us to separate out different kinds of conversions.

In old versions of GA you could use funnels with a “required” step. You might have one goal with a funnel requiring your event page, another goal with a funnel requiring a different page, and rely on them to give you different conversions. There also isn’t an obvious way to do this in GA4.

Automatically ignore suspicious conversions (like people landing direct on the conversion page).

Recreate the kind of funnels we expected in Universal Analytics (in fact we’ll make them better).

I’ll take you through a few bits in GA4 and others using Google Tag Manager. The GA4 approach is more straightforward, but the Tag Manager is more robust and can help you make sure that all of your conversion pixels are showing roughly the same information (because we’re long past the point where GA is the only place we’re recording conversions).

This section is about changes we can make purely through the GA4 interface. As long as you’re sending your page views conversion events to GA4 you should be able to use these tactics without any code changes.

However: There are some limitations of doing things through GA4, for example it can mean that your GA data doesn’t line up with conversions recorded via other platforms.

Julius Fedorovicius (of Analytics Mania fame) has produced a fantastic guide to making sure that conversions are only recorded once per session .

You create a custom audience based on a sequence that begins with “session_start”

No surprise that Julius has come up with a really smart way to handle the problem of double-counting:

If you’ve created Segments in Universal Analytics Audience sequences in GA4 look very like the sequences we used to create for Segments. However, the old Segments were just a way of visualizing data, whereas Audiences in GA4 are a way of grouping data. We can use Audiences to create something new .

That distinction is important because we can do cool things like fire custom events when someone enters an audience (which Julius makes use of in this solution).

This isn’t really a limitation as far as GA goes but it’s a consideration nonetheless. Julius’ solution is great for making sure we’re not double-counting conversions in GA, but GA probably isn’t the only way we’re recording conversions.

The average site probably has a bunch of separate conversion tracking pixels and those could end up double-counting conversions.

For example: Facebook and Google both describe how they avoid double-counting conversions, but their solutions largely rely on exactly matching transaction IDs, and even if they’re handling it okay, there’s a bunch of smaller fish out there that are also offering conversion tracking and can need a bit more hand-holding.

If we want to make sure that we’re only recording one conversion per session, it’s useful to make sure all of our conversion tracking is working in a similar way. Tag Manager is a great solution for that (I describe a solution in the Tag Manager section below).

You can also run into problems if, for example, your confirmation page is somehow indexed or bookmarked by users — people landing directly on it can lead to weird unexpected conversions. We can also use Tag Manager to guard against that a little bit.

Sticking with the GA4 interface for now, we can also adapt the AnalyticsMania approach to create our funnel-based conversions too by adding additional steps to the sequence.

For what it’s worth, conversion funnels are not the ideal way to categorize conversions . If you can use anything more direct (like the id of the form they’ve filled out, a separate thank-you page) then that’s a much more reliable way to categorize conversions. That said, we don’t live in a perfect world, and sometimes there isn’t the option to completely rebuild your conversion process.

In Fedorovicius’ example we just have two steps in our audience sequence:

Which basically means “someone lands on the site and then at any point during their session, they convert”.

To recreate the goal funnels you might be using in Universal Analytics - we can just add another step to the sequence. For instance:

That should mean we can create one conversion which is: Users who went through our event page and then converted.

And another conversion which is: Users who went through our sponsorship page and then converted .

There are some limitations here though, for example, what if someone:

They would fulfill the criteria for our event conversion and the criteria for our sponsorship conversion. We’d record a conversion for each and we’d end up double-counting after all.

This is also a limitation of the old Universal Analytics funnels: Just because a step in the funnel was required doesn’t mean the user can’t wander off around the site between that step and their final conversion. So, if it’s any consolation, this isn’t any worse than old Universal Analytics funnels (but we can still do better).

You might say “well that’s easily solved — at the moment the sequence says is indirectly followed by and we can just change that to is directly followed by ”.

Surely that would mean that someone is on the sponsorship page and goes directly from the sponsorship page to the thank you page, right?

Unfortunately that’s usually not what “directly followed by” means because there’s all kinds of things that can get recorded in analytics which aren’t page views.

For example if someone lands on the sponsorship page, and then scrolls down and lands on the thank you page, the thank you page view doesn’t directly follow the sponsorship page view. It goes:

GA4 has a really cool feature in the sequence builder where we can set a timer in-between steps. Even outside of tracking conversions within a session we can use it to keep track of cool things like people who came to our site, didn’t convert that time, but came back and converted within the next couple days .

Jill Quick has been talking a bunch about how powerful these options are.

We could use this to say something like: person landed on our event page and then landed on our thank you page within 10 minutes .

But as I’m sure you’ve guessed, that ends up being a kind of arbitrary cut off, maybe someone spends some time thinking about how to fill out our form, or maybe someone really quickly goes to one of our other pages and converts there. This could be better than the basic funnel, but we could also end up ignoring completely legitimate conversions.

Using GA4 sequences for this is kind of fine, as I say above it’s certainly not worse than Universal Analytics, but we could do better with Google Tag Manager.

These approaches require you to run all your tracking via Tag Manager. Though even aside

from this, if you’re not already using Tag Manager, I’d advise you to look into it!

Since we need to keep track of what’s happened to a user across multiple pages, these solutions are also going to make use of cookies. In case that fills you with dread, don’t worry:

I’m going to walk you through how to create and delete these cookies (it takes a little Javascript but it’s copy-paste and easier than you think!)

These aren’t the kinds of cookies designed to give away people’s information to other services.

To reiterate what I say above: While this approach takes a bit more effort than just doing things through Google Analytics it allows us to do two things:

Make sure all of our various tracking tags are firing in the same way

Have more fine grained control, particularly if we’re trying to categorise different paths to conversion.
