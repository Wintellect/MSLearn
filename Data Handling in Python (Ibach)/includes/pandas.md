# pandas

Another useful Python library when managing data is [pandas]](https://pandas.pydata.org/). *pandas* is an open source  library provding high performance, easy to use data structures and data analysis tools. Pandas is licensed under the [BSD](https://www.numpy.org/license.html#license) enabling use with few restrictions.

The pandas library is odten used with NumPy. The pandas library relies on the NumPy Array for implementation of pandas and builds on the NumPy functionality.

## Importing the pandas library
Before you can use pandas you need to import the library.
```python
import pandas as pd
```
## Creating a pandas series

A *Series* in pandas is similar to a list in Python. A Series is a one dimensional array capable of holding any data type:

```python
num_series = pd.Series([1,2,3,4])
print(num_series) # outputs :
# 0    1
# 1    2
# 2    3
# 3    4
```
 You can access the values in a series with a loop:
 ```python
for value in num_series:
    print(value) # outputs :
# 1
# 2
# 3
# 4 
```

You can access a specific value by specifying the index position:
```python
print(num_series[0]) # outputs : 1
```
 Unlike Python lists, you can control the index/label of the elements in a series. 
```python
num_series = pd.Series([1,2,3,4],['One','Two','Three','Four'])
print(num_series) # outputs :
# One      1
# Two      2
# Three    3
# Four     4
print(num_series['One']) # outputs : 1
```

## Creating a pandas DataFrame
A pandas *DataFrame* is a two or more dimensional data structure. Each column and row is indexed.  

```python
data = [['SEA','Seattle'],['BOS','Boston'],['HOU','Houston']]
column_names = ['airport_code','city']
airports = pd.DataFrame(data, columns = column_names)
print(airports) # outputs : 
#   airport_code     city
# 0          SEA  Seattle
# 1          BOS   Boston
# 2          HOU  Houston
```
## Slicing a DataFrame

To slice a DataFrame you use the following syntax: 
```python
df2.loc[startrow:endrow, startcolumn:endcolumn]
```
Don't forget with pandas the indexes may not be numeric:
```python
print(airports.loc[0:1,'airport_code':'city']) # outputs
#   airport_code     city
# 0          SEA  Seattle
# 1          BOS   Boston
```

You can request a specific cell using the `loc` function:
```python
print(airports.loc[0,'city']) # outputs : Seattle 
```
You can access one or more specific rows by specifying the index range of the rows:
```python
print(airports[0:1]) # outputs : 
#      airport_code     city
# 0             SEA  Seattle
```

You can access a specific column with the column index:
```python
print(airports['airport_code'])
# outputs a Series 
# 0    SEA
# 1    BOS
# 2    HOU
```
## Reading data from a CSV file

With pandas we use the `read_csv` method to read the contents of a csv file.  
Let's look at some of the parameters of `read_csv`:
- **filepath_or_buffer**: path and name of the csv file.  
- **delimiter**: The string used to separate values.  
- **dtype**: Data type for data or columns, if omitted data type is inferred from the data. 
- **header**: The row number to use as the column names.   
- **skipfooter**: The number of lines to skip at the end of the file. 
- **skipinitialspace**: skip spaces after the delimiter

If you have not already done so in the NumPy lesson, download and examine the AirportCodeList.csv file. The file has a header row containing the names of the columns and a footer row containing the number of rows selected. You might also have noticed there are some extra spaces on some of the rows. 

Let's use `read_csv` to read the csv file into a DataFrame 
```python
airport_codes = pd.read_csv('AirportCodeList.csv',delimiter=',',header=0,skipfooter=1,skipinitialspace=True, engine='python')
print(airport_codes) # outputs : 
        Airport Code              City
# 0                HOU           Houston
# 1                ABQ      Alberquerque
# ...
# 22               GSP        Greenville
```
> You may have noticed an extra parameter: *engine*. This parameter determines which parser engine to use. The 'c' engine is faster, the 'python' engine is more feature-complete. The *skipfooter* parameter is not supported by the 'c' engine so we need to specify the 'python' engine.  

Because the file is quite large you may find it useful to print only the top or bottom rows in the DataFrame. The `head` function returns the top rows from a DataFrame. The `tail` function returns the bottom rows.
```python
flight_df.head(2) # outputs : 
#   Airport Code	        City
# 0	         HOU	Houston
# 1	         ABQ	Alberquerque
flight_df.tail(3) # outputs : 
#           Airport Code	           City
# 21	             FLL	Fort Lauderdale
# 22	             GSP	     Greenville
# 23    23 rows selected	            NaN
```
If you do not need all the columns in the file, the *usecols* parameter allows you to specify a list of columns you want returned:

```python
airport_codes = pd.read_csv('AirportCodeList.csv',usecols=['City'],delimiter=',',header=0,skipfooter=1,skipinitialspace=True, engine = 'python')
print(airport_codes.head()) # outputs :
#            City
# 0       Houston
# 1  Alberquerque
# 2     Baltimore
# 3        Denver
# 4     Las Vegas
```
## Manipulating DataFrames

pandas has a number of useful functions that operate on DataFrames.

The *sort_values* function allows you to sort the rows based on one or more columns:

```python
print(airport_codes.head()) # outputs : 
#   Airport Code          City
# 0          HOU       Houston
# 1          ABQ  Alberquerque
# 2          BWI     Baltimore
# 3          DEN        Denver
# 4          LAS     Las Vegas
sorted_rows = airport_codes.sort_values(by=['City','Airport Code'])
print(sorted_rows.head()) # outputs :
#    Airport Code          City
# 1           ABQ  Alberquerque
# 15          AUS        Austin
# 2           BWI     Baltimore
# 17          BOS        Boston
# 7           CLE     Cleveland
```
## Concatenate DataFrames
How to append rows from one dataframe to another
```python
df_all_rows = pd.concat([df_SN7577i_a, df_SN7577i_b])
df_all_rows
```

Get rid of duplicates

## Merge DataFrames
To do a JOIN across two data frames
```python
df_cd = pd.merge(df_SN7577i_c, df_SN7577i_d, how='inner', left_on = 'Id', right_on = 'Id')
```

## Are there any pandas math functions
The NumPy library also supports mathematical operations across the array. When you apply an operation to the array, that operation is completed against each element in the array or each element in the slice: 
```python
lets_do_math = np.array([[1, 2], [3, 4], [5, 6]])
print(lets_do_math + 1) 
# outputs the entire array 
# with 1 added to each element: 
# [[2 3]
# [4 5]
# [6 7]]
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
Now we can start analyzing information on flight delays. The flight_delays.csv file contains information on past flights. We need to use this data to determine:
- the mean of the flight arrival delays. 
- how many flights arrived more than 10 minutes late.
- the longest delay for any flight.
- flight information for the flight with the longest delay.

Open the file and examine the contents. Each row contains data for one flight. The ARR_DELAY column tells us in minutes how late a flight arrived:
- A negative number indicates the flight landed early.  
- A zero indicates the flight landed on time. 
- A positive number indicated the flight was late. 

Let's start by importing the file and reading in the column headers. The file contains 99 rows. We can print out the length of the array to make sure all the rows were read successfully. We can also print the column names to make sure they are read in successfully:

```python
flight_data = genfromtxt('flight_delays.csv',delimiter=',',dtype=None,names=True,encoding=None)
print (flight_data.dtype.names) # outputs
# ('FL_DATE', 'OP_UNIQUE_CARRIER', 'TAIL_NUM', 'OP_CARRIER_FL_NUM', 'ORIGIN', 'DEST', 'CRS_DEP_TIME', 'DEP_TIME', 'DEP_DELAY', 'CRS_ARR_TIME', 'ARR_TIME', 'ARR_DELAY', 'CRS_ELAPSED_TIME', 'ACTUAL_ELAPSED_TIME', 'AIR_TIME', 'DISTANCE')
```
Now we can use the mean() function to determine the mean of the ARR_DELAY column for all flights: 
```python
print(flight_data['ARR_DELAY'].mean()) # outputs: 2.303030303030303
```

Getting the number of flights that were delayed more than 10 minutes will require using a comprehension that iterates across the array and filters rows based on the value in the ARR_DELAY column. We will put the results into a new array called delayed_flights. The number of rows in the delayed_flights array is the number of flights delayed more than 10 minutes.
```python
delayed_flights = [flight for flight in flight_data if flight['ARR_DELAY'] > 10]
print(len(delayed_flights)) # outputs: 15
```
To figure out the longest delay we need to retrieve the maximum value in the ARR_DELAY column:
```python
print(flight_data['ARR_DELAY'].max()) # outputs : 232
```

To get the flight information for the flight with the longest delay we need to use a comprehension that filters out the row with the maximum value for ARR_DELAY:

```python
biggest_delay = [flight for flight in flight_data if flight['ARR_DELAY'] == flight_data['ARR_DELAY'].max()]
print(biggest_delay) # outputs : 
# [('2018-10-01', 'WN', 'N435WN', 5757, 'ABQ', 'MCI', 1720, 2119, 239, 2005, 2357, 232, 105, 98, 87, 718)] #
```
Congratulations, you are starting to get a better understanding of how many flights are delayed and for how long. Let's continue analyzing flight data in our next lessons using pandas and matplotlib. 
