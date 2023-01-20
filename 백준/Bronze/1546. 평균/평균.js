const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const num = parseInt(input[0]);
const scores = input[1].split(' ').map(Number);
const maxScore = Math.max(...scores);
let result = scores.reduce((acc, cur) => acc + (cur / maxScore) * 100, 0);

console.log(result / num);
