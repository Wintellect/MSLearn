# Create a class

In OOP terms, a class defines how to create a Python object. You can use a class to create as many objects as you need, but the class must describe how to create an object before it can create any objects at all.

In this lesson, you will create a class in Python and then use the class to instantiate an object. The term "instantiate" is just a fancy way of saying that Python uses the class to create an object. Just as you use a blueprint to create a house or a recipe to create a cookie, Python uses classes to create objects.

To run your Python code, you will use [Jupyter notebooks](https://jupyter.org/). Jupyter is an environment based on [IPython](https://ipython.org/) that facilitates interactive programming and data analysis using a variety of programming languages, including Python. Jupyter notebooks enjoy widespread use in research and academia for mathematical modeling, machine learning, statistical analysis, and for teaching and learning how to code.

## Create a notebook

[Azure Notebooks](https://blogs.msdn.microsoft.com/uk_faculty_connection/2017/06/10/guide-to-the-microsoft-azure-notebooks-for-students/) is a cloud-based platform for building and running [Jupyter notebooks](http://jupyter.org/). Azure Notebooks provide Jupyter as a service for free. It's a convenient way to build notebooks and to share them with others without having to install and manage a Jupyter server. And it's completely Web-based, making it an ideal solution for online collaboration.

Azure notebooks are created through the portal at https://notebooks.azure.com and require nothing more than a browser and a [Microsoft account](https://account.microsoft.com/account). Notebooks are contained in projects, whose purpose is to group related notebooks. In this exercise, you will create a new project and then create a notebook inside it.

1. If you don't have a Microsoft account, go to https://account.microsoft.com/account and create one. Having a Microsoft account gives you access to a wealth of resources, many of which are free. Microsoft accounts are free as well.

1. Navigate to https://notebooks.azure.com in your browser and sign in using your Microsoft account. Click **My Projects** in the menu at the top of the page. Then click the **+ New Project** button at the top of the "My Projects" page.

1. Create a new project named "Lab Notebooks" or something similar.

	![Creating a project](media/add-project.png)

	_Creating a project_

	Leaving the "Public" box checked makes it easy to share notebooks later on. You can also go into project settings once a project is created and change its visibility to public or private.  

1. Click **+ New** and select **Notebook** from the menu to add a notebook to the project.

	![Adding a notebook to the project](media/add-notebook-1.png)

	_Adding a notebook to the project_

1. Give the notebook a name such as "Learn Python.ipynb," and select **Python 3.6** as the language. This will create a notebook with a Python 3.6 kernel for executing Python code. One of the strengths of Azure notebooks is that you can use different languages by choosing different kernels.

	![Creating a notebook](media/add-notebook-2.png)

	_Creating a notebook_

	If you're curious, the .ipynb file-name extension stands for "IPython notebook." Jupyter notebooks were originally known as IPython (Interactive Python) notebooks, and they only supported Python as a programming language. The name Jupyter is a combination of Julia, Python, and R — the core programming languages that Jupyter supports.

1. Click the notebook to open it for editing.

You can create additional projects and notebooks as you work with Azure Notebooks. You can create notebooks from scratch, or you can upload existing notebooks. And once a notebook is created or uploaded, you can take advantage of Azure compute resources to run the notebook and leverage popular Python libraries such as [Keras](https://keras.io/), [NumPy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [Scikit-learn](https://scikit-learn.org/stable/index.html).





## OOP in Python

Everything is an object in Python. It would be easy to confuse the Python programming paradigm, the method used to create code, with the underlying language concepts. A programming paradigm would allow you to use the [functional, imperative, object-oriented, or procedural coding styles](https://blog.newrelic.com/engineering/python-programming-styles/). However, no matter which programming paradigm you use, Python itself uses objects for everything.

This section is about Python as a language. Later, you learn about the OOP programming paradigm that Python supports.

To see how objects work in Python, open a [new Azure Notebook session](https://notebooks.azure.com/). (You must sign in using your Microsoft account before you can access any of the Azure Notebook features.) Once you sign in, create a new notebook. You don't really need to assign the notebook a name because you won't hold onto it, but the example uses the name Test. Once you have a new notebook to use, type the following code into it:

```python
print(type(1))
print(type("Hello There!"))
print(type(1.1))
print(type(True))
```

You use the `print()` function to display output on screen. The `type` function shows an object's underlying class. In this case, 1, "Hello There!," 1.1, and True are all objects, which means that they have a class associated with them. Click Run, and you see the output shown here:

![Displaying the classes associated with objects](media/tk.png)

_Displaying the classes associated with objects_

The output shows that the object 1 has a class of `int`, while "Hello There!" has a class of `str`. Notice that Python uses different classes for 1 and 1.1; the class of 1.1 is `float`. If something has a truth value, True or False, then it relies on the `bool` class.

You could easily test other kinds of data (go ahead if you want to experiment!), but be assured that any sort of data you try has a associated class, which means that the data is an object: an instance of that class.

Most classes have methods associated with them. Type the following code into the next cell:

```python
print(dir(1))
```

The `dir()` function provides a directory of things you can do with an object: its methods. You also see methods referred to as *functions* when working with Python. The two terms are viewed as synonymous, but you avoid confusion when talking with other people if you simply call them methods. 

Click **Run**, and you see the output shown here:

![Displaying the methods associated with objects](media/tk.png)

_Displaying the methods associated with objects_

All the entries you see, such as `to_bytes()`, are methods. Remember that a method always represents an action—something you can do. For example, `to_bytes(`) outputs the object value in byte format, which is just a special way of looking at the data. Don't worry about this particular method for now. Even though the methods exist for any value, let's try them out with a variable.

Notice the `__str__()` method in the list. This method turns the value into a `str` (string) type. Saying type means that an object relies on a certain class. So, the type of 1 is `int`.

Type the following code into the next cell:

```python
myVar = 1
print(type(myVar.__str__()))
```

The first line is an assignment. You're assigning the value 1 to an object named `myVar`. The `myVar` object now has an attribute, that of the value 1. The second line of code calls the `__str__()` method that is part of the `int` class and therefore present in the `myVar` object.

Click **Run** and you see the output shown here:

![Using methods changes objects](media/tk.png)

_Using methods changes objects_

The `__str__()` method has created as new object from `myVar` of type `str`. The `myVar` object is still the same, completely untouched; it's still of type `int`. The new object – which doesn't have a name because you haven't assigned it one – is of type `str`.

You often use methods to create new objects that have attributes you need from existing objects. At this point, you have enough information about Python classes and objects to start creating a class of your own.

## Defining classes

Every Python class you create begins with the word `class` (which makes sense). Of course, a class needs a name. Also you must define where the class identification ends; Python uses a colon.

A class also needs to do something. Let's begin with something simple: telling the user that the class has been created. In the real world, you wouldn't actually create a class like this, but it's helpful in learning a little at a time.

Type the following code into your test project:

```python
class myClass:
    print('myClass created!')
```

This is the simplest class you can create. It contains the bare essentials needed to create a class:

- The keyword `class`
- The class name ("myClass")
- A colon to indicate that the class identification is over

Notice that the next line is indented. This is important! Python uses indentation to show structure. In this case, the `print()` function is part of `myClass`.

Click Run and you see the following output:

![Create classes using the class keyword](media/tk.png)

_Create classes using the class keyword_

The output shows that you actually created the class. The `print()` function executes during the creation process. Normally, you wouldn't have a `print(`) statement like this, but here it helps to see how the class creation works.

## Instantiating classes to create objects

At this point, you have a very simple (and nearly useless) class, but it serves to show how objects work with classes. To make a class useful, you need to instantiate an object from it.

Type the following code to see how this process works:

```python
myVar = myClass()
print(type(myVar))
print(dir(myVar))
```

The first line creates the object, `myVar`, from the class `myClass`. Notice the parentheses after `myClass`. The parentheses tells Python to create an object: an instance of the class.

To determine whether the process worked, you can use the `type()` and `dir()` functions, just as you did earlier in the unit.

Click Run and you see the following output:

![Creating an instance of myClass](media/tk.png)

_Creating an instance of myClass_

Notice the output shows that the type of `myVar` is `__main__.myClass`. The `__main__` part of the output is the scope in which this code is executing. A scope is a kind of container that holds pieces of code together. You don't see a scope for the int type because the int type is defined outside the scope of the current application. You see `__main__` for `myClass` because you define `myClass` within the current application. It's the default scope; but you don't need to worry about it for now. The important takeaway, for the moment, is that `myVar` actually is an instance of the `myClass` class.

In addition, notice that you get default methods with your new class. Python provides a class with these default methods to perform essential tasks. However, the methods aren't really functional now. It's simply a good idea to know that they exist. As you continue with these lessons, this information becomes more relevant.