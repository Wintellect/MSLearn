# How to create an Excel UDF with Python

The team one cubicle over has written a remarkable Python application that predicts good times to perform maintenance on shopfloor tool _before they break down_.  Your boss already manages complex scheduling chores with an Excel spreadsheet that's taken years to develop.  While it'd be great to have those real-time updates show up in his reports, it's totally impractical to rewrite all the Excel formulae into Python.

You come to the rescue:  you point out that you can make Python and Excel work _together_.  You'll just provide a **user-defined function** (UDF) in the spreadsheet that refers to the Python library.


## Required package

Several packages include UDF capabilities.  For this Lesson, install open-source **xlwings**:

    python3.6 -m pip install xlwings


## Demonstration

[TODO]

## Further study

Think about VBA and Python.  VBA is generally a bit more convenient for small scripting jobs of which it's capable.  Python can do essentially everything VBA does, _plus_ Python now connects to a vast world of libraries outside Excel, outside Office, and even outside Microsoft.  Ideal is not to try to figure out which is better, but how to make the best use of both.

One engaging way to practice teamwork between Excel and Python is to compute complex results in Python, then graph them with Excel's built-in visualization methods.  Keep the interface between the two constant, while you iteratively improve the calculations on the Python side, and the visual design on the Excel side.


## Summary

* Excel's **add-in** construction defines a standard interface which several different Python packages use to communicate _in real time_ between an active Excel spreadsheet and an executing Python program.
* **xlwings** is a good introductory choice among these packages.
* Definition of a UDF is a good way to program a channel where Excel and Python can exchange results.
