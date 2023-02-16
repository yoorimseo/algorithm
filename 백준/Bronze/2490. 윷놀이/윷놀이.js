const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const arr = input.map((i) => i.split(' '));
const answer = [];

for (let i of arr) {
  const res = i.map(Number).reduce((acc, cur) => acc + cur, 0);

  switch (res) {
    case 3:
      answer.push('A');
      break;
    case 2:
      answer.push('B');
      break;
    case 1:
      answer.push('C');
      break;
    case 0:
      answer.push('D');
      break;
    case 4:
      answer.push('E');
      break;
  }
}

console.log(answer.join('\n'));
