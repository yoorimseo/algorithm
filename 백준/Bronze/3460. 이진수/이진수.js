const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().split("\n").map(Number);

const T = input[0];

for (let i = 1; i < T + 1; i++) {
  let bin = input[i].toString(2).split("").reverse().join("");
  const res = [];

  for (let j = 0; j < bin.length; j++) {
    bin[j] === "1" ? res.push(j) : null;
  }

  console.log(res.join(" "));
}
