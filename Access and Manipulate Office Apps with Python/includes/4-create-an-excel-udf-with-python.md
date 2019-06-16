# How to create an Excel UDF with Python

The team one cubicle over has written a remarkable Python application that predicts good times to perform maintenance on shopfloor tool _before they break down_.  Your boss already manages complex scheduling chores with an Excel spreadsheet that's taken years to develop.  While it'd be great to have those real-time updates show up in his reports, it's totally impractical to rewrite all the Excel formulae into Python.

You come to the rescue:  you point out that you can make Python and Excel work _together_.  You'll just provide a **user-defined function** (UDF) in the spreadsheet that refers to the Python library.


## Required package

Several packages include UDF capabilities.  For this Lesson, install open-source **xlwings**:

    python3.6 -m pip install xlwings


## Demonstration

## Further study

The demonstration above showed Python reading from a spreadsheet.  The same **OpenPyXL** package also writes new spreadsheets, and updates existing ones.  **OpenPyXL**'s capabilities considerably exceed the limits of what [its documentation](https://openpyxl.readthedocs.io/en/stable/) only introduces, in fact.  **OpenPyXL** accesses essentially everything within Excel, although few of those capabilities have been written up as working examples yet.

That's not all:  other Python packages, among which [**PyXLL**](https://www.pyxll.com/) is the most polished, are **add-ins** for Excel:  they communicate with an executing instance of Excel.  Excel can be used as a **dashboard**, for instance, with certain cells lighting up as alarms when a particular Python calculation yields a particular result.  Or the communication can go the other way:  Python can be used to drive a Web site, as [TODO with Jeff:  reference] introduces, with its content coming in real time from an Excel spreadsheet.  The next Lesson shows a small example of the rich additional communication possible between Excel and Python.


## Summary

* 
