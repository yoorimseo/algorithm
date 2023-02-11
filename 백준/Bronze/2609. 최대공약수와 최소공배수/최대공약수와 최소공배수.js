const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const [a, b] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(' ')
  .sort((a, b) => b - a);

function gcd(a, b) {
  let r = 0;
  while (b != 0) {
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}

const gcdNum = gcd(a, b);
console.log(gcdNum, (a * b) / gcdNum);
