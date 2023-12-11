#!/usr/bin/node
//This script prints the first argument passed to it.

let args = process.argv.slice(2);
let firstArg = args[0];
if (firstArg === undefined) {
	console.log("No argument");
}
else {
	console.log(firstArg);
}
