const fs = require('fs');

const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map((item) => parseInt(item));

const chess = [1, 1, 2, 2, 2, 8];
const answer = [];
for (let i in chess) {
  answer[i] = chess[i] - input[i];
}

console.log(answer.join(' '));
