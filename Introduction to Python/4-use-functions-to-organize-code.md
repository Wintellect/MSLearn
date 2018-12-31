# Use functions to organize code

Computer programs grow in size quickly. Almost every program has blocks of code that need to be repeated. Consider the following code, which contains two loops:

```python
items = ['apples', 'oranges', 'bananas']

for item_index, item in enumerate(items):
    print(str(item_index + 1) + '. ' + item)
    
print('')

items = ['carrots', 'broccoli', 'corn']

for item_index, item in enumerate(items):
    print(str(item_index + 1) + '. ' + item)
```

Both loops do exactly the same thing. They iterate over a list of items, printing each item with a numbered prefix indicating its position in the list. Repeating the code for both loops is poor program design. It makes the program longer, and if you find and fix a bug in one of the loops, you have to fix it in the other loop, too. The problem is only exacerbated if a block of code is repeated 20 times rather than two. 

In this lesson, you will learn how to use functions in Python to factor your code and avoid the pitfalls of copy-and-paste programming. Your code will be more readable and more maintainable. And if you find that you need to modify the logic for a programming task that is executed multiple times, you will only have to change it in one place.

## Functions

Functions are blocks of code that are called by name. They can accept parameters containing input to be operated upon, and they can return values. A function that includes parameters can be called many times with different values passed in each time, allowing it to behave differently every time it is called.

In Python, a function is defined with the `def` statement. A very simple function named `greet` that accepts no parameters and returns no value can be defined this way:

```python
def greet():
    print('Hello, World!)
```

A function that adds two numbers and returns the sum can be defined like this:

```python
def add(a, b):
    return a + b
```

The `add` function would be called this way to add 2 and 2:

```python
sum = add(2, 2)
```

By convention, words in multi-word function names are separated by underscores. (This is a convention, not a requirement.) Here's a function that accepts a list and prints the items in the list:

```python
def print_item_list(the_items):
    for item_index, item in enumerate(the_items):
        print(str(item_index + 1) + '. ' + item)
```

And here is an updated version of the code in the introduction that replaces redundant blocks of code with calls the `print_item_list` function:

```python
def print_item_list(the_items):
    for item_index, item in enumerate(the_items):
        print(str(item_index + 1) + '. ' + item)
    
items = ['apples', 'oranges', 'bananas']
print_item_list(items)

print('')

items = ['carrots', 'broccoli', 'corn']
print_item_list(items)
```

### Using built-in functions

`print_item_list` is a custom function, but it calls another function named `enumerate`. The latter is built into Python. `enumerate` iterates over a sequence and returns a sequence known as a `tuple`. The `tuple` is an immutable sequence that is used to return multiple values from a function. The `tuple` returned by `enumerate` contains the item's index as well as the item itself.

The following code is valid, but harder to read:

```python
def print_item_list(the_items):
    for the_item in enumerate(the_items):
        print(str(the_item[0] + 1) + '. ' + the_item[1])
```

This is easier to read:

```python
def print_item_list(the_items):
    for item_index, item in enumerate(the_items):
        print(str(item_index + 1) + '. ' + item)
```

Separating the `tuple` into discrete items named `item_index` and `item` is known as *destructuring*. It's a feature of Python that programmers use to write readable and more maintainable code.

`enumerate` is one of approximately 60 functions that are built into Python. Others include `abs`, `len`, `print`, and `type`. For a complete list of built-in functions, see https://docs.python.org/2/library/functions.html. 

### Returning data from a function

All functions in Python return a value, even if not explicitly stated with a `return` statement. For functions without an explicit return value, the value of `None` is returned:

```python
def do_it():
    print('did it')
    
result = do_it()

print(result) # outputs: None
print(type(result)) # outputs: <class 'NoneType'>
```

`None` simply indicates that the function did not return an explicit value.

### Defining default parameter values

Function parameters can be assigned default values. The default value is used if an explicit value isn't specified when the function is called. If a value *is* specified, that value overrides the default value:

```python
def display_message(msg, msg_type = 'INFO'):
    print(msg_type + ': ' + msg)

display_message('Hello!') # outputs: Hello!: INFO
display_message('Hello!', 'ALERT') # outputs: Hello!: ALERT
```

### Using named parameters

When you pass a parameter in a function call, you have the option of specifying the parameter's name:

```python
def display_message(msg, msg_type = 'INFO'):
    print(msg_type + ': ' + msg)

display_message('Hello!', msg_type = 'ALERT')
```

This isn't especially useful when a function accepts just one or two parameters, but it can be very useful when the function accepts a lot of parameters. Among other things, it lets you specify values for some parameters without specifying values for others.

## Filter airport data by US state

Now let's put what you have learned about functions to work in the notebook you are assembling.

1. Return to the Azure notebook that you created previously.

	![Jupyter notebook in Azure](media/2-initial-notebook.png)

	_Jupyter notebook in Azure_

1. In the empty cell at the end of the notebook, add the following function:

	```python
	def parse_airport_data(airport_data):
	    
	    # skip first character (a double quote), and start with second character (index = 1)
	    airport_data_start = 1
	    
	    # ignore last character (a double quote), minus 2 because of zero-based indexes
	    airport_data_end = len(airport_data) - 2
	    
	    # slide off first and last character
	    airport_data_temp = airport_data[airport_data_start:airport_data_end]
	    
	    # split on quoted comma to get airport code and name
	    code, name = airport_data_temp.split('","')
	    return {
	        'code': code,
	        'name': name
	    }
	```

	The function, which is named `parse_airport_data`, will receive raw airport data and return dictionay containing a `code` field and a `name` field. The `code ` field should be populated from the "Code" column of the "airports.csv" file. The `name` field should be populate from the "Description" column of the "airports.csv" file.




1. Add a function named `filter_airports_by_state` to the new cell. The function will receive a list of airports and return a filtered list of airports for a particular state.

	```python
	def filter_airports_by_state(airports, filter_by_state_abbr):
	    
	    filtered_airports = []
	    formatted_state_abbr = ' ' + filter_by_state_abbr + ':'
	    
	    # in statement can be used with for-in loops to iterate over sequences and
	    # can be used with the if statement to check a sequence to see if it contains
	    # a value
	    for airport in airports:
	        if formatted_state_abbr in airport['name']:
	            filtered_airports.append(airport)
	    
	    return filtered_airports
	```

1. Add a function named `airport_to_csv` to the new cell. The function will return an airport formatted to be a row of CSV data.

	```python
	def airport_to_csv(airport):
	    return '"' + airport['code'] + '","' + airport['name'] + '"'
	```

1. Declare a new variable named `all_airports` and initialize it to an empty list. Iterate over all of the airport data, parse each item of airport data and append it to the `all_airports` list.

	```python
	all_airports = []
	for airport_data in all_airports_data:
	    all_airports.append(parse_airport_data(airport_data))
	```

1.  Use the `state_abbr` variable whose value was capture by the `input` statement and produce a list of airports filtered by the state abbreviation. Store the filtered list in a variable named `state_airports`.

	```python
	state_airports = filter_airports_by_state(all_airports, state_abbr)
	```

1. Create a new variable named `state_airports_data` and initialize it to an empty string. Iterate over the list of `state_airports` and produce a string of newline separated state airport CSV formatted date. 

	```python
	state_airports_data = ''
	for state_airport in state_airports:
	    state_airports_data = state_airports_data + airport_to_csv(state_airport) + '\n'
	```

1. Print the string of `state_airports_data` to ensure the data was extracted as expected.

TODO: Add closing.