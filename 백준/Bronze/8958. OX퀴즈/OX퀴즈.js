const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const line = parseInt(input[0]);
const answer = [];

for (let i = 1; i <= line; i++) {
  let sum = 0;
  let cnt = 0;

  for (let j of input[i]) {
    if (j === 'O') {
      cnt++;
    } else {
      cnt = 0;
    }
    sum += cnt;
  }
  answer.push(sum);
}

console.log(answer.join('\n'));
