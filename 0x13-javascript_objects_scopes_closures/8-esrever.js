#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length; i >= 1; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
