# Reading a csv file with Python

The U.S. [Bureau of Transportation Statistics](https://www.transtats.bts.gov) (BTS) maintains a wealth of information regarding transportation in the United States and makes much of that data available to the public. One of the datasets you can download from the BTS Web site lists all the airports in the world and includes their three-letter airport codes, the cities they're located in, and their names.

In this lesson, you will download that dataset from the BTS Web site, upload it to Azure Notebooks, and load it into the notebook you created in the previous lesson. Along the way, you will learn how to read files in Python and how to perform basic looping using `for-in` statements. In addition, you will learn about one of Python's most important data types: lists, which hold collections of data.

## Download a CSV file containing airport data

The first step is to download the dataset and have a look at its content and structure. The dataset is a text file containing [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) (Comma-Separated Values) data. CSV is an extremely common data format — so common that there are Python libraries whose only purpose is to simplify reading and writing CSV files.

1. [Click here](https://www.transtats.bts.gov/Download_Lookup.asp?Lookup=L_AIRPORT) to open your browser and download a CSV file containing a collection of airport codes, airport locations, and airport names from the BTS Web site. Save the file to the location of your choice and name it **airports.csv**.

	> The file that you're downloading has a .csv\_ file-name extension. Even if you tell the browser to name it **airports.csv**, the file may be saved with a .csv\_ extension. If that happens, rename the file so that it ends in .csv. 

1. Once the download is complete, open **airports.csv** in your favorite text editor. Take a moment to browse the contents of the file:

    ```
    Sea,Seattle
    Hou,Houston
    DTW,Detroit
    Bos,Boston
    LGA,New York
    DUL,Washington
    ```

Observe that the first line is a header containing column names. Each line thereafter contains information regarding a specific airport. Furthermore, each line begins with a quoted string containing an airport code (for example, "JFK" for John F. Kennedy airport in New York), and ends with another quoted string containing the airport's location and name, separated by a colon.


## Uploading files to your Azure Notebook
Return to the Azure notebook that you created in the previous lesson.
# Add image #
Jupyter notebook in Azure
Use the File -> Upload... command to upload airports.csv from your local hard disk. Set "Destination folder" to ~/project so the file will be stored durably rather than just for the length of the session.
# Add image make sure you select projects folder#
Uploading airports.csv
## Reading csv files in Python

In order to load this data, you need to know how to read a csv file in Python. The [csv](https://docs.python.org/2/library/csv.html) library contains a number of useful methods for working with CSV files. In order to use this library in your Notebook you need to import the csv library. Add the following code to your Azure Notebook:  

```python
import csv
```
A file cannot be read unless it is opened first. Use the `open` method to open the file and then use the `reader` function of the csv file to read the file into a reader object. The reader function accepts a *delimiter* which indicates what character separates different values in a row. The default value for delimiter is a comma.

## Parsing the csv data
You can iterate across the reader object to access the content read in from the file.

Use the following code to open the csv file and display the contents

```python
with open('airports.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        print(row)
# outputs 
# ['Sea', 'Seattle']
# ['Hou', 'Houston']
# ['DTW', 'Detroit']
# ['Bos', 'Boston']
# ['LGA', 'New York']
# ['DUL', 'Washington']
```

If you want to store the values in a list you can convert the reader into a list object
```python
airports = []

with open('airports.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    airports = list(csvReader)
print(airports) 
# outputs : [['Sea', 'Seattle'], ['Hou', 'Houston'], ['DTW', 'Detroit'], ['Bos', 'Boston'], ['LGA', 'New York'], ['DUL', 'Washington']]
```
Because our file contains two columns, you could create two lists to hold the values. One for airport codes, and one for airport cities. You can assign the row object to a pair of variables and use those variables to add values to the list.

```python
airport_codes = []
airport_cities = []
with open('airports.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        code, city = row
        airport_codes.append(code)
        airport_cities.append(city)
print(airport_codes) # outputs : ['Sea', 'Hou', 'DTW', 'Bos', 'LGA', 'DUL']
print(airport_cities) # outputs : ['Seattle', 'Houston', 'Detroit', 'Boston', 'New York', 'Washington']
```

Since our data contains two columns we could store the values in a dictionary as keys and values instead of across two lists. 
```python
airports ={}
with open('airports.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        code, city = row
        airports[code]=city
print(airports) # outputs : {'Sea': 'Seattle', 'Hou': 'Houston', 'DTW': 'Detroit', 'Bos': 'Boston', 'LGA': 'New York', 'DUL': 'Washington'}
```
Should use store the data in a dictionary or as two lists? That depends on how you will be using the data later in your code. If you will only need to access one column of data at a time, you should store the data in lists. If you always need to know which code goes with which city you should store the data in a dictionary.

##Cleaning the data
It is common for data files to have data that is not formatted the way we need. Our airport codes are a mix of upper and lower case. We should clean up the airport codes to make them all uppercase using a Comprehension:
```python
airport_codes = [code.upper() for code in airport_codes]
print(airport_codes) # outputs : ['SEA', 'HOU', 'DTW', 'BOS', 'LGA', 'DUL']
```
Don't forget you can use comprehensions on dictionaries as well:
```python
airports = {code.upper():city.capitalize() for (code,city) in airports.items()}
print(airports) # outputs : {'SEA': 'Seattle', 'HOU': 'Houston', 'DTW': 'Detroit', 'BOS': 'Boston', 'LGA': 'New york', 'DUL': 'Washington'}
```


## Parse airport data

In this exercise, you will use string slicing and string splitting to parse the strings read from the data file in the previous lesson into a list of lists, with the inner lists containing data regarding individual airports. Lists of lists are very common in Python and are useful for storing tabular data — that is, data that is organized into rows and columns.

1. Return to the Azure notebook that you created. Add the following statements to the empty cell at the end of the notebook:

	```python
	for airport in all_airports:
	    items = airport.split('","')
	    airport_code = items[0][1:]
	    print(airport_code)
	```

	Based on the discussion of string splitting and slicing in the previous section, can you predict what the output will be?

1. Run the cell and confirm that it produces a lst of airport codes parsed from the strings in the file:

	![Printing airport codes](media/print-airport-codes.png)

	_Printing airport codes_

1. The previous code parsed an airport code from each line read from the data file. The next challenge is to get each airport's name and location. Modify the code above as follows:

	```python
	for airport in all_airports:
	    # Split the airport code from the airport location and name and
	    # remove the quotation mark from the beginning of the airport code
	    items = airport.split('","')
	    airport_code = items[0][1:]

	    # Split the airport location and airport name, and remove the quotation
	    # mark and newline character from the end of the airport name
	    subitems = items[1].split(': ')
	    airport_location = subitems[0]
	    airport_name = subitems[1][:-2]

	    # Print the resulting strings
	    print('{0:8}{1:32}{2:1}'.format(airport_code, airport_location, airport_name))
	```

	The purpose of the code in the `for-in` loop is to divide a string containing an airport code, an airport location, and an airport name into three strings, as diagrammed below. First the string is split at "," to produce `items[0]` and `items[1]`. Then the quotation mark is removed from the beginning of `items[0]`, producing an airport code. Next, `items[1]` is split to produce `subitems[0]` and `subitems[1]`. The former is the airport location, and the quotation mark and embedded newline character are removed from the end of `subitems[1]` to get the airport name.

	![Splitting and trimming strings](media/string-splitting.png)

	_Splitting and trimming strings_

	The final line in the `for-in` loop uses the `format` function that can be called on any string in Python to format a string. It left-aligns `airport_code` in a field that is 8 spaces wide, `airport_location` in a field that is 32 spaces wide, and `airport_name` in a field that occupies the remainder of the line. It's one way in Python to align printed output into columns. Based on this, can you predict what the output will be?

1. Now run the modified cell. Confirm that the output resembles the output below.

	![Printing airport data](media/print-parsed-airports.png)

	_Printing airport data_

1. The next step is to add the airport codes, locations, and names to a list rather than simply print them out. To that end, add the following code to the empty cell at the bottom of the notebook:

	```python
	airports = []
	
	for airport in all_airports:
	    items = airport.split('","')
	    airport_code = items[0][1:]
	    subitems = items[1].split(': ')
	    airport_location = subitems[0]
	    airport_name = subitems[1][:-2]
	    airports.append([airport_code, airport_location, airport_name])
	    
	for airport in airports:
	    print('{0:8}{1:32}{2:1}'.format(airport[0], airport[1], airport[2]))
	```

	This code defines a new list named `airports` and adds to it a list containing the airport code, location, and name for each line in the input. Then it prints each list in the list of lists.

1. Run the cell and confirm that it produces the same output as the previous cell.

1. Use the **File** -> **Save and Checkpoint** command to save the notebook.

Now that you have separated airport codes, airport locations, and airport names into explicit entities, you are prepared to take the next step, which involves filtering the data so the list includes only U.S. airports.
