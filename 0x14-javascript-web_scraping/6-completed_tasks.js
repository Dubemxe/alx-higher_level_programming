#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed_tasks = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed_tasks[task.userId] === undefined) {
          completed_tasks[task.userId] = 1;
        } else {
          completed_tasks[task.userId]++;
        }
      }
    }
    console.log(completed_tasks);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
