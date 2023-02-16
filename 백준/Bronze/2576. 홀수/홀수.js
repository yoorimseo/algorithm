const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const answer = input.map(Number).filter((i) => i % 2 !== 0);

answer.reduce((acc, cur) => acc + cur, 0) === 0
  ? console.log(-1)
  : console.log(`${answer.reduce((acc, cur) => acc + cur, 0)}\n${Math.min(...answer)}`);
