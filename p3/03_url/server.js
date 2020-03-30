var http = require('http');
var fs = require("fs");
var url = require("url");

http.createServer(function (req, res) {
	var q = url.parse(req.url, true);
	console.log(q);
	//console.log(q);
	switch (q.pathname){ 
		case "/":
			fs.readFile("./index.html", function(err, data) {
				if (err) {  
                    res.writeHead(404);  
                    res.write(err);  
                    res.end();  
                }
				res.writeHead(200, {'Content-Type': 'text/html'});
				res.write(data);
				res.end();
			});
			break;
		case "/apple":
			fs.readFile("./apple.html", function(err, data) {
				if (err) {
					res.writeHead(404, {'Content-Type': 'text/html'});
					res.write(err);  
                    res.end();  
				} 
				res.writeHead(200, {'Content-Type': 'text/html'});
				res.write(data);
				res.end();
			});
			break;
		case "/orange":
			fs.readFile("./orange.html", function(err, data) {
				if (err) {
					res.writeHead(404, {'Content-Type': 'text/html'});
					res.write(err);  
                    res.end();
				} 
				res.writeHead(200, {'Content-Type': 'text/html'});
				res.write(data);
				res.end();
			});
			break;
		default:
			res.writeHead(404);  
            res.write("opps this doesn't exist - 404");  
            res.end();  
            break;
	}
}).listen(5000);