#!/usr/bin/node
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n) || parseInt(n, 10) !== n) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    // Recursive case: n * factorial(n-1)
    return n * factorial(n - 1);
  }
}

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

console.log(factorial(num));
