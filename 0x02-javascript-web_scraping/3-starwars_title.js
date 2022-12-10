#!/usr/bin/node
const process = require('process');
const request = require('request');
const episodeNumber = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + episodeNumber;
request(url, function (error, response, text) {
  if (error != null) {
    console.log(error);
  } else {
    const data = JSON.parse(text);
    console.log(data.title);
  }
});
