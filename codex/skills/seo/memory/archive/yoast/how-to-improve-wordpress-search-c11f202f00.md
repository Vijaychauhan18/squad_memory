---
source: https://yoast.com/wordpress-search/
title: How to improve WordPress search
scraped: 2026-03-23
published_on: 2017-09-28
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

# How to improve WordPress search

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-search/
Published: 2017-09-28
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
The default WordPress search engine is rather average, but with a few bits of code, you can improve it a lot. Find out how to improve WordPress search.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

The default WordPress search functionality is certainly lacking in areas. Although changes were made in 2013 to improve it, there are still a few areas where WordPress could use some help. It is, however, relatively easy to improve WordPress search by adding a few pieces of code. Here, I’ll list some of the methods you could use to make WordPress search better.

In older versions of WordPress, search results were sorted by date and not much else. Because this is (at the very least) annoying for websites with a lot of posts, WordPress core introduced a patch that would change the way search results are sorted.

Excerpts in search results by WordPress are not exactly great. Unlike Google, the WordPress search omits emphasis of the keyword if it found matches. Luckily, you can alter parts of the search results and add this feature.

In your theme, look for the file that outputs the search results. In this example, it’s a file that I’ve created manually, called /template-parts/post/content-search.php in a Twenty Seventeen child theme. This file is a copy of content-excerpt.php that exists in the same directory.

Next, look for the file called search.php in the theme’s main directory and look for the following line of code:

By making these changes, you’ll ensure that WordPress will use your custom template instead of the default one. Time to add the actual code that will be doing the emphasizing!

What this function does, is taking the passed content and emphasize every occurrence of the word(s) passed in $search_query and return the text. The class that was added to the <strong> tag can be used to further style the end result (if you want to).

Now that we’ve gone through the steps to setup your custom template parts adding emphasis in the title is relatively easy to do.

Go into your newly created content-search.php and find the line that looks like:

You’d expect that adding emphasis to the excerpt can’t be much harder than adding it to the title. Sadly, this is not the case. With excerpts, WordPress automatically concatenates a “Continue reading” link to the end. You’d be fine as long as the search phrase doesn’t exist in the slug of the post, but most of the time if you’re looking for specific keywords, it will be present in the slug. This results in a broken “Continue reading” link.

To overcome this, you’ll have to temporarily overrule some default WordPress behavior.

The above code will be called to ensure we have a workable “Read more” link.

This part hooks into the function that creates the actual excerpt and adds our emphasis and custom “Read more” link.

Sadly, there’s no elegant alternative for this. Hopefully, someday, a filter will be created that can be called instead of having to overrule large portions of the trim function.

There are a few options to track the search queries that visitors have entered, but we recommend using Google Analytics for this. To get started with tracking searches, please go through the following steps:

If your website is heavily dependent on categories and allows users to use them to refine their searches, Google Analytics gives you the ability to add tracking on this too. For more information on this subject, you can read Google’s documentation on search tracking in this article .

Luckily, there are some alternatives to choose from when you want to improve the search function on your website. As pointed out in the comments, the plugin Relevanssi tackles most issues with the search and helps you get started quickly and easily.

If your website has grown a lot and you want to supercharge your search even more, it might be wise to look at a few, more complex alternatives. One that we use at Yoast is Algolia . This platform contains a ton of features to make search even better. Some features are: Typo-tolerance, support for synonyms, filters, and support for 100+ languages. It also includes integrations with WordPress!

Another alternative is Amazon CloudSearch . It offers similar features to Algolia, and you can enable autoscaling if you think your website needs it. However, ACS does not provide you with an integration out of the box, so you’ll have to write your implementation or look for a WordPress plugin in the Plugin Directory. At the time of writing, there are only two plugins present; CloudSearch and Lift .

As you could read, the WordPress search has improved over the years. Despite this, it still lacks in some aspects. Luckily you can improve it by adding some extra code in your child theme or take it to the next level by using external services such as Algolia and Amazon CloudSearch. Good luck!

Jimmy Comack is Developer Relations Advocate at Yoast by day, gamer and film addict by night. He's a big proponent of open source software and tries to contribute to the OS community when possible.

I’ve been using it for years for some of my money sites. Really happy with the great results. thanks.

Thank you for a good article Really, WordPress is poorly searched It’s better to provide more search options

Thanks for the suggestion for the part in search.php. Just what I needed

Thanks for your great post and thoughts. I do also recommend Relevanssi, great plugin and awesome support. Have been using it for many years and it is a quick way to implement many of these functions.

Thanks for your kind words! For some reason, Relevanssi didn’t show up during my research. I’ll make sure to add it to the Alternatives section.

Thank you for a great post and great suggestions. I’m curious as to why you don’t recommend Google’s internal search. Is that not a good thing anymore?

Google discontinued this feature back in April. Hope this answers your question.

Or, if you don’t like the idea of outsourcing your search for a pricey ongoing monthly premium, and/or you don’t need a huge powerhouse behind your search functionality, there’s Relevanssi plugin. It’s been around for a long time, it has pretty much all of the features you described above (spelling error correction in the premium version), the free version is already excellent, and the premium version is very reasonably priced… https://wordpress.org/plugins/relevanssi/

I’ve been using it for years on any site that requires reasonable search capabilities (yes, native WP search is awful), and I’ve always been happy with the results.

Thanks for your reply. I added it to the top of the Alternatives section.

Great article… but what happens if the Theme is updated? Do these changes then disappear and have to be applied again? Also, is there a working example of what the search is like with these changes applied? Thanks

Hi Phil001, like with any other change you want to do this in a child theme.

I’m going to give this a try. I do have one other question. Is there a way to get WordPress search to query an external website and return results? I have a college catalog that exists in another location and would like to make it searchable using the search on my main website.

Here as Example searching my site for the keyword “yoast”. https://christoph-daum.de/wp-json/wp/v2/posts?search=yoast

A backup is always a good thing especially if you’re a beginner. But if you simply add these lines to a child theme, it isn’t really necessary.

We care about the protection of your data. Read our privacy policy.
