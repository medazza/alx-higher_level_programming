# 0x12. JavaScript - Warm up

## Table of Contents

1. [Introduction](#introduction)
2. [Running a JavaScript Script](#running-a-javascript-script)
3. [Variables and Constants](#variables-and-constants)
4. [Differences between var, const, and let](#differences-between-var-const-and-let)
5. [Data Types in JavaScript](#data-types-in-javascript)
6. [Conditional Statements](#conditional-statements)
7. [Comments](#comments)
8. [Assigning Values to Variables](#assigning-values-to-variables)
9. [Loops](#loops)
10. [Break and Continue Statements](#break-and-continue-statements)
11. [Functions](#functions)
12. [Functions without Return Statements](#functions-without-return-statements)
13. [Scope of Variables](#scope-of-variables)
14. [Arithmetic Operators](#arithmetic-operators)
15. [Manipulating Dictionaries](#manipulating-dictionaries)
16. [Importing a File](#importing-a-file)

## Introduction

JavaScript is an amazing programming language known for its versatility.

## Running a JavaScript Script

To execute a JavaScript script, use a JavaScript runtime environment such as Node.js. In the terminal, run:

```bash
node your_script.js
```

## Variables and Constants

In JavaScript, variables are declared using `var`, `const`, or `let`. Constants are declared using `const`. Example:

```javascript
var x = 10;
const pi = 3.14;
let message = "Hello, World!";
```

## Differences between var, const, and let

- `var` has function-scoped or globally scoped variables.
- `const` is used for variables that should not be re-assigned.
- `let` allows re-assignment of variables.

## Data Types in JavaScript

JavaScript has various data types, including `string`, `number`, `boolean`, `object`, `null`, and `undefined`.

## Conditional Statements

Use `if`, `if...else` statements for decision-making in your code.

```javascript
if (condition) {
  // code to execute if the condition is true
} else {
  // code to execute if the condition is false
}
```

## Comments

Use `//` for single-line comments and `/* */` for multi-line comments.

## Assigning Values to Variables

Assign values to variables using the assignment operator (`=`).

```javascript
let x = 5;
```

## Loops

JavaScript supports `while` and `for` loops for repetitive tasks.

```javascript
while (condition) {
  // code to execute while the condition is true
}

for (let i = 0; i < 5; i++) {
  // code to execute during each iteration
}
```

## Break and Continue Statements

`break` exits a loop, and `continue` skips to the next iteration.

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // exit the loop when i is 5
  }
  // code to execute during each iteration
}
```

## Functions

Define functions using the `function` keyword.

```javascript
function greet(name) {
  return "Hello, " + name + "!";
}
```

## Functions without Return Statements

Functions without a `return` statement return `undefined`.

```javascript
function sayHello() {
  console.log("Hello!");
}
```

## Scope of Variables

Variables have global or local scope, depending on where they are declared.

## Arithmetic Operators

JavaScript supports arithmetic operators like `+`, `-`, `*`, and `/` for mathematical operations.

## Manipulating Dictionaries

In JavaScript, dictionaries are called objects. Use curly braces `{}` to create an object.

```javascript
let person = { name: "John", age: 30 };
```

## Importing a File

For frontend JavaScript, use `<script>` tags in HTML. In Node.js, use `require` or `import` statements.

```javascript
// Node.js
const myModule = require('./myModule');

// ES6 Modules
import { myFunction } from './myModule';
```
## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17