# Sequences and mapping types

Data handling in Python begins with an understanding of *sequences* and *mapping types*. Sequences hold ordered sets of data. Think of an array holding an ordered set of integers or a string holding an ordered set of characters. Each item in the array or string occupies a specific position, and each has a specific zero-based index. Mapping types store unordered sets of data. The most common example of a mapping type is the dictionary, which holds key-value pairs. You retrieve a value from a dictionary by specifying a key instead of an index.

## Sequences
 
Python supports a variety of data types, including strings, integers, floating-point numbers, and Booleans. It also supports sequences, which hold collections of data. The most common sequences are:

- Lists, which are similar to arrays in other programming languages
- Tuples, which are are like lists, but are immutable (more on this in a moment)
- Strings, which are sequences of characters

Sequences play a role in data handling in Python because they support a rich and concise syntax for slicing and dicing data. To understand sequences, let's start with lists.

### Lists

A list is a collection of items of any data type (integers, strings, or even other lists) and is analogous to arrays in other programming languages. Lists are mutable, which means items can be added to and removed from them.

> The terms *mutable* and *immutable* are frequently used in programming. Mutable means the memory referenced by a variable can be changed. Immutable means the memory referenced by a variable cannot be changed. Strings are immutable. If you modify a string in code, a new string is created in memory to hold the modified string. Lists are mutable, meaning items can freely be added and removed.

To create a list, you wrap a sequence of values in square brackets and separate each item in the list with commas. The following example creates a list of integers:

```python
nums = [1, 2, 3, 4, 5]
```

You can iterate through all the values in the list using a loop:

```python
nums = [1, 2, 3, 4, 5]
for value in nums:
    print(value) 
```

To access an item in the list, use its zero-based index:

```python
nums = [1, 2, 3, 4, 5]
print(nums[2]) # outputs: 3
```

One of the features lists support is *slicing*. Slicing allows you to extract a subset of the list. Slicing is performed by specifying a starting index and ending index in square brackets. The following code extracts three characters from a list starting at index 1 and ending at index 4: 

```python
nums = [1, 2, 3, 4, 5]
print(nums[1:4]) # outputs: [2, 3, 4]
```

You can omit the starting index to specify that the slice should start with the first item in the list:

```python
nums = [1, 2, 3, 4, 5]
print(nums[:4]) # outputs: [1, 2, 3, 4]
```

And you can omit the ending index to specify that the slice should end with the final item in the list:

```python
nums = [1, 2, 3, 4, 5]
print(nums[2:]) # outputs: [3, 4, 5]
```

What if you want to modify a list? You can insert an item into a list with the `insert()` function, or add an item to the end of a list with the `append()` function:

```python
nums = [1, 2, 3, 4, 5]
nums.append(6)
print(nums) # outputs: [1, 2, 3, 4, 5, 6]
```

You can remove an item from a list with the `remove()` function:

```python
nums = [1, 2, 3, 4, 5]
nums.remove(4)
print(nums) # outputs: [1, 2, 3, 5]
```

Finally, you can get the number of items in a list with the `len()` function:

```python
nums = [1, 2, 3, 4, 5]
print(len(nums)) # outputs: 5
```

`len()` is a Python function, so rather than call it on a list, you pass it a list.

### Strings

A string is a sequence of zero or more characters. Unlike most other programming languages, Python lacks a character data type. A character in Python is simply a single item in a string.

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

Specifying a negative number for a starting or ending index represents an offset from the end of the string. [:-1] extracts the entire string except the final character, [:-2] extracts the entire string except the final two characters, [:-3] removes the final three characters, and so on:

```python
message = 'This is fun!'
print(message[:-2]) # outputs: This is fu
```

Strings come with built-in functions for string manipulation. A common requirement is to split a string containing a collection of strings separated by commas, spaces, or other characters into a list of strings. The following example splits a string containing a series of strings separated by commas into a list of strings using the `split()` function:

```python
colors_data = 'red,green,blue'
colors = colors_data.split(',')
print(colors) # outputs: ['red', 'blue', 'green']
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

Sequences make it easy to manipulate collections of data. Python's support for sequences is one reason why it is so popular among people who deal with data on a daily basis.

## Mapping types

Whereas sequences store ordered sets of data, mapping types store unordered sets. Mapping types hold collections of key-value pairs. They're called *mapping types* because each item maps a key (for example, "ORD," which is the airport code for Chicago's O'Hare International Airport) to a value (for example, "Chicago"). The only standard mapping type included in Python is the *dictionary*.

### Dictionaries

Each item in a dictionary contains a *key* and a *value*. The following statement creates an empty dictionary named `airports`:

```python
airports = {}
```

You can include key-value pairs inside the curly braces to initialize a dictionary with items. This example creates a dictionary containing airport codes and cities for three airports:

```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles', 'ORD':'Chicago'}
print(airports) # outputs: {'SEA': 'Seattle', 'LAX': 'Los Angeles', 'ORD': 'Chicago'}
```

You can retrieve a value from a dictionary by specifying the value's key:

```python
lax_city = airports['LAX']
print(lax_city) # outputs: Los Angeles
```

You add new values to a dictionary by specifying their values and their keys. The following example adds the Houston airport to the `airports` dictionary: 

```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles', 'ORD':'Chicago'}
airports['HOU']='Houston'
print(airports) # outputs: {'SEA': 'Seattle', 'LAX': 'Los Angeles', 'ORD': 'Chicago', 'HOU': 'Houston'}
```

If an item keyed by "HOU" doesn't exist, it is added to the dictionary. If the item does exist, its value is replaced with "Houston."

To remove an item from a dictionary, use `del`:

```python
airports = {'SEA':'Seattle', 'LAX':'Los Angeles', 'ORD':'Chicago'}
del airports['LAX']
print(airports) # outputs: {'SEA': 'Seattle', 'ORD': 'Chicago'}
```

You can enumerate the items in a dictionary using a `for` loop:

```python
for key, value in airports.items():
    print(key + ' = ' + value)
```

Because items in a dictionary are unordered, the enumeration won't necessarily retrieve items in the order in which they were added.
