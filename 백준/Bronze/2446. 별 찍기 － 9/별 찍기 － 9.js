const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim();
const num = parseInt(input);
let cnt = num;
const star = [];

for (let i = 0; i < num; i++) {
  let str = '';
  cnt--;
  str += ' '.repeat(cnt) + '*'.repeat(2 * i + 1);
  star.push(str);
}

const answer = [...star.slice(1).reverse(), ...star];
console.log(answer.join('\n'));
