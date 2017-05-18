var express = require('express');
var bodyParser = require('body-parser');
var app = express();

app.use(bodyParser.json());

app.get('/getdata', function(req, res) {
	var fs = require('fs');
	
	var config = JSON.parse(fs.readFileSync('config.json', 'utf8'));
	res.json(config.modules);
});

app.post('/setdata', function(req, res) {
	var fs = require('fs');
	
	var config = JSON.parse(fs.readFileSync('config.json', 'utf8'));
	var modules = req.body.modules;
	config.modules = modules;
	fs.writeFileSync('config.json', JSON.stringify(config, null, 2));
	
	res.status(200).end();
});

app.listen(1080);