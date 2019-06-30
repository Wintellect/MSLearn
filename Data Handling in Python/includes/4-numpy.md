# NumPy

One of the most compelling reasons to use Python is the sheer number of libraries available. [NumPy](https://www.numpy.org/) is one of those libraries — one that is purpose-built for scientific computing. It offers Python programmers a rich multidimensional array object that is more performant than Python lists and requires substantially less memory, especially when dealing with very large arrays. It also includes functions for performing fast mathematical operations on array elements, computing [Fourier transforms](https://en.wikipedia.org/wiki/Fourier_transform), and changing an array's dimensions. It even has support support for reading CSV files. NumPy is licensed under the [BSD license](https://www.numpy.org/license.html#license), enabling it to be used with few restrictions.

For an excellent overview of *whys* of using NumPy and NumPy arrays, see [A hitchhiker guide to python NumPy Arrays](https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121). For now, let's focus our attention on the *hows*.

## Working with NumPy arrays

The most common way to create a NumPy array is to use NumPy's `array()` function. The following code imports NumPy and creates an array containing airport codes and cities:  

```python
import numpy as np

airports = np.array(['SEA', 'Seattle', 'HOU', 'Houston', 'BOS', 'Boston'])
print(airports) # outputs: ['SEA' 'Seattle' 'HOU' 'Houston' 'BOS' 'Boston']
```

The `shape` attribute returns the dimensions of the array. This array contains six rows and one column, making it a 6x1 array: 

```python
print(airports.shape) # outputs: (6,)
```

One of the most useful NumPy array functions is `reshape()`, which changes the dimensions of an array. You can reshape the `airports` array to make it three rows and two columns:  

```python
airports = airports.reshape(3, 2)
print(airports)
```

The output is:

```
[['SEA' 'Seattle']
 ['HOU' 'Houston']
 ['BOS' 'Boston']]
```

You can iterate over the items in a NumPy array the same way you iterate over lists:  

```python
for value in airports:
    print(value)
```

And just like Python lists, NumPy arrays can be sliced:

```python
print(airports[2,0]) # outputs: BOS
print(airports[2])   # outputs: ['BOS' 'Boston']
print(airports[:,1]) # outputs: ['Seattle' 'Houston' 'Boston']
```

One functional difference between Python lists and NumPy arrays is that the latter are *homogeneous*. A Python list, for example, can contain integers and strings. A NumPy array can contain integers *or* strings, but it cannot contain both. You can determine what type of data an array holds by reading the array's `dtype` attribute. Similarly, the `nbytes` attribute tells you how much memory an array and all of its elements consume, which can be useful when comparing to the memory consumed by Python lists.

## Operating on NumPy arrays

NumPy provides functions and operators to simplify code that performs mathematical operations on array elements. The following example adds 1 to every item in an array:

```python
lets_do_math = np.array([[1, 2], [3, 4], [5, 6]])
print(lets_do_math + 1)
```

Here's the output:

```
[[2 3]
 [4 5]
 [6 7]]
```

The next example applies the expression `< 3` to each item in the array:

```python
print(lets_do_math < 3) 
```

And here, once more, is the output:

```
[[ True  True]
 [False False]
 [False False]]
```


Finally, this example multiplies by 2 every item in the array:

```python
print(lets_do_math[2] * 2) 
```

NumPy arrays also support operations such as calculating the sum, minimum, maximum, or mean of all the values in an array or array slice:

```python
print(lets_do_math.sum()) # outputs: 21
print(lets_do_math.min()) # outputs: 1
print(lets_do_math[2].max()) # outputs: 6
print(lets_do_math[:,0].mean()) # outputs: 3
```

`sum()`, `min()`, `max()`, and `mean()` are but a few of the many functions you can call on an array. For a complete list, see the documentation for the `ndarray` data type at https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.ndarray.html.

## Reading data from CSV files

NumPy contains a handy function named [genfromtxt()](https://www.numpy.org/devdocs/user/basics.io.genfromtxt.html) for reading CSV files into NumPy arrays. Suppose you have a data file named **airports.csv** that contains the following text:

```csv
Code,City
HOU,Houston
ABQ,Albuquerque
BWI,Baltimore
```

The following statement loads the contents of **airports.csv** into a NumPy array:

```python
airports = np.genfromtxt('airports.csv', delimiter=',', dtype=None, encoding=None, skip_header=1)
```

The first parameter is the path to the CSV file. The second is the delimiter that separates items in the CSV file. If you were reading a tab-delimited (TSV) file, you would modify the `delimiter` parameter as follows:

```python
airports = np.genfromtxt('airports.tsv', delimiter='\t', dtype=None, encoding=None, skip_header=1)
```

The combination of `dtype=None` and `encoding=None` instructs `genfromtxt()` to infer data types, which is slower than specifying a data type but produces more intuitive behavior, especially if the data file contains a mix of strings and numbers. Finally, `skip_header=1` tells `genfromtext()` to skip one header line — the line containing column names.

`genfromtxt()` supports other useful parameters as well. For example, if strings in the data file have leading or trailing spaces, specifying `autostrip=True` automatically removes leading and trailing whitespace:

```python
airports = np.genfromtxt('airports.csv', delimiter=',', dtype=None, encoding=None, skip_header=1, autostrip=True)
```

`genfromtext()` has a counterpart named [`savetxt()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html) that saves the contents of a NumPy array to a CSV file, TSV file, or other text file.

### Working with column names

By default, NumPy arrays created with `genfromtext()` do not have column names. You can specify names with the `names` parameter:

```python
airports = np.genfromtxt('airports.csv', delimiter=',', dtype=None, encoding=None, skip_header=1, names=('Code', 'City'))
print(airports[0]['Code']) # outputs: HOU
```

Or, if the header line contains column names, you can use `names=True` to use those:

```python
airports = np.genfromtxt('airports.csv', delimiter=',', dtype=None, encoding=None, names=True)
print(airports[0]['Code']) # outputs: HOU
```

It is not unusual for data files to contain many more columns than you are interested in. You can specify which columns to load from a data file with the `usecols` parameter:

```python
airports = np.genfromtxt('airports.csv', delimiter=',', dtype=None, encoding=None, names=True, usecols=('Code', 'City'))
```

You can use column indexes instead, which is handy if the columns don't have names:

```python
airports = np.genfromtxt('airports.csv', delimiter=',', dtype='str', skip_header=1, usecols=(0, 1))
```

Now that you know the basics of NumPy arrays, you have another tool for manipulating data like a pro in Python. Let's put this knowledge to work gathering some basic statistics from a dataset containing information about flight delays.