---
source: https://moz.com/blog/build-reddit-keyword-research-tool
title: Build Your Keyword Tool with Python and ChatGPT: A Subreddit Insights Guide
scraped: 2026-03-23
published_on: 2023-11-22
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

# Build Your Keyword Tool with Python and ChatGPT: A Subreddit Insights Guide

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/build-reddit-keyword-research-tool
Published: 2023-11-22
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Unlock Reddit's SEO goldmine with ease. This guide is for SEO pros, content creators, and marketers seeking to automate Reddit research using Python and ChatGPT.

## Extracted Body
With its vast user-generated content, Reddit is a potential goldmine for SEO Insights. However, manually analyzing this massive amount of data to extract valuable information can be time-consuming and inefficient.

This guide describes how to automate the process using ChatGPT and Notable plugins. We'll navigate the necessary tool setup, data extraction, and analysis to draw actionable insights from Reddit, enhancing your SEO strategy.

By following along, you'll learn to overcome the manual analysis barriers of Reddit, making the data work for you. Also, you'll better understand market trends and consumer interests, allowing for more informed digital marketing decisions.

Many SEO professionals I have encountered are not technically inclined and might be unfamiliar with application programming interfaces (APIs). If you're familiar with APIs, please jump to the "Step-by-step guide to acquiring a Reddit API key" section. Otherwise, let's delve in.

An API key is similar to a unique password identifying who requests an API. It helps the API service manage access, track usage, and ensure security.

An API rate limit is a control mechanism that defines how many requests a user or application can make to an API within a specified timeframe. This ensures the service remains stable and available to all users by preventing a user or application from overloading it.

Reddit mentions that clients may make up to 60 requests per minute. However, since we will use the Python Reddit API Wrapper ( PRAW) in this article, it's important to know about this Python package's rate limits.

Based on PRAW's documentation , the rate limits follow Reddit's rules about how often you can make requests. If you hit the limit, the library waits a bit before making a second attempt. However, if Reddit instructs to wait longer than the set maximum wait time, PRAW stops and shows an error.

If you haven't created a Reddit account yet, do so first. Once registered, log in and proceed with the following steps to navigate to the app preferences page.

Click on your profile icon located at the top-right corner of the Reddit home page.

Click on the "Safety & Privacy" tab on the User Settings page.

Scroll down until you see the "App Permissions" section. Click on "Manage Third-Party App Authorization."

The screenshot below provides a visual guide for these steps.

On the App Preferences page, find and click the button labeled "Are you a developer? Create an app...".

Provide a brief "description" for your app. (It is optional but can be filled if desired.)

Having acquired the necessary API key, we will now move on to setting up your Noteable workspace to facilitate smooth interaction with Reddit via ChatGPT. You can review the main chat that generated the results presented in this article using this link .

Open the menu on the bottom left side of the screen using the 3-dot button. Navigate to the "Settings and Beta" section, select "beta features," and turn on the toggle button for plugins.

Now, go to the plugin mode of ChatGPT, open the plugin store, and search for the Noteable plugin in the dropdown menu. Click the "install" button to navigate to a login page on Noteable's website , where you can either sign up for a new account or log in to your existing account.

After creating an account and logging in, you will be redirected to ChatGPT's page. Activate the Noteable plugin by checking the box next to it in the dropdown menu.

It's crucial to keep your API keys on Noteable. I highly recommend using this method instead of directly sharing your API keys through ChatGPT. By storing them as environment variables, you can access the keys programmatically without exposing the actual values in the code, making the process more secure.

This step involves creating two secret values required by the PRAW package, which we will name REDDIT_CLIENT_ID and REDDIT_SECRET_KEY. Start by going to the Noteable app’s dashboard . You can see the "Resources" section on the left side menu. Under this section, click on "Secrets." Then, click the "Create a secret" button.

In the "Name" field, enter a name, such as REDDIT_CLIENT_ID, and in the "Value" field, paste your client ID. Set visibility as private, and go through the same process for your secret key, naming it REDDIT_SECRET_KEY and entering the key that we obtained previously. Now, we are ready to move on to the main section of our work, where we will craft a prompt to extract data from Reddit.

Now, the fun part begins. In this section, I will show you how to structure a single prompt to yield your desired output in a streamlined manner. Your goal is to generate an Excel file containing 200 question titles and question bodies from a subreddit.

For this task, ChatGPT needs to retrieve the keys that we shared with Noteable (REDDIT_CLIENT_ID and REDDIT_SECRET_KEY), which you can get with the “os” module in Python .

We'll use the PRAW package, a Python wrapper for the Reddit API, to interact with Reddit and extract the required data. PRAW simplifies accessing Reddit's data by handling the connection and retrieval following Reddit's API rules. To create, manipulate, and save the extracted data into a DataFrame and subsequently into an Excel file, we ask ChatGPT to use the Pandas library and its dependencies.

Additionally, the prompt includes guidelines for managing active kernels. A 'kernel' in this context refers to an instance of a notebook's engine that runs the code. Managing kernels is important to ensure efficient use of resources in the Noteable workspace. This is relevant in a Noteable workspace where multiple computations or tasks might run simultaneously. When you reach the limit for active kernels, it's necessary to shut down a kernel to free up resources and ensure the smooth execution of tasks.

You also need to specify whether you want the latest or best-performing posts of the Subreddit. Then, define how you structure the spreadsheet, columns, and the data you extract.

To keep things simple, I suggest using the following columns:

Below is an example of a prompt that encompasses the above points. You can copy this prompt, replace the placeholders with your desired information, and paste it into the ChatGPT interface to initiate the data extraction process:

"Please retrieve {enter a number} of the {newest or hottest} posts from the {subreddit name} subreddit using the PRAW package (ensure PRAW is installed). For each post, extract the question title (name the column 'Question title'), question body (name the column 'Question body'), shortlink, upvote score, and number of comments. Once you've gathered this data, store it in a Pandas DataFrame and reset the index to start from 1 (instead of the default 0). Save the data to an Excel file named '{file-name} .xlsx.' Ensure the Excel file doesn't include an index column. After storing the data, provide a preview of the first three rows.

Import the 'os' module to access environment variables and retrieve the following values from the secrets I shared with Noteable:

You can shut down any kernel when you've reached the limit for active kernels."

This wraps up the data extraction segment of our project. After entering the prompt, ChatGPT will take a couple of minutes to complete the task. Although you can download the Excel file from your Noteable app's dashboard, this is optional to progress.

Here, you will learn how to direct ChatGPT to extract the most repeated 1-word, 2-word, and 3-word queries from the Excel file. This analysis provides insight into the most frequently used words within the analyzed subreddit, helping to uncover prevalent topics. The result will be an Excel sheet with three tabs, one for each query type.

In this prompt, we will instruct ChatGPT to read an Excel file, manipulate its data, and save the results in another Excel file using the Pandas library. For a more holistic and accurate analysis, combine the "Question Titles" and "Question Text" columns. This amalgamation provides a richer dataset for analysis.

The next step is to break down large chunks of text into individual words or sets of words, a process known as tokenization. The NLTK library can efficiently handle this.

Additionally, to ensure that the tokenization captures only meaningful words and excludes common words or punctuation, the prompt will include instructions to use NLTK tools like RegexpTokenizer and stopwords.

To enhance the filtering process, our prompt instructs ChatGPT to create a list of 50 supplementary stopwords, filtering out colloquial phrases or common expressions that might be prevalent in subreddit discussions but are not included in NLTK's stopwords. Additionally, if you wish to exclude specific words, you can manually create a list and include it in your prompt.

When you’ve cleaned the data, use the Counter class from the collections module to identify the most frequently occurring words or phrases. Save the findings in a new Excel file named "combined-queries.xlsx." This file will feature three distinct sheets: "One Word Queries," "Two Word Queries," and "Three Word Queries," each presenting the queries alongside their mention frequency.

Structuring the prompt ensures efficient data extraction, processing, and analysis, leveraging the most appropriate Python libraries for each phase.

Below is an example of a prompt that captures the abovementioned points. To utilize this prompt, simply copy and paste it into ChatGPT. It's essential to note that you don't need to adhere strictly to this prompt; feel free to modify it according to your specific needs.

"Let's extract the most repeated 1-word, 2-word, and 3-word queries from the Excel file named ' {file-name} .xlsx.' Use Python libraries like Pandas for data manipulation.

Start by reading the Excel file and combining the 'Question Titles' and 'Question Text' columns. Install and use the NLTK library and its necessary resources like Punkt for tokenization, ensuring that punctuation marks and other non-alphanumeric characters are filtered out during this process. Tokenize the combined text to generate one-word, two-word, and three-word queries.

Before we analyze the frequency, filter out common stop words using the NLTK library. In addition to the NLTK stopwords, incorporate an additional stopword list of 50 common auxiliary verbs, contractions, and colloquial phrases. This additional list should focus on phrases like 'I would,' 'I should,' 'I don't,' etc., and be used with the NLTK stopwords.

Once the data is cleaned, use the Counter class from the collections module to determine the most frequent one-word, two-word, and three-word queries.

Save the results in three separate sheets in a new Excel file called 'combined-queries.xlsx.' The sheets should be named 'One Word Queries,' 'Two Word Queries,' and 'Three Word Queries.' Each sheet should list the queries alongside the number of times they were mentioned on Reddit.

Show me the list of the top 5 queries and their count for each group in 3 tables."

When extracting data from many questions, consider requesting fewer keywords as output to expedite the process. For instance, if you've pulled data from 400 questions, you might ask ChatGPT to show you only the top 3 keywords. If you wish to view more keywords, simply download the file. This approach will reduce ChatGPT's processing time.
