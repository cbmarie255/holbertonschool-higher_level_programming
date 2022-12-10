#!/usr/bin/node
const process = require('process');
const system = require('fs');
const fileName = process.argv[2];
system.readFile(fileName, 'utf8', function (error, data) {
  if (error != null) {
    console.log(error);
  } else {
    console.log(data);
  }
});
