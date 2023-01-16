const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const num1 = parseInt(input[0]);
const num2 = input[1]
  .split('')
  .map((i) => parseInt(i))
  .reverse();
const answer = [];

for (let i = 0; i < 3; i++) {
  let res = num1 * num2[i];
  answer.push(res * Math.pow(10, i));
  console.log(res);
}

console.log(answer.reduce((acc, cur) => acc + cur, 0));
