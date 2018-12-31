# Performing basic stats calculations with numpy

## Airline Data Exercise: Calculating Some Basic Stats for Ontime Flight Data

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this sixth exercise within the module, the ontime flight data will be used to calculate some basic stats.

1. Open the Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks. You may want to make a duplicate copy of this notebook before attempting this exercise.

1. Add a new cell to the bottom of the notebook and add the following code.

```python
airport_delays_monthly_avgs = []

for airport_code in airport_codes:
  airport = airports[airport_code]
  airport_indexes = [ ontime_row[0].decode('UTF-8') == airport_code for ontime_row in ontime ]
  airports_for_code = ontime[airport_indexes]
  airport_dep_delays = airports_for_code['dep_delay']

  dep_delays_mean = airport_dep_delays.mean()
  dep_delays_std = airport_dep_delays.std()

  airport_delays_monthly_avgs.append((
    airport_code,
    airport.city,
    airport.state_name,
    airport_dep_delays.mean(),
    airport_dep_delays.std(),
    len(airports_for_code)
  ))

print(len(airport_delays_monthly_avgs))
```

The variable `airport_indexes` will contain `True` for each index which matches the current `airport_code`. Using the `airport_indexes`, all of the matching flights for the origin airport are sliced out and the `dep_delay` column is extracted. Using the NumPy's built-in mean and standard deviation functions, the mean and standard deviation for departure delay in minutes is calculate for the airport. Combining the airport code, airport location data and calculated stats a values a new list named `airport_delays_monthly_avgs` is created.

Run the code for the entire notebook using 'Restart & Run All' from the 'Kernel' menu. Ensure everything works properly. The execution of this cell will take about 5-10 mins. Ensure the output for the length is 345.

1. Add a new cell to the bottom of the notebook and add the following code.

```python
airport_delays_monthly_avgs.sort(key=lambda a: a[3], reverse=True)
```

This will sort the list data in descending order based upon mean of the airport departure delays. The value of index 3 is the mean. Run the cell.

1. Add a new cell to the bottom of the notebook and add the following code.

```python
with open('./airports_avg_delay_sorted.csv', 'w') as airports_delay_avg_delay_sorted_file:

    airports_avg_delay_sorted_writer = csv.writer(
        airports_delay_avg_delay_sorted_file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )
    
    airports_avg_delay_sorted_writer.writerow([
        'ORIGIN', 'ORIGIN_CITY', 'ORIGIN_STATE',
        'DEP_DELAY_MEAN','DEP_DELAY_STDEV','NUM_OF_FLIGHTS'
    ])
    
    for airport_delays_monthly_avg in airport_delays_monthly_avgs:
        airports_avg_delay_sorted_writer.writerow(airport_delays_monthly_avg)
```

The list `airport_delays_monthly_avgs` is written to a CSV file named 'airports_avg_delay_sorted.csv'. Python's `csv` module will take care of formatting the CSV content correctly. The final outputed file will contain some basic statistics of departure delays at US airpots in the month of October 2018.