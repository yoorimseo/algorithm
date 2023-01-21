const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('');

const dial = {
  3: ['A', 'B', 'C'],
  4: ['D', 'E', 'F'],
  5: ['G', 'H', 'I'],
  6: ['J', 'K', 'L'],
  7: ['M', 'N', 'O'],
  8: ['P', 'Q', 'R', 'S'],
  9: ['T', 'U', 'V'],
  10: ['W', 'X', 'Y', 'Z'],
};
let time = 0;

for (let i of input) {
  time += parseInt(Object.keys(dial).find((key) => dial[key].includes(i)));
}

console.log(time);
