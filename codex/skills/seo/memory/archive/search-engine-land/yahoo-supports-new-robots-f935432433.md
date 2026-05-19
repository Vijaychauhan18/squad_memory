---
source: https://searchengineland.com/yahoo-supports-new-robots-nocontent-tag-to-block-indexing-within-a-page-11120
title: Yahoo Supports New Robots
scraped: 2026-03-23
published_on: 2007-05-02
tags: live_feed, phase1_ingest, search-engine-land, searchengineland, publication, industry-news, archive_backfill, historical_source
topic: industry_news
intent: monitoring, news, source_selection
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Search Engine Land
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Yahoo Supports New Robots

Source: Search Engine Land
Homepage: https://searchengineland.com/
Original URL: https://searchengineland.com/yahoo-supports-new-robots-nocontent-tag-to-block-indexing-within-a-page-11120
Published: 2007-05-02
Strength: industry coverage, rollout monitoring, search product and platform changes

## Summary
For over a decade, search engines have supported standards allowing you to prevent pages from being spidered or included within a search index. Today, Yahoo now supports a new twist — a way to flag that part of your page shouldn’t be included in an index. It’s called the robots-nocontent tag. Many search marketers have […]

## Extracted Body
For over a decade, search engines have supported standards allowing you to prevent pages from being spidered or included within a search index. Today, Yahoo now supports a new twist — a way to flag that part of your page shouldn’t be included in an index. It’s called the robots-nocontent tag.

Many search marketers have long struggled with the problem that the “core” content of a web page — the main body copy or article — can often seemed drowned out from a text analytics perspective by all the clutter around the content. That clutter is often ads, navigational links, cross promotion material and other stuff used in page templates.

The new robots-nocontent tag now allows you to tell Yahoo to ignore the clutter. Simply use the tag (technically, it’s an attribute) to surround text you do NOT want included in searchable content within Yahoo.

How? It’s a little complicated, but not too hard. You need to have a class attribute called robots-nocontent assigned to some tag within your document. The attribute looks like this:

Now let’s say you have a paragraph of text you do NOT want included. You could use the <p> paragraph tags with this class attribute to flag the content as not to be indexed. Here’s the before:

<p> Blah blah here’s my text it is so bad blah blah blah. </p>

And here’s the after, where I’ve bolded how robots-nocontent would be added:

<p class=”robots-nocontent” > Blah blah here’s my text it is so bad blah blah blah. </p>

Let’s say you have a block of text you wanted to flag. You could do this using container tags like <SPAN> or <DIV>. For example, here’s another before and after:

<p> I remembered a bad poem I wanted to write </p> <p> But then I forgot it in the night </p> <p> Sadly I remembered in the day </p> <p> I wrote it; it got indexed, and now it won’t go away </p>

That’s several paragraphs of text, and flagging each paragraph to nocontent would be a pain. Instead, you could enclose all of them with a special <DIV> tag, as bolded below:

<div class=”robots-nocontent”> <p> I remembered a bad poem I wanted to write</p> <p> But then I forgot it in the night</p> <p> Sadly I remembered in the day </p> <p> I wrote it; it got indexed, and now it won’t go away </p> </div>

Yahoo’s new tag was inspired from a microformat draft for robots exclusion you’ll find here . However, that draft is NOT the standard Yahoo is using. Let me say that again, more loudly.

The new robots-nocontent standard is solely Yahoo’s own creation, and they define how it will be used for Yahoo alone. See Yahoo’s official guidelines here . Other search engines might decide to support it, similar to how Google, Yahoo and Microsoft all support the nofollow attribute for links.

Because this was just announced, I haven’t yet surveyed the other search engines to see if they’ll join in. I can tell you that none of them will have an answer today. They’re going to need to consider making such a change and examine how they might implement it.

Some more things about no-content, from talking with Yahoo about it:

You can use the attribute alongside other attributes, as well. Yahoo says you should simply add them within the quoted class area, with a space between attributes.

For example, say you have a class for a DIV tag already called “navigation” that you use to style navigational links. It might look like this:

To add no-content, just insert that attribute anywhere within the quoted section, the part after class=, like this:

Before, after or between other attributes, it makes no difference, Yahoo says.

Now some history. Yahoo first proposed this type of attribute way back in February 2005, at the Web Spam Squashing Summit that Niall Kennedy organized. A month later, Yahoo presented it at an indexing summit that I organized. They revisited it again, sharing it with the audience of the robots.txt summit I organized last month. The response was positive enough from both summits that they’ve decided to try it out.

That’s what I love about these types of summits — they really can produce changes with the search engines (and I’ve got two more coming up, Duplicate Content Summit and Penalty Box Summit at our SMX Advanced show in Seattle next month).

Finally — what will this mean for search marketers and searchers in general. Who knows. When nofollow came out, we saw it start to have a dramatic impact in usage, especially in people being uncertain what they should and shouldn’t flag as nofollow ( Time For Google To Give Up The Fight Against Paid Links? from me last week covers this a bit more).

The robots-nocontent attribute should be less controversial. That’s because it’s not something someone can use against you. Instead, as with ways of blocking content , this is a means for site owner to exercise more control over how they are listed.

Contributing authors are invited to create content for Search Engine Land and are chosen for their expertise and contribution to the search community. Our contributors work under the oversight of the editorial staff and contributions are checked for quality and relevance to our readers. Search Engine Land is owned by Semrush . Contributor was not asked to make any direct or indirect mentions of Semrush . The opinions they express are their own.

Danny Sullivan was a journalist and analyst who covered the digital and search marketing space from 1996 through 2017. He was also a cofounder of Third Door Media , which publishes Search Engine Land and MarTech , and produces the SMX: Search Marketing Expo and MarTech events. He retired from journalism and Third Door Media in June 2017. You can learn more about him on his personal site & blog He can also be found on Facebook and Twitter .

Free technical audit shows what's blocking your search visibility.

1 Year → 1,000 Links: How Digital PR Builds Authority for SEO and AI Search

Blueprint for excellence: How leading agencies drive growth, prove value, and scale smarter

Third Door Media operates business-to-business media properties and produces events, including SMX. It is the publisher of Search Engine Land, the leading digital publication covering the latest search engine optimization (SEO) and pay-per-click (PPC) marketing news, trends and advice. The company headquarters is 800 Boylston Street, Suite 2475, Boston, MA USA 02199.
