#!/usr/bin/node
function factorial (a) {
  if (a > 0) {
    return(a * factorial(--a));
  } else {
    return(1);
  }
}
let n = parseInt(process.argv[2]);
console.log(factorial(n));
