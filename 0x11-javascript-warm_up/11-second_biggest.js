#!/usr/bin/node
// Return second largest of input integers.
function sortNumber (a, b) {
  return (a - b);
}
if (process.argv.length < 4) {
  console.log(0);
} else {
  let n = process.argv.slice(2);
  n.sort(sortNumber);
  console.log(n[n.length - 2]);
}
