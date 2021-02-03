#!/usr/bin/node
/* script that search for the second biggest integer
in a list passed as arguments and prints it.
If nothing is passed or 1 is passed, prints 0 */
const values = process.argv;
if (values.length <= 3) {
  console.log('0');
} else {
  /* sort acepts a comparative fuction which in this case
   organizes values in ascendent order */
  values.sort(function (a, b) {
    return a - b;
  });
  /* slice returns a shallow copy of a portion of an array
   and indicates (-2) extracts the last two elements in the sequence */
  const arrayValues = values.slice(values.length - 2);
  /* last two elements are the biggest integers in ascending order
   the one in [0] is the second biggest one */
  console.log(arrayValues[0]);
}
