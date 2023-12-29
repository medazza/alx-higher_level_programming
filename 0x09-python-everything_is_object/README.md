# 0x09. Python - Everything is object

## What is an Object?
In Python, everything is an object. An object is a self-contained unit that encapsulates data and the functions that operate on that data. Objects are instances of classes, and they can represent anything from simple data types to complex structures.

## Difference between a Class and an Object or Instance
A class is a blueprint or template for creating objects. An object, also known as an instance, is a specific realization of a class. In simpler terms, a class defines the structure, and an object is an instance of that structure.

## Difference between Immutable and Mutable Objects
- **Immutable Object:** An object whose state cannot be modified after it is created. Immutable objects in Python include tuples, strings, and integers.
- **Mutable Object:** An object that can be modified after it is created. Lists and dictionaries are examples of mutable objects in Python.

## What is a Reference?
In Python, a reference is a value that refers to the memory address of an object. Variables in Python are references to objects rather than containers for data.

## What is an Assignment?
Assignment is the process of binding a name to an object. When you assign a value to a variable, you are creating a reference to the object that holds the data.

## What is an Alias?
An alias occurs when two or more variables refer to the same object. Changes made through one alias will affect the object and be reflected in the other aliases.

## How to Know if Two Variables are Identical
Use the `is` keyword to check if two variables refer to the same object in memory. Identical objects have the same memory address.

## How to Know if Two Variables are Linked to the Same Object
Comparing variables using `==` checks if the objects they refer to have the same content. To check if they refer to the same object, use the `is` keyword.

## How to Display the Variable Identifier
In the CPython implementation, you can use the `id()` function to display the memory address (variable identifier) of an object.

## Mutable and Immutable
- **Mutable:** Objects whose state can be changed after creation.
- **Immutable:** Objects whose state cannot be changed after creation.

## Built-in Mutable Types
- Lists
- Dictionaries
- Sets

## Built-in Immutable Types
- Integers
- Floats
- Strings
- Tuples

## How Does Python Pass Variables to Functions
In Python, variables are passed to functions by object reference. Changes made to mutable objects within a function are reflected outside the function, while immutable objects remain unchanged.

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17