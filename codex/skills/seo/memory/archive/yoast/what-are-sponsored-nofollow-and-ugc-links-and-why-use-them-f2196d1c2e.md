---
source: https://yoast.com/outbound-link-sponsored-nofollow-ugc-attributes/
title: What are sponsored, nofollow and ugc links, and why use them?
scraped: 2026-03-23
published_on: 2020-06-24
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

# What are sponsored, nofollow and ugc links, and why use them?

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/outbound-link-sponsored-nofollow-ugc-attributes/
Published: 2020-06-24
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Search engines need a bit of help to qualify links; use the nofollow, sponsored and UGC attribute to help them out. With Yoast SEO it's easy!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Links are an important part of SEO. Without links, Google (or other search engines) may not discover your pages, or might not think that they’re important. Sometimes, though, you might want Google not to follow a link. Or you might want to tell them a particular is sponsored , or added to your page by a user. Why’s that? And how do you implement this on your website? Learn all about sponsored , nofollow and ugc links here!

When you link to another website , search engines may count that as a ‘vote’ for the page you’re linking to. Pages which have many such ‘votes’, from authoritative and trusted websites, may rank higher in the search results as a result (as they, in turn, become more authoritative and trustworthy). That makes links a kind of currency .

That’s why a good SEO strategy should always consider how the types of content, marketing and PR that you do will encourage other websites to link to you. If you’re not already thinking about how your site can earn links from others, our guide to link building tips and tactics is a good place to get inspiration on where to start.

In the past, but still even today, people try to game the system by buying links. Obviously, that’s not the way to go; Google’s penguins might come after you! That’s why we recommend holistic link building , which boils down to creating great resources for your audience and reaching out to get the word out, eventually leading to more links.

But, what happens if you want to link to a page, without voting for it? And, what stops people from finding ways to cheat the system, such as posting links to their site on your website; on comment forms, forums, or social media profiles?

In these cases, we need to use a special type of link, to tell search engines that it shouldn’t be trusted.

In the early days of SEO, many unscrupulous marketers realised that they could easily get hundreds of links to their pages by leaving spam comments on other blogs, by buying links from webmasters, or from placing links on any site which allowed user-submitted content.

To combat this, in 2005 Google introduced a way to mark a link as untrusted ; specifically, a way of saying “don’t follow this link”. By adding a nofollow attribute to your links, they’d no longer count as votes. It also became Google’s policy that any link which is paid for (typically an advert, paid placement, or similar) should use a nofollow attribute to indicate that it shouldn’t affect their ranking calculations.

That’s because paid links are the same as a ‘vote’ for a page. For instance, if someone pays you to put an ad on your website, you might send some visitors to the advertised page or product. Since it’s not a natural endorsement, link value shouldn’t pass on to this particular page; search engines shouldn’t rank it higher because you’ve received some kind of compensation for that link.

This also made it possible to link to a page which you don’t endorse, but you still want to use it as an example in your copy (e.g., “I tried this product , but it was horrible” ).

Today, almost all comment systems and social media platforms automatically add a nofollow attribute to user-submitted content.

Let’s take a closer look at a link. In HTML, a plain link looks like this: <a href="https://www.example.com">example link</a> . You probably use these types of links a lot throughout your content. You use them to point readers to interesting, related content on your own site or someone else’s website.

If you want to indicate that you don’t trust the site you’re linking to, or that it’s a paid placement, including the nofollow attribute would look like this: <a href="https://www.example.com" rel="nofollow">example link</a> .

So far, we’ve only considered whether external links should be nofollow’d . In some cases, it might also make sense to mark an internal link with a nofollow attribute. In Yoast SEO, we automatically add a nofollow attribute to internal links which point to your login or registration pages. This prevents Google from wasting resources crawling and evaluating those pages.

It’s important to understand that most search engines treat nofollow as a ‘hint’, and might follow them whilst still ‘devaluing’ them. An announcement from Google in September 2019 clarified this:

Links contain valuable information that can help us improve search, such as how the words within links describe the content they point at. Looking at all the links we encounter can also help us better understand unnatural linking patterns. By shifting to a hint model, we no longer lose this important information, while still allowing site owners to indicate that some links shouldn’t be given the weight of a first-party endorsement.

In September 2019, Google announced two new types of link attribute. It’s now possible to mark links as sponsored or ugc (short for ‘user-generated content), as well as nofollow . They explained that:

In both cases, these work similarly to the original nofollow attribute – they tell Google note to count the link as a ‘vote’. We don’t know precisely how Google uses this data internally, but they’ve hinted that it’ll help them understand more about the link. That might improve how they count ‘votes’ and evaluate pages.

In July 2020, Bing updated their documentation to clarify that they, too, support the sponsored and ugc properties.

That means that we have four different types of HTML markup for links:

Whilst each of these attributes describe different types of links, it’s possible to combine various rel attributes in one link. For instance, a sponsored and nofollow attribute can exist in one link: <a href="https://www.example.com" rel="nofollow sponsored">example link</a> .

This is useful, because not all search engines support the two new rel attributes, so it’s best practice to use the nofollow attribute along with the sponsored and ugc attribute.

So, now you know what these links and rel attributes look like. But why and when should you use them?

An advertisement or link you get paid for or in any other way should use the sponsored attribute. The reasoning behind this is that Google sees links to a page as an endorsement; you link to an article because it’s a valuable resource you’d like to point your users to. When you get paid to place a reference to another website your motivation is different. It might be something you wouldn’t link to without compensation. With the sponsored attribute Google can differentiate these “unnatural links” from normal links.

As other search engines won’t recognise this sponsored attribute (yet), we do recommend to add the nofollow attribute to this type of link as well.

You should use the ugc attribute whenever users of your website are able to create content or links on it; e.g., in the comment section on your site. If you’re on WordPress, there’s no need to worry about this attribute; WordPress automatically adds a ugc attribute, as well as a nofollow attribute – a specific request from our team – to the links in the comment section on your site.

As not all search engines support the sponsored or ugc attributes, you should still add the nofollow attribute to both these type of links as well.

While this might sound a bit complicated when you’re not an HTML native, qualifying links is simple with the WordPress block editor and Yoast SEO. Since Yoast SEO 14.4 we’ve added an option to easily add a sponsored or nofollow attribute to a link in your content.

If you want to nofollow a link or qualify it as sponsored (and nofollow at the same time), click on the link icon, paste your link and you’ll see these options:

Select the option of your choice by moving the slider and you’re done! Rather watch a video? Check this out:

You’ll find more about this on our help page on link settings. Good luck!

Willemien was the Manager Content of yoast.com. She loves creating user-friendly content and making it easy to find for people and search engines.

I have the latest updates in Yoast premium but I am not using block editor. Does that mean I cannot use this feature? I don’t see any of those options when I click on the link icon.

There’s a small plugin that does something similar and that also works with the classic editor: Title and Nofollow For Links

Hi there. You’re right. This feature can be found in the block editor, but not in the classic editor, unfortunately!

In case you want to read more about the block editor and why we recommend using it, have a look at https://yoast.com/the-block-editor-gutenberg-why-you-should-be-using-it/

So say for Amazon Associate links as an example I should use nofollow and sponsored when I use them or any other affiliate program link?

Thank you for this article, and the new feature. I believe it will make it much easier to remember to set these attributes In the first place. Not to mention the guideline of when to set a follow/sponsored/ugs attribute is good to have at hand :)

Hi Wiebke, thanks so much for your comment! And wonderful to hear that you find this article (and our new feature) helpful :) good luck with your SEO!

Thanks for sharing such an amazing article which is quite helpful. I am new in SEO and still learning more things about it. Till now I have not come up with UGC, It would be helpful for me if could add the full abbreviation of UGC.

Hi Gourav, you’re welcome! I hope this article helps you determine which link attributes to use and where! If you have any questions, let us know :)

Hi, I read your article and found everything is useful. I have understood everything about nofollow, sponsored and ugc links. Are these links helps to increase rank ??

Hi Vijay, these links help you tell Google which outbound links are natural endorsements, and which are not. You can view the use of these links as a part of a holistic SEO strategy, seeing that you might not have ‘endorsed’ a sponsored link if you did not receive some kind of compensation for it. But to learn more about the importance of outbound links for SEO, I would recommend reading this article: https://yoast.com/outbound-links/

Hallo super Sache hier alles past hier auf Yoast SEO mfg Oliver

Thanks for such and enlighten content … I don’t know nofollow and other types of links but you have helped articulate it all But when linking to external post or my post i don’t to see the option to set as nofollow or dofollow .. Is this a new development or there’s something I’m missing out

To answer your question: this feature can be found in the block editor, but not in the classic editor. So that might be the reason why you’re not seeing it.

I am a newbie blogger was struggling with understanding of these links strategies, your blog explained it well. Also, I would like to know why in my Yoast SEO I am not able to see no follow and sponsored option. I only get open in new tab option when I click on the link button. Is it available only in premium version?
