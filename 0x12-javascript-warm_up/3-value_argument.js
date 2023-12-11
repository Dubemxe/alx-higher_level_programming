#!/usr/bin/node
let args = process.argv.slice(2);
let firstArg = args[0];
if (firstArg === undefined) {
	console.log("No argument");
}
else {
	console.log(firstArg);
}
