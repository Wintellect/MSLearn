# Working with Notebooks

To try out your skills, you need to create a new Azure Notebook to run your Python code. Azure Notebooks are contained in libraries whose primary purpose is to group related notebooks. In this unit, you'll create a new project with a notebook and learn how to add and run Python code.

## Create an Azure Notebook
1. Navigate to [https://notebooks.azure.com](https://notebooks.azure.com)  in your browser.
2. Sign in using your Microsoft account.
3. Click **My Projects** in the top menubar.   
![Go to projects](media/CreateAzureNotebookProject.png)  
4. Click + **New Project**. Enter "Airline information" (without quotation marks) for the project name and "airline-information" as the project ID. Uncheck the **Public** box, and select **Create**.  
![Create new project](media/CreateNewProject.png)   
5. Select the **+** sign to add a notebook to the project.  
![Create Azure Notebook](media/CreateNotebook.png)   
Name the notebook "airport_information.ipynb" and select *Python 3.6* as the language. This will create a notebook with a Python 3.6 kernel. One of the strengths of Jupyter notebooks is that you can use different languages by choosing different kernels.  
![Name Azure Notebook](media/NameNotebook.png)  
You can create additional projects and notebooks as you work with Azure Notebooks. Projects provide a means for grouping related notebooks. You can create notebooks from scratch, or upload existing notebooks. 

6. Select your notebook to open it.

## Writing and executing code in your notebook
Jupyter notebooks are composed of cells. Each cell is assigned one of three types:  
- **Markdown** for entering text in markdown format.  
- **Code** for entering code that runs interactively.  
- **Raw NBConvert** for entering data inline.  

1. In the first cell, set the cell type to **Markdown** and enter "Airport information" into the cell itself:  
![Add markdown](media/AddMarkdown.png) 
Markdown cells are used to document your notebooks.  

2. Select the **+** button in the toolbar to add a new cell. Set the cell type to **Code**, and enter the following Python code into the cell to create and print a list of airport codes:
    ```python
    airport_codes = ['SEA','DTW','HOU','BOS']
    print(airport_codes)
    ```
    ![Add Python code in code cell](media/AddCodeCell.png)  

3. Now select the **Run** button to run the code cell. Code entered into code cells is executed by a kernel, which provides an isolated environment for the notebook to run in.  You will see the output of the code displayed beneath the code cell.  
![Execute Python code in code cell](media/RunCodeCell.png)

You can add additional code cells to execute additional python code as needed and add additional markdown cells to document your notebook.  

Congratulations, you have created a notebook and executed Python code. You can use notebooks throughout the rest of the units to try out everything you learn. In the next lesson you will learn how to use the NumPy library to work with data.  

**Next unit: [Numpy](numpy.md)**
