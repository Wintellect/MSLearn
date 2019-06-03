# Set up a development environment

This unit assumes you are using Microsoft VS Code as your development environment. The program is free both to download from Microsoft and to use, and is available for Windows, MacOS, and Linux. You can write software in another environment, but it's much easier to follow along in Microsoft VS Code.

You'll also be using a tool called Azure CLI that extends the command line interface or terminal on your development system. Azure CLI is free both to install and use. It works with the following terminals:
- The bash shell on MacOS and Ubuntu Linux
- The bash shell that installs along with the Windows Subsystem for Linux for Windows 10 (run bash at the command prompt)
- The cmd shell on Windows 10
- PowerShell on Windows 10, MacOS, and Linux

If you use a recent edition of PowerShell, it may already be equipped with Azure CLI. To find out for sure, type az --help at the prompt. If you get a list of subgroups and commands instead of an error message, you have Azure CLI.

If you have Git for Windows, note that Azure CLI does not work with its built-in git bash shell.

## What you're about to do

While you probably know Python, you may never have used it to build an application that can be deployed into the cloud as a website. Configuring your development environment to accomplish this can be a tricky process.

One reason is Flask. Normally, when you run a Python program on your computer, the Python interpreter resides on your hard drive. The operating system stores the path where your operating system locates Python in an environment variable. That path isn't there when your application is deployed to Azure and becomes a Web application. Once deployed, your application runs its own Python instance inside the files you've uploaded. Python calls this self-contained instance a '"virtual environment,'" or venv.

You need your own regular Python installation to build this venv environment in the application's directory. Luckily, there's a command for that. Once that's built, you need to make sure VS Code is running Python in venv.

Now, if you've ever composed a Docker container, you'll recall that container needs local copies of everything upon which your application relies — all its dependencies. Equipping your venv environment is like sending your child away to college  : You want to give it everything it needs to be functional on its own. But from time to time, you still need reassurance that it needs you.

It's the same case with venv  . Every library that your application's source code may reference through the import keyword has to be installed locally. If you were to track down all the dependencies yourself and install them manually, you would lose the rest of your day — maybe the weekend if your application is complex enough. Luckily, git can track down and record your dependencies automatically. The deployment method you learn here involves git, and includes the creation of a local git repository.

To make sure Azure Cognitive Services is functional on both the Azure cloud and your development system, both your development application and your cloud-based Web app need copies of the authorization keys that Azure gives you. However, embedding those keys in your source code is a security hazard once that code is deployed in the public cloud. So you need a single method for your Python code to acquire these keys on your development system, one that does not change in the cloud. In other words, you need the same code to produce the same result, even though the place these keys would be found in the cloud is not even the same kind of place it would find these keys on your computer.

This unit guides you through the process of setting up both your cloud environment and your virtualized development environment. The result is that the same code (the application that translates photos of street signs) works in both places. This is not the same process as setting up your development environment to produce Cognitive Services applications as packages to be installed on users' PCs.

Here are the steps you'll take:
- Register for Azure Cognitive Services
- Obtain and store the main keys and service endpoints
- Set up local directories and install venv
- Use pip to prepare Flask and dependent libraries

## Register for Azure Cognitive Services

To begin an Azure session from your command prompt, type the following:

```bash
az login
```

After a moment, your browser takes you through the regular login dialogs. Once the session begins, instead of your Azure portal, your browser brings up the home page for Azure documentation. You can still open the Azure portal, although you'll be logged into Azure through the command prompt until you log out through the command prompt.

The moment you're logged in, the command prompt shows you a JSON list of the subscriptions associated with your account. Usually you'll see just one record, but an Azure account may have more than one subscription associated with it. This often happens when you accept more than one of Microsoft's offers to try its services for free for one month. When there's more than one, the list will be in alphabetical order by each subscription's name.

One of these records will have its `isDefault` property set to true. Unless you specify otherwise (in other words, make your commands to Azure even longer), everything you do in Azure CLI pertains to this default subscription. If the subscription you want is already the default, you're fine. To make another subscription the default, take down its name property in this list, and then enter the following command next, substituting that name for the <tag> below:

```bash
az account set –subscription <subscription-name>
```

As usual, if the subscription name happens to have spaces, then you'll need "quotation marks" around it. To make certain the change went through, enter this command:

```bash
az account list --all
```

The isDefault property of the subscription you designated should now be true.
With that matter settled, the next order of business is for you to create a resource group that collects together the services your application will need. Then you add a Cognitive Services resource that grants you access to Text Translator and Computer Vision.

For our purposes, we call our resource group Cognite, and we use Azure's East US region (which happens to have a low-cost S0 pricing tier). Here's the command you enter to create this resource group:

```bash
az group create --location eastus --name Cognite
```

Commands to Azure from the command line may take a minute to process, so if you see nothing happening for a while, don't worry. When the command line comes back, you'll see a JSON response for the new resource group with its provisioningState property set to Succeeded.

Next, you instantiate instances of the Translator Text and Computer Vision resources inside this resource group. For the purposes of this application, the name for these instances are TextTrans and CompVision, respectively.

```bash
az cognitiveservices account create --resource-group Cognite --name TextTrans --location global --kind TextTranslation --sku F0 --yes
az cognitiveservices account create --resource-group Cognite --name CompVision --location eastus --kind ComputerVision --sku F0 --yes
```

## Obtain and store the main keys and service endpoints

Each time your application communicates with Translator Text or Computer Vision, it uses a unique key. When you are logged onto your Azure account and already authenticated, then this key is attributed to that account. As you'll see, the endpoint is a URL which your code uses to address Cognitive Services over the Web. Here are the commands for obtaining the authorization keys:

```bash
az cognitiveservices account keys list --resource-group Cognite --name TextTrans --query key1 --output tsv
```

It may take a little time, but soon enough, Azure responds with a series of hexadecimal digits (0 through F). Select and copy this key to your operating system's clipboard.

Now, in a text editor or in a new editor window in VS Code, start a new document. Type the following, replacing the <marked portion> (including the carats) with the key you just copied:

```
TEXTTRANS_KEY=<copied key value>
```

Note there should be no spaces on either side of the = character.
Next, in the command prompt, enter this command for obtaining the endpoint:

```bash
az cognitiveservices account show --resource-group Cognite --name TextTrans --query endpoint --output tsv
```

Azure's response is a complete Web address, such as https://api.cognitive.microsoft.com/sts/v1.0/issuetoken. Copy this URI and paste it onto the end of the text document:

```
TEXTTRANS_ENDPOINT= https://api.cognitive.microsoft.com/sts/v1.0/issuetoken 
```

Replace the URI here with the one that Cognitive Services gives you.  Then repeat this process for the key value and URI endpoint for Computer Vision:

```bash
az cognitiveservices account keys list --resource-group Cognite --name CompVision --query key1 --output tsv
az cognitiveservices account show --resource-group Cognite --name CompVision --query endpoint --output tsv
```



```
CVISION_KEY=<copied key value>
CVISION_ENDPOINT=https://eastus.api.cognitive.microsoft.com/
```

For now, save this text document to a file named **cognite.env**. You'll soon move this document into a directory to be created later.

Next, use the command prompt to store these four environment variables locally, substituting the secret key values for the <tags> shown here. The command you use for this purpose does depend on which operating system you're using. Although the Linux Subsystem for Windows 10 gives that OS a bash shell, its export command sets environment variables for Linux, not Windows. Ironically, you can use the Windows setx command inside bash for Windows. 

```bash
export TEXTTRANS_KEY=<copied key value>
export TEXTTRANS_ENDPOINT= https://api.cognitive.microsoft.com/sts/v1.0/issuetoken
export CVISION_KEY=<copied key value>
export CVISION_ENDPOINT=https://eastus.api.cognitive.microsoft.com/
```

TODO:

```bash
setx TEXTTRANS_KEY <copied key value>
setx TEXTTRANS_ENDPOINT https://api.cognitive.microsoft.com/sts/v1.0/issuetoken
setx CVISION_KEY <copied key value>
setx CVISION_ENDPOINT https://eastus.api.cognitive.microsoft.com/
```

Note one subtle difference between the two systems' command syntax: The export command attaches values to variables using an =, while setx uses a space for that purpose.

## Set up local directories and install venv

The local home directory for your application on your development system may be anyplace convenient for you. The main Python interpreter (the one referenced by your system's PATH environment variable) is accessible from any directory. The venv environment for Flask will be located inside this home directory.

Once you've created the directory where your application will be housed, use your terminal to enter the next command, and the ones that follow:

```bash
python -m venv env
```

This directs Python to run the script that installs the venv environment in a folder called env, which Python creates. Once this script is completed, the Python interpreter and some of its principal libraries are copied into this folder — the bare necessities needed to make Python operable.

```bash
env/scripts/activate
```

If you're using a Windows command prompt, then your slashes should face the other direction \ instead of forward, Linux-style /.

This script moves your terminal '"inside'" the virtual environment, so the resources you use from this point forward belong to the application you're building.

## Use pip to install Flask and dependent libraries

You'll recall that pip is Python's package manager sidekick. It unpacks and installs files according to a script, freeing up enough time for you to retire at a relatively young age.

```bash
python -m pip install --upgrade pip
```

Long-time pip users will recognize this as the command that upgrades pip to the current version. It's vitally important that you have the current version of pip installed, because some older versions of pip installed by the script for venv miss some of the dependencies needed for execution in Azure.

```bash
pip install Flask
```

Note the capital '"F'" in Flask here. This installs the framework that makes Python the scripting language for a website. You're not using pipenv for the installation here because Flask is more than just a dependent library.

Next, bring in the library that your application will need to communicate and exchange information with Cognitive Services:

```bash
pip install azure-cognitiveservices-vision-computervision
```

Note that in this context, the words in the package name are all separated by dashes (-), whereas later in the context of Python, these same separations will use dots (.).

Finally, you run one command that generates a very important file that is used by git later to reproduce the structure of venv in Azure.

```bash
pip freeze > requirements.txt
```

The > redirects the output of this command to a file. In this case, pip produces a list of the dependent packages that would need to be installed in Azure, along with the precise version numbers required. Git relies on this file to help it know what to deploy to Azure. As this application evolves, you'll need to execute this command again to refresh the dependencies, but each time you do so, you'll save yourself perhaps dozens of steps.

In the next unit, you'll do something you may not have expected to do until the end: deploy an application to Azure App Services. You'll create the framework of a Flask Web app and deploy it using git. Then you'll modify it so that it becomes the road sign translator app, with git in VS Code keeping track of all your changes, within its repository. Those changes can be easily deployed to Azure as you go.