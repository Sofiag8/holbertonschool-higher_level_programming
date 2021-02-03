#!/usr/bin/node
/* Factorilizing a passed argument as integer
with a function and recursively */
const argument = parseInt(process.argv[2]);
function factorialize (argument) {
  if (argument) {
    return (argument * factorialize(argument - 1));
  } else {
    return 1;
  }
}
console.log(factorialize(argument));
