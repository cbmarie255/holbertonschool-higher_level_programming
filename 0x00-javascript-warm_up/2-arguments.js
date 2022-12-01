#!/usr/bin/node
const process = require('process');
let shellPrompt;
if (process.argv.length === 3) {
  shellPrompt = 'Argument found';
} else if (process.argv.length < 3) {
  shellPrompt = 'No argument';
} else {
  shellPrompt = 'Arguments found';
}
console.log(shellPrompt);
