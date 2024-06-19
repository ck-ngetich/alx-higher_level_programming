#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let n = '';
      for (let y = 0; y < this.width; y++) {
        n += c;
      }
      console.log(n);
    }
  }
}

module.exports = Square;
