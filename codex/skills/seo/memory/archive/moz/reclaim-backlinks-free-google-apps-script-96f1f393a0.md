---
source: https://moz.com/blog/link-reclamation
title: Reclaim Backlinks + Free Google Apps Script
scraped: 2026-03-23
published_on: 2024-01-31
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

# Reclaim Backlinks + Free Google Apps Script

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/link-reclamation
Published: 2024-01-31
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
Learn how Hunter recovered 66 lost backlinks in just 30 days. Find effective tactics for backlink reclamation and protect your SERP positions.

## Extracted Body
After analyzing our backlink profile, we discovered we lost nine percent (74 backlinks) of the backlinks we acquired in the last three years. With an average backlink acquisition cost of $320, we effectively lost over $24,000.

The most common reasons we lost backlinks included website owners removing the links or technical issues. We didn’t want to leave that on the table and decided to run a backlink reclamation campaign. Within 30 days, we reclaimed 31 backlinks worth $10,000.

In this article, I’ll show you how to create an automated backlink reclamation process that protects your investment and rankings in search engines.

After analyzing over 3,000 backlinks we acquired since 2020, we discovered the two most common reasons backlinks got lost:

While some links are lost for good, we knew we could re-acquire many with a simple email asking the editor for a favor.

The email approach also seemed best because that’s how we built most of these links in the first place.

Diagnose why the links are missing (removed link, removed page, or other technical issues.)

Find the contact information of the website owners or editors to reclaim lost links.

Schedule an email outreach campaign , including follow-up emails, asking the recipients to re-add the links to our website.

We tried a few tools for identifying lost backlinks but found them too complex or expensive for our use case, so we decided to build our own.

The idea was simple. Add all referring and target page URLs in a Google Sheet and build a custom Google Apps Script that checks whether our target page URL is live on the referring page URL.

Since I have zero coding experience, ChatGPT was the logical choice. One hour and two lattes later, I had a working script that automatically checks whether our backlinks are still live on the websites where we previously acquired links

Here are the steps for making the script analyze your backlink profile and identify lost backlinks:

Add a referring page URL in column A (the page that should contain a backlink).

Add a target page URL in column B (the page on your website).

The runtime depends on the number of rows. Once the script analyzes all pages, a new column with the status of the links (in our case, a column named "Lost?") will appear.

Remove all rows with the status "Exists." This will leave only lost backlinks.

Then, remove duplicates and irrelevant results before analyzing each page in detail. Although analyzing Domain Authority (DA) with Moz Link Explorer gives you a good idea about a website’s authority, it’s often not enough to decide whether it’s worth having a backlink from that domain. Try Moz Pro for free to speed up the backlink evaluation process.

Here are a few additional metrics you should take into account to have a clearer picture of domain quality:

Relevance : How relevant is the target website to your website?

Outgoing/incoming links ratio : Do they have more incoming than outgoing links?

Content quality : Is their content helpful, and does it satisfy the user’s intent?

This is a manual process, but it is worth the time investment as it maximizes the impact of your campaign by focusing on reclaiming high-quality and relevant backlinks only.

Next, create a new tab in your spreadsheet and build a matrix with all the metrics shared below.

Target domains that satisfy four or more of these metrics. You can ignore the rest, as those websites aren’t the most relevant fit or highest quality.

Identifying the right decision-makers and finding their email addresses is crucial to every cold email campaign. While we usually put much effort into this part of the process, with backlink reclamation, it’s a bit different. We were already in touch with decision-makers since we collaborated on link building in the past.

The first step was to validate the decision-makers' email addresses and ensure they still worked at the same company. Next, we added all the contact information to the spreadsheet and ran the Hunter for Sheets add-on to verify all the email addresses.

Most email addresses were still valid, so reaching out to these people was safe. To add an extra layer of security, we double-checked if these people still work at the company.

The fastest way is by finding people on LinkedIn and checking their Experience tab.

If your contact no longer works in the company, find an alternative contact with editorial power.

Start by searching the company's LinkedIn page. Click on the People filter and search through the job titles. In my experience, titles containing the words content , marketing , editor , or SEO are the best bets.

Once you identify the right person with the right seniority level in the company, use a tool like Hunter Email Finder to find a valid email address .

Sending emails to valid addresses is crucial to keep the bounce rates low. Bounce rates higher than two percent negatively affect email deliverability, meaning not all emails you send will reach the primary inbox.

Segmentation is vital in cold emails because it helps target and personalize them. After sending over 10,000 emails in the last three years, I have learned that the more you segment your lists, the higher your chances of success. Sure enough, this was the case in our link reclamation campaign.

Next, we segmented our list based on the reason our backlinks got lost, and it resulted in three main segments:

Reclamation: pages that exist but simply deleted our backlinks

We’d later tailor the email sequence based on the segment to keep it more personalized and relevant to the recipient.

When crafting the perfect cold email , the usual advice is to hyper-personalize email sequences. In this campaign, we decided to use a generic approach with minimal personalization apart from a few custom attributes.

The reason was that most people we contacted knew the context of our previous partnership, so spending time on personalization wasn’t necessary.

For people we contacted for the first time, we shared a bit of context by explaining that we had a partnership with their colleagues and would love to continue working with them.

The email copy differed slightly depending on the segment, but the amount of effort we put into personalization was the same.

Here is the email copy we sent to prospects who removed our links:

If we don’t hear from recipients after the entire sequence, we mark it in our database and find alternative people in the company to contact in 3 — 6 months.

Before giving up on the email, try reaching out on LinkedIn or X (formerly Twitter). This works exceptionally well for active prospects on these networks. If you don’t have a premium account, follow their profiles and engage with their content by adding genuine comments to their posts. After a few days, you can send a personalized connection request and continue discussing lost backlinks.

Follow-ups are essential in every cold email campaign. People receive dozens of similar emails daily, so there’s a huge chance your email will get lost in their inbox. That’s why you should always follow up after your first cold email.

Here are stats from our campaigns to prove the importance of follow-ups:

Our follow-up sequences account for over 50% of the responses.

We decided on a simplistic follow-up approach. Here's what it looked like:
