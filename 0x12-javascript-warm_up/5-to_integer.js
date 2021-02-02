#!/usr/bin/node
/* script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer,
if not print Not a number */
const argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argument}`);
}
