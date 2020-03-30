var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db){
	if (err) throw err;
	var mydb = db.db("db1");
	mydb.createCollection("col1", function(err, res){
		if (err) throw err;
		console.log("Collection Created");
		db.close();
	});
});

// MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
// 	if (err) throw err;
// 	var mydb = db.db("db1");
// 	var obj1 = { name: "tyler", number: "7" };
// 	mydb.collection("col1").insertOne(obj1, function(err, res) {
// 		if (err) throw err;
// 		console.log("1 document inserted");
// 		db.close();
// 	});
// });

// MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
// 	if (err) throw err;
// 	var mydb = db.db("db1");
// 	mydb.collection("col1").findOne({}, function(err, result) {
// 		if (err) throw err;
// 		console.log(result);
// 		db.close();
// 	});
// });

// MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
// 	if (err) throw err;
// 	var mydb = db.db("db1");
// 	var arr = [{name: "a"},{name: "b"},{name: "d"},{name: "c"},{name: "f"},{name: "g"},{name: "e"},]
// 	mydb.collection("col1").insertMany(arr, function(err, result) {
// 		if (err) throw err;
// 		console.log("Inserted many");
// 		db.close(); 	
// 	});
// });

// MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
// 	if (err) throw err;
// 	var mydb = db.db("db1");
// 	var query = { name: 'tyler' };
// 	mydb.collection("col1").deleteOne(query, function(err, obj) {
// 	if (err) throw err;
// 		console.log("1 document deleted");
// 		db.close();
// 	});
// });

// MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
// 	if (err) throw err;
// 	var mydb = db.db("db1");
// 	var mySort = {name: 1};
// 	mydb.collection("col1").find({}).toArray(function(err, result) {
// 		if (err) throw err;
// 		console.log(result);
// 		db.close(); 	
// 	});
// 	// mydb.collection("col1").find({}).sort(mySort).toArray(function(err, result) {
// 	// 	if (err) throw err;
// 	// 	console.log(result);
// 	// 	db.close(); 	
// 	// });
// });

// MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
// 	if (err) throw err;
// 	var mydb = db.db("db1");
// 	mydb.collection("col1").drop(function(err, del) {
// 		if (err) throw err;
// 		if (del) console.log("Collection Dropped");
// 		db.close();
// 	});
// 	// mydb.dropCollection("col1", function(err, del){
// 	// 	if (err) throw err;
// 	// 	if (del) console.log("Collection Dropped");
// 	// 	db.close();
// 	// });
// });