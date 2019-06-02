# Perform actions with methods

Methods tell an object what to do and how to do it. A `person` class might contain a `show_face()` method for displaying the person's face, and a `get_age()` method that returns the person's age. Methods frequently operate on data stored in attributes. For example, `get_age()` might subtract a birth date stored in an attribute from today's date to compute a person's age in years. 

Python objects always have methods, even if you don't define any yourself. For example, every object has a `__str__()` method added by Python itself that returns a string representation of the object. The default `__str__()` method works fine for something simple like an `int`, but it does nothing meaningful a `person` object. When you call `__str__()` on a `person` object, you get something like this:

`<__main__.person object at 0x7ff9e91ab978>`

For this reason, Python programmers frequently replace the built-in `__str__()` method with one of their own when they write custom classes to serve an application.

In this unit, you will add methods to the `mPerson` class you wrote in the previous unit to make it a first-class citizen in the Python environment. In addition to adding methods of your own, you will override the `__str__()` method so that it produces output that is meaningful for an `mPerson`. Finally, you will discover that when you pass an object to Python's built-in `str()` function, Python calls the object's `__str__()` method internally.

## Static methods vs. instance methods

Python objects support two types of methods: static methods and instance methods. Static methods apply to all objects of a certain type and can be called without instantiating the class to which the methods belong. Instance methods, on the other hand, apply to a specific object or class instance. A `get_age()` method should be an instance method because one person's age doesn't necessarily equal another person's age.

Only instance methods can access instance attributes. If you stored a person's birth date in an instance attribute, you couldn't read that birth date from a static method because there is no class instance associated with a static method — and therefore no birth date to read.  

## Defining static methods

Static methods work with your class, not with the object instantiated from the class. You can use a static method to create a nicely printed version of the number of faces in the Olivetti Faces dataset. You could do the same thing using special code every time, but the purpose of creating a class of this sort is so that you don't have to keep typing the same code repeatedly.

To create a static method, you add it to your class definition as shown here:

```python
class mRelative:
    num_faces = int(faces.data.shape[0] / 10)
    
    def __init__(self, pic_num, name, cab_file):
        self.pic_num = pic_num
        self.pic_cont = faces.images[pic_num * 10]
        self.name = name
        self.cab_file = cab_file
    
    @staticmethod
    def numFaces(before, after):
        return str(before) + str(mRelative.num_faces) + str(after)
```

The other code in this class defines the attributes. The code in bold is your first method. Notice the first line, `@staticmethod`. This is called a *decoration*, but what it really does is tell Python that this is a static method, not an instance method. There are other ways to determine the difference too, as you will see momentarily. For now, know that this decoration says that this is a static method that belongs to the class as a whole.

Below the decoration, you see the method, which accepts two arguments, before and after. The before argument contains content that appears before the number of faces, while the after argument contains content that appears after the number of faces. The entire return value is a string.

Pay particular attention to how you access the `num_faces` attribute. It's essential to tell Python where to find the attribute, so you precede it with the name of the class, `mRelative.num_faces`. If you fail to do this, Python gives you an error message telling you the attribute is nowhere to be found.

You can test this addition using the following code:

```python
print(mRelative.numFaces("The database contains ", " faces."))
```

The example simply creates a string that tells how many faces there are. Running the code produces this output:

![tk](media/tk.png)

_tk_

## Defining instance methods

Instance methods are associated with a particular object, rather than with the class. They are defined by adding functions to the class that receive `self` as the first parameter. Internally, instance methods are free to access the object's attributes and even other methods.

1. Return to your notebook and enter a new definition for the `mPerson` class:

	```python
	import datetime
	
	class mPerson:
	    def __init__(self, photo, name, date_of_birth):
	        self.photo = photo
	        self.name = name
	        self.birth_date = date_of_birth
	        
	    def get_age(self):
	        return int((datetime.datetime.now() - self.birth_date).days / 365.25)
	    
	    def show_face(self):
	        plt.axis('off')
	        plt.imshow(self.photo, cmap=plt.cm.gray)
	```

	`mPerson` now contains two instance methods: one named `get_age()` that returns the person's age in years, and another named `show_face` that displays the person's face.

	> The age computation isn't exact because it provides only rudimentary handling of leap years. The solution to that is a topic for another day.

1. Now it's time to test these instance methods. Run the following statements in a new cell:

	```python
	aPerson = mPerson(faces.images[0], "Stan", datetime.datetime(1990, 9, 16))
	print(str(aPerson.get_age()))
	aPerson.show_face()
	```

1. Confirm that you see the following output:

	![Output from instance methods](media/instance-method-output.png)
	
	_Output from instance methods_

Neither of the instance methods you added take arguments (other than `self`, which is required of an instance method), but instance methods *can* take arguments just like other functions in Python.

## Overriding the __str__() method

Python supplies a default `__str__()` method, which works well with the primitive built-in object types. But for custom types, it rarely provides the results you want. The default method tells you about the object: the object's name and where the object is located in memory. It would be a lot more useful if it could tell you something specific about the object's content. 

You can replace the built-in `___str__()` method (or any other method, for that matter) by *overriding* it. You don't have to do anything  special to override a method in Python. You just provide a new version of the method in the class.

1. Return to the `mPerson` class in your notebook and add the following method to it:

	```python
	def __str__(self):
	    return self.name + ', age ' + str(self.get_age())
	```

	This method returns a string denoting the person's name and age. The information contained in the string is obtained by reading the object's `name` attribute and calling the object's `get_age()` method.

1. To test the new `__str__()` method, enter the following code and run it:

	```python
	print(str(aPerson))
	print(aPerson.__str__())
	print(aPerson)
	```

How do the outputs from the three `print()` statements differ? Or do they differ at all? What does this tell you about how Python's `str()` function is implemented inside the Python run-time?