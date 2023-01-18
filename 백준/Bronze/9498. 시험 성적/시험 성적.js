const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();

if (0 <= input && input < 60) {
  console.log('F');
} else if (60 <= input && input < 70) {
  console.log('D');
} else if (70 <= input && input < 80) {
  console.log('C');
} else if (80 <= input && input < 90) {
  console.log('B');
} else {
  console.log('A');
}
