---
source: https://www.hobo-web.co.uk/website-frames/
title: Don't Use Website Frames To Design & Build Your Site
scraped: 2026-03-23
published_on: 2007-12-23
tags: live_feed, phase1_ingest, hobo, publication, quality, leak-systems, archive_backfill, historical_source
topic: quality_systems
intent: research, monitoring, source_selection, leak_systems
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Archive backfill - Hobo Web
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Don't Use Website Frames To Design & Build Your Site

Source: Hobo Web
Homepage: https://www.hobo-web.co.uk/
Original URL: https://www.hobo-web.co.uk/website-frames/
Published: 2007-12-23
Strength: leak systems, quality scoring, E-E-A-T, click and satisfaction framing

## Summary
If you are serious about organic search engine optimisation, forget about using, or optimising frames..

## Extracted Body
I’ve been designing and building websites for 25 years, winning awards for websites back in 2006. I’ve been a professional SEO since 2006, when I founded Hobo Web.

Unless you REALLY know what you are doing and why you are doing it…. don’t use frames to design your website .

If possible, avoid using frames . Some people have difficulty navigating within frames, either because the frames are confusing or because the software they are using simply cannot read frames.

When using frames, always offer meaningful NOFRAMES content for those people who cannot read framed information. Use NOFRAMES properly – “ upgrade your browser ” is of no help to someone using (through choice or necessity) the most up-to-date version of a browser that simply doesn’t handle frames. The NOFRAMES section should contain meaningful content with links to the other pages in your site so that they can be accessed without frames.

If you must use Frames, ensure that each frame has a sensible TITLE (in addition to the NAME) which gives a clear indication of the content to be found in that frame.

Frames can, even today, also cause search engines major problems .

For instance, a search engine may only deliver the content frame when accessed through deep links in the SERPs (search engine results pages) – thus rendering your well-thought-out navigation to other pages redundant.

In the nearly 20 years I have been doing this, I have seen many sites appear in Google, complete with a missing navigation system on the page.

The navigation was in another frame, NOT presented by Google as part of the page with the content.

If you are serious about organic search engine optimisation, forget about using or optimising frames and read up on the latest guidelines for SEO.

QUOTE : “ Search Engine Optimisation (SEO) is a technical, analytical and creative process to improve the visibility of a website in search engines. The primary function of SEO is to attract more unpaid traffic to a site that converts into sales (for instance). ” Hobo SEO Tutorial .

A recent discussion in Google Webmaster Hangouts with Google’s Web Trends Analyst, John Mueller, discussed the possibility of prioritising (for ranking) a page with an embedded iframe pulling in another external page’s source code and content.

Could the page with the iframe be made to rank in Google search results instead of the iframe source URL?

QUOTE : “If I syndicate my content to another website with an iframe how can I ensure that the iframe URL gets credit instead of the page embedded (in) the iframe?”

QUOTE : “S o the short version is you can’t – in particular if if a page is embedded within an iframe within a bigger other page then it’s possible that we will index that embedding page as well and when we render that page we obviously see your content because it’s is visible in the iframe as well and to some extent we may say well this is the whole page with this content on it we will index it like that so we could show it in search results like that in general we do figure out this connection between the the iframes version and the embedding page and we do try to show that properly in search to really highlight the original page rather than the just the frame but it’s not something where you can say I want to have both of these visible in search or generally on the web and but I prefer this specific page to actually be shown so things you could do if you if you’re in touch with the other website that’s using the iframe having a rel canonical on that page pointing to the actual content version that you want – alternately if you don’t want your pages to be shown within an iframe there are options that you can put I believe in the head of a page with a special meta tag to say that you don’t want your pages to be iframed and that’s something that browsers will will respect modern browsers at least and that’s something that we respect from our side as well where if we can see that a URL is being shown in iframe but actually that URL wouldn’t work and that I framed and we will respect that for search as well, ” John Mueller Google 2017

The short answer is that ranking number one in Google is not really designed to prioritise such URLs that embed content in an iframe from another page. Google prefers (in general) to present the source URL if it can.

If you control both pages, then you may be able to use a Link Rel Canonical on the source page that is pulled into the Iframe to point to the page that contains the Iframe.

Canonical link elements are only a hint to Google, though, and if users prefer the original, in my experience, Google can, in time, opt to present the original source page in SERPS, despite what Google is directed to do in any canonical link element.

HTML frames are occasionally used to organise a website design by assembling at least two other web pages into a shared visual space.

The strongest arguments against using frames have more to do with usability than accessibility.

For example, frames can reduce the amount of usable space on a page, make it difficult or impossible for users to link directly to or bookmark a specific page within a frameset, and they often prevent users’ Back buttons from working as expected.

As for accessibility , frames are not in and of themselves inaccessible.

Keyboard users and assistive technology users are able to navigate among the various frames that compose a frames page. However, frames do present additional usability challenges that are unique to users with disabilities, particularly those who use screen readers.

Often in a frames interface, a user’s selection of a link in one frame changes the content in another frame.

A sighted user might recognise this change visually, whereas screen reader users receive no indication that a change has occurred. Therefore, in order for this interface to be usable by screen reader users, they must be provided with clear instructions as to what to expect, including where to find the updated content.

Screen reader users can switch back and forth between frames, but they must know which frames to switch to in order to find the content they’re seeking.

Maximum usability of frames for screen reader users also requires that each frame has a meaningful title that speaks to its function. Each frame is titled in the definition of the frameset, by defining of a TITLE attribute for each element. “Navigation” and “Content” are two common examples of frame titles that work well for screen reader users.

In contrast, frame titles like “FrameA” and “FrameB” or “Left Frame” and “Right Frame” should be avoided, because they do not communicate frame function and are of little or no use to screen reader users.

If you must use frames, then do so correctly. For visually enabled users, frames may organise a page into different zones.

For non-visual users, relationships between the content in frames (e.g., one frame has a table of contents, another the contents themselves) should be conveyed through other means.

Frames as implemented today (with the FRAMESET, FRAME, and IFRAME elements) are problematic for several reasons:

In the following sections, we discuss how to make frames more accessible. We also provide an alternative to frames that uses HTML 4.01 and CSS and addresses many of the limitations of today’s frame implementations.

Note that if the frame’s contents change, the text equivalent will no longer apply.

Also, links to descriptions of a frame should be provided along with other alternative content in the NOFRAMES element of a FRAMESET.

and the user agent is not displaying frames, the user will have access (via a link) to a non-frames version of the same information.

Content developers must provide text equivalents of frames so that their contents and the relationships between frames make sense. Note that as the contents of a frame change, so must change any description. This is not possible if an IMG is inserted directly into a frame. Thus, content developers should always make the source (“src”) of a frame an HTML file. Images may be inserted into the HTML file and their text alternatives will evolve correctly.

The following deprecated example should be avoided since it inserts IMG directly in a frame:

Note that if, for example, a link causes a new image to be inserted into the frame:

the initial title of the frame (“Apples”) will no longer match the current content of the frame (“Oranges”).

Content developers should avoid specifying a new window as the target of a frame with target=”_blank”.

QUOTE : ‘ Ensure that a website using a frames environment is usable with non-frames capable browsers by using the <noframes> option.’

Guidelines for UK Government websites Illustrated handbook for Web management teams

QUOTE : ‘ Splitting a page into frames is very confusing for users since frames break the fundamental user model of the web page. All of a sudden, you cannot bookmark the current page and return to it (the bookmark points to another version of the frameset), URLs stop working, and printouts become difficult. Even worse, the predictability of user actions goes out the door: who knows what information will appear where when you click on a link ?’ Jakob Nielsen’s Alertbox for May 1996:

QUOTE : “ Note. A frameset definition never changes, but the contents of one of its frames can. Once the initial contents of a frame change, the frameset definition no longer reflects the current state of its frames.There is currently no way to encode the entire state of a frameset in a URI. Therefore, many user agents do not allow users to assign a bookmark to a frameset. Framesets may make navigation forward and backward through your user agent’s history more difficult for users. ” W3C, 2020

To get a full and complete understanding of how to design with frames , visit the W3C Frames Development page or for more accessibility tips see my Accessibility 101.

QUOTE : “ It makes sense to create websites that are accessible to as many people as possible. To comply with UK law you must put a little effort in to meet accessibility recommendations for websites. The W3c lay down the general guidelines for websites that most people adhere to. ” Shaun Anderson, Hobo 2020
