# Using lambdas and comprehensions

Lambdas and comprehensions are two very useful syntax features for writing more readable Python code while eliminating some syntax and unneeded lines of code. Lambdas allow the creation of single expression functions which can be assigned to variables or defined inline and passed directly as arguments to other functions.

Comprehensions are terse syntax for performing iteration operations over a collection-type object (lists, sets and dictionaries) and performing some kind of transformation and filtering of the data and returning a new collection-type object. Often, comprehensions can be used as an alternative to `for-in` loops that produce new collections (such as lists) and/or combinations of `map` and `filter` functions. In this module, list and dictionary comprehensions are explored. Set comprehensions are not covered as sets are not covered in this module.

## Lambdas Exercise

1. Create a new Jupyter notebook named 'Lambdas and Comprehensions Exercise' in Azure Notebooks.

2. In the first cell, add the following code.

```python
def double(n):
  return n * 2

nums = [1,2,3,4]

double_nums = list(map(double, nums))

print(double_nums) # outputs: [2, 4, 6, 8]
```

1. The `double` function can be changed to a lambda because it is a single expression. Change the `double` function code in the first cell to look like this.

```python
double = lambda n: n * 2
```

Run the cell and verify the same results as before.

1. To simplify this even more the `lambda` function can be moved to the `map` function call. Update the code in the cell to look like this, and run the cell.

```python
nums = [1,2,3,4]

double_nums = list(map(lambda n: n * 2, nums))

print(double_nums) # outputs: [2, 4, 6, 8]
```

Run the cell and ensure the output is the same. Lambda functions are great for reducing code when the function itself is a single expression. If a code block is needed for the function then a normal `def` function definition is needed.

## List Comprehensions Exercise

1. If not already open, open the same notebook you created for the lambdas exercise.

1. The code in the first cell is using a `map` function with a `lambda` function to perform the double transformation. The result of the `map` function call is a `map` object type which needs to be converted to a `list` type. This code can be simplified using a list comprehension.

Modify the code in the first cell to look like this, and run the cell.

```python
nums = [1,2,3,4]

double_nums = [ num * 2 for num in nums ]

print(double_nums) # outputs: [2, 4, 6, 8]
```

Instead of a call to `map` and the `lambda` function definition, a list comprehension was used. A list comprehension is surrounded with square brackets. Within the square brackets a `for-in` structure is used to perform the iteration. The expression which transforms the value is placed **before** the `for` statement. If the transformation requires more than a single expression then a function can be called from here.

1. In addition to a transformation expression, a filtering conditional expression can be applied too. Modify the code in the cell to look like this, and run the cell.

```python
nums = [1,2,3,4]

double_nums = [ num * 2 for num in nums if num % 2 == 0 ]

print(double_nums) # outputs: [4, 8]
```

Only even numbers (2 and 4) will be passed to the transformation function and included in the new list.


## Dictionary Comprehensions Exercise

1. If not already open, open the same notebook you created for the list comprehension exercise.

1. Dictionary comprehensions are similar to list comprehensions except a dictionary is returned instead of a list. The same `for-in` structure is used, conditionals can be applied, and the result of the transformation expression needs to be colon separate key/value pair. The result of the dictionary comprehension is new dictionary. In a new cell at the end of the notebook add the following code, and run the cell.

```python
countries = {
    'US': ( 'United States', 'North America' ),
    'CA': ( 'Canada', 'North America' ),
    'UK': ( 'United Kingdom', 'Europe' ),
    'FR': ( 'France', 'Europe' ),
    'CN': ( 'China', 'Asia' ),
    'IN': ( 'India', 'Asia' )
}
    
north_american_countries = {
    country_code: countries[country_code]
    for country_code in countries
    if countries[country_code][1] == 'North America' }

print(north_american_countries)
```

The output is new dictionary consisting of only the countries in North America. Observe that curly braces instead of square brackets are used to wrap the comprehension. The `country_code` is key to the `countries` dictionary. If the was was not needed the `values` function could be used on the `countries` variable following the `in` statement.

## Airline Data Exercise: Convert the Airport and State Dictionaries to Classes

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this third exercise within the module, the airport and state dictionary structures will be converted to classes.

1. Open the Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks. You may want to make a duplicate copy of this notebook before attempting this exercise.

2. The second cell should have the following code:

```python
def do_strip(x):
    return x.strip()

def split_strip(value, split_value = ','):
  return tuple(map(do_strip, value.split(split_value)))
```

Instead of defining `do_strip` as normal function definition, the code can be simplified to use a lambda function. Modify the code within the cell to look like this.

```python
def split_strip(value, split_value = ','):
  return tuple(map(lambda x: x.strip(), value.split(split_value)))
```

Run the entire notebook and ensure the same results are achieved as before. The output for the state and airports length should be 67 and 6510, respectively.

1. In the second cell, another change which could be made is to change the `map` and `lambda` function to a list comprehension. Modify the code within the cell to look like this.

```python
def split_strip(value, split_value = ','):
  return tuple([ x.strip() for x in value.split(split_value) ])
```

The list comprehension combines aspects of a `map` and `lambda` function to provide an easier to read syntax.

Run the notebook, and ensure the results are the same.
