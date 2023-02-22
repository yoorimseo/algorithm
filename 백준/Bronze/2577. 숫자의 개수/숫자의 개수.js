const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n').map(Number);
const res = input.reduce((acc, cur) => acc * cur, 1);
const arr = String(res).split('').map(Number);
const answer = {};

for (let i of arr) {
  if (!answer[i]) {
    answer[i] = 1;
  } else {
    answer[i] += 1;
  }
}

for (let j = 0; j < 10; j++) {
  if (!answer[j]) {
    console.log(0);
  } else {
    console.log(answer[j]);
  }
}
