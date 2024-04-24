#!/usr/bin/node

let url = process.argv[2];
let filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error('Oops! Something went wrong:', err);
  } else {
    fs.writeFile(filename, body, 'utf8', function(err) {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log('File successfully saved as:', filename);
      }
    });
  }
});
