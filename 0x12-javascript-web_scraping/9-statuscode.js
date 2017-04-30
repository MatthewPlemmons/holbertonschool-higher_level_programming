#!/usr/bin/node
const https = require('https');
https.get(process.argv[2], (response) => {
  console.log('code:', response.statusCode);
});
