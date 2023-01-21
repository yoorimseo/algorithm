const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const arr = [];

for (let i of input) {
  arr.push(i.split('').reverse().join(''));
}
console.log(Math.max(...arr));
