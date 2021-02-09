#!/usr/bin/node
const fs = require('fs');
const argumentsPassed = process.argv;

fs.writeFile(argumentsPassed[2], argumentsPassed[3], 'utf-8', (err) => {
  if (err) { console.log(err); }
});
