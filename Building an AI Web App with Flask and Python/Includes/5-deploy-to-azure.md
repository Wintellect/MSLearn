# Deploy the Web site to Azure

TODO: Add introduction.

## Deploy the site to an Azure App Service

In this exercise, you will use the [Azure CLI](https://docs.microsoft.com/cli/azure/get-started-with-azure-cli?view=azure-cli-latest) to deploy your Web site to Azure so it can be accessed by anyone, from anywhere, using a browser. The Azure CLI is a command-line environment for executing Azure commands for creating and managing Azure resources. Versions are available for Windows, macOS, and Linux.

1. If the Azure CLI isn't installed on your computer, go to https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest and install it now. You can determine whether it's installed by executing an `az -v` command in a Command Prompt or terminal window. If the CLI is installed, a version number will appear in the output.

1. In a Command Prompt or terminal window, log in to Azure with the following command:

	```bash
	az login
	```

	In the ensuing browser window, log in using your Microsoft account. Then close the browser and return to the CLI.

1. Type the following command to list the Azure subscriptions associated with your Microsoft account:

	```bash
	az account list
	``` 

1. The default subscription — the one used to create resources created with the CLI — will be marked `isDefault=true`. If that's the subscription you wish to use, proceed to the next step. Otherwise, use the following command to designate one of the other subscriptions as the default, replacing SUBSCRIPTION_ID with the ID of that subscription: 

	```bash
	az account set -s SUBSCRIPTION_ID
	```

1. Use a `cd` command to change to the project directory containing the Web site.

1. Create a text file named **requirements.txt** in the project directory containing the following statements:

	```
	requests
	Flask
	azure-cognitiveservices-vision-computervision
	``` 

	TODO: Explain requirements.txt.

1. Execute the command below to deploy the Web site to Azure, replacing APP_NAME with the name you want to assign to the site, RESOURCE_GROUP_NAME with the name of the resource group that's created to hold the Azure resources that are created (for example, "contoso-travel-rg"), and LOCATION with the region where you want the App Service to be hosted (for example, "eastus"). The app name must be **unique with Azure**, so you probably won't be able to use a common name such as "contoso" or "contosotravel" unless you append some random characters to the end.

	While not required, it is advisable to specify the same location (region) that you specified when you obtained keys for the Computer Vision API and Translator Text API. This makes calls to these APIs faster by colocating the Web site and the services that it uses in the same region.

	```bash
	az webapp up -n APP_NAME --resource-group RESOURCE_GROUP_NAME --location LOCATION
	```

	The [az webapp up]() command creates an Azure App Service to host your Web site, configures the App Service with the packages specified in **requirements.txt**, zips up the files in the current directory (and its subdirectories), and uploads the site to the App Service — all with one simple command. Sites that run on Node.js and Python are deployed to Linux App Services, while sites built on ASP.NET and ASP.NET Core run in Windows App Services.

Wait for the command to complete; it will take a few minutes. Then confirm from the output that the Web site was successfully deployed.

## Add application settings

When you ran the Web site locally, it used `os.environ` to load API keys for the Computer Vision API and the Translator Text API and the URL of the Computer Vision API from local environment variables. In order for the site to run in Azure, these same settings needed to be added to the Azure App Service's [application settings](https://docs.microsoft.com/azure/app-service/configure-common). In the steps that follow, you will use the Azure CLI to create these application settings in Azure and initialize them with the same values that you used when you loaded them into local environment variables.

1. Execute the following CLI command to create an application setting named "VISION_API_KEY," replacing RESOURCE_GROUP with the name of the resource group created by the `az webapp up` command, APP_NAME with the name assigned to your App Service, and `computer_vision_api_key` with the Computer Vision API key that you obtained earlier:

	```bash
	az webapp config appsettings set -g RESOURCE_GROUP -n APP_NAME --settings VISION_KEY=computer_vision_api_key
	```

1. Now use this command to create an application setting named "VISION_ENDPOINT," replacing `computer_vision_endpoint` with the Computer Vision API endpoint you obtained earlier:

	```bash
	az webapp config appsettings set -g RESOURCE_GROUP -n APP_NAME --settings VISION_ENDPOINT=computer_vision_endpoint
	```

1. Finish up by using the following command to load your Translator Text API key into application settings:

	```bash
	az webapp config appsettings set -g RESOURCE_GROUP -n APP_NAME --settings TRANSLATE_API_KEY=translate_api_key
	```

If you would like, you can log into the [Azure Portal](https://portal.azure.com), open the Azure App Service created by the `az webapp up` command, and view the application settings that these commands created. The screen shot below illustrates what you will see if you do.

![Viewing application settings in the Azure Portal](media/app-settings.png)

_Viewing application settings in the Azure Portal_

## Run the site in Azure

Now it's time to see the fruits of your labor.

1. Point your browser to http://APP_NAME.azurewebsites.net, replacing APP_NAME with the name of your App Service. Confirm that the site appears in your browser and that it looks exactly as it did when running locally.

	![Contoso Travel running in Azure](media/azure-site.png)
	
	_Contoso Travel running in Azure_

1. Choose a language and upload a few photos containing signs with text that you want to translate. Does the site behave the same in Azure as it does when running locally?


If you later make changes to your site and want to update the App Service in Azure, simply run the `az webapp up` command again. Rather than create a new App Service, it will zip-deploy the files in the current directory to the existing App Service. If you would prefer to put the source-code files under source control and deploy them directly from Visual Studio Code, just follow the instructions in [Deploy to Azure App Service on Linux](https://code.visualstudio.com/docs/python/tutorial-deploy-app-service-on-linux).












## What you're about to do

You might think that the part of a tutorial that talks about deploying your application to the cloud would be the last unit or chapter in the set. And that would sound like putting the proverbial cart before the horse. Reality teaches us that such a substitution makes perfect sense when the cart has its own horse propellant.

The propellant, in this case, is git. VS Code is engineered to make maximum use of this very versatile version control manager. As a result, it's possible for you to deploy an application that's essentially a body without parts: a '"Hello World'" application that's not quite ready for the world. Then as you build working, useful functions, you can deploy those changes incrementally, test them in an environment similar to production, and roll them back if they don't work right.

This way, you really can build the airplane in mid-flight. What's more, it's actually both safer and easier. This unit won't go into full detail about how to use git — that's a topic for another module. But you will see how VS Code makes use of this tool to deploy the code you build in a virtualized environment for Python and Flask on your development system, into a completely different environment inside a Docker container in the public cloud.

In this unit, you'll see how to create a kind of '"test pattern'" which assures you that all the necessary connections and dependencies are present and accounted for. You'll use a small amount of Python code that invokes its very common `os.environ` method to report the value of one of the environment variables you created in the previous unit. Rather than simply writing it to the screen using the print() function, however, the application renders an HTML page using Flask. You'll go online to the URI generated by Azure App Services to see this page.

After this test pattern is deployed, you can begin adding functions from Azure Cognitive Services to this chassis, then deploy those functions incrementally to the cloud to see them at work. Here are the steps you'll take:
- Create initial files for the Python code and Flask template
- Run the Flask server locally and test your code here
- Create the Azure App Service for your code
- Load your application's environment variables into Azure
- Create a git repository for your code
- Deploy the repository to Azure and test your code there

## Create initial files for the Python code and Flask template

If you're not already logged in to Azure, do so using a command prompt:

```bash
az login
```

Each instance of VS Code that you launch and use has a workspace that is the central directory for your project. You should become accustomed to launching VS Code from a command prompt from this project directory. Use cd to change to your project directory (the one that contains env as a subdirectory) and launch VS Code with this:

```bash
code .
```

The very first time you launch VS Code from here, it won't know what kind of application you're building; it doesn't have a history yet. So it doesn't search for a venv environment. This time only, you need to show it what to look for and where to look. Here's a way of feeding three birds with a single worm, to opt for a more positive metaphor:

In VS Code, start a new file, and give it one of the most common instructions found at the start of a Python application:

```bash
import os
```

Now save that file in your application's home directory as **app.py**. This is not an arbitrary name; Flask looks for Python code with this filename first. The moment you save this file with this name, VS Code realizes you're writing a Python application. It then loads its Python extensions into memory, including Pylint or whichever '"linter'" you've installed to make your code look better.

At the lower left corner of the VS Code window, you should see this indicator of which interpreter is currently in use:
 


The version number may have gotten higher since the time of this writing. At any rate, this is not the Python interpreter you're looking for; you actually need the one running within venv. To change interpreters, click this area. You see a list of available Python interpreters in VS Code's command palette at the top.
 


From this list, choose the Python interpreter that is associated with venv. Here, you can see it's the environment contained in the 'env' directory. Your new choice is reflected in the VS Code status bar.
 


In the lower right corner of the window, you may see a notification that it needs to install a package that's intrinsic to VS Code, that the venv installation process may have missed (because it's not part of VS Code). Click Install to start that process.
 


If you opened a terminal window (for instance, after installing Pylint) you may notice your prompt has an (env) in front of it. That's to let you know that this terminal prefers the resources installed inside the venv environment, over those installed elsewhere on your computer.
Notice also that the current interpreter notifier has been updated.
 


The first file you create for your project won't look like Python at all. It's a very basic HTML page except for one curious element. Using VS Code, type or copy this code into a new document. Create a subfolder for your project folder, and name it templates. Then save this snippet of code to your project as **index.html**.

```html
<!DOCTYPE html>

<html>
  <head>
    <title>Foreign road sign translator</title>
  </head>
  <body>
    Your Cognitive Services endpoint should be:
    <h2>{{ location }}</h2>
  </body>
</html>
```

The element that stands out from this otherwise innocuous file is `{{ location }}`, just inside the `<h2>` block. The double curly-braces (which could be called '"mustaches'" if another templating language hadn't already claimed that word) carves a hole inside this page, making it into a template. For this initial application, the hole is only one item: the value of a variable that is passed into this page by Flask, as though it were interpreted code. Flask pastes that value into the `<h2>` block when it's time to send the page to be rendered.

Now for the actual Python code. Flask makes interesting additions to Python which use Python's native syntax, although many developers won't be familiar with it at first. These additions do not go so far as to make the code illegible to humans.

Open the **app.py** window and replace its existing text with the following code:

```python
# -*- coding: utf-8 -*-

import os, json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    endpoint = os.environ["COGS_ENDPOINT"]
    return render_template("index.html", location=endpoint)
```

The initial comment merely tells Python to use Unicode encoding for characters. The first unusual part is the instruction app = Flask(__name__). As you know, Python is a dynamic, though strongly typed, programming language. The term Flask(__name__) refers to a complex object that represents the instructions for running a Web server. Flask is, as you'll recall, a Web server. So future instructions that include methods being passed to Flask will address this app object that has been assigned to the term. Another variable name could have been used here instead, but app is fairly common with Flask.

The first instruction passed to Flask by way of the object reference @app acts as a header for the functionality in the home page of the Web site. Remove the top-level domain name from the home page, and you're left with just a single backslash "/". The classic Python function header def index(): could have been named something else; '"index'" is not a reserved word for Flask.

Long-time Python developers will be familiar with the os.environ[] method, which recalls an environment variable by name. Here it references one of the variables we created in the previous unit, COGS_ENDPOINT, and assigns it to a Python variable endpoint. The only thing this very basic function does next is pass endpoint as an argument to Flask's render_template() function, which closes out the def block. Notice how the argument name is location, which is the name given to the hole in the Flask template. When render_template() goes to work, it gathers the argument and pastes it into its copy of index.html in memory, then sends it over the Web to be rendered.

## Run the Flask server locally and test your code

To make certain this code is operational, first save all unsaved documents. Then with the app.py window open, click the Run code button on the VS Code toolbar. In a moment, the output pane shows something similar to the following:

```
[Running] python -u "d:\My Documents\Code\Cognite\tempCodeRunnerFile.py"

[Done] exited with code=0 in 4.925 seconds
```

If you were expecting fireworks, you'll have to wait a bit. What's happened here is that Flask has been issued its marching orders, though it has yet to pick them up. To make the Flask server run, open the Terminal pane in VS Code and issue this command:

```bash
flask run
```

This launches the development-class Web server, which runs in the background until you press Ctrl+C in the terminal window.

Now that it's running, open your Web browser and navigate to http://127.0.0.1:5000 (or http://localhost:5000). You should see a message reporting the current value of a key environment variable, similar to this:
 
To stop Flask for now, enter Ctrl+C in the terminal window.
