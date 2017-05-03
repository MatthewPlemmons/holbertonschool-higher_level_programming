#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w < 1 || h < 1 || w === undefined || h === undefined) {
  } else {
    this.width = w;
    this.height = h;
    this.print = function () {
      for (let i = 0; h > i; ++i) {
        console.log('X'.repeat(w));
      }
    };
  }
};
