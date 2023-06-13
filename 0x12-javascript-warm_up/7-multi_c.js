#!/usr/bin/node

const count = Number(process.argv[2]) || console.log('Missing number of occurences');
for (let i = 0; i < count; i++) {
  console.log('C is fun');
}
