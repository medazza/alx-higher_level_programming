# 0x06. Python - Classes and Objects

## What is OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. It emphasizes the use of objects to represent real-world entities and their interactions. OOP aims to structure code in a way that models relationships and behaviors between objects, making code more modular, reusable, and easier to maintain.

## "First-Class Everything"

In Python, "first-class everything" refers to the principle that everything in the language, including functions, classes, and objects, is treated as an object that can be assigned to variables, passed as arguments, and returned from functions.

## What is a Class

A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that the objects created from it will have.

## What is an Object and an Instance

An object is an instance of a class. It's a concrete realization of the blueprint defined by the class. An instance refers to a single occurrence of the object created from that class.

## Difference Between a Class and an Object or Instance

A class is the template that defines the structure and behavior of objects. An object or instance is a concrete realization of that class with specific data and state.

## What is an Attribute

An attribute is a variable that holds data within a class or object. It represents a characteristic or property of the object.

## Public, Protected, and Private Attributes

In Python, attributes can have different levels of visibility:
- Public attributes are accessible from anywhere.
- Protected attributes are indicated by a single underscore and are considered non-public, although they can still be accessed.
- Private attributes are indicated by a double underscore and are meant to be hidden from external access.

## What is `self`

`self` is a conventionally used parameter name in instance methods of a class. It refers to the instance of the class itself, allowing you to access its attributes and methods.

## What is a Method

A method is a function defined within a class that operates on the attributes of instances created from that class.

## Special `__init__` Method and How to Use It

The `__init__` method is a special method that gets called when an object is created from a class. It initializes the object's attributes and sets its initial state.

## Data Abstraction, Data Encapsulation, and Information Hiding

- Data Abstraction involves representing essential features of an object while hiding unnecessary details.
- Data Encapsulation restricts direct access to certain attributes, promoting the use of methods for interaction.
- Information Hiding aims to prevent the accidental modification of attributes by restricting access.

## What is a Property

A property is a special kind of attribute that is accessed like an attribute but is implemented using methods, allowing for controlled access and modification.

## Difference Between an Attribute and a Property in Python

An attribute is a variable within a class or object, while a property uses getter and setter methods to provide controlled access to an attribute.

## Pythonic Way to Write Getters and Setters

In Python, you can use the `@property` decorator for getters and the `@attribute_name.setter` decorator for setters to implement properties.

## Dynamically Creating Arbitrary New Attributes

You can dynamically create new attributes for existing instances of a class by simply assigning values to new attribute names.

## Binding Attributes to Objects and Classes

Attributes can be bound to both objects and classes. When bound to a class, they are shared among all instances of the class.

## `__dict__` of a Class and/or Instance

`__dict__` is a dictionary that contains the attributes of a class or an instance of a class, including their names and values.

## How Python Finds Attributes of an Object or Class

Python first checks if the attribute is present in the instance's namespace. If not, it looks in the class's namespace and its parent classes until it finds the attribute.

## Using the `getattr` Function

The `getattr` function is used to dynamically access attributes of objects or classes by passing the object and attribute name as arguments. If the attribute doesn't exist, a default value can be provided.

Do Hard things

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17