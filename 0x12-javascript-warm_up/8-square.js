#!/usr/bin/node
/* printing a square with X char, if the passed arg can't be converted
to int then print default message. Use just one time console and a loop */
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let aux = 0; aux < size; aux++) {
    console.log('X'.repeat(size));
  }
}
