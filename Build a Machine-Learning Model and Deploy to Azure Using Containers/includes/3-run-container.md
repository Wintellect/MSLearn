# Run the container in an Azure Container Instance

In this lesson, you will run the Docker image that you built and pushed to the container registry in the previous lesson in an Azure Container Instance. Because the container image has already been uploaded to an Azure Container Registry, running it in a container instance requires just a few simple steps.

1. Return to the [Azure Cloud Shell](https://shell.azure.com) and use the following command to create an Azure Container Instance, replacing REGISTRY_NAME with the name of your container registry, and DNS_NAME with with the DNS.

	```bash
	az container create -g azure-ml-rg -n ml-container --image REGISTRY_NAME.azurecr.io/text-analytics-server --dns-name-label DNS_NAME --ports 80 --ip-address public
	``` 

	What is the significance of the DNS name label? Once a container instance is launched, you can retrieve a fully qualified domain name (FQDN) for placing REST calls to software running in the container. The DNS name label that you enter becomes the first segment of the FQDN — for example, ```textalyzer.northcentralus.azurecontainer.io```.

	The port number that you entered is significant, too. Inside the Dockerfile from which you built the container image is a statement that opens port 80 in the container:

	```dockerfile
	EXPOSE 80
	```

	Opening port 80 in the container instance enables the Flask Web server running in the container to respond to REST calls arriving on port 80.

1. Use the following command t get the container instance's fully qualified domain name (FQDN):

	```bash

	```

1. TODO: Use `wget` (?) to place a test call to the container instance.

The container is running and accepting calls via HTTP. The next step is to build an app that submits text typed by the user to the container to score the text for sentiment.