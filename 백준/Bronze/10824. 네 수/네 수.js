const fs = require('fs');

const [a, b, c, d] = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const res1 = parseInt(a + b);
const res2 = parseInt(c + d);

console.log(res1 + res2);
