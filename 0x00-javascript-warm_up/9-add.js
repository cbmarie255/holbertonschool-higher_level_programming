#!/usr/bin/node
function add(a, b) {
  result = ((parseInt(a) + parseInt(b)));
  return result
}
const process = require('process');
console.log(add(process.argv[2], process.argv[3]))
