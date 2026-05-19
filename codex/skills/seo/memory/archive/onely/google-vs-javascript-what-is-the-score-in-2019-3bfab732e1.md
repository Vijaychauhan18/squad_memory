---
source: https://www.onely.com/blog/google-vs-javascript-what-is-the-score-in-2019/
title: Google vs. JavaScript: What is the Score in 2019?
scraped: 2026-03-23
published_on: 2019-10-04
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

# Google vs. JavaScript: What is the Score in 2019?

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/google-vs-javascript-what-is-the-score-in-2019/
Published: 2019-10-04
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
JavaScript SEO expert Bartosz Goralewicz presented "Google vs. JavaScript - What's the Score in 2019?" at Web Zürich. You can watch the video, view the deck, and read the transcripts to get the full Onely Experience right here.

## Extracted Body
Here is the transcript of Bartosz Goralewicz’s presentation at Web Zürich on August 23, 2019. The topic was “Google vs. JavaScript: What is the Score in 2019?” and covers a wide variety of JavaScript SEO issues. You can browse the whole deck at the bottom of this page.

Martin Splitt: Word of mouth, ads, okay, that’s two ways of getting people on the website, you can also sit at a computer and just go on your website or something, I don’t know.

Another way is actually search engines. So you wanna make sure that search engines find your content online, and there’s like a whole profession around that, basically SEOs. Search engine optimization experts who are helping you to make that happen. And there’s many experts that are basically looking at the basic things, and also some are really going into lots of details, but there’s a whole category of things that can go wrong if you’re using JavaScript and not that many people are addressing that.

So I’m really, really happy that we have our next speaker here, named Bartosz, who is being – constantly challenging my life, basically. By basically constantly running tests and going like, “Hey! Quick question! Is this expected behavior that we should see from Google search?” And I’m like, “Yes. Can you explain it to me? Oh, wow, OK!”

So he asks me the really, really hard questions, but he’s a really, really good presenter in answering the hard questions.

Bartosz Goralewicz: Thank you so much, Martin, for such a nice intro. So we’re most – usually challenging Martin or John [Mueller], so that’s – most of our job is basically annoying Googlers.

But today I want to talk about how to make your website JavaScript-friendly, SEO-friendly, because I’m not sure if you guys – how many of you work with JavaScript websites? Or just with the – Oh, I didn’t expect almost everyone.

So that’s very nice. So basically what most people don’t know about is that most websites, maybe not most, like why do websites have massive issues with JavaScript? And Google are doing so much better, but they are still struggling with a couple of things.

So they want to talk. I’m gonna have a few slides that I’m gonna – we’re gonna ask Martin to close his eyes. But today when I talk about JavaScript and SEO, we all know that this relationship is very, very complicated.

It’s mostly because JavaScript is very, very dynamic and there are so many different flavors, types of JavaScript, and it’s basically an ever-evolving topic.

And if that wasn’t enough, Google and JavaScript have a very, very, very difficult relationship because Google is, only, or maybe not only, how would you say that? Connected to … connected to Angular, how, like, supporting Angular. So Google is somehow connected to Angular.

Martin (offscreen): We have started the project I believe, and we are maintaining it, but just, just for the record: Angular people are really, really nice people. They come to us and say, “Martin can you help us with this thing?” And I’m like “Nope! There’s the open public forum where you can ask those questions and get the same support.”

Bartosz: So Angular, what’s actually – something that probably Martin wouldn’t say, but Angular was one of the most problematic frameworks.

Bartosz: Which is not something that you would expect and the website Angular.io wasn’t indexed in Google for a few years.

Bartosz: So a lot of people, like, in 2016 – we are a technical SEO agency . I’m sorry, I didn’t introduce myself. But we deal with technical SEO for enterprises and for e-commerce and for large websites, and in 2016 we got kind of sick and tired of all the developers and website owners asking us about very, very specific JavaScript SEO things that no one knew about. So there’s that time recently where all the JavaScript madness began, so everyone started developing JavaScript without fully understanding the technology and, at some point, JavaScript became more important than basically earnings and traffic and, yeah, and websites.

And JavaScript SEO is still completely misunderstood in 2019. A lot of developers or SEOs are trying to do JavaScript SEO but what they do is basically they advise everyone to prerender their content.

So it’s not really high-end technical SEO or JavaScript SEO.

And if you look at websites like Wish.com – one of my favorite websites. If you disable JavaScript, their website disappears, which is fine, but at the same time they are not indexed in Google with most of the products and content. So they’re walking away from quite a lot of income, quite a lot of money, and this is not the only example. We’re time-limited but we have a database of probably like 100 websites, including, like, Aliexpress, EA games, and all the big brands that lose massive traffic, and I’m not talking like 10-20% but sometimes like 80% because of how they handle JavaScript.

If you look at Wish.com and their visibility chart, you can see that this relationship is not going well.

This is like an equivalent of a couple that’s having a very rough time. They get together and then it’s happening again. So this is more or less what’s happening with quite a lot of big brands and JavaScript SEO. And there is a massive cost of JavaScript, a massive cost that somehow is overlooked.

Just to show you an example, let’s have a look at the video of CNN being opened on iPhone X and Motorola G4, just to show you how resource-heavy JavaScript can be. So I’m not gonna play the full thing because the Motorola G4 crashed halfway through, but if you look at the iPhone X, it loaded CNN, but Motorola is still struggling to even send the request, so this is a problem that we have to face.

And this is the data from Germany, and if you look at Switzerland it’s actually very, very surprising because if you look, again, Germany 23% for Google.de comes from desktop. So just 20% of traffic comes from desktop devices right now. In Switzerland this is shockingly – you guys still have quite a lot of desktop traffic which I totally don’t understand.

Like, in Europe you’re, like, actually one of the exceptions. But most countries, you guys, are not – most countries actually don’t have that much desktop traffic any more.

Let’s move back in time to 2015 and look at some of the data. So Hulu.com was one of the websites that actually inspired us to dive deeper into this topic. So Hulu.com if you – do you know Hulu.com? They’re the biggest competitors of Netflix and we will see in a minute why there are not doing that well recently. So there – they actually jumped onto the JavaScript hype train in 2015-ish and they figured, okay, they were very curious about that but they couldn’t figure this out.

They didn’t ask themselves one of the most important questions: is, like, can this backfire somehow? Can launching a JavaScript SEO website just – sorry, JavaScript website without full knowledge of JavaScript SEO, is a good idea?

This is – this is how their traffic looked after that. They’ve lost overnight – they lost more than 40%, then within the next upcoming weeks, they’ve lost all together around 70% of the traffic. It goes so bad that you couldn’t find any of the Hulu shows in Google and they were only available at Hulu.com. So if you want to watch any show from Hulu.com the only website that would show up in Google were torrents.

This is how bad it looks like and it’s still not fully fixed until today. But let’s move forward.

So what exactly went wrong? There was no data at that time and we figured, okay, if there is no data then we need to get it somehow. I need to figure we’re gonna create a dream team to basically build an experiment.

And it was the first JavaScriptSEO experiment in the history of the internet. We chose this very cool, very cool name. So it was JSSEO.expert.

The idea was extremely, extremely geeky. A simple query – they were very, very simple. We basically built a website where every single subpage is a different framework. So we would see, OK, how is Google, and other search engines we’re gonna talk about that in a second, how are they dealing with indexing all the different frameworks?

So basically if you go to JSSEO.expert and /vue, you’ll see content generated by Vue. It couldn’t get any simpler. At the very beginning we only had “Hello world!” in, like, within a few days we just – we’ve found a way to generate quite a lot of content through machine learning. But we basically went with Hello World and that wasn’t available in all of the framework, and some of it was, but basically just to give you a short example of how it worked like: if you use, switch off the JavaScript. It disappears. Very simple.

So if we see that Google indexed the content within the red frame, we know that Google parsed that JavaScript framework, the JavaScript code. The idea was extremely, extremely simple, but the results were really, really mind-blowing.

If you look at that Google did pretty well with most of the frameworks, it actually struggled a little bit with Angular – it struggled with AngularJS because it turned out it wasn’t Google’s fault. It was Google’s AngularJS’s fault because they had a problem with their own library. But it got quite interesting because it turned out that Google didn’t crawl the code that was placed externally, but they crawled the content that was based – if the JavaScript code was in line it was working fine.

And we found quite a lot of different anomalies. We played with the data and we basically found a video from 2015 from Jeff Whelpley, who’s somehow involved in the Angular project, saying that if you care about SEO, you still need to have server-rendered content. And this got us thinking how our other sections was dealing with that. And if you look at that, only Google and Ask. Ask is not saying that publicly, but Ask is using Google’s servers and basically database, so Ask is just simply Google. It’s not publicly announced but we fight with that, and it is.

So only Google is able to crawl any JavaScript as of 2017. It changed a little bit. I was talking to the guys who were, like, involved in that project within the Bing – JavaScript project for a while but they are doing something with JavaScript now – is still not even close to the work that was in 2002, but this still wasn’t the main problem. Because we figured, OK, Google can index some of the content, is tricky, but it wasn’t the main problem. We couldn’t find any JavaScript website that ranks until 2018.

And I reached out to John Mueller – good questions – and John Mueller, at that time, unfortunately, couldn’t help us for reasons we can only speculate about. What I’m guessing, they basically didn’t communicate their problems of JavaScript or, I don’t know, but John Mueller couldn’t really help us with our questions. So we figured that we’re going to build more experiments.

Before I move forward with that, I’m guessing you’re pretty technical so I’m not sure this slide is important, but just for those of you who aren’t: HTML is just like a ready-to-go cake, so all the bots, all the users, just basically get the content they seek.

With JavaScript, it’s a little bit more complex, you get all the pieces that you should render – or in this scenario – bake together to get the final four things. It’s very, very, very expensive. So looking at that, some frameworks are indexable, but there is a very, very fine print.

It seems that Google is not really, really fond of JavaScript but at the same time, they are very, very interested in HTML. And if you wanna . . . meme, basically, we saw that every single HTML website is indexed within minutes, with JavaScript it’s not that easy.

And I’m guessing you already know where I’m going with that. But we’re going to build one more experiment. And we’ve created the simplest possible experiment we could think of. We created a very simple JavaScript and HTML website – they’re both identical – but you can only get to page number 3 from page number two and so on.

So basically, if Google would index the page number six we knew we knew that they basically went through every single one of them. With HTML, Google will index them within minutes. With JavaScript, from the home page to page number one and it completely died. And it’s not even – I’m not even talking about hours or days but Google didn’t index any JavaScript within that page for six months.

Basically, everything after – after the first sub-page was invisible. And we’ve been repeating this experiment actually until today. There is a few things that has changed, I’m gonna talk about that but around 2017 and the results are always the same. Google would never crawl JavaScript deeper than the homepage and the first linked page.

We came to the conclusion that JavaScript, even if indexable when you force Google to do that, is gonna kill your crawler budget completely.

After roughly a year, John Mueller admitted that crawling and indexing is slower for JavaScript than static HTML.

We’ve been actually waiting for that for – for two years, from like – the main problem we had is that developers didn’t really believe us, even though we had experiments – because we are the only ones talking about that. So this I don’t even remember that was a tweet or a hangout, this sentence from John Mueller is something we almost tattooed on our foreheads for over a year because we finally had something to talk about with developers. And his advice helped in general, so he’s – his help was really appreciated.

And I know it works both ways, I know that Google actually used that experiment as well. So after failing at the beginning with John Mueller, I reached out to most, like, like, we actually reached out to, like, 20 different Googlers, but Ilya Grigorik was the one who responded. A lot of them were emails, tweets and whatever. And we invited Ilya Grigorik to our Google Doc with every single thing we found out and he started commenting, commenting like crazy for a day, and then he disappeared.

But he said that JavaScript SEO – JavaScript is not bad for SEO if done right, and he mentioned that there is a cost coming from basically rendering that at the Google side. So if you look at JavaScript – JavaScript if it’s not done right, which is a very broad statement. It’s very expensive to run and that’s something we actually confirmed. So even if we put any, like, random number you can see that HTML is really cheap, like, let’s say a page in HTML cost $1, for JavaScript it’s gonna be, let’s say, $100.

Bartosz: Yeah, so fast forward to 2018, and one more thing from Google that we really, really enjoyed is that John Mueller had this Google i/o talk . . . and they mentioned finally that Google is indexing JavaScript with two waves. So the first wave is basically they only look at HTML and the second wave is when the resources are available – is indexing HTML. Sorry, JavaScript. Yeah, and this actually got a little bit tricky because JavaScript and the second wave can take up to – they’ll – like Googlers said up to two weeks.
