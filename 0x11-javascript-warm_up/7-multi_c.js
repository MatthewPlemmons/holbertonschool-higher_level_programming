#!/usr/bin/node
let arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  while (arg) {
    console.log('C is fun');
    --arg;
  }
}
