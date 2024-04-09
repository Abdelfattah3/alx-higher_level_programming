#!/usr/bin/node
function add (a, b) {
  return a + b;
}
if (process.argv.length === 4) {
  const x = parseInt(process.argv[2]);
  const y = parseInt(process.argv[3]);
  const result = add(x, y);
  console.log(result);
} else { console.log('NaN'); }
