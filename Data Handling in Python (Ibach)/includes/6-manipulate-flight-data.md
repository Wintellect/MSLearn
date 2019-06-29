# Title

TODO: Add introduction.

## Load data from CSV files

TODO: Add intro.

1. Begin by returning to [Azure Notebooks](https://notebooks.azure.com) and creating a new notebook named "Flights" in the "Data Handling in Python" project that you created earlier. Select Python 3.6 as the language.

1. Run the following statements in the notebook's first cell to import a pair of large CSV files from Azure blob storage:

	```bash
	!curl https://topcs.blob.core.windows.net/public/flight_data_part1.csv -o part1.csv
	!curl https://topcs.blob.core.windows.net/public/flight_data_part2.csv -o part2.csv
	```

1. Now paste the following statements into the next cell to load the first CSV file into a DataFrame and show the number of rows and columns:

	```python
	import pandas as pd

	df1 = pd.read_csv('part1.csv')
	df1.shape
	```

1. Call `head()` on the DataFrame to display the first five rows:

	```python
	df1.head()
	```

1. Use these statements to load the second CSV file and show the number of rows and columns:

	```python
	df2 = pd.read_csv('part2.csv')
	df2.shape
	```

1. Call `head()` on the DataFrame to display the first five rows:

	```python
	df2.head()
	```

1. It appears that the datasets share the same schema. Use the `append()` method to merge the two and produce a new Dataframe containing all rows from both datasets, and `shape` to confirm that the combined DataFrame contains 620,000 rows:
  
	```python
	df = df1.append(df2, ignore_index=True)
	df.shape
	```

This is a rather large dataset, but data professionals frequently deal with ones that are orders of magnitude larger.

## Clean the data









---

Now you are ready to analyze our data. You need to 
- Load a full set of flight data
- Clean up any duplicate rows and unncessary columns 
- Retrieve the mean and maximum arrival delay time 

It turns out that the *flight_data_part1.csv* file you loaded in the previous lesson does not contain all the flight information. There is a second csv file, *flight_data_part2.csv* you need to load. 

Load the two csv files into DataFrames. Check the number of rows in each DataFrame. You should have 300,000 rows in *flight_data_part1* and 320,000 rows in *flight_data_part2*. Combine them together into one DataFrame: 

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

Now you can use the `mean` function to determine the mean of the ARR_DELAY column for all flights and the `max` function to determine the longest delay: 
```python
print(all_flights.ARR_DELAY.mean()) # outputs : 2.824561633466266
print(all_flights.ARR_DELAY.max()) # outputs : 2153.0
```

BONUS: Can you figure out how many flights arrived more than 10 minutes late? HINT: You don't need a comprehension, look up *filters* on pandas DataFrames.

```python
late_flights = all_flights[all_flights['ARR_DELAY']>=10]
print(len(late_flights)) # outputs : 126988
```
Congratulations you are moving data around like a professional! Now let's finish up with a look at how you visualize your data with *matplotlib*