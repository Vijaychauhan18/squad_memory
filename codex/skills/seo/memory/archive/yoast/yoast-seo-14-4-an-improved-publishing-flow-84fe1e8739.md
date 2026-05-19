---
source: https://yoast.com/yoast-seo-14-4/
title: Yoast SEO 14.4: An improved publishing flow
scraped: 2026-03-23
published_on: 2020-06-23
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

# Yoast SEO 14.4: An improved publishing flow

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/yoast-seo-14-4/
Published: 2020-06-23
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Yoast SEO 14.4 is out! Now, you'll find a new publishing flow helping you keep track of your SEO scores. Plus, a nofollow link feature!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Sometimes, you have releases that start out small and end up with a substantial improvement. Yoast SEO 14.4 is one such release. Initially plannend as a bug fix release, this turned into something that markedly improves the publishing workflow in WordPress. Plus, you can now mark your external links as nofollow or sponsored. You see, Yoast SEO 14.4 is a chockfull release!

Yoast SEO helps you optimize your content to make it awesome for readers as well as search engines. Over the years, Yoast SEO quickly turned into one of the most used writing tools in the world. We’re very proud of that, but we felt there were a couple steps missing from the publishing flow. Plus, we noticed people struggling to find our sidebar in the block editor. Our CTO, Omar Reiss, came up with the concept for improving this and built most of it himself — we even dubbed this The Omar Release internally. Thanks to him, we now have a flow that gives you more SEO insights throughout the publishing process.

One of the most important parts of Yoast SEO is the feedback you get from the SEO analysis and readability analysis. These tools make sure that your content is up to scratch. Now, we make sure that these scores are visible in a number of additional steps. In short, here are the three steps:

By adding SEO scores to these steps, we give you a better handle on your content quality. This is very helpful — sometimes you just need a little positive feedback to hit that publish button!

Did you know we have a sidebar in the WordPress block editor? No? Well, you’re not alone. Omar Reiss, had this to say on that topic: “We’ve noticed for a while that users new to the block editor have trouble finding our sidebar. In the Classic Editor, we’ve always been visible in the publishing screen, but for the block editor, we made an entire sidebar for Yoast SEO. To reach this, you needed to click the big Y logo on the top of the screen. In Yoast SEO 14.4, we’re making it much easier to find by integrating it in the Document sidebar. Now, you immediately see the familiar bullets once you open a post.”

We’re not just making Yoast SEO easier to find, but we’re also guiding people more. Omar: “SEO is crucial in the content publication process. We believe in holistic SEO and SEO plays a part in every step of the process. I’m happy that we can help people remember to work on that. Every post benefits from looking at it with an eye for SEO and the publication flow helps you do that. In addition, that final check makes sure that you can publish you content without hesitation!”

Omar didn’t just came up with the idea of these improvements, but he also built them himself. Omar explains: “I’ve been getting back into programming and for this project I had the chance to work with a couple of interesting Gutenberg APIs. These helped me to get everything going pretty quickly. I have to say, from an extensibility perspective, Gutenberg is maturing quickly! Soon, I’ll publish a blog post about my experiences with these Gutenberg APIs.”

The second addition is an easy way to block search engines from following outgoing links by setting them as nofollow or even sponsored . It has always been a good idea to mark external links as nofollow — especially if these lead to pages you don’t really endorse. In addition, you can use these attributes to show that these links are commercial and you don’t want search engines to follow them .

Recently, Google announced a new way to mark commercial links as such: sponsored . It is not mandatory to mark links you paid for with this new attribute, but it helps Google get a better sense of what happens with links on the web.

In the WordPress block editor, you can now easily mark links as nofollow . In addition, you can also mark these as sponsored in Yoast SEO 14.4. When you mark a link as sponsored , it automatically also applies a nofollow to that link. This is according to Google’s guidelines.

More background in our help documentation on which link setting you should use .

You can see third new feature as part of the publishing flow mentioned above, but I’d still like to highlight it separately. In Yoast SEO 14.4, we made it much easier to share your freshly published post on social media like Twitter and Facebook. After you’ve hit Publish, you will be greeted with a new Share your post setting. Simply click the Facebook or Twitter icon to publish your new masterpiece to the corresponding platform.

That’s Yoast SEO 14.4 for you! This release comes with a better workflow for publishing SEO-proof articles, including a new way to share your content on social media. In addition, we made it a lot easier for you to discourage search engines from following external links.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

I updated a couple of days ago and my Yoast settings are all but gone! Go green/red lights, etc. And certainly no sidebar features. Help?

Hi there Michelle. Sorry to hear about these issues. I think it’s best to contact our support team about this: https://yoast.com/help/support/

I am not seeing the mark outgoing links with nofollow/sponsore on the link function. I have Version 14.4.1.

Hi Carolyn. Are you using the block editor or the classic editor? This feature only works in the block editor, so that might be why you don’t see it. Do try the block editor, it’s really cool!

I like the new features, but is there a way to add “NoFollow” Links to all existing external links? I used a plugin to do this before, but now that I can get this function in Yoast, I’d love to just delete that other plugin.

It would be nice to have an “Apply to all external links” option instead of having to change each link one by one. I’ve got A TON of outbound links.

Hi Lezli. As of now, there’s no way to add a nofollow to all existing external links on your site by pressing a button. What you can do, though, is apply a nofollow per page by using the nofollow feature on the Advanced tab of Yoast SEO: https://yoast.com/help/should-search-engines-follow-links-on-this-page/

Really like the new updates. Any chance you’ll be adding LinkedIn to the Socal Media integration?

Thanks! And LinkedIn might be added in the future, but I’m afraid I can’t give you a definitive answer to this question right now. Sorry about that!

Thanks for the additions! Quick question here. Who has to request the sponsored link label? The advertiser that pays for the link or the provider? How to proceed if the advertiser asks for his advertisement not to be labeled as sponsored? Should you decline the ad all together or just provide him the nofollow option?

Hi Patricia! Usually, the site owner determines what kind of link it will be. It’s in Google’s guidelines to use the sponsored tag for paid links and we ‘d advise adding the nofollow attribute too, as not all search engines support the sponsored attribute yet. Therefore, Yoast SEO automatically adds nofollow to a sponsored link too. To be honest, it sounds a bit shady if someone doesn’t want the link to be marked as sponsored while it is. Not something we’d advise, in any case. If it’s a link from your website, I’d only agree with a nofollow or sponsored link to the advertiser. Here’s more about nofollow and sponsored links: https://yoast.com/outbound-link-sponsored-nofollow-ugc-attributes/

I rather like the new updates, especially the ability to edit the links without headache with necessary tags.Looks like some great features.

Hi Amrita, thanks so much! We love to hear that, as this workflow is meant for exactly that: to make publishing new content easier :)

Shame the “Mark outgoing links with nofollow/sponsored” doesn’t work in the classic editor

Hi Sara, you’re right. This feature can be found in the block editor, but not in the classic editor!

In case you want to read more about the block editor and why we recommend using it, have a look at https://yoast.com/the-block-editor-gutenberg-why-you-should-be-using-it/

This is a great feature plugin. I always use Yoast on all my website.

Awesome! That’s great to hear! And thanks for your kind words :)

Does the “nofollow” and “sponsored” attribute stay even if the Yoast SEO plugin was uninstalled? Not that I’m planning on uninstalling Yoast considering I think it’s the best, but it is an issue I’ve had with plugins that do this in the past.

Hi Thomas! Yes, everything you add via the new link feature will be saved. These attributes will still be there once you remove the plugin, which, of course, we’d rather not have you do ;) You can test this, of course, so you can see how that works.

Hey I’m looking for some detail on the bug fixes in this release. For the last two days, when I go to share on social, the image and meta data aren’t pulling through. Wondering if that’s a yoast issue?

Hi Charlotte. I’m sorry to hear that. Unfortunately, we haven’t received any new bugs regarding social sharing. Maybe you could try following these steps to figure out what’s going on: https://yoast.com/help/facebook-sharing-updated-details/ . Good luck!

Hi Eli, sorry to hear that. Which exact feature do you mean? The nofollow/sponsored link feature?

Is there a way to disable the nofollow/sponsored links feature? I am using the EditorsKit plugin which comes with this feature and is better implemented. After update, this plugin now overwrite the EditorsKit feature.Is there a filter that I can use to disable this feature?

First of all, dare I ask, why do you consider theirs better? Theirs is based on older Gutenberg code that has since changed, and they haven’t updated. Unfortunately, we both have to overwrite the link feature in Gutenberg as they’ve not made it extensible, which is what causes this sort of problem.

I am not sure about the code. I didn’t like the new link interface as it chop off a long URL (I like to see the URL I am linking to, at a glance). Also if I need to add “Open in a new tab” and “nofollow”, it requires a double effort, as the link window closes after each click. In short, it is not that I find the EditorsKit’s implementation is better, but that the latest Gutenberg link interface is poorer in usability.

those are all valid points of feedback that I’m certain the Gutenberg team would like to receive on their Github repo :)

Hello everyone. I loved yoast. It helped me to improve my website seo and also I have learned a lot. Wish all the best.

This is a great feature. I always use Yoast on all my blogs. But I will love it if the option where you can add all the external links with nofollow with just a click of hand is in place. Adding nofollow one after the other is very tiring and you may sometimes not remember to do that if you are publishing a lot of posts each day.

Hi Ann, thanks for using Yoast SEO! We do offer the option to nofollow all the links on one page, if necessary. You can find the explanation here: https://yoast.com/wordpress/plugins/seo/yoast-seo-robots-meta-configuration/ (please scroll down to individual posts/pages). That might help you out a bit! Nofollowing all outbound links on a website isn’t something we recommend doing, because search engines need links to discover content. There must be links on your site search engines should follow, right?

This plugin is very popular and is installed by millions of active users. I wrote a short review of this plugin update with the addition of new features, on my personal blog, in Bahasa Indonesi.

Hi! I still haven’t updated from 13.5 because of all the bugs reported in the inital 14.0 release. Is it safe to update now if i have other plugins like WPML and Advance custom Fields that haven’t reported compatibility?

Is it necessary to do On Page SEO for Contact Us page and for the Career Page. If so how can i do without content
