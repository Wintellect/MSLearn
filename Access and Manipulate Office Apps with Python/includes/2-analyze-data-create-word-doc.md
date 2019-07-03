# Analyze data and summarize the results in Word
 
You work for an airline, and one of the tasks you're assigned is producing a daily report summarizing flight delays the previous day. Creating the report takes about 30 minutes. You first import the data into Microsoft Excel, and then use Excel to compute key statistics such as the average arrival delay for flights that took place the day before and the percentage of flights that were delayed more than 10 minutes. Next, you copy-and-paste from Excel into a Microsoft Word document to produce a nicely formatted report that includes high-level stats, plus a table showing average delays at individual airports. It's not difficult, but it's unrelenting. It has to be done every day, and the manual nature of the process means there is too much room for human error.

Being a technical person, you decide to automate the process. Python libraries such as [Pandas](https://pandas.pydata.org/) provide more than enough muscle for the analytical part. Other libraries such as [Python-docx](https://python-docx.readthedocs.io/en/latest/) provide rich APIs for generating Word documents. In this lesson, you will marry the two to ingest airline data from a CSV file, analyze it, and produce a daily report summarizing the previous day's on-time performance.

## Analyze data with Pandas

Pandas, short for *Python Data Analysis Library*, is the library that people who work with data for a living turn to for gathering insights from large datasets or preparing it for machine learning. The key data structure in Pandas is the [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html), which contains rows and columns like a database table and includes methods for loading data from CSV files, filtering and sorting data, exporting to JSON, CSV, Excel, and SQL, and much more. In all, it contains more than 200 methods and attributes.

In this exercise, you will load a CSV file and use DataFrame methods to analyze the data.

1. Begin by executing the following commands in a Command Prompt window or terminal to install Pandas and Python-docx:

	```bash
	pip install pandas
	pip install python-docs
	```

1. Create a directory to serve as your project directory and `cd` into it. Then use this command to download a CSV file containing the latest daily information on flight delays:

	```bash
	curl https://topcs.blob.core.windows.net/public/flight_delays.csv -o flight_delays.csv
	```

	`curl` is a Linux command. It's also installed on Windows 10 build 1706 and higher. If you are running an older version of Windows, you can download `curl` from the [`curl` download page](https://curl.haxx.se/download.html), or you can download the CSV file directly from [here](https://topcs.blob.core.windows.net/public/flight_delays.csv).

1. Take a moment to browse the contents of **flight_delays.csv**. It contains a header row with column names, and information on 99 flights. The ARR_DELAY column indicates the number of minutes the flight was late arriving. A negative number means the flight arrived at its destination early.

1. Create a text file named **delays.py** and open it with your favorite text editor. You can use any text editor you'd like, but we recommend using [Visual Studio Code](https://code.visualstudio.com/) — Microsoft's free, lightweight source-code editor for Windows, macOS, and Linux that features IntelliSense, integrated Git support, and more.

1. Paste the following code into **delays.py** and then save the file:

	```python
	import pandas as pd
	
	df = pd.read_csv('flight_delays.csv')
	mean_delay = df['ARR_DELAY'].mean()
	delayed_10 = len(df[df['ARR_DELAY'] > 10])
	percent_10 = percent = len(df[df['ARR_DELAY'] > 10]) / df.shape[0]
	mean_by_airport = df.groupby('ORIGIN')['ARR_DELAY'].mean().sort_values(ascending=False)
	
	print('Mean delay: {0:.0f} minutes'.format(mean_delay))
	print('Number of flights that arrived more than 10 minutes late: {}'.format(delayed_10))
	print('Percentage of flights that arrived more than 10 minutes late: {0:.0%}'.format(percent_10))
	print('Mean delays for individual airports:\n')
	print(mean_by_airport)
	```

	TODO: Explain this code.

1. Use the following command to execute **delays.py**:

	```bash
	python delays.py
	```

1. Confirm that the output looks like this:

	```
	Mean delay: 2 minutes
	Number of flights that arrived more than 10 minutes late: 15
	Percentage of flights that arrived more than 10 minutes late: 15%
	Mean delays for individual airports:
	
	ORIGIN
	ABQ    5.735294
	ATL    2.420000
	AMA   -5.400000
	ALB   -6.100000
	Name: ARR_DELAY, dtype: float64
	```

TODO: Add closing.

## Generate a Word document with Python-docx

TODO: Add intro.

1. Open **delays.csv** and insert the following `import` statements at the top of the file:

	```python
	import docx
	from docx.enum.text import WD_ALIGN_PARAGRAPH
	import datetime
	```

1. Add these statements to the bottom of the file, and then save your changes:

	```python
	doc = docx.Document()
	doc.add_heading('Summary of Arrival Delays for {:%b %d, %Y}'.format(datetime.date.today()))
	doc.add_paragraph()
	doc.add_paragraph('Mean delay: {0:.0f} minutes'.format(mean_delay))
	doc.add_paragraph('Number of flights that arrived more than 10 minutes late: {}'.format(delayed_10))
	doc.add_paragraph('Percentage of flights that arrived more than 10 minutes late: {0:.0%}'.format(percent_10))
	doc.add_paragraph()
	doc.add_paragraph('Mean delays for individual airports').alignment = WD_ALIGN_PARAGRAPH.CENTER
	
	table = doc.add_table(rows=mean_by_airport.shape[0]+1, cols=2, style='Table Grid')
	table.rows[0].cells[0].text = 'Airport'
	table.rows[0].cells[1].text = 'Mean Delay in Minutes'
	
	i = 1
	for name in mean_by_airport.index:
	    table.rows[i].cells[0].text = name
	    table.rows[i].cells[1].text = '{:.1f}'.format(mean_by_airport.loc[name])
	    i += 1
	
	doc.save('summary.docx')
	```

	This code uses **Python-docx** to create a Word document, insert content, and save the document under the name **summary.docx**. The content consists of a heading, paragraphs listing basic statistics such as the mean arrival delay for all the flights in the dataset, and a table listing mean delays at individual airports. Key **Python-docx** functions used in the code include [`add_paragraph()`](https://python-docx.readthedocs.io/en/latest/api/document.html#docx.document.Document.add_paragraph) and [`add_table()`](https://python-docx.readthedocs.io/en/latest/api/document.html#docx.document.Document.add_table).

1. Use the following command to execute **delays.py** again:

	```bash
	python delays.py
	```

1. Confirm that the project directory now contains a file named **summary.docx**. Open the file in Microsoft Word. What do you see inside?

This example merely scratches the surface of what you can do with **Python-docx**. Virtually anything that can be done in Microsoft Word can be done with **Python-docx**, too.
