#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '/18/';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movies = JSON.parse(body).results;
  let count = 0;

  movies.forEach(movie => {
    const characters = movie.characters;
    if (characters && characters.includes('https://swapi-api.alx-tools.com/api/people' + id)) {
      count++;
    }
  });
  console.log(count);
});
