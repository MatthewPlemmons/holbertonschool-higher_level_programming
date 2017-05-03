#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/people/18';
request(url, (error, response, body) => {
  if (error) return console.log(error);
  const res = JSON.parse(body);
  console.log(res.films.length);
});
