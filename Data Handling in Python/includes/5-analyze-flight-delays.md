# Exercise: Use NumPy to analyze flight delays

Now it's time to write *real* code to operate on *real* data. In this exercise, you will load a CSV file containing 99 rows of data (plus a header row with column names) regarding flight delays at a selection of U.S. airports on October 1, 2018. From the data, you will answer the following questions:

- What was the mean (average) delay time? 
- How many flights arrived more than 10 minutes late?
- What was the longest delay for any flight on that date?

All of this can be done without NumPy. But with NumPy (and with a comprehension or two), you can do it all in less time than it would take to write the code to parse the CSV file using Python alone.

1. Begin by returning to [Azure Notebooks](https://notebooks.azure.com) and creating a new notebook named "NumPy" in the "Data Handling in Python" project that you created earlier. Select Python 3.6 as the language.

1. Enter the following statement in the notebook's first cell and click the **Run** button to download a CSV file containing flight-delay data:

	```bash
	!curl https://topcs.blob.core.windows.net/public/flight_delays.csv -o flight_delays.csv
	```

1. Add the following code to the next cell and run it to load the contents of the CSV file into memory in a NumPy array and show the column names:

	```python
	import numpy as np

	flight_data = np.genfromtxt('flight_delays.csv', delimiter=',', dtype=None, names=True, encoding=None)
	print (flight_data.dtype.names)
	```

1. Now use the following statement to show the contents of the array:

	```python
	print (flight_data)
	```

	Each row contains data for one flight. The 12th column — ARR_DELAY — tells us in minutes how late a flight arrived. A negative number indicates that the flight arrived early.

1. Use the array's `mean()` function to determine the mean of the values in the ARR_DELAY column for all flights: 

	```python
	flight_data['ARR_DELAY'].mean()
	```

	What was the mean delay time? On average, did flights arrive early or on time on that date?

1. To determine how many flights were delayed more than 10 minutes, use a comprehension to create a list and a filter to ignore flights that don't fit the criterion:

	```python
	delayed_flights = [flight for flight in flight_data if flight['ARR_DELAY'] > 10]
	len(delayed_flights)
	```

	How many flights were delayed by more than 10 minutes?

1. To figure out the longest delay, use `nparray`'s `max()` function to find the largest value in the ARR_DELAY column:

	```python
	flight_data['ARR_DELAY'].max()
	```

1. Suppose you want to print the airline code and flight number for the flight that experienced the longest delay. That's the perfect excuse to use another list comprehension:

	```python
	max_delayed_flight = [flight for flight in flight_data if flight['ARR_DELAY'] == flight_data['ARR_DELAY'].max()]
	print(max_delayed_flight[0][1] + ' ' + str(max_delayed_flight[0][3]))
	```

Observe that the final statement uses column indexes rather than column names. Either works since you loaded column names from the header row of the CSV file. The call to `str()` converts the flight number into a string so it can be printed. Seeing that the flight number is just that — a number and not a string — `genfromtxt()` loaded it as an integer rather than a string.

