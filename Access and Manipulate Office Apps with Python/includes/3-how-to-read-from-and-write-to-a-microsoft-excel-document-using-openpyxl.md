# How to read from and write to a Microsoft Excel document using **OpenPyXL**
 
You're responsible for an enormous, complicated spreadsheet.  You remember that you saw one particular cell in a peculiar color--was it purple?  Blue?  That particular value is suddenly important to you, but how are you going to find it?  Do you have to scan all tens of thousands of individual cells of each of the scores of sheets?

No:  there are easier ways.  In principle, [you can use Excel's built-in **Find** dialogue](https://excel.tips.net/T002396_Finding_Cells_Filled_with_a_Particular_Color.html), but it only knows to search for an exact color match.  You could [write a macro in VBA](https://www.thespreadsheetguru.com/the-code-vault/2014/11/5/retrieve-excel-cells-font-fill-rgb-color-code), but that presents its own problems.  Let's see how long it takes to solve this in Python ...


## Demonstration program

Install OpenPyXL:

    python -m pip install openpyxl

Create

     from openpyxl import load_workbook
     
     DEFAULT_COLOR = 1
     this_workbook = load_workbook(filename="Total Analysis.xlsx")
     for sheet in this_workbook:
         for column in range(1, 1 + len(list(sheet.columns))):
             for row in range(1, 1 + len(list(sheet.rows))):
                this_cell = sheet.cell(column=column, row=row)
                this_font = this_cell.font
                this_color = this_font.color.value
                if this_color != DEFAULT_COLOR:
                    print(f"On sheet {sheet.title}, cell "
                          f"{this_cell.column}{this_cell.row} "
                          f"has color {this_color}.")

If you have any appropriate `Total Analysis.xlsx` at hand, and you launch this program, you'll immediately see output that looks something like

        ...
    On sheet May 2018, cell J110 has color FF00B0F0.
    On sheet May 2018, cell J111 has color FF00B0F0.
    On sheet May 2018, cell M22 has color FF444444.
    On sheet June 2018, cell A27 has color FFFFFF00.
    On sheet June 2018, cell A32 has color 9.
    On sheet June 2018, cell A33 has color 9.
    On sheet June 2018, cell B8 has color FFFF0000.
    On sheet June 2018, cell B9 has color FFFF0000.
        ...

and so on.  While there is still a little work to do matching these color values to your memory of what you saw, you are close to a conclusive answer already.


## One-offs

Notice the peculiar nature of this program.  Generally people think of a computer program as something run many times--maybe thousands or millions of time.  The previous lesson, for instance, focused on an automation that would be useful every couple of weeks.

This small application is different.  It's only designed to be run once, just to help find a one-time result.  That's OK:  some programs are so small and quick to write, that it's faster to let the computer figure out a result for you one time, even including your effort to program the computer, than to undertake any alternative solution.  You can think of this as "experimental" programming.


## Further study

The demonstration above showed Python reading from a spreadsheet.  The same **OpenPyXL** package also writes new spreadsheets, and updates existing ones.  **OpenPyXL**'s capabilities considerably exceed the limits of what [its documentation](https://openpyxl.readthedocs.io/en/stable/) only introduces, in fact.  **OpenPyXL** accesses essentially everything within Excel, although few of those capabilities have been written up as working examples yet.

That's not all:  other Python packages, among which [**PyXLL**](https://www.pyxll.com/) is the most polished, are **add-ins** for Excel:  they communicate with an executing instance of Excel.  Excel can be used as a **dashboard**, for instance, with certain cells lighting up as alarms when a particular Python calculation yields a particular result.  Or the communication can go the other way:  Python can be used to drive a Web site, as [TODO:  reference] introduces, with its content coming in real time from an Excel spreadsheet.


## Summary

...
