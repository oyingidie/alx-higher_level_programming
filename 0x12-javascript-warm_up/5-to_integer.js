#!/usr/bin/node

const convertArg = Number(process.argv[2]);

if (isNaN(convertArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertArg}`);
}
