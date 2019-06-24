## Create a notebook

The first order of business is to create a new Azure Notebook to run your Python code. Azure Notebooks are contained in libraries whose primary purpose is to group related notebooks. In this unit, you'll create a new project with a notebook and write some Python code. 

1. Navigate to https://notebooks.azure.com  in your browser.
2. Sign in using your Microsoft account.
3. Click My Projects in the top menubar.

4. Click + **New Project**. Enter "Airline information" (without quotation marks) for the project name and "airline-information" as the project ID. Uncheck the **Public project** box, and select **Create**.

5. Select the + sign to add a notebook to the project.

Name the notebook "airport_information.ipynb" and select Python 3.6 Notebook as the language. This will create a notebook with a Python 3.6 kernel. One of the strengths of Jupyter notebooks is that you can use different languages by choosing different kernels.

You can create additional projects and notebooks as you work with Azure Notebooks. Projects provide a means for grouping related notebooks. You can create notebooks from scratch, or upload existing notebooks. 

Select your notebook to open it.

## Writing code in your notebook
Jupyter notebooks are composed of cells. Each cell is assigned one of three types:
**Markdown** for entering text in markdown format
**Code** for entering code that runs interactively
**Raw NBConvert** for entering data inline

Code entered into code cells is executed by a kernel, which provides an isolated environment for the notebook to run in. 

1. In the first cell, set the cell type to **Markdown** and enter "Sequences" into the cell itself:

2. Select the + button in the toolbar to add a new cell. Make sure the cell type is Code, and then enter the following Python code into the cell:
```python
x = 5
print(x)
```

3. Now click the *Run* button to run the code cell. You will see the output of the print statement displayed beneath the code cell.

## Work with lists

In this exercise you will create and manage a list that contains the names of cities with airports served by your airline. 

### Create a list

The airline currently serves only five cities: Seattle, Dallas, Detroit, Houston, and Boston. You need to keep track of the city names in your code so you decide to create a list object. 

1. Add a new markdown cell and enter "Create a list".
2. Add a new code cell and write Python code to create a list called cities that contains the names of the cities served by the airline.
3. Add Python code to print the cities list.
4. Run the code. You should see the output:
```python
['Seatte', 'Dallas', 'Detroit', 'Houston', 'Boston']
```
### Add a new city to the list

The airline has added Nashville to the cities served and removed Dallas. You need to update the list of cities to reflect the changes. 
1. Add a new markdown cell and enter "Update list".
2. Add a new code cell and write Python code to add the city Nashville to the cities list.
3. Add code to remove the city Dallas from the list.
4. Add code to print the cities list.
5. Run the code. You should see the output:
```python
['Seatte', 'Detroit', 'Houston', 'Boston', 'Nashville']
```

## Comprehensions
The airline has a code for each city. The code is the first three letters of the city name. You need to keep track of the city codes. Create a city codes list from the city list using comprehensions.
1. Add a new markdown cell and enter "Create a city codes list with comprehensions".
2. Add a new code cell and write a Python comprehension to iterate through the cities list. For each city extract the first three letters and store the result in a list called city_codes.
3. Add code to print the city_codes list.
4. Run the code. You should see the output:
```python
city_codes = [name[0:3] for name in cities]
print(city_codes)
```

## lambda 
It turns out that city codes must be in uppercase letters. You need to create a new list to store city codes all in uppercase. Use the map function and a lambda to create a list called city_codes_uppercase from the cities list.
1. Add a new markdown cell and enter "Create an uppercase city codes list with map and a lambda".
2. Add a new code cell and use the map function to iterate through the cities list and use a lambda to convert the city name to uppercase and extract the first three letters of the city name. Store the result in a list called city_codes_uppercase.
3. Add code to print the cities list.
4. Run the code. You should see the output:
```python
['SEA', 'DET', 'HOU', 'BOS', 'NAS']
```