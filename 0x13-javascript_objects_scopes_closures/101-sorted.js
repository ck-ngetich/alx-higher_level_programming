#!/usr/bin/node
const dict = require('./101-data').dict;

const myList = Object.entries(dict);
const value = Object.values(dict);
const newValue = [...new Set(value)];
const newDict = {};
for (const x in newValue) {
  const arr = [];
  for (const y in myList) {
    if (myList[y][1] === newValue[x]) {
      arr.unshift(myList[y][0]);
    }
  }
  newDict[newValue[x]] = arr;
}
console.log(newDict);
