#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const n = Number(process.argv[2]);
  let x = 0;
  while (x < n) {
    console.log('X'.repeat(n));
    x++;
  }
}
