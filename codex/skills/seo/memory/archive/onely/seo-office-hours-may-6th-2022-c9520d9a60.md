---
source: https://www.onely.com/blog/seo-office-hours-may-6th-2022/
title: SEO Office Hours, May 6th, 2022
scraped: 2026-03-23
published_on: 2022-05-18
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

# SEO Office Hours, May 6th, 2022

Source: Onely
Homepage: https://www.onely.com/blog/
Original URL: https://www.onely.com/blog/seo-office-hours-may-6th-2022/
Published: 2022-05-18
Strength: enterprise technical SEO, JavaScript SEO, large-site indexing and crawler diagnostics

## Summary
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on May 6th, 2022.

## Extracted Body
This is a summary of the most interesting questions and answers from the Google SEO Office Hours with John Mueller on May 6th, 2022.

3:08 “Is there any problem with using web components for SEO?”

John answered, “[…] When it comes to SEO, […] web components are implemented using various forms of JavaScript, and we can process pretty much most JavaScript when it comes to Google Search. And while I would like to say just blindly everything will be supported, you can test this, and you should test this.

And the best way to test this is in Search Console ‒ there’s the URL Inspection tool . And there, you can insert your URL, and you will see what Google will render for that page, the HTML. You can see it on a screenshot, first of all, and then also in the rendered HTML that you can look at as well. And you can double-check what Google is able to pick up from your web components.

If you think that the important information is there, then probably you’re all set. If you think that some of the important information is missing, then you can drill down and try to figure out what is getting stuck there? And we have a lot of documentation on JavaScript websites and web search nowadays, so I would double-check that. […]”

5:18 “Is it OK to use the FAQ schema to mark up questions and answers that appear in different sections of a blog post that aren’t formatted as a traditional FAQ list?”

John replied: “I double-checked the official documentation […] and it looks like it’s fine.

The important part when it comes to FAQ snippets and structured data, in general, is that the content should be visible on the page. So it should be the case that both the question and the answer is visible when someone visits that page, not that it’s hidden away in a section of a page. But if the questions and the answers are visible on the page, even if they’re in different places on the page, that’s perfectly fine.

The other thing to keep in mind is that, like all structured data, FAQ snippets are not guaranteed to be shown in the search results. Essentially, you make your pages eligible to have these FAQ snippets shown, but it doesn’t guarantee that they will be shown.

So you can use the testing tool to make sure that everything is implemented properly. And if the testing tool says that’s OK, then probably you’re on the right track. But you will probably still have to wait and see how Google interprets your pages and processes them to see what is shown in the search results.

For structured data, I think it’s the case for FAQ, but at least for some of the other types, there are specific reports in Search Console as well that give you information on the structured data that was found and the structured data that was shown in the search results, so that you can roughly gauge, is it working the way that you want it to, or is it not working the way that you want it to?

And for things like this, I would recommend trying them out and making a test page on your website, seeing how things end up in the search results, double-checking if it’s what you want to do, and then going off to implement it across the rest of your website.”

If you have more questions about FAQ schema, read the article on our blog with the frequently asked questions about FAQ rich snippets (also known as rich results.)

7:37 “Is Google OK with publishers plagiarizing their own content?”

According to John, “[…] It seems like if you’re re-using your own content, that’s not plagiarizing. […]

From Google’s point of view, if you’re taking content from your own website and publishing that again with some elements of the page changed, that’s essentially up to you. And it’s something where […] you’re not providing a lot of value by just copying the existing article and changing some of the words on it.

So […] from a strategic point of view, probably y ou would be better-suited writing something unique and compelling for those topics, or to create one article that covers these different variations. But […] from a policy point of view, I don’t think there is anything specifically in the way of you taking individual articles and then making a handful of copies of that. […] But my recommendation is [to] make fewer articles that are actually really good.

The one extreme case here that can pop up if you’re […] intensely copying your own content is that you end up creating doorway pages. And that is essentially taking one piece of content and creating lots and lots of variations just with different words in it. And that’s something that would be against our Webmaster Guidelines.

[…] And also that’s something where you’re creating a ton of […] junk pages for your websites, which essentially […] doesn’t provide any unique value overall. And instead of diluting the content of your website like that, I would recommend focusing on making the primary content of your website a lot stronger instead. […]”

10:24 “Our website is not very user-friendly if JavaScript is turned off. Most of the images are not loaded. Our flyout menu can’t be opened. However, the Chrome inspect feature in their all-menu links is there in the source code. Might our dependence on JavaScript still be a problem for Googlebot?”

John: “From my point of view, […] I would test it. […] And probably, I would assume if you’re using JavaScript in a reasonable way, if you’re not doing anything special to block the JavaScript on your pages, then probably it will just work. But you’re much better off not just believing me but rather using a testing tool to try it out. […] So I would double-check our guides on JavaScript and SEO and think about maybe trying things out, making sure that they work the way that you want, and then taking that to improve your website overall.

You mentioned [being] user-friendly with regards to JavaScript. So from our point of view, the guidance that we have is essentially very technical, in the sense that we need to make sure that Googlebot can see the content from a technical point of view and that it can see the links on your pages from a technical point of view. It doesn’t primarily care about user-friendliness .

But, of course, your users care about user-friendliness. And that’s something where maybe it makes sense to do a little bit more so that your users are really for sure having a good experience on your pages.

And this is often something that isn’t just a matter of a simple testing tool, but rather something where maybe you have to do a small user study, or interview some users, or at least do a survey on your website to understand where do they get stuck? What kind of problems are they facing? […] Maybe the text is too small, or they can’t click the buttons properly, those things which don’t align with technical problems but are more user-side things.

[…] If you can improve those, and if you can make your users happier, they’ll stick around, and they’ll come back, and they’ll invite more people to visit your website as well.”

Are you struggling with JavaScript issues? Find out how we can help you with our JavaScript SEO audit or read the ultimate guide to JavaScript SEO on our blog.

13:08 “ Our static page is built with HTML, and our blog is built with WordPress. The majority of our blog posts are experiencing indexing issues in Google. How do I fix this?”

John: “First of all, it’s important to know that these are just different platforms. And essentially, with all of these platforms, you’re creating HTML pages. And the background or the backend side of your website that ends up creating these HTML pages that’s something that Googlebot doesn’t look at. Or at least, that’s something that Googlebot doesn’t try to evaluate.

So if your pages are written in HTML, and you write them in an editor, and you load them on your server, and they serve like that, we can see that they’re HTML pages. If they’re created on the fly on your server based on a database in WordPress or some other platform that you’re using, and then it creates HTML pages, we see those final HTML pages, and we essentially work with those.

So if you’re seeing issues with regards to your website overall when it comes to things like crawling, indexing, or ranking, and you can exclude the technical elements there, that Googlebot is able to see the content, then usually what remains is the quality side of things.

And that’s something that doesn’t rely on the infrastructure that you use to create these pages, but more it’s about the content that you’re providing there and the overall experience that you’re providing on the website. So if you’re seeing something that, for example, your blog posts are not being picked up by Google or not ranking well at Google, and your static HTML pages are doing fine on Google, then it’s not because they’re static HTML pages that they’re doing well on Google, but rather because Google thinks that these are good pieces of content that it should recommend to other users.

And on that level, that’s where I would take a look and not focus so much on the infrastructure but focus on the actual content that you’re providing.

When it comes to content, it’s not just the text that’s like the primary part of the page. It’s like everything around the whole website that comes into play. So that’s something where I would try to take a step back and look at the bigger picture. And if you don’t see from a bigger picture point of view where some quality issues might lie or where you could improve things, I would strongly recommend doing a user study.

And for that, maybe invite a handful of people who aren’t directly associated with your website and have them do some tasks on your website. Then ask them tough questions about where they think maybe there are problems on this website or if they would trust this website, or any other question around understanding the quality of the website. And we have a bunch of these questions in some of our blog posts that you can also use for inspiration . […] Take their answers to heart and think about ways that you can improve your website overall.”

17:12 “I have set canonical URLs on five pages, but Google is showing it on the third page as well. Why is it not only showing the URLs where I’ve set a canonical on it for?”

John said, “[…] Paraphrasing, it sounds like on five pages of your website you set a rel=”canonical”. And there are other pages on your website where you haven’t set a rel=”canonical”. And Google is showing all of these pages indexed essentially in various ways.

I think the thing to keep in mind is the rel=”canonical” is a way of you specifying which of the pages within a set of duplicate pages you want to have indexed like that . Or essentially, which address you want to have used. So, in particular, if you have one page, maybe with the file name in uppercase, and one page with the file name in lowercase, then in some situations, your server might show the same content, technically, they are different addresses. […] But from a practical point of view, your server is showing the same thing.

And Google, when it looks at that, says, well, it’s not worthwhile to index two addresses with the same content. Instead, I will pick one of these addresses and use it to index that piece of content. And with the rel=”canonical”, you give Google a signal and tell it, hey, Google, I want you to use maybe the lowercase version of the address when you’re indexing this content. You might have seen the uppercase version, but I want you to use the lowercase version. And that’s essentially what the rel=”canonical” does.

It’s not a guarantee that we would use the version that you specify there, but it’s a signal for us. It helps us figure out all things else being equal, you really prefer this address, so we will try to use that address. […]

And it comes into play when we’ve recognized there are multiple copies of the same piece of content on your website. And for everything else, we will try to index it to the best of our abilities. And that also means that for the pages where you have a rel=”canonical” on it, sometimes it will follow that advice that you give us. Sometimes our systems might say, I think maybe you have it wrong. You should have used the other address as the canonical. That can happen. I t doesn’t mean it will rank differently, or it will be worse off in Search. It’s just, well, Google systems are choosing a different one.

And for other pages on your website, you might not have a rel=”canonical” set at all. And for those, we will try to pick one ourselves. And that’s also perfectly fine. And in all of these cases, the ranking will be fine. The indexing will be fine. It’s just the address that is shown in the search results that varies.

So if you have the canonical set on some pages but not on others, we will still try to index those pages and find the right address to use for those pages when we show them in Search. So it’s a good practice to have the rel=”canonical” on your pages because you’re trying to take control over this vague possibility that maybe a different address will show. But it’s not an absolute necessity to have a rel=”canonical”.

Do you struggle with Google ignoring your canonical signals and choosing the wrong pages to index? Read our article on how to fix “Duplicate, Google chose different canonical than user.”

20:56 “ What can we do if we have thousands of spammy links that are continuously placed as backlinks on malicious domains? They contain spammy keywords and cause 404s on our domain. We see a strong correlation between these spammy links and a penalty that we got after a spam update in 2021. We disavowed all the spammy links, and we reported the domain which is listed as a source of the links of spam. What else can we do?”

John replied as: “[…] There are two things I think that are important to mention in this particular case. On the one hand, if these links are pointing at pages on your website that are returning 404, so they’re essentially linking to pages that don’t exist, then we don’t take those links into account because there’s nothing to associate them with on your website. Essentially, people are linking to a missing location. And then we’ll say, well, what can we do with this link? We can’t connect it to anything, so we will drop it […] like a lot of those are probably already dropped.

The second part is you mentioned you disavowed those spammy backlinks. And especially if you mention that these are like from a handful of domains, then you can do that with the domain entry in the disavow backlinks tool. And that essentially takes them out of our system as well. So we will still list them in Search Console, and you might still find them there and be a bit confused about that. But essentially, they don’t have any effect at all. If they’re being disavowed, then we tell our systems that these should be taken into account neither in a positive nor a negative way. So from a practical point of view, both from the 404 sides and from the disavow, probably those links are not doing anything negative to your website.

Need help with disavowing some unwanted backlinks? Take advantage of link risk management to reevaluate your backlink strategy.

And if you’re seeing significant changes with regards to your website in Search, I would not focus on those links but rather look further. And that could be within your own website to understand a little bit better what is the value that you’re providing there. What can you do to stand up above all of the other websites with regard to the awesome value that you’re providing users? How can you make that as clear as possible to search engines? […] You can disavow the whole domain that they’re coming from and then move on. There’s absolutely nothing that you need to do there. And especially if they’re already linking to 404 pages, they’re already ignored.”
