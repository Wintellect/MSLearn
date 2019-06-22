# Sequences and dictionaries

An understanding of data handling in Python begins with an understanding of *sequences* and *mapping types*. Sequences hold ordered sets of data. Think of an array holding an ordered set of integers or a string holding an ordered set of characters. Each item in the array or string occupies a specific position, and each has a specific zero-based index. Mapping types store unordered sets of data. The most common example of a mapping type is the dictionary, which holds key-value pairs. You retrieve a value from a dictionary by specifying a key instead of an index.

## Sequences
 
Python supports a variety of data types, including strings, integers, floating-point numbers, and Booleans. It also supports sequences, which hold collections of data. The most common sequences are:

- Lists, which are similar to arrays in other programming languages
- Strings, which are sequences of characters

Sequences play a role in data handling in Python because they support a rich and concise syntax for slicing and dicing data. To understand sequences, let's start with lists.

### Lists

A list is a collection of items of any data type (integers, strings, or even other lists) and is analogous to arrays in other programming languages. Lists are mutable (they can be changed), which means items can be added or removed from a list.

> The terms *mutable* and *immutable* are frequently used in programming. Mutable means the memory referenced by a variable can be changed. Immutable means the memory referenced by a variable cannot be changed. Strings are immutable. If you modify a string in code, a new string is created in memory to hold the modified string. Lists are mutable, meaning items can freely be added and removed.

To create a list, you wrap a sequence of values in square brackets and separate each item in the list with commas. 

The following example creates a list of integers:

```python
nums = [1,2,3,4,5]
```

To iterate through all the values in the list use a loop:
```python
nums = [1,2,3,4,5]
for value in nums:
    print(value) # outputs : 
                 # 1
                 # 2
                 # 3
                 # 4
                 # 5 
```

To access an item in the list, specify its zero-based index in square brackets:

```python
nums = [1,2,3,4,5]
print(nums[2]) # outputs: 3
```

One of the features lists support is *slicing*. Slicing allows you to extract a subset of the list. Slicing is performed by specifying a starting index and ending index in square brackets.  

The following code extracts three characters from a list starting at index position 1 and ending at index position 4: 

```python
nums = [1,2,3,4,5]
print(nums[1:4]) # outputs: [2,3,4]
```

You can omit the starting index to specify the slice should start with the first item in the list:

```python
nums = [1,2,3,4,5]
print(nums[:4]) # outputs: [1,2,3,4]
```

You can omit the ending index to specify  the slice should end with the final item in the list:

```python
nums = [1,2,3,4,5]
print(nums[2:]) # outputs: [3,4,5]
```

The ability to slice data is heavily used in Python applications, especially when performing numerically intensive tasks such as statistical analysis and machine learning.

Add an item to the end of a list with the `append` function:

```python
nums = [1,2,3,4,5]
nums.append(6)
print(nums) # outputs: [1,2,3,4,5,6]
```

Remove an item from the list with the `remove` function:

```python
nums = [1,2,3,4,5]
nums.remove(4)
print(nums) # outputs: [1,2,3,5]
```

To find the number of items in a list, use the `len` function:

```python
nums = [1,2,3,4,5]
print(len(nums)) # outputs: 5
```

### Strings

A string is a sequence of zero or more characters. Unlike most other programming languages, Python lacks a character data type. A character in Python simply a single item in a string.

Because strings are sequences, they support the same slicing syntax as lists. The following examples demonstrate how slicing  extracts substrings from strings:

```python
message = 'This is fun!'
print(message[0]) # outputs T
print(message[0:4]) # outputs This
print(message[:4]) # outputs This
print(message[8:]) # outputs fun!
print(message[8:-1]) # outputs fun
print(message[-4:-1]) # outputs fun
```

Specifying a negative number for a starting or ending index represents an offset from the end of the string. [:-1] extracts the entire string except the final character, [:-2] extracts the entire string except the final two characters, [:-3] removes the final three characters, and so on.

```python
message = 'This is fun!'
print(message[:-2]) # outputs : This is fu
```

Strings come with built-in functions for string manipulation. A common requirement is to split a string containing a collection of strings separated by commas, spaces, or other characters into a list of strings. The following example splits a string containing a series of strings separated by commas into a list of strings using the `split` function.

```python
colors_data = 'red,green,blue'
colors = colors_data.split(',')
print(colors) # outputs: ['red','blue','green']
```

You can concatenate strings using the `+` operator:

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


Sequences make it easy to manipulate collections of data. The Python support for sequences is one reason why it is so popular among people who deal with data on a daily basis.

## Dictionaries

Whereas sequences store ordered sets of data, mapping types stored unordered sets. The most common example of a mapping type in Python is the dictionary.

Each row in a dictionary contains a *key* and a *value*. 

Values are passed inside curly braces. 

The following code creates an empty dictionary called airports:

```python
airports = {}
print(airports) # outputs: {}
```

Keys and values are provided to the dictionary using the syntax *key*:*value*.

The following code creates a dictionary containing the airport codes and cities for three airports:
```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles','ORD':'Chicago'}
print(airports) # outputs : {'SEA': 'Seattle', 'LAX': 'Los Angeles', 'ORD': 'Chicago'}
```

Instead of specifying an index position, you access a value in the dictionary by specifying the key:
```python
lax_city = airports['LAX']
print(lax_city) # outputs: Los Angeles
```
If you want to add another key:value to the dictionary, you just assign a value to a new key.

The following code adds the Houston airport to the airports dictionary: 
```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles','ORD':'Chicago'}
airports['HOU']='Houston'
print(airports) # outputs : {'SEA': 'Seattle', 'LAX': 'Los Angeles', 'ORD': 'Chicago', 'HOU': 'Houston'}
```
To remove a row from a dictionary use the `del` command:
```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles','ORD':'Chicago'}
del airports['LAX']
print(airports) # outputs : {'SEA': 'Seattle', 'ORD': 'Chicago'}
```
Just like you can with lists and strings, you can use the `len` function to return the length of the dictionary:
```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles','ORD':'Chicago'}
nbr_entries = len(airports)
print(nbr_entries) # outputs : 3
```

Now you know the basics of lists, strings,and dictionaries in Python. In the next lesson, you'll learn how to use comprehensions, map, and lambda functions to make it easier working with these types.