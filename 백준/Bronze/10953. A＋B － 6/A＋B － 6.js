const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const line = parseInt(input[0]);

for (let i = 1; i <= line; i++) {
  const [a, b] = input[i].split(',').map(Number);
  console.log(a + b);
}
