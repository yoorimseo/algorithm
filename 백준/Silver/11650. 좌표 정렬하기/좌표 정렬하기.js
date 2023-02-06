const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

let arr = input.slice(1).map((i) => i.split(' ').map(Number));
let answer = '';

arr.sort((a, b) => {
  if (a[0] !== b[0]) return a[0] - b[0];
  return a[1] - b[1];
});
arr.forEach((i) => {
  answer += `${i[0]} ${i[1]}\n`;
});

console.log(answer);