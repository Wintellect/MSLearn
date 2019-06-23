# Run the container in an Azure Container Instance

In this lesson, you will run the Docker image that you pushed to the container registry in the previous lesson in an Azure Container Instance. Because the container image has already been uploaded to your Azure Container Registry, running it in a container instance requires just a few simple steps.

1. Return to the [Azure Cloud Shell](https://shell.azure.com) and use the following command to create an Azure Container Instance, replacing REGISTRY_NAME with the name of your container registry (in two places), DNS_NAME with the DNS name label that will form part of the fully qualified domain name (FQDN) for the running container, and PASSWORD with the access key/password that you saved earlier for the Azure Container Registry:

	```bash
	az container create -g azure-ml-rg -n ml-container --image REGISTRY_NAME.azurecr.io/text-analytics-server --dns-name-label DNS_NAME --ports 8008 --ip-address public --registry-username REGISTRY_NAME --registry-password PASSWORD
	``` 

	What is the significance of the DNS name label? Once a container instance is launched, you can retrieve a fully qualified domain name for placing REST calls to software running in the container. The DNS name label becomes the first segment of the FQDN — for example, ```DNS_NAME_LABEL.northcentralus.azurecontainer.io```.

	> The DNS name label doesn't have to be unique within Azure, but it does have to be unique in the region in which the container instance is created.

	The port number you specified with the `--ports` switch is significant, too. Inside the **Dockerfile** from which you built the container image is a statement that opens port 8008 in the container:

	```dockerfile
	EXPOSE 8008
	```

	And inside **app.py** is a pair of statements that configures the code running in the container to listen for requests on port 8008:

	```python
	if __name__ == '__main__':
	    app.run(debug=True, port=8008, host='0.0.0.0')
	```
	Opening port 8008 in the container instance closes the loop and enables the Flask Web server running in the container to respond to REST calls arriving on port 8008.

1. Wait for the command to complete. (It may take a minute or two.) Then use the following command to get the container instance's fully qualified domain name:

	```bash
	az container show -g azure-ml-rg -n ml-container --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
	```

	Save the FQDN in your favorite text editor. You will need it in the next lesson.

1. Make sure **Bash** is the language selected in the upper left corner of the Cloud Shell. Then execute the following command to place a call to the container and analyze a text string for sentiment, replacing FQDN with the container's fully qualified domain name:

	```bash
	wget -qO- FQDN:8008/predict?text=Great%20food%20and%20excellent%20service
	```

1. Confirm that the output from `wget` includes a number from 0.0 to 1.0:

	```
	0.8948149446550228
	```

	This is the score that quantifies the sentiment expressed in the text string "Great food and excellent service." Remember that 0.0 is negative and 1.0 is positive.

The container is running and accepting calls via HTTP. The next step is to build an app that submits text typed by the user to the app running in the container to score the text for sentiment.