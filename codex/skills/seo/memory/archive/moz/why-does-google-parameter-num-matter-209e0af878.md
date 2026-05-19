---
source: https://moz.com/blog/why-does-google-parameter-num-matter-whiteboard-friday
title: Why Does Google Parameter &num= Matter?
scraped: 2026-03-22
published_on: 2025-11-21
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

# Why Does Google Parameter &num= Matter?

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/why-does-google-parameter-num-matter-whiteboard-friday
Published: 2025-11-21
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
The &num=100 search parameter was recently deprecated. This seemingly small change in a Google search URL parameter is having a massive impact on the SEO industry. In this Whiteboard Friday, Tom Capper explains why the &num=100 parameter was so useful, why Google might have deprecated it, and what…

## Extracted Body
Watch this Whiteboard Friday, as Tom Capper explores the &num=100 parameter and why its depreciation was so impactful.

The &num=100 search parameter was recently deprecated. This seemingly small change in a Google search URL parameter is having a massive impact on the SEO industry. In this Whiteboard Friday Tom Capper explains why the &num=100 parameter was so useful, why Google might have deprecated it, and what tools are doing to work around the problem.

Click on the whiteboard image above to open a high-resolution version!

Happy Friday, Moz fans. Today I want to talk to you about something that you might have seen already if you've been following SEO news or indeed the Moz blog or alerts in some of the tools you used in the last couple of months, and that is something called the &num= or sometimes people just say &num=100 parameter .

So I want to explain in this Whiteboard Friday what this is, why it matters, and what some of the ways forward are that tools are looking at.

So what is this? So the way that rank trackers and other SEO tools, as well, actually work is by scraping Google search results.

So they scrape Google search results not by interacting with the search bar, like you as a user would, but by typing in manually the sort of URL that you would see after using the search bar. So you can see this yourself. If you go and Google something, you'll see in the URL bar at the top, there's a bunch of information in the URL, and these URLs can be more or less manually constructed.

There are a lot of caveats here, a lot of detail that I won't go into. But for example, you could try this yourself, if you were to type in google.com/search?q=moz+blog, so that means Moz space blog, so I'm just searching for the Moz blog, &HL=EN, we're doing this in English, &GL=GB, we're doing this in the UK, you could put various other parameters , there are loads, for example geo-coordinates, personalization, we're not getting into that, &num=100. That last one means I want 100 results.

Now there are a lot of caveats even there. What that actually means is 10 paginated pages of results, where you would expect to see 10 traditional organic results per page. These days, actually, a page of search results might commonly contain in the order of 15 results because, as well as those 10 traditional organic, you'll have various types of features that people can rank in, not even to get into ads and all that kind of thing.

So to call it 100 results is oversimplistic. But that's what happens in the parameter. If you put in 100, you get 10 pages of results, all as one big results page. And then that allows SEO tools to get more data from just making one of these queries.

Why not make 10 individual queries, 10 results at a time? Wouldn't that be just as good?

Well, not quite. Some of the main costs of doing this kind of scraping scale with the numbers of scrapes that you make. So the big one is proxies. Google will typically and if you try this yourself a few times, you will probably find that your browser will be blocked, or there'll be a CAPTCHA for a little while before you're able to do it again.

And that's the same problem that is encountered by SEO tools. So they have to maintain a very large quantity. We have to maintain a very large quantity of IP addresses in order to get around this, and that comes with a significant cost.

If you're making more queries to do them 10 results at a time or something like that, then you need even more IP addresses. The cost scales probably more than linearly.

The other thing you need is JavaScript and cookies. It used to be the case that you could do this as a sort of dumb, headless request, whatever you want to call it, and you would get something representative. In the last few years, that's not been the case. You have to quite convincingly mimic a browser in order to get rankings that represent what users actually see, especially in things like AI Overviews .

Again, there are caveats here that I'm not going to get into. You don't have to fully mimic a browser, but you have to get quite close. So again, this comes with cost, with overheads, with processing costs.

And then there's the parsing at the end, where we actually extract from the HTML that we receive. We extract, okay, so what are the rankings, what are the features, telling them apart, processing that data, calculating pixel heights, all this kind of thing. That, again, comes with a cost that scales.

So what happened was in the case of ourselves and other SEO tools, in mid-September, Google started deprecating this parameter. They started deprecating num=100. So if you used that parameter, it would be ignored, and you would just get the first 10 results. You would just get the first page.

Now, actually, this hadn't been officially supported for a long time. We could speculate about why it stopped working. Maybe it was by accident. Maybe it was on purpose. We don't really know. But one way or another, it gradually stopped working.

Now, in the case of Moz and STAT, we already had a solution in place that we had tested previously to see if it produced more accurate results, which we call stitching internally, which is what I have just been alluding to where you would get the first page of results and then the second. And again, there's a parameter that would allow you to get results from 11 to 20, for example, when you're constructing this URL. So you can get all of these one at a time.

Of course, the cost goes up very significantly when we do this. And then you can also get some issues around the stitch, where we have to be careful in terms of how we do this and how we analyze it afterwards. So you can imagine that if your site was fluctuating between positions 10 and 11, then depending on the timing, maybe you're in position 11 when we called the first page, you're in position 10 when we called the second page, and then you don't appear at all in what we get. That would be a problem.

So this is the kind of thing we have to be aware of. It's even more problematic than it initially seems. So this is the working solution that we had. I think there are some other tools that did okay as well. We had no loss of data. As this problem rolled out, we were able to roll in this kind of solution.

So why does it matter? What does this actually affect? So the most obvious thing is rank tracking. Like you might be interested in your rank tracking. You're probably primarily interested in higher ranking results, the first 2 pages, 20 traditional results, and maybe 25 to 30 total results. You're probably most interested in those top ones. But you might have reasons to be interested further down as well. That's fair enough.

Keyword research, again, if you want to get a list of every keyword that your site ranks for or is relevant for or your competitor is, then you might want deeper rankings.

And also the link index. So our link index and others, one of the big inputs of our link index is URLs that we find on Google search results.

And again, getting more links from Google search results means we get more input into our index. So we have to balance. We want to maintain quality in all of these things, and we have to balance that against the increased cost, which obviously we don't want to pass on to customers.

For rankings, it's flexible. In Moz Pro, you get the first two pages of results. But if you're using STAT, which is our sort of enterprise rank tracking tool, then it's flexible, where we are allowing customers up to 100, and that's something that we go through on a case-by-case basis.

But then for our analysis features, so things like Keyword Explorer and Link Explorer , we're offering 50. So this is basically the same as we were using before in those features, and that's because in these parts of the tool, which is basically this stuff, we think those deeper rankings are particularly important if you want to look at cannibalization or that kind of thing.

So yeah, basically, I would advise you to go and have a look at what your tool is doing.

Hopefully, your tools are Moz and STAT, so I just told you. But go and have a look at what your tool is doing, so you can have some kind of understanding of how this works behind the scenes, and hopefully not, but whether perhaps there might be a cost implication for you in the future.

Something I'd also recommend you go away and do is actually have a play around with this. I think you can learn a lot about how these tools work and get some context by going and playing with some of this in practice and paying attention to the URL when you do make these Google searches.

That's all I have time for today. But thank you very much. I hope you found this interesting.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

I head up the Search Science team at Moz, working on Moz's next generation of tools, insights, and products.

How does Google's AI Overview expand user queries? Tom Capper reveals 10 fan-out categories you can use to improve your prompt tracking and keyword research.

In this episode of Whiteboard Friday, Chloe Osunsami provides 3 simple steps for crafting a successful digital PR strategy in 2026. Join her to discover how to analyze competitors, find AI visibility gaps, and secure authoritative brand mentions.

Is your SEO strategy ready for LLM grounding? Explore the distinction between training data and live web retrieval, and discover how to optimize your brand's visibility in AI search results.
