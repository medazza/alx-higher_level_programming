#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ind = 0; ind < this.height; ind++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
