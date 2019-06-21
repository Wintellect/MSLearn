# Sequences and dictionaries

An understanding of data handling in Python begins with an understanding of *sequences* and *mapping types*. Sequences hold ordered sets of data. Think of an array holding an ordered set of integers or a string holding an ordered set of characters. Each item in the array or string occupies a specific position, and each has a specific index (0-based, of course). Mapping types,by contrast, store unordered sets of data. The most common example of a mapping type is the dictionary, which holds key-value pairs. You can retrieve a value from a dictionary by specifying a key, but you can't retrieve a value by index.

## Sequences
 
Python supports a variety of data types, including strings, integers, floating-point numbers, and Booleans. It also supports sequences, which hold collections of data. The three most common sequences are:

- Lists, which are similar to arrays in other programming languages
- Tuples, which are immutable lists (meaning they can't be changed)
- Strings, which are sequences of characters

Sequences invariably play a role in data handling in Python because they support a rich and very concise syntax for slicing and dicing data. To understand sequences, let's start by learning about lists.

### Lists

A list is a collection of items of any data type — for example, integers, strings, or even other lists — and is analogous to arrays in other programming languages. Lists are mutable (they can be changed), which means items can be added and removed from them.

> The terms *mutable* and *immutable* are frequently used in programming. Mutable means the memory referenced by a variable can be changed. Immutable means the memory referenced by a variable cannot be changed. For example, strings are immutable. If you modify a string in code, a new string is created in memory to hold the modified string. Lists are mutable, meaning items can freely be added and removed.

To create a list, you can wrap a sequence of values in square brackets and separate each item in the list with commas. The following example creates a list of integers:

```python
nums = [1,2,3,4,5]
```

To access an item in the list, specify its zero-based index in square brackets:

```python
print(nums[2]) # outputs: 3
```

One of the most useful features that lists support is *slicing*, which allows you to easily extract a subset of the list. Slicing is performed by specifying a starting index and ending index in square brackets. The following code extracts three characters from a list and prints them to the screen. Note that the last item included in the slice is the item whose index is the ending index minus 1:

```python
nums = [1,2,3,4,5]
print(x[1:4]) # outputs: [2,3,4]
```

You can omit the starting index to specify that the slice should start with the first item in the list:

```python
nums = [1,2,3,4,5]
print(x[:4]) # outputs: [1,2,3,4]
```

And you can omit the ending index to specify that the slice should end with the final item in the list:

```python
nums = [1,2,3,4,5]
print(x[2:]) # outputs: [3,4,5]
```

Python is famous for its slicing capabilities. The ability to slice data is heavily used in Python applications, especially when performing numerically intensive tasks such as statistical analysis and machine learning.

Adding an item to the end of a list is simple:

```python
nums = [1,2,3,4,5]
nums.append(6)
print(nums) # outputs: [1,2,3,4,5,6]
```

Removing an item from the list is equally simple:

```python
nums = [1,2,3,4,5]
nums.remove(4)
print(nums) # outputs: [1,2,3,5]
```

To find the number of items in a list, use Python's built-in `len` function:

```python
nums = [1,2,3,4,5]
print(len(nums)) # outputs: 5
```

### Strings

A string is a sequence of zero or more characters. Unlike most other programming languages, Python lacks a character data type. A character in Python simply a single item in a string.

Because strings are sequences, they support the same slicing syntax as lists. The following examples demonstrate how slicing is performed and substrings are extracted from other strings:

```python
message = 'This is fun!'
print(message[0]) # outputs T
print(message[0:4]) # outputs This
print(message[:4]) # outputs This
print(message[8:]) # outputs fun!
print(message[8:-1]) # outputs fun
print(message[-4:-1]) # outputs fun
```

Specifying a negative number for a starting or ending index represents an offset from the end of the string. In Python, [:-1] is a clever way to remove the final character from a string. Not surprisingly, [:-2] removes the final two characters, [:-3] removes the final three, and so on.

Strings come with built-in functions for string manipulation. A common requirement is to split a string containing a collection of strings separated by commas, spaces, or other characters into a list of strings. Here's an example that splits a string containing a list of strings separated by commas into a list of strings using the `split()` function that can be called on any string:

```python
colors_data = 'red,green,blue'
colors = colors_data.split(',')
print(colors) # outputs: ['red','blue','green']
```

In Python, you can concatenate strings using the `+` operator:

```python
message = 'Hello' + ' ' + 'World!'
print(message) # outputs: Hello World!
```

Because lists are sequences, they can be concatenated the same way:

```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums = nums1 + nums2
print(nums) # outputs: [1, 2, 3, 4, 5, 6]
```


You can see why sequences play an important role in data handling: they make it easy to manipulate collections of data. The fact that Python supports this is one reason why it is so popular among people who deal with data on a daily basis.

## Dictionaries

Whereas sequences store ordered sets of data, mapping types stored unordered sets. The most common example of a mapping type in Python is the dictionary.



TODO: Add content.



Now you know the basics of lists, strings, dictionaries in Python. In the next lesson, you'll learn how to use comprehensions and lambda functions to make working with these types easier.