---
source: https://portent.com/blog/seo/how-to-generate-video-sitemaps-using-google-docs.htm
title: How to Generate Video Sitemaps using Google Docs
scraped: 2026-05-11
tags: elite_article, seo, portent, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# How to Generate Video Sitemaps using Google Docs

Source expert/publication: portent
Source homepage: https://www.portent.com/blog/seo
Original URL: https://portent.com/blog/seo/how-to-generate-video-sitemaps-using-google-docs.htm
Published: unknown

## Why This Matters
Discovered via XML sitemap during elite bulk backfill.

## Extracted Article Passages
- Let me just start out with the ending. The Google Doc below takes a list of pages containing embedded YouTube or Vimeo videos and uses magic to grab all the data you need for a video XML sitemap. Then it makes the sitemap for you.
- You can have it by going to the link below and selecting “Make a copy” under “File.” The instructions are right in the document.
- If you want to know more about how it works, keep reading. But if, not – thanks for stopping by and hopefully this makes your life a bit easier!
- Before I go into the details, I do recommend taking the time to learn more about video sitemaps. Rather than repeat what others have already said, I’ll just tell you to start with the horse’s mouth then read other articles like this great post by Phil Nottingham or this one by Justin Hammack .
- Second, I should say that, even though this tool does generate a fully compliant video sitemap you can give straight to Google, I don’t actually recommend doing that. This isn’t the only video sitemap generator out there, but I wanted something that was a bit more straightforward and would allow me to easily customize the various fields.
- So I made this to specifically help with some of the more time-consuming tasks but still let me optimize the data for each video. I’m still working on the tool that does my entire job for me.
- You’ll notice several tabs on the spreadsheet, but basically the doc does two things. First it sucks up all the meta data from the actual video pages on YouTube or Vimeo. Second, it organizes all that data so you can customize it, then marks that in XML sitemap format.
- 1. Get your list of landing pages. Start with a list of URLs you know have either YouTube videos or Vimeo videos embedded on them. If you have a large site, you can use Screaming Frog or another crawler to scan your sites for pages that have the embed code.
- YouTube has had a few types of embed codes over the years, so I recommend searching for code that contains either “youtube.com/v/” or “youtube.com/embed/”. For Vimeo, the links are going to contain either “player.vimeo.com/video” or “video.com/moogaloop.swf?clip_id” so that’s the text you want to look for.
- 2. Go to the YouTube or Vimeo extractor sheet. Pages with YouTube videos go on the “YouTube Embed Extractor” sheet. Pages with Vimeos go to the “Vimeo Embed Extractor.”
- You’ll notice that there’s also another two tabs in case you already have a list of video pages and would rather just pull the data directly from there. That’s fine, but remember that you need the URL from your own site to make a video sitemap.
- 3. Paste the URLs into the sheet. I know I say it’ll handle 15 URLs in the doc, but I really wouldn’t recommend doing more than 10 URLs at a time. The doc is pulling HTML from both the landing page and video page. This means that when you run 5 URLs, the doc is storing all of the HTML from 10 pages.
- 4. Drag down the formula rows. There’s a few hidden cells so be sure to include the orange cell on the right when you’re dragging down the formulas.
- 5. Copy all the cells in the green zone (including the original landing page) and paste values only into the “Generator” sheet. Seriously, remember to do “values only” otherwise your browser might kill itself.
- 5.1 Rinse and repeat. Keep adding to the “Generator” sheet until you’ve finished all of the pages. Do some Vimeos then some YouTubes if you want. If there are other video types, you can just type those into the “Generator” sheet, too. That’s still easier then marking up a text file manually.
- 6. SEO your data. If you think you’re going to get rich snippets by copying the titles and descriptions directly from YouTube and Vimeo, good luck. Plus, chances are some of the titles and descriptions suck anyway, so just rewrite them. Also, I have columns for some of the more recommended optional tags like “video:category” and “video:uploader.” Add those where you can or leave them blank if you have nothing to put there.

## Retrieval Use
- Use when the task maps to `portent` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

