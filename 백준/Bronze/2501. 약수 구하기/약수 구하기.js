const fs = require("fs");
const [N, K] = fs.readFileSync("dev/stdin").toString().split(" ").map(Number);
const arr = [];

for (let i = 1; i < N + 1; i++) {
  if (N % i === 0) {
    arr.push(i);
  }
}

console.log(arr[K - 1] ? arr[K - 1] : 0);
