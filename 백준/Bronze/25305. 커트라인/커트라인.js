const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [total, num] = input[0].split(' ');
const score = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => b - a);

console.log(score[num - 1]);
