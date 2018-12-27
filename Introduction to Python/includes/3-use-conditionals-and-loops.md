# Use conditionals and loops to control flow

To get started with control-flow structures in Python some data is needed. For this module, data from the United States Bureau of Transportation Statistics (BTS) will be used. The BTS provides flight data on domestic US flights provided by major US air carriers. In this module, flight data from flights in Virginia in October 2018 will be used. Serious analysis of the data will not be performed, but the data will be used to explore the various control flow structures in Python. Python supports several control flow structures: conditionals, loops and error handling.

To get started with the data, it first needs to read in from a file. To open a file in Python the open method is used. The open method has two parameters: the filename path and the mode for opening the file. Files can be opened in one of four modes: read, write, append or read/write. The mode is specified with one of the following string values:

The following is a Python example of how to open the lookup table file for airport codes using the open method:

```python
airport_file = open('./L_AIRPORT.csv', 'r')
```

Once the file is opened, data can be read from it. There are several ways to access the data, but one good is to iterate (loop) over the file contents reading one line at a time. To do this, Python's **for-in** loop can be used. The **for-in** loop will iterate over anything which is iterable (such as a sequence) and will return some data on each iteration (loop).

Here is some code demonstrating how to use a for-in loop to read each line of the **airport_file** file.

```python
for line in airport_file:
  print(line)
```

The **airport_file** is the object which is iterated over, and each line of data from the file is assigned to the **line** variable. When the end of the file is reached the **for-in** loop stops. Loop control-flow structures repeat a block of code over and over again based upon some condition such as the number of items or conditional expression.

When a file is no longer needed, the file resource object needs to be closed to release the resource. The following code closes the file and releases the resource:

```python
airport_file.close()
```

Closing the file is extremely important to properly free up operating system resources.

There are two kinds of loops in Python: **for-in** loops and **while** loop. The **for-in** loop iterates over each item in a collection of data. The **while** loop iterates while its conditional expression evaluates to true.

Using the **range** function, a list of numbers can be easily created. The **range** function allows a start and end number to be specified. If only one number is specified, the start is 0 and the end is the specified number minus 1. The following **range** will produce a list of numbers 0 to 9. Lists are mutable sequences; therefore, they can be iterated over as all sequences are iterable.

```python
nums = range(10)
for x in nums:
  print(x)
```

The above code will output:

```python
0
1
2
3
4
5
6
7
8
9
```

The second loop structure is the while loop. The while loop evaluates a conditional expression and loop as long as expression returns a true or truthy value.

```python
x = 0
while x < 10:
  print(x)
  x = x + 1
```

The above code will output:

```python
0
1
2
3
4
5
6
7
8
9
```

In this example, the variable x will be decremented by 1 until it reaches 0. In Python, 0 is a falsy value; therefore, the loop will stop when it gets to 0.

```python
x = 10
while x:
  print(x)
  x = x - 1
```

The above code will output:

```python
10
9
8
7
6
5
4
3
2
1
```

In addition to repeating code, control flow structures can control which code is executed next based upon some kind of condition. The condition is simply an expression which returns a truthy or falsy value. If the condition is truthy the code is executed if the condition is falsy, the code is not executed or an alternative code block is executed.

#### Exercise: Importing Airport Data

**Step 1.** Start here...

