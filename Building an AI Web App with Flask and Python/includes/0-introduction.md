# Introduction

Imagine you're a professional Web developer and your client is a travel agency. In order to motivate its customers to stay in touch and share their travel experiences, the agency wants its Web site to include a service that translates road signs and billboards in real time. The customer, exploring a foreign land, snaps a picture of a sign she can't read, in a language she doesn't understand. She uploads the picture to the service, and it responds with a translation in her native language. No typing, no forms to fill out — just "Here's a picture, tell me what it says."

To meet the client's requests, the Web site must support the following features:
- Uploading of photos
- Extraction of text from these photos
- Translation of the extracted text into the user's native language

Just a few years ago, such a feature list would have been out of reach of most small businesses. Extracting text from photos and translating text into other languages is typically performed using machine learning and artificial intelligence (AI). Where would these capabilities come from? Today, these features and more are readily available in [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/). It's Microsoft's portfolio of more than 20 services and APIs designed to make AI and machine learning available to anyone who can lay down a few lines of code.

One of these services is the [Computer Vision API](https://azure.microsoft.com/services/cognitive-services/computer-vision/), which can not only extract text from photos, but also identify objects in photos, find faces in photos and predict their age and gender, and more. Another is the [Translator Text API](https://azure.microsoft.com/services/cognitive-services/translator-text-api/), which can translate text between dozens of the world's written languages.

Using these services, you will produce a Web site written in [Python](https://devblogs.microsoft.com/python/) — already among the world's most popular languages — and the [Flask](http://flask.pocoo.org/) framework for Python Web applications. This site will translate signage in photos, which is a feature your client can build upon to attract new customers and retain existing ones.

## Learning objectives

In this module, you build such an application step by step. First, you'll learn about the process of setting up your development system for all three of these components. Here, you'll use Microsoft's [Visual Studio Code](https://code.visualstudio.com/), which is available for Windows, macOS, and Linux. Then you'll build the functions that produce the pages that do what your client is looking for.

In this module, you will learn:
- How to set up your development environment
- How to deploy your application to Azure for customers to use
- How to produce a page that uploads photos to Azure
- How to produce a page that outputs the translation