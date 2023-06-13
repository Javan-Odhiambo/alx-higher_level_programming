#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;

  while (i < j) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j--;
    i++;
  }
  return list;
};
