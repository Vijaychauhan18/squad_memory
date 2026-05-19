---
source: https://moz.com/blog/ai-tools-to-improve-seo
title: 6 Ways ChatGPT Can Improve Your SEO
scraped: 2026-03-23
published_on: 2023-07-24
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

# 6 Ways ChatGPT Can Improve Your SEO

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/ai-tools-to-improve-seo
Published: 2023-07-24
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
From on-page optimizations to technical SEO, AI can do more than create content. Supercharge your organic traffic with these tips from Moz’s SEO Director.

## Extracted Body
Most of the discourse surrounding the impact of artificial intelligence (AI) on SEO has been about content creation. This makes perfect sense. Large language models (LLMs) have fundamentally changed the speed at which businesses and individuals can produce blog posts, marketing copy, social media posts and much more.

I am not the first to provide the caveat that while AI tools can help you speed up your writing process, they can also open up your site to a variety of SEO risks including duplicate content, violations of Google’s E-E-A-T Guidelines , generally robotic copywriting that is devoid of brand voice and personality, and a host of other issues.

AI content generation is certainly something that can help SEOs and businesses in moderation. Google itself has essentially okayed the use of AI, as long as it is with intent to produce “ helpful content ”. This can be easier said than done.

In this article, I want to highlight some ways that free AI tools like ChatGPT can help SEO’s with all sorts of other tasks, other than creating content. There are a wide range of things that SEOs do everyday that can significantly be sped up or even completely done by free AI tools like ChatGPT. These can range from On-Page SEO optimizations to Technical SEO projects.

Perhaps the most straightforward way in which tools like ChatGPT can simplify our work as SEOs is by writing schema markup for us. I will keep this section short, as the process in itself is fairly straightforward.

Write a ChatGPT prompt that describes the schema you want to create, and for which page.

QA the results and run them through a Schema validating tool.

Remember, ChatGPT typically will not visit a URL for you, so you will need to paste the entire text of your page in the prompt.

The response is a block of schema code that you can paste into a validator. Note that the response was not 100% perfect, hence the need to QA. ChatGPT missed the name of the publisher organization. Before dropping this code onto the published page in our CMS, I would change the name of the organization from “Example” to “Moz.”

Another time-saving SEO task that you can jumpstart with ChatGPT is the semantic grouping and categorization of keywords . This can be done within the user interface (UI) of GPT, or through a python script that utilizes OpenAI’s API.

Using the UI, I have had success grouping around 100 keywords at a time. The output will typically be an indented, bulleted list of all your terms categorized into buckets.

A python script gives you more flexibility to increase your number of max tokens and allow you to work with longer lists of keywords.

Below is an extremely simple python script that prompts OpenAI to come up with categories for a list of keywords.

The output will look like something like this. You can use this output to modify groupings in your keyword tracking tool of choice, such as Moz Pro . If you are familiar with using Pandas, you can turn the generated_text output into a dataframe for an easy CSV export.

ChatGPT is exceedingly good at taking large amounts of text input and summarizing it. What better way for SEOs to utilize AI’s summarization capabilities than generating meta descriptions ? Since meta descriptions are inherently summaries of pages, natural language processing (NLP) models do a good job of extracting the main ideas from multiple paragraphs of text and condensing them into one.

When feeding ChatGPT with text to summarize, you can also include a few keywords that you want it to include in its output. This is another instance where you will need outside data from a tool such as Moz Keyword Explorer to help you find focus keywords. Once you have an idea of the main keyword(s) of the page you want to optimize, you can include those in your meta description prompt. That prompt may look something like this:

In my experience, however, ChatGPT is not very good at limiting its responses to a certain word or character length. You may get something like this, and need to change or remove a few sentences.

Still, this simple task could potentially have saved you 10–15 minutes of working with a blank page (or CMS field) and given you a starting point for your meta description.

Another task that leverages ChatGPT’s summarization capabilities is the creation of frequently asked questions (FAQs).

Prompt GPT to create FAQs for a section of page copy that you paste into the tool, and AI will generate some sample FAQs for you. The responses it gives tends to be brief, which is ideal for tagging them with FAQ schema.

After you’ve reviewed and edited the FAQ suggestions that ChatGPT provides, circle back to tip #1 and paste them back into ChatGPT to generate FAQ schema that you can add to your page.

While OpenAI’s free ChatGPT tool does not provide Keyword Volume or other important SEO keyword metrics, it can still be an effective engine for generating content ideas related to a given keyword.

When paired with a tool like Moz Keyword Explorer , the results can be powerful.

Begin the process as you would normally approach keyword research. Identify a list of keywords that you want to include in your page. Then, ask ChatGPT to create topic ideas related to these terms.

I find that prompting the tool for around 50 topics gives you a good sample of page ideas without repetition.

The results are not all going to be perfect titles for you to copy and paste into your CMS without reviewing them, but they can rapidly (and I mean RAPIDLY) give you a sense of direction for your editorial calendar, content marketing strategy or even social media posts. Each of the concepts identified here about SEO, focusing on the specified keywords, has the makings of a well-intentioned blog post topic.

Once you have done your keyword research and compiled terms that you would like to include into a new page on your website, try asking ChatGPT to use them to create a page outline for you, along with a possible page title.

This can serve as a great jumping-off-point for your editorial team (or you) to work with to write your full article. An outline or content brief for a page about keyword research may look something like this:

As is a recurring theme with the use of AI for SEO, the results are not perfect, but they can generate ideas for you to take and run with. For example, you may realize that this outline does not get into the concepts of Search Volume or Keyword Difficulty, which you wanted to address on your page. You can tweak your prompt to specify a few additional keywords that you’d like to include, or manually edit ChatGPT’s output to suit your needs.

My guess is as good as any regarding the direction AI will steer the digital marketing industry, and more specifically SEO. What I do know is that right now, there are so many ways in which AI can make tedious aspects of my job less time consuming, so I can focus my attention on more strategic and big-picture problems. Hopefully this list helps you do the same.

Thinking of pitching for MozCon New York 2026? Learn how to create a standout speaker pitch, discover hot topics organizers love, and boost your chances of taking the stage.

When you're set up for success, being a mentor can be a rewarding experience for you and your mentee. Miracle’s in-depth framework presented in this week’s Whiteboard Friday covers considerations like building trust, setting boundaries, and the qualities that make a great mentor.

Wondering how the latest news around the Google Antitrust ruling will impact search and SEO? Dr. Pete breaks down the final Google antitrust remedies as determined by the court and how this landmark ruling will reshape search and SEO over the next five years.
