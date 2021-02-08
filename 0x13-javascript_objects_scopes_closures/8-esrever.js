#!/usr/bin/node
exports.esrever = function (list) {
  const retro = [];
  for (let i = list.length - 1; i > 0; i--) {
    retro.push(list[i]);
  }
  return retro;
};
