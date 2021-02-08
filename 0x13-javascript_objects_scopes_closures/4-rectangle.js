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

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
// constructor is called from a different file
module.exports = Rectangle;
