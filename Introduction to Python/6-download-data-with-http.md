# Download data with HTTP

When coding data heavy Python projects such as those involving machine learning it is common to write code to download data from online data sources. Common online data sources include websites which make data files available for download. In many cases, these websites regularly publish new data files. While such data files can be manually downloaded through a web browser it can be much more efficient to automate this data collection task through a Python script which downloads the file automatically.

Python provides the `urllib` module, which provides a `request` object for making HTTP requests to download weather data.

```python
import urllib.request

download_url = 'https://www.transtats.bts.gov/Download_Lookup.asp?Lookup=L_AIRPORT'
response = urllib.request.urlopen(download_url)
airports_csv = response.read().decode('utf-8')
print(airports_csv)
```

Observe the decoding of the file using the specified character encoding. It is possible that data downloaded from older systems may use an encoding other than UTF-8. Many older data collection systems produce ASCII text files. Properly decoding them is essential to preparing the data for use.

As part of the legacy API still made available in Python 3, downloaded data can be downloaded directly to a file using the `urlretrieve` function:

```python
download_file_name = 'data.csv'
urllib.request.urlretrieve(download_url, download_file_name)
```

## Download airport lookup file

TODO: Add introduction.

1. Return to the Azure notebook that you created previously.

	![Jupyter notebook in Azure](../media/2-initial-notebook.png)

	_Jupyter notebook in Azure_

1. Add a new Python cell after the cell which ends with

	```python
	state_airport_file_name = state_abbr.lower() + '_airports.csv'
	```

1. In the new Python cell, add the following code to download "airports.csv" file from a web server:

	```python
	# import the Python API for make HTTP (web page) requests
	import urllib.request
	
	# Download the data from from the URL and save to the specified file name
	urllib.request.urlretrieve(download_url, airport_file_name)
	```
	
1. Run the Azure notebook, ensure the file is downloaded and the output file of the airports filtered by state is produced.

TODO: Add closing.