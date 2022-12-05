#!/usr/bin/node
const process = require('process');
const number = process.argv[2];
let factorial = 1;
for (let i = 1; i <= number; i++) {
  factorial *= i;
}
console.log(factorial);
