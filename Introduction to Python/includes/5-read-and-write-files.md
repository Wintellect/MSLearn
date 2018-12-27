# Read and write files

Computer programs are composed of code and data. Variables are used to store data, control flow structures apply logic to the data and method/functions are used to organize logic. Typically, data for computer programs come from external sources including databases, the file system and over computer networks such as downloading a web page.

To open a file from the file system in Python the open function is used. The open function's first two parameters are the file name path and the mode for opening the file. Files can be opened in one of many modes such as read, write, and append. The read, write, and append modes are specified with one of the following string values:

Modes
- read: 'r'
- write: 'w'
- append: 'a'

There are additional modes beyond these, but they are outside the scope of this course.

Files can contain binary or text data. Binary data is very common for operating system files and executable programs. Occasionally, some applications will store their data in a binary format especially for data such as images, sound, video, and other media data.

Most non-media files containing data used for data science and machine learning will be stored as text and usually in a format such as comma-delimited or tab-delimited. In fact, delimited files are so common that popular Python data manipulation libraries such **pandas** can process delimited files natively making it much easier to work with such data in Python applications. In this module, the focus is on reading and writing files using Python-only (no additional packages).

### Writing to a File

Add content here...

```python
colors = ['red','green','blue']

color_file = open('./colors.txt', 'w')

for color in colors:
    color_file.write(color + '\n')
    
color_file.close()
```

Add content here...


```python
colors = ['red','green','blue']

with open('./colors.txt', 'w') as color_file:

    for color in colors:
        color_file.write(color + '\n')
```

### Reading from a File

```python
colors = []

with open('./colors.txt', 'r') as color_file:
    
    for color_data in color_file:
        color = color_data.rstrip()
        
        colors.append(color)

print(colors)
```

### Appending to a File

```python
new_colors = ['orange','yellow','purple']

with open('./colors.txt', 'a') as color_file:
    
    for color in new_colors:
        color_file.write(color + '\n')
        
colors = []
        
with open('./colors.txt', 'r') as color_file:
    
    for color_data in color_file:
        color = color_data.rstrip()
        
        colors.append(color)

print(colors)
```

### Writing Python Programs for Multiple Operating Systems

As mention in the introduction, Python runs on most operating systems. While the execution of most Python code on various operating systems behaves exactly the same, from time-to-time, specials considerations specific to the operating system must be taken into account. Two such considerations are line endings and the default character encoding for text files.

Microsoft Windows uses two characters for line endings "\r\n" and Unix-variant systems such as Apple's macOS and Linux (all distros) use a single character "\n" for line endings. When writing Python applications it can be important to make note of this difference. When writing code which writes to a file only the new line character '\n' should be written regardless of the operating system. Python will translate the new line character into the appropriate line ending depending upon the operating system being used.

To determine the line ending used by the operating system, import the **os** module and observe the value returned by **linesep**:

```python
import os

os.linesep
```

Do not use **os.linesep** when writing files as the Python language takes care of performing line ending translation for you.

Another important consideration is character encoding. Computers represent a character as a number. The number specifies a character in a look-up table. Specifying the character encoding is specifying which character lookup table is being used. Different tables have different purposes. In the early days of computing, a common encoding was the ASCII encoding. As computing became more internationalized more characters were needed so a new encoding called Unicode was created. Unicode comes in several flavors depending upon the number of characters which need to be supported within an application. The more characters supported by the look-up table the more memory and drive space the characters take.

For example, web pages typically use UTF-8 while operating systems typically use UTF-16. Diving into the details of different encodings is outside the scope of this tutorial other than to say that Python will use the preferred encoding determined by the local environment for writing files. For most systems, this will be UTF-8.

When reading and writing files the character encoding (also known as file encoding) can be explicitly set (if needed) when opening the file.

```python
colors = ['red','green','blue']

with open('./colors.txt', 'w', encoding='utf-8') as color_file:

    for color in colors:
        color_file.write(color + '\n')
```

The default encoding for reading files is determined by the file. The default encoding for writing files is determined by the result of the **locale.getpreferredencoding** function.

```python
import locale

print(locale.getpreferredencoding())
```

### Exercise: Saving Airport Data for a US State to a File

**Step 1.** Start here...
