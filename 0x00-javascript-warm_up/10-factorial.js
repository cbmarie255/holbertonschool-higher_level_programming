#!/usr/bin/node
const process = require('process');
const arg = process.argv[2];
function factorial (number) {
  if (isNaN(number) || number === 0) {
    return 1;
  }
  return (number * factorial(number - 1));
}
console.log(factorial(parseInt(arg)));
