const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();
let num = parseInt(input);

while (num > 0) {
  console.log('*'.repeat(num));
  num--;
}
