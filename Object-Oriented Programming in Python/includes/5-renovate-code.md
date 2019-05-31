# Renovating your code

Nothing in the real world stays static for long. In fact, the real world is in constant motion, much to the consternation of us who live in it.

So, it doesn’t surprise you one day to find that your chocolate chip cookie recipe, which normally produces an ample 8 dozen cookies, must now produce 9 dozen cookies to feed the ever growing group of piranha-like denizens of the cookie jungle. You could use a smaller cookie scoop, but then everyone would complain. Instead, you add walnuts to the batter, extending it just enough to produce the additional cookies and making the walnut lovers of the world extremely happy.

Likewise, the wonderfully spacious two-bedroom house built for a young couple feels cramped with the addition of two children, especially when it comes to the single bathroom. You could solve the bathroom problem, at least, by changing that overstuffed closet full of random items into a half bath.

The same premise applies to the applications you write. Once your code faces the realities of the real world, you find that your `mRelative` and `mAcquaintance` classes are being used by people who have no clue as to how to display the faces. Besides, your boss is tired of seeing reports full of green Martian-like faces that apparently went through a wire grater.

This unit helps you renovate your classes so that they can face the real world fully restored to their original luster.

## Adding a drawPic() method

You know that all you need to draw the face of the person who is missing, whether an acquaintance or a relative, is to use `matplotlib.pyplot`. So, really, all you need to do is add that code to the `mRelative` class, as shown here in bold:

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
    
    def face_number(self):
        return "Currently processing face: " + str(self.pic_num)
    
    def person_info(self):
        return ’Getting information for {0} in cabinet {1}.’.format(
            self.name, self.cab_file)
    
    def __str__(self):
        return f’{self.pic_num}, {self.name}, {self.cab_file}’
    
    def drawPic(self):
        %matplotlib inline
        import matplotlib.pyplot as plt
        
        # Load the picture
        plt.imshow(self.pic_cont)

        plt.show
```

As always, you need to rerun the code for downloading the dataset, creating both mRelative and mAcquaintance classes, and instantiating the aRelative and anAcquaintance objects. Once that’s done, you can perform individual tests on them. Make sure you place each test in its own cell; otherwise the plot of one call overwrites the plot of the one previous to it.

```python
aRelative.drawPic()
anAcquaintance.drawPic()
```

Notice that you can call `drawPic()` with `anAcquaintance` without actually adding the method to the associated class. That’s because any change you make to a parent automatically flows to a child.

Take a moment to consider this important point. This flowing effect is one of the main causes of side effects in modified classes. Somewhere a child lurks that will have a problem with the change, so exercise caution in making the change in the first place and perform proper testing in the second.

When you run this code you see output like this:

![tk](media/tk.png)

_tk_

The `drawPic()` method affects both classes even though it appears in only one.

## Improving the output

Even though both classes can now display the picture of the missing person using `drawPic()`, the output still isn’t very friendly. You have access to a lot of graphic manipulation functionality in `matplotlib.pyplot`. The first task would be to get rid of that awful green tinge for the missing people using this code.

```python
# Change the color
plt.gray()
```

You can use any of a number of color palettes, one of which is grayscale, which is how the original photos actually appear. The other changes to the appearance of the image itself appear here:

```python
# Remove the axis ticks
plt.xticks([])
plt.yticks([])
```

Because no one actually knows who these people are without a label, you can also add a title that includes the person’s specifics, as shown here:

```python
# Add a title
plt.title(self.name.__str__())
```

At this point, your updated class should be ready to go. After running the code, you see this output:

![tk](media/tk.png)

_tk_

## Testing for side effects

The side effects of the changes made so far are minor, unless you try using the `__str__()` method with `anAcquaintance`. You don’t get what you expected at all.

Although the output for `aRelative` is fine, `anAcquaintance` is a dictionary, not a name. In order to correct this issue, you need to perform two tasks:

- Create a `personName` attribute for each of the classes that accounts for its method of storing the name attribute
- Change the `plt.title()` method call to `plt.title(self.personName.__str__())`

Modifying `mRelative` as needed is relatively straightforward. You simply add a new attribute to it, as shown here:

```python
def __init__(self, pic_num, name, cab_file):
    self.pic_num = pic_num
    self.pic_cont = faces.images[pic_num * 10]
    self.name = name
    self.personName = name
    self.cab_file = cab_file
```

Modifying `mAcquaintance` requires a little more thought because now you’re constructing a string from a dictionary. Here is the code you need in bold:

```python
def __init__(self, pic_num, name: fullName, relation, info):
    
    # Start by creating the parent object
    mRelative.__init__(self, pic_num, "", -1)
    
    # Add the required attribute.
    self.relation = relation
    self.info = info
    
    # Modify the name attribute.
    self.name = fullName({"first": name[’first’], "last": name[’last’]})
    
    # Remove the cab_file attribute.
    delattr(self, ’cab_file’)
    
    # Add a method for retriving the name.
    self.personName = name[’first’] + " " + name[’last’]
```

Knowing how to manipulate the class data as needed is an essential part of making renovations. Now the classes will produce the desired output as shown here:

![tk](media/tk.png)

_tk_

As in the real world, the classes you design and the objects you instantiate from them will continue to grow and change. This process of growth and change is called the lifecycle of the software. This unit shows that creating a new class is just the beginning, not the end of the development process.