const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();

for (let i = 1; i < 10; i++) {
  console.log(`${parseInt(input)} * ${i} = ${parseInt(input) * i}`);
}
