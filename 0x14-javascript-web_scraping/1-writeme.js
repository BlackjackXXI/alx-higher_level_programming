#!/usr/bin/node
let strng = process.argv[3];
const fs = require('fs');
const file1 = process.argv[2];

try {
  fs.writeFileSync(file1, strng, { encoding: 'utf8' });
} catch (err) {
  console.error(err);
}
