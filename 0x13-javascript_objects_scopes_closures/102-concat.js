#!/usr/bin/node

const fs = require('fs');
const firstSourceFile = fs.readFileSync(process.argv[2], 'utf8');
const secondSourceFile = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], firstSourceFile + secondSourceFile);
