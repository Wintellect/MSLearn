# Summary

In this module, you built a solution that uploads images from a simulated array of cameras to [Azure Blob Storage](https://azure.microsoft.com/services/storage/blobs/), triggers an [Azure Function](https://azure.microsoft.com/services/functions/) each time an image is uploaded, analyzes the images using the [Custom Vision Service](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/), and visualizes the output using [Microsoft Power BI](https://powerbi.microsoft.com/). You also got first-hand experience using [Azure SQL Database](https://azure.microsoft.com/services/sql-database/). It's a sophisticated solution, and one that has applications in the real world.

## Check your knowledge

1. Flask is a framework for building Web apps in which of the following languages?
	- Python, Node.js, and Java
	- Python and Node.js
	- Python and Java
	- Python only

1. What is the name of the HTTP header that carries API keys in calls to Azure Cognitive Services?
	- Ocp-Apim-Cognitive-Key
	- Ocp-Apim-Subscription-Key
	- Ocp-Apim-Auth-Key
	- None of the above

1. What is the default port number that Flask uses to service HTTP requests?
	- 80
	- 5000
	- 8080
	- 127
	
1. Which of the following Azure CLI commands adds an application setting named API_KEY to an App Service named "contoso?"
	- `az webapp config appsettings set -g contoso-rg -n contoso-travel --settings API_KEY=a1b2c3d4`
	- `az webapp config appsettings add -g contoso-rg -n contoso-travel --settings API_KEY=a1b2c3d4`
	- `az appsvc config appsettings set -g contoso-rg -n contoso-travel --settings API_KEY=a1b2c3d4`
	- None of the above; application settings must be added through the Azure Portal

1. Which of the following are valid expression delimiters in Flask?
	- `{{` and `}}`
	- `{%` and `%}`
	- Both A and B
	- None of the above

1. How are messages "flashed" with Flask's `flash()` method shown by default?
	- In alert boxes
	- In modal popup windows that are browser-specific
	- In `<div>` elements decorated with `class="flash"` attributes
	- Flashed messages are not shown by default

1. By default, HTML files served up by Flask must be located in a directory named:
	- static
	- html
	- templates
	- main