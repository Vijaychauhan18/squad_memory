---
source: https://dejan.ai/blog/ai-overviews-dialogflow-agent/
title: AI Overviews = Dialogflow Agent?
scraped: 2026-03-25
published_on: 2025-08-31
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

# AI Overviews = Dialogflow Agent?

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/ai-overviews-dialogflow-agent/
Published: 2025-08-31
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Joshua Squires shared one of the most interesting AI Overview leaks and for some reason it was mostly ignored by the SEO industry. I’d like to draw your attention to it today because it provides two key details framing AI Overviews as an implementation of Google’s Dialogflow agentic framework which is backed up with an […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Joshua Squires shared one of the most interesting AI Overview leaks and for some reason it was mostly ignored by the SEO industry. I’d like to draw your attention to it today because it provides two key details framing AI Overviews as an implementation of Google’s Dialogflow agentic framework which is backed up with an immense amount of documentation and technical detail.

I know these are pretty general concepts, but my intuition immediately drew me towards Dialogflow implementation.

What follow is taken directly from the implementation reference available here: https://cloud.google.com/dialogflow/es/docs/

When building an agent, it is most common to use the Dialogflow ES console ( visit documentation , open console ). The instructions below focus on using the console. To access intent data:

If you are building an agent using the API instead of the console, see the Intents reference . The API field names are similar to the console field names.

You can set a priority for each intent, which affects how it is matched .

In most cases, using the Normal priority is the best option. If there is a potential matching conflict between two intents, it is best to improve the training phrases to address the conflict. If you cannot remove the conflict with training phrases, you can use priorities to provide preference to one of the intents.

If the priority is Ignore , the intent is ignored in runtime detect intent requests.

When using the API, priorities are provided as integers. The larger the number, the greater the priority. If the priority is unset or equal to 0 , the value is converted to 500,000 . The following table shows the relationship between integer priorities and the console’s named priorities:

Dialogflow uses two algorithms to match intents: rule-based grammar matching and ML matching . Dialogflow simultaneously attempts both algorithms and chooses the best result.

The following table lists the pros and cons of these algorithms:

When searching for a matching intent, Dialogflow scores potential matches with an intent detection confidence , also known as the confidence score . These values range from 0.0 (completely uncertain) to 1.0 (completely certain). Without taking the other factors described in this document into account, once intents are scored, there are three possible outcomes:

You can set priorities for intents. When two or more intents match the same end-user expression with similar confidence scores, priority is used to select the best match. Otherwise, the confidence score for intent matching is more important than priority.

Knowledge connectors complement defined intents. They parse knowledge documents (for example, FAQs) to find information related to end-user expressions.

If a defined intent and a knowledge document are both potential matches, the match confidence of each and the knowledge results preference are used to determine which match is the selected match.

While contexts are active, Dialogflow is more likely to match intents that are configured with input contexts that correspond to the currently active contexts.

Here’s the complete discovery document: https://dialogflow.googleapis.com/$discovery/rest?version=v2beta1

Your email address will not be published. Required fields are marked *

Save my name, email, and website in this browser for the next time I comment.
