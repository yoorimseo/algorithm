const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input.slice(1);
const obj = {};

for (let i of arr) {
  if (!obj[i.length]) {
    obj[i.length] = [i];
  } else if (obj[i.length].includes(i)) {
    continue;
  } else {
    obj[i.length].push(i);
  }
}

for (let i in obj) {
  if (obj[i].length > 1) {
    obj[i].sort();
  }
  obj[i].map((str) => console.log(str));
}
