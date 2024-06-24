#!/usr/bin/node

let size = Number(process.argv[2]);
const length = size;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  do {
    let line = '';
    for (let i = 0; i > length; i++) {
      line += 'X';
    }

    console.log(line);
    size--;
  } while (size > 0);
}
