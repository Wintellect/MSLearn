# Structuring data with sequences and maps

Most programming languages provide helpful data structures for manage collections of data. Some data structures manage the collection as items accessed via their positional index in the collection. Some data structures manage the collection via key/value pairs where each item is accessed via key which is mapped to the item

In Python, indexed collections are called sequences and key/value pair collections are called maps. Within the sequence types there are both mutable and immutable sequences. Mutable sequences can change and immutable sequences can never be changed. There are three immutable sequences: string, tuple and bytes. There are two mutable sequences: list and byte arrays. In this course the following types will be used: strings, tuples and lists. For mapping types there is only the dictionary which will be explored as well.

## Exploring Tuples

In this exercise, Python tuples will be explored. Tuples are used all of the time in Python. There are nothing more than a short sequence of values where the sequence is immutable once created. Tuples are commonly used to return multiple value from a function.

1. Create a new Jupyter notebook named 'Sequence and Map Exercises' in Azure Notebooks.

1. Type the following code into notebook cell and run the cell:

	```python
	letters = ('a', 'b', 'c')
	
	print(letters[0]) # outputs 'a'
	print(letters[1]) # outputs 'b'
	print(letters[2]) # outputs 'c'
	```

	Observe the comma separated list of letters being assigned to the `letters` variable. Commonly, paranthese will be wrapped about the tuple elements but this is not required. The following code would work as well:

	```python
	letters = 'a', 'b', 'c'
	
	print(letters[0]) # outputs 'a'
	print(letters[1]) # outputs 'b'
	print(letters[2]) # outputs 'c'
	```

	Items in the tuple are accessed via their positional location in the tuple using a zero-based index. The index of the first item is 0, the second item is 1, so on and so forth.

1. The tuple itself is an actual type, add the following code after the print statements in the same cell.

	```python
	print(type(letters))
	```

1. Commonly, tuples are used to return multiple values from a function. Type the following code into a new notebook cell and run it:

	```python
	
	def do_it():
	  return 'some data', 42
	
	result = do_it()
	
	print(result[0]) # outputs: 'some data'
	print(result[1]) # outputs: 42
	```

	Observe the values are access using an index on the `result` variable

1. In addition to using a single variable, any iterable (which includes tuples) can be unpacked into multiple variables through multiple assignment. Modify the code from the previous step to use multiple assignment and run the code: 

	```python
	
	def do_it():
	  return 'some data', 42
	
	msg, amt = do_it()
	
	print(amt) # outputs: 'some data'
	print(msg) # outputs: 42
	```

Tuples are very useful structures for temporarily organizing a collection data and using it within an application.

## Exploring Lists

Lists serve as the general purpose, common mutable collection structure within Python. Python lists can be thought of as Python's array structure (for those of you coming from another programming language).

  Note: Python lists are not true arrays and can have performance issues. If you need a true array checkout NumPy's array structure provided by the NumPy package covered later in this modiule.

1. If not already open, open the same notebook you created for the tuples exercise.

1. Add the following code to a new notebook cell and run it.

	```python
	colors = [ 'red', 'green', 'blue' ]
	print(colors[0]) # outputs: red
	print(type(colors)) # outputs: 3
	print(len(colors)) # outputs: <class 'list'>
	```

1. New items can be added to the list using the `append` function. In the current cell, add the following lines of code, and run the cell.

	```python
	colors.append('orange')
	
	print(len(colors)) # outputs: 4
	print(colors) # outputs: ['red', 'green', 'blue', 'orange']
	```

	The color 'orange' was appended to the end of the list.

1. Items can be removed from the list using the `remove` function. In the current cell, add the following lines of code, and run the cell.

	```python
	colors.remove('green')
	
	print(len(colors)) # outputs: 3
	print(colors) # outputs: ['red', 'blue', 'orange']
	```

	The color 'green' was removed from the list.

1. Items can be inserted into the middle of list.

	```python
	colors.insert(1, 'green')
	
	print(len(colors)) # outputs: 4
	print(colors) # outputs: ['red', 'green', 'blue', 'orange']
	```

	The color 'green' was inserted in to the list at index position 1.

1. Python provides a number of useful functions for transforming and filtering sequences such as lists. For example, the following code uses the `map` function to iterate over each item in the list and apply the `double` function to it. The return values are used to produce a new list. Create a new cell, type the following code into and run the cell.

	```python
	def double(n):
	  return n * 2
	
	nums = [1,2,3,4]
	double_nums = list(map(double, nums))
	print(double_nums) # outputs: [2, 4, 6, 8]
	```

1. Another useful function is the filter function. For example, the following code uses the `filter` function to iterate over each item in the list and apply the `even` function to it. For each return value that is equal to true the list item will be added to a new list. Create a new cell, type the following code into the new cell and run.

	```python
	def even(n):
	  return n % 2 == 0
	
	nums2 = [1,2,3,4,5,6,7,8]
	even_nums = list(filter(even, nums2))
	print(even_nums) # outputs: [2, 4, 6, 8]
	```

1. Python lists (and all sequences) have extensive support for slicing. Create a new cell, type the following code into the new cell and run it.

	```python
	letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	
	print( letters[2] ) # outputs: 'c'
	print( letters[2:] )
	print( letters[2:8] )
	print( letters[2:8:2] )
	print( letters[-1] )
	print( letters[-3: -1] )
	```

	A single index value returns the item from that position in the list. In this case the item in positional index 2 will be returned which is the letter 'c'.

1. Add the following code to the same cell.

	```python
	print( letters[2:] ) # outputs: ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	```

	With the colon included after the index position of 2 all items with an index of 2 and greater will be returned from the list.

1. Add the following code to the same cell.

	```python
	print( letters[2:8] ) # outputs: ['c', 'd', 'e', 'f', 'g', 'h']
	```

	With an index value of '2:8' all items with positional index from 2 to 7 will returned. While 8 is listed in the range, the index range goes up to but not including 8.

1. Add the following code to the same cell.

	```python
	print( letters[2:8:2] ) # outputs: ['c', 'e', 'g']
	```

	The second 2 in '2:8:2' is a step value. So in this case, the step value will cause every other item to be returned. So the items at positional indexes of 2, 4, and 6 will be returned.

1. Add the following code to the same cell.

	```python
	print( letters[-1] ) # outputs: j
	```

	The negative number indicates to start from the end of the list. So the value of 'j' will be returned since it is the last item in the list.

1. Add the following code to the same cell.

	```python
	print( letters[-3: -1] ) # outputs: ['h', 'i']
	```

	The range will start from the third from the end of the list up to but not including the last item in the list.

## Exploring Dictionaries

In this exercise, dictionaries will be explored. Dictionaries are key/value maps. With a key a value can be retrieved up. When adding new values, they are added along with a key to look them up in the future.

1. If not already open, open the same notebook you created for the lists exercise.

1. Dictionaries are initialized using curly braces. Add the following code to a new notebook cell and run it.

	```python
	person = {}
	```

	This will create an empty dictionary.

1. Initial key/value pairs can be initialized within the curly braces definition of a dictionary. Modify the previous notebook cell with the following code and run it.

	```python
	person = {
	  'first_name': 'Bob',
	  'last_name': 'Smith',
	  'age': 42
	}
	
	print( person['first_name'] )
	```

	Each key/value pair is configured with a colon between the key and value. Multiple key/value pairs are separated by a comma. To access an item in the dictionary, square brackets with a string of the key is used.

1. A common operation with dictionaries to check to see if a dictionary has a certain key. Add the following code to end of the current notebook cell and run it.

	```python
	print( 'first_name' in person )
	```

	Using the `in` operator, it is possible to check the dictionary for a key.

1. It is possible to iterate over the keys of dictionary using the `for-in` loop. Add the following code to the end of the cell and run it.

	```python
	for key in person:
	  print(key)
	```

	Each `key` in the `person` dictionary will be displayed.

1. Modify the previous `for-in` using the code below and run the cell.

	```python
	for key in person:
	  print(key + '=' + str(person[key]))
	```

	Using the `key` each value in the `person` dictionary can be retrieved.

1. Using the `keys` and `values` functions on the dictionary object all of the keys and values of the dictionary object can be retrieved. Add the following code to the current cell and run it.

	```python
	print( person.keys() ) # output: dict_keys(['first_name', 'last_name', 'age'])
	print( person.values() ) # output: dict_values(['Bob', 'Smith', 42])
	```

1. New key/value pairs can be added to the dictionary using the square bracket syntax. Add the following code to the current cell and run it.

	```python
	person['city'] = 'Redmond'
	
	for key in person:
	  print(key + '=' + str(person[key]))
	```

	The new key and its value is output.

1. A key and its value can be removed from the dictionary using the `del` statement. Add the following code to the current cell and run it.

	```python
	del person['age']
	
	for key in person:
	  print(key + '=' + str(person[key]))
	```

	The 'age' key and its value have been removed.

## Loading Airport and State Data

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this first exercise within the module, the airport and state data look up tables will be loaded.

1. Create a new Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks.

2. Create a new cell, add the following code to the cell.

	```python
	import csv
	```

	Python provides a `csv` module which will read and write CSV files. The `import` statement will import this module for usage within the Jupyter notebook (or Python program)

1. Create a new cell, add the following code to the cell.

	```python
	def do_strip(x):
	    return x.strip()
	
	def split_strip(value, split_value = ','):
	    return tuple(map(do_strip, value.split(split_value)))
	```

	The `split_strip` function will split a string into a list and trim the excess white space surrouding each substring in the new list. The string API `split` function is used to split the string at each occurence of the `split_value` (default is a comma) in to a list. Using the `map` function, the `do_strip` function is applied to each item in the list. The return value from `do_strip` is a trimmed value which is added to a new `map` object which is then converted to a tuple using the `tuple` function. The final tuple is returned from the `split_strip` function.

1. Create a new cell, add the following code to the cell.

	```python
	def create_state(state_data):
	
	    state_abbr, state_name_data = state_data
	    country =  'United States'
	
	    state_name_parts = split_strip(state_name_data)
	
	    state_name = state_name_parts[0]
	    if (len(state_name_parts) == 2):
	        country = state_name_parts[1]
	        state_label = 'province'
	    else:
	        state_label = 'state'
	
	    return {
	        'code': state_abbr,
	        'name': state_name,
	        'label': state_label,
	        'country': country
	    }
	```

	The function receives the raw state data from the CSV file and processes it into a dictionary object containing the state abbreviation, state name, state label (state or province), and the country in which the state is located. The dictionary object is used to store data related to a single state.

1. Create a new cell, add the following code to the cell.

	```python
	def load_states(states_csv_file_name):
	
	    states = {}
	
	    with open(states_csv_file_name, 'r') as states_csv_file:
	        states_csv_file_reader = csv.reader(states_csv_file, delimiter=',')
	        for state_line_number, state_data in enumerate(states_csv_file_reader):
	            if state_line_number == 0: continue
	            state = create_state(state_data)
	            states[state['code']] = state
	  
	    return states
	```

	The function `load_states` loads the specified CSV file and processes it with the CSV reader provided by the CSV module. For each state, the a new state dictionary is created from the raw state data using the `create_state` function. Finally, each state is added to a `states` dictionary using the state abbreviation at the key value.

1. Create a new cell, add the following code to the cell.

	```python
	def create_airport(airport, states):
	
	    code = airport[0]
	    name = ''
	    city = ''
	    state_label = ''
	    state_name = ''
	    country = ''
	
	    desc_parts = split_strip(airport[1], ':')
	
	    if len(desc_parts) == 2:
	        location, name = desc_parts
	        location_parts = split_strip(location)
	
	        if len(location_parts) == 2:
	            city = location_parts[0]
	            state_code = location_parts[1]
	
	            if state_code in states:
	                state = states[state_code]
	                state_name = state['name']
	                state_label = state['label']
	                country = state['country']
	            else:
	                country = state_code
	
	    else:
	        name = desc_parts[0]
	
	    return {
	        'code': code,
	        'name': name,
	        'city': city,
	        'state_name': state_name,
	        'state_label': state_label,
	        'country': country 
	    }
	```

	This `create_airport` function serves the same purpose as the `create_state` function.

1. Create a new cell, add the following code to the cell.

	```python
	def load_airports(airport_csv_file_name, states):
	
	    airports = {}
	
	    with open(airport_csv_file_name, 'r') as airports_csv_file:
	        airports_csv_file_reader = csv.reader(airports_csv_file, delimiter=',')
	        for airport_line_number, airport_data in enumerate(airports_csv_file_reader):
	            if airport_line_number == 0: continue
	            airport = create_airport(airport_data, states)
	            airports[airport['code']] = airport
	      
	    return airports
	```

	The `load_airports` function does the same thing as the `load_states` function. In addition to processing the raw airports CSV file data, the `load_airports` function uses the loaded states data to expand on the location information provided by the airports CSV file. Organizing the states data as a dictionary makes it easy to find the state information using the state abbreviations contained in the airports CSV file.

1. Create a new cell, add the following code to the cell.

	```python
	states = load_states('states.csv')
	print('Number of states: ' + str(len(states)))
	airports = load_airports('airports.csv', states)
	print('Number of airports: ' + str(len(airports)))
	```

	Using the data files provided, load the states and airports data. For extra credit, explore the states and airports dictionaries.