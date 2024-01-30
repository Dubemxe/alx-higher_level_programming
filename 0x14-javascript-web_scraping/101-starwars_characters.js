#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, res, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printChars (characters, index) {
  req(characters[index], function (error, res, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
