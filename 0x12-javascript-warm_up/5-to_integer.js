#!/usr/bin/node

const convertArg = Number(process.argv[2]);

if (typeof convertArg === 'number') {
  console.log(`My number: ${convertArg}`);
} else {
  console.log('Not a number');
}
