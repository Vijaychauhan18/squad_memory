---
source: https://yoast.com/gutenberg-alternative-approach/
title: An alternative approach to Gutenberg
scraped: 2026-03-23
published_on: 2017-10-03
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

# An alternative approach to Gutenberg

Source: Yoast SEO Blog
Homepage: https://yoast.com/seo-blog/
Original URL: https://yoast.com/gutenberg-alternative-approach/
Published: 2017-10-03
Strength: SEO education, WordPress SEO, structured content and AI-era optimization guidance

## Summary
We've been thinking hard about the new editing experience for WordPress, Gutenberg. This post outlines what we think would be a better approach.

## Extracted Body
Drive more traffic to your site. Use AI to save time doing SEO tasks. Make SEO easier . And get 24/7 support .

There’s a lot of discussion in the WordPress world right now about a new editing experience that’s in the making. It’s called Gutenberg. While some of that discussion is technical, every user that uses WordPress regularly should be aware of what’s coming. At Yoast, we are quite excited about the concept of Gutenberg. We think it could be a great improvement. At the same time, we have our worries about the speed in which the project is being pushed forward. And, we’re not excited about all the changes.

In this post, I’ll first try to explain what Gutenberg is. Subsequently, I will tell you about the things that are problematic to us. Finally, I will tell and show you what we think should be done about the problems.

Update: I’ve written another post showing some concepts for integrating Yoast SEO with Gutenberg »

Gutenberg is a new approach to how we edit posts in WordPress. It’s basically a new editor. It tries to remove a lot of the fluff that we built up over the years. The intent is to make the new experience lighter and more modern. The end-goal is to make WordPress easier to use. That’s something we really appreciate at Yoast.

Gutenberg introduces the concept of “blocks“. The new editor will be a block-editor: paragraphs, headings, images and YouTube video embeds will all be blocks. Blocks will make it easier to learn how to work with WordPress. People starting out with WordPress, only have to learn the concept of blocks, instead of 3 or 4 different concepts. When we make WordPress easier to use, we make it more accessible to a larger group of people. Making editing easier was the goal from the outset, as Matt Mullenweg is quoted on the Gutenberg Github page :

The editor will endeavour to create a new page and post building experience that makes writing rich posts effortless, and has “blocks” to make it easy what today might take shortcodes, custom HTML, or “mystery meat” embed discovery. — Matt Mullenweg

As well as introducing blocks, Gutenberg also introduces a new look and feel for the editor. For me, the look and feel is mostly a copy of the Medium editor, an editor that got a lot of praise in certain online circles. Gutenberg appears a bit more modern, more contemporary.

Besides introducing a new look and feel and the concept of editing blocks, Gutenberg also introduces an entirely new technology to WordPress. Gutenberg will use a lot of JavaScript, particularly React. While this change in itself is not interesting to the average user, it does impact how WordPress is built.

Here at Yoast, we are worried about the use of new technology combined with the introduction of big new concepts. This is bound to make for a rocky experience. We know from our own experience releasing Yoast SEO 3.0 (we’d rather not talk about that anymore). Even when releases are very well prepared, a lot can go wrong and you’ll be busy fixing it for a long time. We feel worried about the combination of new technology, completely renewed functionality, and the extremely ambitious time plan.

The concept of blocks brings some very powerful new tools to plugin authors. At Yoast, we have lots of ideas on how to make our content analysis better, faster, and more user-friendly with the Gutenberg editor. However, Gutenberg does currently not have the technical necessities in place to allow us to actually build that integration. Yoast SEO can’t integrate with the new editor (yet). Of course, we are actively involved in the technical discussions around this. We are currently heavily discussing how to make it possible for plugins to integrate.

Fact remains that, if you test Gutenberg right now, you’ll see that Yoast SEO is not on the page, anywhere. Nor, for that matter, are all the other plugins you might use like Advanced Custom Fields or CMB2. All of these plugins use so-called meta boxes, the boxes below and to the side of the current editor.

The fact that the Gutenberg team is considering changing meta boxes is, in our eyes, a big mistake. This would mean that many, many plugins would not work anymore the minute Gutenberg comes out. Lots and lots of custom built integrations would stop working. Hundreds of thousands of hours of development time would have to be, at least partly, redone. All of this while, for most sites, the current editor works just fine.

The current version of Gutenberg has major accessibility issues both in its frontend output and in the backend editor. This ranges from inline styles in the output to many other things .

We feel very strongly about accessibility. Not without reasons. The law in many European countries requires government institutions to have properly accessible websites. If Gutenberg breaks their accessibility, they will have to disable it, or face lawsuits. The Gutenberg team needs to realize that accessibility requirements are simply that: requirements.

To conclude: we are very enthusiastic about the idea of blocks, but have strong concerns about some of the technical choices and the speed of the implementation process. We are also worried about the lack of priority given to accessibility issues in the project. But most importantly, we are very much concerned about the fact that plugins are not able to integrate with the new editor.

In a recent post about the JavaScript library of choice for the WordPress ecosystem, WordPress’ project lead Matt Mullenweg said:

It will likely delay Gutenberg at least a few weeks, and may push the release into next year.

At Yoast, we were pretty shocked about these words. In its current form, Gutenberg is not ready -at all- for mainstream usage. In fact, we do not see it as being ready to be released anywhere in the first half of 2018. In our view, ready to be released also means that the community has had ample time to fix all of their integrations. In this point of time, it’s not possible for plugins at all to integrate with Gutenberg. How on earth should plugin authors be able to build their integrations within a few months? That’s not possible. At least not without breaking things.

We think that taking the following three steps would bring Gutenberg much closer to release:

Once we’ve decided on the above, we should start educating plugin & theme developers on what will and what will not work in the new environment.

We’ve made some mockups of what we think this could look like (click for larger versions):

Note that we have disabled the background color and text color controls in the block level mockup. These should be off by default in our opinion, and possibly only allow a subset of colors, chosen by the theme author, when enabled.

I’d love to discuss with you, in the comments here, on Github, on Slack: everywhere!

Joost is an internet entrepreneur and the founder of Yoast. He has a long history in WordPress and digital marketing. On our blog, he has written a lot about SEO in general, technical SEO and important topics related to SEO.

It works great now. It’s not broken. We don’t have fix it (yet). But maybe we will have to if this is forced on us.

Me? I’m going to turn off automatic upgrades and keep my current WP version right up to the last possible minute before I have to switch.

And I know what I’m talking about: as a former Authorized AutoCAD dealer and drafting service bureau chief, I STILL use AutoCAD 14 (from 1997), because it is simply the most productive and fastest AutoCAD for simply turning out drawings.

During the last year I was with AutoDesk, and they came out with “The Best AutoCAD Ever” (Release 13, duh), I had to advise my customers NOT to upgrade to AutoCAD 13 because it was such a productivity decrease. I turned away a potential $125,000 in upgrade income because I was honest with my clients.

Hey Tim. Thanks for the reminder about turning off automatic updates! That’ll solve a boatload of launch issues until they work all the kinks out.

As mentions it is using many JavaScript, Will it affect site speed or SEO?

Look at the way https://www.postleaf.org/ does things and that’s the way we should go. Dust.Js teamed up with Node.Js is quite a powerful duo indeed!

There will always be worry with the introduction of something new! I personally love WP..

@ David Finch: since when does market share of a CMS have anything to do with the fulfilling the goals of a website for a website/business owner?

The Toyota Camry is one of the most popular cars sold. Yet that makes it a terrible choice if you need to haul a metric ton or two of building supplies; a semi-truck would be a much better choice for that. Or maybe I need a track car. I’ll pick up a used Ferrari. Last I checked, Ferrari had less than 1% market share. Does that make the Volvo Semi or Ferrari any less relevant?

Price is irrelevant when it comes to a CMS if meets business goals. FWIW, Automattic charges a minimum of $2500/mo for WP hosting. That doesn’t make your £24 per month hosting irrelevant, they’re simply different markets.

You mentioned, “Gutenberg will use a lot of JavaScript, particularly React.” Does that mean the site will become JavaScript too? If so, won’t that reduce the traffic to sites? Aren’t there browsers and OS that try to limit JavaScript? I guess I am missing something here.

SO – there will be no OPTION to NOT use the new editor when WP releases it?

No but there are other editors you can install or at least there will be.

Completely agree with your view on launching totally new product rather than revamping the existing one. In this way, people will get time to migrate from existing to new product. Here they can also have option for easy migration without worrying about compatibility once the new product get stable.

I stopped building things with WordPress years ago and moved on to better CMSs that had a modern approach, Craft CMS for example.

It was inevitable that at some point WordPress would need to start ditching its legacy code and backwards compatibility to be able to move forward on a cleaner code base. I understand the concerns raised, and do sympathise, but I think overall it’s better to embrace the difficulties of change, rather than keep WP locked in the past.

For people using WordPress as a CMS for delivering content-rich experiences, the block style editor is long overdue and is absolutely necessary if it wants to keep its place as the most used CMS on the planet. It’s probably not so good for people who mainly use WP as a simple blog editor: for them, a single text entry panel is still probably a better UX.

Perhaps WP needs a high-level switch on each page, to choose between these two types of content editing. Or maybe it’s simply time to create a new WP product entirely that can compete with the more robust CMSs out there. Traditional WP for bloggers who want the old experience, and a new “WP Pro” for developers building sites that require complex content management.

I do agree the change needs to happen but slow it down a bit and don’t rush things as that just leads to pain and unhappy customers and an angry community. Would you mind listing these supposed more robust CMS’s that WordPress competes with? Since WordPress has 28.6% of all websites and Joomla in 2nd place has a total of 2.5 million websites in the world, I don’t see any competition.

Oh and Matt, why would I pay for up to $300 for a CMS that isn’t even in the top 10?

Your read is similar to mine: this is a great evolutionary step. Like you, we’ve moved on from WP as well (to Craft) but still follow Yoast because of their contributions not only to WP but to SEO, etc. (I would love to see a Craft CMS port of Yoast SEO but that’s another topic.)

It seems to me there’s a lot of people claiming “WP is moving my cheese!” Yeh, to that I say: “Well go find it!” You want to stay relevant in this space? Evolve or die.
