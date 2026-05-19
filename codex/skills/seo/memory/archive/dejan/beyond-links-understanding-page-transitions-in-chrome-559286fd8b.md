---
source: https://dejan.ai/blog/transitions/
title: Beyond Links: Understanding Page Transitions in Chrome
scraped: 2026-03-25
published_on: 2024-11-27
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

# Beyond Links: Understanding Page Transitions in Chrome

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/transitions/
Published: 2024-11-27
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
When SEOs think about user behavior, the conversation often revolves around clicks, links, and conversions. But in Chrome, there’s an underlying layer of data that tells a much richer story—page transitions. These are the bread and butter of how users navigate, revealing not just where they go, but how they got there. For SEOs, understanding […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

When SEOs think about user behavior, the conversation often revolves around clicks, links, and conversions. But in Chrome, there’s an underlying layer of data that tells a much richer story— page transitions . These are the bread and butter of how users navigate, revealing not just where they go, but how they got there.

For SEOs, understanding these transitions opens up new insights into intent, usability, and the real pathways users take beyond the usual attribution models.

Page transitions in Chrome describe the types of navigational actions that users perform. Think of them as Chrome’s version of “user intent signals,” baked directly into how the browser logs movement from one page to another. These transitions are meticulously categorized into core types and qualifiers , offering a granular view of the motivations behind visits.

This data, when correlated with SERP performance or site analytics, can redefine how you interpret user journeys.

Here’s a breakdown of the core transition types, each with SEO implications:

Qualifiers refine these transitions, offering more detail. For instance:

Note: Article edited for clarity and accuracy based on reader comments.

https://source.chromium.org/chromium/chromium/src/+/main:ui/base/page_transition_types.h

Very interesting Dejan! Could you shine some light on how you capture this data from Chrome/Chromium?

Certainly, for me this data is stored in: C:\Users\dejan\AppData\Local\Google\Chrome\User Data\Profile 1 folder. Yours will be slightly different based on your computer user and profile number in Chrome. One example is an sqlite database file called: “C:\Users\dejan\Desktop\chrome hacking\User 1\History” this is not a folder but a file.

import streamlit as st import sqlite3 import csv from io import StringIO import math import pandas as pd import os

# Get list of valid database files in the directory base_dir = r'C:\Users\dejan\Desktop\chrome hacking\User 1' db_files = [ file for file in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, file)) and not file.endswith('-journal') and f"{file}-journal" in os.listdir(base_dir) ]

# Let user select the database file selected_db = st.selectbox("Select Database File", db_files)

if selected_db: db_path = os.path.join(base_dir, selected_db) st.write(f"Selected Database: **{selected_db}**")

# Connect to the SQLite database conn = sqlite3.connect(db_path) cursor = conn.cursor()

# Get list of tables in the database tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall() tables = [table[0] for table in tables]

# Display a summary table showing the number of records in each table summary_data = [] for table in tables: count = cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] summary_data.append({"Table Name": table, "Record Count": count})

summary_df = pd.DataFrame(summary_data) st.write("**Summary of Tables:**") st.dataframe(summary_df)

# Select table selected_table = st.selectbox("Select Table", tables)

if selected_table: # Fetch and display schema for selected table schema = cursor.execute(f"PRAGMA table_info({selected_table});").fetchall() st.write(f"Schema for {selected_table} table:") st.write(schema)

# Display summary for the selected table column_summary = [] for col in schema: col_name = col[1] non_null_count = cursor.execute(f"SELECT COUNT({col_name}) FROM {selected_table} WHERE {col_name} IS NOT NULL").fetchone()[0] column_summary.append({"Column Name": col_name, "Non-Null Count": non_null_count})

column_summary_df = pd.DataFrame(column_summary) st.write(f"**Summary for {selected_table} table:**") st.dataframe(column_summary_df)

# User input for search query search_query = st.text_input("Search by text")

# Modify SQL query based on search input query = f"SELECT * FROM {selected_table}" if search_query: columns = [col[1] for col in schema] search_conditions = " OR ".join([f"{col} LIKE '%{search_query}%'" for col in columns]) query += f" WHERE {search_conditions}"

# Pagination settings page_size = 100 total_records = len(data) total_pages = math.ceil(total_records / page_size) page_number = st.number_input("Page number", min_value=1, max_value=total_pages, value=1) start_index = (page_number - 1) * page_size end_index = min(start_index + page_size, total_records)

# Add button to download table data as CSV if st.button("Download Table as CSV"): csv_data = StringIO() csv_writer = csv.writer(csv_data) csv_writer.writerow([i[0] for i in cursor.description]) # Write headers csv_writer.writerows(data) # Write data rows csv_data.seek(0) csv_bytes = csv_data.getvalue().encode() st.download_button(label='Download CSV', data=csv_bytes, file_name=f'{selected_table}.csv', mime='text/csv')

# Add button to delete table if st.button("Delete Table"): cursor.execute(f"DROP TABLE IF EXISTS {selected_table};") conn.commit() st.success(f"Table '{selected_table}' deleted successfully.")

# Add button to empty table if st.button("Empty Table"): cursor.execute(f"DELETE FROM {selected_table};") conn.commit() st.success(f"Table '{selected_table}' emptied successfully.")

PS: I recommend you copy the content of that whole folder to a separate location before you attempt loading it to prevent database locked message. Or deleting your history and breaking Chrome.

Curious to know if you’ve looked at if Google could by sending this data across user sessions with Chrome Sync? Doing so could help with their conversion tracking for paid ads.

Hi, very interesting article, that shows which signals may be used by Google. That said, how can this be a “treasure trove of insights” since we can’t access the page transition datas from users ?

Valid point! It’s a treasure trove of insights for Google. I’ve edited the article to avoid suggesting we can get hold of this data (other than our own). Thank you.
