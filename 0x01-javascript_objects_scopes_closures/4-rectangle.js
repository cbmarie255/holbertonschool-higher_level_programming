#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringSquare = '';
    for (let column = 1; column <= this.height; column++) {
      for (let row = 1; row <= this.width; row++) {
        stringSquare += 'X';
      }
      stringSquare += '\n';
    }
    process.stdout.write(stringSquare);
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
