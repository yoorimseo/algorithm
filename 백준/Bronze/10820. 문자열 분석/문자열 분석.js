const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

for (let i of input) {
  if (i === '') {
    continue;
  }
  const strArr = i.split('');
  let [lower, upper, num, blank] = [0, 0, 0, 0];
  for (let j of strArr) {
    if (j === ' ') {
      blank++;
    } else if (Number.isInteger(+j)) {
      num++;
    } else if (/^[a-z]/g.test(j)) {
      lower++;
    } else if (/^[A-Z]/g.test(j)) {
      upper++;
    }
  }
  console.log(lower, upper, num, blank);
}
