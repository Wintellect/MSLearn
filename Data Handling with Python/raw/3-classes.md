# Connect data and code with classes

Python is a multi-paradigm language. It supports structured coding which is independent functions and data. This has been the paradigm used thus far. It supports aspects of functional programming as well. Example of this are using functions like `map` and `filter` with lists. While true functional programming is much more than a `map` function, there are still hints of functional programming in Python. Another major supported paradigm is object oriented programming including classes and classical inheritance. Unlike languages such as Java and C#, Python programs do not have to use classes, but they are fully supported and most larger Python applications utilize them.

## Object-Oriented Programming

Object-oriented programming is known for three qualities:

- encapsulation - hiding code and data within a class
- inheritance - sharing code and data in a parent class with a child class
- polymorphism - overriding a definition of parent class in a child class

Python supports all three concepts either by Python's design or through established conventions of using the language. In languages such as Java and C#, class structures strongly and statically type both their code and data members.

  Note: Strongly-typed code means that there are few implicit type conversions when executing expressions and statically-typed code means the types are defined at coding time not execution time. Python's classes are strongly-typed (as is the whole language) but the classes are only partially statically typed.

Using standard Python class syntax, the function members (known as bound methods) are statically-typed (defined when the class is defined) but the data members are dynamically-typed (added when the class is instantiated).

  Note: It is possible to change a class definition at run-time and it is possible to dynamically add bound methods to object instances using meta-programming but both are outside the scope of this course.

## Purpose of Python Classes

The purpose of Python classes is two-fold:

- provide a structure and dot-notation for record-type object
- share functions with many objects

Most programming languages provide a record or other structure type construct which allows a group of data attributes to be organized together as a single entity. A person has a first name and last name attribute. While `first_name` and `last_name` can be independent variables it is helpful to connect them together as attributes of single entity such as `person.first_name` and `person.last_name`. In the C programming language creating such a structure is known as `struct`. Unfortunately, Python provides no such formal structure. To solve this problem Python developers use a dictionary where each key is named after an attribute and maps to the attribute valie.

The problem with a dictionary is that each attribute is always accessed via a string using square brackets. The syntax for this can be problematic because the string is a data value not a piece of code. Classes can be used to provide a more elegant dot-notation syntax and many editors will provide code completion as well (something which generally will not happed with dictionaries).
	
```python
person['first_name'] # dictionary example, no code completion
person.first_name # class example, some editors will offer code completion
```

The second purpose is the ability to share function definitions (bound methods) with many objects.

```python
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

person1 = Person('Bob', 'Smith')
person2 = Person('Jane', 'Thomas')

print(person1.get_full_name())
print(person2.get_full_name())
```

Observe how the same `get_full_name` function is called on both person objects. Both person objects were created using the same class where the `get_full_name` function is defined.

Technically, functions defined on classes are known as bound methods and the value of `self` is passed in automatically when invoking the function on an object. As learned in the previous module a function is nothing more than a parameterized, callable block of code. Functions enable the reuse of logic throughout an application. Well, classes by definition define a structure which contains both data and code. The code is organized into function definition which are made available on class instances (objects) as bound methods which point back to the methods defined on the class. So bound methods are functions but they are a special case of function.

## Defining a Class

TODO: Add introduction.

1. Create a new Jupyter notebook named 'Class Exercises' in Azure Notebooks.

1. To define a class the `class` statement is used. In the first cell add the following code.

	```python
	class Person: pass
	```

	This will create a class named `Person`. The `pass` statement is a placeholder since no attributes or methods (functions) have been defined on the class.

1. An instance of the class can be created by invoking the class like a function and assigning the return value to a variable. This return value is an object. An object is an instance of a class. There can be many instances created from one class definition. Create a second cell and add the following code to it.

	```python
	person = Person()
	print(person)
	```

	Run all of the cells in the notebook. Something similar to this should be output:

	```text
	<__main__.Person object at 0x7fb0a9081278>
	```

1. Using the `person` variable additional data member (attributes) can be added. Modify the second cell to look like this.

	```python
	person = Person()
	person.first_name = 'Bob'
	person.last_name = 'Smith'
	
	print(person.first_name) # outputs: Bob
	```

	While this code will work, it does not promote consistent reusability as each consumer of the class would need to define their own properties on the instantiated object.

1. A better approach would to define a constructor function which is executed when the object is instantiated which would populate the attributes on the object. In Python the constructor function is defined as the `__init__` function. In Python, functions which have double underscores wrapped aroung the name indicate a special function used by Python when executing the program. Modify the code in the first cell to look like this.

	```python
	class Person:
	
	    def __init__(self, first_name, last_name):
	        self.first_name = first_name
	        self.last_name = last_name
	```

	The first parameter `self` is the instance of the class is not explicitly passed in by the code creating and using the object produced from this class.

	To create an instance using the new `__init__` function modify the code in the second cell to look like this.

	```python
	person = Person('Bob', 'Smith')
	print(person.first_name) # outputs: Bob
	print(person.last_name) # outputs: Smith
	```

	Run the entire notebook. Ensure everything outputs as expected.

1. In addition to attributes, methods can be defined as well. Modify the code in the first cell to look like this.

	```python
	class Person:
	
	    def __init__(self, first_name, last_name):
	        self.first_name = first_name
	        self.last_name = last_name
	
	    def get_full_name(self):
	        return self.first_name + ' ' + self.last_name
	```

	The `get_full_name` method will return a concatenated string of `first_name` and `last_name` attributes on the object. Modify the code in the second cell to look like this.

	```python
	person = Person('Bob', 'Smith')
	print(person.get_full_name()) # outputs: Bob Smith
	```

Run the entire notebook. Ensure everything outputs as expected.

## Class Inheritance

Classes are specifications. They define the structure of an object. In Python, functions (bound methods) are inherited not the definition of instance data attributes.

```python
class Something:

    # non-instance data attribute - inherited
    items = []

    def __init__(self):
        # instance data attribute - not inherited
        self.some_attr = 'test'

    # inherited bound method (function) - inherited
    def do_something(self):
        print('did it!')
```

> There are non-instance data attributes which are shared by all instances of a class (as shown above). They are outside scope of this module.

1. If not already open, open the same notebook you created for the defining a class exercise.

1. In a new cell at the bottom of the notebook, add the following code.

	```python
	class Student(Person):
	
	    def __init__(self, first_name, last_name, student_id):
	        super(Student, self).__init__(first_name, last_name)
	        self.student_id = student_id
	
	    def get_record_info(self):
	        return self.student_id + ' ' + self.last_name + ', ' + self.first_name
	```

	A class inherits the specification of another class by passing the name of the class within the paratheses of a class definition. In this case, the `Student` class will inherit from the `Person` class.

	Within the `__init__` function of the `Student` class, the `__init__` function of the `Person` class is called with the `super` function and the arguments needs for the `Person`'s `__init__` function. This ensure the object is configured correct for the `Student` and `Person` classes.

1. In a new cell at the bottom on the notebook, add the following code.

	```python
	student1 = Student('Bob', 'Smith', 1)
	student2 = Student('Jane', 'Thomas', 2)
	
	print(student1.get_full_name())
	print(student1.get_record_info())
	print(student2.get_full_name())
	print(student2.get_record_info())
	```

Two instances of a student will be created. Both will have access to the same `get_full_name` and `get_record_info` bound methods (functions).

## Convert the Airport and State Dictionaries to Classes

The airline data exercise results in a Jupyter notebook which will load and analyze airport, state and ontime flight data from the Bureau of Transportation Statistics. In this third exercise within the module, the airport and state dictionary structures will be converted to classes.

1. Open the Jupyter notebook named 'Airline Data Exercise' in Azure Notebooks. You may want to make a duplicate copy of this notebook before attempting this exercise.

2. The third cell should have the following code.

	```python
	def create_state(state_data):
	
	    state_abbr, state_name_data = state_data
	    country =  'United States'
	
	    state_name_parts = split_strip(state_name_data)
	
	    state_name = state_name_parts[0]
	    if (len(state_name_parts) == 2):
	        country = state_name_parts[1]
	        state_label = 'province'
	    else:
	        state_label = 'state'
	
	    return {
	        'code': state_abbr,
	        'name': state_name,
	        'label': state_label,
	        'country': country
	    }
	```

	Instead of creating a dictionary to manage the data for a state a class can be used. Replace the code in the cell with the following class definition code.

	```python
	class State:
	
	    def __init__(self, state_data):
	
	        state_abbr, state_name_data = state_data
	        country =  'United States'
	
	        state_name_parts = split_strip(state_name_data)
	        state_name = state_name_parts[0]

	        if (len(state_name_parts) == 2):
	            country = state_name_parts[1]
	            state_label = 'province'
	        else:
	            state_label = 'state'
	
	        self.code = state_abbr
	        self.name = state_name
	        self.label = state_label
	        self.country = country
	```

	Using a class allows for the use of dot notation to access attributes. Also, bound methods (functions) could be added to the class to perform additional functionalities.

1. To utilize the new class, a few additional changes are need to the notebook. The fourth cell should have the following code.

	```python
	def load_states(states_csv_file_name):
	
	    states = {}
	
	    with open(states_csv_file_name, 'r') as states_csv_file:
	        states_csv_file_reader = csv.reader(states_csv_file, delimiter=',')
	        for state_line_number, state_data in enumerate(states_csv_file_reader):
	            if state_line_number == 0: continue
	            state = create_state(state_data)
	            states[state['code']] = state
	  
	        return states
	```

	Replace these two lines:

	```python
	state = create_state(state_data)
	states[state['code']] = state
	```

	With these two lines:

	```python
	state = State(state_data)
	states[state.code] = state
	```

	Notice the `State` class is being used to produce a new `State` instance. Also, the `code` attribute on the `state` object is accessed without using square brackets. Instead, the dot notation for attributes is being used.

1. The fifth cell should contain the following code:

	```python
	def create_airport(airport, states):
	
	    code = airport[0]
	    name = ''
	    city = ''
	    state_label = ''
	    state_name = ''
	    country = ''
	
	    desc_parts = split_strip(airport[1], ':')
	
	    if len(desc_parts) == 2:
	
	        location, name = desc_parts
	        location_parts = split_strip(location)
	
	        if len(location_parts) == 2:
	            city = location_parts[0]
	            state_code = location_parts[1]
	
	        if state_code in states:
	            state = states[state_code]
	            state_name = state['name']
	            state_label = state['label']
	            country = state['country']
	        else:
	            country = state_code
	
	    else:
	        name = desc_parts[0]
	
	    return {
	        'code': code,
	        'name': name,
	        'city': city,
	        'state_name': state_name,
	        'state_label': state_label,
	        'country': country 
	    }
	```

	Replace the following lines of code:

	```python
	state_name = state['name']
	state_label = state['label']
	country = state['country']
	```

	with the following code:

	```python
	state_name = state.name
	state_label = state.label
	country = state.country
	```

	Run the entire notebook and ensure the same results are achieved as before. The output for the state and airports length should be 67 and 6510, respectively.

1. Replace the contents of the 5th cell, the `create_airport` function, with the following code.

	```python
	class Airport:
	
	    def __init__(self, airport, states):
	
	        code = airport[0]
	        name = ''
	        city = ''
	        state_label = ''
	        state_name = ''
	        country = ''
	
	        desc_parts = split_strip(airport[1], ':')
	
	        if len(desc_parts) == 2:
	
	            location, name = desc_parts
	            location_parts = split_strip(location)
	
	            if len(location_parts) == 2:
	                city = location_parts[0]
	                state_code = location_parts[1]
	
	                if state_code in states:
	                    state = states[state_code]
	                    state_name = state.name
	                    state_label = state.label
	                    country = state.country
	                else:
	                    country = state_code
	
	        else:
	            name = desc_parts[0]
	
	        self.code = code
	        self.name = name
	        self.city = city
	        self.state_name = state_name
	        self.state_label = state_label
	        self.country = country 
	```

1. Find the 6th cell with the following code.

	```python
	  def load_airports(airport_csv_file_name, states):
	
	      airports = {}
	
	      with open(airport_csv_file_name, 'r') as airports_csv_file:
	          airports_csv_file_reader = csv.reader(airports_csv_file, delimiter=',')
	          for airport_line_number, airport_data in enumerate(airports_csv_file_reader):
	              if airport_line_number == 0: continue
	              airport = create_airport(airport_data, states)
	              airports[airport['code']] = airport
	        
	      return airports
	```

	Replace the code:

	```python
	airport = create_airport(airport_data, states)
	airports[airport['code']] = airport
	```

	with the following code:

	```python
	airport = Airport(airport_data, states)
	airports[airport.code] = airport
	```

	Run the entire notebook and ensure the same results are achieved as before. The output for the state and airports length should be 67 and 6510, respectively.
