#!/usr/bin/node

const squareZero = require('./5-square.js');

module.exports = class Square extends squareZero {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
