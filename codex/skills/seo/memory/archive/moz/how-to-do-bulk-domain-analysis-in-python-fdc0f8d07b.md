---
source: https://moz.com/blog/bulk-domain-analysis-python
title: How to Do Bulk Domain Analysis in Python
scraped: 2026-03-23
published_on: 2023-06-05
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

# How to Do Bulk Domain Analysis in Python

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/bulk-domain-analysis-python
Published: 2023-06-05
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
How to Do Bulk Domain Analysis in Python

## Extracted Body
The purpose of this Jupyter Notebook is to introduce the Moz Links API using Python. This should work on any notebook hosting environment, such as Google Colab.

If you’re looking at this on Github, the code snippets can be copy/pasted into your own notebook environment. By the time you’ve run this script to the bottom, you will have used every Moz Links API endpoint, and can pick the parts you want for your own project. The official documentation can be found here .

Confused? Be sure to check out my intro to the Moz Links API .

The import statements at the top of a Python program are used to load external resources that are not loaded by default in the Python interpreter. These resources may include libraries or modules that provide additional functionality to the program.

Import statements are usually placed at the top of a program, before any other code is executed. This allows the program to load any necessary resources before they are needed in the program.

Once the resources have been loaded using import statements, they can be used anywhere in the program, not just in the cell where the import statement was written. This allows the program to access the functionality provided by the imported resources throughout its execution.

The libraries here not part of the standard Python library are requests and sqlitedict . You can install the with pip install requests and pip install sqlitedict in your terminal or a Jupyter cell. If you’re using Anaconda, requests is pre-installed.

The code below reads a file named “linksapi.txt” from the “assets” directory, which contains the login credentials, including the access ID and secret key needed to access the Moz API. These credentials are extracted from the file and assigned to two variables named ACCESSID and SECRETKEY . The with statement is used to ensure that the file is properly closed after it’s been read. Create a file whose contents look like this with your credentials manually retreived from moz.com:

Once the credentials are extracted from the file, they are stored in a tuple named AUTH_TUPLE. This tuple can be used as an argument to the Moz API functions to authenticate and authorize access to the data.

The purpose of this approach is to avoid hard-coding sensitive login credentials directly in the program, which could pose a security risk if the code was shared or published publicly. Instead, the credentials are kept in a separate file that is not included in the repository, and can be easily created and updated as needed. This way, the code can be shared without exposing the credentials to the public.

In this code, there are several configuration variables that are used to set up the API call to the Moz Links API.

The first variable, COMMON_ENDPOINT , is a constant that stores the endpoint URL for the Moz API. The second variable, sub_endpoint , is a string that represents the endpoint subpath for the anchor text data, which will be appended to the COMMON_ENDPOINT URL to form the complete API endpoint URL.

The fourth variable, data_dict , is a dictionary that contains the parameters for the API request. In this case, the data_dict specifies the target URL for which we want to retrieve anchor text data, the scope of the data (in this case, page-level), and a limit of 1 result.

Finally, the json_string variable is created by converting the data_dict dictionary into a JSON-formatted string using the json.dumps() function. This string will be used as the request body when making the API call.

These variables are used to configure and parameterize the API request, and can be modified to perform any data_dict request against any Moz Links API sub_endpoint .

In JupyterLab, the last line of a code cell is automatically printed to the output area without requiring an explicit print() statement. The code you provided is using the requests module to send a POST request to a URL url with data in the form of a JSON string json_string . The authentication details are passed using the AUTH_TUPLE variable.

After sending the request, the response object r is printed using the print() statement. This will print the HTTP status code, such as 200 for success, 404 for not found, etc., along with the response headers.

Finally, the .json() method is called on the response object response to parse the response data as JSON and return it as a Python dictionary. This dictionary can be assigned to a variable, used for further processing, or simply printed to the output area without requiring an explicit print() statement due to JupyterLab’s automatic printing behavior for the last line of a code cell.

This code defines a list of different sub-endpoints that can be appended to a common URL prefix to make different API endpoints. An API endpoint is a URL where an API can be accessed by clients. It is a point of entry to the application that acts as a gatekeeper between the client and the server. Each endpoint is identified by a unique URL, which can be used to interact with the API.

In this code, the list of sub-endpoints is defined in the sub_endpoints variable, and each endpoint is represented as a string. The for loop iterates over the list, prints the index number and name of each sub-endpoint using the print function, and increments the index by 1. The enumerate function is used to generate a sequence of pairs consisting of an index and a value from the list.

This code is useful for exploring the available endpoints for a particular API and for selecting the endpoint that corresponds to the desired functionality. By changing the sub-endpoint in the URL, clients can access different resources or perform different operations on the server.

This code defines two lists: names and descriptions . The names list contains human-friendly labels for the set of sub-endpoints, while the descriptions list provides a brief description of each endpoint. The two lists are kept in the same order as the points list defined earlier in the code.

By keeping the three lists in the same order, they can be “zipped” together into a single list of tuples using the zip function. This produces a new list where each tuple contains the name, endpoint, and description for a particular API endpoint. This makes it easy to display a user-friendly summary of each API endpoint with its name and description.

The zip function combines the elements of the three lists element-wise, creating a tuple of the first elements from each list, then a tuple of the second elements, and so on. The resulting list of tuples can be iterated over, and each tuple unpacked to access the individual name, endpoint, and description elements for each API endpoint.

This is a list of API requests in Python dict format, where each dictionary represents a request to a specific endpoint. Don’t hurt your brain too much trying to read it. Just know that I lifted each example from the original Moz documentation and listed them all here in order as nested Python dicts.

You could call the format is a dict of dicts, where each sub-dictionary corresponds to a specific endpoint, same order as the sub_endpoints , names , and descriptions lists for easy combining. The output of running the below cell is doing that list-combining to document every sub_endpoint .

If we’re going to hit an API over and over in mostly the same way, we want to spare ourselves re-typing everything all the time. That’s why we define functions. That’s the def in the below cell. Once that cell is run, the moz( ) function can be used anywhere in this Notebook. You need only feed it the sub_endpoint you want to use and a Python dict of your request. It will return the API’s response.

This does not output anything to the screen. It just defines the function.

The code uses a Python package called SqliteDict which provides a persistent dictionary-like object that can be stored on disk using the SQLite database engine. The with statement in the code sets up a context manager for the SqliteDict object, which automatically handles opening and closing the database connection. The database file is stored at ../dbs/linksapi.db

The code iterates through each sub-endpoint in the sub_endpoints list, and checks if that data has already been retrieved. If it hasn’t, the API is called using the moz() function and the result is saved in the SqliteDict. The db.commit() statement ensures that any changes made to the dictionary during the iteration are saved to the database.

The SqliteDict serves as a local cache to prevent the API from being hit every time the code block is run if the data has already been collected. By using this cache, the code reduces the number of API requests required, which is useful when working with APIs that have quota limits. Congratulations, you’re using a database!

This does not output anything to the screen. It saves the results of the API-calls to a local database.

This code uses the sqldict context manager to open the SQLite database containing the previously retrieved API data. It then iterates over the keys in the database, which correspond to the endpoints that were previously retrieved.

For each key, the code prints the endpoint name, description, and the data retrieved from the API. The pprint function is used to print the JSON data in a more human-readable format, with indentation and line breaks that make it easier to read.

In this Whiteboard Friday, learn about headless CMSs, the advantages of using them, and the differences in your approach to SEO.

Discover how I used AI copilots and the Moz API to turn marketing ideas into real tools. Learn how vibe coding lets any marketer build fast and smart.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.
