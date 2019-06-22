# Run the container in an Azure Container Instance

In this lesson, you will use the Docker image that you built and pushed to the container registry in the previous lesson in an Azure Container Instance. Because the container image has already uploaded to an Azure Container Registry, running it in a container instance requires just a few simple steps.

1. Return the [Azure Cloud Shell](https://shell.azure.com) and use the following command to create an Azure Container Instance, replacing TK with TK,TK with TK, and TK with TK.

	```bash

	``` 

	What is the significance of the DNS name label? Once a container instance is launched, you can retrieve a fully qualified domain name (FQDN) from the Azure Portal for placing REST calls to software running in the container. The DNS name label that you enter becomes the first segment of the FQDN — for example, ```containerslab.northcentralus.azurecontainer.io```.

	The port number that you entered is significant, too. Inside the Dockerfile from which you built the container image is a statement that opens port 8008 in the container:

	```dockerfile
	EXPOSE 8008
	```

	And inside **app.py** is a pair of statements that configures the code running in the container to listen for requests on port 8008:

	```python
	if __name__ == '__main__':
	    app.run(debug=True, port=8008, host='0.0.0.0')
	```

	Opening port 8008 in the container instance closes the loop and enables the Flask Web server running in the container to respond to REST calls arriving on port 8008.

1. TODO: Get the container instance's FQDN.

1. TODO: Use `wget` (?) to place a test call to the container instance.

The container is running and accepting calls via HTTP. The next step is to build an app that submits text typed by the user to the container to score the text for sentiment.