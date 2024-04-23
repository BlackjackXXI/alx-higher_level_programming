#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Oops! Something went wrong:', error);
  } else {
    const movieData = JSON.parse(body);
    console.log('The title of the movie is:', movieData.title);
  }
});