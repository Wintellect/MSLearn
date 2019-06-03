# Introduction

Imagine you're a professional Web developer and your client is a travel agency. It wants its customers to have good reason to stay in touch and share their travel experiences. So the agency wants its website to include a number of useful services, some of which require artificiala dose of intelligence (AI).

One service in particular helps the travel agency's customers translate road signs and billboards in real time. The customer, exploring a foreign land, snaps a picture of a sign she can't read, in a language she can't translate. She sends the picture to the service, and it responds with a translation in her native language. No typing, no forms to fill out — just “Here's a picture, tell me what it says.”

To meet the client's requests, your Web site will need to accommodate the following features:
- Uploading of photos
- Extraction of text from these photos
- Translation of the extracted text into the user's native language
- Optional translation into any other language the user may choose

Just a few years ago, such a feature list would never have been considered by a small business for its own Web site. Where would it get the artificial intelligence functions it needs? Today, those functions are readily available in [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/). It's Microsoft's portfolio of more than 20 services, each with its own API, designed to make AI and machine learning available to businesses of all kinds.

One of these services is the [Computer Vision API](https://azure.microsoft.com/services/cognitive-services/computer-vision/), which can not only extract text but also make a pretty solid guess as to the identity of an object in a photo, or the relative age of a person in a photo judging from his face alone. The [Translator Text API](https://azure.microsoft.com/services/cognitive-services/translator-text-api/) recognizes dozens of the world's written languages.
Using these services, you'll be able to produce a Web site with [Python](https://devblogs.microsoft.com/python/) — already among the world's most popular languages — and the [Flask framework](http://flask.pocoo.org/) for Python Web applications. This site will be capable of translating signage in photos, which is a feature your client can build upon to attract new customers and retain existing ones.

## The tools you will use

Most Web applications you've encountered likely were produced with snippets of JavaScript code embedded inside HTML, and executed by the client-side Web browser. You're about to see – and learn to create – a Web application   that works the opposite way.  In this newer scheme, Python provides the application's structure, assisted by the Flask framework.

### Python

If you've used Python  for any length of time, perhaps you've come to appreciate how uniquely optimized the language is, for the sake of its interpreter. Its symbology is intentionally short and understated. For example, indentation, which for other languages is purely optional or decorative, in Python specifies which instructions belong to what clause. There is no “end loop” or “close brackets” statement in Python; the next line without the same indentation as the last one, closes out the last clause. Entire algorithms can be specified in a single instruction. Instructions are condensed, potent, and unambiguous. By comparison, fitting Web pages with JavaScript can feel like following very explicit instructions for systematically reconstructing an unmade bed.

### Flask

Flask does two things. First, it amends Python by illuminating the structure of a Web site, enabling Python to attach itself to its pages and functions without having to be wedged between the tags and blank spaces in the markup code. Second, it operates as a local Web server for the purposes of developing the Web site around the functions it will provide.

This is what distinguishes development with Python and Flask from HTML and JavaScript: First you build the logic and functionality for the services your customers and your users will need and enjoy. Then you let that logic produce the HTML markup code that browsers will need to make that functionality useful. HTML is the product of your code, rather than the scaffolding upon which it precariously perches. You're not trapped by layout, sequence, and compartmentalization. Instead, you make HTML mind you.

### Azure Cognitive Services

The idea that you can cobble together in a few days' time an application that reads and translates the contents of a foreign billboard, is feasible today thanks to the public cloud. Azure exposes the “engines” of artificial intelligence to you, so you can supply the “chassis” that completes the machine and makes work happen. Azure Cognitive Services expects inputs in a certain fashion, and produces output in a specific format. Thankfully, Python already has libraries that take care of that formatting, so that you're not spending more than half your code parsing commas and spaces.

Because Flask enables Python to define the structure of your Web application, you can call an Azure public cloud function with the same style of logic as you would use for a classic desktop application. The syntax is different, as you might expect, but the procedure is more rational and more natural.

Azure Cognitive Services includes a function that isolates and spells out the text included in an image, and another function that translates text from one language to another. So you don't have to be an AI programmer yourself to build a Web application that meets your client's demands.

## Learning objectives

In this module, you'll see how to build such an application, step-by-step. First, you'll learn about the process of setting up your development system for all three of these components. Here, you'll use Microsoft's [Visual Studio Code](https://code.visualstudio.com/), which is available for Windows, macOS, and Linux. Then you'll build the functions that produce the pages that do what your client is looking for.

In this module, you will learn:
- How to set up your development environment
- How to deploy your application to Azure for customers to use
- How to produce a page that uploads photos to Azure
- How to produce a page that outputs the translation