# Performing basic stats calculations with numpy

## Airline Data Exercise: Calculating Some Basic Stats for Ontime Flight Data

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this sixth exercise within the module, the ontime flight data will be used to calculate some basic stats.

1. Open the Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks. You may want to make a duplicate copy of this notebook before attempting this exercise.

1. Add a new cell to the bottom of the notebook and add the following code.

```python
airport_delays_monthly_avgs = []

for airport_code in airport_codes:
  airport_indexes = [ ontime_row[0].decode('UTF-8') == airport_code for ontime_row in ontime ]
  airports_for_code = ontime[airport_indexes]
  airport_dep_delays = airports_for_code['dep_delay']

  dep_delays_mean = airport_dep_delays.mean()
  dep_delays_std = airport_dep_delays.std()

  airport_delays_monthly_avgs.append((
    airport_code,
    airport_dep_delays.mean(),
    airport_dep_delays.std(),
    len(airports_for_code)
  ))

print(len(airport_delays_monthly_avgs))
```

1. Add a new cell to the bottom of the notebook and add the following code.

```python
airport_delays_monthly_avgs.sort(key=lambda a: a[1], reverse=True)
```

1. Add a new cell to the bottom of the notebook and add the following code.

```python
with open('./airports_avg_delay_sorted.csv', 'w') as airports_delay_avg_delay_sorted_file:

    airports_avg_delay_sorted_writer = csv.writer(
        airports_delay_avg_delay_sorted_file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )
    
    airports_avg_delay_sorted_writer.writerow(['ORIGIN','DEP_DELAY_MEAN','DEP_DELAY_STDEV','NUM_OF_FLIGHTS'])
    for airport_delays_monthly_avg in airport_delays_monthly_avgs:
        airports_avg_delay_sorted_writer.writerow(airport_delays_monthly_avg)
```
  