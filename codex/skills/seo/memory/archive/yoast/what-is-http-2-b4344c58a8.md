---
source: https://yoast.com/what-is-http2/
title: What is HTTP/2?
scraped: 2026-03-23
published_on: 2018-04-19
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

# What is HTTP/2?

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/what-is-http2/
Published: 2018-04-19
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
Site speed is crucial. There are several ways to improve how fast your site loads. One of them is moving to the newish HTTP/2 protocol. This makes sure that your connection gets a nice speed boost. Find out what HTTP/2 is and how it can help you!

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

HTTP/2 is a newish protocol for transporting data that will drastically speed up the web and can help your SEO. The ‘old’ HTTP1.1 protocol only allows web servers to send files down a single line one at a time, and that line has to open and close after each file has been sent – a process that can take ages. HTTP/2 offers a dramatic speed boost as the line can be kept open and a lot of stuff can be sent at once. This post covers how HTTP/2 works, why it’s good for your SEO and how to implement it on your website.

HTTP/2 uses new technologies to take away one of the web’s biggest bottlenecks by introducing full multiplexing connections. Servers can now open a single connection with a browser and keep sending all a website’s files until everything is done. After that, the connection closes and the browser can render the site.

Whenever you click on a link to visit a site a request is made to the server. The server answers with a status message (header) and a file list for that website. After viewing that list, the browser asks for the files one at a time. The difference between HTTP 1.1 and HTTP/2 lies in what happens next.

Say you want a new LEGO set. First, you go to the store to buy your LEGO. When you get home, you open the box and look at the instructions, which tell you what you have to do: one brick at a time. So for every brick you have to look at the instructions to see which brick to use next. The same for the next brick, and so on. This back-and-forth keeps happening until you have finished the entire LEGO set. If your set has 3,300 bricks, that’ll take quite a while. This is HTTP1.1.

With HTTP/2 this changes. You go to the store to pick up your box. Open it, find the instructions and you can ask for all the bricks used on one section of the LEGO set. You can keep asking the instructions for more bricks, without having to look at the manual. “These bricks go together, so here they are.” If you want it really quickly, you could even get all the bricks at once so you can build the set in an instant.

HTTP/2 has a lot of cool features that can help speed up your loading times. The most important one, of course, is full multiplexing, which means that multiple requests can happen at the same time over a connection that stays open for the duration of the transfer process. Another cool thing is Server push; this starts as one request but when the server notices the HTML requires several assets, it can send these all at once without asking. This might be a good fit for your site, but that depends on certain factors too complex to go into here.

Like I said earlier, with HTTP1.1 a browser requests a site -> server sends a header back -> that header contains a status message and HTML body -> for every file needed to build the site, a single connection has to be opened and closed repeatedly. If a piece of this puzzle acts up it can hold up the rest, slowing the process down even further. This is called head-of-line blocking and it sucks big time. This is one of the many reasons why HTTP1.1 could use an update.

We need speed. Site speed has been an SEO ranking factor for years. Now, with the introduction of the mobile-first index, Google will take a critical look at the loading speed of your mobile site. Sites have only gotten bigger over the past few years, and big sites have lots of assets like HTML, JavaScript, CSS, images and so on, which all mean longer loading time.

Another big issue is latency — especially on mobile devices. The longer your latency is, the longer it takes for your request to reach the server and for the server to send back the response. That’s why you should always use a CDN to reduce the time it will take to get your files to your readers from the location nearest to them. While browsers can handle a small number of multiple connections, which in itself, adds additional time to the whole ordeal, the process of sending stuff back and forth doesn’t really change.

There are some things you can do to improve site speed by fine-tuning how your server handles these things, but at its core, HTTP1.1 isn’t a very efficient process. HTTP/2 makes this process a lot easier to manage for servers and browsers, therefore drastically speeding things up. Keep in mind that the advent of HTTP/2 does not retire HTTP1.1 as browsers will still use the old protocol as fallback.

Implementing HTTP/2 is fairly easy and it’s possible that your server is already using it – test it using the tool on the HTTP2.Pro site. Ask your hosting provider to see what your options are. Also choose a Content Delivery Network , also known as a CDN, that offers a full HTTP/2 solution. If you want to implement HTTP/2, you’ll also need an HTTPS connection. If you haven’t got one, get an SSL certificate at Let’s Encrypt, for example, to secure your connection so you can upgrade to HTTP/2.

Edwin is an experienced strategic content specialist. Before joining Yoast, he worked for a top-tier web design magazine, where he developed a keen understanding of how to create great content.

Thank you for sharing this article. What should I do if my host doesn’t support HTTP/2?

It’s not as easy as a flip of a button. Ubuntu is on more than 50% of the cloud servers. Ubuntu does not include support for Https/2 as it is considered an experimental feature by the Apache httpd upstream project.

What this means is that you will need to download non stable apache and try enabling and fixing the issues that arise from it. I tried this on a test server and it was a complete mess for me, the old website-ssl.conf files failed the hardcoded redirects stopped working the apache server crashed and I gave up after 2 hours of trying to fix it.

You should really include information like this when posting the article. Most of the web servers run Ubuntu and Ubuntu does not include http/2 for the reason mentioned above.

“HTTP/2 offers a quick performance win and it even lets you secure your site, because it uses HTTPS connections by default.” Ehm… no, not really. HTTP/2 doesn’t secure the site, HTTPS does and you need to make sure the sites on your server are using HTTPS before moving over to HTTP/2…

Hmm, that was a bit unclear indeed. I’ll fix it. Thanks, Johan!

Excellent heads up there Edwin. Love how new tech seems to be delivering faster & faster solutions to us all. Next call is straight to my Hosts, requesting http/2 implementation. Cheers.

Hey Edwin, If my Hosting Provider doesn’t provide HTTP/2, then What I need to do to get it. Please tell me.

Hi Abhishek. Consider moving hosts! This is an important technical change for hosting companies as well. Forward-thinking companies have gotten on board long ago. If you’re hoster is still lagging behind, maybe it’s time to try your luck elsewhere.

Will be implementing this on my site articlesjar.com soon. Thanks for the suggestion.

Well, HTTP/2 in itself probably not as it is just a new protocol. But since it will give your site a nice speed boost and search engines have been going on about how important speed is, then yes. HTTPS is closely connected to HTTP/2 because without the former, the latter won’t work. So, upgrade both!

It’s the best protocol to boost up the website speed… Thanks Edwin

I think HTTP/2 will make a huge difference in 2018. Everyone has to have it to survive.

It is an important development to upgrade the web, that’s for certain.

Important topic. I am going to test to make sure it uses http/2

Yes, its time there was something to speed up the web. Thanks for the great read.

Awesome post. HTTP/2 will play a major roll in thw furure. Thanks!

I agree that HTTP/2 is a very important development. An easy tool to check if you have HTTP/2 enabled is https://http2.pro/ (also check if you also have ALPN enabled, this is important). Regarding https: you cannot use HTTP/2 without encryption, so you need an SSL certificate. Luckily, most good WordPress webhosts (like us) offer free Let’s Encrypt certificates.

Hey Gijs. Great tip and you are correct about needing an SSL certificate. Another great reason to get your stuff in order.

Thanks – used this link to check that we are http2 enabled. We have NPN NOT ALPN – is this a problem and if so how do we solve this?

Hi! ALPN adds a further speed boost as it makes sure that HTTP1.1 is no longer needed to negotiate between the server and browser. You should check with your hosting company if you can resolve this.

Your website didn’t work :( I found another website can check HTTP/2. And my blog has http/2. :) https://tools.keycdn.com/http2-test

I just checked. “My website doesn’t support HTTP/2” . Thanks for the article though. I had a good read. Thank you Edwin.

You could always use a CDN such as CloudFlare (what we use on multiple domains) and it supports http/2 and you can even buy your https certificate from them, very easy to setup.

Thank you for posting this article. I have to check this with my hosting provider.

We care about the protection of your data. Read our privacy policy.
