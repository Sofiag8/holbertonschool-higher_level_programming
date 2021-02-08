#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
// constructor is called from a different file
module.exports = Rectangle;
