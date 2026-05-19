---
source: https://dejan.ai/blog/how-ai-mode-selects-snippets/
title: How AI Mode Selects Snippets
scraped: 2026-03-25
published_on: 2025-05-28
tags: live_feed, phase1_ingest, dejan, practitioner, reverse-engineering, grounding, archive_backfill, historical_source
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Archive backfill - DEJAN / Dan Petrovic
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# How AI Mode Selects Snippets

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/how-ai-mode-selects-snippets/
Published: 2025-05-28
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
I noticed out commented out bits in the source code of the AI Mode results. They contain actual snippets supplied to Gemini to form the response. This is not what is displayed to the user. It’s what search tool supplies to Gemini which then renders the response to the user. This is kind of a […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

This is not what is displayed to the user. It’s what search tool supplies to Gemini which then renders the response to the user. This is kind of a big deal becauise this selection process dictates how AI Mode will treat the search result (e.g. your website!)

What I found super-interesting is the snippet text selection logic.

You have a page with 200-800 words on it and Google picks max 160 chars out of that seemingly at random.

This one I can understand, a central piece of content that clearly states the page and service:

After analyzing multiple websites and their corresponding Google AI mode snippets, clear patterns have emerged in how Google selects content to display in these snippets. This summary outlines the key findings and provides insights into the likely selection criteria.

The selection process appears to involve a sophisticated multi-factor algorithm rather than simple rule-based extraction:

For website owners and SEO professionals, these findings suggest several strategies to influence Google AI mode snippets:

The selection process show Google’s understanding of content relevance and value, going far beyond simple text extraction to identify the most meaningful and useful content for users.

Title: Custom Soccer Jerseys for Teams | No Minimum Order – FastPrintStar

Snippet: FastPrintStar Make the Best Customized Soccer Jersey for You! * No MOQ. Enjoy the convenience of flexible ordering options that allow you to customize soccer je…

2. Title: Custom Soccer Jerseys for Teams | No Minimum Order

Snippet: The material is both durable and comfortable, perfect for intense matches. Plus, the fit is perfect for all our players. Highly recommend FastPrintStar for anyo…

URL: https://fastprintstar.com/custom-soccer-jerseys/#:~:text=The%20quality%20is%20top%2Dnotch,to%20buy%20custom%20soccer%20jerseys!%22

3. Title: Custom Soccer Jerseys for Teams | No Minimum Order – FastPrintStar

Snippet: Standout Qualities of Our Custom Jerseys Soccer. Looking for a reliable custom soccer jersey maker that delivers both quality and style? At FastPrintStar, we sp…

URL: https://fastprintstar.com/custom-soccer-jerseys/#:~:text=FastPrintStar%20Make%20the%20Best%20Customized,your%20own%20soccer%20jersey%20today!

4. Title: Custom Soccer Jerseys for Teams | No Minimum Order

Snippet: FastPrintStar Make the Best Customized Soccer Jersey for You! At FastPrintStar, we take pride in becoming your best maker to create custom soccer jerseys cheap …

URL: https://fastprintstar.com/custom-soccer-jerseys/#:~:text=FastPrintStar%20Make%20the%20Best%20Customized,Quick%20Turnaround

5. Title: Custom Soccer Jerseys for Teams | No Minimum Order – FastPrintStar

6. Title: Lightspeed Jerseys: Custom Athletic Shirts & Custom Soccer …

Snippet: Fast Turnaround. Most fully sublimated items are printed and shipped in just 7-10 business days.

URL: https://lightspeedjerseys.com/#:~:text=Fast%20Turnaround,just%207%2D10%20business%20days

7. Title: Shirt Designs, Team Shirts and Custom Soccer Jerseys

Snippet: Order attractive, durable, move-with-you personalized and custom decorated soccer T-shirts and custom soccer jerseys from Broken Arrow T-Shirt Printing and Embr…

URL: https://www.brokenarrowwear.com/catalog/athletics/soccer.html

Snippet: Custom One Online is dedicated to providing teams and fans with the highest-quality custom soccer clothing and soccer jerseys personalized to reflect their team…

URL: https://customoneonline.com/pages/jerseys-for-soccer#:~:text=Custom%20One%20Online%20is%20dedicated,style%2C%20comfort%2C%20and%20performance.

10. Title: Design Custom Soccer Uniforms & Jerseys | VistaPrint

Snippet: Bring your team colors to life with personalized soccer jerseys and kits. * A matching look for your team. Whether you’re looking for designer football shirts f…

URL: https://www.vistaprint.com/clothing-bags/teamwear/soccer#:~:text=Unlimited%20customization%20included,new%20team%20members%20and%20players.

11. Title: Shirt Designs, Team Shirts and Custom Soccer Jerseys

Snippet: High Quality Affordable Custom Softball Uniforms and Warm-Ups. Let Broken Arrow T-Shirt Printing and Embroidery customize your soccer uniforms and we will guara…

URL: https://www.brokenarrowwear.com/catalog/athletics/soccer.html#:~:text=High%20Quality%20Affordable%20Custom%20Softball,a%20free%20quote%20in%20minutes!

12. Title: Custom Jerseys – Create Personalized Team Uniforms Online

Snippet: Custom Ink’s Frequently Asked Questions * How do I make customized team jerseys? Creating custom team jerseys online is easy with Custom Ink. Custom Ink offers …

13. Title: Lightspeed Jerseys: Custom Athletic Shirts & Custom Soccer Jerseys

Snippet: Free Names & Numbers Each player can have their own custom item at no additional cost.

URL: https://lightspeedjerseys.com/#:~:text=Free%20Names%20%26%20Numbers,item%20at%20no%20additional%20cost.

14. Title: Custom Soccer Jerseys – Your Design, Team and Number

Snippet: owayo manufactures custom soccer jerseys, shirts and team uniforms of professional quality. Your soccer jerseys are created according to your exact specificatio…

15. Title: Custom Any Name Number 2023-24 FC Kids Soccer Jersey …

Snippet: Report this review. … My son saved up his money to order himself this customized jersey. He loves it and everyone thinks it’s so cool that he has his own name…

URL: https://www.amazon.com/Custom-2023-24-Personalized-Football-Uniforms/dp/B0CN996Y2B#:~:text=Customers%20are%20satisfied%20with%20the,quality…%22%20Read%20more

Snippet: I would recommend this to everyone. … I ordered this full custom soccer uniform for my college sports. It came out to be amazing in quality and the overall lo…

URL: https://www.apparelnbags.com/soccer-team-uniforms/custom-soccer-jersey/product-reviews.htm#:~:text=I%20would%20recommend%20this%20to%20everyone.

17. Title: Custom Soccer Jerseys | Custom Soccer Uniforms – Wooter Apparel
