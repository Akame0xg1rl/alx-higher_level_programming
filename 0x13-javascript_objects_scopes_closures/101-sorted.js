#!/usr/bin/node
const { dict } = require('./101-data');

const occurrenceDict = {};

Object.keys(dict).forEach(id => {
  const occurrences = dict[id];

  if (occurrenceDict[occurrences]) {
    occurrenceDict[occurrences].push(id);
  } else {
    occurrenceDict[occurrences] = [id];
  }
});

console.log(occurrenceDict);
