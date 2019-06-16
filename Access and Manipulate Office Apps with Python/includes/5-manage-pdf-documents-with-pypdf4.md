# How to manage PDF documents with PyPDF4

You have IT (information technology) responsibilities for a law office which just scored a massive civil litigation.  You're now responsible not just for many thousands of documents, but over _two million_ on this one case.

The judge is trying to get an idea of what's involved.  You need to sort the documents into twelve categories, and report how many pages of documents are in each.

With a little effort, you figured out the sort, and have the whole collection segregated in a dozen different designated top-level folders.  It's easy to see how much space the folders take up on disk, and it's equally easy to open individual documents and read how many pages they occupy.  Even if you cut down your time to examine one document to ten seconds, though, it's going to take you ... _seven months_ to collect all the results (more, of course, because human bodies break down when operated this way).

You need help.  You need **PyPDF4**.


## Required package

As you've already read in other Lessons, several packages address a particular domain.  In this case, the domain is documents rendered as PDF (portable document format).  We choose **PyPDF4** for its support of recent revisions of the PDF specification.

For this Lesson, install **PyPDF4**:

    python3.6 -m pip install xlwings


## Demonstration

## Further study

The demonstration above showed Python reading from a spreadsheet.  The same **OpenPyXL** package also writes new spreadsheets, and updates existing ones.  **OpenPyXL**'s capabilities considerably exceed the limits of what [its documentation](https://openpyxl.readthedocs.io/en/stable/) only introduces, in fact.  **OpenPyXL** accesses essentially everything within Excel, although few of those capabilities have been written up as working examples yet.

That's not all:  other Python packages, among which [**PyXLL**](https://www.pyxll.com/) is the most polished, are **add-ins** for Excel:  they communicate with an executing instance of Excel.  Excel can be used as a **dashboard**, for instance, with certain cells lighting up as alarms when a particular Python calculation yields a particular result.  Or the communication can go the other way:  Python can be used to drive a Web site, as [TODO with Jeff:  reference] introduces, with its content coming in real time from an Excel spreadsheet.  The next Lesson shows a small example of the rich additional communication possible between Excel and Python.


## Summary

* Several freely-available packages give Python the ability to read and write Excel spreadsheets.
* Among these, OpenPyXL is well-maintained and highly capable.
* A small Python program of only a dozen line can achieve impressive results in automatically retrieving and processing information from an Excel spreadsheet.
* Python is so productive that it's often worthwhile to write a Python program to solve a one-time need.
