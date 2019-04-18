var express=require('express')
var admin=require('firebase-admin')
var url = require('url');
var path = require('path');
var sql = require('mysql');
var exec = require("child_process").exec;
var bodyParser = require('body-parser')
const app1=express()
app1.use(bodyParser.urlencoded({ extended: false }))
app1.use(bodyParser.json())
app1.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

var port = process.env.PORT || 9000;
app1.listen(port,()=>{
    console.log("Server Active At "+port);  
})