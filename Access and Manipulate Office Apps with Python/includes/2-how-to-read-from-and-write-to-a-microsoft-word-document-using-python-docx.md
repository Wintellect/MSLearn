# How to read from and write to a Microsoft Word document using **python-docx**
 
Every two weeks you host a meeting of departmental managers.  You prepare an agenda for everyone to read ahead of time.  One segment of the meeting focuses on results from the previous fortnight.  The trick is, though, that different departments not only have different key performance indicators (KPIs), but they keep them in wildly different data stores:  everything from Excel through Access to SAP and Salesforce and GitHub.

The good news is that you have access to all these different datasources.  Every weekend, therefore, you pull up all the different relevant reports, and copy-and-paste all the KPIs into the standard format of a Word copy of your agenda.  It's tedious, but you have it down to a routine, and it doesn't take _too_ long.

Does this sound like a familiar story?  Here's a tip:  any time you think, "... tedious ..." in regard to an aspect of your life at the keyboard, your next thought should be, "Here's a job for Python!"


## Semi-automation attitude

You need to write your agenda in Word, for a variety of reasons.  While the schedule and KPIs are in fixed locations, you embed them in your human explanation of business priorities and motivations.  Still, if the routine parts "write themselves"--if they appear in your draft document **automatically**--they're more likely to be accurate, undamaged by any typing mishap, you'll save time, and, perhaps most crucially of all, you preserve your attention for the difficult business challenges that are _not_ routine.

This lesson, therefore, sketches how you can marry Python's ability to automate or script, to Word's convenience and familiarity.  The specific result below is one you actually can achieve from within Word itself:  Word has its own scripting tools.  Once you can do this simple exercise with Python, though, you open up all Python's power as a potential available within your documents.


## A demonstration

1.  As the previous lesson described, arrange a working Python3.6 (or better) for yourself.

1.  Install **python-docx** in your development environment.  With a working Internet connection, this should be as simple as <br /><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python3.6 -m pip install python-docx`<br /><br />at the command line.


## Summary

[That's it.  If you:]

[* know the basics of writing and running Python programs;
* have a way to use Python 3.6 or later; and
* understand how to install standard packages in your Python environment,]

[then you're ready for the lessons that follow.  Let's dig in!]
