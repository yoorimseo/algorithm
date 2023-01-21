const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

input.includes('') ? console.log(0) : console.log(input.length);
