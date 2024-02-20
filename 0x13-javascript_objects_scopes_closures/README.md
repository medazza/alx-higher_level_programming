# 0x13. JavaScript - Objects, Scopes, and Closures

## How to create an object in JavaScript

In JavaScript, objects are a fundamental data type that allows you to store and organize data. You can create objects using object literals or the `Object` constructor. Here's a basic example using an object literal:

```javascript
let person = {
  name: 'John Doe',
  age: 25,
  profession: 'Developer'
};
```

## What this means

In JavaScript, `this` refers to the current execution context. It can behave differently depending on how and where it's used. Understanding `this` is crucial for managing scope and accessing the correct object properties.

## What undefined means

In JavaScript, `undefined` is a primitive value that is automatically assigned to variables that have been declared but not initialized. It indicates the absence of a meaningful value.

## Why variable type and scope are important

Variable types and scope play a crucial role in JavaScript. Properly managing these aspects ensures correct data manipulation, avoids unexpected behavior, and helps prevent bugs in your code.

## What is a closure

A closure is a feature in JavaScript where a function retains access to variables from its outer (enclosing) scope even after the outer function has finished executing. Closures are powerful for creating private variables and functions.

## What is a prototype

In JavaScript, each object has a prototype, which serves as a blueprint for the object. Understanding prototypes is essential for inheritance and object-oriented programming in JavaScript.

## How to inherit an object from another

JavaScript supports inheritance through prototypes. You can use the `Object.create()` method or constructor functions to create objects that inherit properties and methods from another object.

```javascript
// Using Object.create()
let parentObject = {
  greet: function() {
    console.log('Hello!');
  }
};

let childObject = Object.create(parentObject);
childObject.greet(); // Outputs: Hello!
```

These are fundamental concepts in JavaScript that form the building blocks for creating robust and maintainable code.

---
## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17
