#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || w <= 0 || isNaN(h) || h <= 0) {
      return;
    }
    // init instance attributes
    this.width = w;
    this.height = h;
  }
}

// constructor is called from a different file
module.exports = Rectangle;
