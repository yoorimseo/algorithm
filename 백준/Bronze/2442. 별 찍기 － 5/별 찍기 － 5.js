const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();
const num = parseInt(input);
let cnt = 1;
let i = num - 1;

while (i >= 0) {
  console.log(' '.repeat(i) + '*'.repeat(cnt));
  cnt += 2;
  i--;
}
