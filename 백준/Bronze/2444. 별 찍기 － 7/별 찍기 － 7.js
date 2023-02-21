const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim();
const num1 = parseInt(input);
let num2 = num1;
const answer = [];

for (let i = 0; i < num1; i++) {
  let str = '';
  num2--;
  str += ' '.repeat(num2) + '*'.repeat(2 * i + 1);
  answer.push(str);
}

const arr = answer.slice(0, answer.length - 1);

console.log(answer.join('\n'));
console.log(arr.reverse().join('\n'));
