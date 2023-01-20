const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const arr = input.sort((a, b) => a - b);
const answer = [];

for (let i = 1; i < 31; i++) {
  if (!arr.includes(i)) {
    answer.push(i);
  }
}

console.log(answer.join('\n'));
