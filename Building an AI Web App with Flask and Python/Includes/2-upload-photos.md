# Create a site that supports photo uploads

Now that you have an environment for Python and Flask prepared, it's time to begin building a Web site. In this unit, you will create a Web site named "Contoso Travel." You will start with a page that's provided for you, and then add some code to allow users to upload photos to the page. Along the way, you'll learn the basics of how Flask Web apps are structured and how routes such as "http://www.contoso.com/upload" map to functions in your Python code.

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

Expresions delimited by `{{` and `}}` aren't the only special ones that Flask supports. It also supports control-of-flow statements enclosed in `{%` and `%}`. For example, the following HTML template displays a default message in a page if the `message` variable isn't defined:

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

Let's say your site includes a style sheet named **main.css** and a banner named **banner.jpg**. You can drop these files into the "static" subdirectory and reference them in HTML this way:

```html
<link rel="stylesheet" href="/static/main.css">
<img src="/static/banner.jpg">
```

You can also use Flask's `url_for()` function to resolve these URLs:

```html
<link rel="stylesheet" href="url_for('static', filename='main.css')">
<img src="url_for('static', filename='banner.jpg')">
```

One benefit of using `url_for()` is that the file names themselves can be variables, which is useful when building dynamic Web sites.

TODO: Explain this further.

## Create the Contoso Travel Web site

A Web site begins with basic assets such as HTML, CSS, and images. Let's put the concepts that you've learned thus far to work by downloading a set of assets and getting a basic Web site up and running in Flask.

1. Create a directory on your hard disk in the location of your choice. This will be the *project directory* and will hold all of the files that comprise the Web site.

1. [Download a zip file](https://topcs.blob.core.windows.net/public/contoso-travel.zip) containing the assets for Contoso Travel and copy the contents of the zip file into the project directory you created in the previous step.

1. Take a moment to browse the files that you copied into the project directory. Verify that they include:

	- **app.py**, which holds the Python code that drives the site
	- **templates/index.html**, which contains the site's home page
	- **static/main.css**, which contains CSS to dress up the home page
	- **static/banner.jpg**, which contains the Web-site banner
	- **static/placeholder.jpg**, which contains a placeholder image for photos that have yet to be uploaded

	Of these files, **app.py** is of particular significance. Here's what's in it right now:

	```python
	from flask import Flask, render_template
	
	app = Flask(__name__)
	
	# Define route for the app's one and only page
	@app.route("/")
	def index():
	    return render_template("index.html")
	```

	Currently, the app consists of a single page named **index.html** located in the "templates" subdirectory. **index.html** doesn't contain any special expressions at the moment — it is simply a static file — but that will change as you further develop the site. **index.html** loads the popular [Bootstrap](https://getbootstrap.com/) framework and uses it to make the page responsive. It also loads **main.css** from the "static" subdirectory and uses the CSS styles defined there to lend the page a professional appearance.

1. Open a Command Prompt window or terminal and `cd` to the project directory.

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

The page isn't functional yet. It doesn't support photo uploads, even though the user interface for doing so is in place. The next step is to modify the site to allow users to upload photos.

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