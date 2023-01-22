const fs = require('fs');

const [a, b] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map((i) => parseInt(i));

console.log(a + b);
