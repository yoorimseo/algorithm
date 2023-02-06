const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim();
const num = parseInt(input);
const arr = [];
let answer = 0;

for (let i = 0; i < num + 1; i++) {
  if (i === 0 || i === 1) {
    arr.push(i);
    answer += i;
  } else {
    answer = arr[i - 2] + arr[i - 1];
    arr.push(answer);
  }
}
console.log(answer);
