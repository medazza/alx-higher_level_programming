#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let ind = 0; ind < list.length; ind++) {
    if (list[ind] === searchElement) {
	    count++;
    }
  }
	return count;
};
