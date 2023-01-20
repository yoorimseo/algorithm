const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const num = parseInt(input[0]);

for (let i = 1; i <= num; i++) {
  const testcase = input[i].split(' ').map(Number);
  const studentNum = testcase[0];

  const sum = testcase.slice(1).reduce((acc, cur) => acc + cur, 0);
  const average = sum / studentNum;
  let cnt = 0;

  for (let j of testcase.slice(1)) {
    if (j > average) {
      cnt++;
    }
  }

  console.log(((cnt / studentNum) * 100).toFixed(3) + '%');
}
