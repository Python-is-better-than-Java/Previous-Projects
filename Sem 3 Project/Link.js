const express = require('express');
var bodyparser = require('body-parser');
const app = express();
var MongoClient = require('mongodb').MongoClient;
var urlencodedparser = bodyparser.urlencoded({extended: false})

app.use(express.static('public'));
app.post("/user", urlencodedparser, function(req, res){
  play_score = {name: req.body.uname, score: req.body.uscore};
  MongoClient.connect("mongodb://127.0.0.1:27017", { useUnifiedTopology: true }, function (err, client) {
    if(err) throw err;
      console.log("DB is connected");
      const db = client.db('Scores');
      db.collection('scores').insertOne(play_score, function() {
        console.log("Successful");
        res.writeHead(200, { 'Content-type': 'application/json' });
        client.close();
        res.end();
      });
      db.collection('scores').find({}).toArray(function(err, docs){
        console.log(JSON.stringify(docs));
      })
    });
})
app.listen(3001, ()=>{
  console.log("Server is running on http://localhost:3001/Osu-Children.html")
});
