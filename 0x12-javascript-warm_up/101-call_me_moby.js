#!/usr/bin/node

exports.callMeMoby = function (count, func) {
  for (let i = 0; i < count; i++) {
    func();
  }
}
