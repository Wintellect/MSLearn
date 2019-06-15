# Set up a working development environment with Python
 
The recurring theme of this module is to combine the powers of the Python programming language and different "office productivity" tools such as [Microsoft Word](https://www.office.com/?auth=2), [Microsoft Excel](https://www.microsoft.com/en-us/p/excel/cfq7ttc0k7dx), and a PDF viewer. Each lesson practices a particular aspect of this theme.

The lessons which follow can largely be read in any order you choose:  if you have a special focus on Excel, it's fine to start with those lessons.  Before beginning any of the lessons, though, make sure you have a solid foundation in place to ensure your success:

1.  Familiarize yourself with the basic office tools:  Word, Excel, PowerPoint, and so on.  An abundance of on-line help is available to start you with these, or to help you "brush up" on your existing knowledge.

1.  This module also assume you are acquainted with the Python programming language, and know [the basics of how to prepare and launch Python programs](https://docs.microsoft.com/en-us/learn/modules/intro-to-python/).

1.  Arrange for Python 3.6:  Another assumption of this module is that you use Python 3.6 or later.  Read on to the following section for details about Python 3.6.

1.  Practice Python's standard package management.  It's good to learn Python's syntax and semantics so you can code ideas.  Almost equally crucial to effective use of Python, though, is familiarity with use of the Python programs _other_ people write.  Read on below for more on modules and packages.


## Python3.6

One consistent assumption of this module is that you use Python 3.6 or later.  [Why 3.6?](https://www.activestate.com/blog/why-python-3-python-you-always-wanted/)  On one hand, all the programs which follow can actually be run under [Python 2.7](https://pythonclock.org/), Python 3.4, and so on, either unchanged, or with very minor adjustments.  I certainly use older versions of Python on a daily basis.  However, your study will make considerably more sense if you focus on the essentials, rather than version-specific details.  In 2019, Python 3.6 is an appropriate standard starting point.  Do yourself a favor, especially if the computer you use builds in an older version:  take a few minutes to [install Python 3.6](https://realpython.com/installing-python/), and save yourselves many-times-over that investment.  Older versions bring difficulties you do well to avoid.

One alternative to installation of Python3.6 (or later) is to use a cloud-based Python.  Think of this as a Python someone else installed, that you access through your Web browser.  [Azure Notebooks](https://blogs.msdn.microsoft.com/uk_faculty_connection/2017/06/10/guide-to-the-microsoft-azure-notebooks-for-students/) and [Python Anywhere](https://www.pythonanywhere.com/) are a couple of at least a half-dozen good cloud-based services you might consider.

[TODO:  Jeff, I have mixed feelings about this section.  In principle, I'd rather refer to the `python.org` or **realpython** sites, or even the Microsoft store, and leave these common instructions to others rather than supplying them here.]

1. If Python 3.6 or higher isn't installed on your computer, go to https://www.python.org/ and install it now. You can determine whether it's installed on Windows by executing the following command in a Command Prompt window:

[TODO with Jeff:  pick consistent formatting for source blocks.]

	```bash
	python --version
	```

	Similarly, you can check to see whether it's installed on macOS or Linux by executing the following command in a terminal:

	```bash
	python3 --version
	```
 
 or perhaps
 
	```bash
	python3.6 --version
	```

If Python is installed, the version number will appear in the output. If you install Python and are asked during the install process whether Python should be added to the system's PATH, answer yes.

	![Adding Python to the PATH](media/add-to-path.png)

	_Adding Python to the PATH_

1. If you are running Windows, execute the following command to install the latest version of `pip`, the Python package manager:

	```bash
	python -m pip install --upgrade pip
	```

	If you are running macOS or Linux, use this command instead:

	```bash
	python3 -m pip install --user --upgrade pip
	```
 
 or
 
```bash
python3.6 -m pip install --user --upgrade pip
```

Older versions of `pip` may miss dependencies needed for the packages this module uses.


## Practice with modules

One specific but distinct aspect of Python work is "[package management](https://packaging.python.org/overview/)".  You might be quite good with the basic Python programming language:  perhaps you're expert at Python's syntax and coding up good solutions to programming problems.  To make the most of Python, you'll also want to be able to use what others have written.  That's the accomplishment of [the Python Package Index](https://pypi.org/) (PyPI).  Consider this example:  the next lesson focuses on **python-docx**, a **package** Industry Analyst Relations Manager [Steve Canny](https://github.com/scanny) wrote "in his spare time" and shares freely.  To use this package in your own programs, you don't have to write all of **python-docx** yourself, or even copy it into your programs.  Instead, Python allows you to

    import docx
    
within your programs, and from then on use the package just as you use the statements and definitions _you_ write.

Almost.

That is, while the _idea_ is that `import` helps you use what someone else wrote just the way you program with your own source, the practice falls slightly short of that idea.  In fact, a few minor differences arise when you use packages others have written.  The most important difference is that, before you can begin to use an outside package, you must **install** it in your Python environment.  The most standard way to install `python-docx` is to execute

    python -m pip install python-docx
    
at a command line.  As so often with computing matters, numerous variations on this theme occur.  In your particular environment, you might have to write

    python3.6 -m pip install python-docx

or

    !pip install <python-docx>

or even something more different.  A great deal of documentation is available online to help you [install Python packages](https://packaging.python.org/tutorials/installing-packages/).  Remember:  in general you install a package in your environment once, then use it an arbitrary number of times in whatever programs you write in that environment by requesting

    import <PACKAGE-NAME>

in the source of your programs.  In the case of `python-docx`, we first install `python-docx`, then use it with

    import docx

You probably noticed that our example module appears under two different names:  we **install** it as `python-docx`, but **import** it as simply `docx`.  The reasons for this are a subject for another day; for now, it's enough to copy the Lessons which follow.


## Virtual environments

The

    python -m pip install python-docx

mentioned above might have a couple of different actions, depending on the configuration of your specific working environment:

* it might install **python-docx** "globally", so that it's visible to any user on your host; or
* it might update only a single Python **virtual environment** (VE).

A majority of my own work is in VEs.  Many readers of this module, though, will just want to get to the **python-docx** result.  For them, a VE is a programming concept off the straight course to the Word automation they seek.

This module is written to apply both with and without a VE.  Why bother with a VE?  Fundamentally, a VE isolates your programming from other configurations on your computer:  you can install a package, for instance, without risk that the latest version of that package will somehow harm the operation of the operating system and its dependencies.  To construct such a Python VE:

1. Create a directory on your hard disk in the location of your choice. This will be the **project directory** and will hold all of the files that make up your applications. It is also where your virtual Python environment will be created.

1. In a Command Prompt window or terminal, `cd` to the project directory. If you are running Windows, use the following commands to create a virtual environment in the "env" subdirectory and activate the environment:

	```bash
	python -m venv env
	env\scripts\activate
	```

	If you are running macOS or Linux, use these commands instead:

	```bash
	python3 -m venv env
	source env/bin/activate
	```

That's all.  Your VE is now active.  Each time you

    python -m pip install <PACKAGE>

during the lifetime of your activated session, the installation will be _specific to your VE_.  Each time you launch

    python <APPLICATION>

Python will know to use the executable and libraries _specific to your VE_.


## Summary

That's it.  If you:

* know the basics of writing and running Python programs;
* have a way to use Python 3.6 or later; and
* understand how to install standard packages in your Python environment,

then you're ready for the lessons that follow.  Let's dig in!
