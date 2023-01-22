const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input[1].split(' ').map(Number);
let cnt = 0;

for (let i of arr) {
  const res = [];
  for (let j = 1; j <= i; j++) {
    if (i % j === 0) {
      res.push(j);
    }
  }

  if (res.length === 2 && res.includes(i) && res.includes(1)) {
    cnt++;
  }
}

console.log(cnt);
