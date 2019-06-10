# Set up a development environment

The first order of business is to set up a development environment for Web sites written in Python and Flask. This will enable you to build and test Contoso Travel locally prior to deploying it to Azure and making it available publicly.

In this unit, you will install Python on your computer if it isn't already installed. Then you will install Flask and the [Python SDK for the Computer Vision API](https://pypi.org/project/azure-cognitiveservices-vision-computervision/). The latter makes it easy to call Azure's Computer Vision API from Python applications. Finally, you will install the [Azure CLI](https://docs.microsoft.com/cli/azure/get-started-with-azure-cli?view=azure-cli-latest), which provides a command-line interface to Azure and also requires Python.

## Create a Flask environment

Flask is a Web framework for applications written in Python. In order to run Flask Web sites on your computer, both Flask and Python must be installed.

1. If Python 3.6 or higher isn't installed on your computer, go to https://www.python.org/ and install it now. You can determine whether it's installed on Windows by executing the following command in a Command Prompt window:

	```bash
	python --version
	```

	Similarly, you can check to see whether it's installed on macOS or Linux by executing the following command in a terminal:

	```bash
	python3 --version
	```

	If Python is installed, the version number will appear in the output. If you install Python and are asked during the install process whether Python should be added to the system's PATH, answer yes.

	![Adding Python to the PATH](media/add-to-path.png)

	_Adding Python to the PATH_

1. If you are running Windows, execute the following command to install the latest version of `pip`, the Python package manager:

	```bash
	python -m pip install --upgrade pip
	```

	If you are running macOS or Linux, use this command instead:

	```bash
	python3 -m pip install --user --upgrade pip
	```

	This is important because older versions of `pip` may miss some of the dependencies needed for execution in Azure.

1. Now execute the following commands to install Flask and the Python SDK for Azure's Computer Vision API:

	```bash
	pip install Flask
	pip install azure-cognitiveservices-vision-computervision
	```

Check the output and make sure that both packages installed without errors.

## Install the Azure CLI

The [Azure CLI](https://docs.microsoft.com/cli/azure/get-started-with-azure-cli?view=azure-cli-latest) is a command-line environment for creating and managing Azure resources. Versions are available for Windows, macOS, and Linux. In subsequent units, you will use the Azure CLI to create various Azure resources, including an [Azure App Service](https://azure.microsoft.com/services/app-service/) to host a Web site. In this exercise, you will install the Azure CLI and log into it for the first time.

1. If the Azure CLI isn't installed on your computer, go to https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest and install it now. You can determine whether it's installed by executing an `az -v` command in a Command Prompt or terminal window. If the CLI is installed, a version number will appear in the output.

1. In a Command Prompt or terminal window, log in to Azure with the following command:

	```
	az login
	```

	In the ensuing browser window, log in using your Microsoft account. Then close the browser and return to the CLI.

1. Type the following command to list the Azure subscriptions associated with your Microsoft account:

	```
	az account list
	``` 

	The default subscription — the one used to create resources created with the CLI — will be marked `isDefault=true`. If that's the subscription you wish to use, or if it's the only subscription in the list, you're done. Otherwise, use the following command to designate one of the other subscriptions as the default, replacing SUBSCRIPTION_ID with the ID of that subscription: 

	```
	az account set -s SUBSCRIPTION_ID
	```

If you aren't familiar with the Azure CLI, you can learn more about it and the numerous commands it supports in [Get started with the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest). Most operations that you perform in Azure can be performed with the CLI or through the [Azure Portal](https://portal.azure.com). Power users tend to prefer the CLI, in part because CLI commands can be used in scripts to automate repetitive tasks.