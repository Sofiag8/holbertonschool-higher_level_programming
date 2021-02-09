#!/usr/bin/node
const request = require('request');
const argumentsPassed = process.argv;

request.get(argumentsPassed[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
