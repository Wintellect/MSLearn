# Use variables, types, and operators

In programming languages (as well as mathematics), variables are used to store temporary data. Variables are used in expressions to execute logic (programming code) which manipulates variables to calculate new values. Consider the following expression:

```python
x + 1
```

The symbol 'x' is a variable. Its value can be changed and then evaluated within the expression to produce new values. For example, when x is 2, the value of the expression is 3. When x is 5, the value of the expression 6. Variables hold values and expressions use variables along with other logic to produce new values.

In Python, a variable is declared and populated with data using the assignment operation, the equals "=" sign. The variable being assigned to is on the left-hand side of the assignment operator and the expression being evaluated is on the right-hand side of the assignment operator.

```python
x = 1 # assign an expression which is a constant value

y = x + 5 # use a variable in an expression

z = y # an expression can be a single variable
```

When performing assignment the variable receiving the value is on the left-hand side and the expression being evaluated is on the right-hand side.

### Working with Data Types

Another common feature of programming languages is data types for storing data. Each language comes with many predefined types and the ability to define new types composed of predefined types. Unlike many other languages, Python represents all data as an object. Python provides many special purposes types as well as more standard types.

#### Numbers

A common set of types are types which store numbers. Computers treat integer numbers and decimal numbers differently. Consider the following code:

```python
x = 1 # integer

x = 1.0 # decimal (known as floating point)
```

To see their types, use the **type** statement with the **print** statement as follows:

```python
x = 1
print(type(x)) # outputs: <class 'int'>

x = 1.0
print(type(x)) # outputs: <class 'float'>
```

The addition of the ".0" to the end of "1" makes a big difference in how the programming language understands the data type of the value. The data type impacts how the value is stored in memory, how the processor (CPU) handles the data when evaluating expressions, how the data relates to other data, and what kinds operations can be performed with it.

Another common type is the boolean type with the values of **True** and **False**.

```python
x = True
print(type(x)) # outputs: <class 'bool'>
```

From Python's perspective, boolean is a special type of integer. Technically, **True** has a value of 1 and **False** has a value of 0. Typically, booleans are not used to perform numerical mathematical expressions; nevertheless, it is interesting to understand the relationship between types. Many types are nothing more than specialized versions of more general types. Integers are a subset of floating point numbers, and booleans are a subset of integers.

#### Sequences

Sequences are a collection of some kind of data type. In many programming languages, sequences are referred to as arrays. The most commonly used collection is a sequence of characters known as a string. Python does not have an explicit character type like other programming languages (although the character type in other languages is really nothing more than an integer type). Instead, Python treats all collections of characters (zero or more) as something called a string. Strings are used all of the time. Any text data defined within double quotes or single quotes is a string value.

```python
x = 'This is a string.'
print(type(x)) # outputs: <class 'str'>
```

Strings can be added to other strings:

```python
x = 'Hello' + ' ' + 'World!'
print(x) # outputs: Hello World!
```

When quoting strings, either a pair of double quotes or single quotes may be used. There is no difference between the produced strings. If a string contains a double quote then usually the single quotes will be used and if the string contains a single quote then double quotes will be used.

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

If the string contains the same quote character as the quote character wrapping the string then the quote character within the string must be escaped with a backslash.

```python
x = 'Tim said, \'Hello World!\''
print(x) # outputs: Tim said, 'Hello World!'
```

Another useful feature of strings (and all sequences) is the ability to slice out part of the sequence, or in the case of strings, the ability to slice out characters in the string.

```python
x = 'Python is a fun language with which to code.'
print(x[12:15]) # outputs: fun
```

The square brackets are used to indicate slicing and the numbers indicate the starting index of the slice and the ending index of the slice. The index is the number of characters the character is from the start of the string. The first character has an index of zero (this is known as zero-based indexing). The second character has an index value of 1, the third character has an index value of 2, so on and so forth. The sequence value (for a string, the character value) of the ending index is not included in the sliced data. Python is famous for the power of its slicing abilities. The ability to slice data is heavily used throughout all Python applications especially when performing data analysis for tasks such as machine learning.

#### Strings

Strings are one of the common kinds of sequences. They are a sequence of characters. String objects come with an extensive API (application programming interface) for manipulating the string of characters.

For example, the upper function changes a string's characters to all uppercase.

```python
message = 'Hello'

message.upper()

print(message) # outputs: HELLO
```

Likewise, the lower function changes the string to be all lowercase.

```python
message.lower()

print(message) # outputs: hello
```

The replace function takes a search string to search for within the original string. Each time the search string is found it is replaced with a replacement string.

```python
message = 'This is fun!'

message.replace('is', 'was')

print(message) #outputs: This was fun!
```

#### List of Data

In addition to strings, there are several other kinds of sequences. A commonly used sequence is the list. The list is a sequence of any type similar to an array in other languages such as JavaScript, Java, C# or C++. Lists are mutable (they can be changed) which means items can be added and removed from the list.

    Note: The terms mutable and immutable are frequently used in the programming. Mutable means the memory referenced by a variable can be changed. Immutable means the memory referenced by a variable cannot be changed. For example, strings are immutable. Each time a string is changed, a new string is created in memory. Lists are mutable, items can be added and removed. There are many reasons why structures are chosen to be mutable or immutable. Discussion of those reasons is beyond the scope of this tutorial; nevertheless, keep those two terms in mind as they will become more important as you progress in your learning and usage of Python.

To create a list, wrap a sequence of value with square brackets with each item separated with commas:

```python
nums = [1,2,3,4,5]
print(nums) # outputs: [1, 2, 3, 4, 5]
print(type(nums)) # outputs: <class 'list'>
```

To access an item in the list, an item is referenced by index using the square brackets:

```python
nums[2] # outputs: 3
```

The same slicing syntax used for strings can be used for lists (because both are sequences):

```python
nums[1:4] # outputs: [2, 3, 4]
```

To add an item to the list:

```python
nums.append(6)
print(nums) # outputs: [1, 2, 3, 4, 5, 6]
```

To remove an item from the list:

```python
nums.remove(4)
print(nums) # outputs: [1, 2, 3, 5, 6]
```

To find the length of a list (or any sequence including strings) the len function is used:

```python
print(nums) # outputs: [1, 2, 3, 5, 6]
print(len(nums)) # outputs: 5
```

Sequences are very useful and have many more features. In the course following this one, [Introduction to Handling Data in Python](#), sequences are further explored.

#### Strings and Lists

Commonly, strings and lists are used together. Lists can be used to create strings and strings can be used to create lists.

A common operation is to split a string into a list of items. Consider the following example a colors string split into a list of colors using the **split** function:

```python
colors_data = 'red,green,blue'

colors = colors_data.split(',')

print(colors) # outputs: ['red','blue','green']
```

Another common example is converting a list into a string using the **join** function:

```python
colors = ['red','blue','green']

colors_data = ','.join(colors)

print(colors_data) # outputs: 'red,green,blue'
```

#### The None Value

Most programming languages have some kind of value which means an absence of a value. The name of this value can go by many different names: null, nil, and undefined. In the Python the name of the value which represents the absence of a value is **None**.

```python
some_var = None
```

The **None** value is more than only a value it is also a type, the **NoneType**.

```python
type(None) # outputs: NoneType
```

Functions (covered later in this module) return a value of **None** if they do not have an explicit return type.

#### Truthy and Falsy

Like many programming languages, Python has the concept of truthy and falsy. The concept of truthy and falsy associates a true or false value with a non-boolean type. For example, the value of 1 is truthy but the value of 0 is falsy. The value of 'Some Content' is truthy, but the value of '' (zero-length string) is falsy. The value of None is falsy. 

### Operators

Python expressions use operators to calculate new values. The behavior of operators is determined by the type of data upon which the operator is being applied. For example, the plus operator "+" with numbers adds them together and the plus operator with strings concatenates them together.

```python
print('a' + 'a') # outputs: aa
print(1 + 1) # outputs: 2
```

Some operators are applied to one value (the value is the result of another expression) these are known as unary operators. For example, the not operator outputs False for a True value and True for a False value.

```python
print(not True) # outputs: False
```

Some operators are applied to two values. When using two values they must compatible types.

For example, the following values are compatible types: 

```python
print(1 + 1.0) # Valid because both 1 and 1.0 are numbers, the output is 2.0
print(1 +  True) # Valid because booleans are an integral type, the output is 2
```

Here is an example of incompatible types:

```python
print(1 + 'a') # This will throw a type error, strings and numbers are not compatible with the plus operator
```

There are lots of operators in Python, here are some of the more common ones:

* \+ - adds two numbers, concatenates two strings
* \- - subtracts two numbers
* \* - multiplies two numbers
* \/ - divides two numbers

* not - return the opposite of true or false
* and - returns the first value if it is false or falsy; otherwise, returns the second value
* or - returns the first value if it is true or truthy; otherwise, returns the second value

### Exercise: Initializing Variables for Importing Airport Data

**Step 1.** If not open, open the "Prepare US State Airport Data" notebook created in the previous exercise.

**Step 2.** Add a new Python cell to the end of the notebook.

**Step 3.** Add to the cell the following Python code:

```python
download_url = 'https://t4dmsftlabsdata.file.core.windows.net/airlinedata/airports.csv?st=2018-12-26T18%3A09%3A02Z&se=2018-12-27T18%3A09%3A02Z&sp=r&sv=2018-03-28&sr=f&sig=7WumCj0WoxOt0RZ875Xcj45%2FYgLrqhYf757gUErYj0I%3D'
```

To access the airport data needed for the exercise it must be downloaded from Azure Storage when using Azure Notebooks. The original source of the data is here: [BTS Link](https://www.transtats.bts.gov/Download_Lookup.asp?Lookup=L_AIRPORT)

The **download_url** will be used in the last exercise to download the data using Python code. For now, a pre-downloaded file will be used.

**Step 4.** Add the following Python code to the cell:

```python
airport_file_has_header = True
airport_file_name = 'airports.csv'
```

The source data file has a header for the first row. Setting the variable **airport_file_has_header** to true will tell the code which will be written later that the first row of the file should be ignored.

The variable **airport_file_name** will store the file name which contains the airport data. In the last exercise this variable will be used to save the downloaded airport data.

**Step 5.** Add the following Python code to the cell:

```python
state_abbr = state_abbr or 'VA'
```

If no value for the variable **state_abbr** is specified, set the variable **state_abbr** to 'VA'.

**Step 6.** Add the following Python code to the cell:

```python
state_airport_file_name = state_abbr.lower() + '_airports.csv'
```

Convert the variable **state_abbr** to lowercase and use it to set the variable for the extracted state file name.

**Step 7.** Run the cell. There is no output for this exercise. These variables will be used in future exercises.