#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstInteger = Number(process.argv[2]);
const secondInteger = Number(process.argv[3]);

const sumIntegers = add(firstInteger, secondInteger);
console.log(sumIntegers);
