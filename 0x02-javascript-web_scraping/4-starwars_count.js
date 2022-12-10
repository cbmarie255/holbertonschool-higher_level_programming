#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, text) {
  if (error != null) {
    console.log(error);
  } else {
    let appearances = 0;
    const data = JSON.parse(text);
    data.results.forEach(function (count) {
      count.characters.forEach(function (character) {
        const urlSplit = character.split('/');
        if (urlSplit[urlSplit.length - 2] === '18') {
          appearances++;
        }
      });
    });
    console.log(appearances);
  }
});
