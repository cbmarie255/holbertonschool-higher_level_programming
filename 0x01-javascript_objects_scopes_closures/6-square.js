#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let character = 0; character < this.height; character++) { console.log(c.repeat(this.width)); }
  }
}
module.exports = Square;
