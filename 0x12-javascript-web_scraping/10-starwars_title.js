#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) return console.log(error);
  const res = JSON.parse(body);
  console.log(res.title);
});
