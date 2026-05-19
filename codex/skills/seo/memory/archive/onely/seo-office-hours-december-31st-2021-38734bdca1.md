---
source: https://www.onely.com/blog/seo-office-hours-december-31st-2021/
title: SEO Office Hours, December 31st, 2021
scraped: 2026-03-23
published_on: 2022-01-04
tags: live_feed, phase1_ingest, onely, publication, technical-seo, javascript-seo, archive_backfill, historical_source
topic: technical_seo
intent: research, monitoring, source_selection, technical_seo
role: researcher, seo, pinchy, developer
confidence: high
canonical: false
canonical_group: Archive backfill - Onely
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# SEO Office Hours, December 31st, 2021

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-december-31st-2021/
Published: 2022-01-04
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on December 31st, 2021.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on December 31st, 2021.

05:21 ” Some of our URLs are indexed properly, but we are unable to find the cache file. What is the issue here?”

According to John, “That can happen. That’s normal in the sense that the cache pages in the search results are handled separately from the indexing. So it can happen that we have a page in our index that we don’t have a cache page for. So if you look for the cache page, it’ll say [for example] 404, but that’s not a sign of a problem. That’s essentially the way that our systems work.”

06:52 “I wonder if a poor translation of a new language version can negatively affect the SEO for a domain’s more established, main language versions. […] Do you consider the language quality of each language version on the same domain independently, or can there be some negative effect if one language version is of poor quality, all the other language versions on the same domain suffer as well?”

John said, “I guess the short answer is yes. The main issue here is less about these being translated versions of the content, but more that, for some things, we look at the quality of the site overall. And […] if you have significant portions that are lower quality, it doesn’t matter so much for us why they would be lower quality, if they’re bad translations, or if they’re terrible content. But if we see that they’re significant parts that are lower quality, then we might think overall, this website is not so fantastic as we thought. And that can have effects in different places across the website.

So in short, I guess if you have a very low-quality translation that’s also indexed and very visible in search, then that can pull down the good quality translation as well or the good quality original content that you also have.”

If you want to make your content available for other languages and countries, check out our SEO international guide.

10:19 “How does Google assess if something is an automated translation or if something is of poor quality? If the entire user interface, for example, is of poor quality, can it be balanced out by SEO text with high quality, things like that?”

John replied: “I don’t know if we have anything that specifically looks for low-quality translations. So at least the way that I understand it, it’s more a matter of us trying to understand the quality of the website overall. And that’s usually not something where they’re individual things that we could point at and say, if you have five misspellings on a page, that’s a sign of low quality. These things happen individually. And all of these factors individually are hard to say that they’re a sign of something being low-quality, but rather we have to take everything together. […]

And that’s also a reason why sometimes when you significantly improve the quality of a website overall or when things get significantly worse, it just takes a lot of time for our systems to figure out overall the view of this website is now better or worse. So from that point of view, it’s not that we have anything specific that we could point at. The best that I could do, if you want individual items, is to look at the blog post we did on core updates […], which has a bunch of different questions in there which you could ask yourself about the website, which you could also go and look at together with some testers or users to get external feedback as well. And it’s not so much that we have algorithms that try to copy that directly, but it’s almost like a guiding direction where we say, well, this is the direction we want to go. And then we will work to make our algorithms try to figure that out.”

19:53 “We have a site where there are 100 pages that […] are tagged with meta robots noindex tag , but they are accessible to the users. There are a lot of good authority sites in the industry that are linking back to these pages. So though we are getting referral traffic […], we aren’t getting anything [from organic traffic] because obviously, they are not indexed. What if we set up 301 redirects for Googlebot on these URLs to some relevant pages? Will that be against Google guidelines?”

John answered, “That seems kind of borderline. It also feels like the kind of thing where you might just use a rel=” canonical” and leave it at that to point at the page that you do want to have indexed. Because if you’re doing this redirect specifically for Googlebot, then I think, on the one hand, from a technical point of view, it’s very easy to get that wrong and to have something messed up. From a user point of view, I don’t think it would be a big issue because we would probably only index the target page anyway. So it’s not that a user would click on a link in the search results and end up on one page that looks very different from what they clicked on. So, on the one hand, I think it feels like there are easier solutions to this with a rel=” canonical” to do essentially the same thing, but I don’t think it would be super problematic. […]

From my point of view, I would prefer to try to use the rel=”canonical” as much as possible to make sure that you don’t have to set up any separate infrastructure to cloak to Googlebot and all of the problems associated with that because it feels like you have to put a lot of work in to make that work the way that you want it. And the other approach is just so much simpler and […] less error-prone.”

Additionally, John confirmed that using 301 redirects in this case “[…] won’t be against Google guidelines. What would be problematic is if this page was indexable and you redirect it depending on the user agent, then that could be seen as a sneaky redirect. But since we’re indexing the target page, then it doesn’t matter what you do on the pages that lead up to that page provided that they’re not indexed.”

23:48 “If a text block is available in source code, but there’s no way to see that content by users. [Can that text get indexed?]”

John answered, “Maybe. If it’s in a normal HTML on the page and it’s just hidden, then it’s possible that we pick that up and use it for indexing. I don’t think it’s a great idea to do it on purpose, but it can happen. And it is something to keep in mind, especially if you’re trying to avoid indexing some specific kind of text. So, for example, one thing that I saw recently is someone had an error message in the part of the page that was hidden. And it was only shown if there was an error on the page, but it was always on the page. And our systems picked that up and thought, well, this page is an error page – we can ignore it.

So from that point of view, […] if you want it indexed, make sure it’s visible and indexable. If you don’t want it indexed, then make sure it’s not indexable and not actually on the page at all.”

35:02 “ I did a website migration to a new domain. […] I had AMP enabled on the old one, and my old AMP articles are always ranked in Google Top Stories. But now my new one is not. I have AMP disabled right now on my new domain because I didn’t like it, and it gives [me] too much trouble. […] But AMP is not needed to include in Top Stories right now. Why my new domain is not ranked in Google Top Stories?”

According to John, “It’s hard to say. I think if you’re doing a domain migration and switching off AMP at the same time, then especially with something like Top Stories, that might be a little bit confusing. But it sounds like otherwise, things are being picked up well. So probably, you’re on the right track there.

The thing with Top Stories, in particular, is it’s an organic search feature. And it’s not something that the site gets because they deserve it, but it’s more that we try to figure out what we should be showing in a Top Stories section. And sometimes that can be more, sometimes that can be less. Sometimes that includes content from individual sites or individual types of articles […]. What I would consider doing here is, on the one hand, giving it a little bit more time.

The other thing is to double-check things around the Page Experience setting, because like we mentioned in the blog post , when we turned that off, we essentially said, pages with a very good Page Experience score can essentially appear in Top Stories as well. So it’s not the case that we would take any page and show it in the Top Stories, but rather we would use the Page Experience score almost as a ranking factor to determine what we would show within the Top Stories section.”

Experiencing issues with your website migration? Have a look at our website migration services and contact us.

42:29 “I am currently improving the website quality after I have multiple pages getting Discovered, [currently] not indexed. I wonder in what timeframe I can expect Google to pick up quality changes.”

John said, “Making bigger quality changes on a website takes quite a bit of time for Google systems to pick that up. So I would assume that this is something more along the lines of several months and not several days. So that’s the timeframe that I would aim for here.

And because it takes such a while to get quality changes picked up, my recommendation would be not to make small changes and wait and see if it’s good enough, but rather make sure that, if you’re making significant quality changes, […] and not that you’re going to have to go back and improve that again. Because […] you don’t want to wait a few months and then decide, oh, I need to change some other pages, too. Make sure that you have everything covered.”

45:09 “I sell handmade shoes. They’re all produced for a specific age range, within the same material, technique, etc. […] Would it be counted as duplicate content by Google if I write one high-quality product description for all? Or is it better to have unique descriptions for each one, which reduces the quality of the content?”

John’s response was: “I don’t know if unique descriptions would reduce the quality of the content. So from that point of view, I would argue that you can have both unique and high-quality descriptions. […]

But the general question with regards to duplicate content is, we would probably see this as duplicate content, but we would not demote a website because of duplicate content. So from a practical point of view, what would happen is, if someone is searching for a piece of text that is within this duplicated description on your pages, then we would recognize that this piece of text is found on a bunch of pages on your website, and we would try to pick maybe one or two pages from your website to show. It’s not that we would demote or penalize your website in any way because it has duplicate content. […] So if someone is searching specifically for that content, it doesn’t make sense for us to show all of those pages. And that’s reasonable when people are searching for a piece of content. They don’t need to find all of the pages within your website that have that piece of content.

The thing to watch out for here is, if you don’t have anything in the textual content at all that covers the visual element of your products, then it makes it very hard for us to show these properly in the search results. So for example, […] if you have blue shoes and red shoes and you never mentioned which color these shoes are in, then if someone is searching for blue shoes, we might think, well, your pages are not that relevant because you don’t mention the word ‘blue’ anywhere on your pages. So that’s the angle I would take here. It’s fine to have parts of the description duplicated, but I would make sure that you at least have something in there that has text about the visual elements that are unique to those individual products that you’re selling.”

Google Search Console notified you about indexing problems due to duplicate content? Read our guides and fix:

48:04 “I have a question about a notification from Search Console. It’s about my author archive pages that are missing a field URL. I would like to noindex my author archive pages. Will it have an impact on my site appearing in search? […] Will my E-A-T score go down if I noindex the author archive pages?”

John replied, “ We don’t have an E-A-T score. So from that point of view, you don’t have to worry about that.

In general, the notification you received in Search Console is probably about structured data that you’re using on these pages. And if you don’t want those pages indexed, then by noindexing those pages, you will remove that notification as well. If you’re using a plugin on your site that generates structured data there, then maybe you can disable it for those author pages, and it’ll be fixed as well. Or maybe you can fix the fields that the structured data provides, and that will also solve the problem.

My guess is that the structured data that you’re using on these pages is not critical for your site, is not something that we would show in the search results directly anyway. So from that point of view, probably you’re fine with either removing the structured data from those pages [or] noindexing those pages if they’re not critical for your site. All of that would be fine.

I would see this slightly differently if I knew that this was a site that focused a lot on the authority, knowledge, and the name of the authors, where if people are actively searching for the name of the author, then your collection of content by that author might be useful to have in the search results. So for those sites, I think it would be useful to keep that indexed. But then you would probably already want to keep that indexed because they’re getting traffic from search. So if you’re not seeing any traffic at all to these author pages and they’re just random people who are writing for your blog, then probably noindexing them would be fine.”

Is your page “ Excluded by noindex tag ” in Google Search Console?

Read my article to make sure that you used the noindex tag on purpose.

Hi! I’m Bartosz, founder and Head of Innovation @ Onely. Thank you for trusting us with your valuable time and I hope that you found the answers to your questions in this blogpost.

In case you are still wondering how to exactly move forward with your organic growth – check out our services page and schedule a free discovery call where we will do all the heavylifting for you.
