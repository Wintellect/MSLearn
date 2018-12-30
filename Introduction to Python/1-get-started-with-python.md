# Get started with Python

In order to learn Python, you need an environment in which to execute Python code. One option is to download a Python distribution from the [Python Web site](https://www.python.org) and install it on your PC or laptop. Versions are available for Windows, macOS, and a variety of Linux distributions. Another option is to download and install [Anaconda](https://www.anaconda.com), which is a specialized Python distribution tailored for scientific programming tasks such as data science and machine learning.

Another popular way to get started with Python — one that requires nothing more than a modern Web browser such as Edge or Chrome — is through [Jupyter notebooks](https://jupyter.org). Jupyter is an environment based on [IPython](https://ipython.org/) that facilitates interactive programming and data analysis using a variety of programming languages, including Python. Jupyter notebooks enjoy widespread use in research and academia for mathematical modeling, machine learning, statistical analysis, and for teaching and learning how to code.

[Azure Notebooks](https://notebooks.azure.com/) is a cloud-based platform for building and running [Jupyter](http://jupyter.org/) notebooks. Azure Notebooks provide Jupyter as a service for free. It's a convenient way to build notebooks and share them with others without having to install and manage a Jupyter server. And it's completely Web-based, making it an ideal solution for collaborating online.

In this lesson, you will learn the basics of Python. Then you will create a Jupyter notebook in Azure Notebooks and use it to execute some simple Python code that reads input from the keyboard and echoes it to the screen.

## Learn the basics of Python

A great way to get started with Python is learning how to read input from the keyboard, write output the screen, and include comments in your code.

### Writing output to the screen

In Python, the `print` statement outputs data to the screen. The following line of code displays "Hello World!" on the screen:

```python
print('Hello World!')
```

> Technically, the `print` outputs to `stdout`, which is short for *standard output*. The default destination for output written to `stdout` is the screen. It is possible (but beyond scope of this tutorial) to change the destination of `stdout`. Changing the destination of `stdout` would change the destination of the print statement.

The data to be displayed is passed as an argument to the `print` statement. Arguments are used to pass data. In this case, the argument is a sequence of characters known as a *string*. The string includes all of the text in single quotes but does not include the quotation marks themselves. Strings are one of the most common data types in computer programming. Python has extensive support for strings and provides many useful features for working with them.

### Reading keyboard input

`input` is used to read input from the keyboard. Unlike `print`, which is a statement, `input` is a *function*. A statement is a command that runs some code but does not return a value. A function is a command that runs some code and returns a value. The `print` statement simply outputs the string passed to it to the screen. It does not return a value. The `input` function, by contrast, reads what the user types on the keyboard and returns it as a string.

> The `input` function collects data from `stdin`, which is short for *standard input*. The default source of data for **stdin** is the keyboard. As with `stdout` it is possible to change the source of`stdin`.

Here is an example that uses the `input` function to capture a person's name and then display it on the screen:

```python
name = input('Enter your name:')
print(name)
```

The string passed as an argument to the `input` function is the prompt that the user will see. In this example, you are asking the user to type his or her name. The user types his or her name and presses **Enter**, causing the `input` function to return. The function's return value is the name that the user typed, and that name is assigned to the variable named `name`. Variables and data types will be covered in the next lesson, but for now, think of them as a place to temporarily store data in your application.

The variable `name` is then used as an argument to the `print` statement to output the user's name to the screen.

### Commenting your code

All programming languages support including comments in source code. Comments are not executable statements. Instead, they serve to explain how the code works or why it was written that way. Comments are a great way to document complicated code and to include TODOs reminding you to come back and do something later — for example, "make sure this code works with empty strings."

Python supports comments using the pound sign (or hashtag) followed by the text of the comment:

```python
# I am a comment...
```

Comments are one-line only. For multiline comments, a pound sign must be placed at the start of each line.

Some programmers tend to eschew comments in favor of writing "self-documenting code," which is somewhat self-explanatory as a result of descriptive variable and function names. There is nothing wrong with self-documenting code, but never hesitate to use comments in an effort to be as explicit as possible about your thoughts and intentions. The purpose of a block of code may be clear to you because you wrote it 10 minutes ago. But a year from now, a well-placed comment may be as helpful to you as it is to other programmers who are seeing your code for the first time. 

## Create an Azure notebook

Now let's use what you've learned to add some simple Python code to an Azure notbeook and execute the code. The first order of business is to create an Azure notebook. Azure notebooks are contained in projects, whose primary purpose is to group related notebooks. In this exercise, you will create a new project and then create a notebook inside it.

1. If you don't have a Microsoft account, go to https://account.microsoft.com/account and create one. Having a Microsoft account gives you access to a wealth of resources, many of which are free. Microsoft accounts are free as well.

1. Navigate to https://notebooks.azure.com in your browser and sign in using your Microsoft account. Click **My Projects** in the menu at the top of the page. Then click the **+ New Project** button at the top of the "My Projects" page.

1. Create a new project named "Lab Notebooks" or something similar.

	![Creating a project](media/add-project.png)

	_Creating a project_

1. Click **+ New** and select **Notebook** from the menu to add a notebook to the project.

	![Adding a notebook to the project](media/add-notebook-1.png)

	_Adding a notebook to the project_

1. Give the notebook a name such as "Prepare US State Airport Data.ipynb," and select **Python 3.6** as the language. This will create a notebook with a Python 3.6 kernel for executing Python code. One of the strengths of Azure notebooks is that you can use different languages by choosing different kernels.

	![Creating a notebook](media/add-notebook-2.png)

	_Creating a notebook_

	If you're curious, the .ipynb file-name extension stands for "IPython notebook." Jupyter notebooks were originally known as IPython (Interactive Python) notebooks, and they only supported Python as a programming language. The name Jupyter is a combination of Julia, Python, and R — the core programming languages that Jupyter supports.

1. Click the notebook to open it for editing.

You can create additional projects and notebooks as you work with Azure Notebooks. You can create notebooks from scratch, or you can upload existing notebooks. And once a notebook is created or uploaded, you can take advantage of Azure compute resources to run the notebook and leverage popular Python libraries such as [Keras](https://keras.io/), [NumPy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [Scikit-learn](https://scikit-learn.org/stable/index.html).

## Add code and markdown to the notebook

Jupyter notebooks are composed of *cells*. Each cell is assigned one of four types:

- **Markdown** for entering text in [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) format
- **Code** for entering code that runs interactively
- **Raw NBConvert** for entering data inline
- **Heading** for section headers   

Code entered into code cells is executed by a *kernel*, which provides an isolated environment for the notebook to run in. The popular IPython kernel supports code written in Python, but [dozens of other kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) are available supporting other languages. Azure Notebooks support Python, R, and F#. They also support numerous packages and libraries that are commonly used in Python.

The notebook editor currently shows an empty cell. In this exercise, you will add markdown content to that cell, and then add another cell containing Python code.

1. In the first cell, set the cell type to **Markdown**.

	![Creating a markdown cell](media/convert-to-markdown.png)

	_Creating a markdown cell_

1. Add the following markdown to the cell:

	```markdown
	# Prepare US State Airport Data
	
	In this scenario, a lookup table of airline data will be downloaded and processed to extract all airports for the specified US state abbreviation. The extracted airport data will be written to a new CSV file. The new CSV file name will be prefixed with the state abbreviation. This scenario represents a common situation in data science and machine learning where data is downloaded from public sources and prepared for specific experiments.
	
	## Preparation Steps
	* Input State Abbreviation
	* Define Variables
	* Read Airport File Data
	* Define Functions for Processing the Data
	* Write State Airport File Data
	* Download Airport File for Processing
	```

1. Click the **Run** button to run the cell and add a new cell after it.

	![Executing the first cell](media/run-first-cell.png)

	_Executing the first cell_

1. Type (or paste) the following code into the empty cell at the end of the notebook. The first statement prompts the user to enter the abbreviation for a U.S. state such as WA or TN. The second statement outputs to the screen the abbreviation that the user entered:

	```python
	state_abbr = input('Enter the state abbreviation of airport data to prepare:')
	
	print('Airport data for the state of ' + state_abbr + ' will be prepared.')
	```

1. Run the cell. Then type a state abbreviation and press **Enter**. Confirm that the abbreviation you typed is echoed to the screen.

	![Executing the second cell](media/run-second-cell.png)

	_Executing the second cell_

1. Modify the code in the cell you just executed to include comments:

	```python
	# Store the data entered by the user in the state_abbr variable
	state_abbr = input('Enter the state abbreviation of airport data to prepare:')
	
	# Output the state_abbr variable to the screen
	print('Airport data for the state of ' + state_abbr + ' will be prepared.')
	```

1. Run the cell and confirm that it behaves the same as it did before.

1. Use the **File** -> **Save and Checkpoint** command to save the notebook.

Now that the notebook is saved, you can return to it later and pick up where you left off, even if you close the notebook or close the browser.
