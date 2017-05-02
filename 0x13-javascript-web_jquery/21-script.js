#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/people/5/?format=json';
request(url, (error, response, body) => {
  if (error) return console.log(error);
  $('DIV#character').text(JSON.parse(body).name);
});
