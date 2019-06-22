# Introduction

TODO: Add scenario.

[Containers](https://www.docker.com/what-container) are revolutionizing software development, and [Docker](http://www.docker.com) is the world's most popular containerization platform. Containers allow software and files to be bundled into self-contained packages that can be run on different computers and different operating systems. The following description comes from the Docker Web site:

![](media/container-overview.png)

Containers are similar to virtual machines (VMs) in that they provide a predictable and isolated environment in which software can run. Because containers are smaller than VMs, they start quickly and use less RAM. Moreover, multiple containers running on a single machine share the same operating system kernel. Docker is based on open standards, enabling Docker containers to run on all major Linux distributions as well as on Windows Server 2016.

## Containers in Azure

To support running containerized applications in the cloud, Azure offers [Azure Container Instances](https://azure.microsoft.com/services/container-instances/), which provide a robust, scalable, and easy-to-use environment for hosting containerized applications, as well as the [Azure Container Registry](https://azure.microsoft.com/services/container-registry/). The latter allows container images to be hosted in Azure rather than in external repositories such as [Docker Hub](https://hub.docker.com/) and loaded quickly into Azure Container Instances.

In this module, you will get first-hand experience with Azure Container Instances and the Azure Container Registry and learn about building and operationalizing machine-learning models at the same time. You will begin by using [Scikit-learn](https://scikit-learn.org/stable/index.html) to build and train a machine-learning model that scores text for sentiment. You will then use the [Azure Cloud Shell](https://azure.microsoft.com/features/cloud-shell/) to build a Docker image containing a [Flask](http://flask.pocoo.org/) Web server that exposes the model using a REST endpoint, and deploy the image to an Azure Container Registry. Finally, you will run the Docker image in an Azure Container Instance and use the cross-platform app pictured below to score the text that you type for sentiment on a scale of 0.0 (negative) to 1.0 (positive) by invoking the machine-learning model in the container.

![Analyzing text for sentiment](media/textalyze.png)

## Learning objectives

Here's a preview of the skills you will acquire in this module:

- How to run Python code in [Azure Notebooks](https://notebooks.azure.com)
- How to build, train, and serialize machine-learning models using Scikit-learn
- How to load a serialized machine-learning model
- How to create an Azure Container Registry
- How to build a Docker image and deploy it using the Azure Cloud Shell
- How to run a containerized app in an Azure Container instance
- How to use Flask to expose a REST API from a container
- How to call that REST API from a [Node.js](https://nodejs.org/) app

As you do, you will answer a question that is commonly asked by enterprise developers: if I build a machine-learning model in Python, how do I operationalize it in such a way that I can call it from apps written in other languages?