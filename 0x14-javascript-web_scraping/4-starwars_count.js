#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response && response.statusCode !== 200) {
    console.error('status code:', response.statusCode);
    return;
  }
  const filmsData = JSON.parse(body);
  let wedgeMovies = 0;
  filmsData.results.forEach(film => {
    for (const p of film.characters) { if (p.includes(characterId)) wedgeMovies++; }
  });
  console.log(wedgeMovies);
});
