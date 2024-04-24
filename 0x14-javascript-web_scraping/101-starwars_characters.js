#!/usr/bin/node

const request = require('request');
const util = require('util');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const prequest = util.promisify(request);

(async () => {
  try {
    const filmData = (await prequest(apiUrl, { json: true })).body;
    for (const characterUrl of filmData.characters) {
      const characterData = (await prequest(characterUrl, { json: true })).body;
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
})();
