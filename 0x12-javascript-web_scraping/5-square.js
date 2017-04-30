#!/usr/bin/node
const Rectangle = require('./4-rectangle').Rectangle;
exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
  Square.prototype = Object.create(Rectangle.prototype);
  Square.prototype.constructor = Square;
}
