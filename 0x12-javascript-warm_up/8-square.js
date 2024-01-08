#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

const size = parseInt(args[0]);

if (!isNaN(size)) {
  for (let ind = 0; ind < size; ind++) {
    let row = '';
    for (let jnd = 0; jnd < size; jnd++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
