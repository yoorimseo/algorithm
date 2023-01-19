const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();

let num = parseInt(input);
let newNum = 0;
let cnt = 0;

while (parseInt(input) !== newNum) {
  const x = Math.floor(num / 10);
  const y = num % 10;
  const z = (x + y) % 10;

  newNum = y * 10 + z;
  num = newNum;

  cnt++;
}

num === 0 ? console.log(1) : console.log(cnt);
