#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; arg > i; ++i) {
      console.log('X'.repeat(arg));
  }
}
