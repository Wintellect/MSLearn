# Analyze flight delays

In order to try your hand with Python and some of the libraries that make it a great language for analyzing and manipulating data, you need an environment in which to execute Python code. You could install Python on your computer. It's included in most Linux distributions, but if you're running Windows, chances are it has to be installed separately.

An alternative, and one widely used by Python porgrammers, is Jupyter notebooks. Jupyter is an environment based on [IPython](https://ipython.org/) that facilitates interactive programming and data analysis using a variety of programming languages, including Python. Jupyter notebooks enjoy widespread use in research and academia for mathematical modeling, machine learning, and statistical analysis. [Azure Notebooks](https//notebooks.azure.com) provide Jupyter as a service for free. It's a convenient way to build notebooks and share them with others without having to install and manage a Jupyter server. And it's completely Web-based, making it an ideal solution for collaborating online.

![Azure notebook](media/notebook.png)

In this lesson, you will log into Azure Notebooks using your Microsoft account, create your first notebook, and apply some of the principles learned in previous lessons to crack open a CSV file and gather some basic statistics regarding flight delays.

## Create a notebook

Azure notebooks are created through the portal at https://notebooks.azure.com and require nothing more than a browser and a [Microsoft account](https://account.microsoft.com/account). Notebooks are contained in projects, whose primary purpose is to group related notebooks. In this exercise, you will create a new project and then create a notebook inside it.

1. Navigate to https://notebooks.azure.com in your browser and sign in using your Microsoft account. Click **My Projects** in the menu at the top of the page. Then click the **+ New Project** button at the top of the "My Projects" page.

1. Create a new project named "Data Handling in Python." Check the "Public" box if you'd like to share notebooks with other people later on. You can also go into project settings once a project is created and change its visibility to public or private. 

	![Creating a project](media/add-project.png)

	_Creating a project_

1. Click **+ New** and select **Notebook** from the menu to add a notebook to the project.

	![Adding a notebook to the project](media/add-notebook-1.png)

	_Adding a notebook to the project_

1. Name the notebook "Flight Delays.ipynb," and select **Python 3.6** as the language. This will create a notebook with a Python 3.6 kernel for executing Python code. One of the strengths of Azure notebooks is that you can use different languages by choosing different kernels.

	![Creating a notebook](media/add-notebook-2.png)

	_Creating a notebook_

	If you're curious, the **.ipynb** file-name extension stands for "IPython notebook." Jupyter notebooks were originally known as IPython (Interactive Python) notebooks, and they only supported Python as a programming language. The name Jupyter is a combination of Julia, Python, and R — the core programming languages that Jupyter supports.

1. Click the notebook to open it for editing.

You can create additional projects and notebooks as you work with Azure Notebooks. You can create notebooks from scratch, or you can upload existing notebooks. And once a notebook is created or uploaded, you can take advantage of Azure compute resources to run the notebook and leverage popular Python libraries such as [Keras](https://keras.io/), [NumPy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [Scikit-learn](https://scikit-learn.org/stable/index.html).

## Analyze flight information

Now it's time to write *real* code to operate on *real* data. In this exercise, you will load a CSV file containing 99 rows of data regarding flight delays at a selection of U.S. airports on October 1, 2018. From the data, you will answer the following questions:

- What was the mean (average) delay time? 
- How many flights arrived more than 10 minutes late?
- What was the longest delay for any flight on that date?

Start by deleting the two cells you added to the notebook. (This isn't strictly necessary, but we may as well keep the notebook clean.) Then proceed to load and analyze the data.

1. Enter the following statement in the notebook's first cell and click the **Run** button to execute it:

	```bash
	!curl https://topcs.blob.core.windows.net/public/flight_delays.csv -o flight_delays.csv
	```

	This statement uses Bash's `curl` command to load a CSV file from Azure blob storage. You can execute Bash commands in Azure notebooks by preceding them with exclamation points (!).

1. Add the following code to the next cell and run it to load the contents of the CSV file into memory in a NumPy array and show the column names:

	```python
	import numpy as np

	flight_data = np.genfromtxt('flight_delays.csv', delimiter=',', dtype=None, names=True, encoding=None)
	print (flight_data.dtype.names)
	```

1. Now use the following statement to show the contents of the array:

	```python
	print (flight_data)
	```

	Each row contains data for one flight. The 12th column — ARR_DELAY — tells us in minutes how late a flight arrived. A negative number indicates the flight arrived early. Zero indicates it arrived on time. A positive number indicates that the flight was late.

1. Use the array's `mean()` function to determine the mean of the values in the ARR_DELAY column for all flights: 

	```python
	print(flight_data['ARR_DELAY'].mean())
	```

	What was the mean delay time? On average, did flights arrive early or on time on that date?

1. To determine how many flights were delayed more than 10 minutes, use a comprehension to create a list and a filter to ignore flights that don't fit the criterion:

	```python
	delayed_flights = [flight for flight in flight_data if flight['ARR_DELAY'] > 10]
	print(len(delayed_flights))
	```

	How many flights were delayed by more than 10 minutes?

1. To figure out the longest delay, use `nparray`'s `max()` function to find the largest value in the ARR_DELAY column:

	```python
	print(flight_data['ARR_DELAY'].max())
	```

1. Suppose you want to print the airline code and flight number for the flight that experienced the longest delay. That's the perfect excuse to use another list comprehension:

	```python
	max_delayed_flight = [flight for flight in flight_data if flight['ARR_DELAY'] == flight_data['ARR_DELAY'].max()]
	print(max_delayed_flight[0][1] + ' ' + str(max_delayed_flight[0][3]))
	```

Observe that the final statement uses column indexes rather than column names. The call to `str()` converts the flight number into a string so it can be printed. Seeing that the flight number is just that — a number and not a string — `genfromtxt()` loaded it as an integer rather than a string.

