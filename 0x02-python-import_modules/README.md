# 0x02. Python - Import & Modules

This readme file provides a comprehensive guide on working with modules, importing functions from other files, and utilizing various features of Python related to code organization and execution.

## Table of Contents
- [Importing Functions from Another File](#importing-functions-from-another-file)
- [Using Imported Functions](#using-imported-functions)
- [Creating a Module](#creating-a-module)
- [Using the built-in function `dir()`](#using-the-built-in-function-dir)
- [Preventing Code Execution on Import](#preventing-code-execution-on-import)
- [Command Line Arguments in Python](#command-line-arguments-in-python)

## Importing Functions from Another File
To import functions from another Python file, use the `import` statement followed by the module name (file name without the `.py` extension). For example, to import a function named `my_function` from a file named `my_module.py`:

```python
import my_module

result = my_module.my_function()
```

## Using Imported Functions
After importing a module, you can use its functions using the module name and function name:

```python
import my_module

result = my_module.my_function()
```

## Creating a Module
To create a module, simply create a new `.py` file and define functions, classes, or variables in it. These can then be imported and used in other scripts.

**my_module.py:**
```python
def my_function():
    return "Hello from my_function!"
```

## Using the built-in function `dir()`
The `dir()` function lists all names in the current scope, including functions, classes, modules, and variables. It's useful for exploring available functionalities within a module or an object.

```python
import my_module

print(dir(my_module))
```

## Preventing Code Execution on Import
When importing a module, Python executes all top-level code in that module. To prevent specific code from running on import, use the `if __name__ == "__main__":` construct:

```python
def some_function():
    print("Function executed!")

if __name__ == "__main__":
    some_function()
```

## Command Line Arguments in Python
You can pass command line arguments to your Python scripts using the `sys.argv` list from the `sys` module:

```python
import sys

# Script name is sys.argv[0], arguments start from sys.argv[1]
arg1 = sys.argv[1]
arg2 = sys.argv[2]

print("Argument 1:", arg1)
print("Argument 2:", arg2)
```

Remember to execute the script with additional arguments:

```bash
python my_script.py arg1_value arg2_value
```

This concludes the guide to importing, modules, and various related features in Python.


Do Hard Things

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17