const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');

if (input[0] > 0) {
  if (input[1] > 0) {
    console.log(1);
  } else {
    console.log(4);
  }
} else {
  if (input[1] > 0) {
    console.log(2);
  } else {
    console.log(3);
  }
}
