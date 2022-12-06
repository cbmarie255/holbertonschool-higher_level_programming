#!/usr/bin/node
const process = require('process');
const request = require('request');
const system = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, function (error, response, text) {
  if (error) {
    console.log(error);
  } else {
    system.writeFile(fileName, text, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
