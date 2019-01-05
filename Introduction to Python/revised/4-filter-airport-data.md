# Filter airport data

Now that the airport data in **airports.csv** has been parsed into a list of lists with each item in the inner list containing strings denoting an airport code, airport location, and airport name, the data can be organized and presented in more meaningful ways. In this lesson, you will filter the list of lists created in the previous lesson so that it includes only U.S. airports. Then you will add logic that permits users to enter the abbreviation for a U.S. state and produce a list (and a count) of all the airports in that state. 

## Generate a list of U.S. airports

Let's start by using what you already know plus the `endswith` function that can be called on strings in Python to generate a new list of lists that contains only U.S. airports.

1. Return to the Azure notebook that you created in the first lesson.

1. Add the following code to the end of the notebook to create a list named `us_airports` that includes only airports located in the U.S.:

	```python
	us_airports = []
	
	us_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
	          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
	          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
	          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
	          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
	
	for airport in airports:
	    if airport[1].endswith(tuple(us_states)):
	        us_airports.append(airport)
	```

	TODO: Explain this code, especially the tuple.

1. Run the cell and verify that it executes without error. Then add the following code to the empty cell at the end of the notebook to list all U.S. airports:

	```python
	for airport in us_airports:
	    print('{0:8}{1:32}{2:1}'.format(airport[0], airport[1], airport[2]))
	```

1. Run the cell and confirm that the output includes only airports in the United States:

	![Printing a list of U.S. airports](media/print-us-airports.png)

	_Printing a list of U.S. airports_

1. Use the **File** -> **Save and Checkpoint** command to save the notebook.

The next step is to add code that prompts the user for a state abbreviation and filters the list down to those airports located in that state. But first, let's take a moment to learn about an important building block of Python programs: functions.

## Functions in Python

Functions are blocks of code that are called by name. They can accept parameters containing input to be operated upon, and they can return values. A function that includes parameters can be called many times with different values passed in, allowing it to behave differently each time it is called.

Functions are important because they promote code reuse. Rather than copy-and-paste a block of code 10 times, you can place the same code in a function and call the function 10 times. If you later discover that the code needs to be modified (perhaps because you found a bug), you only have to change it one place. 

Python contains more than 60 built-in functions that you can call at any time. You have already used some of these functions: `print`, `input`, and others. A complete list of built-in functions can be found [here](https://docs.python.org/2/library/functions.html). Significantly, you can also define functions of your own to help organize your code and make it more readable and more maintainable.

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
def print_list(items):
    for item_index, item in enumerate(items):
        print(str(item_index + 1) + '. ' + item)
```

The function shown in the previous example calls a built-in function named `enumerate`. `enumerate` iterates over a sequence and returns a sequence known as a `tuple`. The `tuple` is an immutable sequence that is used to return multiple values from a function. The `tuple` returned by `enumerate` contains the item's index as well as the item itself. The following code is valid, but less intuitive and harder to read:

```python
def print_list(items):
    for item in items:
        print(str(item[0] + 1) + '. ' + item[1])
```

Separating the `tuple` into discrete items named `item_index` and `item` is known as *destructuring*. It's a feature of Python that programmers use to write code that is more easily maintained.

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

This isn't especially useful when a function accepts just one or two parameters, but it can be very useful when the function accepts a lot of parameters. Among other things, it lets you specify values for some parameters without specifying values for others. You used this feature in an earlier lesson when you wanted to prevent `print` from outputting a newline at the end of each line.

## Filter airport data by state

Now let's enhance the notebook to allow users to interactively query the data for airports in a specified state. And let's use functions to make the code both compact and tidy.

1. Return to the Azure notebook in which you generated a list of U.S. airports. In the empty cell at the end of the notebook, add the following function definition:

	```python
	def get_airports_by_state(airports, state):
	    result = []
	    for airport in airports:
	        if airport[1].endswith(state):
	            result.append(airport)
	    return result
	```

1. Run the cell to make sure there are no syntax errors. Then add the following code to the empty cell at the end of the notebook:

	```python
	state = input('Enter a state abbreviation: ')
	state_airports = get_airports_by_state(us_airports, state)
	
	for airport in state_airports:
	    print('{0:8}{1:32}{2:1}'.format(airport[0], airport[1], airport[2]))
	```

1. Run the cell and enter a state abbreviation such as TN or VA. Then press **Enter**. Confirm that the result is a list of airports in that state:

	![Airports in the state of Tennessee](media/print-tn-airports.png)

	_Airports in the state of Tennessee_

1. On your own, modify the code in the previous cell to show the number of airports in the specified state:

	![Modified output](media/modified-output.png)

	_Modified output_

	Hint: You can use the `len` function to count the number of items in a list. And you can use Python's built-in `str` function to convert the number returned by `len` into a string.

1. Use the **File** -> **Save and Checkpoint** command to save the notebook.

You have now filtered the list so that it only includes U.S. airports and given the user the ability to query the filtered list state by state. In the next lesson, you will enhance the output with some visualizations. If a picture is worth a thousand words, then a few well-placed visualizations will dress up the output and present it in a more meaningful way.