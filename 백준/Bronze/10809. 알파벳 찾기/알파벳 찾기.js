const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();

const Alphabet = new Array(26).fill().map((_, i) => String.fromCharCode(i + 97));

Alphabet.map((s) => console.log(input.indexOf(s)));
