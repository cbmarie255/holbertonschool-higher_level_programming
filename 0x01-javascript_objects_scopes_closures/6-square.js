#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
