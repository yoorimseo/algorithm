const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();

let num = parseInt(input);
let i = 0;

while (num > 0) {
  let res = '';
  res = ' '.repeat(i) + '*'.repeat(num);
  i++;
  num--;
  console.log(res);
}
