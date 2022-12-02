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
}
module.exports = Rectangle;
