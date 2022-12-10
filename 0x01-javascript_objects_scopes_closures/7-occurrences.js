#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (occurance) {
    if (occurance === searchElement) {
      count++;
    }
  });
  return count;
};
