const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const maxNum = Math.max(...input);

console.log(maxNum);
console.log(input.indexOf(maxNum) + 1);
