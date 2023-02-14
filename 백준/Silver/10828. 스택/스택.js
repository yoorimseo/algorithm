const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const orderArr = input.slice(1).map((i) => i.split(' '));
const arr = [];
let answer = [];

for (let i of orderArr) {
  let order = i[0];

  switch (order) {
    case 'push':
      arr.unshift(parseInt(i[1]));
      break;
    case 'pop':
      arr.length > 0 ? answer.push(arr.shift()) : answer.push(-1);
      break;
    case 'size':
      answer.push(arr.length);
      break;
    case 'empty':
      arr.length > 0 ? answer.push(0) : answer.push(1);
      break;
    case 'top':
      arr.length > 0 ? answer.push(arr[0]) : answer.push(-1);
  }
}

console.log(answer.join('\n'));
