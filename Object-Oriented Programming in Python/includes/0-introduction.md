# Introduction

We all work with objects every day. In fact, everything in the real world is an object. If you pick up a pencil, you interact with the pencil as an object. The pencil has certain attributes, such as a color and a particular kind of lead. You can perform actions with it, such as leave a note for a loved one. Events can happen to your pencil, such as when you drop it.

Objects also come in groups, such as a box of pencils. You can then select a single pencil from the box. The pencils might be different colors—that is, they have different attributes—but they're all pencils, so they all belong to the group.

It turns out that objects also provide a convenient way for programmers to envision how things should work in an application. This unit is all about helping you start to visualize the incredibly abstract notion of code as an object to make coding easier to do.

The goal is to see the world of coding in a new way. Like pencils, these code objects have attributes, allow you to perform tasks, and experience events. You can also create groups of objects so that a single object, `myObject`, becomes a group of objects, `myObjects`.

## What is OOP?

Legendary programmer named Alan Kay originally conceived of object-oriented programming (OOP) as a way to define:

- Attributes: the object's characteristics
- Methods: a way to perform tasks
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

There's a lot to do, so let's get started.