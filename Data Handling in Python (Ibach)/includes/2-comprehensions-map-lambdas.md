# Comprehensions, maps, and lambdas

In the previous lesson, you learned about sequences and mapping types in Python. Now let's explore [comprehensions](https://medium.com/better-programming/list-comprehension-in-python-8895a785550b), the [`map()` function](https://docs.python.org/3/library/functions.html#map), and [lambda functions](https://www.w3schools.com/python/python_lambda.asp), which make sequences and dictionaries easier to work with.

## Comprehensions

Comprehensions in Python provide a concise syntax for creating sets of data, especially lists. Suppose you wanted to create a list containing the squares of the numbers 0 through 4. One way to do it is to iterate over a list of numbers, squaring each one and adding the square to a list:

```python
squares = []
for i in [0, 1, 2, 3, 4]:
    squares.append(i**2)
```

Comprehensions allow the same list to be created using a single line of code:

```python
squares = [i**2 for i in [0, 1, 2, 3, 4]]
```

The general syntax for a list comprehension is:

```python
[expression(x) for x in iterable if condition]
```

`expression(x)` is the operation to perform on the variable `x` during each iteration, `for x in iterable` specifies the variable name and the iterable name, and `if condition` is an optional conditional expression used to filter values accessed through the iterable. An *iterable* is an object you can iterate over, meaning you can enumerate all of its items. Lists and strings are both examples of iterable objects.

The following example uses a conditional expression to filter the list to only include squares of even numbers:

```python
squares = [i**2 for i in range(5) if i % 2 == 0]
```

In Python 3, comprehensions can also be used to create dictionaries. The following example takes a dictionary containing lowercase airport codes and city names and creates a new dictionary. In the new dictionary, airport codes are uppercase, and city names are capitalized:

```python
airports = {'sea':'seattle', 'hou':'houston', 'ord':'Chicago'}
upper_airports = {code.upper():city.capitalize() for code, city in airports.items()}
print(upper_airports) # outputs: {'SEA': 'Seattle', 'HOU': 'Houston', 'ORD': 'Chicago'}
```

Comprehensions that create dictionaries may also include conditional statements, just like comprehensions that create lists.

## The `map()` function

Python's `map()` function is also useful when working with data. It applies a function to all the items in an iterable. The syntax of the `map()` function is as follows:

```python
map(function, iterable)
```

The following code declares a function named `double()` that returns double the value passed in as a parameter. Then it uses the `map()` function to double all the values in a list:

```python
def double(value):
    return value*2

nums = [1, 2, 3, 4 ,5]
doubles = map(double, nums)
print(list(doubles)) # outputs: [2, 4, 6, 8, 10]
```

Why is the `list()` function called in the `print` statement? In Python 2, `map()` returns a list, but in Python 3, it returns a `map` object. The `list()` function creates a list from the `map` so `print()` can print its contents.

## Lambda functions

Lambda functions are small anonymous functions. *Anonymous* means lambda functions do not have names as conventional functions do. The syntax for lambda functions is:

```python
lambda arguments : expression
```

A lambda function can accept any number of arguments, but can only have one expression. The following example defines a lambda function that accepts a single argument (`x`) and returns twice the value of `x` passed to it:

```python
lambda x: x * 2
```

Lambdas let you simplify your code by defining simple functions inline. For example, you could rewrite the code from the previous section that calls `double()` from the `map()` function this way:

```python
nums = [1, 2, 3, 4, 5]
doubles = map(lambda x: x*2, nums)
print(list(doubles)) # outputs: [2, 4, 6, 8, 10]
```

Python offers a rich assortment of data structures and language features for dealing with those data structures. Let's put some of these to work before diving into data-handling libraries.