const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const divisor = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

if (divisor.length > 1) {
  console.log(divisor[0] * divisor.at(-1));
} else {
  console.log(divisor[0] * divisor[0]);
}
