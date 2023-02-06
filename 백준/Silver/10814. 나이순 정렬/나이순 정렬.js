const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input.slice(1).map((i) => i.split(' '));
const obj = {};

for (let i in arr) {
  if (!obj[arr[i][0]]) {
    obj[arr[i][0]] = [arr[i][1]];
  } else {
    obj[arr[i][0]].push(arr[i][1]);
  }
}

for (let i in obj) {
  for (let j of obj[i]) {
    console.log(i, j);
  }
}
