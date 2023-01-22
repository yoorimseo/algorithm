const fs = require('fs');

const [a, b, c] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

if (b >= c) {
  console.log(-1);
} else {
  console.log(Math.floor(a / (c - b) + 1));
}
