# 0x0B. Python - Input/Output

Python programming is truly awesome, especially when it comes to handling Input/Output operations. In this README file, we'll explore various aspects of file handling, cursor manipulation, and the power of JSON in Python.

## How to Open a File

To open a file in Python, you can use the `open()` function. Here's a basic example:

```python
file_path = "example.txt"
with open(file_path, "r") as file:
    # Your code for file operations goes here
```

This ensures that the file is properly closed after use.

## How to Write Text in a File

To write text to a file, you can open it in write mode ("w"):

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python I/O!")
```

## How to Read the Full Content of a File

Reading the entire content of a file is straightforward:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## How to Read a File Line by Line

For reading a file line by line, use a loop:

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line)
```

## How to Move the Cursor in a File

You can use the `seek()` method to move the cursor to a specific position in the file:

```python
with open("example.txt", "r") as file:
    file.seek(5)  # Move the cursor to the 6th byte
    data = file.read(10)
    print(data)
```

## How to Make Sure a File is Closed After Using It

Using the `with` statement ensures that the file is closed automatically when the block is exited.

## What is and How to Use the `with` Statement

The `with` statement simplifies resource management, especially when dealing with file I/O. It automatically takes care of closing the file.

## What is JSON

JSON (JavaScript Object Notation) is a lightweight data interchange format, easy for humans to read and write, and easy for machines to parse and generate.

## What is Serialization

Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted, such as JSON.

## What is Deserialization

Deserialization is the process of converting a serialized format (like JSON) back into a usable data structure.

## How to Convert a Python Data Structure to a JSON String

Python provides the `json` module for this purpose:

```python
import json

data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string)
```

## How to Convert a JSON String to a Python Data Structure

Use the `json.loads()` method:

```python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_data = json.loads(json_string)
print(python_data)
```

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17