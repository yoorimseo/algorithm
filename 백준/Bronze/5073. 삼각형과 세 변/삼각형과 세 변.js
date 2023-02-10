const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const arr = input.slice(0, input.length - 1);
const answer = [];

for (let i of arr) {
  const obj = {};
  const line = i.split(' ').map(Number);
  const max = Math.max(...line);
  const sum = line.reduce((acc, cur) => acc + cur, 0) - max;

  if (max >= sum) {
    answer.push('Invalid');
  } else {
    for (let j of line) {
      if (!obj[j]) {
        obj[j] = 1;
      } else {
        obj[j] += 1;
      }
    }

    if (Object.keys(obj).length === 1) {
      answer.push('Equilateral');
    } else if (Object.keys(obj).length === 2) {
      answer.push('Isosceles');
    } else {
      answer.push('Scalene');
    }
  }
}

console.log(answer.join('\n'));
