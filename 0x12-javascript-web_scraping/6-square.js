#!/usr/bin/node
const Square = require('./5-square').Square;
Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    this.print();
  } else {
    for (let i = 0; this.height > i; ++i) {
      console.log(c.repeat(this.width));
    }
  }
};
exports.Square = Square;
