# Set up a development environment

The first order of business is to set up a Python development environment. If you are running Linux or macOS, Python is probably already installed on your computer. If you use Windows, Python might need to be installed. Regardless of which operating system you use, if Python is installed, you might need to update it because the exercises in this module require Python 3.6. or higher.

You also need to decide whether to set up a [virtual Python environment](https://docs.python.org/3/library/venv.html) to isolate the packages you install, or run Python "on the metal" and install packages such as [Python-docx](https://python-docx.readthedocs.io/en/latest/) and [PyPDF4](https://pypi.org/project/PyPDF4/) globally. The advantage to the former is that installing new packages doesn't affect other packages you've installed. There's nothing worse than running through a set of learning exercises, only to find out later that Python apps that have been working flawlessly suddenly don't work any more.

## Install Python

Let's begin by making sure Python 3.6 or higher is installed on your computer.

1. If Python 3.6 or higher isn't installed on your computer, go to https://www.python.org/ and install it now. You can determine whether it's installed on Windows by executing the following command in a Command Prompt window:

	```bash
	python --version
	```

	Similarly, you can check to see whether it's installed on macOS or Linux by executing the following command in a terminal:

	```bash
	python3 --version
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

Finish up by using a `python --version` or `python3 --version` command to make sure Python is installed and that it has been added to the PATH.

## Set up a virtual Python environment (optional)

You should now be able to execute Python 3 code and install Python 3 packages on your computer. You can optionally go a step further and create a virtual Python environment for working the exercises in this module. Doing so prevents the packages you install from potentially interfering with packages that are already installed. Here's how to set up a virtual environment.

1. Create a directory on your hard disk in the location of your choice. This is where your virtual Python environment will be created.

1. In a Command Prompt window or terminal, `cd` to the directory you created in the previous step. If you are running Windows, use the following commands to create a virtual environment in the "env" subdirectory and activate the environment:

	```bash
	python -m venv env
	env\scripts\activate
	```

	If you are running macOS or Linux, use these commands instead:

	```bash
	python3 -m venv env
	source env/bin/activate
	```

1. Confirm that the text "(env)" appears next to the command prompt. This indicates that the virtual environment is active.

When you use `pip` to install Python packages, the installs will be local to the virtual environment as long as the virtual environment is active. In addition, Python programs that are executed while the virtual environment is active will use the packages installed in the virtual environment rather than packages that are installed globally.