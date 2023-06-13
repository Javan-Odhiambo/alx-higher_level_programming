#!/usr/bin/node

console.log('My number:', (Number(process.argv[2]) | 0 || 'Not a number'));
