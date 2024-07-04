#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    do {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }

      console.log(row);
      this.height--;
    } while (this.height > 0);
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
