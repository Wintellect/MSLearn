# Deploy the Web site to Azure

TODO: Add introduction.

## Deploy the site to an Azure App Service

TODO: Add intro.

1. TODO: Add instructions for installing the Azure CLI, logging in for the first time, and setting the default subscription.

1. Use a `cd` command to change to the project directory containing the Web site.

1. Execute the following command in the Command Prompt or terminal to generate a file named **requirements.txt** containing a list of packages installed with your site:

	```bash
	pip freeze > requirements.txt
	```

	TODO: Explain requirements.txt.

1. Execute the following command to deploy the Web site to Azure, replacing tk.

	```bash
	az webapp up -n APP_NAME --resource-group RESOURCE_GROUP_NAME --location LOCATION
	```

	The [az webapp up]() command creates an Azure App Service to host your Web site, configures the App Service with the packages specified in **requirements.txt**, and uploads the site to the App Service — all with one simple command.

1. Wait for the command to complete (it could take a few minutes). Then confirm that the Web site was successfully deployed. The output following a successful deployment will look something like this:

	```

	```

TODO: Add closing.

## Add application settings

When you ran the Web site locally, it used calls to `os.environ()` to load API keys for the Computer Vision API and the Translator Text API as well as the URL of the Computer Vision API from local environment variables. In order for the site to run in Azure, these same settings needed to be added to the Azure App Service's [application settings](https://docs.microsoft.com/azure/app-service/configure-common). In the steps that follow, you will use the Azure CLI to create these application settings in Azure and initialize them with the same values that you used when you loaded them into local environment variables.

1. Open the Azure CLI and execute the following command to create an application setting named "VISION_API_KEY," replacing RESOURCE_GROUP with the name of the resource group created by the `az webapp up` command, APP_NAME with the name assigned to your App Service, and `computer_vision_api_key` with the Computer Vision API key that you obtained in an earlier unit:

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

## Run the production site

TODO: Add intro.

1. Point your browser to http://APP_NAME.azurewebsites.net, replacing APP_NAME with the name of your App Service. Confirm that the site appears in your browser and that it looks exactly as it did when running locally.

	![Contoso Travel running in Azure](media/azure-site.png)
	
	_Contoso Travel running in Azure_

1. Choose a language and upload a few photos containing signs with text that you want to translate. Does the site behave the same in Azure as it does when running locally?

TODO: Add closing.













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

## Create an Azure App Service

Here is where we begin the process of setting up your Azure account to run your Flask application, so that you can build in segments and deploy as you go. Start by opening the Azure App Service extension in VS Code.
 
Click the + button to start the process of generating a new App Service. Then in the command palette, choose a subscription to which you want your application to be attributed.

When the command palette asks you for a globally unique name for this application, enter EverywhereASign. As a best practice, the name of your application should be something you would expect to see on the tail end of a URL. So omit any '"special characters.'" And even though Azure would permit your name to include a dash (-), refrain from using that as well.

Next the command palette shows you a list of runtime interpreters. Of course, you'll choose the most recent version of Python listed.

In a few minutes, you see a notification telling you the App Service has been created, and asking you if you're ready to deploy files now. You're actually not ready, because you need to set up a git repository first, so click No.
 


In the Azure App Service extension pane, expand your chosen subscription so you can see the components of your new App Service. Then right-click on the name of your application (EverywhereASign) and from the popup menu, select Browse Website.
 
Azure registers the applications in its App Services as a subdomain of its azurewebsites.net domain. So in a moment, your browser opens up one of those pages that looks like an '"auto-parking'" message from a domain names vendor.
 

You don't actually need to do anything with this page. It's just a placeholder. But you may think of it also as a success message telling you that the service is present and ready to be used.

## Load environment variables into Azure

In the previous unit, you created a file called **cognite.env** that holds copies of four environment variables critical to your application being able to use Azure Cognitive Services. Here is where that file comes into play. Uploading it to the Azure App Service you just created automatically populates that service with these variables.

In the Azure App Service pane, expand EverywhereASign, then right-click on Application Settings, and select Upload Local Settings.
 
In the command palette, click Browse, then in the file selector, choose **cognite.env**. In a moment, VS Code notifies you that these settings were uploaded successfully.

## Create a git repository for your code

The reason you can start the deployment process now rather than waiting until after you've finished making and debugging your application is git. Once you've built a git repository (or repo, as you may hear folks say), you can comfortably build your application in working increments, and deploy those increments as you go.

For the purposes of this application, you'll build your git repository on your development system locally. In a situation where you'd be developing this application on more than one system, or where several people may contribute to it simultaneously, you would want to use GitHub for storing a global repository.

Start by opening a VS Code terminal pointing to the project's home directory. You should see the (env) marker in front of the prompt. Then enter the following command:

```bash
pip freeze > requirements.txt
```

The freeze directive tells pip to produce a list of dependencies for this project. You'll recognize the > character as redirecting the output of the command from the screen to a file. Git specifically looks for requirements.txt when it assembles the repository.

Next, start a new document in VS Code, enter the following text, and save it to a file in your project directory named .gitignore.

```
.gitignore
.vscode/
__pycache__
.env/
*.old
```

Yes, it's odd to have a file whose name lacks any characters before the . but in this case, it serves to highlight the importance of the file, especially in a sorting order. Each line of this file represents a pattern. Any file (or, in the case of leading periods and trailing slashes, directory) whose name matches one of these patterns is excluded from tracking by git. Having *.old around gives you an opportunity to hold on to older versions of files (e.g., requirements.txt.old) without letting them clutter up the repository.

With these files ready to go, you can begin the process of initializing the git repo. Make sure Flask isn't running at the moment. Then in the VS Code toolbar, click the Source Control icon. When the Source Control pane pops up, click the Git icon in the upper right corner.
 



 
In a moment, git compiles a list of all the little incremental things that would jointly conspire to produce your project — what it considers, for now, uncommitted changes. There could be a thousand or more of these items, but don't be daunted by this. Every repository starts with an initial commitment, and that's what you'll produce next.

To stage these '"changes'" for commitment to the repo, right-click the ellipsis button, and from the popup, select Stage All Changes.
 


Depending on how many '"changes'" there are, the staging process could take a minute or two. During this period, the Source Control icon is marked with a clock. Once it's done, everything in the list that was marked with CHANGES is now marked STAGED CHANGES.

To commit these staged changes and launch the repo's initial state, type a name such as Initial state into the Message field, and click the checkmark.
 
You'll know the process has finished when the Changes count shrinks to 0. From now on, every time you make an incremental change to the project, a token for that change shows up in this list.
Deploy your repository to Azure and test your code there

Here's where you begin actually uploading files to Azure. Re-open the Azure App Service pane. Right-click the name of your project (EverywhereASign) and from the popup menu, select Configure Deployment Source.
 
In the command palette, choose LocalGit.
 
Right-click the project name again and select Deploy to Web App.
 

One more time, from the command palette, choose the project directory.
 

While your repository is being deployed, a VS Code notification asks if you prefer to deploy your repository to this same location in Azure each time. There's no reason not to click Yes.
 
Uploading is complete when you see this notification asking you if you'd like to see your website in action. Click Browse Website.
 
Normally Azure assigns you a domain name using the name of your project as its subdomain. Of course, if you follow along with this example to the letter, you will not be assigned https://everywhereasign.azurewebsites.net/, because this very example already used it. So expect Azure to give you a permutation of this subdomain name, though you'll still recognize it.
 
As you can see, the uploading of environment variables to Azure was successful, thanks to the process you undertook in the previous unit. In the next unit, you'll make this same application do something genuinely interesting.