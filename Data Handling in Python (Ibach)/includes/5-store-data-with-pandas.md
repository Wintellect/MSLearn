# Load data with Pandas

NumPy is great for loading data from CSV files and performing fast mathematical calculations on the data. But when it comes to cleaning, analyzing, and manipulating data, nothing beats [Pandas](https://pandas.pydata.org/). Pandas, short for *Python Data Analysis Library*, is the library that people who work with data for a living turn to for gathering insights from the data or preparing it for machine learning. It uses NumPy for speed and efficiency, and it goes far beyond NumPy in terms of the tools it offers for working with data. Like NumPy, Pandas is licensed under the [BSD license](https://www.numpy.org/license.html#license), enabling wide-ranging use with few restrictions.

The key data structure in Pandas is the [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html), which you can think of as a two-dimensional table of rows and columns with labeled axes. DataFrame includes methods for loading data from CSV files, filtering and sorting data, checking for and replacing missing values, removing rows and columns with missing values, joining DataFrames, rendering data on-screen, and more. DataFrame contains more than 200 methods. A simple call to [`DataFrame.head()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head) in a Jupyter notebook gives you a look at the structure and content of the data:

![Viewing a DataFrame](media/dataframe.png)

Data handling is simpler when you have Pandas to lend a hand. In this lesson, you will learn the basics of Pandas and use it to load and analyze a large dataset.

## Importing the pandas library

Before you can use pandas you need to import the library:
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

Unlike Python lists, you can control the index/label of the elements in a series: 

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

A pandas *DataFrame* is a two or more dimensional data structure. Each column and row is indexed:  

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

With pandas you use the `read_csv` function to read the contents of a csv file. Let's look at some of the parameters of `read_csv`:

- **filepath_or_buffer**: path and name of the csv file  
- **delimiter**: The string used to separate values  
- **dtype**: Data type for data or columns, if omitted, data type is inferred from the data 
- **header**: The row number to use for reading the column names   
- **skipfooter**: The number of lines to skip at the end of the file 
- **skipinitialspace**: skip spaces after the delimiter

## SUSAN ADD LNK TO AIRPORTCODELIST.CSV

If you have not already done so in the NumPy lesson, download and examine the AirportCodeList.csv file. The file has a header row containing the names of the columns and a footer row containing the number of rows selected. You might also have noticed there are some extra spaces on some of the rows. 

Let's use `read_csv` to read the csv file into a DataFrame 

```python
airport_codes = pd.read_csv('AirportCodeList.csv' ,delimiter=',', header=0, skipfooter=1, skipinitialspace=True, engine='python')
print(airport_codes) # outputs : 
        Airport Code              City
# 0                HOU           Houston
# 1                ABQ      Alberquerque
# ...
# 22               GSP        Greenville
```

> You may have noticed an extra parameter: *engine*. This parameter determines which parser engine to use. The 'c' engine is faster, the 'python' engine is more feature-complete. The *skipfooter* parameter is not supported by the 'c' engine so you need to specify the 'python' engine when you use *skipfooter*.  

Because the file is quite large you may find it useful to print only the top or bottom rows in the DataFrame. The `head` function returns the top rows from a DataFrame. The `tail` function returns the bottom rows:

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
airport_codes = pd.read_csv('AirportCodeList.csv', usecols=['City'], delimiter=',', header=0, skipfooter=1, skipinitialspace=True, engine = 'python')
print(airport_codes.head()) # outputs :
#            City
# 0       Houston
# 1  Alberquerque
# 2     Baltimore
# 3        Denver
# 4     Las Vegas
```

## Reading flight information

In the previous lesson you improted a csv file of flight information using NumPy. In this exercise you will import a much bigger csv file into a pandas DataFrame.

## SUSAN ADD LNK TO FLGHT_DATA_PART1.CSV

Download the file flight_data_part1.csv. Open the file and examine the contents. This file has 300,000 rows and will help us get a more complete picture of the impact of flight delays for our airline. The first row of the file contains the column headers. There are no footer rows in the file.

Read the datafile into a DataFrame called *flights_part1*. Read the column names from the header row. Make sure any spaces after commas are not treated as part of the data:

```python
import pandas as pd
flights_part1 = pd.read_csv('flight_data_part1.csv',delimiter=',',skipinitialspace=True)
```

Use the `len` function to make sure you have successfully imported 300,000 rows into the DataFrame: 

```python
print(len(flights)) # outputs: 300000
```

print the last 5 rows of the DataFrame just to make sure the data in the columns looks correct (column values are not shifted, no extra spaces in column values, etc...): 

```python
print(flights.tail(5)) # outputs : 
#            FL_DATE OP_UNIQUE_CARRIER TAIL_NUM  OP_CARRIER_FL_NUM ORIGIN DEST  \
# 299995  2018-10-15                OH   N582NN               5248    CLT  TLH   
# 299996  2018-10-15                OH   N582NN               5248    TLH  CLT   
# 299997  2018-10-15                OH   N706PS               5250    CLT  CRW   
# 299998  2018-10-15                OH   N706PS               5250    CRW  CLT   
# 299999  2018-10-15                OH   N537EA               5252    ORD  DAY   

#         CRS_DEP_TIME  DEP_TIME  DEP_DELAY  CRS_ARR_TIME  ARR_TIME  ARR_DELAY  \
# 299995          1610    1607.0       -3.0          1737    1730.0       -7.0   
# 299996          1808    1804.0       -4.0          1940    1927.0      -13.0   
# 299997           750     745.0       -5.0           901     859.0       -2.0   
# 299998           931     926.0       -5.0          1052    1039.0      -13.0   
# 299999          1820    1817.0       -3.0          2026    2032.0        6.0   

#         CRS_ELAPSED_TIME  ACTUAL_ELAPSED_TIME  AIR_TIME  DISTANCE  
# 299995                87                 83.0      61.0       386  
# 299996                92                 83.0      65.0       386  
# 299997                71                 74.0      41.0       221  
# 299998                81                 73.0      44.0       221  
# 299999                66                 75.0      38.0       240  
```

Congratulations, you now have a large amount of flight data loaded and ready to analyze. In the next lesson you will learn how you can use pandas to work with data in DataFrames.