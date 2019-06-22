# Call the container from a client app

Now comes the fun part: using REST calls to invoke the machine-learning model running in the container from a client app in order to analyze text for sentiment. In this lesson, you will build the app, and you will use [Node.js](https://nodejs.org/) and [Electron](https://electronjs.org/) as the platform so the app can run on Windows, macOS, and Linux.

1. If Node.js isn't installed on your computer, go to https://nodejs.org/ and install it it now. You can determine whether Node is installed — and what version is installed — by opening a Command Prompt or terminal window and typing the following command:

	```bash
	node -v
	```

	If Node is installed, the version number will be displayed. If the version number is less than 8.0, **download and install the latest version**.

1. Create a project directory on your hard disk to hold the app.

1. Create a text file named **project.json** in the project directory. Paste in the following text, and then save the file:

	```json
	{
	  "name": "Textalyzer",
	  "version": "1.0.0",
	  "scripts": {
	    "start": "electron ."
	  },
	  "dependencies": {
	    "electron-prebuilt": "^1.4.13"
	  }
	}
	```

	This file contains metadata for the app and lists the app's dependencies so those dependencies can be loaded with an `npm install` command.

1. `cd` into the project directory at the command prompt. Then execute the following command to download and install the packages that the app requires:

	```bash
	npm install
	```

1. Create a file named **predict.js** in the project directory and paste in the following code:

	```javascript

	```

	TODO: Describe this code.


1. Replace FQDN on line TK with the container's fully qualified domain name that you retrieved in the previous lesson. The modified line should look something like this:

	```javascript
	var url = "http://containerslab.northcentralus.azurecontainer.io:8008/predict";
	```

1. Return to the command prompt and use the following command to start the client app:

	```bash
	npm start
	```

1. Type a text string into the box and click the **Analyze** button. Wait for a message box to appear with the results. How positive or negative is the text? Recall that 0.0 represents sentiment that is extremely negative, while 1.0 indicates that the text is extremely positive.

	![Analyzing text for sentiment](media/textalyzer.png)

	_Analyzing text for sentiment_

1. Try other strings and score them for sentiment, too.

The fact that this is working means you have built and trained a machine-learning model, embedded the model in a Docker container hosted in Azure, and written a cross-platform client app that places REST calls to the container to analyze text for sentiment — and all in about an hour. This is the power of machine learning combined with the ease of use of Azure containers.
