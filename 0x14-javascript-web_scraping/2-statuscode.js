#!/usr/bin/node

const lien = process.argv[2];
const request = require('request');

request(lien, (err, res) => {
  if (err) console.log(err);
  console.log('code:', res.statusCode);
});
