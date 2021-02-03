#!/usr/bin/node
/* printing addition of two integers
with a predetermine function */
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(parseInt(add(a, b)));
