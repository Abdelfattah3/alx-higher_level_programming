#!/usr/bin/node
const args = process.argv[2];
if (!isNaN(parseInt(args))) {
  const i = parseInt(args);
  let x = 1;
  for (x = 1; x <= i; x++) { console.log('C is fun'); }
} else { console.log('Missing number of occurrences'); }
