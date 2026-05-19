---
source: https://yoast.com/testing-yoast-seo-7-0/
title: Help us test Yoast SEO 7.0
scraped: 2026-03-23
published_on: 2018-02-22
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

# Help us test Yoast SEO 7.0

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/testing-yoast-seo-7-0/
Published: 2018-02-22
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
We having something special for you today: a preview version of Yoast SEO 7.0. This is one of our biggest releases yet and we need your help making it as awesome as possible. Please help us test Yoast SEO 7.0!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

We have got something special for you, but before we release it for real, we need your help testing it: Yoast SEO 7.0. This is one of the biggest releases we have ever done, hence the jump from version 6.3 to 7.0. We’ve greatly simplified the interface, deprecated unused features and combined others into smarter features. By cleaning up our code, we have also drastically improved the performance of the plugin. Now, we need your help testing Yoast SEO 7.0 so we can fix every bug we can find before the final release two weeks from now.

You can test the latest beta for Yoast SEO 7.0 by downloading it and installing it in your WordPress backend. We would advise you to install it on a test install or staging environment. Installing it on a live site is at your own risk . As always, make a backup before playing with beta software.

Download Yoast SEO 7.0 beta here » (this beta is no longer available)

Please report any issues you find in our Yoast SEO GitHub repository . You can find more information about the process on the Contributing to Yoast SEO page . Together, we can make this an incredible release.

There’s going to be a lot of changes in Yoast SEO 7.0, both visible and invisible. See the changelog for the full list of changes . Here, I’ll go over some of the most obvious changes within your favorite SEO plugin. It all started with a quest to simplify things…

The configuration pages will be different, simpler, more user-focused.

The “Meta Robots” setting in the old version does exactly the same as the “Allow search engines” question in the new one but is understandable to people who have less experience with SEO.

In the old situation, Yoast SEO had an XML sitemaps menu item. In it, you could exclude “post types” (like Posts and Pages) and “taxonomies” (Categories and Tags, for example) from appearing in the XML sitemap. The only reason you would want to exclude post types and taxonomies from the XML sitemap is when you don’t want them to appear in the search engines. So… If your answer to the question above was “No”, I don’t want <x> to appear in the search engines, we now also exclude them from the XML sitemap. This might seem like a simple change, but it took a large portion of our options away in one fell swoop.

You could also disable XML sitemaps entirely on this menu item. This is what we call a “feature toggle”. This toggle has been moved to the Features tab on the Dashboard.

The Titles & Metas menu item has been renamed “Search Appearance”. There are a few more settings on this page now, but in a more logical arrangement:

General & Homepage have been combined. This tab also features the contents of the “Your Info” / “Company Info” tab we had on the Dashboard before. Media is new and is explained below. Breadcrumbs and RSS were moved here from the Advanced menu item, which is now completely gone.

When you upload an image or a video to WordPress, WordPress automatically creates an attachment URL for it, next to allowing you to link to the media item directly. This is much the same as a post URL, but it has no real SEO value. Most sites therefore never use these attachment URLs, but because WordPress sometimes links to them, they do start being indexed by search engines.

Yoast SEO long had a feature that allowed you to redirect attachment URLs for images to the post they were embedded in. This seems logical. But an image can be embedded in multiple posts, and as the Media part of WordPress gets better, this happens more often. At this point, where do you redirect an attachment URL to?

It also means that images that are not attached to a post could not be redirected. So we’ve changed that behavior: there’s now a toggle that will disable all attachment URLs. If you enable that (which will be the default for new sites), we redirect all attachment URLs to the media item itself. Clean, simple, much better SEO wise and much easier to understand.

The Advanced menu item had three tabs: Breadcrumbs, Permalinks, and RSS. Breadcrumbs and RSS have been moved to Search Appearance; Permalinks is gone. There were two features there that we kept around:

For a while, Yoast SEO had a toggle for advanced features. This felt like a good idea at the time, but instead of properly explaining features, we hid them. In Yoast SEO 7.0, we’ve improved all features that were hard to explain. Luckily there were only a few of those, and they were so old that I’ve had to delete code that I wrote myself ten years ago.

Under the hood, there have also been several performance optimizations. We’ve changed how we set and retrieve options. We’ve removed all functions that had been deprecated before 2017. This is old code that we no longer use but was kept around for backward compatibility. These changes lead to less memory usage and a faster plugin overall.

Well, to be honest, I have to give credit to Yoast Academy for this one. I was recording screencasts of the backend and couldn’t stand some of the things I had to explain. So we decided to start fixing them. Our development team has worked very hard to keep up with all the ideas, and we’re very proud to show you what we’ve built.

Because 7.0 is a big thing, we thought we’d make it even bigger: Yoast SEO is getting a new icon. The traffic light we’ve used for so long has turned out not to be a good metaphor across all cultures. In fact, we’ve learned that traffic lights differ per country and green is sometimes on top, and sometimes on the bottom.

So, without further ado: this is the new icon for Yoast SEO:

We’re planning to release the final version of Yoast SEO 7.0 on Tuesday, March 6th. Since this is such a big release, we’ve decided to extend the testing period by two weeks so we can get as many eyes as possible on this release before we push it to everyone. You can help us find and fix issues by installing the release candidate, as mentioned above and go on a bug hunting trip. Add any issue you find or feedback you have to GitHub.

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

Dear Joost, Thanks for creating such a great product. I’m still on the free version, but hope to progress to the more advanced version in the near future.

Just a small thing i’ve noticed, that maybe useful for your next upgrade.

The “Featured Image” that can be loaded on a standard WP page…I’ve noticed my loaded images are often not pulling through specifically on Facebook (i’m referring to the featured image). I think it maybe related to the image size loaded in the Media section of WP.

I’m just wondering if this is the solution, if you could not build in an automatic image sizing feature for this function as i have a feeling FB does not like images that are not correctly sized to their dimensions.

Regards from Cape Town, and thanks again! Keep up the excellent work. Stephen.

Hi Hendro, not sure if you mean you use Yoast SEO premium or another plugin? Either way, yes, we believe 7.0 is much more powerful: smarter, faster and easier to use! And just so you know, of course Yoast SEO premium will be updated as well ;-)

The media URLs can be a nightmare so I’m glad to see Yoast is stepping it up in this area! Are there plans to update the bulk editing tool? It would be nice to be able to assign simple settings (keywords, indexing, and slug) all in one go.

Don’t worry, Gulshan, we’re still all about sensible default settings! We’ve just improved a lot of things and made configuration easier :-)

Good news, I hope the problems of the previous versions have been solved.

Hi Joost, I am using Yoast plugin, how the new update works and affects my website….. Please help me with some valuable inputs…

Hi James, you can read about the changes above! Please do note that this is a beta version. Using it on your live site is at your own risk.

I’m testing the new beta. Looks fine. However there is no sitemap generated. I’m testing on a virtual machine an not on port 80. Can that be the reason?

What does it mean to rewrite titles in General & Homepage? Must be active or disabled? which one is better?

Will take it for a spin during the weekend Thanks again for a great plugin!

Great, we will see another great Yoast Version, thanks from my soul.

This is what i’ve been waiting for. I’m currently testing Y7 on my localhost. Thanks for this excellent plugin.

Pages with duplicate title tags and now google webmaster giving error with – Pages with duplicate title tags how can it be sloved?

if your pages have duplicate titles that means you don’t use the %%page%% magic variable in your title settings. I’d recommend doing this in all the templates for archives that can be paginated.

Number of index pages Example: yoast.com/page/2 yoast.com/page/3 yoast.com/tag/seo/page/2 yoast.com/tag/seo/page/3

Thank you Joost, I just downloaded my copy and I am looking forward to have it installed on a brand new site I am going to start building. This is an awesome plug in, and I believe it is going to be even better than the previous version. Thanks for sharing

Awesome. I have downloaded the version 7 and looking forward to test it on my subdomain.

Hey Jose, First of congratulations for updating your plugins. If we see some error on your plugins so I am definitely tell you. Regards, Basit Ansari

I’d still love to know when the feature will be available to strip links from your site via main-sitemap.xsl . It’s a healthy start that you added the “noopener noreferrer” unlike previous versions. But I’d rather pay for a premium version to disable this then keeping a backup file every time a new version comes out.

Why are you worried about that link? It’s not a crawlable link, it’s in the stylesheet…

Why must you have a p class=”expl” in the first place? The H1 title does a perfectly good job explaining what it is. After-all, it’s just a sitemap and not a full web-page thus the rules of writing a paragraph to maintain SEO does not matter.
