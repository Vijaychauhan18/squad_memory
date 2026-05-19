---
source: https://developers.google.com/search/docs/appearance/video
title: Video SEO best practices
scraped: 2026-05-18
tags: google, official, video_seo, video, structured_data
topic: video_seo
intent: research, synthesis, source_selection, primary_source_reasoning
role: researcher, seo, pinchy
confidence: high
canonical: true
canonical_group: Primary source official_doc
use_for: video discovery, indexing, and video-rich-result guidance
avoid_for: claiming any patent or doc alone proves live ranking behavior
---

# Video SEO best practices

Source type: official_doc
Original URL: https://developers.google.com/search/docs/appearance/video
Page updated label: 2025-12-18 UTC

## Why This Matters
video discovery, indexing, and video-rich-result guidance

## Extracted Passages
- If you have videos on your site, following these video SEO best practices can help more people find your site through video results on Google. Videos can appear in several different places on Google, including the main search results page, Video mode, Google Images, and Discover :
- The technical requirements for getting your content in Google's search results applies to videos too. There are some additional requirements to making your videos eligible to be discovered, crawled, and indexed by Google Search:
- To make it easier for Google to find your videos, we recommend providing metadata about the video. We support structured data , video sitemaps , and the Open Graph protocol (OGP) .
- To be eligible for video features, use a supported video file type. Google can process the following video file types: 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, QVT, RAM, RM, VOB, WebM, WMV, and XAP.
- Some CDNs use quickly expiring URLs. If the video's thumbnail URL changes too often, Google may not be able to successfully index your videos. To make sure your videos can be indexed, use a single unique and stable thumbnail URL for each video.
- To make your videos eligible for specific features like key moments and video previews, make sure your video files are available at stable URLs too. This also helps Google discover and process the videos consistently, confirm they are still available, and collect signals on the videos.
- If you are concerned about bad actors (for example, hackers or spammers) accessing your content, you can verify Googlebot before displaying a stable version of your media URLs. For example, you can choose to serve the contentUrl property only to trusted clients like Googlebot, whereas other clients accessing your page wouldn't see that field. With this setup, only trusted clients will be able to access the location of your video file.
- To be eligible for video features (including video results on the main search results page, Video mode, Key Moments , the Live Badge , and other rich formats), create a dedicated watch page for each video, if it makes sense for your business.
- A watch page 's main purpose is to show users a single video. The following pages are watch pages because watching an individual video is the main reason the user is visiting the page:
- These pages aren't watch pages because the video is complementary to the rest of the content on the page:
- Make sure each watch page has a page title and description that are unique to that video. For tips, check our best practices for writing good titles and descriptions .
- If your website embeds videos from third-party platforms like YouTube, Vimeo, or Facebook, Google may index the video both on your web page and on the third-party platform's equivalent page. Both versions may appear in video features on Google, as long as the pages meet the video indexing criteria .
- For your own watch page where you've embedded the third-party player, we still recommend that you provide structured data , and you may also include these pages in your video sitemaps . To be eligible for more video features, check with your video host to ensure they allow Google to fetch your video file .
- The URL of the watch page that's embedding the video. If you're using a video sitemap, this URL is the value for the video sitemap tag.
- The URL of a specific player for the video. This is often the src value for an element in the HTML of the watch page:
- If you're using structured data, provide the video player URL as the value for the VideoObject.embedUrl property.
- The URL of the video file's actual content bytes, which could be hosted on the embedding site, a CDN, or on a streaming service.
- If you're using structured data, provide the video file's URL as the value for the VideoObject.contentUrl property.

## Retrieval Use
- Use this note before relying on third-party commentary when the task is about Google search systems, ranking mechanics, spam policy, crawling, indexing, or patent-backed hypotheses.
- For patents, treat the material as system-design clues and hypothesis generators, not proof of current live algorithm behavior.

