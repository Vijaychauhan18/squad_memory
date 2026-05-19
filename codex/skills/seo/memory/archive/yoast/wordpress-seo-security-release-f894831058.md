---
source: https://yoast.com/wordpress-seo-security-release/
title: WordPress SEO Security release
scraped: 2026-03-23
published_on: 2015-03-11
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

# WordPress SEO Security release

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-seo-security-release/
Published: 2015-03-11
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Read more about WordPress SEO Security release - from Yoast

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

This morning we released an update to our WordPress SEO plugin (both free and premium) that fixes a security issue. A bit more details follow below, but the short version of this post is simple: update. Now. Although you might find your WordPress install has already updated for you.

We fixed a CSRF issue that allowed blind SQL injection. The one sentence explanation for the not so technical: by having a logged-in author, editor or admin visit a malformed URL a malicious hacker could change your database. While this does not allow mass hacking of installs using this hole, it does allow direct targeting of a user on a website. This is a serious issue, which is why we immediately set to work to fix it when we were notified of the issue.

Why we didn’t catch it? Well… Long story. It should have been caught in one of our regular security reviews. The values were escaped using esc_sql , which one would expect would prevent SQL injection. It does not. You’ll need far stricter sanitization. Not an excuse but it’s a good lesson to learn for other developers.

We were notified of this issue by Ryan Dewhurst of the WPScan team, who waited for us to release an update before publishing his find to the public, for which we thank him! This type of responsible disclosure is what keeps us all safe, but it only does so if you update .

Because of the severity of the issue, the WordPress.org team put out a forced automatic update (thanks!). If you didn’t specifically disable those and you were:

If you are on an older version, we can’t auto-update you, but you should really update for tons of reasons. Of course you should really move to 1.7.4 as soon as you can anyway.

Note: If you’re using WordPress SEO Premium, you should immediately update to version 1.5.3. You can find the how-to in our knowledge base .

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

yeah, have encountered the plugin deactivating itself on MULTIPLE sites over the last week…this is definitely an issue

looks like you didn’t like my other email address as my previous reply looks like it went through.. here is my issue:

i recently took over a site that is using thyis plugin version 1.5.2.6 and when i upgrade to 1.7.4, the site breaks.. all of the pages give a ‘not found’ and i’m not sure why. i don’t think the previous person did any custom coding as they weren’t technical enough but they did update a lot of the settings for this plugin. is there something i can look at that makes this happen that maybe someone else encountered?

tried using this reply form 3 times now and can’t get my issue posted.

Some of my clients websites were having issues after the update but was a easy fix and up and running now.

Love the plugin but I’ve had to disable WordPress SEO (1.7.4) as it doesn’t work with my WordPress 4.1.1 running the Radius theme – happy to pay for the premium version, but need assurances it will work first!

Thanks for getting this sorted guys, I better crack on and get 30 or so sites updated.

It’s nice to see such a great plugin actively maintained. When i first heard about this security patch it was from another sources. Yet my dashboard was saying there are no updates available. Later i saw it was done automatically .

Hi, I tried to update from 1.7.1 for a client but was not able to. What might be the reason for that? Thx for your help!

Thanks! Update successfull, two older Versions I updated via FTP.

I have WordPress SEO on version 1.5.3 and it doesn’t give me the option to update. Also when I go to Plugins and search to download a newer version the option isn’t there.

I am using this plugin for the seo, but thank you for this update, now my blog is secure :)

My version hasn’t auto updated (currently 1.7.1) yet. If I just download and do a manual update, is that ok? Will I keep all my settings from the current version? Should I deactivate 1.7.1 first or just install 1.7.4? Thanks

Is there already any news on what to with affected sites, we had a massive break in on three sites on the same shared hosting on the 11th at around midnight (the plugin was at that time not updated), malicious files were uploaded, unknown admins registered and tons of posts inserted directly through SQL.

After following whatever I could find it seems I have managed to banish the unauthorized access yet the posts like this one:

are still there, WordPress does say that there is 29000+ posts, yet I cannot see them. I haven’t found any literature on systems affected by this bug yet and was wondering if anyone would know what to do.

Actually the websites don’t contain any posts posted by me so if there is an SQL trick to simply delete all of them this would probably suffice.

Hey Can I use this Plugin In My Blogger Blog ? Please Reply as soon as possible..

Just to corroborate on what Apoorv Agrawal said on sitemap issue. I’m having the same problem, my sitemap page is showing 404 error page.

Well hello yoast I don’t know since how long this issue was up but one thing that I’m certainly getting issue with is site map site map is not getting generated rather it’s talking it to 404 pages! Hope to get a solution!

Thanks for the quick fix and communicating to us officially about this issue.

Currently using free version and giving so impressive results..will be going for Premium version very soon for more features..

Just made the update for the plugin. It’s working fine now and there’s no error for my blog at all.

Thanks for the quick fix. SEO Yoast in the best SEO plugin :)

Just few days ago, I activated the automatic plugin update feature in my WordPress, and now I can thanks to the option for securing my websites while I was enjoying my sleep.

I received couple of messages from friends about the security breach, and vulnerability. I took sometime to manually check each and every installation of my WordPress that runs SEO Yoast plugin.

My site’s plugin was also deactivated. If Yoast didn’t do this, I wonder who / what deactivated the plugin on so many of our websites.

I´ve 2 websites they have ver 1.4 and didn´t update automatically, so I´ve to upload the latest version manualy, right? Is there the possiblity of loosing my custom Title and Meta Tags?

So what happen to the websites already attacked? I can see spam links on the top of my page? I discover this issue few weeks a go and we thought its from Contact form 7. Never guess its from yoast. Thanks Don

It’s probably got nothing to do with this issue, to be honest. We’ve not seen hacks in the wild yet.

Thanks for the update Joost de Valk. I have updated plugin just now!

@ambrosite asked what the fix was but no answer. It looks like WPSEO_Utils::filter_input() is called, which calls filter_input(). As FILTER_DEFAULT is filter used (without any flags) and PHP docs says: “This will result in no filtering taking place by default.”, how does this fix the issue?

Look a bit further, we added sanitization functions that restrict the order and orderby values to a limited set.

Thanks. I had only looked around the lines mentioned in the WPScan disclosure. I will have to study the code to learn from it.

ive just looked through Yoast WP SEO plugin interface for a clients install and cant see version number reference anywhere, only ref is to verison 4 which i presume must be WP not Yoast , where do we look to check version number ?

Well, a good place to find the version number for any plugin would be on the WordPress plugins page in your install :)

cool cheers, im looking at a WP Multi User instal so cant see it since not a network admin but the developer has confirmed latest version so all is good , thanks

I have to say, “one would expect this would prevent an SQL injection” is somewhat rude. I write code that is used by almost nobody, and I take the time – my own time – to read the documentation of every single function I call. I don’t want to diminish your character or the nature of your contributions to the Internet and to WordPress as a whole, but this is a very flagrant piece of damage control. I’m compelled to call it out, I was recommending Yoast to my employer just this morning and I am quite embarssed. I really do regret it, now. Sorry, Joost but… they run a serious business and will be targeted.

first of all, this code was contributed by an external developer. Second, this was reviewed multiple times and not found before. If you can guarantee me that if I let you do code reviews we’ll never find anything again in the code you have reviewed, I’d like to hire you!
