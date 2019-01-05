# Parse airport data

In the previous lesson, you uploaded a CSV file containing a list of airports all over the world to Azure Notebooks and wrote some Python code to read the file and create a list of strings from the file's content. In this lesson, you will parse the content that you read and convert the data into a more useful format. Before you start, let's take a moment to learn more about strings in Python.

## Working with strings in Python

Strings are among the most commonly used data types. A string is simply a collection of zero or more characters. Python does not have an explicit character type like many other programming languages do. Any text data defined within single or double quotation marks is a string value:

```python
message = 'This is a string'
print(message) # outputs: This is a string
```

Strings can be added to other strings (an operation known as "concatenation") with the `+` operator:

```python
message = 'Hello' + ' ' + 'World!'
print(message) # outputs: Hello World!
```

When quoting strings, you may use single or double quotation marks. There is no difference between the resulting strings. You can embed a double quotation mark in a string by enclosing the string itself in single quotes, and you can embed a single quotation mark in a string by enclosing the string in double quotes. If the string contains the same quotation mark as the one used to quote the string, you may escape the embedded quotation mark with a backslash:

```python
message = 'Tim said, \'Hello World!\''
print(message) # outputs: Tim said, 'Hello World!'
```

Strings support slicing using the same syntax used for slicing lists. (Lists and strings are both examples of *sequences* in Python, and slicing can be performed on any sequence.) The following examples demonstrate how slicing is performed and substrings are extracted from other strings:

```python
message = 'This is fun!'
print(message[0]) # outputs T
print(message[0:4]) # outputs This
print(message[:4]) # outputs This
print(message[8:]) # outputs fun!
```

String slicing will play a large role in parsing the airport data that you loaded in the previous lesson. So will string functions, which can be called to manipulate strings in various ways.

### Using string functions

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

A common requirement is to split a string containing a collection of strings separated by commas, spaces, or other characters into a list of strings. Here's an example that splits a string containing a list of strings separated by commas into a list of strings using the `split` function:

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

`upper`, `lower`, `replace`, `split`, and `join` are but a few of the more than 40 functions that you can call on a string in Python. For a complete list, see https://www.w3schools.com/python/python_ref_string.asp.

## Parse the airport data into a list of lists

In this exercise, you will use string slicing and string splitting to parse the strings read from the data file in the previous lesson into a list of lists, with the inner lists containing data regarding individual airports. Lists of lists are very common in Python and are useful for storing tabular data — that is, data that is organized into rows and columns.

1. Return to the Azure notebook that you created in the first lesson.

	![Jupyter notebook in Azure](media/initial-notebook-3.png)

	_Jupyter notebook in Azure_

1. Add the following Python code to the empty cell at the end of the notebook:

	```python
	for airport in all_airports:
	    items = airport.split('","')
	    airport_code = items[0][1:]
	    print(airport_code)
	```

	Based on the discussion of string splitting and slicing in the previous section, can you predict what the output will be?

1. Run the cell and confirm that it produces a lst of airport codes parsed from the strings in the file:

	![Printing airport codes](media/print-airport-codes.png)

	_Printing airport codes_

1. The previous code parsed an airport code from each line read from the data file. The next challenge is to get each airport's name and location as well. Modify the code above as shown below and rerun the cell. Once more, can you predict what the output will be?

	```python
	for airport in all_airports:
	    items = airport.split('","')
	    airport_code = items[0][1:]
	    subitems = items[1].split(': ')
	    airport_location = subitems[0]
	    airport_name = subitems[1][:len(subitems[1]) - 2]
	    print('{0:8}{1:32}{2:1}'.format(airport_code, airport_location, airport_name))
	```

	The last line uses Python's `format` function to format a string. It left-aligns `airport_code` in a field that is 8 spaces wide, `airport_location` in a field that is 32 spaces wide, and `airport_name` in a field that occupies the remainder of the line. It's one way in Python to align printed output into columns.

1. Confirm that the output resembles the output below.

	![Printing airport data](media/print-parsed-airports.png)

	_Printing airport data_

1. You have proven that you can parse the strings read from the input file into airport codes, locations, and names. The next step is to add the airport codes, locations, and names to a list rather than simply print them out. To that end, add the following code to the empty cell at the bottom of the notebook:

	```python
	airports = []
	
	for airport in all_airports:
	    items = airport.split('","')
	    airport_code = items[0][1:]
	    subitems = items[1].split(': ')
	    airport_location = subitems[0]
	    airport_name = subitems[1][:len(subitems[1]) - 2]
	    airports.append([airport_code, airport_location, airport_name])
	    
	for airport in airports:
	    print('{0:8}{1:32}{2:1}'.format(airport[0], airport[1], airport[2]))
	```

	This code defines a new list named `airports` and adds to it a list containing the airport code, location, and name for each line in the input. Then it prints each list in the list of lists.

1. Run the cell and confirm that it produces the same output as the previous cell.

1. Use the **File** -> **Save and Checkpoint** command to save the notebook.

Now that you have separated airport codes, airport locations, and airport names into separate entities, you are prepared to take the next step, which involves filtering the data so you can answer basic questions such as "How many airports are located in the state of Virginia?"
