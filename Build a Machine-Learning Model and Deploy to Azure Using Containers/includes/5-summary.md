# Summary

At the outset, it seemed a daunting task: train a machine-learning model to analyze text for sentiment, operationalize the model in a Docker container, run the container in Azure, and expose a REST API for invoking the model. You went one step further and built a cross-platform app for demonstrating the solution. It wasn't as difficult as it first seemed, thanks to Scikit-learn, Flask, Docker, and the Docker support in Azure.

You could go even further. You could build an app that monitors Twitter for tweets about your company, quantify the sentiment of each tweet, and fire a notification to the communications department if the running average falls below a certain threshold — for example, if the average sentiment expressed in the last 10 tweets is less than 0.4. You've already done the hard part. The rest is simply a variation on what you've already learned.

## Check your knowledge

1. The command used to build a Docker image in the Azure Cloud Shell is:
	- `az acr docker`
	- `az acr build`
	- `az docker build`
	- `az acr build-image`

1. The purpose of Scikit-learn's `CountVectorizer` is to:
	- Convert a corpus of text into numbers
	- Convert a corpus of strings into another language
	- Compute the probability that a text string can be normalized
	- Count the number of strings in a Python list or dictionary

1. The Python module used to save and load Scikit-learn models is:
	- `tickle`
	- `pickle`
	- `picklify`
	- `jsonify`

1. The **Dockerfile** command used to open a port in a container is:
	- OPEN
	- LISTEN
	- LISTENON
	- EXPOSE

1. Which of the following is true about storing Docker images in Azure Container Registry?
	- The images load faster when hosted in Azure Container Instances
	- Access to the images can be restricted using Azure Active Directory (AAD)
	- Images are easily replicated across Azure regions
	- All of the above

1. Which of the following statements is true when you create an Azure Container Registry with the `--admin-enabled true` option?
	- The registry name doubles as the user name for logging in
	- The registry name doubles as the password for logging in
	- The registry name is subject to additional security rules
	- The registry name must start with "admin_"