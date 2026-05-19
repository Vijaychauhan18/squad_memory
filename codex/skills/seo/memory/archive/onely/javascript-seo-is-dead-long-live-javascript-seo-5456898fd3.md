---
source: https://www.onely.com/blog/javascript-seo-is-dead-long-live-javascript-seo/
title: JavaScript SEO is Dead, Long Live JavaScript SEO
scraped: 2026-03-23
published_on: 2019-09-05
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

# JavaScript SEO is Dead, Long Live JavaScript SEO

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/javascript-seo-is-dead-long-live-javascript-seo/
Published: 2019-09-05
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
Is JavaScript SEO dead? Alive? Resting? JS SEO is the Schrodinger's Cat of the SEO industry. Luckily for Bartosz Goralewicz, he got a hopeful prediction about JS SEO from some surprising sources: Google's Martin Splitt and John Mueller.

## Extracted Body
Is JavaScript SEO dead? The short answer is: no, it’s not. The longer answer is: it’s evolving into something more technical.

Whether or not JavaScript SEO is dead is one of the favorite regular debates at Onely, especially with its CEO Bartosz Goralewicz, who has made a career out of pushing the envelope in the field. In fact, thanks to Bartosz’s work, Onely was one of the first agencies to address the issue of JavaScript in SEO.

Some days the consensus is that the writing is on the wall, some days, it’s merely resting. JavaScript SEO has become the Schrodinger’s Cat of the SEO industry.

Back in June, in Bartosz’s video JavaScript SEO is Dead! Now What? , he said, “JavaScript SEO is dying. It has an expiration date of sorts. I guess we all know that… If Google… starts rendering JavaScript at scale, what’s gonna happen to JavaScript SEO?”

Google’s inability to render JavaScript websites at scale is one of the defining characteristics of the branch of SEO that shares its namesake. If a large e-commerce uses JavaScript to create its dynamic website and the world’s most popular search engine is unable to “see” its content for users to later find it, this creates a very expensive problem for the e-commerce.

In the meantime, Google has to invest a lot of money into rendering JavaScript websites and has created solutions like its two waves of indexing as a workaround until they have the resources to address the issue head-on.

In a Google Webmasters Hangout conversation, Bartosz had with John Mueller (Webmaster Trends Analyst at Google) and Martin Splitt (developer advocate at Google), Splitt noted, “And I wouldn’t say that two waves of indexing are dead, but it’s definitely something that . . . I expect, eventually, rendering, crawling, and indexing will come closer together. We’re not there yet, but I know the teams are looking into it.”

This eventually brought Bartosz to the topic of whether or not JavaScript SEO is dying, and Mueller and Splitt’s answers on the subject were enlightening.

Mueller said, “I would say that we are hoping to make it all a little bit better and so that you don’t have to do more things, but kind of like with normal technical SEO , I don’t see JavaScript SEO dying. Because there [are] just so many things that you can do wrong, and it takes a lot of experience to be able to debug and find out and improve things.”

Splitt added, “JavaScript SEO is not gonna go away. It’s gonna change, right?”

Want to know more about what Bartosz learned in his conversation with J ohn Mueller and Martin Splitt? Then check out “ Is Google’s Two Waves of Indexing Over? ”!

This is the relevant transcript from the Google Webmaster Central Office-hours Hangout , as recorded on August 23, 2019. This hangout was hosted by Googlers John Mueller and Martin Splitt from Google Zürich. Onely’s CEO Bartosz Goralewicz was the invited guest.

Bartosz Goralewicz: Just to finish that. Because I had this concept in my head that JavaScript SEO is dying slowly, it’s gonna eventually dissolve because you guys are getting better with that. So basically, you are on the path of just killing two waves eventually completely, right? Can we –

John Mueller: I would say that we are hoping to make it all a little bit better and so that you don’t have to do more things, but kind of like with normal technical SEO, I don’t see JavaScript SEO dying. Because there is just so many things that you can do wrong, and it takes a lot of experience to be able to debug and find out and improve things –

Martin Splitt: And it keeps changing, right? It’s new stuff coming in. With every new bit on the web platform, you’re like, does this work with Googlebot?

BG: So, this is interesting. Sorry, sorry, I want to follow up on what you said. So you’re saying, even if you guys get so good with JavaScript, obviously basically, resources and, I’m guessing, some kind of technology that you use to optimize that – You still think that JavaScript SEO is gonna be –

BG: In two years or three years, you still think it’s gonna be a thing? Because I had this concept, it’s gonna dissolve.

JM: I mean, it’s gonna be a thing in that, uh, like, we will be better at it, but there’s still, there’s always technical details that you can get working well, or get working kind of –

JM: Like, with JavaScript, like, with normal technical SEO, it’s already hard, and it’s something that a lot of people struggle with, whether it’s, like, the internal linking and you have unique URLs and all of these things.

And, with JavaScript, it’s all hidden away, so you really have to know how JavaScript works, and when something goes wrong, that’s really not gonna be trivial to find. And new frameworks, like new elements in Chrome, all of these things, they kind of come together –

BG: But my logic was that you guys are using the latest version of Chrome –

BG: So with new frameworks, they actually work in the latest version of Chrome, so eventually it’s gonna be one to one…?

MS: It’s a little naive to think that, because the thing is that you’re in the end still not, it’s not that there is a human being sitting in front of it looking at your website going like, “Oh, okay!” It’s a technical infrastructure –

MS: No! I know! There is technical infrastructure, and there are so many interesting implementation details that can interact with the web platform in interesting ways. To give you a very simple example: what we are doing with web components. I’m writing the guidance now, so excuse me if I’m not having like a very polished answer right now, you get the raw answer from me.

MS: Web components work fine in Chrome, we have the latest version of Chrome, Chrome 76, as of today (actually, a couple of days ago) in Googlebot. That’s fine.

The thing there is, we have to make a decision what to index, so as the user, depending – let’s say I go to a website that has a web component, and there’s something in the shadow DOM, then I see the shadow DOM content. [But] if I would run Internet Explorer 10, I see the light DOM content which gets overwritten.

So some people might be like, “Oh yeah, so, if I have a fallback for crawlers that do not understand JavaScript [or] I think I’m gonna be in the first wave of indexing first, I put my fallback content into the light DOM, but then, Googlebot never sees that.

That’s still something that you need to know and be aware of. So you might end up with, like, some person coming to you and going like, “This content is there, it’s in the DOM, we don’t understand why it’s not showing up. And then you have to know, that’s because of JavaScript, specifically because of shadow DOM, the shadow DOM overwrites the light DOM, and the way that the Googlebot works is it flattens the shadow DOM into the [flattened] DOM [tree], overwriting the light DOM in this specific case.

So, to make my point from earlier, JavaScript SEO is not gonna go away. It’s gonna change, right? It has- it used to be –

MS: Today, JavaScript SEO is about finding the pitfalls and the gotchas in today’s technology and, like, working around them or, like, figuring out a better way to do them.

And in the future, it’s gonna be more like, this is what can go wrong. It works out of the box, but these are the things that can still go wrong, and these are the things we need to do to debug them.

BG: So because we got a little bit geeky here, so just to summarize that, (I know you are trying to simplify that), but to simplify that even further, basically what you are saying is like: in the future, JavaScript SEO is gonna evolve into making your job – so, Google’s job – a little bit easier and making sure that everything we push out to clients is basically very easy to crawl, index and understand.

JM: I think that’s one thing, but also all of the troubleshooting stuff kind of comes in that.

That’s something where we can provide some tools to help, but things like shadow DOM and light DOM, it’s like, how are you gonna figure that out unless you already know that this is a thing or things like, you’re using <canvas> to put content out there, and we think, oh, <canvas> is an image, so we index it as an image.

MS: There’s a bunch of consulting. Right now, it’s more figuring out what’s going wrong probably and helping troubleshooting, and it’s gonna turn more into, like, there’s ten ways of doing this in JavaScript, 9 of them are terrible because – it’s like, while developers are trying to figure out the right way –

That’s one of the reasons why I want developers and SEOs to sit at the same freaking table. Because developers are like, “Okay, so this is really hard for us, this is making everything slower,” and they are not necessarily thinking about, “Can Google index this, or can, can search index –

BG: Because I found out that for (I know we have to finish, sorry), I found out that for a while, a lot of developers and SEOs figured, “Okay, JavaScript SEO is just advising developers to prerender.”

JM: I mean, it’s also one of those things, where in the first step, you have to know what the limitations are and when you know the limitations, you can kind of work around them, and if you have a website and you need to get it indexed, like, you can say, well, Google will figure it out in a couple of years. Like, that’s not a good business model. Like, you have to do what you have to do.

BG: I was actually, completely – looking at how quickly you catch up to technologies, how well you are doing compared to, like, experiments from a year ago – I had this vision in my head like, okay, in one or two years –

MS: It warms my heart because you are one of the few people who say we quickly catch up.

BG: Oh, we are gonna publish that quickly, we are gonna publish that soon, because the heavy lifting you did with indexing is tremendous because just two years ago you couldn’t index six pages of JavaScript when a link was nested in JavaScript. So, yeah, sorry, so basically, you’re saying it’s gonna evolve into being much more complex? I actually, sorry, sorry, I got excited! I like that idea.
