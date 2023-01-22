const fs = require('fs');
const [n, m] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const prime = { 1: true };
const answer = [];

for (let i = 2; i <= Math.ceil(Math.sqrt(m)); i++) {
  if (prime[i]) {
    continue;
  }

  for (let j = i ** 2; j <= m; j += i) {
    prime[j] = true;
  }
}

for (let i = n; i <= m; i++) {
  !prime[i] && answer.push(i);
}

console.log(answer.join('\n'));
