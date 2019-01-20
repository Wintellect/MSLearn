# Use variables, types, and operators

Variables are one of the fundamental building blocks of programs written in Python. Variables hold data in memory for your program. They have names, and they can be referenced by name. Variables also have *types* such as string and integer, and they can be used in expressions that use *operators* such as `+` and `-` to manipulate their values.

In this lesson, you will learn about variables, data types, and operators in Python, and then put them to work in the notebook that you created in the previous lesson.

## Variables

In programming, variables are used to store the data that a program uses as it executes. They are used in expressions to calculate new values. Consider the following expression:

```python
x + 1
```

The symbol `x` is a variable. Its value can be changed and then evaluated within the expression to produce new values. For example, when `x` is 2, the value of the expression is 3. When `x` is 5, the value of the expression 6.

In Python, a variable is declared and then assigned a value using the assignment operator `=`. The variable being assigned to is on the left-hand side of the operator, and the expression being evaluated is on the right-hand side of the operator:

```python
x = 1 # assign x the value 1
y = x + 5 # assign y the value of x plus 5
z = y # assign z the value of y
```

These examples assign numbers to variables, but numbers are just one of several data types that Python supports. In the previous lesson, you used strings, which is another commonly used data type.

## Data types

Virtually every programming language supports built-in data types such as numbers and strings. Python provides many special-purpose data types as well as more standard types. Internally, Python represents all data as objects. Among other things, this means that you can call functions on the variables that you declare in order to manipulate them — for example, to convert all of the characters in a string variable to uppercase or lowercase.

### Working with numbers

Virtually all programs manipulate numbers. Computers treat integer numbers and decimal numbers differently. Consider the following code:

```python
x = 1 # integer
x = 1.0 # decimal (known as floating point)
```

Python creates integers from a built-in data typed called `int`, and decimals (floating-point numbers) as instances of `float`. The `type` function returns a variable's data type. The following code outputs types to the screen: 

```python
x = 1
print(type(x)) # outputs: <class 'int'>

x = 1.0
print(type(x)) # outputs: <class 'float'>
```

The addition of the ".0" to the end of "1" makes a big difference in how the programming language treats a value. The data type impacts how the value is stored in memory, how the processor (CPU) handles the data when evaluating expressions, how the data relates to other data, and what kinds operations can be performed with it.

Another common data type is the Boolean type, which holds the value `True` or `False`:

```python
x = True
print(type(x)) # outputs: <class 'bool'>
```

From Python's perspective, `bool` is a special type of integer. Technically, `True` has a value of 1 and `False` has a value of 0. Typically, Booleans are not used to perform mathematical operations; rather, they are used to make decisions and perform branching. Nevertheless, it is interesting to understand the relationship between types. Many types are nothing more than specialized versions of more general types. Integers are a subset of floating point numbers, and Booleans are a subset of integers.

### Working with strings

Strings are among the most commonly used data types. A string is simply a collection of zero or more characters. Python does not have an explicit character type like many other programming languages do. Any text data defined within single or double quotation marks is a string value:

```python
x = 'This is a string'
print(x) # outputs: This is a string
print(type(x)) # outputs: <class 'str'>
```

Strings can be added to other strings (an operation known as "concatenation") with the `+` operator:

```python
x = 'Hello' + ' ' + 'World!'
print(x) # outputs: Hello World!
```

When quoting strings, you may use single or double quotation marks. There is no difference between the resulting strings. You can embed a double quotation mark in a string by enclosing the string itself in single quotes, and you can embed a single quotation mark in a string by enclosing the string in double quotation marks:

```python
x = 'Hello World!'
print(x) # outputs: Hello World!

x = "Hello World!"
print(x) # outputs: Hello World!

x = "Tim said, 'Hello World!'"
print(x) # outputs: Tim said, 'Hello World!'

x = 'Tim said, "Hello World!"'
print(x) # outputs: Tim said, "Hello World!"
```

If the string contains the same quotation mark as the one used to quote the string, you may escape the embedded quotation mark with a backslash:

```python
x = 'Tim said, \'Hello World!\''
print(x) # outputs: Tim said, 'Hello World!'
```
String objects come with an extensive API (Application Programming Interface) for manipulating them. For example, the `upper` function can be called on any string. It changes a string's characters to all uppercase:

```python
message = 'Hello'
message.upper()
print(message) # outputs: HELLO
```

Similarly, the `lower` function changes the string to all lowercase:

```python
message = 'Hello'
message.lower()
print(message) # outputs: hello
```

The `replace` function replaces a specified sequence of characters in a string with another sequence of characters:

```python
message = 'This is fun!'
message.replace('is', 'was')
print(message) #outputs: This was fun!
```

`upper`, `lower`, and `replace` are but three examples of the more than 40 functions that you can call on a string in Python. Others include `find`, `islower`, `isupper`, `join`, and `split`.

### Working with sequences

Sequences hold collections of data: integers, strings, and so on. In Python, strings are sequences that hold collections of characters.

One of the most useful features of sequences is *slicing*, which allows you to easily extract a part of the sequence. As an example, the following code extracts three characters from a string and prints them to the screen:

```python
x = 'Python is a fun language with which to code.'
print(x[12:15]) # outputs: fun
```

Square brackets are used to perform the slicing, and the numbers indicate the starting and ending indexes of the slice. The first character has an index of zero. (This is known as zero-based indexing and is common to most, but not all, programming languages.) The second character has an index of 1, the third character has an index of 2, and so on. The sequence value — for a string, the character value — of the ending index is not included in the sliced data.

Python is famous for its slicing capabilities. The ability to slice data is heavily used in Python applications, especially when performing numerically intensive tasks such as statistical analysis and machine learning.

### Working with lists

Another commonly used sequence is the *list*. The list is a sequence of any type and is analogous to arrays in other programming languages. Lists are mutable (they can be changed), which means items can be added and removed from them.

> The terms *mutable* and *immutable* are frequently used in the programming. Mutable means the memory referenced by a variable can be changed. Immutable means the memory referenced by a variable cannot be changed. For example, strings are immutable. If you modify a string in code, a new string is created in memory to hold the modified string. Lists are mutable, meaning items can freely be added and removed.

To create a list, wrap a sequence of values in square brackets and separate each item in the list with commas:

```python
nums = [1,2,3,4,5]
print(nums) # outputs: [1, 2, 3, 4, 5]
print(type(nums)) # outputs: <class 'list'>
```

To access an item in the list, specify its zero-based index in square brackets:

```python
nums[2] # outputs: 3
```

The same slicing syntax used for strings can be used for lists (because both are sequences):

```python
nums[1:4] # outputs: [2, 3, 4]
```

Adding an item to the end of a list is simple:

```python
nums.append(6)
print(nums) # outputs: [1, 2, 3, 4, 5, 6]
```

Removing an item from the list is equally simple:

```python
nums.remove(4)
print(nums) # outputs: [1, 2, 3, 5, 6]
```

To find the length of a list (or any sequence including strings), use Python's built-in `len` function:

```python
print(nums) # outputs: [1, 2, 3, 5, 6]
print(len(nums)) # outputs: 5
```

`len` is one of dozens of built-in functions that Python supports. Here is a handy reference to some of the others: https://www.w3schools.com/python/python_ref_functions.asp.

### Combining strings and lists

Strings and lists are frequently used together. Lists can be used to create strings and strings can be used to create lists.

A common requirement is to split a string containing a collection of strings separated by commas, spaces, or other characters into a list of strings. Consider the following example, which splits a string containing a list of strings separated by commas into a list of strings using the `split` function:

```python
colors_data = 'red,green,blue'
colors = colors_data.split(',')
print(colors) # outputs: ['red','blue','green']
```

Another example involves combining a list of strings into a single string using the `join` function:

```python
colors = ['red','blue','green']
colors_data = ','.join(colors)
print(colors_data) # outputs: 'red,green,blue'
```

### Understanding the `None` value

Most programming languages have some kind of value that represents an absence of a value. It goes by many different names, depending on the language: null, nil, and undefined are just a few examples. In Python, the keyword `None` represents the absence of a value:

```python
some_var = None
```

The `None` value is more than just a value. It is also a type:

```python
type(None) # outputs: NoneType
```

Functions, which will be covered in a subsequent lesson, return a value of `None` if they do not have an explicit return value.

## Operators

Python expressions use operators to calculate new values. The behavior of operators is determined by the type of data to which the operator is applied. For example, using the `+` operator with numbers computes the sum of the numbers. Using it with strings concatenates the strings:

```python
print('a' + 'a') # outputs: aa
print(1 + 1) # outputs: 2
```

Some operators are applied to one value. These are known as *unary operators*. For example, the `not` operator outputs `False` for a `True` value and `True` for a `False` value:

```python
print(not True) # outputs: False
```

Some operators may be applied to two values. In this case, the two values must be of compatible types (but not necessarily the same type). For example, you can add an integer to a floating-point value to produce a floating-point value containing the sum of two numbers: 

```python
print(1 + 1.0) # Valid because both 1 and 1.0 are numbers, the output is 2.0
```

You can even add an integer to a Boolean value since Booleans are stored as numbers internally:

```python
print(1 +  True) # Valid because booleans are an integral type, the output is 2
```

You cannot, however, add an integer to a string. The following statement produces an error:

```python
print(1 + 'a')
```

There are many operators in Python. Here are some of the more common ones:

- \+ - adds two numbers or concatenates two strings
- \- - subtracts two numbers
- \* - multiplies two numbers
- / - divides two numbers
- not - returns the opposite of true or false
- and - returns the first value if it is false or falsy; otherwise, returns the second value
- or - returns the first value if it is true or truthy; otherwise, returns the second value

You will use operators extensively in Python to manipulate data and perform computations from it. Refer to https://www.w3schools.com/python/python_operators.asp for a more extensive list of operators that the language supports.

## Add variables to the notebook

Now that you understand the basics of variables, data types, and operators, let's return to the notebook you created in the previous lesson and declare some variables in it. You won't do anything with these variables in this lesson, but you *will* use them in subsequent lessons.

1. Return to the Azure notebook that you created in the previous exercise.

	![Jupyter notebook in Azure](media/2-initial-notebook.png)

	_Jupyter notebook in Azure_

1. Add the following Python code to the empty cell at the end of the notebook:

	```python
	download_url = 'https://t4dmsftlabsdata.file.core.windows.net/airlinedata/airports.csv?st=2018-12-26T18%3A09%3A02Z&se=2018-12-27T18%3A09%3A02Z&sp=r&sv=2018-03-28&sr=f&sig=7WumCj0WoxOt0RZ875Xcj45%2FYgLrqhYf757gUErYj0I%3D'
	```

	This statement defines a variable named `download_url` and assigns it a string value. The string is the URL of a CSV file (a comma-delimited text file) containing a dataset with a list of more than 6,500 airports in the United States, along with their airport codes, locations, and names. The original source of the data is a [Bureau of Transportation Statistics Web site](https://www.transtats.bts.gov/Download_Lookup.asp?Lookup=L_AIRPORT). You won't be using this data just yet, but you will use it in a subsequent lesson once you learn how to download files from the Web in Python. In the meantime, you will use a file that has already been downloaded for you.

1. Now add these statements to the same cell:

	```python
	airport_file_has_header = True
	airport_file_name = 'airports.csv'
	```
	
	The source data file has a header for the first row. Later, `airport_file_has_header` will be used to tell your code to ignore the first line when importing data. `airport_file_name` stores the name of the file containing the airport data. You will use this in a subsequent lesson to save the downloaded airport data.

1. Add the following statement to the cell:

	```python
	state_abbr = state_abbr or 'VA'
	```

	The purpose of this statement is to assign the string value 'VA' (the abbreviation for Virginia) to the variable named `state_abbr` if that variable doesn't already a value.

1. Add the following statement to the cell to generate a file name and assign it to `state_airport_file_name`:

	```python
	state_airport_file_name = state_abbr.lower() + '_airports.csv'
	```
	
1. Run the cell. Note that there is no output from any of the statements you added. The variables that you defined will be used in future lessons.

	![Running the cell](media/3-run-cell.png)
	
	_Running the cell_

Finish up by using the **File** -> **Save and Checkpoint** command to save the notebook.