# Perform actions with methods

Methods tell the software how an action is performed. Just as a recipe has a series of steps to put together the ingredients and a blueprint's instructions tell a worker how to connect the various pieces of wood, Python objects need methods to describe how they are to interact with the attributes that describe it. Without steps, instructions, or methods an object is inert—it just sits there looking pretty, but without any purpose whatsoever.

Python objects always have methods. However, the methods may not be useful in context of the object. For example, the `__str__()` method that you discover later in this unit displays the string representation of the object. Python comes with a default `__str__()` that works fine for something simple like an int, but does not work at all acceptably for a complex object like `aRelative` (the object created from the `mRelative` class). When you use the `__str__()` method on `aRelative`, what you get as output is something like `<__main__.mRelative object at 0x7ff9e91ab978>`. It's sort of the same thing that happens when someone leaves out a step in a recipe or omits an instruction out of a blueprint: the result often doesn't make much sense.

This unit tells you about Python methods. In it, you add to the `mRelative` class so that you can now perform actions with it. The actions provided in this unit are basic, but they give you a good idea of what you can do with methods. Of course, the only true limit on methods is your own imagination.

## Static methods vs. instance methods

Real-world objects have two kinds of methods: static and instance. Static methods apply to all objects of a certain type. For example, when you bake cookies, you normally set the oven temperature to 350 degrees Farenheit. Likewise, when building a house, you prepare the ground before you pour a foundation.

When working with the `mRelative` class, you might want a nicely formatted output showing the number of unique faces in the dataset. You could access the `num_faces` attribute directly, which would mean creating a sentence every time, but this method would make creating formatted output simpler, so it's useful to have it. There isn't a good reason to perform more work than you need to.

Instance methods apply to a particular object. For example, in baking cookies, you might need to add the chocolate chips to the batter – but that only makes sense when the recipe contains chocolate chips. The step of adding the chips works with the attribute of having chocolate chips in the first place. Likewise, a blueprint's instructions to dig a basement, which only makes sense when the house needs a basement. Otherwise, the first story of the house appears in a hole, making it impossible to access because the front door is now underground.

Likewise, instance methods in Python normally relate to the attributes in some way. They're unique to that particular object. The `mRelative` class can benefit from a few special instance methods:

- Displaying the current face number
- Displaying the missing person's information
- Overriding the default `__str__()` method to display something better

The third instance method requires a little more explanation, so you see it covered in its own section in this unit.

## Defining static methods

Static methods work with your class, not with the object instantiated from the class. You can use a static method to create a nicely printed version of the number of faces in the Olivetti Faces dataset. You could do the same thing using special code every time, but the purpose of creating a class of this sort is so that you don't have to keep typing the same code repeatedly.

To create a static method, you add it to your class definition as shown in bold here:

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

The other code in this class defines the attributes. The code in bold is your first method. Notice the first line, @staticmethod. This line is called a decoration, but what it really does is tell Python that this is a static method, not an instance method. There are other ways to determine the difference too, as you see later in the unit. For now, know that this decoration says that this is a static method that belongs to the class as a whole.

Below the decoration, you see the method, which accepts two arguments, before and after. The before argument contains content that appears before the number of faces, while the after argument contains content that appears after the number of faces. The entire return value is a string.

Pay particular attention to how you access the num_faces attribute. It's essential to tell Python where to find the attribute, so you precede it with the name of the class, mRelative.num_faces. If you fail to do this, Python gives you an error message telling you the attribute is nowhere to be found.

You can test this addition using the following code:

```python
print(mRelative.numFaces("The database contains ", " faces."))
```

The example simply creates a string that tells how many faces there are. Running the code produces this output:

![tk](media/tk.png)

_tk_

## Defining instance methods

Instance methods are associated with a particular object, rather than with the class. You use instance methods to do something with the object, such as baking your favorite cookie or building a house. The verbs baking and building are equivalent to instance methods. You don't bake just any old cookie, you bake a specific cookie. Likewise, even if you're building an entire block of the same house, for the moment, you're building a specific house.

Consequently, as when working with attributes, you refer to self when working with instance methods. Doing so tells Python that this method refers to this particular object and to no other object.

To see how this works, add the following code to your class:

```python
def face_number(self):
    return "Currently processing face: " + str(self.pic_num)
    
def person_info(self):
    return 'Getting information for {0} in cabinet {1}.'.format(
        self.name, self.cab_file)
```

As stated earlier, you create two instance methods that work with the object attributes. The `face_number()` method outputs the number of the face that you're currently processing in the dataset. Notice that this method uses concatenation (the addition of two string elements – that is, "abc" concatenated with "def" is "abcdef") to provide output. Before you add it to the text, you must convert the int value, self.pic_num, to a string; otherwise Python displays an error message.

The `person_info()` method uses a different approach. In this case, you create a string containing placeholders within curly braces. This is called a format string because it uses the `format()` method to create a string from attributes that may be of different types. A format string can perform amazing transformations, but for now, just note that this format string contains two placeholders, one for each of the attributes.

Now it's time to test your new class. Of course, you need to run the class code again so Python recognizes the changes. Then recreate the aRelative object using code like this:

```python
aRelative = mRelative(0, "Stan", 123)
At this point, you can test the aRelative object using this code:

print(aRelative.face_number())
print(aRelative.person_info())
```

The first call displays the face number, while the second displays the person's information. Here's what you can expect as output:

![tk](media/tk.png)

_tk_

## Getting object content with __str__()

Python supplies a `__str__()` method, which works fine in a limited number of cases. Generally you may find it rarely  provides the results you want. The default method tells you about the object: the object's name and where the object is located in memory. It would be a lot more useful if the object could tell you something specific, such as the object content. 

When you create a new method to replace an existing method, what you're doing is called overriding the method. Yes, a method already exists, but now you need a new one. It's like baking cookies. Most cookies bake just fine at 350. But perhaps you've created the ultimate in really thin cookies and they burn at 350, so now you need to override the usual method and bake your cookies at 325 instead. Likewise, when building a house, you might find that the house was supposed to have a basement, but an underground stream is in the way. So, this particular house needs to override the usual method and not have a basement.

You don't have to do anything particularly special to override a method in Python. You just provide a new version of the method in the class. Here is the `__str__()` method for the `mRelative` class:

```python
def __str__(self):
        return f'{self.pic_num}, {self.name}, {self.cab_file}'
```

All that this method does is print out the three attributes supplied when you instantiate the `aRelative` object. Notice that it uses a different form of the format string so that you don't have to convert any of the attributes to different types. (Placing the "f" outside the string and then including the attribute names within curly brackets works well when you don't want to do a lot of formatting.) The output of the `__str__()` method must always be a string, so you couldn't output an int or something like a tuple.

To test the `__str__()` method, you use the following code:

```python
print(str(aRelative))
print(aRelative.__str__())
print(aRelative)
That's right, the __str__() method works the same whether you call the str() method, call __str__(), directly or simply print the object! Here's the output you can expect to see:
```

![tk](media/tk.png)

_tk_






