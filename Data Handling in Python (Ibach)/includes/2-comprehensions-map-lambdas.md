# Comprehensions, maps, and lambdas

In the previous lesson, you learned about sequences and mapping types in Python. Now let's explore [comprehensions](https://medium.com/better-programming/list-comprehension-in-python-8895a785550b), the [map function](https://docs.python.org/2/library/functions.html#map), and [lambda functions](https://www.w3schools.com/python/python_lambda.asp), which make sequences and dictionaries easier to work with. In this lesson, you will learn how to use these features to make code that deals with collections of data simpler and more concise.

## Comprehensions

Comprehensions in Python provide a concise syntax for creating sequences and dictionaries. Suppose you wanted to create a list containing the squares of the numbers 0 through 4. One way to do it is to iterate over a list of numbers, squaring each one and adding the square to a list:

```python
squares = []
for i in [0, 1, 2, 3, 4]:
    squares.append(i ** 2)
```

You could be more concise by using Python's `range()` function:

```python
squares = []
for i in range(5):
    squares.append(i**2)
```

Comprehensions allow the same list to be created using a single line of code:

```python
squares = [i**2 for i in range(5)]
```

The syntax for a list comprehension is:

```python
list_var = [expression(x) for x in iterable]
```

`list_var` is the name of the list to create, `expression(x)` is the operation to perform on the variable `x` during each iteration, and `for x in iterable` is the variable name and the iterable name. An *iterable* is an object you can iterate over, meaning you can enumerate all of its items. Lists and strings are both examples of iterable objects. `range()` returns an iterable object, too, although the type of that object differs in Python 2 and Python 3.

You can also use conditional statements in a comprehension to filter which values are included in the new list. The following exammple filters the list to only include squares of even numbers:

```python
squares = [i**2 for i in range(5) if i % 2 == 0]
```

In Python 3, comprehensions can also be used to create dictionaries. The following example takes a dictionary containing lowercase airport codes and city names and creates a new dictionary. In the new dictionary, airport codes are uppercase, and city names are capitalized:

```python
airports = {'sea':'seattle', 'hou':'houston','ord':'Chicago'}
upper_airports = {code.upper():city.capitalize() for code, city in airports.items()}
print(upper_airports) # outputs : {'SEA': 'Seattle', 'HOU': 'Houston', 'ORD': 'Chicago'}
```

Comprehensions that create dictionaries may also include conditional statements, just like comprehensions that create lists.

## Map

The `map` function is also useful when working with data. It applies a function to all the items in the list.

The syntax of the map function is:
```python
map(function, iterable)
```

Similar to what you did with comprehensions you can use the map function to create new lists.

The following code declares a function called *double* which returns double the value passed in as a parameter. The map function calls your function to double all the values in a list:

```python
def double(value):
    return value*2

nums = [1,2,3,4,5]
doubles = map(double, nums)
print(list(doubles)) # outputs : [2, 4, 6, 8, 10]
```
>You may have noticed a call to the `list` function in the print statement. Because the map function returns a map object, you must use the list function to convert it to a list.

## Lambda functions

Anywhere you use a named function you can also use lambda functions. Lambda functions are small anonymous functions. They can accept any number of arguments, but can only have one expression. 

The syntax for lambda functions is:
```python
lambda arguments : expression
```
- *arguments* are the parameters passed to the lambda function.  
- *expression* is the expression to operate on the parameters.  

The following lambda doubles the value passed to the function:
```python
double = lambda x: x * 2
print(double(4)) # outputs : 8
```

Lambdas can be used instead of functions in your code. For example, you can make your code with the map function more concise by using a lambda instead of a named function to double the values in the input list:

```python
nums = [1,2,3,4,5]
doubles = map(lambda x: x*2, nums)
print(list(doubles)) # outputs : [2, 4, 6, 8, 10]
```

Now you know the basics of lists, strings, dictionaries, comprehensions, map, and lambda expressions in Python. In the next lesson, you'll create an Azure Notebook so you can start writing and executing Python code to manipulate the airline data.  
**Next unit: [Creating an Azure Notebook](3-Creating-Azure-Notebook.md)**