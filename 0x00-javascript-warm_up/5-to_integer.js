#!/usr/bin/node
const process = require('process');
const numberArg = process.argv[2];
if (numberArg === undefined) {
  console.log('Not a number');
} else if (isNaN(numberArg)) {
  console.log('Not a number');
} else if (parseInt(numberArg)) {
  console.log('My number: ' + parseInt(numberArg));
}
