---
source: https://moz.com/blog/resolve-technical-issues-whiteboard-friday
title: Technical SEO Issues — How to Resolve Them
scraped: 2026-03-22
published_on: 2025-03-14
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

# Technical SEO Issues — How to Resolve Them

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/resolve-technical-issues-whiteboard-friday
Published: 2025-03-14
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Discover three hidden technical SEO issues silently sabotaging your website! SEO expert Kristina Azarenko reveals how improper buttons, background images, and lazy loading prevent Google from crawling your content, plus actionable fixes to boost your site's visibility.

## Extracted Body
Discover three hidden technical SEO issues silently sabotaging your website! In this edition of Whiteboard Friday, republished from the Moz archives, SEO expert Kristina Azarenko reveals how improper buttons, background images, and lazy loading prevent Google from crawling your content, plus actionable fixes to boost your site's visibility.

Hey, my name is Kristina Azarenko. I'm a Technical SEO Consultant, turned a course creator. I packed 10 years of my experience into two popular courses, Technical SEO Pro and Azure Friendly Website Creations. And I learned early in my career that in technical SEO, the devil is in the detail.

Because you might think that things are working properly, but then when you look under the hood, you might find that there is some minor technical SEO issue that is actually costing you lots of traffic.

And today I'm going to show you three specific examples of these unexpected technical SEO issues that you can find on your or your client's website potentially, and then how to resolve those issues. So let's start.

The first one is buttons versus links. What do you know about this?

So buttons trigger an action like adding it to a cart or submitting a form. And links point from page A to page B, or page one to page two, whatever. They serve as part of internal linking or external linking and really help with navigation across the websites. And then buttons can be styled as links, and links can be styled as buttons. That's where things might get tricky.

And one more thing is that from a web perspective, buttons are added with a button or input if they're a part of the form. And links are added with a href and then a URL.

The issue happens, though, when buttons serve as links. I've seen it on many websites when people want to style a link as a button, but then they want to add the link there. And what they do, is they use window location and then href URL, or they use an on click event to the URL.

Well, from a user perspective, nothing is different if there is a link or a link added like this into a button. But from a web development perspective, from a web sender's perspective, that makes a huge difference because, in this case, you rely on Google to interact with your content, and Google doesn't. And in this case, in the second case, when you have href and then the URL, you're actually telling Google everything is great. You just use this link to attribute it to the internal linking on my website, and that's exactly what you want to do, especially in the main navigation of the website.

To sum it up, when it comes to buttons and links, use links to point from one page to another page. Use buttons when you want to trigger some action like adding to a cart or submitting a form. And don't confuse the two. That's it. These are the rules. They're pretty simple, and they will definitely help you in different situations when you need to decide what element to use.

Okay, so onto the next one: images as backgrounds. It's not surprising that images are important because they appear in Google search results and drive image search traffic, but this only happens if Google can actually index those images.

The issue, though, happens when images are added as background images with CSS. Again, I've seen it so many times when people use background images while, in reality they meant to use normal images that they want to be indexable and then rankable. However, it will not be possible if you use CSS for adding images because they are treated as background images. And even though there is a URL pointing to the image location, you explicitly tell Google to disregard this image in terms of ranking and in terms of indexing because this image is just a background image which is part of the design. It makes sense.

So if you want the images to be indexable and rankable, use image and then source and then point to the image location. To sum it up, use image sources for indexable images. And if you want to use CSS, use it but for background images only that are only part of the design, and you don't really care for them about bringing traffic to your website.

Okay, and the last one is image lazy loading. It's very important to understand that it's very different how we see the website and how Google sees the website.

So when you go to a website, whether it's desktop or mobile, you see the content above the fold, whether it's images or the copy, and then you need to scroll to see the rest. But when it comes to Google Bots, it's very important to make sure that Google Bots can see all the content on the page right away.

So whether it's the copy or its images, you need to make sure that the whole content is seen so that Google can look at the page and estimate how optimized it is. Otherwise, if you just show some above-the-fold content to Google, that's not going to be enough.

And what's important to really get here is that Google doesn't interact with content, and Google doesn't scroll. So if you rely on Google to interact with your content or scroll, you will be disappointed because it will just not do that. And a good, really good example of this is when placeholder images are indexed instead of the normal images.

Placeholder image is kind of a dummy image that you would use below the fold to make sure that it's really light, so it doesn't impact the loading of the page, or the speed of loading of the page. And then once you scroll as a user, this placeholder image will be switched to the normal image. But guess what? Google doesn't scroll, so in this situation, what you need to do, you need to make sure that all the images are seen by Google.

So even if you're using placeholder images, you always need to have a default image URL that Google can go to, grab the image, index it, and so that it can be crawled. So that should be used here in the URL. So image source and then the URL, the URL of the default image, and the location. And then you can always use source to list the image files for different screen resolutions as well.

To sum it up, don't rely on Google to scroll or interact with your content. And secondly, use the image source and then the default image that Google will see and index, not a placeholder, but a default image.

So as I said, technical SEO is really fascinating. I love it a lot. And with three things that I find really important for technical SEO to be really good in this field.

First of all, you need to know how to find issues like this, for example. You also need to define if this issue is a real issue or if it's some random alert from some SEO tool that you can actually ignore. Third, you need to know how to resolve this issue on this particular website that you are working on, considering the business goals, the tax tech, and the resources that you have. That's it. Thank you.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

Kristina is a technical SEO with over a decade of experience in the industry.

She’s worked on the agency side, in-house and then as a consultant, she helped medium and large businesses build comprehensive technical SEO frameworks to ensure success in attracting valuable organic traffic from search engines.

Now Kristina uses all her hands-on experience to teach people around the world technical SEO using her signature TSP framework through the Tech SEO Pro course.

Her mission is to break down and simplify complex things so SEOs can understand and use them to advance their careers.

How does Google's AI Overview expand user queries? Tom Capper reveals 10 fan-out categories you can use to improve your prompt tracking and keyword research.

In this episode of Whiteboard Friday, Chloe Osunsami provides 3 simple steps for crafting a successful digital PR strategy in 2026. Join her to discover how to analyze competitors, find AI visibility gaps, and secure authoritative brand mentions.

Is your SEO strategy ready for LLM grounding? Explore the distinction between training data and live web retrieval, and discover how to optimize your brand's visibility in AI search results.
