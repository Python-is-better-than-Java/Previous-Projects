var express = require('express');
var app = express();
var bodyparser = require('body-parser');
var MongoClient = require("mongodb").MongoClient;
var urlencodedparser = bodyparser.urlencoded({extended: false})
app.use(express.static('public'));
app.post("/end", urlencodedparser, function(req, res){
    response = {
        name: req.body.uname,
        score: req.body.uscore};
    MongoClient.connect("mongodb://127.0.0.1:27017", {useUnifiedTopology: true}, function(err, client){
        if(err) throw err
        const db = client.db("Project");
        db.collection('Hinode').insertOne(response, function(err, objs){
            res.send("Save Successful!!!")
        });
    });
})
app.listen(3000, ()=>console.log("Server is running on http://localhost:3000/hinode.html"));