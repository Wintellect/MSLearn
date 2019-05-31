# Inherit a class

Inheritance is one of those terms that can mystify people because we use it term in so many ways. For example, someone can inherit resources from another person: or someone reads the "last will and testament" and suddenly you're rich beyond your wildest dreams.  Many people try to describe OOP in the context of genetic inheritance, but that analogy falls a bit short for a lot of reasons. For example, your grandmother might have green eyes, but your mother doesn't, yet you do. Genetic inheritance skips generations -- and that's not how computers work.

So to better understand the concept of inheritance, we use examples like recipes or architectural drawings. When you think of inheritance in OOP, think of the word "except." I like that chocolate chip cookie recipe, except there aren't enough chocolate chips (a change to the original recipe) and the recipe doesn't include any nuts (an addition to the original recipe). I like that house design, except that the kitchen and dining room are too small, and the living room is way too large (both changes). The hall closet also isn't needed, so we can use the space for some other need (a deletion).

In OOP terms, that means all of the original elements are in the new class as were in the existing class, except those that you didn't want for whatever reason.

When thinking about except, consider these issues:

- Something needs to be added
- Something needs to be removed
- Something needs to be changed

This unit looks at a new class, `mAcquaintance`. It works just like `mRelative`, except that you must now consider your relationship with the missing person (an addition); you need more than just a first name (a change); and you no longer have a cabinet (a deletion); but you do have access to an information resource (an addition). The purpose of `mAcquaintance` is to handle missing person cases where there isn't a direct family connection; it could be a person from work or a person who does volunteer activity with a particular group. Even though the connection is more tenuous, the concern is just as real. However, the information is necessarily less personal. It's different, so you must handle it differently.

## Differentiating between parent and child

You may have favorite cookbooks containing the best recipes you've ever found, except they're not quite what you want. Most cooks mark up their cookbooks with little changes that improve the recipes. The original recipe is the parent and acts as a starting point for the child. Even though the original recipe produces a final product, you want a slightly different final product, so you mark it up. The marks you put on the recipe transform it from the original that you almost like, to the unique version that you really like.

Buildings work a bit differently, but the concept is the same. A blueprint may contain a template for a basic building. This parent is never actually used for a building because it lacks features, such as kitchen details, that a completed building needs. However, you could still build this building and modify it later.

If you are a real estate developer, to make a row of houses that all look the same from the outside more appealing, you offer options. The options add, remove, or change elements of the template. These are the children. The children still have the same dimensions as the parent and the essential elements are in the same place, but the children are inherently different from the parent because they provide a buildable design.

Inheritance in Python is a combination of these two ideas. You can start out with either a fully functional class that is useful immediately or a template class that you could still instantiate, but isn't useful immediately. In both cases, you can use the except principle to say that you like the way the class is constructed, except for specific features.

If you have experience with other languages such as C# or Java, you may wonder if Python supports static classes. Static classes are [classes you can't instantiate](https://www.c-sharpcorner.com/UploadFile/74ce7b/static-class-in-C-Sharp/); you can only inherit them. The short answer is no: You can instantiate an object from any class in Python; there is no such thing as a static class.

Generally, you don't need to create static classes in Python because of the manner in which the language works. However, you can create modules containing [only static methods](https://stackoverflow.com/questions/30556857/creating-a-static-class-with-no-instances) that could simulate a static class. This unit doesn't discuss this approach because creating pseudo-static classes really isn't the Pythonic way to do things.

## Extending a class

The process of adding to a class extends the original definition. You subclass, create a child version of the parent class, to obtain useful new features. In the case of `mAcquaintance`, you need to add attributes to represent a relationship with the other person and a attribute to define the information resource. With this in mind, type the following code into your **Missing_Relatives_Example.ipynb** file. You can use the same file for both parent and child classes (unlike some languages where you must use separate files).

```python
class mAcquaintance(mRelative):
    
    def __init__(self, pic_num, name, relation, info):
        
        # Start by creating the parent object
        mRelative.__init__(self, pic_num, "", -1)
        
        # Add the required attributes.
        self.relation = relation
        self.info = info
```

To create a subclass, you begin by adding the name of the parent to the class definition in parenthesis. The line, `class mAcquaintance(mRelative):`, says that `mAcquaintance` is a subclass, a child, of `mRelative`.

In order to extend `mRelative`, you must create an `__init__(`) method in `mAcquaintance` that overrides the __info__() method in `mRelative`. You learn more about overriding things later in this unit, but just put the concept of overriding aside for the moment.

The next line looks odd indeed, but believe it or not, you actually create an instance of `mRelative` and assign the values you want to it. In this case, you pass along the `pic_num` because you eventually need it for `mAcquaintance`. However, notice that the name and `cab_file` arguments contain empty values because you don't need them.

The next two lines add new attributes, just as you did for `mRelative`. However, these attributes are exclusive to `mAcquaintance`.

To try out the new class, you must first run all of the code for `mRelative`, including importing the database (you don't have to perform the tests). After you run the `mRelative` code, you can run the `mAcquaintance` code to create the class.

Testing the class requires that you instantiate an object using this code:

```python
anAcquaintance = mAcquaintance(1, "Albert", "Friend", "Mother")

print(anAcquaintance.__dict__)
print(anAcquaintance.__dict__.keys())
```

It's important to note that when you create the `mAcquaintance` object, `anAcquaintance`, you use the syntax for creating an `mAcquaintance`, not an `mRelative` object. This is why you see four arguments instead of three: `pic_num`, name, relation, and info.

Just creating an object doesn't  tell you if you were successful, though; you need to see the attributes. This is where the __dict__ attribute comes into play. You didn't create this attribute; you get it from Python. The __dict__ attribute is a dictionary containing key and value pairs. Of course, sometimes you don't want to know the content of the keys, you just want to see the keys, so you can call __dict__.keys() instead.

Here is the output of this code.

![tk](media/tk.png)

_tk_

What you see is a key, such as `pic_num`, followed by a colon, followed by its value. The entries are separated with commas.The rather lengthy array is the value of the `pic_cont` argument. Otherwise, the other arguments should look pretty straightforward. Notice that name (near the bottom) contains an empty string and `cab_file` really does contain a value of -1.

The last line contains just the names of the attributes. All of the entries you expect are there, but they came from two different places: the parent and the child.

## Modifying an attribute

Overriding anything in a class is always problematic. A few purists would say that overriding anything other than staid standbys like `__init__()` and `__str__()` means that you really didn't want to use the parent class in the first place, but this isn't the approach that most people use. When creating `mAcquaintance` you naturally need to know more information than before, so overriding the name attribute, while considered a horrible thing to do by some, really isn't unreasonable. You're using name in the same manner as before. It simply has a different shape.

Of course, you want to reduce any potential for error. Consequently, you want to make sure that anyone using your class provides the right sort of data. You can do this with any of the `__init__()` arguments, but this example looks at one case specifically because it's unique, name. You start by creating a special data type that enforces what you want to see as input using this code:

```python
# Define a new type for this class.
from typing import NewType
fullName = NewType('fullName', {'first': str, 'last': str})
```

The first line simply imports `NewType()` so you can use it to create a new type. The `NewType()` method requires two arguments: the name of the new type (`fullName` in this case) and the form that this new type should take. In this case, the new type is a dictionary with two keys: first and last. Both of these values must be strings.

Now you have to enforce your will upon the user of your class. Here's an updated version of the `mAcquaintance` with the changes in bold:

```python
class mAcquaintance(mRelative):
    
    def __init__(self, pic_num, name: fullName, relation, info):
        
        # Start by creating the parent object
        mRelative.__init__(self, pic_num, "", -1)
        
        # Add the required attributes.
        self.relation = relation
        self.info = info
        
        # Modify the name attribute.
        self.name = fullName({"first": name['first'], "last": name['last']})
```

The first change is that name must now be of the `fullName` type. You can't simply pass a string to it without raising an error. The type appears after the argument name with a colon. You can use this approach for any of the arguments. For example, if you want to ensure that relation is a string, you can use relation: `str` to enforce that requirement.

Now that you have your new type, you need a new attribute. This represents a change from the `mRelative` class. Notice how you create the dictionary of type `fullName` using the input arguments. You could simply make one equal to the other, as is done for the other attributes; this approach is clearer and also more certain to produce error free results. You create the dictionary, as before, and access each of the expected values using the appropriate key.

So, let's see how this works. The following code has the changes you need to make to the original test code in bold:

```python
personName = fullName({'first': 'Sam', 'last': 'White'})
anAcquaintance = mAcquaintance(1, personName, "Friend", "Mother")

print(anAcquaintance.__dict__)
print(anAcquaintance.__dict__.keys())
```

When you run this code, you see the output shown here:

![tk](media/tk.png)

_tk_

As you can see, name now appears as a dictionary with the appropriate values associated with the correct keys.

## Removing an attribute

The new `mAcquaintance` class is nearly complete. However, you have the `cab_file` attribute hanging around unused. Odd things can happen when you're not tidy—people might choose to assign a value to that attribute and you don't really know what that will do to the code unless you perform all sorts of testing on it – and even then you'll miss bugs.

It's sort of like forgetting to cross out the baking soda you no longer need in a recipe. Someone might not realize that you added baking powder to use in place of the baking soda, so the baking soda is no longer needed.

As with making modifications, some purists will go the raised eyebrow route when you perform this next task of removing the `cab_file` attribute, but really, you'll be glad that you kept your classes tidy in the long run. Python actually provides a method, `delattr()`, to perform this task. You can add this following code to your `mAcquaintance` class:

```python
# Remove the cab_file attribute
delattr(self, 'cab_file')
```
You don't have to make any changes to the test code in this case. All you need to do is run it to see the following output, which shows that the `cab_file` attribute is now gone.

![tk](media/tk.png)

_tk_