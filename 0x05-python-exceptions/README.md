# 0x05. Python - Exceptions

## Difference between Errors and Exceptions
In Python, both errors and exceptions refer to situations where the normal flow of a program is disrupted. However, there is a distinction between the two. Errors are generally more severe and are caused by fundamental issues in the code, such as syntax errors or issues with importing modules. Exceptions, on the other hand, are events that occur during the execution of a program, often due to external factors or unforeseen circumstances.

## What are Exceptions and How to Use Them
Exceptions are events that occur during the execution of a program that disrupt the normal flow of code. They are objects that encapsulate information about the error, making it easier to understand and handle the error. In Python, exceptions are raised when an error occurs, and they can be caught and handled using try-except blocks.

To use exceptions, you can use the following syntax:
```python
try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception
```

## When Do We Need to Use Exceptions
Exceptions are useful when you anticipate the possibility of errors occurring during the execution of your code. They provide a structured way to handle errors and prevent your program from crashing. You should use exceptions when there are situations that are beyond your control, such as file not found, network errors, or invalid user input.

## How to Correctly Handle an Exception
To correctly handle an exception, you can use try-except blocks. Within the try block, you place the code that might raise an exception. If an exception is raised, it's caught by the corresponding except block where you can define the appropriate handling logic. This way, even if an exception occurs, your program can continue executing.

```python
try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception
```

## Purpose of Catching Exceptions
The main purpose of catching exceptions is to prevent your program from crashing when an error occurs. By catching exceptions and providing appropriate error-handling code, you can gracefully recover from errors and display meaningful error messages to users, making your program more user-friendly and robust.

## How to Raise a Builtin Exception
You can raise a built-in exception in Python using the `raise` statement. This is useful when you want to indicate that a specific error condition has occurred in your code. For example:

```python
if some_condition:
    raise ValueError("This is a custom error message")
```

## When Do We Need to Implement a Clean-up Action After an Exception
Sometimes, you might need to ensure that certain actions are taken regardless of whether an exception occurred or not. This is where the `finally` block comes into play. The code inside the `finally` block will be executed no matter what, whether an exception was raised or not. This is useful for implementing cleanup operations, such as closing files or releasing resources.

```python
try:
    # Code that might raise an exception
finally:
    # Code that will run regardless of exceptions
```

Do Hard Things

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17