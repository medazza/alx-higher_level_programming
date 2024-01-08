#!/usr/bin/node

function factorial (number) {
  if (Number.isNaN(number) || (number <= 0)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(Number.parseInt(process.argv[2])));
