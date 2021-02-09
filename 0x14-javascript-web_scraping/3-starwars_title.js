#!/usr/bin/node
const request = require('request');
const idNumber = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${idNumber}`;

request(url, function (error, response, body) {
  if (error) { console.log(error); }
  console.log(JSON.parse(body).title);
});
