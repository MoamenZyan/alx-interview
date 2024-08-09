#!/usr/bin/node

function doRequest (url) {
    const req = require('request');
    return new Promise((resolve, reject) => {
      req.get(url, (error, res, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body));
      });
    });
}
  

async function main () {
    const args = process.argv;

    if (args.length < 3) return;

    const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
    const movie = await doRequest(movieUrl);

    if (movie.characters === undefined) return;
    for (const characterUrl of movie.characters) {
      const character = await doRequest(characterUrl);
      console.log(character.name);
    }
}

  main();
