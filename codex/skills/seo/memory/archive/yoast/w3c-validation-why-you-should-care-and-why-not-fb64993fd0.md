---
source: https://yoast.com/w3c-validation-seo/
title: W3C Validation: Why you should care (and why not)
scraped: 2026-03-23
published_on: 2010-06-13
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

# W3C Validation: Why you should care (and why not)

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/w3c-validation-seo/
Published: 2010-06-13
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
It's been discussed many times before: should you W3C validate your site for perfect SEO? It's not that simple, read why here.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

Every once in a while I get an email about W3C validation. The people emailing me either point me at the fact that my own site doesn’t validate correctly (thank Facebook for most of that), or they ask me whether I think W3C Validation is important. Most of them ask even more specifically: whether I think W3C validation is important for SEO.

Since I’ve taken it upon me to create articles for each question that I’ve answered more than once, let’s have a look at the pros and cons of W3C validation.

We’ll have a look at the pros and cons of W3C and web design first, before we dive into the SEO aspects. There are two types of validation errors in my opinion: there are errors that break or hamper rendering, which I’ll refer to as hard validation errors, and there are validation errors that don’t cause rendering issues, which I’ll refer to as soft validation errors.

An example of a hard validation error: an unclosed anchor – <a> – tag. This can cause serious issues. Just about any unclosed element that should be closed and is not can cause you to look at styling issues for far too long. W3C validation is a very easy way to catch coding errors like that and thus it makes debugging and continued development of HTML a lot easier.

Having hundreds of validation errors is not usually a sign of code quality, so trying to keep the number of errors, hard or soft, down is usually a good idea. Whether you really have to bring it down to zero is another discussion, as over obsessing with certain issues can be a costly thing to do. Is your client, or are you, really willing to pay to get the page to validate when all that’s not working is the fact that you use an iframe (something I’d call a soft validation error) when you’re required to use a Strict DTD? Some clients might be willing to pay for that, most I’ve worked with don’t care that much.

I’ve seen people do weird things to get their site to validate. Adding a JavaScript library to your site purely for the goal of getting your site to validate, for instance. Is that really a service to the website’s visitors? Adding 50kb of download for each visitor because you didn’t stand up to your client? I don’t think so.

So, on to the question that’s on a lot of people’s minds. While Googling for this subject I noticed loads of people have written about this topic, which made me decide just my own opinion wouldn’t suffice for this article; so you’ll get mine and the opinion of some of my friends. First of all, let me draw from my own experience.

While doing SEO for a major Dutch news site, I found out this site had its entire front-page show up blank in Google’s cache. The reason was that they were using an unclosed – and rather obscure – HTML tag, the XMP tag. The XMP tag is basically the same as the PRE tag, but instead of rendering tags inside it, it outputs them. This XMP tag wasn’t closed properly, and thus, Google’s spider choked on it, causing their pages not to be indexed the way they should. So this error caused a browser, which is what Googlebot is in essence, not to render. That’s the kind of validation errors I think you should fix. For other validation errors, like the use of target=”_blank” with a Strict document type, I do not care, and would not want my client to spend development time on my behalf fixing it.

I do know that I use the number of errors as a sign of code quality when doing quick scans, and poor code quality can very well be a reason for ranking badly. Do remember though that validating your site with the W3C doesn’t validate the semantics of your HTML.

But as I said: that’s just my simple opinion, let’s get some of my friends opinions:

First of all I asked Aaron Wall, of SEOBook fame, his answer was pretty direct:

“If you want to get links from web designers who charge high rates then W3C validation is important to SEO, otherwise it has little direct importance outside of ensuring proper rendering to end users. When one visits Amazon.com or Google or Yahoo! (or just about any billion Dollar+ internet company) they will find a website that doesn’t validate. Why is that?”

Is Aaron suggesting that validation being good for SEO is a web design industry scam because they need a better reason to get people to pay for writing valid HTML other than “we like it”? Yes, he is.

Next up was Greg Boser, his reply went along the same lines:

“We try to use frameworks that validate, but we don’t spend a ton of time trying to rework a plugin or widget that cause minor errors that aren’t site operation critical.”

Next up, Brent Payne , SEO Director for Tribune, seems to be right in line with my thinking:

“I like to keep errors under 25 or so, though Tribune has 100+ errors. Perfect code, I don’t think is necessary but you don’t want to have too malformed of HTML. Some say it is a ranking factor, I say you just don’t want to have stuff that is too unexpected for the bots.”

Dennis Goedegebuure , Senior Manager & Head of SEO at eBay Inc., said:

“It depends on the type of errors and how many, it all depends on whether the crawler can actually read the real content of the page.”

Lastly, I asked Jaimie Sirovich , the author of two technical SEO books , he said:

“As long as google.com doesn’t validate, I’d say no. They actually don’t quote attributes, I’d guess deliberately to shrink page size.”

(In fact, as Dennis pointed out, Google doesn’t even close the body and html tags). When asked what kind of issues he would fix, Jaimie was very resolute:

In other words: fix unclosed and or improperly nested tags, don’t bother about the rest.

Most SEO’s seem to agree that having code that isn’t properly nested or has big errors is bad for SEO. They all agree too that it’s not going to get you any better rankings when you really have valid HTML.

My final conclusion thus is: both for web design & SEO reasons, you’ll want to fix any and all blatant errors that might cause bad rendering or parser issues. Don’t worry about attributes that are not allowed though, nor about that one plugin using <b> tags instead of <strong> . It’s just not worth your time or money.

Don’t agree with me? Here’s a kicker: even Matt Cutts says there’s no bonus for validating, check out the following video:

Update, March 15th 2011, Matt did another video together with Danny Sullivan of SearchEngineLand:

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

Great article, the proven link between good clean validated coding and the effect on SEO, means i ensure all of my sites are compliant.

Surely it’s just good practice when building a website to ensure that it validates, validation doesn’t just help with search engines but all cross browser compatibility and accessibility.

I totally agree with everything you said above, I spend alot of time explaining to clients that a few minor errors will not affect the SEO of the website, for some reason we find when quoting on websites other web design companies have sold hard to fact they need valid html and avoid other companies that dont offer it, the top ranking website in the UK for ‘Web Design’ have alot of HTML errors which proves the point its not essential to SEO.

Although there are plenty of “hard errors” on the google page, HTML has always allowed you to omit closing tags and attibute quotes in some cases, so those are not necessarily errors.

The bigger message ought to be that you have to remember both human and machine consumers of Web pages, as well as Braille terminals and screen/text readers, and Web clients both current and future.

I think we agree on that one, but stuff like ARIA (mostly known for the aria-required attribute) has never validated, and yet is good for a lot of people. It’s those kind of non validation that I don’t care about. Of course I care about stuff that would break people’s browsers.

Great post! You just took a load of pressure off concerning validation. I have always thought i had to have 0 errors to look competent, but i gave up as it took too much time. I think as far as it doesnt interfere with rendering and user experience then it shouldnt be a bother.

Validation is a mixed bag. With our clients, we stress that the template code should validate. It is a good starting point for most. As for the code on the page, while we agree that there are bad errors and not so bad errors, it often costs more time and effort to have us review the code to determine which error is ok and which is not ok. If we tell clients to always validate code, then we do not have to check everything every time and in the long run it is cheaper. Otherwise you can get into discussions even arguments about what is good HTML and what is not. This is really true when there are multiple development teams working on a site.

Having pages validate has proven to be easier over the years than to evaluate each page on an individual basis as to whether the errors are serious enough to fix or not to fix.

I really think people should stop giving Google such a hard time about it not validating. Although people think it is easy to just give quick fixes that return small size pages and validate, it’s literally impossible to factor in all of the different browsers / devices that Google’s website must see everyday. I know myself that my website doesn’t validate because of Internet Explorer 6.0 and I’m sure that there are other browsers throughout the world that are 10x worse! Validation is important, but I’d rather have my website look normal to a user than to be able to display a W3 Validated badge on my website.

The larger and more frequently updated a site, the less realistic valid markup is. Taking the time to scan the result of a validation is definitely worthwhile to avoid any major issues, as code should be well formed to avoid errors such as ‘lost’ content. However, as per the above we know that many large sites do not validate fully and suffer no apparent ill effect. Weighing the benefit to the business of having well formed code v. the cost to implement it is the method we use to assign priority. This often adds up to a poor investment of time and resources, versus more productive ways of spending your time.

In keeping with the title I do and don’t agree with you – I agree that there are some important parts to validation – like unclosed tags etc that will cause majour issues and some less important ones like for example I remember amazon affiliate links never used to validate – I ended up making php refirects to keep their code off my page.

And it’s very true that validated your site does eliminate alot of cross browser issues and it’s cheaper than paying for a service like browsercam.

However, all of these points are based on practicalities – I’m a strong beleiver in doing things the right way and that’s why w3c is there right? It’s the industry recognised way of doing things: in this sense I think it IS very important for sites to validate – and I think it goes back to the old days of designers writing pure table layouts to get the desired asthetics, whilst sacrificing everything else.

Nice to see a post about something we DON’T have to do! Very refreshing and interesting. Thanks!

Even if validation is SEO hokum (i don’t believe it is), the fact remains that there is no good reason *not* to validate your code. It makes it much more maintainable in the future and bug fixing is infinitely easier.

One major point you forgot to address is browser scripting. Errors on the markup trigger the error correction mode on browsers, which can lead to unwanted DOM quirks. Most of the stuff people keep crying about browser scripting on the Web is closely related to markup issues. If you keep your markup valid, manipulating the DOM shouldn’t be too hard.

Also, once you get acquainted with W3 specs, you get to write valid HTML from starters. So, in the end of the day, you just have to fix minor issues that got by during the development process.

I agree with the points made in this article. Pay attention to validation, but don’t overdo it.
