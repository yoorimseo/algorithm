const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [hour, min] = input[0].split(' ').map(Number);
let cook = Number(input[1]);

min += cook;

if (min >= 60) {
  hour += Math.floor(min / 60);
  min = min % 60;
}

if (hour >= 24) {
  hour -= 24;
}

console.log(hour, min);
