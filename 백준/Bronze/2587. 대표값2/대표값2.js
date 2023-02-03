const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = [...input].map(Number).sort((a, b) => a - b);
const average = arr.reduce((acc, cur) => acc + cur, 0) / arr.length;
const midNum = arr[Math.floor(arr.length / 2)];

console.log(`${average}\n${midNum}`);
