#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    for (let count = 0; count < this.height; count++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
