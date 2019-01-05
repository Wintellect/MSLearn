# Get started with Python and Azure Notebooks

In order to learn Python, you need an environment in which to execute Python code. One option is to download a Python distribution from the [Python Web site](https://www.python.org) and install it on your PC or laptop. Versions are available for Windows, macOS, and a variety of Linux distributions. Another option is to download and install [Anaconda](https://www.anaconda.com), which is a specialized Python distribution tailored for scientific programming tasks such as data science and machine learning.

Another popular way to get started with Python — one that requires nothing more than a modern Web browser such as Edge or Chrome — is through [Jupyter notebooks](https://jupyter.org). Jupyter is an environment based on [IPython](https://ipython.org/) that facilitates interactive programming and data analysis using a variety of programming languages, including Python. Jupyter notebooks enjoy widespread use in research and academia for mathematical modeling, machine learning, statistical analysis, and for teaching and learning how to code.

[Azure Notebooks](https://notebooks.azure.com/) is a cloud-based platform for building and running [Jupyter](http://jupyter.org/) notebooks. Azure Notebooks provide Jupyter as a service for free. It's a convenient way to build notebooks and share them with others without having to install and manage a Jupyter server. And it's completely Web-based, making it an ideal solution for collaborating online.

In this lesson, you will create  an Azure notebook and use it to learn some of the basics of Python. In subsequent lessons, you will expand the notebook to tk.

## Create an Azure notebook

The first order of business is to create an Azure notebook. Azure notebooks are contained in projects, whose primary purpose is to group related notebooks. In this exercise, you will create a new project and then create a notebook inside it.

1. If you don't have a Microsoft account, go to https://account.microsoft.com/account and create one. Having a Microsoft account gives you access to a wealth of resources, many of which are free. Microsoft accounts are free as well.

1. Navigate to https://notebooks.azure.com in your browser and sign in using your Microsoft account. Click **My Projects** in the menu at the top of the page. Then click the **+ New Project** button at the top of the "My Projects" page.

1. Create a new project named "Lab Notebooks" or something similar.

	![Creating a project](media/add-project.png)

	_Creating a project_

1. Click **+ New** and select **Notebook** from the menu to add a notebook to the project.

	![Adding a notebook to the project](media/add-notebook-1.png)

	_Adding a notebook to the project_

1. Give the notebook a name such as "Learn Python.ipynb," and select **Python 3.6** as the language. This will create a notebook with a Python 3.6 kernel for executing Python code. One of the strengths of Azure notebooks is that you can use different languages by choosing different kernels.

	![Creating a notebook](media/add-notebook-2.png)

	_Creating a notebook_

	If you're curious, the .ipynb file-name extension stands for "IPython notebook." Jupyter notebooks were originally known as IPython (Interactive Python) notebooks, and they only supported Python as a programming language. The name Jupyter is a combination of Julia, Python, and R — the core programming languages that Jupyter supports.

1. Click the notebook to open it for editing.

You can create additional projects and notebooks as you work with Azure Notebooks. You can create notebooks from scratch, or you can upload existing notebooks. And once a notebook is created or uploaded, you can take advantage of Azure compute resources to run the notebook and leverage popular Python libraries such as [Keras](https://keras.io/), [NumPy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [Scikit-learn](https://scikit-learn.org/stable/index.html).

## Input and output in Python

The purpose of creating the notebook is to have a platform for entering and executing Python code. A great way to get started with Python is learning how to read input from the keyboard, write output the screen, and include comments in your code.

### Writing output to the screen

In Python, the `print` statement outputs data to the screen. The following line of code displays "Hello World!" on the screen:

```python
print('Hello World!')
```

The data to be displayed is passed as an argument to the `print` statement. In this case, the argument is a sequence of characters known as a *string*. The string includes all of the text in single quotes but does not include the quotation marks themselves. Strings are one of the most common data types in computer programming. Python has extensive support for strings and provides many useful features for working with them.

### Reading keyboard input

`input` is used to read input from the keyboard. Unlike `print`, which is a statement, `input` is a *function*. A statement is a command that runs some code but does not return a value. A function is a command that runs some code and returns a value. The `print` statement simply outputs the string passed to it to the screen. It does not return a value. The `input` function, by contrast, reads what the user types on the keyboard and returns it as a string.

Here is an example that uses the `input` function to capture a person's name and then display it on the screen:

```python
name = input('Enter your name:')
print(name)
```

The string passed as an argument to the `input` function is the prompt that the user will see. In this example, you are asking the user to type his or her name. The user types his or her name and presses **Enter**, causing the `input` function to return. The function's return value is the name that the user typed, and that name is assigned to the variable named `name`. The `name` variable is then used as an argument to the `print` statement to output the user's name to the screen.

### Commenting your code

All programming languages support including comments in source code. Comments are not executable statements. Instead, they serve to explain how the code works or why it was written that way. Comments are a great way to document complicated code and to include TODOs reminding you to come back and do something later — for example, "make sure this code works with empty strings."

Python supports comments using the pound sign (or hashtag) followed by the text of the comment:

```python
# I am a comment...
```

Comments are one-line only. For multiline comments, place a pound sign at the start of each line.

Some programmers tend to eschew comments in favor of writing "self-documenting code," which is somewhat self-explanatory as a result of descriptive variable and function names. There is nothing wrong with self-documenting code, but never hesitate to use comments in an effort to be as explicit as possible about your thoughts and intentions. The purpose of a block of code may be clear to you because you wrote it 10 minutes ago. But a year from now, a well-placed comment may be as helpful to you as it is to other programmers who are seeing your code for the first time. 

## Add code to the notebook

Now let's use what you just learned in the notebook you created a few moments ago.

Jupyter notebooks are composed of *cells*. Each cell is assigned one of four types:

- **Markdown** for entering text in [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) format
- **Code** for entering code that runs interactively
- **Raw NBConvert** for entering data inline
- **Heading** for section headers   

Code entered into code cells is executed by a *kernel*, which provides an isolated environment for the notebook to run in. The popular IPython kernel supports code written in Python, but [dozens of other kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) are available supporting other languages. Azure Notebooks support Python, R, and F#. They also support numerous packages and libraries that are commonly used in Python.

1. Return to the notebook that you created a few moments ago. Type (or paste) the following Python code into the empty cell at the top of the notebook:

	```python
	print('Hello, World!')
	```

1. Now click the **Run** button to run the cell and add a new cell after it. Confirm that "Hello, World!" appears in the output of the first cell:

	![Running the first cell](media/first-run.png)

	_Running the first cell_

1. Type the following statements into the empty cell at the end of the notebook:

	```python
	name = input('Enter your name: ')
	print('Hello, ' + name)
	```

1. Run the cell. When prompted, type your name and press **Enter**. Confirm that a personalized greeting appears in the output:

	![Running the second cell](media/second-run.png)

	_Running the second cell_

1. Modify the code in the cell you just executed to include comments:

	```python
	# Ask for the user's name
	name = input('Enter your name: ')

	# Display a personalized greeting
	print('Hello, ' + name)
	```

1. Run the cell and confirm that it behaves the same as it did before.

	![Running the modified cell](media/third-run.png)

	_Running the modified cell_

1. Use the **File** -> **Save and Checkpoint** command to save the notebook.

Now that the notebook is saved, you can return to it later and pick up where you left off, even if you close the notebook or close the browser.