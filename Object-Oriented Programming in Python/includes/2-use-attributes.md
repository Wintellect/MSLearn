# Define characteristics with attributes

Attributes tell you about an object. Saying that a flower is pink tells you about the color of the flower. The color pink is an attribute of the flower. It's possible to create Python classes without attributes, but then you know nothing about the object. In other words, the object may as well not exist because there is nothing to say about it. Therefore, you never see useful Python classes that lack attributes.

When dealing with a built-in Python class (a class that comes with Python), such as an `int`, the class defines the attributes for you. An instance of the `int` class has a single attribute, a number, such as the value 1. The `int` class is relatively simple in that it only has one attribute — the numeric value — but you can create classes that have more attributes. In fact, to be truly useful, most classes need more than one attribute.

Think about a blueprint for a house that contains only one piece of wood or a recipe that contains only one ingredient. They wouldn't be particularly useful. The real world is full of examples where the description of an object, its class, requires the use of more than one attribute. Consequently, you can view the various pieces of wood, screws, nails, and other elements of a house blueprint to be the attributes of that house. The various ingredients (attributes) of a recipe could include chocolate, flour, eggs, butter, and so on.

In this unit, you start defining a class to hold the information needed by the missing relatives database. To make things simple, you create a `mRelative` class to hold a single relative. You can then use the functionality in Python to turn each of the individual relatives into a list of missing relatives.

## Class attributes vs. instance attributes

Attributes come in two varieties: class attributes and instance attributes. A class attribute is one that applies to *all* instances of a class rather than to individual instances (objects created from the class). For example, if you wrote a `person` class for the missing-persons app, you could include a class attribute indicating the total number of people in the database. The value of that attribute wouldn't be tied to individual `person` instances.

An instance attribute is one that is "instanced" for each and every object you create. A `person` class might have a `name` attribute that holds a person's name. `name` would need to be an instance attribute so every `person` could be assigned a different name. That class could also have attributes defining additional information about a missing person, such as:

- Photos of the person's face
- A photo number identifying a particular facial photo
- A unique ID for the person such as a Social Security number

You can certainly define other attributes, but these instance attributes will do fine for the example. Knowing these pieces of information will tell you enough to locate additional information about the missing person. The picture number and picture content come from the downloadable database, you provide a name based on what you know about the person, and the cabinet file number is based on the system you use for filing additional details in your filing cabinet.

## Load a database of faces

Let's begin building a missing-persons example by loading a database of facial images. The dataset you will load is a publicly available one called the [Olivetti Faces dataset](https://scikit-learn.org/0.19/datasets/olivetti_faces.html) and was originally created by AT&T.

1. Return to the Azure Notebooks project you created in the previous unit and create a new Python 3.6 notebook named **Missing Persons.ipynb** or something similar. Then open the notebook.

1. One of the many popular packages available in Azure Notebooks is [Scikit-learn](https://scikit-learn.org/stable/index.html), which is an open-source library used build [machine-learning](https://en.wikipedia.org/wiki/Machine_learning) models. Scikit includes several built-in datasets, one of which is the Olivetti faces dataset.

	Paste the following statements into the empty cell at the top of the notebook to load the faces dataset:

	```python
	from sklearn.datasets import fetch_olivetti_faces
	
	# Load the dataset
	faces = fetch_olivetti_faces()

	# Prove that the dataset was loaded
	print(faces.data.shape)
	```

	The first line imports the Scikit function that loads the datset. The second loads the dataset, and the third shows the shape of the dataset.

1. Run the code and examine the output. The dataset contains 400 faces, each of which consists of an image with 4,096 pixels. The dataset contains 10 photos each of 40 different people. The first ten images in `faces.images` represent the first person, the next 10 images represent the second person, and so on.

1. Want to see what the faces look like? Paste the following statements into the next cell and run them:

	```python
	%matplotlib inline
	import matplotlib.pyplot as plt
	
	# Plot the first 50 faces
	fig, axes = plt.subplots(5, 10, figsize=(12, 7), subplot_kw={'xticks': [], 'yticks': []})
	
	for i, ax in enumerate(axes.flat):
	    ax.imshow(faces.images[i], cmap=plt.cm.gray)
	```

	The code begins with something quite odd — a statement that starts with a percent sign. This is a "magic function" that relates specifically to Jupyter notebooks. It tells Jupyter to display graphics inline with the rest of the material in the notebook, which is quite handy when you need to visualize data.

	The next statement imports a module from the versatile [Matplotlib](https://matplotlib.org/) library and gives it the name `plt` to make it easier to use. The remaining statements use Matplotlib's `imshow()` function to display the images.

1. Confirm that the output resembles the following:

	![The first five people in the Olivetti dataset](media/show-faces.png)

	_The first five people in the Olivetti dataset_

Now that we have some faces to work with, let's shift our thinking to objects, classes, and attributes.

## Defining class attributes

It would be handy to know how many faces the dataset contains. However, the number might change each time you load the dataset from the source location. In addition, the Olivetti Faces dataset provides ten different views of each face, so just downloading the dataset and checking the shape still doesn't tell you the number of faces in the dataset. In order to know how many faces the dataset contains, you need a class attribute — one that won't vary when you create a class instance. Use this code to create the initial class and the class attribute:

```python
class mRelative:
    num_faces = int(faces.data.shape[0] / 10)
```

The class begins with the `class` keyword, followed by the class name, as usual. You already know that `faces.data.shape` contains the size of the dataset. The number of pictures appears as the first element in the list, which is element 0 because Python uses zero-based indexes. So, `faces.data.shape[0]` returns the number of pictures. You then divide this value by 10 because you know that there are ten pictures of each face. Enclosing this math in `int()` turns the floating point number that the division normally returns into an integer because you can't have part of a face — the dataset only contains whole faces.

You don't know that the code has worked though, which means you need to test it. Class attributes are always available. You don't have to create an instance of the class to access the class attributes. Consequently, you can perform the following test to see the number of faces in the Olivetti Faces dataset.

```python
print(mRelative.num_faces)
```

When you run this code, you see the output shown here—the expected 40 faces:

![tk](media/tk.png)

_tk_

## Defining instance attributes

Instance attributes differ from one class instance (object) to another. You can't access them from the class, as you can with class attributes. Instead, you must create an instance of the object and assign values to the attributes. Python provides multiple ways to create instance variables, but the most common is to define an `__init__()` function that contains the attributes you want the object to have once created. Add the instance attributes to the `mRelative` class as shown here:

```python
class mRelative:
    num_faces = int(faces.data.shape[0] / 10)
    
    def __init__(self, pic_num, name, cab_file):
        self.pic_num = pic_num
        self.pic_cont = faces.images[pic_num * 10]
        self.name = name
        self.cab_file = cab_file
```

This new code starts by defining function using def, just as you normally do with Python. The `self` variable refers to the object. When you talk about yourself, you say "myself", not someone else's name. Likewise, when a Python object wishes to refer to its specific instance, it uses `self`.

The input arguments: `pic_num`, `name`, and `cab_file` are variables containing attributes that you learned about earlier in the unit. However, you might wonder where the picture content attribute is. This is an attribute that you obtain programmatically from the dataset. So, you see that the code that follows assigns the `pic_num` variable (the picture number attribute) to `self.pic_num` — the instance variable associated with this object. Assigning the other attributes follows the same pattern.

Assigning a value to `self.pic_cont` is different because the image content appears in a different part of the dataset. In order to display the image later, you must obtain it from `faces.images`, rather than `faces.data`. Remember that there are 10 images for each face, so if you want the image for face 0, then you use image 0, but if you want the image for face 1, then you actually need image 10.

It's time to test these new attributes. The following code creates an instance of `mRelative` as `aRelative`. It uses face 0, gives the entry the name "Stan," and assigns Stan's data to file cabinet entry 123.

```python
aRelative = mRelative(0, "Stan", 123)
print(aRelative.num_faces)
print(aRelative.name, " is number ", 
      aRelative.pic_num, " in cabinet ", 
      aRelative.cab_file)
```

After you create the object, you can use `print()` to test it. Notice that an object has access to both class and instance attributes. If you were to try to print instance attributes from `mRelative`, Python would tell you that these attributes don't exist. Here is the output from this part of the example:

![tk](media/tk.png)

_tk_

## Implementing data hiding

Python doesn't actually allow you to truly hide data — at least not in the same sense that other languages do anyway. Guido van Rossum, the creator of Python, felt that data hiding in the conventional sense actually made languages harder to use. Consequently, you can't hide anything in Python. As an adult, it's expected that you'll follow the rules in working with data. Of course, you still need some means of telling others that it's not a good idea to play with particular variables.

When working with Python, you rely on a convention for data hiding. A public variable, one that anyone can work with, has just a name. If you add an underscore, such as `_myProtectedVar`, then the variable is marked as protected, even though it actually isn't. You could still access it, but everyone is hoping you won't. A protected variable is meant to be accessible only within the host class and any subclasses you create.

You can also create private variables using two underscores, such as `__myPrivateVar`. In this case, you should only access the variable within the class that created it. Accessing it even in a subclass could cause problems.

All this said, if you make an attribute protected or private when working in environments such as Jupyter, the environment will enforce the level of data hiding you request and the code won't be able to access it. So, in this respect, Python does implement data hiding, but it's only by convention and you need to be aware of that when you send your code to parts unknown.

## Displaying faces

You still haven't seen a picture. The picture is there, but you need to do something special to see it. The easiest way to display a picture with Python is to use the [matplotlib](https://matplotlib.org/) package. For now, you just need it to display the picture hiding in the `aRelative.pic_cont` attribute. The following code shows the quickest method for accomplishing this task:

```python
%matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(aRelative.pic_cont)
plt.show()
```

The code begins with something quite odd — a command that starts with a percent sign. This is a "magic function" that relates specifically to Jupyter notebooks. It tells Jupyter to display graphics inline with the rest of the material in the notebook, which is actually quite handy when you need to create a report.

The code the follows imports the specific module you need from `matplotlib.pyplot` and gives it the name `plt` to make it easier to use. You then use the special `imshow()` function to read the `aRelative.pic_cont` attribute. However, nothing shows on screen until you call `plt.show()`. Here's what you can expect to see:

![tk](media/tk.png)

_tk_