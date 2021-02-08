#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // a - accumulator, v - current value, ternary operator ? if true, else :
  const counter = list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0);
  return counter;
};
