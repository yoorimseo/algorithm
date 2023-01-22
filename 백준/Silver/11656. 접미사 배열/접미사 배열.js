const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();
const answer = [];

for (let i = 0; i < input.length; i++) {
  let str = input;
  answer.push(str.slice(i));
}

console.log(answer.sort().join('\n'));