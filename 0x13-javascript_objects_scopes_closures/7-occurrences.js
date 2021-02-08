#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const counter = list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0);
  return counter;
};
