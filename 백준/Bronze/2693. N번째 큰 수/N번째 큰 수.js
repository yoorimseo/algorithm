const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().split("\n");

const T = Number(input[0]);

for (let i = 1; i < T + 1; i++) {
  const arr = input[i]
    .split(" ")
    .map(Number)
    .sort((a, b) => b - a);
    
  console.log(arr[2]);
}
