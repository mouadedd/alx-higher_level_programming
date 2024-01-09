#!/usr/bin/node
let theArg = 0;

exports.logMe = function (item) {
  console.log(theArg + ': ' + item);
  theArg++;
};
