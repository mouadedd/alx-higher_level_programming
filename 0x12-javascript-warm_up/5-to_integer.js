#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  // used the ! instead of isnan but it miss the case when the argement is not a number
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
