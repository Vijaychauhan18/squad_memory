---
source: https://yoast.com/cloak-affiliate-links/
title: How to cloak your affiliate links
scraped: 2026-03-23
published_on: 2017-01-24
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

# How to cloak your affiliate links

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/cloak-affiliate-links/
Published: 2017-01-24
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
There are multiple reasons why you should redirect or cloak your affiliate links. Learn why and how to do this in this post.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

We used to consult for sites that monetize, in part, with affiliate links. We normally advised people to redirect affiliate links. In the past, we noticed that there wasn’t a proper script available online that could handle this for us, so we created one to tackle this problem. In this post, I explain how you can get your hands on it and how you can get it running on your website.

A quick online search will result in tons of reasons as to why you should redirect your affiliate links. The “historical” reason for this is hiding from search engines that you’re an affiliate. It would be naive to think that search engines don’t understand what’s happening, but nevertheless, this seems like a valid reason.

There are also a few more advantages to cloaking your affiliate links, such as:

Step 2 ensures search engines won’t follow the redirects, but we’ll add some extra security measures in our script to prevent accidental indexing of our affiliate links. Step 3 is as easy as manually adding each redirect to your redirect directory’s .htaccess file, assuming you’re running your website on an Apache-based server. Alternatively, you can use the script we produced to make it easier on yourself. The added bonus of this script is that it also works for servers running Nginx!

The script we created consists of three files, one of which is optional: an index.php file, a redirects.txt file and, to finish it all off, a .htaccess file to prettify your URLs.

This file contains the logic that handles the actual redirection by performing a 302 redirect. Additionally, it sends a X-Robots-Tag header along to ensure search engines that can detect this header, obey the noindex, nofollow rules we pass along in it. We do this as an extra security measure in case you might forget to exclude the affiliate link in your robots.txt.

The redirects.txt file is a comma-separated file that contains a list of names and destination URLs like so:

Note that the file should always contain the following line at the very top to ensure people don’t attempt to redirect themselves to a non-existing URL:

Just change example.com to your own domain and you’re ready to go!

If you only install the above two files, you’ll already have enough in place to get things running. However, we advise you prettify the URLs because this dramatically increases the readability. Without prettifying your URLs, you’ll end up with something like /out/?id=yoast instead of /out/yoast .

Prettifying can be achieved by adding a .htaccess file to the mix. This small file also helps ensure people can’t access your redirects.txt file to take a peek and see what affiliate links are available.

In the past, we’ve received questions about using WordPress plugins to tackle this cloaking issue. Despite there being a lot of valid options, they have one small caveat: speed. Because these plugins depend on WordPress’ core code, they need to wait for it to be fully booted before being able to execute themselves. This can easily add a second or two to the total loading and redirecting time if you’re on a slow server. Our non-plugin solution is faster because it doesn’t depend on WordPress to run.

Ultimately, the best option depends on your needs. If you want to collect statistics on your affiliate links, you might be better off with a plugin. Otherwise, just use our script to keep things fast.

If you’re interested in running this nifty script on your own website, you can download the files . Feeling adventurous? You can find the source code on GitHub . People running Nginx can find sample code in this gist to see how to make it work for them.

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

Is this something that in the future Google might decide that they don’t like?

This is one of the best explanation for cloaking affiliate links. I have been using plugins to do redirects but from now on I will use a custom script like mentioned here.

Cool article, but it’s way easier to use ‘pretty links’ plugin, surely?

Very valuable to know. Instagram wouldn’t let me have affiliate link until I used this technique. Keep up the good work!

Wouldn’t this create a false bounce rate? As all clickthrougs on the first pageview would make it a bounce?

I have used a slightly different method for several years that works similarly. What I haven’t done is blocked the folder in my robots.txt file. (I’ve been doing it manually, but blocking at the source is more elegant and foolproof).

I notice the /out/ folder is not blocked in your robot.text file. Is this from a recent change, or no longer needed?

this is a clever way! In the past I even noticed some of my cloaked links appearing in the search engines and stats, did not quite block something properly :-) But, there is a caveat with Amazon, as they are not a big fan of cloaked links. They do allow something like EasyAzonPro to operate, but that plugin does show you are being taken to Amazon (when hovering). With your method I am not sure Amazon would approve, unless a site owner makes it really clear the link is going to Amazon (which is their main concern).

Yep, that is correct. I spent a few hours reading all their Associates agreements and they say it needs to be clear that you are linking to amazon. Else you break their Tos.

Surprisingly though: If you use amazons own site stripe quick link method you see something like this while hovering – http://amzn.to/2jdsKaw . Weird heh?

You failed to mention pixel tracking which I find doesn’t work with a redirect script.

Nice and handy little script. I got it running on my site now but can’t seem to make the links prettier via the .htaccess code. When I implement that I receive a 404 error. So using https://www.lenzencenter.nl/out/?id=lenson works, but I can’t get the link https://www.lenzencenter.nl/out/lenson pointing to the Lenson site.

I wonder what can be the problem. Amongst others I have WP Rocket running. Could this be causing my problem? How can I best test to get the pretty links working?

We care about the protection of your data. Read our privacy policy.
