# Visualizing data with matplotlib

In the previous lessons you learned how to store and manipulate data using Python, and the NumPy and pandas libraries.  In this lesson we will learn how to visualize data with plots and graphs using the matplotlib library.

## Importing the matplotlib library 
We will need the matplotlib library for visualizations along with numpy and pandas for data storage and manipulation
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```
## Displaying a simple graph

Using *matplotlib* to display a graph follows a pattern. 
 1. Create a data object containing information you want to visualize. 
 2. Define a plot which determines what data to display.
 3. Display the graph.

Create a DataFrame containing two columns with the corresponding temperatures in Celsius and Farenheit:
```python
column_names = ['Celsius','Farenheit']
data = [[0,32],[5,41],[10,50],[15,59],[20,68],[25,77],[30,86],[35,95]]
temperatures = pd.DataFrame(data, columns = column_names)
```

We use the `plot` function to create a linear graph of the two temperatures. The `plot` function requires the following parameters:
- **x** the values to plot across the x axis
- **y** the values to plot across the y axis

After calling the `plot` function to define a graph, call the `show` function to display the graph:
```python
plt.plot(temperatures['Celsius'],temperatures['Farenheit'])
plt.show()
```
Generates the following output:
![Celsius vs Farenheit](\Media\SimpleCelsiusvsFarenheit.png)

## Adding labels and titles
Graphs are easier to read when they are labelled.
- `title` adds a title to the plot
- `xlabel` adds a label to the x-axis
- `ylabel` adds a label to the y-axis

```python
plt.plot(temperatures['Celsius'],temperatures['Farenheit'])
plt.title('Celsius vs Farenheit')
plt.xlabel('Celsius')
plt.ylabel('Farenheit')
plt.show()
```
Generates the following output:
![Graph with labels](\Media\CelsiusvsFarenheitWithLabels.png)

# Calling `plot` function of DataFrame
the pandas DataFrame object has a numebr of plotting functions. If your data is stored in a pandas DataFrame you can call the `plot` function of the DataFrame passing in the column names for the x and y axis:
```python
column_names = ['Celsius','Farenheit']
data = [[0,32],[5,41],[10,50],[15,59],[20,68],[25,77],[30,86],[35,95]]
temperatures = pd.DataFrame(data, columns = column_names)

# Call plot function of DataFrame 
# Passing in DataFrame column names for x and y axis
temperatures.plot(x='Celsius',y='Farenheit')
plt.title('Celsius vs Farenheit')
plt.xlabel('Celsius')
plt.ylabel('Farenheit')
plt.show()
```

## Scatter plots
[Scatter plots](https://en.wikipedia.org/wiki/Scatter_plot) are very useful when analyzing data. They allow us to determine if there might be a correlation between two columns or whether the two values are independent on each other. Basically we want to figure out does one value always go up when the other goes up? Does one value always go down when the other goes up? If there is a correlation between the values the dots displayed will form a sloped line.

Use the `scatter` function to display a scatter plot instead of a line graph:
```python
column_names = ['Celsius','Farenheit']
data = [[0,32],[5,41],[10,50],[15,59],[20,68],[25,77],[30,86],[35,95]]
temperatures = pd.DataFrame(data, columns = column_names)

# Call scatter function to create scatter plot
plt.scatter(temperatures['Celsius'],temperatures['Farenheit'])
plt.show()
```
Generates the following output:
![Scatter plot Celsius vs Farenheit](\Media\scatterplotCelsiusFarenheit.png)

if you prefer working with DataFrame functions directly, add the *kind* parameter to the DataFrame `plot` function to generate the exact same output:
```python
# specify kind parameter = 'scatter'
temperatures.plot(x='Celsius',y='Farenheit',kind='scatter') 
plt.title('Celsius vs Farenheit')
plt.xlabel('Celsius')
plt.ylabel('Farenheit')
plt.show()
```
The dots in our scatter plot create a sloped line indicating a correlation between the two values. If there was no correlation you might see a plot like this:
![Scatter plot showing no correlation](\Media\RandomScatterPlot.png)
# Creating bar charts
Bar charts are another great tool for visualizing data. 
Suppose You had a DataFrame containing the total number of different pets owned by people in an appartment building:
```python
column_names = ['Pet type','Total Owned']
data = [['Cat',75],['Dog',105],['Bird',3],['Other',17]]
pets = pd.DataFrame(data, columns = column_names
```
To display this in a bar chart you call the `bar` function and pass in the data to use as categories, then the data to use for totals in each category:
```python
plt.bar(pets['Pet type'],pets['Total Owned'])
plt.show()
```
Generates the following output:
![Total pets by category bar chart](\Media\PetsBarChart.png)

If you prefer working directly with the DataFrame `plot` function, you can specify *bar* for the *kind* parameter to generate a bar chart:
```python
pets = pd.DataFrame(data, columns = column_names)
pets.plot(x='Pet type',y='Total Owned', kind='bar')
plt.show()
```
# Grouping data for bar charts
Sometimes the data we receive needs to be summarized before it can provide useful information in a bar chart. Imagine if instead of having the total number of each pet type, we had received raw data telling us the name of each person and what type of pet they own:
```python
column_names = ['Owner','Pet type','Total Owned']
data = [['Diane','Cat',2],['Dave','Dog',1],['Matt','Bird',1],['Fahd','Cat',1]]
pets = pd.DataFrame(data, columns = column_names)
pets.plot(x='Pet type',y='Total Owned', kind='bar')
plt.show()
```
Generates the following chart showing the total pets of each type for each owner.   
![Bar chart showing total of each pet type per owner](\Media\BarChartNotHelpful.png)

It is more useful to have the total number of each pet type aggregated across all owners. To achieve this use the `groupby` function to group the data for the plot:
```python
DataFrameName.groupby(grouping)[aggregation column].aggregation().plot(kind='bar')
```
- *DataFrameName* : name of the DataFrame containing data to plot.
grouping* : name of column across which to create groups.
- *aggregation column* : name of column across which to perform the aggregation (sum, count, mean, etc..)
- *aggregation* : the aggregation action to perform (sum, count, mean, etc...)

To get the total number of pets for each type of pet:
- *DataFrameName* will be *pets*. 
- *grouping* will be *Pet type*.
- *aggregation column* will be *Total Owned*.
- *aggregation* will be *sum*.
```python
pets.groupby('Pet type')['Total Owned'].sum().plot(kind='bar')
plt.show()
```
Generates the following graph:
![Aggregated bar chart](\Media\AggregatedBarChartPets.png)

## Histograms
A histogram shows the distribution of data. Bar graphs show data for multiple columns. A histogram shows how data is distributed for a single column. 
Suppose you want to know how many people have 1 pet, how many people have 2 pets, how many people have 3 pets, and so on. A histogram is the perfect visualization.

To create a histogram you must specify 
- *kind* equals *hist* 
- the *bins* parameter to define how to bin each subtotal. For example:
    - bins=[0,1,2,3] would return the total number of people who own 0 pets, 1 pet, 2, pets, and 3 pets.
    - bins=[0,2,4,6] would return the total number of people who have 0 or 1 pets 2 or 3 pets, 4 or 5 pets, and 6 pets.


- *rwidth* is an optional parameter that specifies the width of each bar.

We can create a histogram showing how many people own how many pets:
```python
pets[['Total Owned']].plot(kind='hist',bins=[0,1,2,3,4,5],rwidth=0.5)
plt.show()
```
Generates the following output:
![Total pets owned histogram](\Media\PetsHistogram.png)
## Analyzing flight data
In the last lesson you loaded a DataFrame containing flight information. Let's use matplotlib to visualize the flight data and gain some insights into the flight delays.
Specifically we want to check 
 - What data might be correlated to arrival delays.
 - The average delay times for each airport.
 - A histogram showing how many flights are delayed by how long.
Let's start by examining the all_flights.csv file. We will need to use the data in the following columns:
- *DEP_DELAY*: number of minutes late the flight departed,
- *ARR_DELAY*: number of minutes late the flight arrived.
- *OP_CARRIER_FL_NUM*: flight number.
- *ORIGIN*: origin airport of flight.
- *DEST*: destination airport of flight.

First we need to load a pandas DataFrame with the flight data:
```python
flight_df = pd.read_csv('all_flights.csv')
```
### Looking for data correlation
Use a scatter plot to see if there is a correlation between departure delays and arrival delays:
```python
flight_df.plot(kind='scatter',x='DEP_DELAY',y='ARR_DELAY')
plt.show()
```
Generates the output:
![Scatter plot departure and arrival delays](\Media\ScatterPlotArrivalDepartureDelay.png)
The dots show a sloped line indicating there is a correlation between arrival and departure delays.

Use another scatter plot to see if there is a correlation between arrival delays and flight numbers:
```python
flight_df.plot(kind='scatter',x='OP_CARRIER_FL_NUM',y='ARR_DELAY')
plt.show()
```
Generates the output:
![Scatter plot flight number and arrival delays](\Media\ScatterPlotFlightNumDelay.png)

There is no sloped line in this scatter plot so there does not appear to be any correlation between arrival delays and flight numbers.

### Delay times by airport
Display a bar chart showing the mean departure delay by originating airport for a flight:
```python
flight_df.groupby('ORIGIN')['DEP_DELAY'].mean().plot(kind='bar')
plt.show()
```
Generates the output:
![Bar chart departure delay all airports](\Media\barchartdelaysAllairports.png)

This chart is hard to read, so let's extract only the rows for the busiest airports: Atlanta (ATL), Los Angeles (LAX), Chicago (ORD), Dallas (DFW). 

```python
flights_busy_airports = flight_df.loc[flight_df['ORIGIN'].isin(['ATL','LAX','ORD','DFW'])]
```
Display a bar graph showing the mean flight departure delay at the busiest airports.
```python
flights_busy_airports.groupby('ORIGIN')['DEP_DELAY'].mean().plot(kind='bar')
plt.show()
```

Generates the following output:
![Bar chart of departure delay mean at busiest airports](\Media\BarDepartureDelayBusyairports.png)

The mean departure delays do not seem that large. Create a bar chart showing the maximum flight delays at each of the busy airports
```python
flights_busy_airports.groupby('ORIGIN')['DEP_DELAY'].max().plot(kind='bar')
plt.show()
```
Generates the following output:
![Bar chart of highest delays at busiest airports](\Media\BarChartMaxDelays.png)

### Histogram of flight delay times
We can see from the bar charts that the mean flight delay times are quite reasonable even at the busiest airports. We also saw that the longest flight delays were significant! We need to get a sense of how many flights had small delays and how many flights had long delays.
Create a histogram of arrival delays to show how many flights were between 0-10 minutes late, 10-20 minutes late, adn so on up to 120 minutes (two hours):
```python
flight_df[['ARR_DELAY']].plot(kind='hist',bins=[0,10,20,30,40,50,60,70,80,90,100,110,120],rwidth=0.8)
plt.show()
```
Generates the following output:
![Flight delay histogram](\Media\flightDelayhistogram.png)

Congratulations, you have now learned how to store, manipulate and visualize data in Python! We have only scratched the surface in terms of the capabilities of Python, NumPy, pandas, and matplotlib. So if you need to perform a function or create a graph that was not covered in this lesson, search for documentation and tutorials, you may discover there is a function or parameter to do exactly what you need. You are now ready to handle data in Python.


