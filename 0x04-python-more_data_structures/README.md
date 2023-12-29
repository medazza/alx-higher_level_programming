# 0x04. Python - More Data Structures: Set, Dictionary

## What are sets and how to use them
A set is an unordered collection of unique elements in Python. To create a set, you can use curly braces `{}` or the `set()` constructor. Sets are commonly used for tasks that require uniqueness, such as removing duplicates from a list. Here's how to create and use sets:

```python
# Creating a set
my_set = {1, 2, 3}

# Adding elements to a set
my_set.add(4)

# Removing elements from a set
my_set.remove(2)

# Checking membership
if 3 in my_set:
    print("3 is in the set")
```

## What are the most common methods of set and how to use them
Sets have various methods for performing operations like union, intersection, difference, and more. Some common set methods include `union()`, `intersection()`, `difference()`, and `symmetric_difference()`. Here's an example of using these methods:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)

# Intersection of two sets
intersection_set = set1.intersection(set2)

# Difference of two sets
difference_set = set1.difference(set2)

# Symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
```

## When to use sets versus lists
Use sets when you need to work with unique elements and order doesn't matter. Lists are ordered and allow duplicates, while sets do not.

## How to iterate into a set
You can iterate through a set using a `for` loop:

```python
my_set = {1, 2, 3}

for element in my_set:
    print(element)
```

## What are dictionaries and how to use them
A dictionary is an unordered collection of key-value pairs in Python. Keys are unique, and they are used to access values associated with them. Dictionaries are created using curly braces `{}` or the `dict()` constructor. Here's how to create and use dictionaries:

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 20, 'school': 'ALX'}

# Accessing values by key
name = my_dict['name']

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'

# Removing a key-value pair
del my_dict['age']
```

## When to use dictionaries versus lists or sets
Use dictionaries when you need to store data in a key-value format, especially when you want to quickly access values by their associated keys. Lists are used for ordered collections, and sets for unordered collections of unique elements.

## What is a key in a dictionary
A key in a dictionary is a unique identifier that is used to access a corresponding value. Keys must be immutable, which means they cannot be changed after they are created. Common key types are strings and numbers.

## How to iterate over a dictionary
You can iterate through a dictionary using a `for` loop to access its keys and values:

```python
my_dict = {'name': 'John', 'age': 20, 'schoool': 'ALx'}

for key, value in my_dict.items():
    print(f'{key}: {value}')
```

## What is a lambda function
A lambda function, also known as an anonymous function, is a small, unnamed function defined using the `lambda` keyword in Python. Lambda functions are often used for simple operations and are defined without using the `def` keyword. Here's an example:

```python
add = lambda x, y: x + y
result = add(3, 5)  # Result is 8
```

## What are the map, reduce, and filter functions
These are higher-order functions in Python used for processing sequences, such as lists, efficiently:

- `map(function, iterable)`: Applies the given function to each item in the iterable and returns an iterator of the results.

- `reduce(function, iterable)`: Applies the given function cumulatively to the items of the iterable, reducing it to a single result.

- `filter(function, iterable)`: Returns an iterator from elements of the iterable for which the function returns `True`.

Example of using `map`:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# squared will be [1, 4, 9, 16, 25]
```

Example of using `reduce` (requires importing `functools`):

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# product will be 120
```

Example of using `filter`:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers will be [2, 4]
```

Do hard things

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17