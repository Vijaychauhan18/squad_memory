---
source: https://yoast.com/pagination-infinite-scrolling/
title: Pagination or infinite scrolling: which is best for SEO?
scraped: 2026-03-23
published_on: 2016-12-07
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

# Pagination or infinite scrolling: which is best for SEO?

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/pagination-infinite-scrolling/
Published: 2016-12-07
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Why you should be using pagination instead of infinite scroll (and why infinite scroll works better for social websites).

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Something that’s always up for discussion is how to load new content on your archive, category or search results pages. You can do this in a number of ways. You can list a certain amount of posts or products and add a ‘next’ link at the bottom of that list. You can add a ‘load more’ button at the bottom. Or even load more content when scrolling down (infinite scrolling). Or, you might add numeric pagination at the bottom of your page, so users can jump to the next, or last page. In this post, we’ll tell you what works best for SEO.

Google recently announced that it isn’t using rel=next/prev anymore . Our advice hasn’t changed, though. Yoast SEO will still take care of all pagination automatically as other search engines still use it to discover content.

I’m not a huge fan of ‘older’/’next’/’newer’/’previous’ links at the bottom of my page. It leaves me stranded with no idea how long my journey is going to be. It’s unclear and doesn’t trigger me to click. In that case, I’d rather find the site’s search form and look for specific blog posts or products. Although Google is able to follow that link to the next page, it will take a vast amount of time to index all the subpages of archives on larger sites. Our Yoast SEO plugin helps a bit by adding rel=”next” and rel=”prev” to pages like that, but it’s still up to Google to see how many archive links it wants to follow per crawl session. This is, obviously, not my preferred method.

Like with older/newer links, infinite scrolling leaves me wondering how long that scroll will be. And what about mobile websites? It’s probably extra JavaScript that needs to be loaded, which might slow down the site unnecessarily. Although this method was pretty popular for a while, I see fewer sites using infinite scroll (apart from most social network sites). But that might just be me.

One of the SEO downsides is that the content is hidden until scrolling. True, Google seems to index hidden content (although they stated differently back in 2015 ). Still, the general rule of thumb seems to be that content that isn’t hidden holds more SEO value than content that is hidden. Next to that, your infinite scroll is probably triggered by JavaScript. Although Google gets better at indexing all things JavaScript, it still means that user behavior is harder to understand when using JavaScript.

That brings us to UX and conversion. Infinite scrolling gives the user a smooth experience, however, the focus lays less on the individual items. Usually the focus shifts to displaying the most current information at the top of the page, which obviously makes sense for social media, like Twitter or Facebook.

And, since we’re discussing infinite scroll: have you ever tried to reach the footer at instagram.com ? I really wanted to click that API link in the footer the other day. But that’s just another reason I prefer our next option: pagination.

Pagination means spreading the content over a number of pages and linking these. As mentioned above, you could link these pages by adding ‘older’ or ‘previous’ links, but that isn’t the best solution. Linking multiple pages, like Google does, just makes more sense:

This way, you allow Google and your visitors to click on a lot more pages of your archive. A common use of pagination for archives is to use links to the first and last page as well. Besides that, links in the ‘line-up’ can vary like this:

That way, you’re not just sending people to consecutive pages, but also guiding them to others. The benefit of this is that every page in the archive becomes reachable within just two, maybe three clicks. Even with search engines picking up on your XML sitemaps for all the pages, this provides links to a specific page that lead to specific, related pages, which in return could help your SEO.

One extra remark here: even in paginated archives like this, it pays off to add the rel=”prev” and rel=”next” tags to your template, to tell Google how consecutive pages relate in that archive.

Even though Google and other search engines are getting better and better to index your site – no matter what kind of archive or category ‘experience’ you provide your visitor – we’d still like to recommend pagination. Infinite scroll is a great method to use when the focus lays less on the specific items of a page and more on going through the archive. Pagination helps your visitor and Google to ‘jump’ through your archive and find specific items they’re looking for.

Michiel was one of our very first employees and used to be a partner at Yoast. Kick start your site optimization with his articles!

I did change from pagination to inifinite scroll on one of my sites…. and did experience a lot of errors in google search console. However, for mobile viewing it just looked better and easier for people to scroll through the site. Which is fine. Especially if you consider that most are getting there from a keyword search anyway…. so they get the info they searched for. Wanted to test between the two sites which seems to work and look better. Seems that both are ok, iff… you are getting most traffic from organic search. That’s my two cents. (and changing around can be a mission… so rather stick with what you are using before going willy nilly and making changes).

To get rid of the duplicate titles and meta tags problem caused by pagination, add the following code. It worked for my site. I use pagination for pages but not for posts because all of my posts only have a single page. You can check for pages with duplication in Google Search Console (Webmaster Tools) under HTML improvements. Mine all disappeared after I added the code.

Add the following code to the Appearance => Editor => functions.php page:

/** Add Page Number to Title and Meta Description for SEO **/ if ( ! function_exists( ‘multipage_metadesc’ ) ){ function multipage_metadesc( $s ){ global $page; $paged = get_query_var( ‘paged’ ) ? get_query_var( ‘paged’ ) : 1; ! empty ( $page ) && 1 1 && $s .= ‘ – ‘ . sprintf( __( ‘Part %s’ ), $paged ); return $s; } add_filter( ‘wpseo_metadesc’, ‘multipage_metadesc’, 100, 1 ); }

if ( ! function_exists( ‘multipage_title’ ) ){ function multipage_title( $title ){ global $page; $paged = get_query_var( ‘paged’ ) ? get_query_var( ‘paged’ ) : 1; ! empty ( $page ) && 1 1 && $title .= ‘ – ‘ . sprintf( __( ‘Part %s’ ), $paged ); return $title; } add_filter( ‘wpseo_title’, ‘multipage_title’, 100, 1 ); }

Thanks for your addition. I have to add: use at your own risk and don’t use if you don’t know what you are doing . As mentioned, our plugin does something similar. And be aware that Google understands these consecutive pages pretty well these days.

is it true that using pagination in blog posts will add duplicate content ?

Depends. Google is pretty good at recognizing ‘series’ of pages, and sometimes even shows this in the search result pages.

Remember, Google has pagination in search results not infinite scroll…

Thank you for this post. This is a question that’s been going around in my head and I think this is a great answer for SEO. However, my Google Search Console HTML Improvements is reporting each of these pages (/page/2/, /page/3/, /page/4/, etc – I have a lot of them!) as having duplicate meta tags and duplicate title tags which isn’t good for SEO. Is there a way to rectify this?

Hi Sheri and thanks for your question. There are two ways to go about this: 1) Noindex subpages, which is a bit drastic and not really needed anymore and 2) Add the page number to the title and meta description. This is in our plugin, actually: %%page%% . Of course, this just solves the GSC issue, it’s not that you’re making it all so unique. For these archives, depending on how heavily you leverage these, that might just be enough, right?

Yes!!! First am also a visitor to this site. You can cancel that error by using yoast plugin, after enabling the advance mode, I think it’s under titles and meta or just go through the new features the plugin added to your wordpress after enabling the advanced mode. ” you will see where you can set noindex to pages like page 2, page 3, etc so that Google will stop indexing it and saying duplicated title and meta (it is not useful for “it is part of Google pegium bla bla bla), if you are not clear about what I meant, just enable the advanced mode and go through it.

I thing pagination is better to infinite scrolling, because pagination provide users to see easily and he/she can easily jump on specific page. Instead of scrolling and get too bore and loading time, pagination take less time and provide more information.

Hii Michiel, Thanks for this helpful guide. I am new in seo but your guide will absolutely work for me. Thanks.

Infinite scrolling is just irritating. Especially when the scrollbar gets smaller and smaller. But, this website just looks amazing theoutline.com/post/420/welcome-to-the-outline (I noticed that the it is completely a different page after a few scrolls). Any thoughts about that?

That page mimics an infinite scroll, but indeed it just hops from one page to another. While the effect might appeal nice, I personally think it looks a bit unorganized. I think it depends a lot on the type of site/product/brand you have, plus the type of target audience you want to address if you are able to pull something like this off. For most businesses, I wouldn’t go there, tbh.

I agree with pagination being the best, but I’m trying to figure out the best way to implement it. Suggestions?

Oh, and thanks for the article — right on time, as I was just talking yesterday about pagination for a long site page :)

:) No problem, Elizabeth. Have you tried PageNavi ? I think that will help you out.

Hello Michiel, many thanks for your post. I have 1 question :-) In case of pagination, do I need to make the subpages of the archive ( /page/2 …) indexeble through your SEO plugin?

Hi Francesco, there is no need for that anymore . Google is perfectly capable of handling these subpages these days!

I wonder what is your opinion about infinite scrolling with pagination (example here: http://scrollsample.appspot.com/items )?

That might just be the way to do this. A quick check in Google learns that all separate pages are indexed. Nice example, thanks for bringing it to the table!

We care about the protection of your data. Read our privacy policy.
