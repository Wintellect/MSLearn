# Create a site that supports photo uploads

Now that you have an environment for Python and Flask prepared, it's time to begin building a Web site. In this unit, you will create a Web site named "Contoso Travel." You will start with a page that's provided for you, and then add some code to allow users to upload photos to the page. Along the way, you'll learn the basics of how Flask Web apps are structured and how routes such as "http://contosotravel/upload" map to functions in your Python code.

## Flask fundamentals

Every Flask application begins with a file named **app.py**, which Flask automatically looks for when an application starts up. The following **app.py** file implements the simplest possible Web site — one with a single page that displays "Hello, world" to the user:

```python
from flask import Flask

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return "<h1>Hello, world</h1>"
```

The first statement imports a function named `Flask()` from the `flask` package installed with `pip`. The second statement calls that function to create a Flask app and assign it to the variable named `app`.

The fourth and fifth statements define a function that's called when the user requests the site's home page — for example, "http://www.contoso.com/." The preceding statement — `@app.route("/")` — maps the route ("/") to the function. The function name is unimportant, but `index` is commonly used as the name for the function that renders the site's home page.

### Routing in Flask

Suppose your Web site contains several pages rather than just one. You can use `@app.route()` to map all the routes that the site supports to functions that render the corresponding pages:

```python
from flask import Flask

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return "<h1>This the home page</h1>"

# Define a route for the app's About page
@app.route("/about")
def about():
    return "<h1>This the About page</h1>"

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return "<h1>This the Contact Us page</h1>"
``` 

If the app is hosted at www.contoso.com, it now supports the following URLs:

- www.contoso.com/
- www.contoso.com/about
- www.contoso.com/contact

You can continue adding routes and functions until the pages that your site supports are accessible by URL. Once more, the function names are unimportant. It's the routes that count.

### HTML templates

You typically don't want to include inline HTML in the functions that render your site's pages. Instead, you want to define those pages in HTML files.

Flask contains a function named `render_template()` that looks for HTML files in a subdirectory named "templates" and renders them out to the page. The following example produces the exact same output as the previous example. It assumes that the directory in which **app.py** is located has a subdirectory named "templates" containing HTML files named **index.html**, **about.html**, and **contact.html**:

```python
from flask import Flask, render_template()

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return render_template("index.html")

# Define a route for the app's About page
@app.route("/about")
def about():
    return render_template("about.html")

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return render_template("contact.html")
``` 

Why is the function named `render_template()`? Because it can do more than simply load static HTML files. It also allows allows you to pass it user-defined variables and inject their values into the page at run-time. You could, for example, place a file named **master.html** in the "templates" subdirectory and include the following markup in it:

```html
<h1>{{ message }}</h1>
```

You could then write **app.py** this way:

```python
from flask import Flask, render_template()

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return render_template("master.html", message="This is the home page")

# Define a route for the app's About page
@app.route("/about")
def about():
    return render_template("master.html", message="This is the About page")

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return render_template("master.html", message="This is the Contact Us page")
``` 

In effect, **master.html** becomes a template for output, and you customize the output for each page by passing a variable named `message` into the template and referencing that variable in the template using `{{ ... }}` expressions. For more information on using templates in Flask, see [Templates](http://flask.pocoo.org/docs/1.0/tutorial/templates/).

### Control-of-flow expressions

Expresions delimited by `{{` and `}}` aren't the only special ones that Flask supports. It also supports control-of-flow statements enclosed in `{%` and `%}` delimiters. For example, the following HTML template displays a default message in a page if the `message` variable isn't defined:

```html
{% if message %}
    <h1>This is a default message</h1>
{% else %}
	<h1>{{ message }}</h1>
{% endif %}
```

Expressions such as these can even be used to conditionally execute JavaScript code:

```html
{% if message %}
    <script type="language/javascript">
        window.alert("Error: No message specified");
    </script>
{% else %}
	<h1>{{ message }}</h1>
{% endif %}
```

Control-of-flow statements such as these are frequently used to display error messages passed to Flask's `flash()` function. For example, let's say you encounter an error condition in **app.py** and want to display a message to the user in a JavaScript alert box. Here's the code in **app.py**:

```python
from flask import flash

flash("This is an error message") 
``` 

You could then include the following statements in the corresponding HTML file to display the error message:

```html
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <script type="language/javascript">
            window.alert("{{ messages[0] }}");
        </script>
    {% endif %}
{% endwith %}
```

This example assumes that just one error message was flashed, but you can call `flash()` multiple times to queue up several messages and enumerate them with a `{% for message in messages %}` statement. For more information on message flashing in Flask, see [Message Flashing](http://flask.pocoo.org/docs/1.0/patterns/flashing/).

### Static files

Most Web sites contain images, style sheets, and other static files that don't change as the application executes. Flask looks for these files in a special subdirectory named "static."

TODO: Finish this section.

## Create the Contoso Travel Web site

A Web site begins with basic assets such as HTML, CSS, and images. Let's put the concepts that you've learned to work by downloading a set of assets and getting a basic Web site up and running in Flask.

1. Create a directory on your hard disk in the location of your choice. This will be the *project directory* and will hold all of the files that comprise the Web site.

1. [Download a zip file](https://topcs.blob.core.windows.net/public/contoso-travel.zip) containing the assets for Contoso Travel and copy the contents of the zip file into the project directory you created in the previous step.

1. Take a moment to browse the files that you copied into the project directory. Verify that they include:

	- **app.py**, which holds the Python code that drives the site
	- **templates/index.html**, which contains the site's home page
	- **static/main.css**, which contains CSS to dress up the home page
	- **static/banner.jpg**, which contains the Web-site banner
	- **static/placeholder.jpg**, which contains a placeholder image for photos that have yet to be uploaded

	Of these files, **app.py** is of particular significance. Here is what's in the file right now:

	```python
	from flask import Flask, render_template
	
	app = Flask(__name__)
	
	# Define route for the app's one and only page
	@app.route("/")
	def index():
	    return render_template("index.html")
	```

	The first statement imports a pair of functions from the Flask module you installed in the previous unit. The second statements invokes one of those functions to create an object named `app` representing the application.

	TODO: Complete this description.

1. Open a Command Prompt or terminal window and `cd` to the project directory.

1. If you are running Windows, execute the following command to create an environment variable named FLASK_ENV that tells Flask to run in development mode: 

	```
	set FLASK_ENV=development
	```

	If you are running Linux or macOS, use this command instead:

	```
	export FLASK_ENV=development
	```

	Running Flask in development mode is helpful when you're developing a Web site because Flask automatically reloads any files that change while the site is running. If you let Flask default to production mode and change the contents of an HTML file or other asset, you have to restart Flask to see the change in your browser.

1. Now use the following command to start Flask:

	```
	flask run
	```

1. Open a browser and navigate to http://localhost:5000. Confirm that the Web site appears in the browser as shown below.

	![Contoso Travel](media/initial-run.png)

	_Contoso Travel_

The page isn't functional yet. It doesn't support photo uploads, even though the user interface for doing so is in place. The next step, therefore, is to modify the site to allow users to upload photos.

## Add support for uploading photos

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

Finish up by saving your changes to **index.html** and **app.py**. It's time to see the results.

## Upload a photo

Let's make sure your changes have the desired effect by uploading a photo to the site.

1. Assuming Flask is still running in the project directory (if it's not, you can start it again with a `flask run` command), either refresh the page in your browser or open a new browser instance and navigate to http://localhost:5000.

1. Click the **Upload Photo** button and select a photo from your local file system.

1. Confirm that the photo you selected appears on the page:

	![Contoso Travel showing an uploaded photo](media/uploaded-photo.png)

	_Contoso Travel showing an uploaded photo_

You now have a basic Flask Web site running that accepts photo uploads. The next step is to modify the site to extract text from those photos.






## Extras

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