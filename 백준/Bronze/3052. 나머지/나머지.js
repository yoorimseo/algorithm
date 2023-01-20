const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const arr = [];

for (let i of input) {
  arr.push(i % 42);
}

const setArr = new Set(arr);
const newArr = [...setArr];

console.log(newArr.length);
