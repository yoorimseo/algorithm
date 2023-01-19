const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const testcase = input[1].split(' ').map(Number);
const findNum = parseInt(input[2]);
let cnt = 0;

for (let i of testcase) {
  if (i === findNum) cnt++;
}

console.log(cnt);
