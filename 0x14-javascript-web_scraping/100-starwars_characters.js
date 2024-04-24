#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
    console.error('Please provide a movie ID as an argument.');
    process.exit(1);
}
const movieId = process.argv[2];
const movieUrl = `https://swapi.co/api/films/${movieId}/`;
request(movieUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching movie data:', error);
        process.exit(1);
    }
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    charactersUrls.forEach((url, index) => {
        request(url, (error, response, body) => {
            if (error) {
                console.error(`Error fetching character data for character ${index + 1}:`, error);
            } else {
                const characterData = JSON.parse(body);
                console.log(characterData.name);
            }
        });
    });
});
