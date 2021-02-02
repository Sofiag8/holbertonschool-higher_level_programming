#!/usr/bin/node
/* printing x times a string where x is the number passed
as argument. If x cant be converted to a int then print
Missing number of occurrences and only use a loop and two
consoles */
let x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of ocurrences');
} else {
  while (x > 0) {
    x--;
    console.log('C is fun');
  }
}
