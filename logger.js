
const EventEmitter = require('events');

var url = 'http://mylogger.io/log'

class Logger extends EventEmitter {
  log(message) {
    //Send an HTTP request
    console.log(message);
    //Raise an event
    this.emit('messageLogged', {id: 1, ulr: 'http://'});
  }
}

module.exports = Logger;
// var logger = module.exports.log = log;
