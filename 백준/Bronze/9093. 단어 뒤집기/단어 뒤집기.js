const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const n = parseInt(input[0]);
const arr = input.slice(1).map((i) => i.split(' '));
const answer = [];

for (let i of arr) {
  let str = '';
  for (let j of i) {
    j = j.split('').reverse().join('');
    str += j + ' ';
  }
  answer.push(str.trim());
}

console.log(answer.join('\n'));
