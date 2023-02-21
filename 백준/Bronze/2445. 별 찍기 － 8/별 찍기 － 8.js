const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim();
const num1 = parseInt(input);
let num2 = num1;
const answer = [];

for (let i = 0; i < num1; i++) {
  let str = '';
  str += '*'.repeat(num2) + ' '.repeat(2 * i) + '*'.repeat(num2);
  num2--;
  answer.push(str);
}

const arr = [...answer].reverse();
const res = [...arr.slice(0, arr.length - 1), ...answer];

console.log(res.join('\n'));
