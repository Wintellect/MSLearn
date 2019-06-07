# Create a site that supports photo uploads

In this unit, you will be producing very rudimentary HTML pages. They will not be styled or architected or use any sophisticated CSS. This is so you can focus on just the working mechanism of this application. (You're probably good enough with Web design that you can add the pretty things yourself.)

You'll see some structural elements of this Python + Flask app that may be novel to you, even if you've programmed in Python since its beginning. These elements deal with how Flask attributes Python functions to specific Web pages.

You will not need to use Azure Storage, or any other cloud-based file storage, for this unit. Azure Cognitive Services does include functions that look to the URL of a stored file. Setting up a Python application to be an authorized user of that file requires a significant number of steps, many of which involve cryptography, authentication, and secret keys. All this can be bypassed by sending the photo file directly to the application as a byte stream, using the session that Azure has already authenticated. So if you were preparing in your mind for several hours of wading through Active Directory credentials, relax — it's unnecessary.

## Download starter code for the Web site

A Web site begins with basic assets such as HTML, CSS, and images. Let's start by downloading a set of assets and getting a basic Web site up and running in Flask.

1. Create a directory on your hard disk in the location of your choice. This will be the *project directory* and will hold all of the files that comprise the Web site.

1. [Download a zip file](https://topcs.blob.core.windows.net/public/contoso-travel.zip) containing the assets for Contoso Travel and copy the contents of the zip file into the project directory you created in the previous step.

1. Take a moment to browse the files that you copied into the project directory. Verify that they include:

	- **app.py**, which holds the Python code that drives the site
	- **templates/index.html**, which contains the site's home page
	- **static/main.css**, which contains CSS to dress up the home page
	- **static/banner.jpg**, which contains the Web-site banner
	- **static/placeholder.jpg**, which contains a placeholder image for photos that have yet to be uploaded

	TODO: Describe app.py.

1. Open a Command Prompt or terminal and `cd` to the project directory.

1. If you are running Windows, execute the following command to create an environment variable named FLASK_ENV that tells Flask to run in development mode: 

	```
	set FLASK_ENV=development
	```

	If you are running Linux or macOS, use this command instead:

	```
	export FLASK_ENV=development
	```

	Running Flask in development mode is helpful when you're developing a Web site because Flask will automatically reload any files that change while the site is running. If you let Flask default to production mode and change the contents of an HTML file or other asset, you have to restart Flask to see the change in your browser.

1. Now use the following command to start Flask:

	```
	flask run
	```

1. Open a browser and navigate to http://localhost:5000. Confirm that the Web site appears in the browser as shown below.

	![Contoso Travel](media/initial-run.png)

	_Contoso Travel_

The page isn't functional yet. It doesn't support photo uploads, even though the user interface for doing so is in place. The next step, therefore, is to write some Python code that allows users to upload photos.

## Add code for uploading photos

In this exercise, you will modify **index.html** and **app.py** so users can upload photos to the Web site.

1. If Visual Studio Code isn't installed on your PC, go to https://code.visualstudio.com/ and install it now. Visual Studio Code is a free, lightweight source-code editor for Windows, macOS, and Linux. It features IntelliSense, integrated Git support, and much more.

1. Start Visual Studio Code and use the **File** > **Open Folder...** command to open the project directory containing the Web site.

1. Use Visual Studio Code's Explorer to open **index.html** in the "templates" folder. This is the Web site's home page, and the one that will be used to upload photos.

	![Opening index.html](media/open-index.png)

	_Opening index.html_

1. Paste the following code into **index.html** immediately before the closing `</body>` tag near the bottom of the file:

	```html
	<script type="text/javascript">
	    $(function() {
	        $("#upload-button").click(function() {
	            $("#upload-file").click();
	        });
	
	        $("#upload-file").change(function() {
	            $("#submit-button").click();
	        });
	    });
	</script>
	```

	TODO: Describe this code.

1. Open **app.py** in Visual Studio Code and replace its contents with the following statements:

	```python
	import base64
	from flask import Flask, render_template, request
	
	app = Flask(__name__)
	
	@app.route("/", methods=["GET", "POST"])
	def index():
	    if request.method == "POST":
	        # Display the image that was uploaded
	        image = request.files["file"]
	        uri = "data:image/jpg;base64," + base64.b64encode(image.read()).decode("utf-8")
	
	    else:
	        # Display a placeholder image
	        uri = "/static/placeholder.png"
	
	    return render_template("index.html", image_uri=uri)
	```

	TODO: Describe this code.

1. Return to **index.html** and find the `<img>` element on line 42. Replace `/static/placeholder.png` on that line with `{{ image_uri }}`. Here is the modified line:  

	```html
	<img id="uploaded-image" src="{{ image_uri }}">
	```

	TODO: Describe this code.

1. Save your changes.

TODO: Add closing.

## Test the result

TODO: Add intro.

1. Assuming Flask is still running in the project directory (if it's not, you can start it again with a `flask run` command), either refresh the page in your browser or open a new browser instance and navigate to http://localhost:5000.

1. Click the **Upload Photo** button and select a photo from your local file system.

1. Confirm that the photo you selected appears on the page:

	![Contoso Travel showing an uploaded photo](media/uploaded-photo.png)

	_Contoso Travel showing an uploaded photo_

You now have a basic Flask Web site running that accepts photo uploads. The next step is to add logic to extract text from the photos.






## What you're about to do

An API can be a convenient tool for interacting with a public cloud service, especially if everything you exchange with that service — on both the give and take side — is text. For the application you're building now, you're giving Azure an image that happens to depict text that an ordinary computer would not be able to read. You need Azure's AI to detect where that text is located, and what it might be saying in the user's native language.

An image file is an unusual order of beast. Python has many variable types, and is dynamic enough to know how to apportion a variable with the right type when you assign a value to it. But an image is not one of those types. The way an API or an SDK would have you pass an image to it, is by giving it an address on the Web where it can find that image. Now, you could make things easy on yourself by assuming your image is always uploaded to one location in, say, the company blog. But that's not easy on the user, who just wants to be able to point to an image and say, "Tell me what this says."

Azure has two ways of representing the "this" part of that instruction: as a file with a URL to which it may be granted access, or a stream fed directly to it by the application. Microsoft trains its image recognition algorithms using public files it finds out on the Web, and actually invites users to take part in the training process. But if your user is standing with her hands full of baggage at a foreign airport, or in a car parked on the shoulder while she tries to make sense of a street sign, she won't have the opportunity to check Wikipedia to see if it happens to already have a picture of what she's having trouble reading.

The most convenient way this application can work is if the image comes from the application itself. This way, the image can be stored locally — which, if you think about it, is where someone who just snapped this image would store it, not the cloud. Moreover, as it's using Azure functions during development and as it runs for customers in the public cloud, the application needs to use the same image handling functions in exactly the same way.

Here are the steps you'll take in this unit:
- Produce an HTML page that gathers input
- Declare the code's dependent libraries
- Add the code for authenticating to Cognitive Services

## Produce an HTML page that gathers input

If it's not started already, launch VS Code from the project directory using the code . method. Make sure you're logged onto Azure from the command prompt. If you're not logged on at the moment, enter this command:

```bash
az login
```

As before, your browser marshals the login process.

A straight HTML file can be very straightforward. For this application, you only need a few controls, which will be embedded in the index file for the Web site. You don't need any Flask templating yet, because we haven't collected the output yet for posting to the user. Here is **index.html**, the default page for the Web site, in its entirety:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Foreign road sign translator</title>
    </head>
    <body>
            <form name="transform" action="/process" method="POST" enctype=multipart/form-data>
                <p>Sign appears to be written in this language:
                    <select name="origlang" size="4">
                        <option value="unk" selected="selected">Unknown</option>
                        <option value="zh-Hant">Chinese (simplified)</option>
                        <option value="zh-Hans">Chinese (traditional)</option>     #*
                        <option value="en">English</option>     #* Originally supported language
                        <option value="fr">French</option>      #*
                        <option value="de">German</option>      #*
                        <option value="it">Italian</option>     #*
                        <option value="ja">Japanese</option>    #*
                        <option value="ko">Korean</option>      #*
                        <option value="pt">Portugese</option>   #*
                        <option value="es">Spanish</option>     #*     
                    </select></p>

                <p>Translate into this language:
                <select name="translang" size="12">
                    <option value="en" selected="selected">English</option>
                    <option value="zh-Hant">Chinese (simplified)</option>
                    <option value="zh-Hans">Chinese (traditional)</option> 
                    <option value="fr">French</option>
                    <option value="de">German</option>
                    <option value="it">Italian</option>
                    <option value="ja">Japanese</option>
                    <option value="ko">Korean</option>
                    <option value="pt">Portugese</option>
                    <option value="es">Spanish</option>
                </select></p>
 
                <p>Select the image that needs translating:</p>
            
                <input name="file" type="file" accept=".jpg, .jpeg, .png, .gif" placeholder="File input dialog">
                <input type="submit" value="Upload">
            </form>
    </body>
</html>
```

Here there are two list boxes: one called origlang representing the language that ComputerVision will be translating from (which may be left "Unknown"), the other called translang representing the language to translate to. For both of these list boxes, the value property of each option corresponds to a BCP-47 (Best Current Practice) language code that will be used by both the call to the API and the call to the SDK. There's a no-frills input file selector control which lets the user find the billboard image locally. By limiting the file types the selector will accept to JPEG, PNG, and GIF here in the HTML, a lot of work is spared in the Python logic making sure the image is an acceptable format.

(The languages shown here are among the earliest languages that Azure Cognitive Services supported. Other BCP-47 language codes are supported today, although for newer languages in Azure's repertoire than those listed here, results may be spotty.)

### Flask's interesting rendering rules

Without exception, every HTML page that you intend for Flask to render must be stored in the \templates directory of your project folder. This may seem unusual, especially if you're accustomed to the directory structure of your dev site corresponding to that of your production site. When Flask renders a template or an element of HTML code, it appears in the URL folder or subfolder whose name is associated with the Python function where the instruction for rendering that code appears.

That's not an easy concept to digest on first appearance, so let's break that down: There is always a function associated with the index.html file, which of course corresponds with the root of the site. Any rendering that takes place on account of instructions that appear in the Python function associated with **index.html** will always appear in the browser, in the root of the site.

Now, suppose you redirect control to a function associated with a page called **results.html**. You can name that function whatever you want in Python (not necessarily results). And you can associate it with a page with the same name or a different name — for example, result. When Flask renders the code in **results.html**, the browser will attach it to the subdirectory explicitly named in the code, whatever that is. So if it's result, the Address line of the browser will read /result at the end.

You'll see this principle in action later in this unit.

### Declare the code's dependent libraries

Next, you'll enter the preliminary instructions that link to the necessary libraries, and lay the groundwork for the application. Although you deployed the prototype for this application earlier to Azure as EverywhereASign, that's not the name Flask gives it. Just as a Web server looks to index.html as the default page for the site's core domain, the Flask framework looks a particular Python file in the root directory of the project as the default location for the site's Python logic.

If you're using the most recent version of Flask (and you should be), then that file is called **app.py**, which you should store in your root project folder. In the previous unit, you created a kind of placeholder **app.py** file. For this rather significant update, you'll replace it entirely with the sign reader source code. As you might expect, **app.py** begins with `import` statements:

```python
# -*- coding: utf-8 -*-

import os, json, requests, uuid
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException

from msrest.authentication import CognitiveServicesCredentials
```

It may seem odd that the first instruction should be phrased as a comment (preceded by a #), but it has a legitimate purpose here, instructing the Python interpreter that characters in the source code should be treated as Unicode UTF-8 variably encoded units. For now, this may be an overly cautious choice, but since this is a program that deals with foreign languages, you may in the future want to give yourself the freedom to add foreign character sets.

This application requires the following common Python libraries for these reasons:
- os provides calls made to the operating system. This application needs access to the environmental variables which you spent so much time setting up in the previous unit.
- json is necessary because Azure packages its multi-part responses with JSON code.
- requests is Python's main library for handling HTTP GET and POST operations, which you use when operating an API. The SDK method, which will also be demonstrated here, bypasses this more direct method of contacting the cloud.
- uuid is Python's library for assisting with Universally Unique Identifiers (UUID), which are used by the Cognitive Services API.

The main library that transforms Python into a Web language is flask (lower-case "f"), from which this application selectively imports the principal package Flask (upper-case "f"). To keep the application leaner and more robust, you can import just the extra Flask functions that it uses. Here, importing has been restricted to `render_template` which renders a designated HTML-based Flask template, and request which Flask uses to gather the data from HTML input controls.

Importing the ComputerVisionClient library enables the application to utilize the SDK. If you were to stick with just using the API to pass instructions to Azure using a POST request, you wouldn't need this library.

## Add code for authenticating to Cognitive Services

Flask changes the importance of functions in Python source code, for reasons which you'll see in just a bit. For now, the Flask library needs a handle for referring to the application itself, so that its symbols may be attached to it. As a standard more than a rule, Flask developers use the symbol app for this purpose, although you could just as easily choose some other variable. The following instruction in the header effectively makes your Python application into a Flash application:

```python
app = Flask(__name__)
```

Remember that `Flask` (capital "F") is the package you imported. It has an internal variable to represent the code, `__name__`, which this instruction assigns to the much less ostentatious symbol app. We'll come back to this symbol shortly.

For now, here is where all that hard work you did in the first unit with creating the environment variables, pays off. This next section is in the header of the source code, which means its variables will have global scope (available to all the functions), and its instructions will be executed first. First, the app retrieves the environment variables for authenticating to the Translator Text API, and sets the global variables for assembling an API call.

```python
# initialize all the Azure services

TTendpoint = os.environ["TEXTTRANS_ENDPOINT"]
TTaccesskey = os.environ["TEXTTRANS_KEY"]
TTpathend = "/translate?api-version=3.0"

TTheaders = {
    'Ocp-Apim-Subscription-Key': TTaccesskey,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
```

The URL that the API contacts is assigned to `TTendpoint`, and the secret authentication key from your Azure account is assigned to `TTaccesskey`. The `environ` method of Python's `os` library acts like a glossary: you give it the key, it returns the value. In this case, the key names come from the environment variable assignments. The tail end of the API call to Translator Text is always the same for each use, and is assigned to `TTpathend`.

The Python dictionary that's assigned to `TTheaders` are properties that the Translator Text API requires to execute the instruction. Notice `TTaccesskey` — this is where the API accepts your secret authentication key. As long as you're logged into Azure already, this key will be enough to get you API access. The `uuid.uuid4()` function generates a long, random session ID that Azure will use to log and trace your session.

The part that sets up the application to access the SDK (instructions that a phrased like Python instead of a jam-packed URL) looks somewhat different:

```python
CVendpoint = os.environ["CVISION_ENDPOINT"]
CVaccesskey = os.environ["CVISION_KEY"]

CVcredentials = CognitiveServicesCredentials(CVaccesskey)
CVclient = ComputerVisionClient(CVendpoint, CVcredentials)
```

Retrieving the environment variables works the same way, so there's no surprise there. Here, you have CVendpoint and CVaccesskey variables that are the counterparts of `TTendpoint` and `TTaccesskey`. But notice the authentication processes here are expressed as functions, acquired from the Computer Vision library. First the `CognitiveServicesCredentials()` function passes the secret key to Azure and grabs the credentials that authenticate the user. Those credentials are then passed on to `ComputerVisionClient()`, which is a function whose return value is an object. That object is assigned the symbol `CVclient`. For the remainder of the application, when you need to communicate with the Computer Vision SDK, you use this symbol as the root of the instruction.

You'll need a global variable to represent the name of a folder that will serve as a kind of "transporter room" for streaming the chosen file to Azure. So you'll add this statement:

```python
cachefolder = "filecache/"
```

The previous unit contained a placeholder `def index()` function which reported the value of an environment variable. For now, replace that function with one that's actually smaller and far simpler:

```python
@app.route("/")
def index():
    return render_template("index.html")
```

For most Web applications you'll ever produce, most of their logic and functionality will be on the back end. This application's **index.html** file contains only input controls, so there's really not much to do until the user clicks on the Submit button and the inputs can be read from those controls.
Flask amends Python's lexicon so that functions are attributed to specific pages. This function could have been named something other than `def index()`; it's that fact that it's attributed to the home route (the single backslash) with `@app.route("/")` is what makes this function answerable when the Web site launches. For now, all it needs to do is render the HTML code you entered earlier, and the Flask function `render_template()` accomplishes that.

In the next unit, you'll add the Flask functions that respond to the input, the Python functions that communicate with Azure Cognitive Services, and the Flask templates for rendering the output. Then you'll submit those additions as changes to the Git repository and deploy them to the Web.