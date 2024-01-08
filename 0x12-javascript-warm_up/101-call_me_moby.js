#!/usr/bin/node
module.exports = {
  callMeMoby: function (x, theFunction) {
    for (let ind = 0; ind < x; ind++) {
      theFunction();
    }
  }
};
