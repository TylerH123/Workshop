var http = require('http');
var mod = require("./module.js")

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end(mod.helloWorld());
}).listen(5000);