# Manipulating pandas DataFrames

In the previous lesson you learned how to create a DataFrame and populate it with data. pandas has a number of functions you can use operate on the data.

## Sorting 
The `sort_values` function allows you to sort the rows in a DataFrame based on one or more columns:

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
Sometimes the data we need to read is stored in multiple data files and we need to merge all the data into a single dataframe. 

The `concat` function allows you to append the rows from one DataFrame onto a second DataFrame:

```python
# Create a DataFrame with the first three airports
column_names = ['airport_code','city']
data = [['SEA','Seattle'],['BOS','Boston'],['HOU','Houston']]
airport_part1 = pd.DataFrame(data, columns = column_names)

# Create a DataFrame with the last three airports
data = [['DTW','Detroit'],['LGA','New York'],['DUL','Washington']]
airport_part2 = pd.DataFrame(data, columns = column_names)

# Use concat to combine the two DataFrames
all_airports = pd.concat([airport_part1,airport_part2], ignore_index=True)
print(all_airports) # outputs : 
#   airport_code        city
# 0          SEA     Seattle
# 1          BOS      Boston
# 2          HOU     Houston
# 3          DTW     Detroit
# 4          LGA    New York
# 5          DUL  Washington
```
> When you concatenate two DataFrames using generated indexes, you get duplicate index numbers. Each DataFrame has the first row with index 0, the second row with index 1, and so on. The *ignore_index* parameter tells the `concat` function to ignore the existing indexes and create a new one.  

## Removing duplicates

Sometimes the data we work with contains duplicate records. The `drop_duplicates` function will remove the duplicate rows: 

```python
column_names = ['airport_code','city']
data = [['DTW','Detroit'],['LGA','New York'],['DTW','Detroit']]
airports = pd.DataFrame(data, columns = column_names)
print(airports) # outputs : 
#   airport_code      city
# 0          DTW   Detroit
# 1          LGA  New York
# 2          DTW   Detroit

airports= airports.drop_duplicates()
print(airports) # outputs : 
#   airport_code      city
# 0          DTW   Detroit
# 1          LGA  New York
```

## Merge DataFrames
There will be times the columns of data you need are divided across two DataFrames. The `merge` function allows you to join columns spread records in two DataFrames.

Imagine you have a list of airport codes and their cities in one DataFrame and a list of scheduled flights in another DataFrame. The flight information includes the airport code but you need to look up the city for each airport code. We can use `merge` to do the lookup.

The following parameters are required:
- *how* specifies the type of join to perform. The most commond join type is an  *inner* join. For an *inner* join, we expect to find one matching row for each lookup
- *left_on* specifies the column name in the first DataFrame listed (the one on the left when looking at the code) which has a corresponding value in the second DataFrame. 
- *right_on* specifies the column name in the second DataFrame listed (the one on the right when looking at the code) which will contain a value to match the value contained in the *left_on* column.

It is probably easier to understand with  an example. Let's start with a DataFrame that contains a list of the airport codes and cities:
```python
column_names = ['airport_code','city']
data = [['DTW','Detroit'],['LGA','New York'],['DUL','Washington']]
airport_codes = pd.DataFrame(data, columns = column_names)
print(airport_codes) # outputs : 
#   airport_code        city
# 0          DTW     Detroit
# 1          LGA    New York
# 2          DUL  Washington
```

Next we have a second DataFrame that contains flight information:
```python
column_names = ['departure_date','dest_airport','dep_time','flight_num']
data = [['12/31/2019','DTW','08:15',499],['12/31/2019','LGA','09:35',748] ,['12/31/2019','LGA','13:15',749]]
flights = pd.DataFrame(data, columns = column_names)
print(flights) # outputs :
#   departure_date dest_airport dep_time  flight_num
# 0     12/31/2019          DTW    08:15         499
# 1     12/31/2019          LGA    09:35         748
# 2     12/31/2019          LGA    13:15         749
```

What if we need the destination city for each flight? We have the destination airport code, but we need to look up the corresponding city in the airport_codes DataFrame. the value in *dest_airport* of the *flights* DataFrame should match an *airport_code* in the *airport_codes* DataFrame: 

```python
all_data = pd.merge(flights, airport_codes,how = 'inner', left_on = 'dest_airport', right_on = 'airport_code' )
print(all_data) # outputs : 
#   departure_date dest_airport dep_time  flight_num airport_code      city
# 0     12/31/2019          DTW    08:15         499          DTW   Detroit
# 1     12/31/2019          LGA    09:35         748          LGA  New York
# 2     12/31/2019          LGA    13:15         749          LGA  New York
```

We now have the corresponding city for each flight. 
# Deleting columns
You can delete a column from a DataFrame using the `del` operator.

You might have noticed when we merged the *flight* and *airport_codes* DataFrames that we copied over the *city* and the *airport_code*. We don't need  *airport_code* since it is a duplicate of *dest_city*. So we can delete that extra column:
```python
del all_data['airport_code']
print(all_data) # outputs : 
#   departure_date dest_airport dep_time  flight_num      city
# 0     12/31/2019          DTW    08:15         499   Detroit
# 1     12/31/2019          LGA    09:35         748  New York
# 2     12/31/2019          LGA    13:15         749  New York
```

## pandas math operations
Similar to NumPy, the pandas library  supports mathematical operations across the DataFrame. When you apply an operation to the DataFrame, that operation is completed against each element in the DataFrame or each element in the slice: 
```python
# Create a DataFrame containing the numbers 1 through 6 
column_names = ['first_column','second_column']
data = [[1,2],[3,4],[5,6]]
lets_do_math = pd.DataFrame(data, columns = column_names)

print(lets_do_math + 1) 
# outputs the entire array 
# with 1 added to each element: 
#    first_column  second_column
# 0             2              3
# 1             4              5
# 2             6              7

print(lets_do_math < 3)
# outputs the result of the evaluation 
# is element < 3 for each element in the array:
#    first_column  second_column
# 0          True           True
# 1         False          False
# 2         False          False
```
pandas also supports operations such as calculating the sum, min, max, or mean of all the values in the DataFrame columns:
```python
print(lets_do_math.sum()) 
# outputs sum of each column :
# first_column      9
# second_column    12

print(lets_do_math.mean()) 
# outputs mean of values in each column :
# first_column     3.0
# second_column    4.0

print(lets_do_math['second_column'].max())
# outputs highest value in specified column : 6
```

## Analyzing flight information
Now we are ready to analyze our data. We need to 
- Load a full set of flight data.
- Clean up any duplicate rows and unncessary columns. 
- retrieve the mean and maximum arrival delay time. 

It turns out that the *flight_data_part1.csv* file you loaded in the previous lesson does not contain all the flight information. There is a second csv file, *flight_data_part2.csv* you need to load. 

Load the two csv files into DataFrames. Check the number of rows in each DataFrame. You should have 300,000 rows in *flight_data_part1* and 320,000 rows in *flight_data_part2*. Combine them together into one DataFrame. 

```python
import pandas as pd

flights_part1 = pd.read_csv('flight_data_part1.csv',delimiter=',',skipinitialspace=True)

flights_part2 = pd.read_csv('flight_data_part2.csv',delimiter=',',skipinitialspace=True)

print(len(flights_part1)) # outputs : 300000
print(len(flights_part2)) # outputs : 320000
```
Double check the new DataFrame has all the rows (620,000). Make sure the index numbers were re-assigned when the new DataFrame was created. If index numbers are assigned correctly, the last row in the DataFrame should have an index of 619999:

```python
all_flights = pd.concat([flights_part1, flights_part2], ignore_index=True)

print(len(all_flights)) # outputs : 620000
print(all_flights.tail(1)) # outputs : 
#            FL_DATE OP_UNIQUE_CARRIER TAIL_NUM  OP_CARRIER_FL_NUM ORIGIN DEST  \
# 619999  2018-10-31                YV   N902FJ               5789    ABQ  PHX   

#         CRS_DEP_TIME  DEP_TIME  DEP_DELAY  CRS_ARR_TIME  ARR_TIME  ARR_DELAY  \
# 619999          1232    1228.0       -4.0          1258    1251.0       -7.0   

#         CRS_ELAPSED_TIME  ACTUAL_ELAPSED_TIME  AIR_TIME  DISTANCE  
# 619999                86                 83.0      63.0       328  
```

The two files contain some of the same data. Remove all the duplicate rows from the DataFrame. Check to make sure you have 616101 rows left after removing all the duplicates:

```python
all_flights = all_flights.drop_duplicates()
print(len(all_flights)) # outputs: 616101
```

Delete the *TAIL_NUM* column since it will not be needed for our data analysis:

```python
del all_flights['TAIL_NUM']
```

Now we can use the mean() function to determine the mean of the ARR_DELAY column for all flights: 
```python
print(all_flights.ARR_DELAY.mean()) # outputs : 2.824561633466266
print(all_flights.ARR_DELAY.max()) # outputs : 2153.0
```

BONUS: Can you figure out how many flights arrived more than 10 minutes late? HINT: You don't need a comprehension, look up *filters* on pandas DataFrames.

```
late_flights = all_flights[all_flights['ARR_DELAY']>=10]
print(len(late_flights)) # outputs : 126988
```
Congratulations you are moving data around like a professional! Now let's finish up with a look at how we  visualize our data with *matplotlib*