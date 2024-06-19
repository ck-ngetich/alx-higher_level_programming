#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let m = 0; m < this.height; m++) {
      let z = '';
      for (let n = 0; n < this.width; n++) {
        z += 'X';
      }
      console.log(z);
    }
  }
}

module.exports = Rectangle;
