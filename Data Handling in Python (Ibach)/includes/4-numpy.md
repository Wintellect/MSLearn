# NumPy

One of the most compelling reasons to use Python is the number of powerful libraries available. [NumPy](https://www.numpy.org/) is one of those libraries — one that is purpose-built for scientific computing. It implements a rich multidimensional array object that is more performant than Python lists and requires substantially less memory — sometimes orders of magnitude less, especially when dealing with large arrays. NumPy arrays, unlike Python lists, are easily reshaped. A simple function call, for example, converts a 5x4 array into a 2x10 array. NumPy also includes functions for performing fast mathematical operations on arrays, computing [Fourier transforms](https://en.wikipedia.org/wiki/Fourier_transform), and performing basic statistical operations. It even has support support for reading CSV files. For an overview of NumPy arrays and why they are ubiquitous in Python applications that handle data, see [A hitchhiker guide to python NumPy Arrays](https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121). NumPy is licensed under the [BSD license](https://www.numpy.org/license.html#license), enabling it to be used with few restrictions.

In this lesson, you will tk.

## Importing the NumPy library

Before you can use NumPy you need to import the library:

```python
import numpy as np
```

## Creating a NumPy array

You create a NumPy array using the `array` function. The following code creates an array containing airport codes and cities:  

```python
airports = np.array(['SEA', 'Seattle', 'HOU', 'Houston', 'BOS', 'Boston'])
print(airports) # outputs : ['SEA' 'Seattle' 'HOU' 'Houston' 'BOS' 'Boston']
```

The `shape` function returns the dimensions of the array. The array created above is six rows and one column, making it a 6x1 array: 

```python
print(airports.shape) # outputs : (6,)
```

One of the useful NumPy functions is the ability to change the dimensions of an array using `reshape`. You can reshape your airports array to make it three rows and two columns:  

```python
airports = airports.reshape(3,2)
print(airports) # outputs : 
                # [['SEA' 'Seattle']
                # ['HOU' 'Houston']
                # ['BOS' 'Boston']]
```
## Accessing content of a NumPy array

Just like Python lists, NumPy arrays allow you to use loops to iterate through all their values:  

```python
for value in airports:
    print(value) # outputs :
                 # ['SEA' 'Seattle']
                 # ['HOU' 'Houston']
                 # ['BOS' 'Boston']
```

Just like Python lists, NumPy arrays can be sliced:

```python
print(airports[2,0]) # outputs a specific cell: BOS
print(airports[2])   # outputs a specific row : ['BOS' 'Boston']
print(airports[:,1]) # outputs a specific column : ['Seattle' 'Houston' 'Boston']
```

## Reading data from a CSV file

NumPy contains a rich function [genfromtxt](https://www.numpy.org/devdocs/user/basics.io.genfromtxt.html) for reading CSV files into NumPy arrays.

Let's look at some of the parameters of `genfromtxt`:
- **fname**: name of the csv file
- **delimiter**: The string used to separate values  
- **dtype**: Type of the resulting array. Setting this value to *None* will determine the type from the data itself but is slower than setting the dtype explicitly
- **skip_header**: The number of lines to skip at the beginning of the file  
- **skip_footer**: The number of lines to skip at the end of the file 

### SUSAN TO ADD LINK TO ARIPORTCODELIST.CSV FILE

Download and examine the AirportCodeList.csv file. The file has a header row containing the names of the columns and a footer row containing the number of rows selected. You might also have noticed there are some extra spaces on some of the rows. 

Use `genfromtxt` to read the file contents:  

```python
airport_codes = genfromtxt('AirportCodeList.csv', delimiter=',',dtype=None, encoding=None, skip_header=1, skip_footer=1)
print(airport_codes) # outputs : 
                     # [['HOU' 'Houston']
                     # ['ABQ' 'Alberquerque']
                     # ['BWI    ' ' Baltimore']
                     # ...
                     # ['GSP' ' Greenville']]
```

> You may have noticed an additional parameter: *encoding*. Encoding is used to decode the inputfile.  When you use dtype=*None* to auto-detect types, NumPy cannot tell which fields are bytes and fields are strings. By specifying encoding = *None* you are telling NumPy to treat them as strings. If you have bytes you must specify the dtype explicity.   

### Stripping excess whitespace

You have successfully read all the rows but you can see the extra spaces in the input file are affecting our data. Add the *autostrip* parameter and set it to *True* to strip the excess white space:

```python
airport_codes = genfromtxt('AirportCodeList.csv', delimiter=',',autostrip=True, dtype=None, encoding=None, skip_header=1, skip_footer=1)
print(airport_codes) # outputs : 
                     # [['HOU' 'Houston']
                     # ['ABQ' 'Alberquerque']
                     # ['BWI' 'Baltimore']
                     # ...
                     # ['GSP' 'Greenville']]
```

### Importing column names

As files get bigger, it can be difficult to keep track of which column is in which position. It might be easier to name to the columns. You do this with the *names* parameter. You can either assign the column names manually, or if they are in the first row of the file, you can read them from the header row by adding the *names* parameter and setting it to *True*:

```python
airport_codes = genfromtxt('AirportCodeList.csv', delimiter=',',autostrip=True, dtype=None, encoding=None, names=True, skip_footer=1)
print (airport_codes.dtype.names) # outputs column names : ('Airport_Code', 'City')
print(airport_codes['City']) # outputs : 
# ['Houston' 'Alberquerque' ... 'Greenville']
```

## NumPy math functions

The NumPy library also supports mathematical operations across the array. When you apply an operation to the array, that operation is completed against each element in the array or each element in the slice: 

```python
lets_do_math = np.array([[1, 2], [3, 4], [5, 6]])
print(lets_do_math + 1) 
# outputs the entire array 
# with 1 added to each element: 
# [[2 3]
#  [4 5]
#  [6 7]]

print(lets_do_math < 3)
# outputs the result of the evaluation 
# is element < 3 for each element in the array:
# [[ True  True]
#  [False False]
#  [False False]]

print(lets_do_math[2] * 2) 
# outputs the third row of the array
# with each element multiplied by 2
# [10 12]
```
NumPy arrays also support operations such as calculating the sum, min, max, or mean of all the values in the array or slice:
```python
print(lets_do_math.sum()) # outputs sum of entire array : 21
print(lets_do_math.min()) # outputs lowest value in entire array : 1
print(lets_do_math[2].max()) # outputs highest value in 3rd row : 6
print(lets_do_math[:,0].mean()) # outputs mean of values in first column : 3
```

## Analyzing flight information

## SUSAN ADD LINK TO FLGHT_DELAYS.CSV

Now you can start analyzing information on flight delays. The flight_delays.csv file contains information on past flights. You need to use this data to determine:

- The mean of the flight arrival delays 
- How many flights arrived more than 10 minutes late
- The longest delay for any flight
- Flight information for the flight with the longest delay

Open the file and examine the contents. Each row contains data for one flight. The ARR_DELAY column tells us in minutes how late a flight arrived:

- A negative number indicates the flight landed early 
- A zero indicates the flight landed on time
- A positive number indicated the flight was late

Let's start by importing the file and reading in the column headers. The file contains 99 rows. You can print out the length of the array to make sure all the rows were read successfully. You can also print the column names to make sure they are read in successfully:

```python
flight_data = genfromtxt('flight_delays.csv', delimiter=',', dtype=None, names=True, encoding=None)
print (flight_data.dtype.names) # outputs
# ('FL_DATE', 'OP_UNIQUE_CARRIER', 'TAIL_NUM', 'OP_CARRIER_FL_NUM', 'ORIGIN', 'DEST', 'CRS_DEP_TIME', 'DEP_TIME', 'DEP_DELAY', 'CRS_ARR_TIME', 'ARR_TIME', 'ARR_DELAY', 'CRS_ELAPSED_TIME', 'ACTUAL_ELAPSED_TIME', 'AIR_TIME', 'DISTANCE')
```
Now you can use the mean() function to determine the mean of the ARR_DELAY column for all flights: 

```python
print(flight_data['ARR_DELAY'].mean()) # outputs: 2.303030303030303
```

Getting the number of flights that were delayed more than 10 minutes will require using a comprehension that iterates across the array and filters rows based on the value in the ARR_DELAY column. You will put the results into a new array called delayed_flights. The number of rows in the delayed_flights array is the number of flights delayed more than 10 minutes:

```python
delayed_flights = [flight for flight in flight_data if flight['ARR_DELAY'] > 10]
print(len(delayed_flights)) # outputs: 15
```

To figure out the longest delay you need to retrieve the maximum value in the ARR_DELAY column:

```python
print(flight_data['ARR_DELAY'].max()) # outputs : 232
```

To get the flight information for the flight with the longest delay you need to use a comprehension that filters out the row with the maximum value for ARR_DELAY:

```python
biggest_delay = [flight for flight in flight_data if flight['ARR_DELAY'] == flight_data['ARR_DELAY'].max()]
print(biggest_delay) # outputs : 
# [('2018-10-01', 'WN', 'N435WN', 5757, 'ABQ', 'MCI', 1720, 2119, 239, 2005, 2357, 232, 105, 98, 87, 718)] #
```
Congratulations, you are starting to get a better understanding of how many flights are delayed and for how long. Let's continue analyzing flight data in our next lessons using pandas and matplotlib. 
