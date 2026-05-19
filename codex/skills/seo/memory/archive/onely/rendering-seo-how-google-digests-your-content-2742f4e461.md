---
source: https://www.onely.com/blog/rendering-seo-how-google-digest-your-content/
title: Rendering SEO: How Google Digests Your Content
scraped: 2026-03-23
published_on: 2021-10-06
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

# Rendering SEO: How Google Digests Your Content

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/rendering-seo-how-google-digest-your-content/
Published: 2021-10-06
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Read the newest posts on our blog to make sure you're not missing out on anything!

## Extracted Body
This is a transcript of a conversation between Bartosz Góralewicz, Martin Splitt from Google, and Jason Barnard. They hosted a webinar to discuss Rendering SEO in practical terms. You can watch the webinar recording here , but since it’s packed with so much information, we hope you’ll also find this transcript to be helpful!

Bartosz: Today, we’re gonna look at rendering from Google’s perspective, which is a little different from what we’re seeing in Chrome, and hence Martin is here to navigate us through those murky waters.

And just briefly, in our research, and again, this is not coming from Martin, we started seeing first mentions of rendering and layout in Google patents around 2011. And my personal theory is that’s why Google Panda content quality updates and all those wonderful things started to happen around that date.

And there are a lot of new findings, this is a fairly new field of how Google looks at both layout and rendering, and this is something we hope to make a little bit more friendly here with Martin. So this is the goal today – to make this as simple and usable, and practical as possible.

As I mentioned, most of the Google patents that we got to around this topic, and that’s how this actually started, they focus on layout.

The layout seems to be quite important, and we probably know that, like, text appearing above the fold is more important, and there are a lot of patents that will tell you that some elements of the page have a little different role than, e.g., ads or text that’s below the fold.

So this is one, and for years we were focusing on JavaScript SEO as Jason mentioned, and when going deeper, we realized JavaScript SEO was mostly, “can Google see your content properly, can you change that JavaScript to HTML” and things like that, but when we dove a little bit deeper we saw that this is just the tip of the iceberg.

A lot of the aspects of how Google renders the content and how they see the layout is gonna affect most of the SEO that’s happening after this initial phase of crawling, rendering, and indexing.

So we as an agency left the field of JavaScript SEO a little bit, and we dove into Rendering SEO which is way more complex, way more exciting. Even though, we are going to try and keep it simple today. Jason, you have to be the guard of that.

There are a lot of things that are quite exciting, we probably won’t get precise answers from Martin, he hates this slide, I’m sorry, Martin.

There are things Google mentioned like they will interrupt scripts, a lot of funky little bits and pieces that are interesting, but just to tell you for all the people who are not as advanced in technical SEO – why layout and rendering SEO matters. Sometimes Google won’t pick up the whole page you posted.

So if you’re seeing your URL is indexed it doesn’t really mean that Google indexed the whole thing. This could be due to rendering, quality, technology so that’s where it gets quite colorful and exciting.

Something I wanna mention when we talk today is that there are four shades of your website. Without knowing, a lot of us cloak the content, because your content now looks different on mobile with JavaScript and without JavaScript, and this goes for most websites nowadays, so it’s not only those React- or Angular-powered websites, it’s also about WordPress, Wix, maybe Duda as well, and most of those simpler frameworks. We also have the same problem with desktop. So there are so many different ways you can interact with content, and it’s mostly because of rendering, how this code is gonna be rendered on an end device.

Without further ado, let’s begin. We have Martin here so I won’t take too much of your time.

I have the first question just to start it up somehow. So Martin, can rendering SEO help me rank better? I’m assuming this is the first question that’s in everyone’s head.

Is it practical, is it something that will get us traffic, leads, all those funny and cool things?

Martin: I mean, I usually don’t answer ranking questions, I’ll make an exception here.

Generally speaking – no. But specifically speaking, if there is a problem where something breaks your render and the content doesn’t show up then Googlebot does not see the content or does not see it properly, then, you know, that may actually hurt you in the sense of, we don’t see the content.

So we might not index the page. Or we might index the page but not rank it for the content that you care about. So yes, in the end, it can make a difference and have an impact – yeah, of course.

Rendering issues on your website may contribute to your URLs getting indexed without content.

Read the article on how to fix the “Page indexed without content” status in your Google Search Console.

Bartosz: One thing I want to do before we dive into the questions from the audience is, w here does rendering sit in the whole scenario?

We can quickly get into a scenario of what was first, the chicken or the egg, but my understanding of that was always that Google creates a queue and then crawls, renders, and obviously optionally indexes the page – would that be oversimplification?

Martin: That is slightly oversimplifying but is fundamentally true. So we get lots of URLs and we get so many URLs that we can’t crawl them all at the same time for the obvious reasons. Ok, I shouldn’t say for the obvious reasons. We can’t crawl all the URLs all the time, at the same time for reasons of bandwidth, so there’s only so much internet bandwidth that we can use.

If you have an online shop, and you come online tomorrow with a new online shop website and you have a million product URLs, your server might crash if we crawl all these URLs at the same time, so we have to spread this out through time, so there’s a queue in between us discovering the URL and the URL actually being crawled.

This queue is relatively transparent in the sense that the Search Console shows you when the URL has been last crawled and also it’s transparent in a way that your server tells you. You can check when was the last request done to this URL from a Googlebot User-agent and IP, so that’s a very transparent queue.

What happens then is once we have it crawled, we can look into the HTML that we received, we can look into the HTTP status. If it’s a 404 status then pretty much the processing ends here. If there’s a robots meta tag that says noindex then our work ends here as well.

But if we get a bunch of HTML content and we can go forward with processing it and the rest of the pipeline, we also then queue the page for JavaScript execution, which it’s what we would call “rendering.” The second queue is very opaque, in a sense you don’t really see how long it takes us to render, if we render at all, when we render, you don’t know, and that’s not accidentally so, because theoretically, we see this all as a transactional process, in the intake, there’s the URL that we discovered and the output of that is indexed document or non-indexed document. That’s pretty much what can happen here.

And there is not that much that you can do about rendering really in terms of changing the queue position or doing much in terms of figuring out what is rendered or what should be rendered. You see that in the Search Console as well, you see what comes out of rendering if you look at View Crawled Page , you’ll see what we would see there. So there isn’t an additional queue that you skipped over, and there are a few more complications where the simplified model might not necessarily apply. But you can assume the flow normally is discovering, crawling, queuing, rendering, indexing, and then potentially ranking later.

Bartosz: Just want to clarify one thing because you mentioned that, before this gets into a topic online, you mentioned that you render the page and you mentioned JavaScript as well, but what I got from our previous conversations is that rendering is not only about JavaScript.

Bartosz : So even if you’ve got a non-Javascript website, like there is no line of JavaScript and no referral to external scripts, you should also be concerned with rendering.

Jason: I was about to ask the question: H ow many of us are actually concerned by rendering because that conception, the idea that it’s JavaScript only, we’re all concerned…?

Martin : Yeah. All of the websites are being rendered and all of you are to some degree concerned, yes, that’s true, that’s correct.

Jason : Basically, if you don’t have any JavaScript, do you have to worry about this at all?

Martin : You don’t necessarily have to worry about it, but you’re still affected by it. There are still potential implications from rendering.

Martin : That ties back to what Bartosz said earlier, like the text above the fold or where does Google think your main content is and stuff like that.

Jason : Right, yeah. Which is brilliant. I mean, it basically says, a part of rendering is basically understanding what role each chunk of the page plays. Bartosz showed us a screenshot where some of it was not indexed, some of it was ads, some of it was a header, some of it was the footer. Rendering is the point in which Google decides what role each part of the page plays, therefore it can make this decision on whether to index it and whether or not to prioritize it, in terms of what Bartosz was saying – is this the main content?

Martin : So maybe we need to talk a little bit about what rendering really is? Because I’m not sure if everybody knows what that means, right? Should we do that?

Bartosz : Sorry, Martin, this is a very good moment for all the people watching to ask all of the questions about every single item you didn’t understand right now.

Bartosz : We have no idea with Martin at which point we’re going to lose the audience, but what we are trying to address to be fully transparent, the feedback from our previous conversation was that sometimes we got a little too geeky, too nerdy, so we want to really make this simple.

Jason : Brilliantly said. Define rendering, what is it, what’s the process?

Martin : Right. If you think about HTML as a recipe and you have all the ingredients there, you have a bunch of text, images, stuff. But you don’t really have it in the recipe, the recipe is a piece of paper with all the instructions on how to make the thing.

The resources of the website are the ingredients, such as the CSS, JavaScript files, and the images the videos, all of that stuff that you load to actually make the page look the way it looks afterward.

The website you know and use in your browser you see in your browser – that’s the final dish.

Rendering is pretty much the cooking, the preparation process.

Crawling fundamentally just goes into a big book of recipes and takes out a page with the recipe and then puts that into our realm reach, basically we are standing here on a kitchen table and we just wait for the cooking to begin, and crawling will basically hand us the recipe.

And then rendering is the process where rendering goes, “AHA, interesting! Crawler, over there, can you get me these 10 ingredients?”, and the crawler conveniently goes, “yes I got you these 10 ingredients that you need”, and we start cooking, that’s what rendering is.

So rendering parses the HTML. HTML fundamentally when it comes form crawling is just a bunch of text, conveniently formatted, but text.
