const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, x] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
const answer = [];

for (let i of arr) {
  if (i < x) {
    answer.push(i);
  }
}

console.log(answer.join(' '));
