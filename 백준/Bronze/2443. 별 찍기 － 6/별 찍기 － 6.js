const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();
let num = parseInt(input);
let cnt = num - 1;
let i = 0;

while (i < parseInt(input)) {
  console.log(' '.repeat(i) + '*'.repeat(num) + '*'.repeat(cnt));
  cnt--;
  num--;
  i++;
}
