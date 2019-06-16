# Summary

In this module, you learned that a great way to solve many problems involves use of a couple of co-operating technologies.  The lessons here specifically brought Python together with common office automation tools to achieve results that would have been tedious or impractical with either alone.

You also practiced use of "third-party" Python packages, freely available without fee from the standard Python PyPI repository.

Finally, you heard that it's time to migrate to Python 3.6 or higher.


## Check your knowledge

1. Python has a growing reputation for its use by artificial intelligence researchers, robotocists, Web site builders, and so on.  Yes or no:  is Python also suitable for one-time-only investigation of a specific computing problem or need?

1. Describe a situation where you might need to construct a spreadsheet, and you use Python to generate a first draft of the spreadsheet.

1. A buddy tells you about a cool new programming package she's using.  You copy the source of the program she demonstrated for you, run it, and see ...<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;`NameError: name COOL-PACKAGE is not defined`<br /><br />What special Python statement might be missing from the top of your program?

1. If you hear a fellow worker complain that an assignment is boring, and just involves mindless pointing-and-clicking through to a result, do you have any reaction other than, "tough"?

1. Your cousin blows your mind by writing a remarkable Python library that compares different retail electricity vendors.  It impresses you so much that you say, "you ought to register that so _any_ Python programmer can install it--just make it available on ..." [name the repository]

1.  One way to compute a particular weighted average in Excel is with a formula such as<br /><br >&nbsp;&nbsp;&nbsp;&nbsp;`= (C14 * D14 + C15 * D15 + C16 * D16 + C17 * D17 + C18 * D18 + C19 * D19 + C20 * D20) / sum(D14:D18)`<br /><br />Explain three benefits of Python's corresponding expression<br /><br >&nbsp;&nbsp;&nbsp;&nbsp;`weighted_average = sum([amount * factor for amount, factor in zip(amounts, factors)]) / sum(amounts)`

1.  Explain one disadvantage of expressing the last computation as<br /><br >&nbsp;&nbsp;&nbsp;&nbsp;`numpy.average(factors, weights=amounts)`

[TODO:  work in introspection and REPL practice.  Or not.]
