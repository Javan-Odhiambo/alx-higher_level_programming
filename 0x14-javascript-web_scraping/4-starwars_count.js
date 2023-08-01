#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body).results;
  const films = [];
  data.map(film => films.push(...film.characters));
  const filtered = films.filter(el => el.endsWith('18/'));
  console.log(filtered.length);
});
