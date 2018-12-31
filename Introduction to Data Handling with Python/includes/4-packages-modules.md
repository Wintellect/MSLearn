# Using packages and modules


## Airline Data Exercise: Dividing an Notebook into Modules and using a Package

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this fourth exercise within the module, the airport and state dictionary loading code will be moved to a new file and the numpy package will be used.

1. Open the Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks. You may want to make a duplicate copy of this notebook before attempting this exercise.

1. Create a new text file in same folder as 'Airline Data Exercise' notebook. Rename the text file to 'airport_data.py'. Copy the following code from the 'Airline Data Exercise' notebook into the 'airport_data.py' file.

```python
import csv

# map/lambda version
# def split_strip(value, split_value = ','):
#   return tuple(map(lambda x: x.strip(), value.split(split_value)))

# list comprehension version
def split_strip(value, split_value = ','):
  return tuple([ x.strip() for x in value.split(split_value) ])

class State:

  def __init__(self, state_data):

    state_abbr, state_name_data = state_data
    country =  'United States'

    state_name_parts = split_strip(state_name_data)

    state_name = state_name_parts[0]
    if (len(state_name_parts) == 2):
      country = state_name_parts[1]
      state_label = 'province'
    else:
      state_label = 'state'

    self.code = state_abbr
    self.name = state_name
    self.label = state_label
    self.country = country
    
def load_states(states_csv_file_name):

  states = {}

  with open(states_csv_file_name, 'r') as states_csv_file:
    states_csv_file_reader = csv.reader(states_csv_file, delimiter=',')
    for state_line_number, state_data in enumerate(states_csv_file_reader):
      if state_line_number == 0: continue
      state = State(state_data)
      states[state.code] = state  
  return states

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
          state_name = state.name
          state_label = state.label
          country = state.country
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

Save the 'airport_data.py' file.

As learned above there are multiple ways to divide an application into multiple files using Jupyter notebooks. In this example, a simple (non-Jupyter notebook) Python file was created. This is the pattern you would follow for a normal Python program not running in Jupyter notebooks.

1. Remove the code copied in the previous step from the 'Airline Data Exercise' notebook. Save the 'Airline Data Exercise' notebook.

1. Add a new cell at the top of the 'Airline Data Exercise' notebook. In the new cell, add the following code.

```python
from airport_data import load_states, load_airports
```

Run the code for the entire notebook using 'Restart & Run All' from the 'Kernel' menu. Ensure everything works properly. The output should display 67 states and 6510 countries.

  Hint: When setting up multiple Python files and performing imports it is a good practice to restart the kernel after changing the imported files or when adding/removing imports. Not restarting the kernel can lead to confusion about what is loaded and what is not loaded. Code which should work fails because something is not loaded as expected.

From the 'airport_data.py' file the `load_states` and `load_airports` functions were imported and used in the second cell to load the state and airport data. This is one approach to dividing a Python application into multiple files. While this is a good approach for non-Jupyter notebook Python applications, when working with Jupyter notebooks it is more common to structure an external module as a Jupyter notebook.

1. Create a new Jupyter notebook named 'Aiport Data Module'. Unlike the previous file name which was all lowercase and underscores for spaces, this notebook will use mixed case and real spaces in the file name. Why? Because more developers use mixed casing and spaces in their notebook names. So its important to understand the conventions for importing notebooks using such naming.

In the 'Airport Data Module' notebook, add the following code to the first cell.

```python
import csv

# map/lambda version
# def split_strip(value, split_value = ','):
#   return tuple(map(lambda x: x.strip(), value.split(split_value)))

# list comprehension version
def split_strip(value, split_value = ','):
  return tuple([ x.strip() for x in value.split(split_value) ])

class State:

  def __init__(self, state_data):

    state_abbr, state_name_data = state_data
    country =  'United States'

    state_name_parts = split_strip(state_name_data)

    state_name = state_name_parts[0]
    if (len(state_name_parts) == 2):
      country = state_name_parts[1]
      state_label = 'province'
    else:
      state_label = 'state'

    self.code = state_abbr
    self.name = state_name
    self.label = state_label
    self.country = country
    
def load_states(states_csv_file_name):

  states = {}

  with open(states_csv_file_name, 'r') as states_csv_file:
    states_csv_file_reader = csv.reader(states_csv_file, delimiter=',')
    for state_line_number, state_data in enumerate(states_csv_file_reader):
      if state_line_number == 0: continue
      state = State(state_data)
      states[state.code] = state  
  return states

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
          state_name = state.name
          state_label = state.label
          country = state.country
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

Save the notebook.

1. In the 'Airline Data Exercise' notebook, replace the code in the first cell:

```python
from airport_data import load_states, load_airports
```

with the following code:

```python
import sys
!{sys.executable} -m pip install import_ipynb

from Airport_Data_Module import load_states, load_airports
```

The exclamation point instructs Jupyter notebooks to executing the line of code. The `sys.executable` is the path to the Python interpreter. The `-m` option tells Python to run `pip` the Python package management tool. The `install` command directs `pip` to install the `import_ipynb` package. The `import_ipynb` package will allow Jupyter notebooks to be imported into Jupyter notebooks. Because Jupyter notebooks do not follow the same format as a standard Python module this package is needed to properly handle the importing of the notebook.

The name of the module will follow the casing of the notebook file name with spaces being replaced as underscores.

Run the code for the entire notebook using 'Restart & Run All' from the 'Kernel' menu. Ensure everything works properly.

1. Jupyter notebooks has very permissive notebook naming standards relative to the recommended naming practices of Python modules. For example, Jupyter notebooks can be named with dashes. Unfortunately, dashes are not supported in Python module names when using the `from-import` syntax. To load Jupyter notebooks with a dash in the notebook name additional steps must be taken.

Rename the 'Aiport Data Module' notebook to 'Airline Data Exercise - Aiport Data Module'.

1. In the 'Airline Data Exercise' notebook, replace the code in the first cell:

```python
import sys
!{sys.executable} -m pip install import_ipynb

from Airport_Data_Module import load_states, load_airports
```

with the following code:

```python
import sys
!{sys.executable} -m pip install import_ipynb

import import_ipynb
airport_data_module = __import__('Airline Data Exercise - Airport Data Module')

load_states = airport_data_module.load_states
load_airports = airport_data_module.load_airports
```

The `__import__` function loads a Python module using a string-based name. The name of the notebook does not have to be valid Python syntax. There is no ability to selectively import functions into name variables while doing the import itself so additional code is needed to copy the function references to move convenient function names.

Run the code for the entire notebook using 'Restart & Run All' from the 'Kernel' menu. Ensure everything works properly.
