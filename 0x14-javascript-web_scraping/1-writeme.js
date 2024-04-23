#!/usr/bin/node
const fs = require('fs');
let file = process.argv[2];
let string = process.argv[3];
try {
  fs.writeFileSync(file, string, { encoding: 'utf8' });
} catch (err) {
  console.error(err);
}
