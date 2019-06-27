# Create an Azure notebook

In order to try your hand with Python and some of the libraries that make it a great language for analyzing and manipulating data, you need an environment in which to execute Python code. You could install Python on your computer. It's included in most Linux distributions, but if you're running Windows, chances are it has to be installed separately.

An alternative, and one widely used by Python porgrammers, is Jupyter notebooks. Jupyter is an environment based on [IPython](https://ipython.org/) that facilitates interactive programming and data analysis using a variety of programming languages, including Python. Jupyter notebooks enjoy widespread use in research and academia for mathematical modeling, machine learning, and statistical analysis. [Azure Notebooks](https//notebooks.azure.com) provide Jupyter as a service for free. It's a convenient way to build notebooks and share them with others without having to install and manage a Jupyter server. And it's completely Web-based, making it an ideal solution for collaborating online.

![Azure notebook](media/notebook.png)

In this lesson, you will log into Azure Notebooks using your Microsoft account, create a project, and create your first notebook. In subsequent lessons, you will add additional notebooks to the project in order to get first-hand experience handling data in Python.

1. Navigate to https://notebooks.azure.com in your browser and sign in using your Microsoft account. Click **My Projects** in the menu at the top of the page. Then click the **+ New Project** button at the top of the "My Projects" page.

1. Create a new project named "Data Handling in Python." Check the "Public" box if you'd like to share notebooks with other people later on. You can also go into project settings once a project is created and change its visibility to public or private. 

	![Creating a project](media/add-project.png)

	_Creating a project_

1. Click **+ New** and select **Notebook** from the menu to add a notebook to the project.

	![Adding a notebook to the project](media/add-notebook-1.png)

	_Adding a notebook to the project_

1. Name the notebook "Airports.ipynb," and select **Python 3.6** as the language. This will create a notebook with a Python 3.6 kernel for executing Python code. One of the strengths of Azure notebooks is that you can use different languages by choosing different kernels.

	![Creating a notebook](media/add-notebook-2.png)

	_Creating a notebook_

	If you're curious, the **.ipynb** file-name extension stands for "IPython notebook." Jupyter notebooks were originally known as IPython (Interactive Python) notebooks, and they only supported Python as a programming language. The name Jupyter is a combination of Julia, Python, and R — the core programming languages that Jupyter supports.

1. Click the notebook to open it for editing.

You can create additional projects and notebooks as you work with Azure Notebooks. You can create notebooks from scratch, or you can upload existing notebooks. And once a notebook is created or uploaded, you can take advantage of Azure compute resources to run the notebook and leverage popular Python libraries such as [Keras](https://keras.io/), [NumPy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [Scikit-learn](https://scikit-learn.org/stable/index.html).

## Execute code in the notebook

Jupyter notebooks are composed of cells. Each cell is assigned one of three types: 

- **Markdown** for entering text in markdown format. 
- **Code** for entering code that runs interactively  
- **Raw NBConvert** for entering data inline

Code entered into code cells is executed by a *kernel*. The popular IPython kernel supports code written in Python, but dozens of other kernels are available supporting other languages. Azure notebooks (Jupyter notebooks created in Azure) support Python, R, and F#. They also support numerous packages and libraries that are commonly used in Python.

1. In the first cell, set the cell type to **Markdown** and type "# Airport codes" (without quotation marks) into the cell itself. The click the **Run** button in the notebook's toolbar:

	![Creating a markdown cell](media/first-cell.png)

	_Creating a markdown cell_

1. Type the following code into the next cell and click **Run** again to execute the code:

	```python
    airport_codes = ['SEA', 'DTW', 'HOU', 'BOS']
    print(airport_codes)
	```

	Confirm that a list of airport codes appears in the output:

	![Running a code cell](media/second-cell.png)

	_Running a code cell_

You can add additional cells to the notebook as needed to execute code and document your work. Finish up by selecting **Save and Checkpoint** from the notebook's **File** menu to save the notebook. Get in the habit of saving early and often to minimize the chance of losing your work.  
