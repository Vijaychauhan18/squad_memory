---
source: https://moz.com/blog/vibe-coding-seo-tools-whiteboard-friday
title: Vibe Coding Your Own SEO Tools — Whiteboard Friday
scraped: 2026-04-25
published_on: 2026-04-24
tags: live_feed, phase1_ingest, moz, publication, seo-education, whiteboard-friday, archive_backfill, historical_source
topic: seo_education
intent: research, monitoring, source_selection, education
role: researcher, seo, pinchy, current
confidence: medium
canonical: false
canonical_group: Archive backfill - Moz Blog
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# Vibe Coding Your Own SEO Tools — Whiteboard Friday

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/vibe-coding-seo-tools-whiteboard-friday
Published: 2026-04-24
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Metadata
Author: Gus Pelogia
Schema types: Article

## Section Outline
- Table of Contents
- What you need to start vibe coding
- Fuel your insights with real-time SEO data
- How to write your prompts
- Essential concepts to learn
- Sample prompts
- Scale your research with bulk SEO data and metrics from Moz API
- Ideas for tools you can vibe code
- Tag matching
- Entity confidence tracker
- Hreflang matching
- Content decay tracker

## Summary
Ready to learn how to "vibe code" custom SEO tools using ChatGPT and Google Colab? Gus Pelogia shares 5 automation ideas, including entity tracking and hreflang matching, to save you time.

## Extracted Body
#### Table of Contents

- Copied!

Ready to learn how to vibe code custom SEO tools using ChatGPT and Google Colab? Gus Pelogia shares 5 automation ideas, including entity tracking and hreflang matching, to save you time.

Click on the whiteboard image above to open a high-resolution version!

Hi there. I'm Gus Pelogia, SEO product manager, and I'm here to talk to you about vibe coding your own SEO tool .

Now let's just get straight out of the bat, I'm not promising that you're going to build the next revolutionary AI SaaS and you're going to make a lot of money. This is about making little tools that will save you time on your day-to-day, maybe get you away from a bunch of boring tasks, and then just speed up the process, maybe give you a good draft of things that you can review yourself and then make it your own.

### What you need to start vibe coding

So there are three things that you need to vibe code your own tools. First, you need an LLM. I start with ChatGPT. You might try another one.

You may need an API to connect the dots between your LLM and the place where your code is going to run. Your code can be on Google Colab, which is a Python environment that runs on your browser. You don't have to install anything. You're literally going to copy the code from the LLM, paste it there, and magic is going to happen. Or a place like Google Sheets if you want to run your tool in a place that you're more familiar with. You can do both of them.

### Fuel your insights with real-time SEO data

### How to write your prompts

Now, let's go through a little bit of the process here. I'm not going to read you a whole prompt. We can put them on the blog post that is going to come with this video. But there are a couple of rules that you need to follow. You may find different ways to do this. This is how I like to do it. It works for me, so I'm happy to share.

I always start my prompt by saying that I want a code for Google Colab or Google Sheets, so it knows what language and what format it needs to be. It knows what kind of things are already preinstalled on Google Colab, so you don't have to worry about the code that it's broken or it doesn't work as you expect.

Then, you make sure that you call the API you need. So in my case, I use the OpenAI API. Then, make sure that you ask for a CSV. So, in my case, I always upload the CSV, and I want the CSV in return with the output from the codes that I asked for.

Finally, just be very direct and explicit about the elements you have on your sheet. So in Column A, I have a URL. In Column B, I have embeddings. In Column C, I have a tag. Whatever it is, just make sure to declare what is in each column of your sheet, so then it's very easy for the AI to understand where the information is and where it's going to go.

### Essential concepts to learn

There are some essential concepts that are important to learn in a case like this, and these are related to the tools that I'm going to show you guys, some ideas that I've tried and tested. You might just go off and create your own, and that's absolutely fine. That's the idea here.

But vector embeddings essentially transform words into numbers, and they create a corpus of your page. So all the words on that page have a specific meaning when they are all together. So embeddings will extract all of that from your pages. Then you have cosine similarity, which will look at the corpus of page A, page B, and page C, or even if it's tags or whatever information you have in different columns, and cosine similarity will match them to say how close the information from A is to the information on B.

You might play around with some other APIs as well. I've done a few things with the Google Knowledge Graph API. So you can get some information from Google in there, but you just need to know that you need to call this specific API. So maybe you want to know the name of the API, things like that. You're still going to need to get your own API key. Some are paid as you use them, like OpenAI. Some might have free limits. If you're using Gemini or if you're using the Google Knowledge Graph, you're not going to spend any money at least till you've tried them for a little bit.

### Sample prompts

> I need a Google Colab code that will use OpenAI to: Check the vector embeddings existing in column C. Use cosine similarity to match with two suggestions from each locale (Locale identified in Column A) The goal is to find which pages from each locale are the most similar to each other, so we can add hreflang between these pages. I'll upload a CSV with these columns and expect a CSV in return with the answers.

> Write a Google Apps Script that calls the Google Knowledge Graph API, searches for a specific query (e.g., 'Taylor Swift'), and prints the fields @id, name, @type, description, url, and resultScore. If the query doesn't return a valid result, please print the message 'Query is not present on the Knowledge Graph panel. Guide me on how to add this to Google Sheets to trigger updates daily

### Scale your research with bulk SEO data and metrics from Moz API

### Ideas for tools you can vibe code

So let's go through the actual tool ideas that you can do when you're vibe coding

These are things that I tried and tested myself, and I'm happy with the results. You can always make it better. You can improve things. But it does give you a good taste of what can be done in vibe coding. Those are things that I made maybe in 15 minutes, half an hour. It is quite simple to get those first steps and say, "Oh, this works." Maybe you want to do some improvements, and you refine the code and what you're expecting.

But I'm always just asking ChatGPT. So if the code of one page doesn't work, I will say, "I got this error. Can you fix it for me?" Then you get a new piece of code, and then you try the new one, and you go on and on and on.

#### Tag matching

So the first one is tag matching. I wanted to match certain CTAs with a certain page.

I just had a huge volume of pages that I didn't know where to start. So, I uploaded the tags in a column and the URL and embeddings in two other columns, and I asked ChatGPT to match the two of them. Well, I uploaded the code to Google Colab, and that happened through vector embeddings and cosine similarity.

#### Entity confidence tracker

Then maybe you want to build an entity confidence tracker. We all know Google runs on entities these days. They have a tool where you can just put in any word or any phrase, and it will give you an answer to say if Google understands that as an entity and how strong the confidence in that entity is.

Maybe you want to track your brand name. Or in my case, at some point, I was obsessed with tracking my own name and checking if my knowledge panel was there and if the confidence was increasing. So I built something on Google Sheets that would just do a ping every day and see, and save the confidence level that it was straight on my Google Sheets.

I did it once, and it's been running every day for the last year.

#### Hreflang matching

Maybe you don't want to do manual hreflang matching, or at least not from scratch. You can build something through vibe coding as well, and just upload embeddings from the original source and embeddings from the pages that I want to be matched.

The results are pretty good. In my case, there are pages in a lot of languages, and it does work. It doesn't need to be just English or just the same language. It gives me a very good draft. Then I can go and just spot check and say, "Does this page make sense to be connected to this page?" So it gives you a few steps out of the way right there.

#### Content decay tracker

Everyone seems to be suffering from traffic decreasing these days. Maybe you want to see which pages have lost more traffic over time. So instead of going page by page and seeing, well, two years ago, it had this traffic, and now it has this traffic, you can just do all of this at once and get it in bulk which are the pages that are performing better, which are the ones that are performing worse, and how worse or better they are doing over a certain period of time.

This is just the manual labor. It's just like crunching the data. The real work, the exciting part, is how you are going to figure out putting those pages or this content back on the right track.

#### Find related pages

Finally, maybe you want to find related pages, which is also a combination of vector embeddings and cosine similarity.

So you upload your list of pages and embeddings, and it will find lots of matches. There is an article on the Moz blog explaining how to do this, and we can link from the post as well.

This is all we have for today. I'm Gus Pelogia, and I hope you're excited to vibe code some of your own SEO tools as well.

It's going to save you a lot of time on a Friday or any other day of the week to spend more time doing the things that really matter. Thank you.

Editor's note: This video originally aired in January 2026. We've brought this back to the top of the blog because it remains a helpful reference for your 2026 SEO strategy.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.

#### Gus Pelogia

Gus Pelogia is a journalist turned SEO, currently a Senior SEO Product Manager at Indeed, the #1 job site in the world. He’s spoken at events such as BrightonSEO, Semrush Spotlight, LondonSEOXL, Tech SEO Summit and many more conferences across Europe. Gus is also a contributor to Moz, Search Engine Land, and other well-known industry blogs.

#### Scale revenue from SEO with Moz Pro

#### Get the latest SEO tips and strategies in your inbox

### AI & Search Whiteboard Friday Rollup

Did you know there is only a 12% overlap between organic and AI search rankings? Navigate the shift to AI search with these fundamental episodes of Whiteboard Friday from industry experts. Learn about query fan-outs, AI citations, and how to build content workflows that preserve your voice.

### Travel Marketing: How to Compete and Future-Proof in 2026 — Whiteboard Friday

Prepare your travel brand for AI search in 2026. Chloe Osunsami shares how to use digital PR, human-first narratives, and tailored outreach to boost visibility.

### Reddit Brand Strategy for AI Search — Whiteboard Friday

Learn how to build a Reddit brand strategy for AI search. Victory Umurhurhu explains how to navigate Reddit communities to boost visibility and build audience trust.
