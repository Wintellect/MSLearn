# Use Azure Cognitive Services to extract text from photos

At the end of this unit, you’ll have a fully working application. Along the way, you’ll set up the VS Code debugger so that you can run the code locally, set breakpoints, and inspect it thoroughly. Flask has provisions for debuggers, and there are a handful of interesting choices... if you didn’t already have VS Code, which leverages Microsoft’s decades of experience with producing code development environments. So you’ll actually leave Flask’s debugging mode set to Off, and leave the driving to VS Code.

## What you’re about to do

Reusable functions have been a hallmark of high-level programming languages since the advent of FORTRAN. Web programming made reusable functions difficult to implement, particularly for JavaScript. Every page in the site that utilized the same functions would need to use an HTML `<script>` tag with its `src` attribute linked to the same file; and then JavaScript itself had its own import statements. You probably would only use those import statements in a library file that would itself be imported. And only in a language like JavaScript would you find yourself implementing a skill such as “importing exports.”

JavaScript code modules are about as reusable as Styrofoam cups. Sure, those cups are marketed that way, because “reusable” sounds better than “disposable.” But every single new page, you find yourself getting another one from the dispenser.

Flask is a genuine effort to make Web pages behave like real programs. There is one application, with one file containing the logic for all the related pages in a site. So you declare all your dependencies once, as you did in the previous unit. That logic is separated from the HTML files, which are rendered as templates that borrow some of their content from the Flask functions.

What’s more, the code that manages each of the pages can be separated from the code that processes the back-end logic. This creates opportunities for genuinely reusable code: functions represented by names, and that reside just next door to the page logic. It’s the Web the way it should have been done to start with — the way FORTRAN would have handled it.

So what you’ll do in this unit is gather the inputs from the index.html file and process them into parameters. You’ll then pass those parameters to independent functions (straight Python, not Flask) that will contain the API and SDK calls to Azure. These independent functions will be designed so that a more complex Web application built on this chassis would be able to use them simply by passing parameters the same way.

In this unit, you’ll accomplish the following:
- Build a Flask function for processing input
- Build Python functions for acquiring results from Azure
- Produce the HTML Flask templates for formatting output
- Set up the VS Code debugger for Flask
- Deploy final changes to Azure

## Build a Flask function for processing input

