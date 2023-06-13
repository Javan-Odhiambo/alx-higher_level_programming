#!/usr/bin/node

const count = (Number(process.argv[2]) || console.log('Missing size'));

for (let i = 0; i < count; i++) {
  console.log('X'.repeat(count));
}
