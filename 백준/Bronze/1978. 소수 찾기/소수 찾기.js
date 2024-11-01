const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);

const maxNum = Math.max(...arr);
const isPrime = new Array(maxNum + 1).fill(true);
isPrime[0] = false;
isPrime[1] = false;

for (let i = 2; i * i <= maxNum; i++) {
  if (isPrime[i]) {
    for (let j = i * i; j <= maxNum; j += i) {
      isPrime[j] = false;
    }
  }
}

let cnt = 0;
for (let num of arr) {
  if (isPrime[num]) {
    cnt++;
  }
}

console.log(cnt);