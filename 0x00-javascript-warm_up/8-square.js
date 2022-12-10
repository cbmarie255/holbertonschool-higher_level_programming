#!/usr/bin/node
const process = require('process');
const squareSize = process.argv[2];
let stringSquare = '';
if (isNaN(squareSize)) {
  console.log('Missing size');
} for (let row = 1; row <= squareSize; row++) {
  for (let column = 1; column <= squareSize; column++) {
    stringSquare += 'X';
  }
  stringSquare += '\n';
}
process.stdout.write(stringSquare);
