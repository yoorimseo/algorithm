const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input
  .slice(1)
  .map(Number)
  .sort((a, b) => a - b);
const average = arr.reduce((acc, cur) => acc + cur, 0) / arr.length;
const midNum = arr[Math.floor(arr.length / 2)];
const obj = {};
const range = Math.max(...arr) - Math.min(...arr);

for (let i of arr) {
  if (!obj[i]) {
    obj[i] = 1;
  } else {
    obj[i] += 1;
  }
}

let max = 0;

for (let i in obj) {
  if (obj[i] > max) {
    max = obj[i];
  }
}

const arr2 = [];
let frequentNum = 0;

for (let i in obj) {
  if (obj[i] === max) {
    arr2.push(i);
  }
}

const res = arr2.map(Number).sort((a, b) => a - b);
arr2.length > 1 ? (frequentNum = res[1]) : (frequentNum = res[0]);

console.log(`${Math.round(average)}\n${midNum}\n${frequentNum}\n${range}`);
