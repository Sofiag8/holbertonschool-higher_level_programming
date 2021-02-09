#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
request(url, function (error, response, body) {
  if (error) { console.log(error); }
  JSON.parse(body).results.forEach(function (element) {
    element.characters.forEach(id => id.includes('18') ? counter++ : counter);
    return counter;
  });
  console.log(counter);
});
