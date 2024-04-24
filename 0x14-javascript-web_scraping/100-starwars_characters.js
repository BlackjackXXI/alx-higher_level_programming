#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi.co/api/films/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
