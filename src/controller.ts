var express=require('express')
var admin=require('firebase-admin')
var url = require('url');
var path = require('path');
var sql = require('mysql');
import {PythonShell} from 'python-shell';
var exec = require("child_process").exec;
var bodyParser = require('body-parser')
const app=express()
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});
app.get('/input', (req, res) => {
    res.setHeader('content-type', 'text/html');
    res.sendFile(__dirname + '/input.html');
});
app.post('/getResult',(req,res,next)=>{
    console.log(req.query.text)
    var dataString=""
   
    try{
        let option={
            mode: 'text',
            scriptPath: './',
            args: [req.query.text]
        }
        PythonShell.run(`scripty.py`,option,function(err,result){
            if (err) throw err;
            console.log(result)
            res.send(result)
        })
    }catch(e){
        console.log(e)
    }
    
    // child.stdout.on('data', function(data){
    //     console.log(data)
    //     dataString += data.toString();
    //   });
    //   child.stdout.on('end', function(){
    //     console.log('result=',dataString);
    //     res.send(dataString)
    //   })
    //   child.stdin.end();
})
var port = process.env.PORT || 8000;
app.listen(port,()=>{
    console.log("Server Active At "+port);  
})
