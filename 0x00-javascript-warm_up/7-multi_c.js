#!/usr/bin/node
const process = require('process');
const loopArg = process.argv[2];
if (isNaN(loopArg)) {
  console.log('Missing number of occurances');
} else if (!isNaN(loopArg)) {
  let x;
  for (x = 0; x < loopArg; x++) {
    console.log('C is fun');
  }
}
