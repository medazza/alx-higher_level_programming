# 0x0A. Python - Inheritance

## Why Python Programming is Awesome

Python is awesome for several reasons:
- **Readability:** Python's syntax is clear and expressive, making it easy to read and write code.
- **Versatility:** Python is a versatile language suitable for various applications, from web development to data analysis and machine learning.
- **Community:** Python has a large and active community, providing support, libraries, and frameworks that contribute to its continual improvement.
- **Extensive Libraries:** Python comes with a rich set of libraries, making it efficient for a wide range of tasks.

## What is a Superclass, Baseclass, or Parentclass

In object-oriented programming, a superclass, baseclass, or parentclass is a class that is extended or inherited by other classes. It provides common attributes and methods that are shared by its subclasses.

## What is a Subclass

A subclass is a class that inherits attributes and methods from a superclass. It can also have additional attributes or methods or override existing ones.

## How to List All Attributes and Methods of a Class or Instance

You can list all attributes and methods of a class or instance using the built-in `dir()` function. For example:
```python
print(dir(MyClass))
print(dir(my_instance))
```

## When Can an Instance Have New Attributes

An instance can have new attributes at any time by simply assigning values to new attribute names. For example:
```python
my_instance.new_attribute = "value"
```

## How to Inherit Class from Another

Inheritance in Python is achieved by specifying the superclass in the class definition. For example:
```python
class ChildClass(ParentClass):
    # additional attributes and methods
```

## How to Define a Class with Multiple Base Classes

You can define a class with multiple base classes by separating them with commas. For example:
```python
class ChildClass(ParentClass1, ParentClass2):
    # additional attributes and methods
```

## What is the Default Class Every Class Inherits From

The default class every class inherits from in Python is the `object` class.

## How to Override a Method or Attribute Inherited from the Base Class

You can override a method or attribute by redefining it in the subclass with the desired implementation. For example:
```python
class ChildClass(ParentClass):
    def overridden_method(self):
        # new implementation
```

## Which Attributes or Methods Are Available by Heritage to Subclasses

All public attributes and methods from the superclass are available to subclasses through inheritance.

## What is the Purpose of Inheritance

The purpose of inheritance is to promote code reuse, organize code in a hierarchical structure, and allow for the creation of specialized classes based on existing ones.

## What Are, When, and How to Use isinstance, issubclass, type, and super Built-in Functions

- **isinstance:** Checks if an object is an instance of a specified class or a tuple of classes.
- **issubclass:** Checks if a class is a subclass of another class.
- **type:** Returns the type of an object. Used to check the type of an object or create new types.
- **super:** Returns a temporary object of the superclass, allowing you to call its methods.

For example:
```python
if isinstance(obj, MyClass):
    # do something

if issubclass(ChildClass, ParentClass):
    # do something

obj_type = type(obj)
```

These built-in functions are useful for checking types, relationships between classes, and accessing methods of the superclass.
```

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17