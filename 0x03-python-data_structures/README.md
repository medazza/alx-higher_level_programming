# 0x03. Python - Data Structures: Lists, Tuples

## What are Lists and How to Use Them

In Python, a list is a versatile data structure that allows you to store a collection of items. These items can be of any data type, including other lists. Lists are defined using square brackets `[]` and items are separated by commas.

Example:
```python
my_list = [1, 2, 3, "alx", "banana", True]
```

## Differences and Similarities Between Strings and Lists

Strings and lists are both sequences, meaning they can hold multiple items. However, strings can only hold characters, while lists can hold any data type. Lists are mutable, meaning you can modify their contents after creation, whereas strings are immutable.

## Common Methods of Lists and How to Use Them

Python offers a variety of methods to manipulate lists:
- `append(item)`: Adds an item to the end of the list.
- `insert(index, item)`: Inserts an item at a specific index.
- `remove(item)`: Removes the first occurrence of the specified item.
- `pop(index)`: Removes and returns the item at the specified index.
- `len(list)`: Returns the number of items in the list.

Example:
```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.insert(1, 5)
my_list.remove(2)
popped_item = my_list.pop(0)
```

## Using Lists as Stacks and Queues

You can use lists as stacks (Last-In-First-Out) and queues (First-In-First-Out) using the `append()` and `pop()` methods for stacks, and the `append()` and `pop(0)` methods for queues.

Example of using a list as a stack:
```python
stack = []
stack.append(1)
stack.append(2)
popped_item = stack.pop()  # Removes and returns 2
```

## List Comprehensions and How to Use Them

List comprehensions provide a concise way to create lists. They consist of an expression followed by a `for` loop and optional `if` conditions.

Example:
```python
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
```

## Tuples and How to Use Them

Tuples are similar to lists, but they are immutable, meaning you cannot change their contents after creation. Tuples are defined using parentheses `()`.

Example:
```python
my_tuple = (1, 2, 3, "apple")
```

## When to Use Tuples Versus Lists

Use tuples when you have data that shouldn't be modified, such as coordinates or configuration settings. Use lists when you need a mutable collection of items.

## What is a Sequence

A sequence is an ordered collection of items. Lists, strings, and tuples are all examples of sequences in Python.

## Tuple Packing

Tuple packing refers to creating a tuple by placing comma-separated values on the right-hand side of an assignment without parentheses.

Example:
```python
coordinates = 3.14, 2.71
```

## Sequence Unpacking

Sequence unpacking allows you to assign the elements of a sequence to multiple variables.

Example:
```python
x, y = coordinates
```

## The `del` Statement and How to Use It

The `del` statement is used to delete items from a list or variables from memory.

Example:
```python
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Deletes the item at index 2 (value 3)
```

Do Hard Thing

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17