#!/usr/bin/node
let secBigg = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort((a, b) => a - b);
  secBigg = args[args.length - 2];
}
console.log(secBigg);
