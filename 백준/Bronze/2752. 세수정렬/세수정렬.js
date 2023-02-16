const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ');
const arr = input.map(Number).sort((a, b) => a - b);

console.log(arr.join(' '));
