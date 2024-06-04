#!/usr/bin/node
const args = process.argv[2];
if (!isNaN(parseInt(args))) {
  const i = parseInt(args);
  let x = 1;
  let j = 1;
  for (x = 1; x <= i; x++) {
    for (j = 1; j <= i; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else { console.log('Missing size'); }
