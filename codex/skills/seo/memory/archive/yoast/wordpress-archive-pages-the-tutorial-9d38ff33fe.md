---
source: https://yoast.com/wordpress-archive-pages/
title: WordPress archive pages: the tutorial
scraped: 2026-03-23
published_on: 2017-03-03
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

# WordPress archive pages: the tutorial

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/wordpress-archive-pages/
Published: 2017-03-03
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
WordPress supports archive pages. Learn how you can use these archive pages better and ensure they add value to your blog with this tutorial.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Once your website starts growing and you continue writing blog posts, you’ll eventually end up with archive pages. These archive pages can be based on taxonomies, categories, custom post types and even dates. WordPress has built-in support for these archive pages, however there are some small drawbacks. In this post, I’ll explain to you how you can use these archive pages in a better way and ensure they actually add value to your blog.

WordPress supports automatic creation of archive pages. This ensures that you don’t have to think about making them by hand. Sadly, these pages tend to only consist of a list of posts based on a category / taxonomy / post type without any further introduction. This means that your visitors are left stranded on a page without much explanation about what they’re looking at. The chances of your visitors finding what it is they’re looking for are terribly slim in this case and usually visitors will decide to leave that page immediately.

A simple solution to this problem: Add an “introduction” of some sorts to the page. A clear header can already greatly help out your visitors, but for extra important pages we recommend adding a description as well to better highlight the content that can be found on that archive page.

Before avidly writing these introductions, lets ensure they are properly displayed on the pages.

If you want to add an introduction to a category, tag or custom taxonomy archive, you can easily create a custom template file to override the default ones. For example, you can create a category.php file in your theme to override the default template file. If you want more information on how the templating hierarchy works in WordPress, just look at this infographic before continuing.

In your newly created category.php template file, add the following snippet above the WordPress loop:

The above code takes the title and description that you added in the WordPress backend for the category and displays it on the category archive page. This method also applies to tag and custom taxonomy archives.

If you use the Genesis theme, you won’t have to do any of the above alterations. Luckily, Genesis already has built-in support for this type of thing. In the latest versions of Genesis, all you need to do is edit your desired category or term and scroll down until you see the Category Archive Settings.

Here you can add a title and description which will automatically be displayed on archive pages.

Or if that doesn’t work, you can just add this to your Genesis child theme’s functions.php:

Of course, you are free to expand the above function to add some more CSS classes to further style the output.

Altering custom post type archives is a bit trickier than overriding default tags, categories and taxonomies. You can add a new file called archive-{posttype}.php where you replace the {posttype} portion with the name of your custom post type. By then adding the following code to said file, you can achieve a similar result:

Now for the hard part. Because custom post types don’t have any type of form in the WordPress backend, it’s impossible to easily add a description to these custom types nor is there a recommended way of storing the data. One method you can use when you use a child theme in Genesis, is by expanding the functions.php file with the following code:

As you may have noticed, the code example uses two custom genesis options: $post_type . '-title' and $post_type . '-intro' . These can be defined in your Genesis child theme. You can read how to do that over here .

To avoid duplicate content issues, the previous code snippets make use of a simple check to ensure we’re not on a paginated page. The is_paged() function call determines whether or not we’re on a paginated page. If it detects the query variable paged , we can assume that this page is one in a series of multiple pages and thus should not display the description.

Since the introduction of rel=”next” and rel=”previous” , websites that have paginated archives and who have properly implemented the rel="next" and rel="previous" attributes, will be receiving more visitors on the first page in the series. Nevertheless, you should not solely rely on this, but use it in conjunction with the is_paged() option.

To ensure that people actually read the introduction text, it’s very important to add proper styling to the page. After all, these introductions need to be made with humans in mind first, SEO second. Don’t fall into the trap of styling it the same way as your posts as this might result in visitors not understanding that the text is actually something entirely different from your content. A good example can be seen in the following screenshot:

Based on the information shared in this post, you should be able to make clear archive pages that help your visitors understand the content they are looking at. Additionally, you should be able to create these archive pages for custom post types. We look forward to seeing some of your beautifully styled archive pages.

Jimmy Comack is Developer Relations Advocate at Yoast by day, gamer and film addict by night. He's a big proponent of open source software and tries to contribute to the OS community when possible.

is_paged() is a core function which will return true if the page being displayed is “paged” and the current page number is greater than one.

Can you point us to some example code for styling the text with the box surround – similar to your example above?

Very interesting workaround to make archive pages readable. I will definitely give it a try in one of my websites. Thanks a lot for the post.

Hi I am running Genesis and don’t see that option in my Theme settings?

Running the current Genesis framework here, too, and no sign of those options anywhere. Would love to know before I add more code. Anyone?

I had to get my hands on a copy of Genesis first, hence the late reply. Sorry about that! It looks like they changed some things around and the Archive options have been moved to the Category and Tag edit screens. I updated the text and screenshot according to this new method. Hope it helps!

hi a number of outstanding providers of webmaster services and products. Please take some time to visit

We care about the protection of your data. Read our privacy policy.
