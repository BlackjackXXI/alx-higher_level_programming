#!/usr/bin/node
const request = require('request');
const lien = process.argv[2];

request(lien, (err, res) => {
  if (err) console.log(err);
  console.log('code:', res.statusCode);
});
