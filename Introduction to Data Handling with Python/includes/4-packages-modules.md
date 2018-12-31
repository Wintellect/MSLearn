# Using packages and modules

Building Python applications and build Python Jupyter Notebooks often requires using third-party code libaries or diving the application/notebook into multiple files. Packages and package managers provide the ability to easily employ third-party libaries within your projects. Python has two popular package managers PIP and Conda. PIP is distributed with Python and Conda is distributed with the Anaconda distribution of Python. In this module, PIP will be used. PIP downloads packages from the Python Package Index [https://pypi.org/](https://pypi.org/). PIP can be used from the command line or executed within a Jupyter Notebook. Most Jupyter Notebooks installations some with a number of packages pre-installed such as NumPy, Pands and Matplotlib. For other packages which are not standard, they will need to be installed.

Within packages and within projects code can be organized with modules. In Python, each file is a module and each module is a file. When working with a larger Python program or Jupyter Notebook it can be helpful to divide the application source code into multiple files. Each of those files would be a module.

## Packages Exercises

1. Create a new Jupyter notebook named 'Package and Module Exercises' in Azure Notebooks.

1. In the first cell, add the following code.

```python
import numpy
```

Run the cell, if the package is installed there will be no output. If the package is not installed, there will be an error. Most Jupyter notebook installations will have the `numpy` package installed.

1. Replace the code in the first cell with the following code:

```python
import import_ipynb
```

Run the cell, most likely the package is not installed and there will be an error similar to this:

```text
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-2-2044c9f20ccd> in <module>()
----> 1 import import_ipynb

ModuleNotFoundError: No module named 'import_ipynb'
```

1. To install the package from within a Jupyter Notebook, add the following code to the top of the cell.

```python
import sys
!{sys.executable} -m pip install import_ipynb

import import_ipynb
```

The exclamation mark instructs Jupyter notebooks to execute the line of code as a terminal command. The `sys.executable` is the path to the Python interpreter. The `-m` option tells Python to run `pip` the Python package management tool. The `install` command directs `pip` to install the `import_ipynb` package. The `import_ipynb` package will allow Jupyter notebooks to be imported into Jupyter notebooks. Because Jupyter notebooks do not follow the same format as a standard Python module this package is needed to properly handle the importing of the notebook.

1. To install a package from a terminal window, open the terminal for Jupyter Notebooks. Run the following command from the terminal.

```bash
pip install import_ipynb
```

The `install` command for `pip` program will install the specified package. The output should look similar to this if the package is not installed:

Collecting import_ipynb
twisted 18.7.0 requires PyHamcrest>=1.9.0, which is not installed.
Installing collected packages: import-ipynb
Successfully installed import-ipynb-0.1.3

1. To uninstall a package from a terminal window, open the terminal for Jupyter Notebooks. Run the following command from the terminal.

```bash
pip uninstall import_ipynb
```

The `uninstall` command for `pip` program will install the specified package. The output should look similar to this if the package is not installed:

```text
Uninstalling import-ipynb-0.1.3:
  Would remove:
    /home/ec2-user/anaconda3/lib/python3.7/site-packages/import_ipynb-0.1.3.dist-info/*
    /home/ec2-user/anaconda3/lib/python3.7/site-packages/import_ipynb.py
Proceed (y/n)? y
  Successfully uninstalled import-ipynb-0.1.3
```

Installing and uninstalling a package from the terminal affects the packages used by the Jupyter notebooks as well.

1. Commonly it is desired to save a list of all of the installed packages so that if the code is executed on different machine or a different environment the needed packages can be easily installed. To create a list of the packages a file named `requirements.txt` is created. Create a `requirements.txt` file using the following command:

```bash
pip freeze > requirements.txt
```

Observe the contents of the file. All of the installed packages and their versions will be listed.

1. DO NOT RUN THIS COMMAND. To install of the packages for a `requirements.txt` file in a new environment run the following terminal command.

```bash
pip install -r requirements.txt
```

There is no need to run this command for this exercise. Just hold on to it for use in your future projects.

## Module Exercies

1. If not already open, open the same notebook you created for the packages exercise.


## Airline Data Exercise: Dividing an Notebook into Modules and using a Package

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this fourth exercise within the module, the airport and state dictionary loading code will be moved to a new file and the `import_ipynb` package will be used.

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

class Airport:

  def __init__(self, airport, states):

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

    self.code = code
    self.name = name
    self.city = city
    self.state_name = state_name
    self.state_label = state_label
    self.country = country
    
def load_airports(airport_csv_file_name, states):

  airports = {}

  with open(airport_csv_file_name, 'r') as airports_csv_file:
      airports_csv_file_reader = csv.reader(airports_csv_file, delimiter=',')
      for airport_line_number, airport_data in enumerate(airports_csv_file_reader):
            if airport_line_number == 0: continue
            airport = Airport(airport_data, states)
            airports[airport.code] = airport
      
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

class Airport:

  def __init__(self, airport, states):

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

    self.code = code
    self.name = name
    self.city = city
    self.state_name = state_name
    self.state_label = state_label
    self.country = country
    
def load_airports(airport_csv_file_name, states):

  airports = {}

  with open(airport_csv_file_name, 'r') as airports_csv_file:
      airports_csv_file_reader = csv.reader(airports_csv_file, delimiter=',')
      for airport_line_number, airport_data in enumerate(airports_csv_file_reader):
            if airport_line_number == 0: continue
            airport = Airport(airport_data, states)
            airports[airport.code] = airport
      
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

import import_ipynb
from Airport_Data_Module import load_states, load_airports
```

The name of the module will follow the casing of the notebook file name with spaces being replaced as underscores.

Run the code for the entire notebook using 'Restart & Run All' from the 'Kernel' menu. Ensure everything works properly.

1. Jupyter notebooks has very permissive notebook naming standards relative to the recommended naming practices of Python modules. For example, Jupyter notebooks can be named with dashes. Unfortunately, dashes are not supported in Python module names when using the `from-import` syntax. To load Jupyter notebooks with a dash in the notebook name additional steps must be taken.

Rename the 'Aiport Data Module' notebook to 'Airline Data Exercise - Aiport Data Module'.

1. In the 'Airline Data Exercise' notebook, replace the code in the first cell:

```python
import sys
!{sys.executable} -m pip install import_ipynb

import import_ipynb
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
