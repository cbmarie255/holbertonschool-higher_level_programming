#!/usr/bin/node
const process = require('process');
const system = require('fs');
const fileName = process.argv[2];
const string = process.argv[3];
system.writeFile(fileName, string, 'utf8', function (error, data) {
  if (error != null) {
    console.log(error);
  }
});
