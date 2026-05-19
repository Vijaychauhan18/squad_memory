---
source: https://moz.com/blog/vibe-coding-to-build-seo-tools
title: How I Used Vibe Coding to Build Custom SEO Tools (Without Writing Code!)
scraped: 2026-03-22
published_on: 2025-10-16
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

# How I Used Vibe Coding to Build Custom SEO Tools (Without Writing Code!)

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/vibe-coding-to-build-seo-tools
Published: 2025-10-16
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Raise your local SEO visibility with complete local SEO management.

## Extracted Body
I’ve spent most of my career developing marketing ideas faster than I could implement them. Waiting on engineers, wrestling with confusing API docs, or shelving concepts that never made it out of the backlog became the norm. Sound familiar? It’s a frustrating loop.

That’s when I started experimenting with vibe coding. With AI copilots and APIs, you can skip the bottlenecks and spin up a working prototype faster than you can finish your airport burger.

I'm sharing my three-phase journey from a single Python script to a full web app using the Moz API. You'll also get my framework for prompting LLMs to build your own custom solutions.

I define vibe coding as building real, working tools with the help of AI copilots. You don’t need to know how to code. You just need a clear goal, an API, and a willingness to experiment.

It’s that simple. I’m not sitting in front of a blank code editor anymore. I’m collaborating with an AI that writes, debugs, and improves in real time. Vibe coding lets me move from concept to prototype in hours, not weeks.

For years, building tools felt impossible. I’d come up with an idea, then wait weeks for engineers who were preoccupied with higher-priority projects.

When I did get help, progress crawled. Everything depended on someone else’s time. And even when I tried to take control, confusing API docs made it hard to start.

The long dev cycles drained momentum. You’d lose the spark before anything shipped.

That’s why vibe coding hit so hard. It finally gave marketers like me a way to build fast, keep the ideas alive, and let my coding colleagues focus their time on other revenue-driving initiatives

This whole thing started with a simple request. Chima, one of our content strategists, needed Brand Authority data for fifteen hundred domains for a Moz blog post. I had a Python script that could pull a single API request at a time, but running it 1,500 times would have taken days.

I was sitting in the Montreal airport, pint of Guinness on one side, burger on the other, when I decided to fix it. What if I could turn that single script into a bulk analysis tool?

That’s when I jumped on the vibe coding train. I opened Google Colab, enlisted ChatGPT and Claude as copilots, and started rewriting my script. A few prompts later, I had a working bulk checker using the Moz API .

It wasn’t pretty, but it worked. And once I saw that first CSV file populate, I realized something big: I didn’t need to wait for developers anymore. I could build my own tools - fast.

Once I had the idea, I opened Google Colab and started small. My goal was to take the Moz API and build a script that could handle bulk search intent requests instead of one at a time.

I began with a single API call to test the connection. When that worked, I asked my copilot to expand the code for multiple keywords.

At first, it was a mess - errors everywhere. I expected ChatGPT to read the docs for me and magically build the entire thing in one shot. It didn’t.

That’s when I realized prompting isn’t about delegating. It’s a collaboration. I needed to provide context, explain the errors, and specify what I wanted fixed. Once I did that, the code started working.

Within a few iterations, I had a working prototype that took a list of keywords, ran them through the Moz Search Intent endpoint , and exported the results as a CSV. That small script saved hours of manual work and became the foundation for everything I built after.

And of course, the data assisted Chima with her request for Brand Authority metrics, which was then published in a Moz Blog post, “ Ziff Davis's Study Reveals That LLMs Favor High DA Websites. ”

That was my first taste of vibe coding. A working script, built in an airport, powered by curiosity and Guinness.

The Python script worked, but sharing it was painful. No one on my team wanted to mess with Colab or code. So I opened Gemini and said, “Let’s turn this into a Google Sheets add-on.”

I wanted something anyone could use - plug in an API key, choose an endpoint, and pull data right into a sheet. Gemini asked about the layout, buttons, and error handling. After a few rounds, it clicked.

By the end of the weekend, I had a working add-on. It pulled keyword metrics, saved API keys, and handled errors cleanly. The content team can use it without needing to touch the code.

From there, I knew the next step. If I could build in Sheets, I could build on the web.

After the Google Sheets add-on, I wanted more freedom. Sheets worked, but it wasn’t scalable. Everyone had to run their own version, and publishing through Google’s extension store took forever. I wanted a web app anyone could access instantly.

I took everything I’d already built in Sheets, fed the code into Gemini, and entered, “How can I create a working app using the Moz API in Gemini?”

That’s when things got interesting. Gemini tried to turn me into a backend developer overnight. It assumed I knew how to spin up servers and handle CORS policies. News flash: I didn’t.

But with a little patience and a lot of debugging, we got there.

The Moz API was the anchor. Its documentation was clean, the endpoints were stable, and it gave me the flexibility to test different datasets (rankings, search intent, Brand Authority) all from one interface. Within a few hours, I had a working web app that pulled live Moz data through my API key and displayed it beautifully.

Then I started having fun. I added dark mode and a retro theme!

I updated the ranking keywords endpoint so users could pull up to 500 results at once.

I added a live quota counter that used the Moz API to track monthly usage.

That build changed everything. The Moz API gave me the reliability to experiment fast, and vibe coding gave me the freedom to build without waiting for engineers.

That project proved it! Any marketer can turn an idea into a real tool when the data and documentation are on their side.

If there’s one thing I’ve learned through all this, it’s that prompting is a skill. The way you talk to your copilot determines how well it can build with you. Once I stopped treating LLMs like magic buttons and started working with them like collaborators, everything clicked.

Avoid vague prompts. I break the task into sequential steps right in the prompt. I never try to one-shot the entire build.

I build the foundation (API calls) first, then the UI, then accessibility. This keeps the project manageable.

I never say, "Code doesn't run." I state the error clearly, explain the expected result, and ask the LLM to analyze the script to find the error. For example: "It only returns 25 keywords. Can you analyze the script to figure out why it is not accepting the custom value in the API call?"

I give the LLM a specific persona and context. For example: "You are a Next.js developer with experience deploying on Vercel. Help me build a front-end where the user can add their Moz API key."

I never just accept a fix. I ask the LLM to explain how it solved the error so I can learn the underlying programming fundamentals. This prevents me from making the same mistake twice.

Here’s a helpful workflow you can follow ( check out the downloadable PDF here ):

Prompts are the new superpower. The more you refine them, the more you realize you’re designing the logic behind how your AI builds with you.

This whole journey started with one script and a bit of curiosity. I built a Python prototype, turned it into a Google Sheets add-on, and finished with a web app powered by the Moz API.

Prompting became my real skill. The more I practiced, the better I got at steering LLMs toward exactly what I wanted. And the Moz API made it easy to turn those prompts into something real and measurable.

Here’s the truth: marketers don’t have to wait for developers anymore. You can build your own tools, test your ideas, and create something that moves your business forward.

Vibe coding gives you that freedom. Grab your copilot, plug into the Moz API, and build the thing you’ve been thinking about. You’ll learn more in one weekend of building than in a month of planning.

Currently the VP of Revenue at Moz, Jonathan Berthold is a seasoned SEO and paid media performance marketer with 14 years of experience focused on driving ROI through conversion rate optimization, product development, and creative problem-solving.

You can now track your AI Visibility with the all-in-one SEO tool marketers trust.
