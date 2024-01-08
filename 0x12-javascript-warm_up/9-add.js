#!/usr/bin/node

function add (a, b) {
  return a + b;
}

console.log(
  add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]))
);
