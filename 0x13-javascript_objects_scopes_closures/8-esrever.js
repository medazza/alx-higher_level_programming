#!/usr/bin/node

exports.esrever = function (list) {
  const nwList = [];
  for (let ind = list.length - 1; ind >= 0; ind--) {
    nwList.push(list[ind]);
  }
  return nwList;
};
