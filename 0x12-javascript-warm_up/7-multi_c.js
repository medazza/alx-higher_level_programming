#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

const numOfOccurrences = parseInt(args[0]);

if (!isNaN(numOfOccurrences)) {
  for (let ind = 0; ind < numOfOccurrences; ind++) {
    console.log('C is fun');
  }
} else {
  console.log('Missign number of occurrences');
}
