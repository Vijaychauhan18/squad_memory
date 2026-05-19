---
source: https://moz.com/blog/moz-links-api-introduction
title: The Moz API: An Introduction to SEO APIs
scraped: 2026-03-23
published_on: 2023-05-29
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

# The Moz API: An Introduction to SEO APIs

Source: Moz Blog
Homepage: https://moz.com/blog
Original URL: https://moz.com/blog/moz-links-api-introduction
Published: 2023-05-29
Strength: SEO education, beginner-to-advanced resources, brand/entity SEO, whiteboard-style explainers

## Summary
The Moz API: An Introduction

## Extracted Body
What exactly IS an API? They’re those things that you copy and paste long strange codes into Screaming Frog for links data on a Site Crawl, right?

I’m here to tell you there’s so much more to them than that – if you’re willing to take just a few little steps. But first, some basics.

API stands for “application programming interface”, and it’s just the way of… using a thing. Everything has an API. The web is a giant API that takes URLs as input and returns pages.

But special data services like the Moz API have their own set of rules. These rules vary from service to service and can be a major stumbling block for people taking the next step.

When Screaming Frog gives you the extra links columns in a crawl, it’s using the Moz API, but you can have this capability anywhere. For example, all that tedious manual stuff you do in spreadsheet environments can be automated from data-pull to formatting and emailing a report.

If you take this next step, you can be more efficient than your competitors, designing and delivering your own SEO services instead of relying upon, paying for, and being limited by the next proprietary product integration.

Most APIs you’ll encounter use the same data transport mechanism as the web. That means there’s a URL involved just like a website. Don’t get scared! It’s easier than you think. In many ways, using an API is just like using a website.

As with loading web pages, the request may be in one of two places: the URL itself, or in the body of the request. The URL is called the “endpoint” and the often invisibly submitted extra part of the request is called the “payload” or “data”. When the data is in the URL, it’s called a “query string” and indicates the “GET” method is used. You see this all the time when you search:

When the data of the request is hidden, it’s called a “POST” request. You see this when you submit a form on the web and the submitted data does not show on the URL. When you hit the back button after such a POST, browsers usually warn you against double-submits. The reason the POST method is often used is that you can fit a lot more in the request using the POST method than the GET method. URLs would get very long otherwise. The Moz API uses the POST method.

A web browser is what traditionally makes requests of websites for web pages. The browser is a type of software known as a client . Clients are what make requests of services. More than just browsers can make requests. The ability to make client web requests is often built into programming languages like Python, or can be broken out as a standalone tool. The most popular tools for making requests outside a browser are curl and wget .

We are discussing Python here. Python has a built-in library called URLLIB, but it’s designed to handle so many different types of requests that it’s a bit of a pain to use. There are other libraries that are more specialized for making requests of APIs. The most popular for Python is called requests . It’s so popular that it’s used for almost every Python API tutorial you’ll find on the web. So I will use it too. This is what “hitting” the Moz API looks like:

Given that everything was set up correctly (more on that soon), this will produce the following output:

This is JSON data. It's contained within the response object that was returned from the API. It’s not on the drive or in a file. It’s in memory. So long as it’s in memory, you can do stuff with it (often just saving it to a file).

If you wanted to grab a piece of data within such a response, you could refer to it like this:

This says: “Give me the first item in the results list, and then give me the external_pages value from that item.” The result would be 7162 .

NOTE: If you’re actually following along executing code, the above line won’t work alone. There’s a certain amount of setup we’ll do shortly, including installing the requests library and setting up a few variables. But this is the basic idea.

JSON stands for JavaScript Object Notation. It’s a way of representing data in a way that’s easy for humans to read and write. It’s also easy for computers to read and write. It’s a very common data format for APIs that has somewhat taken over the world since the older ways were too difficult for most people to use. Some people might call this part of the “restful” API movement, but the much more difficult XML format is also considered “restful” and everyone seems to have their own interpretation. Consequently, I find it best to just focus on JSON and how it gets in and out of Python.

I lied to you. I said that the data structure you were looking at above was JSON. Technically it’s really a Python dictionary or dict datatype object. It’s a special kind of object in Python that’s designed to hold key/value pairs. The keys are strings and the values can be any type of object. The keys are like the column names in a spreadsheet. The values are like the cells in the spreadsheet. In this way, you can think of a Python dict as a JSON object. For example here’s creating a dict in Python:

Pretty much the same thing, right? Look closely. Key-names and string values get double-quotes. Numbers don’t. These rules apply consistently between JSON and Python dicts. So as you might imagine, it’s easy for JSON data to flow in and out of Python. This is a great gift that has made modern API-work highly accessible to the beginner through a tool that has revolutionized the field of data science and is making inroads into marketing, Jupyter Notebooks .

But beware! As data flows between systems, it’s not uncommon for the data to subtly change. For example, the JSON data above might be converted to a string. Strings might look exactly like JSON, but they’re not. They’re just a bunch of characters. Sometimes you’ll hear it called “serializing”, or “flattening”. It’s a subtle point, but worth understanding as it will help with one of the largest stumbling blocks with the Moz (and most JSON) APIs.

Actual JSON or dict objects have their own little APIs for accessing the data inside of them. The ability to use these JSON and dict APIs goes away when the data is flattened into a string, but it will travel between systems more easily, and when it arrives at the other end, it will be “deserialized” and the API will come back on the other system.

This is the concept of portable, interoperable data. Back when it was called Electronic Data Interchange (or EDI), it was a very big deal. Then along came the web and then XML and then JSON and now it’s just a normal part of doing business.

If you’re in Python and you want to convert a dict to a flattened JSON string, you do the following:

This looks almost the same as the original dict, but if you look closely you can see that single-quotes are used around the entire thing. Another obvious difference is that you can line-wrap real structured data for readability without any ill effect. You can't do it so easily with strings. That’s why it’s presented all on one line in the above snippet.

Such stringifying processes are done when passing data between different systems because they are not always compatible. Normal text strings on the other hand are compatible with almost everything and can be passed on web-requests with ease. Such flattened strings of JSON data are frequently referred to as the request .

Now that you understand what the variable name json_string is telling you about its contents, you shouldn’t be surprised to see this is how we populate that variable:

This is one of my key discoveries in learning the Moz API. This is in common with countless other APIs out there but trips me up every time because it’s so much more convenient to work with structured dicts than flattened strings. However, most APIs expect the data to be a string for portability between systems, so we have to convert it at the last moment before the actual API-call occurs.

Now you may be wondering in that above example, what a dump is doing in the middle of the code. The json.dumps() function is called a “dumper” because it takes a Python object and dumps it into a string. The json.loads() function is called a “loader” because it takes a string and loads it into a Python object.

The reason for what appear to be singular and plural options are actually binary and string options. If your data is binary, you use json.load() and json.dump() . If your data is a string, you use json.loads() and json.dumps() . The s stands for string. Leaving the s off means binary.

Don’t let anybody tell you Python is perfect. It’s just that its rough edges are not excessively objectionable.

For those of you completely new to Python or programming in general, what we’re doing when we hit the API is called an assignment. The result of requests.post() is being assigned to the variable named response .

We are using the = sign to assign the value of the right side of the equation to the variable on the left side of the equation. The variable response is now a reference to the object that was returned from the API. Assignment is different from equality. The == sign is used for equality.

The requests library has a function called post() that takes 3 arguments. The first argument is the URL of the endpoint. The second argument is the data to send to the endpoint. The third argument is the authentication information to send to the endpoint.

You may notice that some of the arguments to the post() function have names. Names are set equal to values using the = sign. Here’s how Python functions get defined. The first argument is positional both because it comes first and also because there’s no keyword. Keyworded arguments come after position-dependent arguments. Trust me, it all makes sense after a while. We all start to think like Guido van Rossum.

The name in the above example is called a “keyword” and the values that come in on those locations are called “arguments”. Now arguments are assigned to variable names right in the function definition, so you can refer to either argument1 or argument2 anywhere inside this function. If you’d like to learn more about the rules of Python functions, you can read about them here .

Okay, so let’s let you do everything necessary for that success assured moment. We’ve been showing the basic request:

…but we haven’t shown everything that goes into it. Let’s do that now. If you’re following along and don’t have the requests library installed, you can do so with the following command from the same terminal environment from which you run Python:

Often times Jupyter will have the requests library installed already, but in case it doesn’t, you can install it with the following command from inside a Notebook cell:

And now we can put it all together. There’s only a few things here that are new. The most important is how we’re taking 2 different variables and combining them into a single variable called AUTH_TUPLE . You will have to get your own ACCESSID and SECRETKEY from the Moz.com website .

The API expects these two values to be passed as a Python data structure called a tuple . A tuple is a list of values that don’t change. I find it interesting that requests.post() expects flattened strings for the data parameter, but expects a tuple for the auth parameter. I suppose it makes sense, but these are the subtle things to understand when working with APIs.

Using all upper case for the AUTH_TUPLE variable is a convention many use in Python to indicate that the variable is a constant. It’s not a requirement, but it’s a good idea to follow conventions when you can.

You may notice that I didn’t use all uppercase for the endpoint variable. That’s because the anchor_text endpoint is not a constant. There are a number of different endpoints that can take its place depending on what sort of lookup we wanted to do. The choices are:

And that leads into the Jupyter Notebook that I prepared on this topic located here on Github . With this Notebook you can extend the example I gave here to any of the 12 available endpoints to create a variety of useful deliverables, which will be the subject of articles to follow.

In this Whiteboard Friday, learn about headless CMSs, the advantages of using them, and the differences in your approach to SEO.

Discover how I used AI copilots and the Moz API to turn marketing ideas into real tools. Learn how vibe coding lets any marketer build fast and smart.

The author's views are entirely their own (excluding the unlikely event of hypnosis) and may not always reflect the views of Moz.
