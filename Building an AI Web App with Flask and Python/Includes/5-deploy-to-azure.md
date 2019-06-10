# Deploy the Web site to Azure

[Azure App Service](https://azure.microsoft.com/en-us/documentation/articles/app-service-value-prop-what-is/) is a set of services provided by Microsoft Azure to enable developers to easily build and deploy Web apps. Included in the App Service family are [Azure Web Apps](https://azure.microsoft.com/en-us/documentation/articles/app-service-web-overview/), which allow you to quickly and easily deploy Web sites built with tools and languages you’re already familiar with.

Azure Web Apps makes deploying Web sites extraordinarily easy – and not just Web sites built using the Microsoft stack. You can deploy Python apps that use MySQL just as easily as ASP.NET apps that use SQL Server. You can select from a wide variety of Web App templates or build templates of your own. You can configure Web Apps to auto-scale as traffic increases to ensure that your customers aren’t left waiting during periods of peak demand. You can publish apps to staging locations and test them in the cloud before taking them live, and then swap staging and production with the click of a button. You can even create [WebJobs](https://docs.microsoft.com/azure/app-service/webjobs-create) – programs or scripts that run continuously or on a schedule to handle billing and other time-critical tasks. In short, Azure Web Apps takes the pain out of publishing and maintaining Web apps and are just as suitable for a personal photo-sharing site as they are for enterprise-grade sites serving millions of customers.

In this unit, you will deploy Contoso Travel to Azure as an Azure Web App so it can be accessed by anyone, from anywhere, using a browser. And you will learn about App Service application settings, which allow API keys and other "secrets" used by an application to be stored securely in the cloud.

## Create an Azure App Service

In this exercise, you will use the [Azure CLI](https://docs.microsoft.com/cli/azure/get-started-with-azure-cli?view=azure-cli-latest) to deploy your Web site to Azure.

1. Create a text file named **requirements.txt** containing the following statements in the project directory — the directory containing the Contoso Travel site:

	```
	requests
	Flask
	azure-cognitiveservices-vision-computervision
	``` 

	**requirements.txt** contains a list of Python packages that must be installed along with the app when the app is deployed to Azure.

1. Open a Command Prompt or terminal window and `cd` to the project directory.

1. Execute the command below to deploy the Web site to Azure, replacing APP_NAME with the name you want to assign to the site. The name must be **unique with Azure**, so you probably won't be able to use a common name such as "contoso" or "contosotravel" unless you append some random characters to the end.

	```
	az webapp up -n APP_NAME --resource-group contoso-travel-rg --location northcentralus
	```

	The [az webapp up]() command creates an Azure App Service to host your Web site, configures the App Service with the packages specified in **requirements.txt**, zips the files in the current directory and its subdirectories, and uploads the site to the App Service — all with one simple command. Sites that run on Node.js and Python are deployed to Linux App Services, while sites built on ASP.NET and ASP.NET Core run in Windows App Services.

	> Observe that you deployed the App Service in the same region (North Central US) as the Computer Vision API. This makes calls to the API faster by colocating the Web site and the API that it uses in the same Azure region.

Wait for the command to complete; it will take a few minutes. Then confirm from the output that the Web site was successfully deployed.

## Add application settings

When you ran the Web site locally, it used `os.environ` to load API keys for the Computer Vision API and the Translator Text API and the URL of the Computer Vision API from local environment variables. In order for the site to run in Azure, these same settings needed to be added to the Azure App Service's [application settings](https://docs.microsoft.com/azure/app-service/configure-common). In the steps that follow, you will use the Azure CLI to create these application settings in Azure and initialize them with the same values that you used when you loaded them into local environment variables.

1. Execute the following CLI command to create an application setting named "VISION_API_KEY," replacing APP_NAME with the name assigned to your App Service and `computer_vision_api_key` with the Computer Vision API key that you obtained earlier:

	```
	az webapp config appsettings set -g contoso-travel-rg -n APP_NAME --settings VISION_KEY=computer_vision_api_key
	```

1. Now use this command to create an application setting named "VISION_ENDPOINT," replacing `computer_vision_endpoint` with the Computer Vision API endpoint you obtained earlier:

	```
	az webapp config appsettings set -g contoso-travel-rg -n APP_NAME --settings VISION_ENDPOINT=computer_vision_endpoint
	```

1. Finish up by using the following command to load your Translator Text API key into application settings, replacing `translate_api_key` with your key:

	```
	az webapp config appsettings set -g contoso-travel-rg -n APP_NAME --settings TRANSLATE_API_KEY=translate_api_key
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














## Extra

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

The initial comment merely tells Python to use Unicode encoding for characters. The first unusual part is the instruction `app = Flask(__name__)`. As you know, Python is a dynamic, though strongly typed, programming language. The term `Flask(__name__)` refers to a complex object that represents the instructions for running a Web server. Flask is, as you'll recall, a Web server. So future instructions that include methods being passed to Flask will address this app object that has been assigned to the term. Another variable name could have been used here instead, but app is fairly common with Flask.

The first instruction passed to Flask by way of the object reference @app acts as a header for the functionality in the home page of the Web site. Remove the top-level domain name from the home page, and you're left with just a single backslash "/". The classic Python function header def index(): could have been named something else; '"index'" is not a reserved word for Flask.

Long-time Python developers will be familiar with the `os.environ` method, which recalls an environment variable by name. Here it references one of the variables we created in the previous unit, COGS_ENDPOINT, and assigns it to a Python variable endpoint. The only thing this very basic function does next is pass endpoint as an argument to Flask's `render_template()` function, which closes out the def block. Notice how the argument name is location, which is the name given to the hole in the Flask template. When `render_template()` goes to work, it gathers the argument and pastes it into its copy of **index.html** in memory, then sends it over the Web to be rendered.

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
