---
source: https://www.searchenginejournal.com/googles-ucp-update-carts-catalogs-and-loyalty-in-ai-shopping/571496/
title: Google’s UCP Update: Carts, Catalogs, And Loyalty In AI Shopping
scraped: 2026-05-11
tags: elite_article, seo, search-engine-journal, article_snapshot
topic: seo_article
intent: research, synthesis, source_selection
role: researcher, seo, pinchy
confidence: medium
canonical: false
canonical_group: Elite article harvest
use_for: article-level context, synthesis, deeper retrieval
avoid_for: exact verbatim quoting
---

# Google’s UCP Update: Carts, Catalogs, And Loyalty In AI Shopping

Source expert/publication: search-engine-journal
Source homepage: https://www.searchenginejournal.com/
Original URL: https://www.searchenginejournal.com/googles-ucp-update-carts-catalogs-and-loyalty-in-ai-shopping/571496/
Published: 2026-05-10

## Why This Matters
The latest UCP updates signal a shift from experimentation to readiness as AI-driven commerce infrastructure becomes embedded in existing retail systems. The post Google’s UCP Update: Carts, Catalogs, And Loyalty In AI Shopping appeared first on Search Engine Journal .

## Extracted Article Passages
- UCP is evolving from concept to infrastructure, with new capabilities that enable multi-item purchases, live inventory checks, and loyalty-aware transactions.
- Google’s Universal Commerce Protocol can now handle shopping carts, live catalog queries, and loyalty program benefits for AI agent transactions. On March 19, Google announced three new UCP capabilities and a simplified onboarding path through Merchant Center, two months after Google and Shopify unveiled UCP at the National Retail Federation conference in January 2026.
- The January launch had a big coalition (Mastercard, Visa, Walmart, Target, Best Buy) but limited functionality. UCP could handle single-item checkout sessions and not much else. The March update closes the gap between UCP’s ambition and UCP’s practical capability.
- I covered UCP in depth in Selling to AI: The Complete Guide to Agentic Commerce , where I compared UCP to OpenAI and Stripe’s Agentic Commerce Protocol (ACP) . This article covers what changed in March and what the changes mean for retailers.
- Cart. UCP’s new Cart capability lets AI agents add multiple items to a shopping cart from a single retailer in one operation. Until March 2026, UCP only supported single-item checkout sessions , meaning an agent buying three products from one store needed three separate transactions. The Cart capability also supports pre-purchase exploration: agents can build baskets before a shopper commits, then convert the basket to a checkout session when the shopper is ready. UCP Cart is currently published as a draft specification.
- Catalog. UCP’s new Catalog capability lets agents query real-time product details directly from a retailer’s inventory, including variants, pricing, and stock levels. The difference between Catalog and existing Google Shopping product feeds: product feeds are static snapshots updated periodically, while Catalog provides live data at the moment of the query. An agent using Catalog can check whether a specific size is in stock before presenting the product to a shopper. UCP Catalog is also a draft specification.
- Identity Linking. UCP’s Identity Linking capability lets shoppers connect retailer accounts to UCP-integrated platforms using OAuth 2.0. When a shopper with a Nike membership buys through Google AI Mode, Identity Linking carries over that shopper’s member pricing, discounts, and free shipping. Without Identity Linking, shopping through an AI agent means losing the loyalty benefits a shopper would get when logged into the retailer’s website directly. Identity Linking is the only capability in this update already in UCP’s stable release rather than draft.
- Google is building a simplified UCP onboarding process directly in Merchant Center, targeting retailers who don’t have engineering teams to implement a protocol from scratch. Google says the Merchant Center UCP rollout will happen “over the coming months.”
- One concrete detail: products using the native_commerce product attribute will display a checkout button in Google AI Mode and the Gemini app. For retailers already managing product feeds through Google Merchant Center, UCP onboarding should be a settings change rather than an integration project.
- Commerce Inc, Salesforce, and Stripe will implement UCP on their platforms, with Google describing the timeline as “in the near future.” Retailers on Commerce Inc, Salesforce, or Stripe won’t need to implement UCP directly. The platform handles the protocol layer, similar to how Shopify’s Agentic Storefronts already abstract away multi-protocol complexity for Shopify merchants.
- Salesforce’s dual-protocol position is notable. Salesforce announced ACP support in October 2025. With UCP support coming too, Salesforce Commerce Cloud merchants will be able to serve both protocols from a single platform , reaching AI agents on ChatGPT (via ACP) and Google AI Mode (via UCP) without separate integrations.
- Stripe occupies an even more central position. Stripe co-created ACP with OpenAI and is now implementing UCP as well. Stripe is becoming the shared payment layer across both competing agentic commerce protocols.
- UCP’s January announcement was a statement of intent. UCP’s March update is a statement of readiness. Three things stand out:
- UCP is reaching feature parity with ACP. OpenAI and Stripe’s Agentic Commerce Protocol launched in September 2025 with cart management and catalog access built in from day one. UCP launched in January 2026 without either capability. Cart, Catalog, and Identity Linking close that gap, giving UCP the core primitives AI shopping agents need to handle multi-item, loyalty-aware transactions.
- Google’s onboarding play targets mass adoption, not enterprise showcases. Google wants millions of Merchant Center retailers on UCP, not just the enterprise brands (Walmart, Target, Best Buy) that endorsed UCP at NRF. Merchant Center integration is how Google reaches that scale. A retailer managing Google Shopping feeds today could become UCP-enabled without writing a line of code.
- Identity Linking is UCP’s clearest differentiator over ACP. Neither ACP nor any other agentic commerce protocol offers an equivalent to Identity Linking. Identity Linking solves a specific adoption barrier: shoppers lose loyalty pricing, member discounts, and free shipping when buying through an AI agent instead of logging into a retailer’s website directly. Removing that friction makes agentic commerce more attractive to both retailers protecting their loyalty programs and shoppers unwilling to give up membership benefits.

## Retrieval Use
- Use when the task maps to `search-engine-journal` or overlaps with the article title.
- Prefer this note over the source snapshot when you need article-level detail.

