#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) return console.log(error);
  const res = JSON.parse(body);
  let dict = {};
  for (const n of res) {
    if (n.completed === true) {
      if (!dict[n.userId]) {
        dict[n.userId] = 0;
      }
      dict[n.userId] += 1;
    }
  }
  console.log(dict);
});
