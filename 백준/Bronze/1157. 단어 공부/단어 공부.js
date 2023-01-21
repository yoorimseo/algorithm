const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();
const arr = input.toLocaleLowerCase();
const obj = {};

for (let i of arr) {
  if (obj[i] === undefined) {
    obj[i] = 1;
  } else {
    obj[i] += 1;
  }
}

const max = Math.max(...Object.values(obj));
let answer = '';

for (let j in obj) {
  if (obj[j] === max) {
    answer += j;
  }
}

answer.length === 1 ? console.log(answer.toUpperCase()) : console.log('?');
