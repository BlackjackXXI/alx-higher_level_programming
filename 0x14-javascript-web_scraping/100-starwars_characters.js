#!/usr/bin/node
const request = require('request');
let movieUrl = 'https://swapi.co/api/films/' + process.argv[2];

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let charsUrl = JSON.parse(body)['characters'];
    for (let chars of charsUrl) {
      request(chars, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          let charBod = JSON.parse(body)['name'];
          console.log(charBod);
        }
      });
    }
  }
});