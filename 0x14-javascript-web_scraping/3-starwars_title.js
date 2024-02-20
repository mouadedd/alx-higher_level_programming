#!/usr/bin/node

const request = require('request');
const ep = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + ep;

request.get(url, (err, rep, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const episode = JSON.parse(body);
  console.log(episode.title);
});
