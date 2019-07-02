# Use machine learning to perform sentiment analysis in Excel

Imagine that you're a software developer at an Internet vacation-rentals firm and the company's communications department has asked you to create a spreadsheet lets them analyze text for sentiment. The idea is that if sentiment towards the company turns negative on social media, communications can get out in front of it.

Scoring text for sentiment is rather easily accomplished today with machine learning. Python has a number of world-class libraries available for building and training machine-learning models, including [Scikit-learn](https://scikit-learn.org/stable/index.html). Excel supports [User-Defined Functions](https://support.office.com/en-ie/article/create-custom-functions-in-excel-2f06c10b-3622-40d6-a1b2-b6748ae8231f), which enable users to write custom functions that are called just like `SUM()` and `AVG()` and other functions built into Excel. But UDFs are written [Visual Basic for Applications](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications). in order to use Scikit-learn in Excel, you need to be able to write UDFs in Python.

Fortunately, there are libraries that let you do just that. One of them is [Xlwings](https://www.xlwings.org/), an open-source library that combines the power of Excel with the versatility of Python. With it, you can write Python code that loads or creates Excel spreadsheets and manipulates their content, write Python macros triggered by button clicks in Excel, access Excel spreadsheets from Jupyter notebooks, and more. You can also use Xlwings to write Excel UDFs

## Install Xlwings

The first step in building the spreadsheet that Communications wants is installing **Xlwings** and other Python packages such as **Scikit-learn**.











Several packages include UDF capabilities.  For this Lesson, install open-source **xlwings**:

    python3.6 -m pip install xlwings


## Write a User-Defined function





## Invoke the UDF from EXcel





## Further study

Think about VBA and Python.  VBA is generally a bit more convenient for small scripting jobs of which it's capable.  Python can do essentially everything VBA does, _plus_ Python now connects to a vast world of libraries outside Excel, outside Office, and even outside Microsoft.  Ideal is not to try to figure out which is better, but how to make the best use of both.

One engaging way to practice teamwork between Excel and Python is to compute complex results in Python, then graph them with Excel's built-in visualization methods.  Keep the interface between the two constant, while you iteratively improve the calculations on the Python side, and the visual design on the Excel side.