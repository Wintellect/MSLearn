# Create an Azure notebook

To get started with Python programming a development environment needs to be configured. There are several ways to utilize Python. One common way is to download Python from the Python website: [https://www.python.org](https://www.python.org). The website will provide an installer and source code to enable installing Python on a myriad of environments including Microsoft Windows, Apple's macOS, and all Linux distributions. In addition to the standard Python distribution, there are specialized distributions such as Anaconda, [https://www.anaconda.com](https://www.anaconda.com). Anaconda is a specialized distribution for scientific programming including data science and machine learning. Another popular way to get started with Python is through Jupyter Notebooks, [https://jupyter.org](https://jupyter.org).

Jupyter Notebooks is a web application which enables developers to write and execute Python programs within a web browser. They are great for learning Python and performing various experiments such as training a machine learning model. Jupyter Notebooks can be launched from within the Anaconda distribution on a local machine or used in the cloud through a service such as Azure Notebooks: [https://notebooks.azure.com](https://notebooks.azure.com).

In this course, Azure Notebooks will be used to write and execute all of the code. This will enable you to get up and running will little setup as well as explore the great Jupyter Notebook service which Azure provides. To get started visit, [https://notebooks.azure.com](https://notebooks.azure.com), register for an account (or sign in with an existing Microsoft Azure Account) to get started.

### Using a Microsoft Account

To get started Azure Notebooks a Microsoft account will be needed. If you already have one, then all that is need to associate the account with Azure Notebooks and give Azure Notebooks permission to access your account. To enable this access do the following:

1. Open a web browser (such as Microsoft Edge), and browse to [https://notebooks.azure.com](https://notebooks.azure.com)
1. Click the "Sign-In" link in the upper right-hand corner. Login as normal to Microsoft and when presented with any dialogs asking for permission to connect Azure Notebooks to your account grant the permission requested.

If you do not have a Microsoft account then do the following:

1. Open a web browser (such as Microsoft Edge), and browse to [https://notebooks.azure.com](https://notebooks.azure.com)
1. Click the 'Sign In' link and follow the prompts to create a new account. You will need a working email address to complete the registration process.
1. Once registration is complete, a dialog will be presented asking for permission to connect Azure Notebooks to your account, grant the permission requested.

### Creating and Running a Notebook

Creating a new notebook is very easy. If you have no notebooks, Azure Notebook will present you a link to create a new project. Projects contain notebooks, and in order to create a notebook, we must have a project to place it in. Click the link and follow the prompts to create a new project.

Once the project is created you will see a file listing with a single README.md file listed. The README.md file is for projects notes. The README.md file is not a Jupyter Notebook and cannot run any Python code.

To create a new notebook book, click the dropdown with the plus "+" symbol on it. The first option will be to create a new notebook. You will be presented with several language options. One very cool thing about Azure is the different languages which are pre-configured including different versions of Python, R as well as F#! For this course, choose the latest version of Python 3 (which at this time is Python 3.6).

For the notebook name, specify "Hello World", then click "New". The dialog will disappear and the file list will appear again. Click the on the name of the new notebook and the notebook will be loaded and coding can begin.

### Duplicating and Renaming Notebooks

Add content here...

### Displaying Data to the Screen

The **print** statement outputs data to the screen.

    Note: Technically, the **print** statement outputs to something called **stdout**. The default value of **stdout** is the screen. Nevertheless, it is possible (but beyond scope of this tutorial) to change the destination of **stdout**. Changing the destination of **stdout** would change the destination of the print statement.

Here is an example of using the **print** statement to display "Hello World!":

```python
print('Hello World!')
```

Observe that the data to be displayed is passed as an argument to the print statement. An argument is used to pass data into statements and functions. Within the statement or function, the data is used to customize its operation. In this case, the data is a sequence of characters known as a string. The string includes all of the text between the single quotes but does not include the quotes themselves. Strings are one of the most common types of data used in computer programs. As will be discussed later, Python has extensive support for strings providing many useful features for working with them.

### Collecting Keyboard Data

The **input** function is used to collect keyboard data and returned the user entered data. Unlike **print** command which is referred to as a statement, the **input** command is referred to as a function. A statement is a command which runs some code but does not return a value. A function is a command which runs some code and returns a value. The **print** statement simply outputs to the screen the data passed to it, there is nothing to return. On the other hand, the **input** function collects user entered keyboard data and returns it to the program. Because it returns data, it is called a function.

    Note: Technically, the **input** function collects data from **stdin**. The default value for **stdin** is the keyboard.  Nevertheless, it is possible (but beyond scope of this tutorial) to change the source of **stdin**. Changing the source of **stdin** would change the source from which the **input** function collects data.

Here is an example of using the **input** function to capture a person's age and then display it on the screen:

```python
age = input('Enter your age:')
print(age)
```

Observe the string passed as an argument to the **input** function. The string is the prompt which the user will see so they know what kind of data is being requested. In this case, the age of the user is being requested. Once the user enters their age and presses "enter" or "return" the **input** function returns the data and assigns to the variable named **age**. Variables are covered in detail in the next section but for now, think of them as a place to temporarily store data in your application.

The variable **age** is then used as an argument to the **print** statement to output data to the screen.

### Commenting Python Code

All programming languages provide some kind of mechanism to add comments to the source code. The comments are not executable code but serve to explain to other programmers how some section of code executes. Comments are a great way to explain complicated programming code, explain why something needs to be done or just serve as a reminder to do something.

Python supports comments using the pound sign (or hashtag) followed by the text of the comment. Comments are one-line only. For multi-line comments, a pound sign (or hashtag) must be placed at the start of each line.

# I am a comment…

Many developers write what is known as self-documenting programming code to avoid lots of comments. Self-documenting code is code which reads pretty easily through very descriptive variable and functions names and avoidance of confusing programming control structures. Such code is good and can reduce the number of comments required but never hesitate to add a comment to programming code if you think it would be helpful to explain the why and how of what the code is trying to achieve.


### Documenting a Notebook

In addition to writing and executing Python code, notebooks can contain documentation as well. To help format the documentation, Markdown is used. Markdown is commonly used to format text documents with a simple syntax. Markdown is converted to HTML which displays with nice formatting within a web browser.

When adding a cell to the notebook, change the content from 'Code' to 'Markdown'. To view the formatted output, run the cell.

To create text which is formatted as a header the following syntax is used:

```markdown
# Hello World Notebook
```

To create a list of items:

```markdown
* Item 1
* Item 2
* Item 3
```

To add links to other pages:

```markdown
[Microsoft](http://www.microsoft.com)
```

The value within the square brackets is the label for the link and the value within the parentheses is the URL.

### Exercise: Creating a Notebook to Import Airport Data

**Step 1.** Open a web browser and browse to [https://notebooks.azure.com](https://notebooks.azure.com). Log in with your Microsoft account (or create a Microsoft Account)

[Screenshot of Microsoft Account Login]

**Step 2.** Create a new project named "Introduction to Python".

[Screenshot of Create a Project]

**Step 3.** Within the project, create a new notebook named "Prepare US State Airport Data".

[Screenshot of Create a Notebook]

**Step 4.** In the first cell, enter the following Python code.

```python
print('Hello <Your Name>!')
```

Replace '\<Your Name\>' with the name of your choice.

**Step 5.** Run the cell by clicking 'Run'.

[Screenshot of Run Button]

The output will look like this:

[Screenshot of Output]

**Step 6.** Ask the user for their age the following line of code:

```python
input('What is your age?')
```

**Step 7.** Run the cell.

[Screenshot of the Output]

**Step 8.** Add a cell to the top of the notebook. Change the content from the 'Code' to 'Markdown'. Add the following content and run the cell.

```markdown
# Hello <Your Name>
```

Run the cell. The output will look similar to this:

[Screenshot of the Output]

