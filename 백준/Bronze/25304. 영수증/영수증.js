const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const total = parseInt(input[0]);
const num = input[1];
let testTotal = 0;

for (let i = 0; i < num; i++) {
  const test = input[i + 2].split(' ').map(Number);
  testTotal += test[0] * test[1];
}

total === testTotal ? console.log('Yes') : console.log('No');
