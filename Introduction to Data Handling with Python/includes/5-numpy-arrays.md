# Using numpy arrays

Python data structures such as lists and dictionaries do perform well in terms of raw performance. Because of Python's approach to memory management structures such as lists and dictionaries are easy to work with but when those structures are used with CPU intensive code their slowness becomes very evident. Fortunately, many packages written in C and C++ have been written for Python which allow Python's easy to use syntax while storing and manipulating the date in much better performing, lower level data structures. On such library is NumPy. NumPy is used for processing lots of numeric data quickly.

## Creating an Array Exercise

1. Create a new Jupyter notebook named 'NumPy Array Exercises' in Azure Notebooks.

1. In the first cell, add the following code, and run the cell.

```python
import numpy as np
```

The `as` statement enable the thing being imported to be aliased to another name. Generally, the `numpy` module is imported with an alias of `np`.

1. Add a new cell, add the following code, and run the cell.

```python
data = [ 1, 2, 3, 4, 5 ]

nums = np.array(data)

print(nums)
```

1. Add a new cell, add the following code, and run the cell.

```python
print(nums[2:4])
```

1. Add a new cell, add the following code, and run the cell.

```python
double_nums = nums * 2

print(double_nums)
```

1. Add a new cell, add the following code, and run the cell.

```python
print(np.arange(1, 10))
```

1. Add a new cell, add the following code, and run the cell.

```python
print(np.linspace(1, 10, 100))
```

1. Add a new cell, add the following code, and run the cell.

```python
nums = np.array(data, dtype=float)

print(nums)
```

## Structured Arrays Exercise

1. If not already open, open the same notebook you created for the creating an array exercise.


## Extracting Unique Values Exercise

1. If not already open, open the same notebook you created for the structure arrays exercise.


## Airline Data Exercise: Creating a Numpy Array of Ontime Flight Data

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this fifth exercise within the module, the ontime flight data will be combined with the airport and state data to create a numpy array.

1. Open the Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks. You may want to make a duplicate copy of this notebook before attempting this exercise.

1. Add a new cell at the bottom of the notebook, and add the following code.

```python
ontime_rows = []

with open('./ontime_oct2018.csv') as ontime_csv_data:
  csv_reader = csv.DictReader(ontime_csv_data)

  for i, ontime_row in enumerate(csv_reader):
    if i == 0: continue

    try:
      dep_delay = float(ontime_row['DEP_DELAY'])
      if dep_delay < 0: dep_delay = 0
      ontime_rows.append( (ontime_row['ORIGIN'], dep_delay) )
    except:
      continue

print(len(ontime_rows))
```

The 'ontime_oct2018.csv' file contains all of the flights for major domestic US airlines for the month of October 2018. The contents of the CSV file will be read into a dictionary using Python's built-in `csv` module. For each flight entry, the departure delay in minutes along with the origin will be captured. If the departure delay is less than 0 (indicating it took off early) the delay will captured as 0. If the delay is a non-numeric value the flight will be dropped. The result of the code is a Python list of the origin airport and departure delay of all flights.

Run the code for the entire notebook using 'Restart & Run All' from the 'Kernel' menu. Ensure everything works properly.

The length of the `ontime_rows` list should be 611831.

1. With the data loaded, a NumPy array needs to be created to allow for efficient analysis of the data. Add a new cell and add the following code to the cell.

```python
ontime = np.array(ontime_rows, dtype=[('airport_code', 'S3'),('dep_delay', 'f4')])

print(len(ontime))
```

A new NumPy array will be created with the list data. Each array element will have two columns: one for the airport code and one for the departure delay in minutes. The aiport code will a string of length 3 as defined in  the `dtype`. The departure delay will be a floating point value (a number with a decimal).

Run the cell, and ensure length of the `ontime` NumPy array is 611831.

1. Add a new cell, and add the following code to the cell.

```python
airport_codes = np.unique([ airport_code.decode('UTF-8') for airport_code in ontime['airport_code'] ])

print(len(airport_codes))
```

The `np.unique` function returns an array of unique value from another array. The other array will be a list comprehension of the ontime data's airport codes. The `airport_code` needs to be decoded to UTF-8 because the NumPy array does not store the string as a UTF-8 encoded string inside of the array.

Run the cell, and ensure length of the `ontime` NumPy array is 345.



