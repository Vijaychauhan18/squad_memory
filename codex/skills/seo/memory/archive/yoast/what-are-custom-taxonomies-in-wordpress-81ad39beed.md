---
source: https://yoast.com/wordpress-custom-taxonomies/
title: What are custom taxonomies in WordPress?
scraped: 2026-03-23
published_on: 2017-08-28
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

# What are custom taxonomies in WordPress?

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-custom-taxonomies/
Published: 2017-08-28
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Custom taxonomies allow for easy content grouping in WordPress. Go check out what custom taxonomies are and how you can use them on your site!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

In WordPress, content can be grouped using categories and tags by default. WordPress calls these groups taxonomies . When you are serious about your content and have a lot of it, it will pay off to create other groups as well. By creating these custom taxonomies, you’re making your life as a content writer easier. More importantly, you’ll structure your website to your best effort for your visitors. They’ll be able to locate content that’s relevant to them and find related content more easily. This article will dive into the use of custom taxonomies.

WordPress introduced the concept of tags in version 2.3. As described by Wikipedia , a tag is ‘a non-hierarchical keyword or term assigned to a piece of information.’ This means WordPress has had a hierarchical way of classifying information (categories), and a non-hierarchical way of organizing information (tags) since version 2.3. As far back as 2006 (!), people were discussing the fact that tags are not categories. The problem is that WordPress calls them both ‘taxonomies,’ but that’s not entirely correct. The word taxonomy assumes a hierarchy of sorts, as explained on another Wikipedia page .

With version 2.8, WordPress introduced custom taxonomies . Or actually, allowed easier access to the already available backend for custom taxonomies. These custom taxonomies can be either non-hierarchical (e.g. ‘tag’-like) or hierarchical (e.g. ‘category’-like). But for now, only the non-hierarchical taxonomies benefit from the smooth integration. These are more like actual taxonomies though, as they add a kind of hierarchy to the tag structure.

Let me give you an example: you could have a ‘People’ and a ‘Places’ taxonomy. Say, you write a new post and decide to add a keyword in the ‘People’ taxonomy. By doing that, you’re saying that it’s a keyword (or tag, if you want) of the type ‘People,’ so it is hierarchical in a way. But it also makes the keyword that much more informative, as it adds another layer of information.

Some years ago, Roy Huiskes made this visual for us by making a graphical explanation of the subject:

Fun fact: That People taxonomy section in the image above would include some more branches nowadays .

You can imagine using this for locations, or employees on a company site, but also writers on a book site, destinations on a travel site, etcetera. It groups items in a convenient way, both for maintenance and your visitors.

Adding custom taxonomies in WordPress isn’t that hard. To manually register a taxonomy, you can use the register_taxonomy() function. Most WordPress developers have probably used this one time or another, right?

WordPress.org has an example of how to approach this for a People taxonomy:

This piece of code adds a meta box to your WordPress post edit screens, that looks like the tag box. It even works in the same way. I’m not a fan of tag clouds, but yes, in theory, you could even create a cloud for your new taxonomy. For a more in-depth explanation, check this post by wpmudev.org (2016).

These custom taxonomies can be public and private, which also makes them extremely useful for internal grouping of elements as well. I can imagine grouping VIP users, social influencers; you name it.

So, in conclusion, custom taxonomies can be very useful. If you have loads of content and want to create order, for both yourself and your users, you could use them.

That leaves me with two questions: Are you using custom taxonomies and if yes, how did you add these to your site? I’m looking forward to your answers in the comments!

Michiel was one of our very first employees and used to be a partner at Yoast. Kick start your site optimization with his articles!

I do not use categories in my blog post permalink. I think this is the best way. I also do not use /category/ in my category page.

Thank you for this article, currently i am using your yoast seo premium Plugin and this article help me lot…

For your blog post permalink settings, try: /%category%/%postname%/

We care about the protection of your data. Read our privacy policy.
