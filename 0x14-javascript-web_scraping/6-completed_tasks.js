#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Oops! Something went wrong:', err);
  } else {
    const completedTasks = {};
    for (const task of body) {
      if (task.completed) {
        completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
      }
    }
    console.log(completedTasks);
  }
});
