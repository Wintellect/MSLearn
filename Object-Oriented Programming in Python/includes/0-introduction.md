# Introduction

Imagine that you work for a company that helps locate missing persons. You have been asked to write some code to be used in an application that catalogs missing persons and information about them in a database. Your code will define the information stored about a person, including a photo. The application is written in Python, so you will be using Python as well.

You could write classic [procedural code](https://en.wikipedia.org/wiki/Procedural_programming) containing functions such as `add_missing_person_to_database()` and `get_information_about_missing_person()`. But such code, while common, can also be difficult to maintain — especially as, over time, the code base grows in size and complexity.

Object-oriented programming (OOP) is a proven way of structuring your code so that it is easier to write, understand, test, and maintain. Rather than leave it to other programmers to figure out how to take the photos you store and display them on the screen, for example, you could define an object that represents a missing person and build the capability to display that person's photo into the object. Subsequently, anyone could render a photo of a missing person on the screen with a simple function call.

Writing object-oriented code in Python is a little different than writing procedural code, but if you know the basics of Python, it isn't difficult. In this module, you will learn how to write object-oriented code in Python and also see first-hand some of the benefits of doing so.

## What is OOP?

Legendary programmer named [Alan Kay](https://en.wikipedia.org/wiki/Alan_Kay) originally conceived of object-oriented programming as a way to define:

- Attributes: the object's characteristics
- Methods: a way to instruct an object to perform tasks
- Events: things that happen to the object

Kay [created this concept in the 1970s](http://web.eecs.utk.edu/~huangj/CS302S04/notes/oo-intro.html) for modeling simulations. By modeling a complex coding scenario such as writing a simulation as a series of objects based on what the simulation would do in the real world, Kay made the concept of writing the code much easier to think about.

It could be hard to think about the code used to create a simulation no matter the model. But object oriented programming makes it easier to grasp. You can now relate the model to something that you already understand: an object. The code performs a real world act. When the code runs, you see the real world similutation take place. So, OOP is a method of looking at complex coding models in a way that simplifies the modeling.

## Why is OOP important?

Most people don't understand abstractions well, yet computers thrive on them. Your computer sees everything as a set of numbers manipulated by algorithms. Unless you're a math genius, communicating even simple ideas to a computer could fry your brain!

So, the purposes of OOP are to:

- **Simplify your life**: Make it possible for you to communicate what you want the computer to do in a manner that you use naturally, but the computer can understand.

- **Define ideas consistently**: Find a common way to express what you want to do so that others understand. For example, we all know that cats and dogs belong to the animal kingdom and that animals have common characteristics. So you might start by defining an animal object. You then create cat and dog objects starting with the animal object using an OOP feature called inheritance.

- **Specify the manner used to create objects**: Each object defines attributes, methods, and events using specific techniques. You obtain repeatable results by defining each object in an application, library, or other code group using a specific standard. Understanding how one object is constructed makes it possible to create others using like techniques and to understand any object using those techniques with greater ease.

- **Perform code-writing tasks with less effort**: Creating an animal object means that you only have to specify all the things that make animals different from other objects once. To create a cat or a dog object, all you need to define is what makes a cat or a dog unique. Using the animal object as the basis for the cat and dog objects is called code reuse.

## The elements of OOP

Objects in programming are complete: They combine data and code into a single entity so you can work with them as a unit. Just as someone must create a specification for manufacturing a pencil, OOP requires that you specify how to create your object.

A common analogy from architecture and other forms of manufacture is that you start with a blueprint, which contains a parts list (the data) and instructions (the code) for building a house. An alternative example is a a recipe. If you want to repeat that fabulous chocolate chip cookie experience, then you need a recipe that contains a list of ingredients (the data) and baking instructions (the code) to do it. This blueprint or recipe is called a *class* in Python.

Yet a blueprint isn't a house and a recipe isn't a cookie. You must obtain the materials and follow the instructions provided by the blueprint or recipe to create the real world object. 

A house is an *instance* of a blueprint. You can build as many houses as you like by following the blueprint; it doesn't wear out. Likewise, you can bake as many cookies as you want from the same recipe. In OOP, to create an object, you create an instance of a class.

Within the class are all of the things that you normally associate with objects in the real world. Just as the pencil has characteristics such as a color, a class has *attributes* that contain data that define the object characteristics. When you want to perform a task with your object, you call a *method*. When something happens to your object, it generates an *event*.

## Learning objectives

In this module, you will learn:

- How to define classes in Python
- How to instantiate classes in Python
- How to add attributes to classes
- How to add methods to classes
- How to create new classes that inherit from others

There is much to learn, so let's get started.