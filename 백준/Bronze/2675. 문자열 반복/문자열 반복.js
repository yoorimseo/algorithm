const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const num = parseInt(input[0]);

for (let i = 1; i <= num; i++) {
  const arr = input[i].split(' ');
  const repeatNum = parseInt(arr[0]);
  const strArr = arr[1].split('');
  let answer = '';

  for (let j of strArr) {
    answer += j.repeat(repeatNum);
  }

  console.log(answer);
}
