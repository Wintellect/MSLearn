# Comprehensions and lambdas

In the previous lesson, you learned about sequences and dictionaries in Python. Now let's explore [comprehensions](https://medium.com/better-programming/list-comprehension-in-python-8895a785550b) and [lambda functions](https://www.w3schools.com/python/python_lambda.asp), which make sequences and dictionaries — especially sequences — easier to work with. In this lesson, you will learn how to use comprehensions, map, and lambda functions (also known as *anonymous functions*) to make code that deals with collections of data simpler and more concise.

## Comprehensions

Comprehensions in Python provide a concise syntax for creating sequences, especially lists. Let's take a look at list comprehensions.

A list comprehension in Python is created using the following syntax:
```python
list_var = [expression(x) for x in iterable]
```

*list_var* is the name of the list to create.  
*expression(x)* is the operation to perform on the variable for each element.  
*for x in iterable* is the element name and the iterable object name.  

It might be easier to understand if we see the equivalent code as a loop:
```python
for x in iterable:
    list_var.append(expression(x))
```

>An *iterable* is an object you can iterate over, meaning you can traverse through all the values. Lists, and strings are examples of iterable objects.  

You can use comprehensions to create new lists. The following code uses the `range` function as the iterable to create a list containing the squares of the numbers 0 through 4:

```python
squares = [num**2 for num in range(5)]
print(squares) # outputs : [0, 1, 4, 9, 16]
```

By specifying an existing list as an iterable, you can create a new list based on the content of the original list. 

The following code creates a new list called squares containing the squares of the values in the nums list:
```python
nums = [1,2,3,4,5]
squares = [num**2 for num in nums]
print(squares) # outputs : [1, 4, 9, 16, 25]
```

Again, this may be easier to understand if you see the equivalent code in a loop:
```python
nums = [1,2,3,4,5]
squares = []
for num in nums:
    squares.append(num**2)     
print(squares) # outputs : [1, 4, 9, 16, 25]
```
You can add conditional statements to a comprehension to filter which values are included in the new list:

```python
list_var = [expression(x) for x in iterable if condition]
```

The following code filters the list to only include squares of even numbers in the new list:
```python
nums = [1,2,3,4,5]
even_nums = [num**2 for num in nums if num % 2 == 0]
print(even_nums) # outputs : [4, 16]
```

Comprehensions can also be used on dictionaries using the syntax:
```python
dict_var = {expression(key): expression(value) for (key, value) in iterable}
```

In order to use a comprehension on a dictionary you must use the *items* operation to treat the dictionary as an iterable object.

The following code takes a dictionary containing airport codes and cities all in lowercase and creates a new dictionary. In the new dictionary, the airport codes are converted to uppercase, and the city names are capitalized:
```python
airports = {'sea':'seattle', 'hou':'houston','ord':'Chicago'}
upper_airports = {code.upper():city.capitalize() for (code,city) in airports.items()}
print(upper_airports) # outputs : {'SEA': 'Seattle', 'HOU': 'Houston', 'ORD': 'Chicago'}
```
## Map
The `map` function is also useful when working with data. It applies a function to all the items in the list.

The syntax of the map function is:
```python
map(function, iterable)
```

Similar to what we did with comprehensions we can use the map funciton to create new lists.

The following code declares a function called double, then uses the map function to double all the values in a list:

```python
def double(value):
    return value*2

nums = [1,2,3,4,5]
doubles = map(double, nums)
print(list(doubles)) # outputs : [2, 4, 6, 8, 10]
```
Because the map function returns a map object, we use the `list` function to convert it to a list.

## Lambda functions

Anywhere you use a named function you can also use lambda functions. Lambda functions are small anonymous functions. They can accept any number of arguments, but can only have one expression. 

The syntax for lambda functions is:
```python
lambda arguments : expression
```
*arguments* are the parameters passed to the lambda function.  
*expression* is the expression to operate on the parameters.  

The following lambda doubles the value passed to the function:
```python
double = lambda x: x * 2
print(double(4)) # outputs : 8
```

Lambdas can be used instead of functions in our code. For example, we can make our code with the map function more concise by using a lambda instead of a named function to double the values in the input list:

```python
nums = [1,2,3,4,5]
doubles = map(lambda x: x*2, nums)
print(list(doubles)) # outputs : [2, 4, 6, 8, 10]
```

Now you know the basics of lists, strings, dictionaries, comprehensions, map, and lambda expressions in Python. In the next lesson, you'll put this knowledge to work using a dataset stored in a CSV file.