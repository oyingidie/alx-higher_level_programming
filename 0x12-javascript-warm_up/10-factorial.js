#!/usr/bin/node

function factorial (i) {
  if (i === 0 || isNaN(i)) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}

const argumentPassed = Number(process.argv[2]);
console.log(factorial(argumentPassed));
